---
repo: "McpKit"
role: deprecated-polyglot-mcp-sdk
status: deprecated
last_boundary_review: 2026-06-18
review_cadence: 30d
in_scope:
  - "Historical McpKit absorption evidence and deletion traceability"
  - "Legacy source-to-target mapping for Python, Rust, Go, registry, and branch-only work"
out_of_scope:
  - "New MCP framework work"
  - "New server implementations"
  - "New polyglot SDK surfaces"
---

# Boundary — McpKit

## In Scope

- **Deletion traceability** for the deprecated `KooshaPari/McpKit` repository.
- **Absorption mapping** for McpKit source surfaces into their canonical homes.
- **Historical branch evidence** until the remaining branch-only deltas are archived or closed.

## Out of Scope

| Not here | Lives in | Reason |
| -------- | -------- | ------ |
| Python FastMCP framework | `KooshaPari/PhenoFastMCP` | Active Python FastMCP fork/base owns tools, resources, prompts, clients, transports, docs, and examples |
| Rust FastMCP framework and macros | `KooshaPari/PhenoFastMCP-rust` | Active Rust fork owns `fastmcp-*` workspace, protocol, server, transport, client, and macro crates |
| Go MCP framework | `KooshaPari/PhenoFastMCP-go` | Active Go fork owns MCP server/client, stdio, HTTP/SSE, tracing, and examples |
| Python `agentmcp` package | `phenotype-python-sdk/packages/agentmcp-hex/` | Extracted SDK package for the Python hexagonal agent edge |
| Rust MCP asset crate | `phenotype-mcp-asset` | Extracted pure Rust asset/pack library |
| Server implementations | `PhenoMCPServers` | Runtime server apps and catalogs live outside the framework repos |
| Ecosystem registry rationale | `phenotype-registry` | This repo preserves the disposition record |

## Boundary Crossings

| Crossing | Direction | Surface | Status |
| -------- | --------- | ------- | ------ |
| Python framework absorption | `McpKit → PhenoFastMCP` | package/docs/examples | green |
| Rust framework absorption | `McpKit → PhenoFastMCP-rust` | Cargo workspace/macros/transport | green |
| Go framework absorption | `McpKit → PhenoFastMCP-go` | Go module/server/client/transports | green |
| Agent package extraction | `McpKit/python/agentmcp → phenotype-python-sdk/packages/agentmcp-hex/` | Python SDK package | amber |
| Asset crate extraction | `McpKit/rust/phenotype-mcp-asset → phenotype-mcp-asset` | Rust crate | green |
| Branch-only cleanup | `origin/chore/1st-hygiene-2026-06-08 → archive/decision` | git branch delta | amber |

## Last Boundary Review

**Date:** 2026-06-18
**Reviewer:** Codex absorption audit continuation
**Worklog / finding:** `findings/2026-06-18-McpKit-source-inventory.md`; `worklogs/L7-003-ecosystem-reconciliation-2026-06-18.json`
**Decisions:**
- McpKit is not an active implementation boundary.
- Deletion status is `DELETE_AFTER_PATCHES`.
- `PhenoFastMCP`, `PhenoFastMCP-rust`, and `PhenoFastMCP-go` were confirmed as local git clones and own the active framework lanes.
- `agentmcp-hex` and `phenotype-mcp-asset` preserve the non-framework extracted surfaces.
- Remaining open work is branch-only cleanup for `origin/chore/1st-hygiene-2026-06-08`.

**Next review:** on final McpKit branch cleanup or 2026-07-18, whichever comes first.
