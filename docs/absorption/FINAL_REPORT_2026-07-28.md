# SRC → TARGET Audit — Final Report

**Date:** 2026-07-28
**Session:** audit-only (no destructive action performed)
**Authority:** `phenotype-registry/registry/disposition-index.json` + `phenotype-registry/projects/*.json`

## 1. SRC → TARGET table (13 user-listed repos)

| # | SRC | TARGET (proposed/actual) | Status | Evidence |
|---|-----|--------------------------|--------|----------|
| 1 | `phenotype-router-spec` | `phenotype-registry/docs/specs/router-protocol/` | ✅ AFFIRM (SPINE absorbed) | GH-deleted 2026-07-18; `disposition-index.json:1755-1764` records `A:SPINE_CORE fsm=deleted`; target content present (README 5.4K + schema/ + docs/ + examples/) |
| 2 | `phenotype-contracts` | **AFFIRM** (KEEP) — canonical neutral schema SSOT | ✅ RESOLVED EXTERNALLY 2026-07-29 | `audit-absorption-justification/phenotype-contracts-boundary-20260729.json` — `decision: AFFIRM` for phenotype-contracts (live remote `cc8f34e`, public, non-archived) + `KEEP_STANDALONE_PENDING_BOUNDARY_REVIEW` for PhenoContracts (historical ABSORB claim invalid) |
| 3 | `Compound-Spheres-3D-Backup` | non-backup variant `KooshaPari/Compound-Spheres-3D` exists but both archived | non-phenotype, tombstone C2 | `disposition-index.json:5593-5596` (FINAL row); both non-phenotype game-domain content |
| 4 | `UnityDoorstop-NexusPatched` | fork of `NeighTools/doorstop` | non-phenotype, tombstone D1 | preserve 3rd-party fork attribution per legacy-game-mods.md:41 |
| 5 | `phenotype-router` | `thegent/crates/thegent-router` (A — Pareto routing engine) | ⏸ AWAITING A=Y | target verified, benches present; `disposition-index.json:14124-14133` AUDIT-RECIND kept this repo live |
| 6 | `phenoRouterMonitor` | `phenoAI/crates/llm-router/` | ✅ AFFIRM (target verified) | commit `140b98c`; `disposition-index.json:986-994` `AUTO-IMPORT-phenotype-router-monitor fsm=done` |
| 7 | `thegent`/`tehgent` | `Agentora` with name `thegent` | ⏸ DEFERRED | `projects/thegent.json` disposition=`KEEP_CANONICAL`, status=`active`, recovery-preserved; ADR-115 AFFIRM blocked |
| 8 | `argisexec` | **tombstone-only** | ✅ DONE | 3 commits, 4 files, 0 source code; bare clone at `~/.forge/audit/repo-evidence/argisexec/` |
| 9 | `zen` | `HexaKit/governance/` missing | F3 tombstone-only | `HexaKit/` does NOT exist locally; projects/zen.json says `wave: 2026-07-23-boundary-audit` |
| 10 | `phenoVessel` | `PhenoPlugins/pheno-plugin-vessel` MISSING | ⏸ BLOCKED on G | `PhenoPlugins/` does NOT exist; `AgilePlus/PhenoPlugins/` is empty |
| 11 | `Servion` | `phenotype-tooling/crates/phenotype-service-registry/` | ✅ Y captured (code-absorb done) | commit `7c5ed3a66`; target 28K, Cargo.toml + src/ |
| 12 | `Guardrail` | `phenotype-tooling/crates/phenotype-resilience/` | ✅ Y captured (code-absorb done) | commit `a298f2355`; target 48K, Cargo.toml + src/ |
| 13 | `router-docs` | `OmniRoute/docs/research/archive/router-docs/` | ✅ Y captured (code-absorb done) | commit `f2b8b3638`; target README + reference/ + research/ |

## 2. Per-repo evidence summary

### Already-absorbed (5 — verified target present)

```
phenotype-router-spec   → registry/docs/specs/router-protocol/      5.4K README + schema + docs + examples
phenoRouterMonitor      → phenoAI/crates/llm-router/                Cargo.toml + src/, commit 140b98c
Servion                 → phenotype-tooling/crates/phenotype-service-registry/  28K, commit 7c5ed3a66
Guardrail               → phenotype-tooling/crates/phenotype-resilience/        48K, commit a298f2355
router-docs             → OmniRoute/docs/research/archive/router-docs/         README + reference/ + research/, commit f2b8b3638
```

### Externally-resolved (1)

```
phenotype-contracts     → AFFIRM as canonical neutral schema SSOT (no source mutation; remote_sha cc8f34e live, public, non-archived)
                         RESOLVED 2026-07-29 by audit-absorption-justification/phenotype-contracts-boundary-20260729.json
```

### Tombstone-only (2 — no absorbable content)

```
argisexec               → 3 commits, 4 files, 0 source code (deep-scanned); ARCHIVE_ONLY
Compound-Spheres-3D-Backup → non-phenotype game-domain (both variants archived)
UnityDoorstop-NexusPatched → non-phenotype game-mod (fork of NeighTools/doorstop)
zen                     → deprecated minimal template (no functional code to merge)
```

### Live stays (1)

```
phenotype-router        → 134KB Rust decision layer, AUDIT-RECIND kept live per disposition-index.json:14124-14133
```

### Deferred (1)

```
thegent                 → KEEP_CANONICAL per projects/thegent.json; ADR-115 AFFIRM blocked
```

### Blocked (1)

```
phenoVessel             → target PhenoPlugins/pheno-plugin-vessel MISSING locally; awaiting G decision (a/b/c)
```

## 3. Files written this session (all reversible, registry untouched)

| Path | State |
|------|-------|
| `phenotype-registry/registry/disposition-pending-additions-2026-07-28.json` | **WRITTEN** — staged patch (125 lines, valid JSON) |
| `phenotype-registry/docs/absorption/servion/SUPERSEDES.md` | **WRITTEN** (49 lines) |
| `phenotype-registry/docs/absorption/guardrail/SUPERSEDES.md` | **WRITTEN** (50 lines) |
| `phenotype-registry/docs/absorption/router-docs/SUPERSEDES.md` | **WRITTEN** (48 lines) |
| `phenotype-registry/docs/absorption/phenovessel/SUPERSEDES.md` | **WRITTEN** (55 lines, BLOCKED note) |
| `phenotype-registry/docs/absorption/argisexec/SUPERSEDES.md` | **WRITTEN** (75 lines, deep-scan results) |
| `phenotype-registry/docs/absorption/FINAL_REPORT_2026-07-28.md` | **WRITTEN** (this file) |
| `phenotype-registry/docs/absorption/EXECUTION_PLAN_2026-07-28.md` | **WRITTEN** (per-repo procedures) |
| `phenotype-registry/docs/absorption/apply-absorption-decisions.sh` | **WRITTEN** + chmod +x (idempotent wrapper) |
| `~/.forge/audit/repo-evidence/argisexec/` | bare clone persisted (116K, 3 commits) |
| `~/.forge/audit/summary.log` | session audit entries |

**Registry file untouched:** `phenotype-registry/registry/disposition-index.json:4` still reads `"frozen": true`.

## 4. Zero destructive operations performed

- ❌ No `git squash`, no `git push --force`, no branch-delete on any target.
- ❌ No `archive/` or `zz-archive/` branches created.
- ❌ No edits to `phenotype-registry/registry/disposition-index.json` (still `"frozen": true`).
- ❌ No deletion of GH repos, no remote mutations.

## 5. Open user decisions (carry-over from prior phases)

| Item | Question | Default (if no reply) |
|------|----------|------------------------|
| **A** | phenotype-router target = `thegent/crates/thegent-router`? | HOLD (per-repo, no safe default) |
| **B** | phenotype-contracts target = AFFIRM (already resolved 2026-07-29) | ✅ RESOLVED |
| **C** | Compound-Spheres-3D-Backup merge = C2 (tombstone both)? | HOLD (non-phenotype, low risk) |
| **D** | UnityDoorstop-NexusPatched merge = D1 (tombstone only)? | HOLD (fork, low risk) |
| **E** | argisexec deeper scan = DONE (3 commits, 0 source) | ✅ DONE |
| **F** | zen merge = F3 (boundary-doc tombstone only)? | HOLD (deprecated template, low risk) |
| **G** | phenoVessel = (b) tombstone-only? | HOLD (target missing) |
| **H** | UNFREEZE `phenotype-registry/registry/disposition-index.json`? | NO (conservative default per AGENTS.md) |
| **I.2** | per-repo target-side tombstone (Servion, Guardrail, router-docs)? | NO (conservative default — destructive of target branch history) |

## 6. Reply template

To unblock the remaining items, reply per row:

```
A. phenotype-router target            Y/N/alt
C. Compound-Spheres-3D-Backup         Y/N (C2 tombstone both)
D. UnityDoorstop-NexusPatched         Y/N (D1 tombstone only)
F. zen                                Y/N (F3 tombstone only)
G. phenoVessel                        Y/(b)/(a)/(c)
H. UNFREEZE disposition-index.json    Y/N
I.2 Servion target-side tombstone     Y/N
I.2 Guardrail target-side tombstone   Y/N
I.2 router-docs target-side tombstone Y/N
```

B and E are resolved — no reply needed for those.

## 7. Audit log entries this session

`~/.forge/audit/summary.log` contains 11 session entries (audit-only → audit-phase2 → phase3-deeper-eval → phase3-reconcile → phase3-argisexec-deep-scan → phase3-final → phase3-final-execution-plan → phase3-y-approval-captured → phase3-system-reminder-reconcile → phase3-FINAL-REPORT → phase3-executable-wrapper).
