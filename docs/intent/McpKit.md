---
repo: "McpKit"
aliases: []
role: deprecated-polyglot-mcp-sdk
status: deprecated
last_verified: 2026-06-18
bound_prompts: 8
bound_plans: 0
bound_responses: 0
device: macbook
---

# Intent — McpKit

## Intent Statement

McpKit was the legacy polyglot MCP SDK/framework container for the Phenotype ecosystem. It is no longer an active implementation repo. Its durable intent is preserved as absorption evidence while the actual framework and package surfaces move to narrower canonical homes.

Deletion recommendation: `DELETE`. The active targets are `PhenoFastMCP` for Python FastMCP framework work, `PhenoFastMCP-rust` for Rust framework/macros/transport, `PhenoFastMCP-go` for Go server/client framework work, `phenotype-python-sdk/packages/agentmcp-hex/` for the Python agent edge, `phenotype-mcp-asset` for the Rust asset-pack crate, and `PhenoMCPServers` for server implementations. The remaining branch-only McpKit delta was reviewed and is archive-only.

## Bound Prompts

| Date | Source | File | Tag |
| ---- | ------ | ---- | --- |
| ? | claude-code | `docs/curated-prompts/claude-code/unknown/5dc22f7cd6007471.md` | narrative |
| ? | claude-code | `docs/curated-prompts/claude-code/unknown/e4c1b5e6a5354ed0.md` | policy-setting |
| ? | claude-code | `docs/curated-prompts/claude-code/unknown/273eb955eda1d8dc.md` | bugfix |
| ? | claude-code | `docs/curated-prompts/claude-code/unknown/87dc15ca14fc009c.md` | bugfix |
| ? | claude-code | `docs/curated-prompts/claude-code/unknown/0e45ba6005919332.md` | narrative |
| ? | claude-code | `docs/curated-prompts/claude-code/unknown/4aac4fb3a706acde.md` | bugfix |
| ? | claude-code | `docs/curated-prompts/claude-code/unknown/f2cacf17cf9bed5e.md` | narrative |
| ? | claude-code | `docs/curated-prompts/claude-code/unknown/633349ece571427a.md` | narrative |

## Bound Plans

| Date | Source | File | Status |
| ---- | ------ | ---- | ------ |

## Bound Responses (specs, ideas, plans from agents)

| Date | Source | File | Kind |
| ---- | ------ | ---- | ---- |

## Boundary

See: [`docs/boundary/McpKit.md`](../boundary/McpKit.md)

## Ecosystem Role

Deprecated source repo; registry role is deletion traceability only.

## Open Questions

- None for active implementation. Optional administrative cleanup: archive/delete McpKit and stale branches after registry changes are committed.

## Change Log

| Date | Change | Worklog |
| ---- | ------ | ------- |
| 2026-06-17 | Initial binding (L7-001 sweep) | `worklogs/L7-001-intent-boundary-curation-2026-06-17.json` |
| 2026-06-18 | McpKit absorption targets verified; role changed to deprecated deletion-traceability source | `worklogs/L7-003-ecosystem-reconciliation-2026-06-18.json` |
| 2026-06-18 | Branch-only delta reviewed; `origin/chore/1st-hygiene-2026-06-08` classified archive-only; recommendation upgraded to `DELETE` | `worklogs/L7-003-ecosystem-reconciliation-2026-06-18.json` |
