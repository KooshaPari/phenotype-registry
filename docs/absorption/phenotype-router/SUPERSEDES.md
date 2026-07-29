# ABSORPTION DOCKET — `phenotype-router` → `Agentora/crates/bifrost-routing`

## State

| field | value |
|-------|-------|
| source | `KooshaPari/phenotype-router` (Public, Rust, Jun 21) |
| target | `Agentora/crates/bifrost-routing` (verified, exists locally) |
| classification | `B:WORKING` (134KB Rust decision layer per ADR-050/051) |
| status | `REDIRECT_TO_BIFROST` |
| archive decision | SUPERSEDE was **recanted** 2026-07-18 (per disposition-index AUDIT-RECIND) |
| deprecated date | 2026-07-28 (replaced by bifrost-routing redirect) |

## Migration works

`phenotype-router` (134KB Rust decision-layer lib per ADR-050/051) is being
redirected to `Agentora/crates/bifrost-routing` per user choice 2026-07-28.

### Why bifrost-routing

User feedback 2026-07-28: *"router no other target e.g. bifrsost or another"*

`Agentora/crates/bifrost-routing` meets the criteria:
- **Rust** edition=2021, MIT/Apache-2.0
- **Bifrost transport** notation per ADR-050 (pairs with Phenotype decision layer)
- **Exists locally** with `Cargo.toml` + `src/` (error.rs, lib.rs, models.rs, routers.rs)
- **Canonical home** for the Phenotype router decision layer

### Decision-layer pair (phenotype-router spec + bifrost-routing)

- `phenotype-router-spec` (the 25KB JSON-schema spec) → `phenotype-registry/docs/specs/router-protocol/`
  (SPINE absorbed, GH-deleted 2026-07-18)
- `phenotype-router` (the 134KB Rust runtime) → `Agentora/crates/bifrost-routing`
  (REDIRECT, this docket)

### What was done

1. Verified `Agentora/crates/bifrost-routing` exists locally with Cargo.toml + src/.
2. Updated registry row `AUTO-IMPORT-phenotype-router` to redirect target.
3. Created this docket.
4. Registry re-frozen at v1.6.82 (2026-07-28).

### What was NOT done

- No code merge (decision layer is independent; bifrost-routing lib has its own
  models/routers/error).
- No source-side squash on `phenotype-router` (no local clone; GH-archived).
- No `archive/` branch on `Agentora/` for phenotype-router (target is new home).

## Supersedes chain

| from | to | reason |
|------|----|--------|
| `phenotype-router` (134KB Rust decision layer) | `Agentora/crates/bifrost-routing` | user-directed 2026-07-28; ADR-050 Bifrost transport home for Phenotype decision layer |
| `phenotype-router` SUPERSEDE (recanted 2026-07-18) | source re-classified as B:WORKING | AUDIT-RECIND 2026-07-18 explicitly recanted the prior SUPERSEDE-was-WRONG note |

## User decision (2026-07-28)

> *"router no other target e.g. bifrsost or another"*

Captured in registry row `AUTO-IMPORT-phenotype-router.note` (2026-07-28 addendum).

## Open items

1. `phenotype-router` GH repo is archived — no local clone to deep-scan.
2. If future Bifrost-core enhancements pull from `phenotype-router`, the redirect
   should be revisited (currently the target lib is small and serves as a stub).
