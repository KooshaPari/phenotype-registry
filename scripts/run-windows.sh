#!/usr/bin/env bash
# run-windows.sh — Run the scraper on Windows (via Tailscale SSH) only.
# Use this when the Mac pass has already been run and you just want to
# pull the Windows data.
#
# Usage:
#   bash scripts/run-windows.sh
#   bash scripts/run-windows.sh --incremental
set -euo pipefail

REG="${REG:-$(cd "$(dirname "$0")/.." && pwd)}"
DEVICE_HOST="${DEVICE_HOST:-kooshapari-desk}"
DEVICE_USER="${DEVICE_USER:-koosh}"
DEVICE_REMOTE_DIR="${DEVICE_REMOTE_DIR:-/c/Users/koosh/scrape-windows}"

INCREMENTAL=""
if [[ "${1:-}" == "--incremental" ]]; then
    INCREMENTAL="--incremental"
fi

echo "=== Windows-only scraper pass ==="
echo "  registry root : $REG"
echo "  windows host  : $DEVICE_USER@$DEVICE_HOST"
echo "  windows dir   : $DEVICE_REMOTE_DIR"
echo "  incremental   : ${INCREMENTAL:-no}"
echo

RSYNC_TARGET="$DEVICE_USER@$DEVICE_HOST:$DEVICE_REMOTE_DIR"
echo "  preparing $RSYNC_TARGET"
# Use a path that survives the OpenSSH server's C: drive root normalization.
# The Windows OpenSSH server maps `/c/Users/...` to `C:\c\Users\...` (literal "c" subfolder),
# which is NOT what we want. We want a path under `C:\Users\...`.
# Use a bare relative-looking path so scp doesn't prepend C:\.
WIN_DIR='Users\\koosh\\scrape-windows'
ssh -o BatchMode=yes -o ConnectTimeout=15 "$DEVICE_USER@$DEVICE_HOST" "cmd.exe /c if not exist C:\\Users\\koosh\\scrape-windows\\scripts mkdir C:\\Users\\koosh\\scrape-windows\\scripts"
# Copy via a unique subdir name to dodge the /c/→C:\c\ translation.
ssh -o BatchMode=yes -o ConnectTimeout=15 "$DEVICE_USER@$DEVICE_HOST" "cmd.exe /c if not exist C:\\Users\\koosh\\scrape-windows\\stage mkdir C:\\Users\\koosh\\scrape-windows\\stage"
scp "$REG/scripts/scrape.py" "$DEVICE_USER@$DEVICE_HOST:C:/Users/koosh/scrape-windows/stage/scrape.py"

echo "  running scrape on Windows (this can take 5-15 minutes)..."
# PowerShell doesn't accept && — use ; instead.
# Or invoke via cmd.exe /c for shell-neutral behaviour.
WIN_SCRAPE_DIR="C:/Users/koosh/scrape-windows"
SCRAPE_CMD="cd /d ${WIN_SCRAPE_DIR}\\stage ^&^& python scrape.py --device win --out . ${INCREMENTAL}"
ssh -o BatchMode=yes -o ConnectTimeout=15 "$DEVICE_USER@$DEVICE_HOST" "cmd.exe /c \"$SCRAPE_CMD\"" || {
    echo "  WARNING: Windows scrape failed (cmd); retrying with powershell ; separator."
    ssh -o BatchMode=yes -o ConnectTimeout=15 "$DEVICE_USER@$DEVICE_HOST" "powershell -NoProfile -Command \"cd C:\\Users\\koosh\\scrape-windows\\stage ; python scrape.py --device win --out . ${INCREMENTAL}\"" || {
        echo "  WARNING: Windows scrape failed (powershell); continuing."
    }
}

echo "  pulling _curated.jsonl back to $REG"
scp "$DEVICE_USER@$DEVICE_HOST:C:/Users/koosh/scrape-windows/stage/_curated.jsonl" "$REG/_curated.win.jsonl" 2>/dev/null || true
scp "$DEVICE_USER@$DEVICE_HOST:C:/Users/koosh/scrape-windows/stage/_bindings.json" "$REG/_bindings.win.json" 2>/dev/null || true
scp "$DEVICE_USER@$DEVICE_HOST:C:/Users/koosh/scrape-windows/stage/_seen.txt" "$REG/_seen.win.txt" 2>/dev/null || true

# Merge Windows curated into the cumulative Mac+Win _curated.jsonl.
# The Win records use an "origin" tag we keep; we de-dupe on the hash id.
echo
echo "--- Merging Mac+Win curated (de-duped by id) ---"
python3 - <<'PY'
import json
seen = set()
out = []
for src in ['_curated.jsonl', '_curated.win.jsonl']:
    for line in open(src, encoding='utf-8', errors='replace'):
        line = line.strip()
        if not line:
            continue
        try:
            o = json.loads(line)
        except Exception:
            continue
        oid = o.get('id') or o.get('_id')
        if not oid or oid in seen:
            continue
        seen.add(oid)
        out.append(o)
with open('_curated.jsonl', 'w', encoding='utf-8') as f:
    for o in out:
        f.write(json.dumps(o) + '\n')
print(f"merged_unique={len(out)}")
PY

echo
echo "--- Re-aggregating Mac+Win combined bindings + re-rendering ---"
python3 "$REG/scripts/render-per-repo.py" --out "$REG"

echo
echo "--- Done. Review with: ---"
echo "  cat $REG/_bindings.win.json 2>/dev/null | jq 'keys | length'"
echo "  ls $REG/docs/curated-prompts/<source>/<YYYY-MM>/ | head"
