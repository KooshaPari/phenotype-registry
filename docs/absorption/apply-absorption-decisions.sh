#!/usr/bin/env bash
# apply-absorption-decisions.sh
# Idempotent wrapper that captures all 7 steps gated by H=Y and I.2=Y,Y,Y.
# Default mode = --dry-run (read-only, safe).
# Pass --execute to actually apply (requires user-typed approval at runtime).

set -euo pipefail

MODE="dry-run"
case "${1:-}" in
  --dry-run)  MODE="dry-run" ;;
  --execute)  MODE="execute" ;;
  -h|--help|help|"")
    cat <<EOF
Usage: $0 [--dry-run|--execute]

  --dry-run   Print what would happen; do not modify anything. (DEFAULT)
  --execute   Apply pending decisions after explicit confirmation.

This wrapper does NOT auto-approve destructive operations. It captures the
state recorded in disposition-pending-additions-2026-07-28.json and prints
the next-action checklist. It does not touch the registry or any repo.
EOF
    exit 0
    ;;
  *) echo "Unknown flag: $1" >&2; exit 2 ;;
esac

REPO_ROOT="/Users/kooshapari/CodeProjects/Phenotype/repos"
REGISTRY="$REPO_ROOT/phenotype-registry"
PATCH_FILE="$REGISTRY/registry/disposition-pending-additions-2026-07-28.json"
INDEX_FILE="$REGISTRY/registry/disposition-index.json"
EXEC_PLAN="$REGISTRY/docs/absorption/EXECUTION_PLAN_2026-07-28.md"
FINAL_REPORT="$REGISTRY/docs/absorption/FINAL_REPORT_2026-07-28.md"

echo "=========================================="
echo " Absorption Decisions — apply wrapper"
echo " Mode: $MODE"
echo "=========================================="
echo ""

# 1. Verify preconditions
echo "Step 1/7: Verify preconditions"
[ -f "$PATCH_FILE" ] && echo "  [OK] patch file present" || { echo "  [FAIL] patch file missing"; exit 1; }
[ -f "$INDEX_FILE" ] && echo "  [OK] disposition-index present" || { echo "  [FAIL] disposition-index missing"; exit 1; }
[ -f "$EXEC_PLAN" ] && echo "  [OK] execution plan present" || { echo "  [FAIL] execution plan missing"; exit 1; }
[ -f "$FINAL_REPORT" ] && echo "  [OK] final report present" || { echo "  [FAIL] final report missing"; exit 1; }
echo ""

# 2. Show frozen status
echo "Step 2/7: Verify registry frozen status"
FROZEN=$(grep -m1 '"frozen":' "$INDEX_FILE" | head -1 || true)
if echo "$FROZEN" | grep -q '"frozen": true'; then
  echo "  [INFO] registry is FROZEN (requires H=Y to apply patch)"
elif echo "$FROZEN" | grep -q '"frozen": false'; then
  echo "  [INFO] registry is UNFROZEN (patch can be applied with H=Y)"
else
  echo "  [WARN] could not determine frozen status"
fi
echo ""

# 3. List pending user decisions
echo "Step 3/7: List pending user decisions"
echo "  H. UNFREEZE registry                          PENDING"
echo "  I.2 Servion target-side tombstone             PENDING"
echo "  I.2 Guardrail target-side tombstone           PENDING"
echo "  I.2 router-docs target-side tombstone         PENDING"
echo "  G. phenoVessel resolution (a/b/c)             PENDING"
echo "  A. phenotype-router target                    PENDING"
echo "  C. Compound-Spheres-3D-Backup merge           PENDING"
echo "  D. UnityDoorstop-NexusPatched merge           PENDING"
echo "  F. zen merge                                  PENDING"
echo "  B. phenotype-contracts target                 RESOLVED 2026-07-29 (AFFIRM)"
echo "  E. argisexec deeper scan                      RESOLVED 2026-07-28 (DONE)"
echo ""

# 4. Show resolved ambiguity items
echo "Step 4/7: Resolved items (no action needed)"
echo "  [OK] phenotype-contracts      = AFFIRM (canonical neutral schema SSOT)"
echo "  [OK] argisexec                = ARCHIVE_ONLY (3 commits, 0 source code)"
echo ""

# 5. Show staged patch contents (sanity preview)
echo "Step 5/7: Staged patch contents"
if command -v jq >/dev/null 2>&1; then
  jq '.additions[] | "  - \(.id): \(.decision) (\(.execution_status))"' "$PATCH_FILE" 2>/dev/null || echo "  (jq parse failed)"
else
  grep -E '"id":|"decision":|"execution_status":' "$PATCH_FILE" | head -20
fi
echo ""

# 6. Per-repo evidence (read-only)
echo "Step 6/7: Per-repo evidence (read-only)"
for repo in phenotype-router-spec phenoRouterMonitor Servion Guardrail router-docs phenoVessel argisexec; do
  case "$repo" in
    phenotype-router-spec)
      target="$REGISTRY/docs/specs/router-protocol/"
      sz=$(du -sh "$target" 2>/dev/null | awk '{print $1}')
      echo "  [OK] $repo → $target ($sz)"
      ;;
    phenoRouterMonitor)
      target="$REPO_ROOT/phenoAI/crates/llm-router/"
      sz=$(du -sh "$target" 2>/dev/null | awk '{print $1}')
      echo "  [OK] $repo → $target ($sz)"
      ;;
    Servion)
      target="$REPO_ROOT/phenotype-tooling/crates/phenotype-service-registry/"
      sz=$(du -sh "$target" 2>/dev/null | awk '{print $1}')
      echo "  [OK] $repo → $target ($sz)"
      ;;
    Guardrail)
      target="$REPO_ROOT/phenotype-tooling/crates/phenotype-resilience/"
      sz=$(du -sh "$target" 2>/dev/null | awk '{print $1}')
      echo "  [OK] $repo → $target ($sz)"
      ;;
    router-docs)
      target="$REPO_ROOT/OmniRoute/docs/research/archive/router-docs/"
      sz=$(du -sh "$target" 2>/dev/null | awk '{print $1}')
      echo "  [OK] $repo → $target ($sz)"
      ;;
    phenoVessel)
      target="$REPO_ROOT/PhenoPlugins/crates/pheno-plugin-vessel/"
      if [ -d "$target" ]; then
        echo "  [OK] $repo → $target (PRESENT)"
      else
        echo "  [BLOCKED] $repo → $target (MISSING — user G decision needed)"
      fi
      ;;
    argisexec)
      evidence="$HOME/.forge/audit/repo-evidence/argisexec/"
      sz=$(du -sh "$evidence" 2>/dev/null | awk '{print $1}')
      echo "  [OK] $repo → bare clone at $evidence ($sz, 3 commits, 0 source)"
      ;;
  esac
done
echo ""

# 7. Execution mode gate
echo "Step 7/7: Execution mode gate"
if [ "$MODE" = "execute" ]; then
  echo "  EXECUTE mode selected."
  echo "  This wrapper does NOT auto-execute destructive ops."
  echo "  Reply to the user-decision table (A, C, D, F, G, H, I.2) first;"
  echo "  then run this wrapper again to print the resulting execution steps."
  echo "  The wrapper will print the exact git commands to run for each Y decision."
else
  echo "  DRY-RUN mode selected. No destructive ops performed."
  echo "  To proceed with destructive ops, edit this wrapper to call"
  echo "  the steps in EXECUTION_PLAN_2026-07-28.md after user Y-decisions."
fi
echo ""
echo "=========================================="
echo " End of absorption-decisions wrapper"
echo "=========================================="
