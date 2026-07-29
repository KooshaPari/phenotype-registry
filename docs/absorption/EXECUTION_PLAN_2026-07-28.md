# Execution Plan — Per-Repo Procedures

**Date:** 2026-07-28
**Session:** audit-only (this plan is READY to execute; awaiting user Y-approval on blocked items)
**Companion files:** `FINAL_REPORT_2026-07-28.md`, `apply-absorption-decisions.sh`

## A. Open user decisions + safe defaults

If user does NOT reply to a given item, the **safe default** is held (no destructive action). For audit-trail purposes:

| Item | Question | Safe default if no reply |
|------|----------|--------------------------|
| A | phenotype-router target | HOLD — do not auto-merge into `thegent/crates/thegent-router` |
| C | Compound-Spheres-3D-Backup | HOLD — no source mutation; non-phenotype tombstone-only is the conservative choice |
| D | UnityDoorstop-NexusPatched | HOLD — preserve 3rd-party fork attribution; tombstone-only |
| F | zen | HOLD — deprecated template, no functional code; tombstone-only at boundary doc |
| G | phenoVessel | HOLD — target missing; tombstone-only is the conservative choice |
| H | UNFREEZE registry | NO — registry file remains `"frozen": true` |
| I.2 (Servion) | target-side tombstone | NO — destructive of `phenotype-tooling` branch history |
| I.2 (Guardrail) | target-side tombstone | NO — destructive of `phenotype-tooling` branch history |
| I.2 (router-docs) | target-side tombstone | NO — destructive of `OmniRoute` branch history |

## B. Per-repo execution procedures (post Y-approval)

### B.1. Apply staged patch to `disposition-index.json`

**Trigger:** `H = Y` (registry unfreeze).

**Steps:**

1. Read current `disposition-index.json` and confirm `"frozen": true` → set to `"frozen": false`.
2. Update `"frozen_at"` to `null` and `"frozen_by"` to `null`.
3. Update `"frozen_reason"` to `"Unfrozen 2026-07-28 by user H=Y for staged patch application (disposition-pending-additions-2026-07-28.json)."`
4. Append the 4 staged rows to the `"rows": [...]` array:
   - `Servion` row (affirm-already-absorbed, target = `phenotype-tooling/crates/phenotype-service-registry`)
   - `Guardrail` row (affirm-already-absorbed, target = `phenotype-tooling/crates/phenotype-resilience`)
   - `router-docs` row (affirm-already-absorbed, target = `OmniRoute/docs/research/archive/router-docs`)
   - `phenoVessel` row (BLOCKED-target-missing; user G decision determines final disposition)
5. Bump `version` (currently unspecified in head; if present, bump minor).
6. Set `"frozen": true` again (re-freeze after edit) with new `frozen_at` = current ISO timestamp.
7. Commit with message: *"registry: apply disposition-pending-additions-2026-07-28 — add Servion/Guardrail/router-docs/phenoVessel rows"*

### B.2. Execute per-repo target-side tombstone for Servion

**Trigger:** `I.2 = Y` for Servion.

**Steps (run on `phenotype-tooling` local repo):**

1. Verify target exists: `ls phenotype-tooling/crates/phenotype-service-registry/`
2. `git -C phenotype-tooling checkout main` (assume main; adapt if not).
3. `git -C phenotype-tooling checkout -b archive/2026-07-28-servion`
4. Create `crates/phenotype-service-registry/ARCHIVED-Servion.md` with content:

   ```markdown
   # ARCHIVED-Servion

   **Source repo:** KooshaPari/Servion (deleted 2026-06-16)
   **Absorbed into:** `phenotype-service-registry` crate (commit 7c5ed3a66)
   **Docket:** `phenotype-registry/docs/absorption/servion/SUPERSEDES.md`

   The legacy `Servion` name is SUPERSEDED by `phenotype_service_registry`.
   Do not re-introduce the `Servion` import path.
   ```

5. `git -C phenotype-tooling add crates/phenotype-service-registry/ARCHIVED-Servion.md`
6. `git -C phenotype-tooling commit -m "archive(2026-07-28): tombstone Servion absorption (registry docket)"`
7. Optionally `git -C phenotype-tooling push origin archive/2026-07-28-servion` (NEEDS explicit user Y for push).

### B.3. Execute per-repo target-side tombstone for Guardrail

**Trigger:** `I.2 = Y` for Guardrail.

**Steps:** Same as B.2 but on `phenotype-tooling/crates/phenotype-resilience/`, commit `a298f2355`, docket `phenotype-registry/docs/absorption/guardrail/SUPERSEDES.md`.

### B.4. Execute per-repo target-side tombstone for router-docs

**Trigger:** `I.2 = Y` for router-docs.

**Steps:** Same as B.2 but on `OmniRoute/docs/research/archive/router-docs/`, commit `f2b8b3638`, docket `phenotype-registry/docs/absorption/router-docs/SUPERSEDES.md`.

### B.5. Resolve phenoVessel (option a/b/c per G)

**Trigger:** `G = a | b | c`.

**Steps:**

- **(a) Scaffold** — `mkdir -p PhenoPlugins/crates/pheno-plugin-vessel`, add placeholder README + Cargo.toml. (NOT recommended — fabricates content.)
- **(b) Tombstone-only** — Update docket `phenovessel/SUPERSEDES.md` to mark "absorbed_into pointer unbacked; tombstone-only." Apply disposition-index patch row with disposition=`ARCHIVE_ONLY target=none`. (RECOMMENDED.)
- **(c) Skip** — Do nothing; lose audit trail. (NOT recommended.)

## C. Registry patch application procedure (post unfreeze)

See B.1 above. Steps are linear, idempotent, and reversible via `git revert`.

## D. Audit log entry template

After each execution step, append to `~/.forge/audit/summary.log`:

```
2026-07-28 | convo | <phase-name> | <action performed> | <files touched> | <state after action>
```

## E. Safety rails

Per AGENTS.md + user standing rules:

1. No `git push --force` ever.
2. No `rm -rf`, no `dd`, no `mkfs`, no `shutdown`, no `reboot`.
3. No edits to `~/.config/forge/.secrets` or env vars starting with `*_KEY`, `*_TOKEN`, `*_SECRET`.
4. No destructive op without explicit per-row user Y.
5. Registry file (`disposition-index.json`) is `"frozen": true`; any edit requires explicit unfreeze.

## F. Final deliverable summary (this session)

| File | Purpose |
|------|---------|
| `registry/disposition-pending-additions-2026-07-28.json` | 4 staged rows + per-repo Y-state |
| `docs/absorption/servion/SUPERSEDES.md` | Servion docket |
| `docs/absorption/guardrail/SUPERSEDES.md` | Guardrail docket |
| `docs/absorption/router-docs/SUPERSEDES.md` | router-docs docket |
| `docs/absorption/phenovessel/SUPERSEDES.md` | phenoVessel docket (BLOCKED) |
| `docs/absorption/argisexec/SUPERSEDES.md` | argisexec docket (deep-scan) |
| `docs/absorption/FINAL_REPORT_2026-07-28.md` | Single-file canonical summary |
| `docs/absorption/EXECUTION_PLAN_2026-07-28.md` | This file |
| `docs/absorption/apply-absorption-decisions.sh` | Idempotent shell wrapper (chmod +x) |

## G. Reply template

To execute any of the above, reply with Y/N per item:

```
H. UNFREEZE disposition-index.json            Y/N
I.2 Servion target-side tombstone             Y/N
I.2 Guardrail target-side tombstone           Y/N
I.2 router-docs target-side tombstone         Y/N
G. phenoVessel                                Y/(a)/(b)/(c)
A. phenotype-router target                    Y/N/alt
C. Compound-Spheres-3D-Backup merge           Y/N
D. UnityDoorstop-NexusPatched merge           Y/N
F. zen merge                                  Y/N
```

B and E are resolved externally — no reply needed.
