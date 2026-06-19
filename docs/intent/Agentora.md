---
repo: "Agentora"
aliases: []
role: agent-runtime
status: active
last_verified: 2026-06-18
bound_prompts: 11
bound_plans: 0
bound_responses: 0
device: macbook
adr_023_substrate: "phenotype-*-framework"
origin: "KooshaPari/McpKit/rust/agentora/ (stale snapshot, McpKit archived 2026-06-17 per ADR-017)"
canonical: "KooshaPari/Agentora"
canonical_status: "pre-existing, 47 crates"
disposition_row_id: 53
disposition_wave: "McpKit-Absorption-2026-06-18"
disposition_value: "DOCUMENT"
source_pr: "KooshaPari/Agentora#89 (MERGED 2026-06-19 00:10:54 UTC; added ORIGIN.md)"
---

# Intent — Agentora

## Intent Statement

`Agentora` is the canonical agent framework for the KooshaPari fleet — a 47-crate Rust workspace implementing a hexagonal-architecture agent runtime (skills, tools, memory, events). It is the **canonical** home for Rust agent work and is listed under `agent-runtime` + `product/app` in `ECOSYSTEM_MAP.md` §1. The `McpKit/rust/agentora/` subdirectory was a **stale snapshot** (1 crate, 13 commits) of Agentora, and is **subsumed** by the canonical `KooshaPari/Agentora` repo — no code migration is needed. Per ADR-017, the only artifact required is provenance attribution, which was added as `ORIGIN.md` via PR `KooshaPari/Agentora#89` (MERGED 2026-06-19 00:10:54 UTC). The disposition is `DOCUMENT` — a new disposition value meaning "existing target repo, no code extraction, just provenance attribution". This intent file supersedes the L7-001 stub (which listed 11 historical bound prompts but no extraction provenance); the bound-prompt list remains unchanged.

## Bound Prompts

| Date | Source | File | Tag |
| ---- | ------ | ---- | --- |
| ? | claude-code | `docs/curated-prompts/claude-code/unknown/448ace8bf2346324.md` | narrative |
| ? | claude-code | `docs/curated-prompts/claude-code/unknown/6ff3acf070989faf.md` | policy-setting |
| ? | claude-code | `docs/curated-prompts/claude-code/unknown/d86bb9895691eabd.md` | policy-setting |
| ? | claude-code | `docs/curated-prompts/claude-code/unknown/168185ba08461766.md` | bugfix |
| ? | claude-code | `docs/curated-prompts/claude-code/unknown/40e89ff68e353ce9.md` | narrative |
| ? | claude-code | `docs/curated-prompts/claude-code/unknown/f109012456bbc4a3.md` | repo-defining |
| ? | claude-code | `docs/curated-prompts/claude-code/unknown/2f021e96fd12bc0b.md` | policy-setting |
| ? | claude-code | `docs/curated-prompts/claude-code/unknown/14c8f4543269c5ba.md` | implementation |
| ? | claude-code | `docs/curated-prompts/claude-code/unknown/6f5c2612882fc1a9.md` | repo-defining |
| ? | claude-code | `docs/curated-prompts/claude-code/unknown/d03d7f2da9f21c77.md` | narrative |
| ? | claude-code | `docs/curated-prompts/claude-code/unknown/026518921e127850.md` | narrative |

## Bound Plans

| Date | Source | File | Status | Outcome |
| ---- | ------ | ---- | ------ | ------- |
| 2026-06-19 | forge subagent (L5-110.x) | `findings/2026-06-18-McpKit-source-inventory.md` | done | Provenance attribution via ORIGIN.md (Agentora#89); no code migration |

## Bound Responses (specs, ideas, plans from agents)

| Date | Source | File | Kind | Outcome |
| ---- | ------ | ---- | ---- | ------- |
| 2026-06-18 | forge subagent | `findings/2026-06-18-McpKit-source-inventory.md` | audit | McpKit absorption audit — identified `rust/agentora` as a stale snapshot of canonical Agentora; DOCUMENT disposition |

## Boundary

See: [`docs/boundary/Agentora.md`](../boundary/Agentora.md)

## Ecosystem Role

`agent-runtime` (and `product/app`) per `ECOSYSTEM_MAP.md` §1 (`phenotype-*-framework` per ADR-023 substrate placement). **Canonical home** for Rust agent runtime work. **Cross-references:** the deprecated source `KooshaPari/McpKit/rust/agentora/` (stale snapshot, archived 2026-06-18 per ADR-017), the absorbed `KooshaPari/PhenoProc` (per Agentora#79), and the stub `KooshaPari/PhenoAgent` (pending merge into Agentora).

## Open Questions

- None — `DOCUMENT` disposition is terminal; provenance attribution via `ORIGIN.md` is the final action.

## Change Log

| Date | Change | Worklog |
| ---- | ------ | ------- |
| 2026-06-17 | Initial binding (L7-001 sweep) | `worklogs/L7-001-intent-boundary-curation-2026-06-17.json` |
| 2026-06-18 | Disposition row 53 added to `registry/disposition-index.json` (DOCUMENT, fsm=done) | commit `578af944` |
| 2026-06-19 | Provenance attribution via ORIGIN.md (Agentora#89 MERGED) | `findings/2026-06-18-McpKit-source-inventory.md` |
| 2026-06-18 | Stub upgraded with McpKit extraction provenance (L7-003 reconciliation; new docs/intent/ structure) | `worklogs/L7-003-ecosystem-reconciliation-2026-06-18.json` |
