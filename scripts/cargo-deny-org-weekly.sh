#!/bin/bash
# Org-wide cargo-deny weekly check (local alternative to Actions billing-blocked CI)
# Generated 2026-04-27 via Kimi K2.5 (nvidia/moonshotai/kimi-k2.5)
set -uo pipefail

WORKDIR="${1:-/Users/kooshapari/CodeProjects/Phenotype/repos}"
REPORT_DIR="${2:-/tmp/cargo-deny-reports}"
mkdir -p "$REPORT_DIR"
REPORT="$REPORT_DIR/cargo-deny-report-$(date -u +%Y%m%d-%H%M).md"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

echo "# Cargo Deny Org Report ($(date -u +%Y-%m-%dT%H:%M:%SZ))" > "$REPORT"
echo "" >> "$REPORT"

check() {
  local dir="$1"
  local name out ec
  [[ -f "$dir/Cargo.toml" ]] || return 0
  case "$dir" in *-wtrees|*/.archive*|*/worktrees*) return 0 ;; esac
  name=$(basename "$dir")
  out="$TMP/$name.log"
  echo "## $name" > "$out"
  if timeout 90 cargo deny --manifest-path "$dir/Cargo.toml" check 2>&1 | tail -50 >> "$out"; then
    ec=${PIPESTATUS[0]}
  else
    ec=$?
  fi
  if [[ $ec -eq 0 ]]; then
    echo "" >> "$out"; echo "✅ PASS" >> "$out"
  elif [[ $ec -eq 124 ]]; then
    echo "" >> "$out"; echo "⏱️ TIMEOUT (90s)" >> "$out"
  else
    echo "" >> "$out"; echo "❌ FAIL (exit $ec)" >> "$out"
  fi
  echo "" >> "$out"
}
export -f check
export TMP

find "$WORKDIR" -maxdepth 2 -type d ! -path "$WORKDIR" -print0 2>/dev/null | xargs -0 -P 4 -I{} bash -c 'check "$@"' _ {}

# Aggregate
for f in "$TMP"/*.log; do cat "$f" >> "$REPORT"; done

# Summary
total=$(ls "$TMP"/*.log 2>/dev/null | wc -l | tr -d ' ')
fail=$(grep -l "FAIL\|TIMEOUT" "$TMP"/*.log 2>/dev/null | wc -l | tr -d ' ')
echo "" >> "$REPORT"
echo "## Summary" >> "$REPORT"
echo "Total repos checked: $total" >> "$REPORT"
echo "Failed/Timeout: $fail" >> "$REPORT"
echo "" >> "$REPORT"

echo "Report: $REPORT"
echo "Total: $total | Fail/Timeout: $fail"
