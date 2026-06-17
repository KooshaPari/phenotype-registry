# Ecosystem Boundary-Shaping Charter

**Status:** Active
**Date:** 2026-06-16
**Goal:** tight, coherent **domain boundary per repo** across the polyrepo ecosystem.

## Doctrine — three dispositions (NEVER delete-on-sight)

A stub / empty / broken / unused / incomplete module is **not** a delete candidate by
default. On-paper-good boundaries (e.g. a "Testing Boundary") still deserve an owner.
For each module/crate/folder choose one:

1. **Decompose** — repo spans multiple domains → split into tightly-scoped domain repos.
2. **Absorb** — a better existing repo should own this boundary → move it there
   (history-preserving). **Reverse:** infra-generic things present in *every* repo
   (tests, CI, governance) → hoist into a **scaffolding / source-import generator**
   (unified maintenance + per-repo distributed config/tailoring), not N hand-maintained copies.
3. **Dynamic-install monorepo** — only when sub-components are individually **too small
   to justify their own repo's governance**. Loose-coupled, dynamic install / lighter loads.

## Target topology (hypothesis — shapes work, not mandated arch)

| Layer | Repo(s) | Role |
|-------|---------|------|
| **Scaffolding** | **HexaKit** | Project + file **templates / generators** that bootstrap new repos onto our arch patterns. NOT a lib holder. Owns the infra-generic layer (tests/CI/governance) as generated, tailorable scaffolding. |
| **Domain SDKs** | McpKit · AuthKit→Authvault · ResilienceKit · TestingKit · PhenoObservability · phenotype-gfx | One installable SDK per domain (mcp, auth, resilience, testing, observability, graphics…). |
| **Umbrella** | a `phenoSDK`-style meta | Dynamic **install/import** of the domain SDKs. |
| **Too-small monorepo** | phenoShared | Home only for bits too small to own a repo; dynamic install. |

## Decomposition map (large/unfocused collections)

| Repo | Size | Signal | Disposition (draft — assessment PR per repo) |
|------|------|--------|----------------------------------------------|
| **PhenoKits** | 666 MB | Python "toolkit collection" — largest, multi-domain | **Decompose** into domain Python SDKs; fold shared base into phenotype-python-sdk; archive shell after. |
| **pheno** | 170K LOC, 11 workspaces | Rust mega-monorepo | **Decompose** by workspace into domain repos / existing *Kits; keep only too-small bits. |
| **HexaKit** | 22 MB | "hexagonal toolkit" currently holds libs | **Reframe** → templates/scaffolding-gen; relocate any real libs out to domain SDKs. |
| **phenoShared** | 23 crates | tiny infra crates | **Keep as dynamic-install monorepo** for the genuinely-small; relocate any crate big/coherent enough to be a domain SDK (e.g. http-client-core, rate-limit, secret → ResilienceKit/AuthKit?). |
| **phenotype-python-sdk / go-sdk** | — | "consolidates McpKit/Tokn / PlatformKit" | Confirm they're the per-language SDK umbrellas; align with domain-SDK layer. |
| **phenokits-commons** | 639 KB | "cross-cutting commons" | Likely **absorb** into HexaKit (generated) or phenoShared (too-small). |

## Execution
Per repo: assessment job → per-module disposition table → history-preserving move PRs →
archive emptied shells only after relocation. Tracks back to [block-c-consolidation](./block-c-consolidation.md).
See also: org memory `feedback_repo_boundary_shaping`.
