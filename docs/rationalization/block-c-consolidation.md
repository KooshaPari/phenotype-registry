# Block C — Consolidation SSOT

**Status:** Active
**Date:** 2026-06-16
**Scope:** Cloud / MCP / Routing / Substrate / Spine — 20 repos owned by the Block-C chat.

This is the single source of truth for Block-C rationalization. Per-repo audit
PRs link back here; this file links forward to them.

## Strategic merges (3)

| # | Merge | Members | Verdict | Plan |
|---|-------|---------|---------|------|
| 1 | **GFX SDK** | phenotype-voxel + phenotype-terrain + phenotype-water | ✅ Consolidated → **KooshaPari/phenotype-gfx** (polyglot monorepo + umbrella, history-preserving subtree; voxel=Rust, terrain/water=C#; unify at data layer via spec/interop.md) | done 2026-06-16 |
| 2 | **Auth dedup** | authvault + duplicate auth repos | Collapse into canonical `authvault` | per-repo PR |
| 3 | **Generic-lib rescope** | phenoShared + py/rs/go util shards | Reverse of merge — split or bulk-up over-generic libs into named, purpose-scoped packages | per-repo PR |

## Per-repo audits

Each Block-C repo carries `docs/audit/BLOCK-C-AUDIT.md` on its own main. Status tracked here.

| Repo | Audit landed | Notes |
|------|--------------|-------|
| Tokn | ✅ merged (#66, 2026-06-16) | consolidation plan on main |
| services | ⏳ | governance baseline open |
| phenotype-registry | ✅ this doc | SSOT host |
| PhenoMCP | ⏳ | |
| PhenoVCS | ⏳ | |
| authvault | ⏳ | merge target (see #2) |
| phenotype-voxel | ⏳ | GFX merge source (see #1) |
| phenotype-terrain | ⏳ | GFX merge source (see #1) |
| phenotype-water | ⏳ | GFX merge source (see #1) |
| phenoShared | ⏳ | rescope (see #3) |

## Durability rule

Every Block-C deliverable lands on **remote (branch + PR)** the moment it is
produced. Local-only branches are treated as lost. This file and the per-repo
audits are the durable record; forge job logs are not.
