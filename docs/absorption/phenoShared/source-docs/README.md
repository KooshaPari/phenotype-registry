# phenoShared — Tombstone

[![Status](https://img.shields.io/badge/status-DECOMPOSED-red?style=flat-square)](TOMBSTONE.md)
[![ADR](https://img.shields.io/badge/ADR-ECO--014-orange?style=flat-square)](https://github.com/KooshaPari/phenotype-registry/blob/main/docs/adr/ADR-ECO-014-phenoshared-decompose.md)

> **This repository is retired.** phenoShared was interim staging only (ADR-ECO-014).
> All crate source has been relocated to DOMAIN_ROLES terminal owners. See
> [TOMBSTONE.md](TOMBSTONE.md) and [docs/disposition/](docs/disposition/) for pointers.

## What happened

1. Cross-cutting Rust crates were temporarily consolidated here during the HexaKit
   workspace dissolution (waves 7–13).
2. Each crate was absorbed into an existing terminal owner — no new repos were created.
3. The last fleet git pin (`phenotype-cache-adapter` in HexaKit) was drained to an
   inline stub on 2026-06-19.
4. Source trees were removed; this repo now serves as a disposition tombstone.

## Where to find crates now

| Need | Go to |
|------|-------|
| Error types, string/iter/validation utils | [phenotype-types](https://github.com/KooshaPari/phenotype-types) |
| Config loading | [phenotype-config](https://github.com/KooshaPari/phenotype-config) |
| HTTP client, policy, state machine, health, retry | [ResilienceKit](https://github.com/KooshaPari/ResilienceKit) |
| Event bus / event sourcing | [Eventra](https://github.com/KooshaPari/Eventra) |
| Logging / observability | [PhenoObservability](https://github.com/KooshaPari/PhenoObservability) |
| Async traits, macros, contracts | [phenotype-rust-sdk](https://github.com/KooshaPari/phenotype-rust-sdk) |
| Auth / security | [Authvault](https://github.com/KooshaPari/Authvault) |
| Cache adapter stub | [HexaKit](https://github.com/KooshaPari/HexaKit) `crates/phenotype-cache-adapter-stub` |

## Optional rename

A follow-up registry PR may rename this repo to `phenoShared-tombstone`. Do not
rename without governance approval.

MIT
