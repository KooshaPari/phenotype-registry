# Gateway Boundary Audit — DELETE gate matrix

> Full DELETE gate for repos in the Gateway & Multi-Repo Merge Rationalization program.  
> Charter: [boundary-shaping.md](../rationalization/boundary-shaping.md) + 5-check gate in [RATIONALIZATION_EXECUTION.md](../../RATIONALIZATION_EXECUTION.md).

## Summary matrix

| Repo | Disposition | Gate | Next step |
|------|-------------|------|-----------|
| agentapi | ABSORB | ✅ archived | Harvest → pointer only |
| agentapi-plusplus | **AFFIRM** cli_proxy | ❌ 34 branches | Wave 15 merge |
| cliproxyapi-plusplus | AFFIRM peer | ❌ 11 branches | Wave 16 |
| bifrost | DYNAMIC-KEEP vendor | ✅ policy | Sync lane only |
| vibeproxy / vibeproxy-monitoring-unified | RETIRE | ✅ | Redirect / stub retire |
| OmniRoute | **AFFIRM** route | ❌ protect | No archive |
| phenotype-omlx | ARCHIVED / FINISH? | 🔶 decision | Wave 17 |
| PhenoCompose | **AFFIRM** platform | ❌ pheno dep | Wave 17b + 18b |
| PhenoRuntime | DELETE | 🔶 harvest | Wave 6 harvest |
| BytePort, Settly, PlatformKit, portage, phenoXddLib | ARCHIVED | ✅ | Wave 18 stubs |
| phenotype-hub, Paginary, acp, thegent-workspace | ARCHIVED/scaffold | ✅/🔶 | Wave 18 |
| pheno | ARCHIVED last | ✅ fleet gate | Wave 18b — org scan clean; `gh repo archive` deferred |
| phenoShared | **DECOMPOSE** | ❌ staging monorepo | ADR-ECO-014 — relocate crates then delete |
| phenotype-e2e-base | ABSORB | 🔶 | Wave 19 → journeys |
| agileplus-spec-harmonizer | AFFIRM tooling | ✅ | Register in map |

## Layer ownership

| Layer | Canonical owners | Never merge |
|-------|------------------|-------------|
| Route / API gateway | OmniRoute, Tokn, agentapi-plusplus | bifrost → OmniRoute |
| Inference runtime | phenotype-omlx (decision), phenoAI consumer | mlx-lm engine into agentapi++ |
| Engine / isolation | nanovms (tooling), PhenoCompose | Into gateway repos |

## Out of scope

- vibeproxy-* reconciliation (user deferral)
- Tracera lane
- FocalPoint vendor, GDK/hwLedger/KaskMan

## pheno fleet blockers (second-order)

**Gate pass (2026-06-18):** org manifest scan — 0 external `KooshaPari/pheno` refs (Tracera exempt per W18b chokepoint). All `pheno_fleet_blockers` in `registry/chokepoints.json` now `verified-clean` or `repointed`. `gh repo archive KooshaPari/pheno` deferred — registry tombstone `projects/pheno.json` + disposition-index `gate-pheno` row (`fsm: archive_pending`).

Repoint strategy (complete): per-crate **DOMAIN_ROLES** owners (`phenotype-config`, `phenotype-resilience`, `PhenoObservability`, `phenotype-types`, `Eventra`); `phenoShared` is interim staging only ([ADR-ECO-014](../adrs/ADR-ECO-014-phenoshared-decompose.md)).
