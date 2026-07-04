#!/usr/bin/env bash
# grade.sh — Fleet-wide project grading engine (ROOT ENTRY POINT)
# This file is a thin delegation shim.
# The canonical grader lives under:
#   registry/audit-absorption-justification/grade.sh
# All flags and arguments are forwarded to the canonical grader.
#
# Usage (same as canonical):
#   ./grade.sh [--fast] [--json] [--html]
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CANONICAL="$SCRIPT_DIR/registry/audit-absorption-justification/grade.sh"

if [[ ! -x "$CANONICAL" && ! -f "$CANONICAL" ]]; then
  echo "ERROR: canonical grader not found: $CANONICAL" >&2
  exit 1
fi

exec "$CANONICAL" "$@"
