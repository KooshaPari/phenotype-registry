#!/usr/bin/env bash
# run-all.sh — Run the scraper on both Mac (this device) and Windows (via Tailscale SSH).
#
# Usage:
#   bash scripts/run-all.sh           # full sweep
#   bash scripts/run-all.sh --incremental
#
# Expects the registry worktree at $REG (defaults to current dir or its parent).
set -euo pipefail

REG="${REG:-$(cd "$(dirname "$0")/.." && pwd)}"
DEVICE_HOST="${DEVICE_HOST:-kooshapari-desk}"
DEVICE_USER="${DEVICE_USER:-koosh}"
DEVICE_REMOTE_DIR="${DEVICE_REMOTE_DIR:-/c/Users/koosh/scrape-windows}"

INCREMENTAL=""
if [[ "${1:-}" == "--incremental" ]]; then
    INCREMENTAL="--incremental"
fi

echo "=== phenotype-registry scraper orchestrator ==="
echo "  registry root : $REG"
echo "  windows host  : $DEVICE_USER@$DEVICE_HOST"
echo "  windows dir   : $DEVICE_REMOTE_DIR"
echo "  incremental   : ${INCREMENTAL:-no}"
echo

echo "--- Mac pass ---"
python3 "$REG/scripts/scrape.py" --device mac --out "$REG" $INCREMENTAL

echo
echo "--- Windows pass (via tailscale SSH) ---"
RSYNC_TARGET="$DEVICE_USER@$DEVICE_HOST:$DEVICE_REMOTE_DIR"
echo "  preparing $RSYNC_TARGET"
ssh -o BatchMode=yes -o ConnectTimeout=15 "$DEVICE_USER@$DEVICE_HOST" "mkdir -p $DEVICE_REMOTE_DIR/scripts"
scp "$REG/scripts/scrape.py" "$DEVICE_USER@$DEVICE_HOST:$DEVICE_REMOTE_DIR/scripts/scrape.py"
echo "  running scrape on Windows (this can take several minutes)..."
ssh -o BatchMode=yes -o ConnectTimeout=15 "$DEVICE_USER@$DEVICE_HOST" "cd $DEVICE_REMOTE_DIR && python scripts/scrape.py --device win --out . $INCREMENTAL" || {
    echo "  WARNING: Windows scrape failed; continuing with Mac data only."
}
echo "  pulling _curated.jsonl back to $REG"
scp "$DEVICE_USER@$DEVICE_HOST:$DEVICE_REMOTE_DIR/_curated.jsonl" "$REG/_curated.win.jsonl" 2>/dev/null || true
scp "$DEVICE_USER@$DEVICE_HOST:$DEVICE_REMOTE_DIR/_bindings.json" "$REG/_bindings.win.json" 2>/dev/null || true
scp "$DEVICE_USER@$DEVICE_HOST:$DEVICE_REMOTE_DIR/_seen.txt" "$REG/_seen.win.txt" 2>/dev/null || true

echo
echo "--- Render per-repo intent + boundary from combined bindings ---"
python3 "$REG/scripts/render-per-repo.py" --out "$REG"

echo
echo "--- Done. Review with: ---"
echo "  cat $REG/_bindings.json | jq 'keys | length'"
echo "  cat $REG/_bindings.win.json | jq 'keys | length' 2>/dev/null"
echo "  ls $REG/docs/curated-prompts/<source>/<YYYY-MM>/ | head"
