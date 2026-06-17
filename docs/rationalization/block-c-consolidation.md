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
| 2 | **Auth dedup** | Authvault (canonical) ← AuthKit | ⚠️ Corrected by measurement (AuthKit#118): AuthKit's **auth surface is empty** (Authvault is the only auth in org → nothing to fold into Authvault). But AuthKit carries **1,732 lines of non-auth infra** (`phenotype-bid`, `content-hash`, `security-aggregator`, `contracts`). Correct action = **relocate those crates to phenoShared** (which already has their missing deps `phenotype-time`/`phenotype-health`, fixing AuthKit's compile breaks) **then archive** the empty auth shell — NOT archive-alone (would orphan code). Collision to resolve: phenoShared already has a `phenotype-contracts`. **Tokn** excluded (LLM cost tracking, not auth). **phenotype-auth-ts** stays separate (TS sibling). | relocation PR phenoShared#170 (cargo metadata green; CI-gated); archive AuthKit after merge |
| 3 | **Generic-lib rescope** | phenoShared + py/rs/go util shards | RESCOPE. ⚠️ Audit's "delete empty stubs / -3,200 lines" verdict **corrected by measurement** (phenoShared#169 comment): cache-adapter (569 lines) + state-machine (575 lines) have real but *unwired* impl — fix lib.rs exposure or archive-if-unused, do NOT delete. | audited + corrected |

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
