# phenoVessel — Absorption Docket (BLOCKED)

**Date:** 2026-07-28
**Source:** KooshaPari/phenoVessel (private, source deleted 2026-06-16)
**Target:** `PhenoPlugins/pheno-plugin-vessel` *(declared in projects/phenoVessel.json:10)*
**Disposition:** BLOCKED — target not materialized
**Wave:** 2026-07-28-audit-only
**Decision authority:** `projects/phenoVessel.json`

## State (as of 2026-07-28) — BLOCKED

- **Source repo:** KooshaPari/phenoVessel — DELETED from GitHub on 2026-06-16 per `projects/phenoVessel.json:11`. No local clone exists; no remote clone possible.
- **Declared target:** `PhenoPlugins/pheno-plugin-vessel` — **NOT FOUND LOCALLY**:
  - `/Users/kooshapari/CodeProjects/Phenotype/repos/PhenoPlugins/` — does NOT exist (despite being listed in the session's initial repo listing — the listing was stale).
  - Only `AgilePlus/PhenoPlugins/` exists, and its contents are EMPTY (no README.md, no Cargo.toml, no plugin source).
  - `find /Users/kooshapari/CodeProjects/Phenotype/repos -maxdepth 5 -name "pheno-plugin-vessel*"` returned **0 results**.

## Why this is blocked

The declared absorption target was never materialized. The source repo was deleted before the absorbing crate was created. There is no code anywhere in the local workspace that corresponds to `phenoVessel`'s absorbed content — the absorbed_into pointer is **unbacked**.

This is **not** a "loss" in the strict sense — `phenoVessel` was a deprecated HTML-template scaffold (per `projects/phenoVessel.json:3-8`: `languages: ["html"]`, `type: "plugin"`). Whatever HTML scaffolding it contained has either been re-implemented ad-hoc in another Pheno plugin crate, or it was always negligible. But we cannot confirm either without the source repo, which is gone.

## Options for resolution

### (a) Scaffold the target retroactively *(not recommended)*

- Create `/Users/kooshapari/CodeProjects/Phenotype/repos/PhenoPlugins/` (currently missing).
- Create `crates/pheno-plugin-vessel/` with placeholder HTML scaffolding matching whatever minimal value the source had.
- **Risk:** fabricates content. Per AGENTS.md, we do not synthesize content we cannot verify.

### (b) Tombstone-only at this docket *(recommended)*

- Acknowledge in the registry that the absorption was **declared but never materialized**.
- This docket serves as the only artifact: *"phenoVessel was declared absorbed into PhenoPlugins/pheno-plugin-vessel, but the target was never created; absorbed content lost or never existed."*
- Add a row to the registry disposition-index marking this as `B:WORKING fsm=lost` (a new disposition) or `fsm=archived target=none`.

### (c) Skip — lose audit trail *(not recommended)*

- Do nothing.
- The audit trail is broken. Future readers will see the `absorbed_into` pointer and look for the target, which doesn't exist.

## User Y-approval state

- **Y** NOT received (blocked on `G` decision).
- Pending user reply to: `G. phenoVessel = (a) scaffold / (b) tombstone-only / (c) skip`

## Recommended action

Choose **(b) tombstone-only**. This is the conservative, audit-preserving choice that does not fabricate content.

## Related artifacts

- `phenotype-registry/projects/phenoVessel.json:1-12` — source metadata + absorbed_into pointer (now stale).
- `phenotype-registry/registry/disposition-pending-additions-2026-07-28.json` — staged registry patch row.
