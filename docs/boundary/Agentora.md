---
repo: "Agentora"
role: agent-runtime
status: active
last_boundary_review: 2026-06-18
review_cadence: 90d
adr_023_substrate: "phenotype-*-framework"
origin: "KooshaPari/McpKit/rust/agentora/ (stale snapshot, McpKit archived 2026-06-17 per ADR-017)"
canonical: "KooshaPari/Agentora"
canonical_status: "pre-existing, 47 crates"
disposition_row_id: 53
disposition_value: "DOCUMENT"
in_scope:
  - "Rust agent runtime framework (47 crates, hexagonal architecture)"
  - "Skills, tools, memory, event subsystems for agent execution"
  - "Provenance attribution to McpKit/rust/agentora/ via ORIGIN.md (Agentora#89)"
  - "Pre-existing canonical home — no code migration from McpKit"
out_of_scope:
  - "Python agent runtime — lives in KooshaPari/thegent"
  - "MCP transport — lives in PhenoMCPServers, PhenoFastMCP, substrate"
  - "Stale McpKit/rust/agentora/ subdirectory — subsumed; no reactivation"
  - "PhenoAgent stub — pending merge into Agentora (separate track)"
---

# Boundary — Agentora

## In Scope

- **Canonical Rust agent framework**: 47-crate Rust workspace at `KooshaPari/Agentora`.
- **Hexagonal architecture**: agents (aggregates), policies (value objects), ports (interfaces), adapters (impls), events.
- **Skill/tool/memory/event subsystems**: the four pillars of the agent runtime.
- **Provenance attribution to McpKit**: `ORIGIN.md` (added via `Agentora#89`, MERGED 2026-06-19) documents the historical relationship to the now-archived `McpKit/rust/agentora/` subdirectory.
- **Pre-existing canonical home**: this is the **canonical** Agentora repo; no code extraction or migration is needed.

## Out of Scope

| Not here | Lives in | Reason |
| -------- | -------- | ------ |
| Python agent runtime | `KooshaPari/thegent` | Different language edge; thegent is the Python facade |
| MCP transport (HTTP/SSE/stdio) | `PhenoMCPServers`, `PhenoFastMCP*`, `substrate` | MCP is a separate concern; agent runtime is transport-agnostic |
| FastMCP framework primitives | `PhenoFastMCP` (py/go/rust) | Different framework, different layer |
| Stale McpKit/rust/agentora/ subdir | (subsumed) | 1 crate, 13 commits; canonical Agentora (47 crates) subsumes it; McpKit archived |
| `PhenoAgent` stub | (pending merge into Agentora) | Empty manifest; future track, not this disposition |
| `KooshaPari/Agentora-2nd` worktree | (supersession) | Pre-existing worktree; canonical is `KooshaPari/Agentora` main |

## Boundary Crossings

| Crossing | Direction | Surface | Status |
| -------- | --------- | ------- | ------ |
| Skill API | consumer crate → `Agentora` | Rust API (`agentora::skill::Skill`) | green |
| Tool API | consumer crate → `Agentora` | Rust API (`agentora::tool::Tool`) | green |
| Memory API | consumer crate → `Agentora` | Rust API (`agentora::memory::Memory`) | green |
| Event bus | consumer crate → `Agentora` | Rust API (`agentora::event::EventBus`) | green |
| Migration from McpKit | `McpKit (archived) → Agentora` | n/a (one-shot provenance attribution only) | green |
| Provenance | `Agentora → McpKit` | `ORIGIN.md` (Agentora#89) | green |
| PhenoAgent stub merge | `PhenoAgent → Agentora` | n/a (future track) | red (pending) |

## Last Boundary Review

**Date:** 2026-06-18
**Reviewer:** forge subagent (L7-003 reconciliation + McpKit absorption audit)
**Worklog / finding:** `worklogs/L7-003-ecosystem-reconciliation-2026-06-18.json`; `findings/2026-06-18-McpKit-source-inventory.md`
**Decisions:**
- Disposition = `DOCUMENT` (new value: existing target repo, no code extraction, provenance attribution only).
- ADR-023 classification: `phenotype-*-framework` (inversion-of-control framework; opinionated lifecycle, ports, adapters, conventions).
- Provenance attribution via `ORIGIN.md` (Agentora#89 MERGED 2026-06-19) is the terminal action.
- 90-day review cadence (canonical repo, stable; next review 2026-09-16).

**Next review:** 2026-09-16
