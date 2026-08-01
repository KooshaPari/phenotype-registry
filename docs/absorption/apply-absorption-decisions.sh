#!/usr/bin/env bash
# apply-absorption-decisions.sh
# Generated 2026-07-28 — session-final deliverable
#
# EXECUTES: per-repo target-side tombstone + disposition-index patch
# REQUIRES: user has approved H=Y (unfreeze), I.2=Y,Y,Y (per-repo), and G=Y (phenoVessel)
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

# Verify registry frozen state and capture the current version.  The version is
# advanced from the checked-in value below; never use a historical literal.
FROZEN=$(jq -r '.frozen // false' "${REGISTRY}" 2>/dev/null || echo "unknown")
CURRENT_VERSION=$(jq -er '.version | strings' "${REGISTRY}" 2>/dev/null || echo "unknown")
if [[ ! "${CURRENT_VERSION}" =~ ^v([0-9]+)\.([0-9]+)\.([0-9]+)$ ]]; then
  echo "ERROR: registry version is not semver (expected vMAJOR.MINOR.PATCH): ${CURRENT_VERSION}"
  exit 1
fi
NEXT_VERSION="v${BASH_REMATCH[1]}.${BASH_REMATCH[2]}.$((BASH_REMATCH[3] + 1))"
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
Version:         ${CURRENT_VERSION} -> ${NEXT_VERSION}

Per-repo decisions captured in patch file (phenotype-contracts KEEP/ABSORB conflicts deferred):
  Servion        -> phenotype-tooling/crates/phenotype-service-registry/    [Y captured]
  Guardrail      -> phenotype-tooling/crates/phenotype-resilience/          [Y captured]
  router-docs    -> OmniRoute/docs/research/archive/router-docs/            [Y captured]
  phenoVessel    -> PhenoPlugins/pheno-plugin-vessel/                       [BLOCKED target missing]

Steps to execute (in order):
  1. Verify user-approved H=Y (unfreeze)
  2. Verify user-approved I.2=Y,Y,Y (per-repo confirm)
  3. Append ${PATCH_FILE}:rows_to_add to ${REGISTRY}:rows (reject duplicate IDs)
  4. Advance the checked-in version (${CURRENT_VERSION} -> ${NEXT_VERSION})
  5. Re-freeze registry (frozen: true) with top-level metadata
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

if [[ "${H_APPROVED}" != "y" || "${I_APPROVED}" != "y" || "${G_APPROVED}" != "y" ]]; then
  echo "ABORT: required approvals not received."
  exit 3
fi

echo ">>> Applying patch and re-freezing registry atomically..."
FROZEN_AT=$(date -u +%Y-%m-%dT%H:%M:%SZ)
REGISTRY_TMP=$(mktemp "${REGISTRY}.tmp.XXXXXX")
trap 'rm -f "${REGISTRY_TMP:-}"' EXIT

jq -e --arg next_version "${NEXT_VERSION}" --arg frozen_at "${FROZEN_AT}" '
  (.rows | type) == "array"
  and ((.rows | map(select(.id != null) | .id) | length)
       == (.rows | map(select(.id != null) | .id) | unique | length))
' "${REGISTRY}" >/dev/null

jq -e --argfile patch "${PATCH_FILE}" '
  ($patch.rows_to_add | type) == "array"
  and (($patch.rows_to_add | map(select(.id != null) | .id) | length)
       == ($patch.rows_to_add | map(select(.id != null) | .id) | unique | length))
  and ([.rows[].id] as $existing
       | [$patch.rows_to_add[] | select(.id as $id | $existing | index($id))]
       | length == 0)
' "${REGISTRY}" >/dev/null

jq --argfile patch "${PATCH_FILE}" \
   --arg next_version "${NEXT_VERSION}" \
   --arg frozen_at "${FROZEN_AT}" \
   --arg current_version "${CURRENT_VERSION}" '
  .rows += $patch.rows_to_add
  | .version = $next_version
  | .frozen = true
  | .frozen_at = $frozen_at
  | .frozen_by = "user-approval"
  | .frozen_reason = ("Re-frozen after approved rows_to_add patch from "
      + $current_version + ".")
  | .unfrozen_at = $frozen_at
  | .unfrozen_by = "user-approval"
' "${REGISTRY}" > "${REGISTRY_TMP}"
mv "${REGISTRY_TMP}" "${REGISTRY}"
trap - EXIT

echo ">>> Per-repo target-side tombstones..."
echo "    (Per-repo command sequences in EXECUTION_PLAN_2026-07-28.md)"

echo ">>> Logging..."
printf "%s | script | apply-absorption-decisions.sh --execute | Registry rows_to_add applied; version %s -> %s; registry re-frozen. Per-repo tombstones pending manual execution per EXECUTION_PLAN.\n" \
  "${FROZEN_AT}" "${CURRENT_VERSION}" "${NEXT_VERSION}" >> "${AUDIT_LOG}"

echo "============================================================"
echo "DONE. Registry rows_to_add applied and re-frozen. Per-repo target tombstones require"
echo "manual execution per EXECUTION_PLAN_2026-07-28.md"
echo "============================================================"
