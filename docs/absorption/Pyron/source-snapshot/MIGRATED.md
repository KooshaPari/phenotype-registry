# MIGRATED — Pyron absorption map

**Date:** 2026-06-19  
**Source repo:** [KooshaPari/Pyron](https://github.com/KooshaPari/Pyron) (tombstone)  
**Policy:** Pyron is not a boundary owner. Consumers must pin canonical repos directly.

## Absorption targets

| Former Pyron path / role | Canonical owner | Install / pin |
|--------------------------|-----------------|---------------|
| Config / `settly`, `Settly/`, `crates/phenotype-config-*` | [phenotype-config](https://github.com/KooshaPari/phenotype-config) | `settly = { git = "https://github.com/KooshaPari/phenotype-config", branch = "main" }` |
| Observability / `tracingkit`, `metrickit`, `logkit`, `Metron/`, `Traceon/` | [PhenoObservability](https://github.com/KooshaPari/PhenoObservability) | Git pin per crate in PhenoObservability workspace |
| Resilience / `stashly`, `Stashly/` | [phenotype-resilience](https://github.com/KooshaPari/phenotype-resilience) (Rust), [phenotype-python-sdk](https://github.com/KooshaPari/phenotype-python-sdk) (Python) | See each repo's README |
| `crates/phenotype-contracts` (vendored + generic traits) | [phenotype-rust-sdk](https://github.com/KooshaPari/phenotype-rust-sdk) | Domain-specific: [Authvault](https://github.com/KooshaPari/Authvault), [Eventra](https://github.com/KooshaPari/Eventra), [Agentora](https://github.com/KooshaPari/Agentora) contract crates |
| `python/pheno-mcp`, `crates/phenotype-mcp` | [PhenoMCP](https://github.com/KooshaPari/PhenoMCP) (Python), [substrate](https://github.com/KooshaPari/substrate) `crates/phenotype-mcp` (Rust) | `pip install git+https://github.com/KooshaPari/PhenoMCP.git` |
| Python middleware (`phenotype-middleware-py/`) | Absorbed into domain SDKs — see [phenotype-python-sdk](https://github.com/KooshaPari/phenotype-python-sdk) | No Pyron path dependency |

## Removed dependency classes

The tombstone workspace intentionally has **no** `Cargo.toml`, **no** `pyproject.toml`, and **no** git pins to:

- `KooshaPari/phenoShared`
- `KooshaPari/phenotype-monorepo` (or legacy monorepo paths)
- Any interim staging repo

## Historical waves (pre-gut)

| Wave | Change | PR |
|------|--------|-----|
| Wave 2–7 | Repoint settly, logkit, stashly, domain git pins | #52–#55 |
| Wave 13 | Exclude test crates; pin test-infra → TestingKit | #56 |
| Wave F | pheno-mcp redirect manifest | #58 |
| P4 | phenotype-contracts decompose; drop vendored trees | #61 |
| Gut | Full tombstone (this commit) | TBD |

## For agents

Do not rebuild infrastructure in Pyron. Update fleet pins to canonical owners above, then delete any remaining `KooshaPari/Pyron` git dependencies.
