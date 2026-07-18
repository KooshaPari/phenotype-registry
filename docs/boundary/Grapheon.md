# Boundary — Grapheon

> Canonical Grapheon graph server runtime. Boundary file created
> 2026-07-17 during registry batch4 refresh.

## In Scope

- **Graph server runtime** — claims/evidence graph store with HTTP
  transport layer.
- **Persistence adapters** — pluggable backends (MemoryPort trait
  integration via thegent-memory for episodic memory, optional
  Postgres/SQLite bindings).
- **HTTP server** — accepts REST requests at `/intents`, `/claims`,
  `/evidence`, `/graph` paths; returns JSON.
- **CLI** — `grapheon-server` and `grapheon-admin` binaries.

## Out of Scope

| Not here | Lives in | Reason |
| -------- | -------- | ------ |
| FFI consumer bindings | `pheno-cdylib-bridge` (in `pheno` monorepo) | Rust↔Go C-ABI surface |
| Go HTTP client | `phenotype-go-sdk/packages/graphclient` | SDK wrapper, not server |
| AI agent runtime | `thegent` | Grapheon is a data layer; thegent orchestrates agents |
| Auth | `Authvault` (AuthKit absorbed) | Tokens & vault surface |

## Boundary Crossings

| Crossing | Direction | Surface | Status |
| -------- | --------- | ------- | ------ |
| MemoryProvider | Grapheon → thegent-memory | Trait impl | green |
| HTTP /intents | Clients → Grapheon | REST JSON | green |
| MCP server | `PhenoMCPServers` → Grapheon | MCP protocol | amber (gate review pending) |
| FFI | `pheno-cdylib-bridge` → Grapheon | `extern "C"` shim | green |

## Last Boundary Review

**Date:** 2026-07-17
**Reviewer:** registry batch4 audit (queue-refresh-batch4)
**Disposition-index row:** DSPI-NEW (`repo-Grapheon`, fsm=queued)
**Decisions:**
- ABSORB target: `pheno` monorepo `crates/grapheon/` per registry
  batch4 row.
- Separate from `grapheon-bindings` (Go HTTP client; absorbed 2026-07-17
  into `phenotype-go-sdk/packages/graphclient`).

**Next review:** on absorption completion
