---
repo: "agentmcp-hex"
role: SDK
status: active
last_boundary_review: 2026-06-18
review_cadence: 30d
adr_023_substrate: "phenotype-*-sdk"
origin: "KooshaPari/McpKit/python/agentmcp/ (McpKit archived 2026-06-17 per ADR-017)"
extracted_on: "2026-06-18"
disposition_row_id: 54
package_path: "phenotype-python-sdk/packages/agentmcp-hex/"
version: "0.3.0"
in_scope:
  - "Hexagonal DDD agent framework (agents, policies, ports, adapters, value objects)"
  - "Stable Python import surface published under phenotype-python-sdk namespace"
  - "Test suite compatibility with the original McpKit/python/agentmcp/ tests"
  - "Re-export of PhenoFastMCP framework primitives for the Python edge"
out_of_scope:
  - "MCP transport implementation — lives in PhenoFastMCP (the framework) and PhenoMCPServers (the implementations)"
  - "FastMCP server registration — lives in PhenoFastMCP"
  - "Skill execution / runtime — lives in PhenoMCPServers"
  - "Rust agent runtime — lives in KooshaPari/Agentora (this is the Python edge of the same pattern)"
  - "Cross-language polyglot facade (Rust ↔ Python) — lives in phenotype-hub if/when needed"
---

# Boundary — agentmcp-hex

## In Scope

- **Hexagonal DDD agent framework**: `Agent` aggregate, `Policy` value objects, `Port` interfaces, `Adapter` implementations.
- **Domain events**: `AgentCreated`, `PolicyViolated`, `ToolInvoked` (in-memory; no broker).
- **Stable Python API**: importable as `from phenotype_python_sdk.agentmcp_hex import Agent, Policy, Port, Adapter` (or the package's final distribution name — pending PR `phenotype-python-sdk#21` review).
- **Test parity**: original `McpKit/python/agentmcp/tests/` test suite passes against the new home unchanged (or with a thin re-export layer).
- **Re-export of framework primitives**: convenience re-exports of `PhenoFastMCP` MCP primitives for the Python edge.

## Out of Scope

| Not here | Lives in | Reason |
| -------- | -------- | ------ |
| MCP transport (HTTP/SSE/stdio) | `PhenoFastMCP` | This package is transport-agnostic; the framework owns transport |
| FastMCP server registration | `PhenoFastMCP` | Framework concern, not agent concern |
| Skill execution runtime | `PhenoMCPServers` | Deployable server implementations |
| Rust agent runtime | `KooshaPari/Agentora` | Rust edge; this is the Python edge of the same pattern |
| Cross-language polyglot facade | `phenotype-hub` (future) | Not yet needed; deferred per ADR-023 |
| The other McpKit Python packages | `phenotype-python-sdk/packages/*` | Per McpKit absorption audit, sibling Python packages absorbed to phenotype-python-sdk |

## Boundary Crossings

| Crossing | Direction | Surface | Status |
| -------- | --------- | ------- | ------ |
| Agent API | consumer → `agentmcp-hex` | Python import (`phenotype_python_sdk.agentmcp_hex.Agent`) | amber — pending PR `phenotype-python-sdk#21` merge |
| Framework re-exports | `agentmcp-hex` → `PhenoFastMCP` | Python import (re-export) | green |
| Migration from McpKit | `McpKit (archived) → agentmcp-hex` | n/a (one-shot extraction) | green |
| Provenance | `agentmcp-hex` → `McpKit/python/agentmcp/` | n/a (documented in `docs/intent/`) | green |
| Test suite | test runner → `agentmcp-hex` | pytest | amber — port-in-progress |

## Last Boundary Review

**Date:** 2026-06-18
**Reviewer:** forge subagent (L7-003 reconciliation + McpKit absorption audit)
**Worklog / finding:** `worklogs/L7-003-ecosystem-reconciliation-2026-06-18.json`; `findings/2026-06-18-McpKit-source-inventory.md`
**Decisions:**
- New canonical home for the Python agentmcp package, extracted from McpKit.
- ADR-023 classification: `phenotype-*-sdk` (cross-language SDK; polyglot facade).
- fsm=open: awaiting PR `phenotype-python-sdk#21` review; amber status on API and test crossings.
- 30-day review cadence; align with L7-001 sweep rhythm; final disposition on PR merge.

**Next review:** 2026-07-18 (or on PR `phenotype-python-sdk#21` merge, whichever is first)
