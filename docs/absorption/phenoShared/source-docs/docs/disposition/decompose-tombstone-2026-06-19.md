# phenoShared full decompose — tombstone gut (2026-06-19)

**Branch:** `chore/gut-decompose-tombstone-2026-06-19`  
**ADR:** ADR-ECO-014 (interim staging ONLY — retired)  
**Gate:** `gate-phenoshared` DELETE hold lifted after HexaKit last-pin drain

## Action

Strip all relocated crate source trees from this repo. Retain:

- `README.md` (tombstone notice)
- `TOMBSTONE.md`
- `docs/disposition/*`

No new repos created. Crates absorb into existing DOMAIN_ROLES owners.

## Crate → terminal owner map

| Crate | Terminal owner | Notes |
|-------|----------------|-------|
| `phenotype-error-core` | phenotype-types | Drained HexaKit wave 5b |
| `phenotype-errors` | phenotype-types | Drained HexaKit wave 5b |
| `phenotype-iter` | phenotype-types | HexaKit git pin → main |
| `phenotype-string` | phenotype-types | HexaKit git pin → main |
| `phenotype-validation` | phenotype-types | HexaKit git pin → main |
| `phenotype-time` | phenotype-types | HexaKit git pin → main |
| `phenotype-content-hash` | phenotype-types | Content addressing primitives |
| `phenotype-config-core` | phenotype-config | H14 interim; terminal owner |
| `phenotype-config-loader` | phenotype-config | Wave E absorption |
| `phenotype-http-client-core` | ResilienceKit (phenotype-resilience) | Charter explicit |
| `phenotype-state-machine` | ResilienceKit | Wave 3 drain |
| `phenotype-policy-engine` | ResilienceKit | Wave 3 drain |
| `phenotype-health` | ResilienceKit | Traits crate; PO owns runtime layer |
| `stashly` | ResilienceKit / phenotype-types | ADR-ECO-001 cache canonical |
| `phenotype-retry` | ResilienceKit | Retry policy primitives |
| `phenotype-event-bus` | Eventra | Wave 2; pending Eventra main landing |
| `phenotype-event-sourcing` | Eventra | Wave 2; L5 lifts in progress |
| `phenotype-logging` | PhenoObservability | Wave 3 drain |
| `phenotype-async-traits` | phenotype-rust-sdk | Thin facade |
| `phenotype-macros` | phenotype-rust-sdk | Thin facade |
| `phenotype-contracts` | phenotype-rust-sdk | Generic `Contract` trait |
| `phenotype-security-aggregator` | Authvault | Wave 4 drain |
| `phenotype-secret` | Authvault | Secret-adjacent |
| `phenotype-cache-adapter` | HexaKit stub | Archive-if-unused; see `phenotype-cache-adapter-archive-verdict.md` |
| `phenotype-domain` | — | DDD layer; per-bounded-context SDK |
| `phenotype-application` | — | CQRS layer; per-bounded-context SDK |
| `phenotype-port-interfaces` | HexaKit (reference) | Hexagonal port vocabulary |
| `phenotype-postgres-adapter` | — | Service-local infra |
| `phenotype-redis-adapter` | — | Service-local infra |
| `phenotype-http-adapter` | — | Service-local infra |
| `phenotype-nanovms-client` | — | NanoVMs orchestration; evaluate |
| `phenotype-bid` | — | Orphan; registry backlog |
| `phenotype-build-info` | — | Build metadata; evaluate |
| `phenotype-context` | — | Request context; evaluate |
| `phenotype-rate-limit` | ResilienceKit | Rate limiting |
| `ffi_utils` | — | FFI helpers; evaluate |

## Fleet pin drain status (2026-06-19)

| Consumer | phenoShared pins remaining |
|----------|---------------------------|
| HexaKit | **0** — last pin (`phenotype-cache-adapter`) → inline stub |
| Pyron | `phenotype-contracts`, `stashly` |
| PhenoLang | `phenotype-contracts` |
| PhenoObservability | `phenotype-error-core` |
| phenotype-python-sdk | `phenotype-contracts` |
| ObservabilityKit | `phenotype-health` |
| TestingKit | `phenotype-health` (optional) |

Follow-up lanes required before repo archive/delete.

## Related disposition docs

- [wave-d-stashly-reloc.md](wave-d-stashly-reloc.md)
- [wave-e-absorption.md](wave-e-absorption.md)
- [phenotype-cache-adapter-archive-verdict.md](phenotype-cache-adapter-archive-verdict.md)
