# Pyron — Tombstone (absorbed 2026-06-19)

> **Status:** GUT / TOMBSTONE — this repository no longer owns Phenotype infrastructure boundaries.
> All absorbed capabilities live in canonical domain-role repos listed in [MIGRATED.md](./MIGRATED.md).

Pyron was the Phenotype organizational shelf / infrastructure kit. Its contents were decomposed per
[ADR-029](https://github.com/KooshaPari/phenotype-monorepo-state/blob/main/docs/adr/2026-06-15/ADR-029-dmouse92-to-kooshapari.md)
and [ADR-ECO-014](https://github.com/KooshaPari/phenotype-registry/blob/main/docs/adr/ADR-ECO-014-phenoshared-decompose.md).

**Do not add dependencies on this repo.** Use the absorption targets below.

| Need | Go to |
|------|-------|
| Config / settly | [phenotype-config](https://github.com/KooshaPari/phenotype-config) |
| Observability (tracing, metrics, logging) | [PhenoObservability](https://github.com/KooshaPari/PhenoObservability) |
| Resilience / stashly | [phenotype-resilience](https://github.com/KooshaPari/phenotype-resilience) · [phenotype-python-sdk](https://github.com/KooshaPari/phenotype-python-sdk) |
| Shared Rust contracts | [phenotype-rust-sdk](https://github.com/KooshaPari/phenotype-rust-sdk) (+ domain slices in Authvault / Eventra / Agentora) |
| MCP (Python + Rust runtime) | [PhenoMCP](https://github.com/KooshaPari/PhenoMCP) · [substrate](https://github.com/KooshaPari/substrate) (`crates/phenotype-mcp`) |

See [TOMBSTONE.md](./TOMBSTONE.md) for disposition details and [MIGRATED.md](./MIGRATED.md) for the full redirect map.
