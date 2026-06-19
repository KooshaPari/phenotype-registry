---
repo: "phenotype-mcp-asset"
role: shared-lib
status: active
last_boundary_review: 2026-06-18
review_cadence: 30d
adr_023_substrate: "pheno-*-lib"
origin: "KooshaPari/McpKit/rust/phenotype-mcp-asset/ v0.2.0 (McpKit archived 2026-06-17 per ADR-017)"
extracted_on: "2026-06-18"
disposition_row_id: 52
in_scope:
  - "Phenotype-pack (.phenotype) asset parsing and validation"
  - "Asset manifest schema (skill, plugin, agent role card)"
  - "Asset bundling/unbundling for MCP server distribution"
  - "Stable, semver-versioned Rust crate API (no workspace-only assumptions)"
out_of_scope:
  - "MCP transport (HTTP/SSE/stdio) — lives in PhenoMCPServers and PhenoFastMCP-rust"
  - "Skill execution / runtime — lives in PhenoMCPServers servers/"
  - "Asset storage backend (S3, filesystem) — caller-provided via trait injection"
  - "Asset encryption / signing — lives in pheno-crypto (HexaKit crate)"
---

# Boundary — phenotype-mcp-asset

## In Scope

- **Phenotype-pack format**: read/write `.phenotype` pack archives (tar/zstd with manifest.json).
- **Manifest validation**: JSON-Schema validation of skill, plugin, and agent role card manifests.
- **Asset bundling**: produce a Phenotype-pack from a directory of asset files + manifest.
- **Asset unbundling**: extract a Phenotype-pack to a directory, with atomicity guarantees.
- **Stable Rust API**: `pub` types are semver-stable; consumers do `cargo add phenotype-mcp-asset`.

## Out of Scope

| Not here | Lives in | Reason |
| -------- | -------- | ------ |
| MCP transport (HTTP/SSE/stdio) | `PhenoMCPServers`, `PhenoFastMCP-rust` | This crate is transport-agnostic; transport is the consumer's concern |
| Skill execution runtime | `PhenoMCPServers/servers/` | Out of scope — asset handling is a pure-data concern |
| Asset storage backend | caller-provided via `AssetStore` trait | Single concern: pack I/O. Storage is injected. |
| Asset encryption / signing | `pheno-crypto` (HexaKit crate) | Cryptography belongs in the canonical crypto crate |
| The other 4 McpKit Rust crates | `PhenoFastMCP-rust` | Per McpKit absorption audit, sibling crates absorbed to PhenoFastMCP-rust |
| Python SDK equivalents | `phenotype-python-sdk/packages/agentmcp-hex/` | This crate is Rust-only; Python SDK has its own asset handling if needed |

## Boundary Crossings

| Crossing | Direction | Surface | Status |
| -------- | --------- | ------- | ------ |
| Asset read API | `PhenoMCPServers → phenotype-mcp-asset` | Rust API (`phenotype_mcp_asset::Pack::open`) | green |
| Asset write API | `PhenoMCPServers → phenotype-mcp-asset` | Rust API (`phenotype_mcp_asset::Pack::create`) | green |
| Manifest schema | `phenotype-mcp-asset → hexaKit/schemas/` | JSON-Schema (vendored) | green |
| Migration from McpKit | `McpKit (archived) → phenotype-mcp-asset` | n/a (one-shot extraction) | green |
| Provenance | `phenotype-mcp-asset → McpKit` | n/a (documented in `docs/intent/`) | green |

## Last Boundary Review

**Date:** 2026-06-18
**Reviewer:** forge subagent (L7-003 reconciliation + McpKit absorption audit)
**Worklog / finding:** `worklogs/L7-003-ecosystem-reconciliation-2026-06-18.json`; `findings/2026-06-18-McpKit-source-inventory.md`
**Decisions:**
- New canonical home for the asset crate, extracted from McpKit v0.2.0.
- ADR-023 classification: `pheno-*-lib` (pure reusable library; single concern).
- 30-day review cadence (next review 2026-07-18); align with L7-001 sweep rhythm.

**Next review:** 2026-07-18
