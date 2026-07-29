# Guardrail — Absorption Docket

**Date:** 2026-07-28
**Source:** KooshaPari/Guardrail (private, source deleted 2026-06-16)
**Target:** `phenotype-tooling/crates/phenotype-resilience/`
**Disposition:** AFFIRM (already absorbed)
**Wave:** 2026-07-28-audit-only
**Decision authority:** registry disposition-index + `projects/Guardrail.json`

## State (as of 2026-07-28)

- **Source repo:** KooshaPari/Guardrail — DELETED from GitHub on 2026-06-16 per `projects/Guardrail.json:11`. No local clone exists; no remote clone possible.
- **Target crate:** `phenotype-tooling/crates/phenotype-resilience/` — **PRESENT** (48K, Cargo.toml + src/).
- **Absorbing commit:** `a298f2355` — *"feat(resilience): add phenotype-resilience workspace crate (#72)"* — captured in `phenotype-tooling` git history.

## Migration works (what was absorbed)

Per the commit message and target crate evidence:

1. **Rate limiting** — token-bucket + sliding-window primitives.
2. **Circuit breaking** — half-open state machine + failure thresholds.
3. **Bulkhead isolation** — semaphore-based concurrency partitioning.
4. Consumed by downstream tooling via `phenotype-resilience` crate name (the legacy `Guardrail` name is gone from the import graph).

## Supersedes chain

```
KooshaPari/Guardrail (private, 2024-2025)
  └─ ABSORBED → phenotype-tooling/crates/phenotype-resilience (PR #72)
       └─ This docket serves as the audit-trail tombstone for Guardrail's GitHub repo.
            └─ Subsequent reference: import as `phenotype_resilience` only.
                 └─ Legacy `Guardrail` name is SUPERSEDED — do not re-introduce.
```

## User Y-approval state

- **Y** received 2026-07-28 (parsed from *"for next 3 Y to all"*).
- **I.2 (target-side tombstone):** PENDING. Requires explicit `Y` to create `archive/` branch on `phenotype-tooling`.

## Open items

- A future pass will add an `archive/2026-07-28-guardrail` branch on `phenotype-tooling` containing a single tombstone commit referencing this docket (pending I.2=Y).
- This docket is the authoritative reference until then.

## Related artifacts

- `phenotype-registry/projects/Guardrail.json:1-12` — source metadata + absorbed_into pointer.
- `phenotype-registry/docs/boundary/phenotype-resilience.md` — boundary intent doc.
- `phenotype-tooling/crates/phenotype-resilience/` — verified target.
- `phenotype-registry/registry/disposition-pending-additions-2026-07-28.json` — staged registry patch row.
