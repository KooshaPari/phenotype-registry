---
repo: "agentmcp-hex"
aliases:
  - "agentmcp"
  - "mcpkit-python-agentmcp"
role: SDK
status: active
last_verified: 2026-06-18
bound_prompts: 0
bound_plans: 0
bound_responses: 0
device: macbook
adr_023_substrate: "phenotype-*-sdk"
origin: "KooshaPari/McpKit/python/agentmcp/ (McpKit archived 2026-06-17 per ADR-017)"
extracted_on: "2026-06-18"
disposition_row_id: 54
disposition_wave: "McpKit-Absorption-2026-06-18"
source_pr: "KooshaPari/phenotype-python-sdk#21 (OPEN, awaiting review)"
package_path: "phenotype-python-sdk/packages/agentmcp-hex/"
version: "0.3.0"
supersedes:
  - "KooshaPari/McpKit/python/agentmcp/"
---

# Intent — agentmcp-hex

## Intent Statement

`agentmcp-hex` is the Python SDK package extracted from the now-archived `KooshaPari/McpKit/python/agentmcp/` crate on 2026-06-18 and absorbed into `phenotype-python-sdk` as `phenotype-python-sdk/packages/agentmcp-hex/`. It provides a hexagonal Domain-Driven Design (DDD) agent framework — agents, policies, ports, adapters, value objects — and is published under the `phenotype-python-sdk` namespace for fleet-wide consumption. Per ADR-023, this is a `phenotype-*-sdk` (cross-language SDK; stable public API; polyglot facade). The boundary of "done" is: a published PyPI package importable as `phenotype_python_sdk.agentmcp_hex` (or the package's chosen distribution name), with the hexagonal DDD pattern preserved end-to-end, and the original `McpKit/python/agentmcp/` test suite passing against the new home. P1 patch from the McpKit absorption audit. Currently awaiting PR `phenotype-python-sdk#21` review (fsm=open per `registry/disposition-index.json` row 54).

## Bound Prompts

| Date | Source | File | Tag |
| ---- | ------ | ---- | --- |
| ?    | —      | —    | —   |

(No curated prompts are bound to this package yet. The original 21 prompts that bound to `McpKit` are listed in `docs/intent/AgentMCP.md` and remain re-attributed to `PhenoFastMCP` per ADR-017; this new SDK package starts with zero bound prompts.)

## Bound Plans

| Date | Source | File | Status | Outcome |
| ---- | ------ | ---- | ------ | ------- |
| 2026-06-18 | forge subagent (L5-110.x) | `findings/2026-06-18-McpKit-source-inventory.md` | open | P1 patch in flight; PR `phenotype-python-sdk#21` awaiting review |

## Bound Responses (specs, ideas, plans from agents)

| Date | Source | File | Kind | Outcome |
| ---- | ------ | ---- | ---- | ------- |
| 2026-06-18 | forge subagent | `findings/2026-06-18-McpKit-source-inventory.md` | audit | McpKit absorption audit — P1 extraction row for `python/agentmcp` |

## Boundary

See: [`docs/boundary/agentmcp-hex.md`](../boundary/agentmcp-hex.md)

## Ecosystem Role

`SDK` per `ECOSYSTEM_MAP.md` §1 (`phenotype-*-sdk` per ADR-023 substrate placement). **Consumers:** `PhenoFastMCP` (the framework that documents the supersession path; absorbs the Py edge of the MCP layer). **Cross-references:** the deprecated source `KooshaPari/McpKit/python/agentmcp/` (archived 2026-06-18 per ADR-017), the SDK parent `KooshaPari/phenotype-python-sdk`, and the framework sibling `PhenoFastMCP`.

## Open Questions

- Awaiting PR `phenotype-python-sdk#21` review and merge; package not yet published to PyPI.
- Distribution name (`phenotype-python-sdk` namespace vs. standalone) — final call pending SDK maintainers.

## Change Log

| Date | Change | Worklog |
| ---- | ------ | ------- |
| 2026-06-18 | Initial extraction (L7-001 reconciliation; new package registered under docs/intent/ structure) | `worklogs/L7-003-ecosystem-reconciliation-2026-06-18.json` |
| 2026-06-18 | Disposition row 54 added to `registry/disposition-index.json` (ABSORB, fsm=open) | commit `578af944` |
