---
repo: "phenotype-mcp-asset"
aliases:
  - "mcp-asset"
role: shared-lib
status: active
last_verified: 2026-06-18
bound_prompts: 0
bound_plans: 0
bound_responses: 0
device: macbook
adr_023_substrate: "pheno-*-lib"
origin: "KooshaPari/McpKit/rust/phenotype-mcp-asset/ v0.2.0 (McpKit archived 2026-06-17 per ADR-017)"
extracted_on: "2026-06-18"
disposition_row_id: 52
disposition_wave: "McpKit-Absorption-2026-06-18"
source_pr: "new repo (KooshaPari/phenotype-mcp-asset created 2026-06-18 12:17 UTC)"
consumers:
  - "PhenoMCPServers"
supersedes:
  - "KooshaPari/McpKit/rust/phenotype-mcp-asset"
---

# Intent — phenotype-mcp-asset

## Intent Statement

`phenotype-mcp-asset` is the canonical fleet lib for the Phenotype-pack asset handler used by MCP servers. It was extracted from the now-archived `KooshaPari/McpKit/rust/phenotype-mcp-asset/` crate (v0.2.0) on 2026-06-18 as a standalone Rust library at v0.3.0. The crate is consumed by `PhenoMCPServers` (the registry entry for deployable MCP server implementations) to bundle, validate, and load Phenotype-pack assets (skill manifests, plugin descriptors, agent role cards). Per ADR-023, this is a `pheno-*-lib` (pure reusable library; language-specific; single concern, single crate). The boundary of "done" is: a stable, semver-versioned Rust crate with no workspace-only assumptions, suitable for direct `cargo add` consumption by any fleet member that needs to read/write `.phenotype` packs. P0 patch from the McpKit absorption audit.

## Bound Prompts

| Date | Source | File | Tag |
| ---- | ------ | ---- | --- |
| ?    | —      | —    | —   |

(No curated prompts are bound to this repo yet. The 8 prompts that historically bound to `McpKit` were re-attributed to `PhenoFastMCP` + `PhenoMCPServers` per ADR-017; this new repo starts with zero bound prompts.)

## Bound Plans

| Date | Source | File | Status | Outcome |
| ---- | ------ | ---- | ------ | ------- |
| 2026-06-18 | forge subagent (L5-110.x) | `findings/2026-06-18-McpKit-source-inventory.md` | done | P0 patch landed; extraction complete; new repo created |

## Bound Responses (specs, ideas, plans from agents)

| Date | Source | File | Kind | Outcome |
| ---- | ------ | ---- | ---- | ------- |
| 2026-06-18 | forge subagent | `findings/2026-06-18-McpKit-source-inventory.md` | audit | McpKit absorption audit — identified 6 crates for extraction; this is the asset crate |

## Boundary

See: [`docs/boundary/phenotype-mcp-asset.md`](../boundary/phenotype-mcp-asset.md)

## Ecosystem Role

`shared-lib` per `ECOSYSTEM_MAP.md` §1 (`pheno-*-lib` per ADR-023 substrate placement). **Consumers:** `PhenoMCPServers` (the canonical MCP server registry). **Cross-references:** `PhenoFastMCP-rust` (the framework sibling that absorbs the other 4 McpKit Rust crates), `PhenoMCPServers` (the registry consumer), and the deprecated source `KooshaPari/McpKit` (archived 2026-06-18 per ADR-017, retention deferred).

## Open Questions

- None — extraction landed 2026-06-18; awaiting first consumer PR from `PhenoMCPServers`.

## Change Log

| Date | Change | Worklog |
| ---- | ------ | ------- |
| 2026-06-18 | Initial extraction (L7-001 reconciliation; new repo registered under docs/intent/ structure) | `worklogs/L7-003-ecosystem-reconciliation-2026-06-18.json` |
| 2026-06-18 | Disposition row 52 added to `registry/disposition-index.json` (ABSORB, fsm=done) | commit `578af944` |
| 2026-06-18 | Project record added to `projects/phenotype-mcp-asset.json` + `registry/components.lock` (L5-114) | commit `757f4056` |
