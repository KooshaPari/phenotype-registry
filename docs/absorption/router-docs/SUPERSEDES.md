# router-docs — Absorption Docket

**Date:** 2026-07-28
**Source:** KooshaPari/router-docs (private, source deleted 2026-06-16)
**Target:** `OmniRoute/docs/research/archive/router-docs/`
**Disposition:** AFFIRM (already absorbed)
**Wave:** 2026-07-28-audit-only
**Decision authority:** registry disposition-index + `projects/router-docs.json`

## State (as of 2026-07-28)

- **Source repo:** KooshaPari/router-docs — DELETED from GitHub on 2026-06-16 per `projects/router-docs.json:11`. No local clone exists; no remote clone possible.
- **Target dir:** `OmniRoute/docs/research/archive/router-docs/` — **PRESENT** (172B README + `reference/` + `research/`).
- **Absorbing commit:** `f2b8b3638` — *"docs(archive): absorb router-docs research corpus from archive"* — captured in `OmniRoute` git history. Followed by cleanup commit `1893b92f4`.

## Migration works (what was absorbed)

Per the commit message and target dir evidence:

1. **Router protocol research corpus** — 33 reference files + 10 research entries moved into `OmniRoute/docs/research/archive/router-docs/`.
2. **Routing-decision studies** — pre-ADR-050/051 background notes on Pareto routing, hysteresis, hash-chain benches.
3. **Historical router-design alternatives** — material that informed `OmniRoute`'s routing-decision evolution.

## Supersedes chain

```
KooshaPari/router-docs (private, 2025)
  └─ ABSORBED → OmniRoute/docs/research/archive/router-docs/ (commit f2b8b3638)
       └─ This docket serves as the audit-trail tombstone for router-docs's GitHub repo.
            └─ Subsequent reference: cite `OmniRoute/docs/research/archive/router-docs/` only.
                 └─ Legacy `router-docs` name is SUPERSEDED — do not re-introduce.
```

## User Y-approval state

- **Y** received 2026-07-28 (parsed from *"for next 3 Y to all"*).
- **I.2 (target-side tombstone):** PENDING. Requires explicit `Y` to create `archive/` branch on `OmniRoute`.

## Open items

- A future pass will add an `archive/2026-07-28-router-docs` branch on `OmniRoute` containing a single tombstone commit referencing this docket (pending I.2=Y).
- This docket is the authoritative reference until then.

## Related artifacts

- `phenotype-registry/projects/router-docs.json:1-12` — source metadata + absorbed_into pointer.
- `OmniRoute/docs/research/archive/router-docs/README.md` — target README.
- `phenotype-registry/registry/disposition-pending-additions-2026-07-28.json` — staged registry patch row.
