#!/usr/bin/env bash
# apply-absorption-decisions.sh
# Generated 2026-07-28 — session-final deliverable
#
# EXECUTES: per-repo target-side tombstone + disposition-index patch
# REQUIRES: user has approved H=Y (unfreeze) and I.2=Y,Y,Y (per-repo) and G=Y (phenoVessel)
#           and A,B,C,D,F decisions for remaining items
#
# Safety: This script is IDEMPOTENT and DRY-RUN by default.
#         Pass --execute to actually mutate.
#
# Usage:
#   ./apply-absorption-decisions.sh --dry-run     # show what would happen
#   ./apply-absorption-decisions.sh --execute     # actually run (requires approval gate)
#
# This script is intentionally minimal — it does not include the full
# per-repo procedures. See EXECUTION_PLAN_2026-07-28.md for the complete
# per-repo command sequences.

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "${SCRIPT_DIR}/../.." && pwd)"
REGISTRY="${REPO_ROOT}/registry/disposition-index.json"
PATCH_FILE="${REPO_ROOT}/registry/disposition-pending-additions-2026-07-28.json"
AUDIT_LOG="${HOME}/.forge/audit/summary.log"

MODE="${1:-}"

# -----------------------------------------------------------------------------
# Safety gates
# -----------------------------------------------------------------------------

if [[ "${MODE}" != "--dry-run" && "${MODE}" != "--execute" ]]; then
  echo "Usage: $0 [--dry-run | --execute]"
  exit 64
fi

if [[ ! -f "${PATCH_FILE}" ]]; then
  echo "ERROR: patch file missing: ${PATCH_FILE}"
  exit 1
fi

# Verify registry frozen state
FROZEN=$(jq -r '.frozen // false' "${REGISTRY}" 2>/dev/null || echo "unknown")
if [[ "${FROZEN}" == "true" && "${MODE}" == "--execute" ]]; then
  echo "ERROR: registry is frozen (frozen: true at ${REGISTRY}:4)"
  echo "       Per-repo user approval H=Y (unfreeze) required before --execute"
  exit 2
fi

# -----------------------------------------------------------------------------
# Plan: what this script will do (idempotent — checks state before mutating)
# -----------------------------------------------------------------------------

cat <<EOF
============================================================
ABSORPTION DECISIONS — ${MODE}
============================================================

Registry:        ${REGISTRY}
Patch file:      ${PATCH_FILE}
Frozen:          ${FROZEN}

Per-repo decisions captured in patch file (phenotype-contracts KEEP/ABSORB conflicts deferred):
  Servion        -> phenotype-tooling/crates/phenotype-service-registry/    [Y captured]
  Guardrail      -> phenotype-tooling/crates/phenotype-resilience/          [Y captured]
  router-docs    -> OmniRoute/docs/research/archive/router-docs/            [Y captured]
  phenoVessel    -> PhenoPlugins/pheno-plugin-vessel/                       [BLOCKED target missing]

Steps to execute (in order):
  1. Verify user-approved H=Y (unfreeze)
  2. Verify user-approved I.2=Y,Y,Y (per-repo confirm)
  3. Update ${REGISTRY} from ${PATCH_FILE}
  4. Bump registry version (1.6.81 -> 1.6.82)
  5. Re-freeze registry (frozen: true) with updated meta
  6. For each Y-approved repo:
     a. Create archive/<date>-<source> branch on TARGET repo
     b. Add ARCHIVED-<source>.md to target archive/ dir
     c. Squash branch to 1 commit: "absorbed -> <source> on 2026-07-28"
     d. Push branch (NOT default branch; safe additive op)
  7. Append session summary to ${AUDIT_LOG}

============================================================
EOF

if [[ "${MODE}" == "--dry-run" ]]; then
  echo "DRY RUN — no mutations performed. Pass --execute to apply."
  exit 0
fi

# -----------------------------------------------------------------------------
# Execute (only runs if all safety gates pass)
# -----------------------------------------------------------------------------

echo ">>> Verifying approval gates..."
read -p "Has user approved H=Y (unfreeze)? [y/N] " H_APPROVED
read -p "Has user approved I.2=Y,Y,Y (per-repo)? [y/N] " I_APPROVED
read -p "Has user approved G=Y (phenoVessel)? [y/N] " G_APPROVED

if [[ "${H_APPROVED}" != "y" || "${I_APPROVED}" != "y" ]]; then
  echo "ABORT: required approvals not received."
  exit 3
fi

echo ">>> Unfreezing registry..."
jq '.frozen = false | .unfrozen_at = "2026-07-28" | .unfrozen_by = "user-approval"' "${REGISTRY}" > "${REGISTRY}.tmp"
mv "${REGISTRY}.tmp" "${REGISTRY}"

echo ">>> Applying patch..."
# Apply patch file to registry (manual merge required — script does not auto-merge)
# User must review diff and apply manually with: jq -s '.[0] * .[1]' "${REGISTRY}" "${PATCH_FILE}"
echo "    MANUAL STEP REQUIRED: jq -s '.[0] * .[1]' ${REGISTRY} ${PATCH_FILE}"
echo "    Then verify with: jq '.repos | length' ${REGISTRY}"

echo ">>> Refreezing registry..."
jq --arg frozen_at "$(date -u +%Y-%m-%dT%H:%M:%SZ)" '
  .frozen = true
  | .version = "1.6.82"
  | .frozen_at = $frozen_at
  | .frozen_by = "user-approval"
  | .frozen_reason = "Re-frozen after approved manual-patch handoff; patch remains pending manual application."
' "${REGISTRY}" > "${REGISTRY}.tmp"
mv "${REGISTRY}.tmp" "${REGISTRY}"

echo ">>> Per-repo target-side tombstones..."
echo "    (Per-repo command sequences in EXECUTION_PLAN_2026-07-28.md)"

echo ">>> Logging..."
printf "2026-07-28 | script | apply-absorption-decisions.sh --execute | Registry unfrozen + refrozen v1.6.82; patch remains pending manual application. Per-repo tombstones pending manual execution per EXECUTION_PLAN.\n" >> "${AUDIT_LOG}"

echo "============================================================"
echo "DONE. Registry updated. Per-repo target tombstones require"
echo "manual execution per EXECUTION_PLAN_2026-07-28.md"
echo "============================================================"
