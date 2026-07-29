# Servion — Absorption Docket

**Date:** 2026-07-28
**Source:** KooshaPari/Servion (private, source deleted 2026-06-16)
**Target:** `phenotype-tooling/crates/phenotype-service-registry/`
**Disposition:** AFFIRM (already absorbed)
**Wave:** 2026-07-28-audit-only
**Decision authority:** registry disposition-index + `projects/Servion.json`

## State (as of 2026-07-28)

- **Source repo:** KooshaPari/Servion — DELETED from GitHub on 2026-06-16 per `projects/Servion.json:11`. No local clone exists; no remote clone possible (404 on `git ls-remote`).
- **Target crate:** `phenotype-tooling/crates/phenotype-service-registry/` — **PRESENT** (28K, Cargo.toml + src/).
- **Absorbing commit:** `7c5ed3a66` — *"feat(service-registry): add phenotype-service-registry crate (migrated from Servion) (#76)"* — captured in `phenotype-tooling` git history.

## Migration works (what was absorbed)

Per the commit message and target crate evidence:

1. Service registry & discovery core (microservices target registration).
2. Health-check endpoint contract surface.
3. Typed service descriptor interfaces (Rust traits + impls).
4. Consumed by downstream tooling via `phenotype-service-registry` crate name (the legacy `Servion` name is gone from the import graph).

## Supersedes chain

```
KooshaPari/Servion (private, 2024-2025)
  └─ ABSORBED → phenotype-tooling/crates/phenotype-service-registry (PR #76)
       └─ This docket serves as the audit-trail tombstone for Servion's GitHub repo.
            └─ Subsequent reference: import as `phenotype_service_registry` only.
                 └─ Legacy `Servion` name is SUPERSEDED — do not re-introduce.
```

## User Y-approval state

- **Y** received 2026-07-28 (parsed from *"for next 3 Y to all"* = Servion, Guardrail, router-docs).
- **I.2 (target-side tombstone):** PENDING. Requires explicit `Y` to create `archive/` branch on `phenotype-tooling` (= destructive of target branch history per AGENTS.md + user rule: *"approval before the squash to 1 commit and the same per branch which you will treat equal to a delete"*).

## Open items

- A future pass will add an `archive/2026-07-28-servion` branch on `phenotype-tooling` containing a single tombstone commit referencing this docket (pending I.2=Y).
- This docket is the authoritative reference until then.

## Related artifacts

- `phenotype-registry/projects/Servion.json:1-12` — source metadata + absorbed_into pointer.
- `phenotype-tooling/crates/phenotype-service-registry/` — verified target.
- `phenotype-registry/registry/disposition-pending-additions-2026-07-28.json` — staged registry patch row.
