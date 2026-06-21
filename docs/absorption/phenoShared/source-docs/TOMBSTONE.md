# phenoShared — Tombstone (ADR-ECO-014)

**Status:** DECOMPOSED / INTERIM STAGING RETIRED  
**Date:** 2026-06-19  
**Policy:** [ADR-ECO-014](https://github.com/KooshaPari/phenotype-registry/blob/main/docs/adr/ADR-ECO-014-phenoshared-decompose.md)

`phenoShared` was an interim dynamic-install monorepo for cross-cutting Phenotype
Rust crates. All crate source has been relocated to **DOMAIN_ROLES terminal owners**
or absorbed into existing repos. This repository is retained as a **tombstone** with
disposition pointers only — no publishable workspace remains.

## Do not

- Add new crates here
- Pin new git dependencies to this repo
- Expect `cargo build --workspace` to succeed

## Terminal owners (absorb targets)

| Crate(s) | Terminal owner |
|----------|----------------|
| `phenotype-error-core`, `phenotype-errors`, `phenotype-iter`, `phenotype-string`, `phenotype-validation`, `phenotype-time`, `phenotype-content-hash` | [phenotype-types](https://github.com/KooshaPari/phenotype-types) |
| `phenotype-config-core`, `phenotype-config-loader` | [phenotype-config](https://github.com/KooshaPari/phenotype-config) |
| `phenotype-http-client-core`, `phenotype-state-machine`, `phenotype-policy-engine`, `phenotype-health`, `stashly`, `phenotype-retry` | [phenotype-resilience](https://github.com/KooshaPari/ResilienceKit) |
| `phenotype-event-bus`, `phenotype-event-sourcing` | [Eventra](https://github.com/KooshaPari/Eventra) |
| `phenotype-logging` | [PhenoObservability](https://github.com/KooshaPari/PhenoObservability) |
| `phenotype-async-traits`, `phenotype-macros`, `phenotype-contracts` | [phenotype-rust-sdk](https://github.com/KooshaPari/phenotype-rust-sdk) |
| `phenotype-security-aggregator`, `phenotype-secret` | [Authvault](https://github.com/KooshaPari/Authvault) |
| `phenotype-cache-adapter` | [HexaKit](https://github.com/KooshaPari/HexaKit) inline stub (`crates/phenotype-cache-adapter-stub`) — archive-if-unused |
| `phenotype-domain`, `phenotype-application`, `phenotype-port-interfaces` | Distributed to domain SDKs per bounded context |
| `phenotype-postgres-adapter`, `phenotype-redis-adapter`, `phenotype-http-adapter` | Infrastructure adapters — owner TBD per service repo |
| `phenotype-nanovms-client`, `phenotype-bid`, `phenotype-build-info`, `phenotype-context`, `phenotype-rate-limit`, `ffi_utils` | Orphan / evaluate per registry backlog |

## Optional rename

Consider renaming this repo to `phenoShared-tombstone` after fleet pin drain completes
(registry PR required; do not rename without governance approval).

## Disposition docs

See [`docs/disposition/`](docs/disposition/) for wave-by-wave relocation records.
