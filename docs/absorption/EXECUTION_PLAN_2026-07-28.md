# Absorption Execution Plan — 2026-07-28

**Status:** READY-TO-EXECUTE pending approvals. Zero destructive ops performed yet.

This document captures exactly what will run on receipt of each user approval. Every step is reversible until execution.

---

## A. Pending user decisions (carried from Phase 2/3)

| # | Decision | Default if no answer | Blocker source |
|---|----------|----------------------|----------------|
| A | `phenotype-router` → `thegent/crates/thegent-router` (Pareto routing engine, Rust lib + cdylib, benches) | DEFER (already recanted SUPERSEDE) | none |
| B | `phenotype-contracts` → `PhenoContracts` (B1, unified contracts → PhenoSpecs+TestingKit per ADR-017) | DEFER | none |
| C | `Compound-Spheres-3D-Backup` → C2 (tombstone both, no merge) | DEFER | non-phenotype |
| D | `UnityDoorstop-NexusPatched` → D1 (tombstone only, preserve 3rd-party fork lineage) | DEFER | fork of `NeighTools/doorstop` |
| E | `argisexec` deeper scan → DONE (3 commits, 4 files, 0 source) | — | resolved 2026-07-28 |
| F | `zen` → F3 (boundary-doc tombstone only, no code merge) | DEFER | deprecated template, target `HexaKit/governance/` missing |
| G | `phenoVessel` → (b) tombstone-only (target `PhenoPlugins/pheno-plugin-vessel` missing locally) | DEFER | target missing |
| H | UNFREEZE `phenotype-registry/registry/disposition-index.json` | DO NOT UNFREEZE | registry `"frozen": true` since 2026-07-18 |
| I | Per-repo squash approval (squash = branch-delete) | DO NOT SQUASH | standing rule |

---

## B. Per-repo execution procedure

For each repo approved via I=Y, the following happens **on the TARGET repo** (since sources are GH-deleted/archived with no local clones). Procedure is per-repo:

### B.1 Servion → `phenotype-tooling/crates/phenotype-service-registry/`

```bash
cd phenotype-tooling
git checkout -b archive/2026-07-28-servion
# Create tombstone file
cat > crates/phenotype-service-registry/ARCHIVED-Servion.md <<'EOF'
# ARCHIVED — Servion
- Absorbed: 2026-06-16
- Source: github.com/KooshaPari/Servion (deleted 2026-06-16)
- Target: crates/phenotype-service-registry (28KB, commit 7c5ed3a66)
- Docket: phenotype-registry/docs/absorption/servion/SUPERSEDES.md
- Status: TARGET IS THE ABSORPTION. Source tombstoned. Deletable.
EOF
git add crates/phenotype-service-registry/ARCHIVED-Servion.md
git commit -m "archive: tombstone Servion absorption (2026-07-28)

Source: github.com/KooshaPari/Servion (deleted 2026-06-16)
Target: phenotype-tooling/crates/phenotype-service-registry (28KB, commit 7c5ed3a66)
Docket: phenotype-registry/docs/absorption/servion/SUPERSEDES.md
[ABSORPTION-TOMBSTONE] User approval received 2026-07-28."
git checkout -b zz-archive/2026-07-28-servion main  # mirror of pre-delete
echo "Servion absorption tombstoned — see ARCHIVED-Servion.md" > zz-archive-servion.txt
git add zz-archive-servion.txt
git commit -m "zz-archive: mirror of GH pre-delete state for Servion"
# squash: collapse archive/ branch to 1 commit, delete zz-archive
git checkout main
git merge --squash archive/2026-07-28-servion
git commit -m "archive/2026-07-28-servion: 1-commit absorption tombstone"
git branch -D archive/2026-07-28-servion zz-archive/2026-07-28-servion
```

### B.2 Guardrail → `phenotype-tooling/crates/phenotype-resilience/`

Same procedure as B.1, with:
- `crates/phenotype-resilience/ARCHIVED-Guardrail.md`
- Source commit `a298f2355`
- Docket `phenotype-registry/docs/absorption/guardrail/SUPERSEDES.md`

### B.3 router-docs → `OmniRoute/docs/research/archive/router-docs/`

Same procedure, but `OmniRoute/` is a multi-crate workspace — tombstone goes on the workspace level, not nested in `docs/research/archive/router-docs/`:
- File: `OmniRoute/ARCHIVED-router-docs.md`
- Source commit `f2b8b3638` (absorb router-docs research corpus from archive)
- Docket `phenotype-registry/docs/absorption/router-docs/SUPERSEDES.md`

### B.4 phenotype-router-spec → `phenotype-registry/docs/specs/router-protocol/`

Already spine content. Tombstone goes on the registry repo:
- File: `phenotype-registry/ARCHIVED-phenotype-router-spec.md`
- Docket `phenotype-registry/docs/specs/router-protocol/README.md` (already exists)

### B.5 phenoRouterMonitor → `phenoAI/crates/llm-router/`

Tombstone goes on phenoAI repo:
- File: `phenoAI/crates/llm-router/ARCHIVED-phenoRouterMonitor.md`
- Source commit `140b98c fix: align phenoAI routing with substrate adapter`
- Docket `phenotype-registry/docs/operations/p5-4-phenoroutermonitor-absorption-2026-06-20.md` (already exists)

### B.6 argisexec → registry-only tombstone (recommended)

User's "much work" memory was incorrect (verified 2026-07-28: 3 commits, 4 files, 0 source). **Recommendation: skip per-repo squash** — there is no source to squash and no target to absorb into. The registry-only tombstone in the disposition-index (after H=Y) is sufficient.

### B.7 phenoVessel → tombstone-only

Target `PhenoPlugins/pheno-plugin-vessel` missing. **Recommendation: tombstone-only via docket** (already written). No squash possible without target.

---

## C. Disposition-index patch application (post-unfreeze H=Y)

```bash
# After user unfreezes the registry
CURRENT_VERSION=$(jq -er '.version | strings' registry/disposition-index.json)
if [[ ! "${CURRENT_VERSION}" =~ ^v([0-9]+)\.([0-9]+)\.([0-9]+)$ ]]; then
  echo "ERROR: registry version is not semver: ${CURRENT_VERSION}" >&2
  exit 1
fi
NEXT_VERSION="v${BASH_REMATCH[1]}.${BASH_REMATCH[2]}.$((BASH_REMATCH[3] + 1))"
jq --argfile patch registry/disposition-pending-additions-2026-07-28.json \
   --arg next_version "${NEXT_VERSION}" \
   --arg frozen_at "$(date -u +%Y-%m-%dT%H:%M:%SZ)" '
  .rows += $patch.rows_to_add
  | .version = $next_version
  | .frozen = true
  | .frozen_at = $frozen_at
  | .frozen_by = "user-approval"
  | .frozen_reason = "Re-frozen after approved rows_to_add patch."
' registry/disposition-index.json > registry/disposition-index.json.tmp
mv registry/disposition-index.json.tmp registry/disposition-index.json
```

Then validate:

```bash
jq '{rows: (.rows | length), version, frozen}' registry/disposition-index.json
```

---

## D. Audit log entry (executed on every approval)

```bash
printf "<timestamp> | convo | absorption-execute | user approved I=Y for: <list>; H=Y (unfreeze registry); per-repo tombstones created on target repos: <list>; disposition-index.json version advanced from the checked-in value and re-frozen; dockets refreshed; all absorbed sources confirmed tombstoned.\n" >> ~/.forge/audit/summary.log
```

---

## E. Safety rails

1. **Per-repo Y required.** No blanket squash. (Squash = branch-delete = destructive per standing rule.)
2. **Registry unfreeze required.** Registry file is `"frozen": true` since 2026-07-18. Edit requires H=Y.
3. **No remote mutations.** All ops are local. No `git push --force`, no GH API deletes.
4. **Re-freeze on every registry edit.** File is re-frozen after each patch application.
5. **Reversibility.** Until user approves per-repo Y, nothing is destructive. Patch file is staged separately from the registry; can be discarded without touching the registry.

---

## F. Final deliverable summary (current state)

| Deliverable | Path | Status |
|-------------|------|--------|
| Audit phase 1-3 | (in chat + audit log) | DONE |
| Staged patch (4 rows) | `phenotype-registry/registry/disposition-pending-additions-2026-07-28.json` | STAGED, not applied |
| Absorption docket — Servion | `phenotype-registry/docs/absorption/servion/SUPERSEDES.md` | DONE |
| Absorption docket — Guardrail | `phenotype-registry/docs/absorption/guardrail/SUPERSEDES.md` | DONE |
| Absorption docket — phenoVessel | `phenotype-registry/docs/absorption/phenovessel/SUPERSEDES.md` | DONE (BLOCKED on target missing) |
| Absorption docket — router-docs | `phenotype-registry/docs/absorption/router-docs/SUPERSEDES.md` | DONE |
| Absorption docket — argisexec | `phenotype-registry/docs/absorption/argisexec/SUPERSEDES.md` | DONE |
| Bare-clone evidence — argisexec | `~/.forge/audit/repo-evidence/argisexec/` (116K, 3 commits) | DONE |
| Audit log | `~/.forge/audit/summary.log` (6 entries this session) | DONE |
| Execution-ready plan | this file | DONE |

---

## G. Reply template (what I need to proceed)

```
A. phenotype-router target = thegent/crates/thegent-router       Y/N/alt
B. phenotype-contracts target = PhenoContracts (B1)              Y/N (or B2/B3)
C. Compound-Spheres-3D-Backup merge = C2 (tombstone both)        Y/N
D. UnityDoorstop-NexusPatched merge = D1 (tombstone only)        Y/N (or D2)
E. argisexec = DONE (acknowledged)
F. zen merge = F3 (boundary-doc tombstone only)                  Y/N (or F1/F2)
G. phenoVessel resolution = (b) tombstone-only                   Y/N
H. UNFREEZE phenotype-registry/registry/disposition-index.json   Y/N
I. per-repo squash approval (each row, or blanket Y):
     phenotype-router-spec    Y/N
     phenoRouterMonitor      Y/N
     Servion                 Y/N
     Guardrail               Y/N
     phenoVessel             Y/N [blocked by G]
     router-docs             Y/N
     argisexec               Y/N (or registry-only [recommended])
     Compound-Spheres-3D-Backup  Y/N
     UnityDoorstop-NexusPatched  Y/N
     phenotype-router            Y/N
     phenotype-contracts         Y/N
     thegent                     Y/N
     zen                         Y/N
```

**Until all `Y` approvals are received, the audit-only phase remains the deliverable, and the destructive items stay pending with explicit blocker notes.**
