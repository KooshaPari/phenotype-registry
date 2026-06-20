# TOMBSTONE — KooshaPari/Pyron

**Effective:** 2026-06-19  
**Branch:** `chore/gut-tombstone-absorbed-2026-06-19`  
**Prior state:** Archived organizational shelf (~30 projects, Rust workspace, Python middleware, git submodules)  
**Disposition:** Full gut — workspace replaced with redirect stubs only. Pyron is **not** a boundary owner.

## Why

Pyron accumulated vendored copies and interim git pins for capabilities that belong in domain-role repos.
Fleet drain (PR #61 and prior waves) repointed consumers; this tombstone removes the remaining shelf body
so the repo cannot be mistaken for a buildable infrastructure kit.

## What was removed

- Entire Rust workspace (`crates/*`, root `Cargo.toml` / `Cargo.lock`) — 17+ phenotype-* member crates
- Python packages (`python/pheno-mcp`, `python/pheno-core`, `python/phenosdk`, middleware, etc.)
- Git submodules (`Apisync`, `vendor/phenodocs`, shelf project trees)
- Organizational shelf content (apps, libs, templates, docs, CI, governance, ~3700 tracked paths)
- All `phenoShared` and interim monorepo git dependency pins

## Canonical owners (existing repos only)

| Absorbed role | Canonical repo(s) |
|---------------|-------------------|
| Config / settly | [phenotype-config](https://github.com/KooshaPari/phenotype-config) |
| Observability | [PhenoObservability](https://github.com/KooshaPari/PhenoObservability) |
| Resilience / stashly | [phenotype-resilience](https://github.com/KooshaPari/phenotype-resilience), [phenotype-python-sdk](https://github.com/KooshaPari/phenotype-python-sdk) |
| phenotype-contracts (generic + domain) | [phenotype-rust-sdk](https://github.com/KooshaPari/phenotype-rust-sdk); domain slices: [Authvault](https://github.com/KooshaPari/Authvault), [Eventra](https://github.com/KooshaPari/Eventra), [Agentora](https://github.com/KooshaPari/Agentora) |
| pheno-mcp | [PhenoMCP](https://github.com/KooshaPari/PhenoMCP) (Python), [substrate](https://github.com/KooshaPari/substrate) `phenotype-mcp` (Rust) |

## Stub paths retained

Pointer-only directories remain at historical paths so old links resolve to redirects:

- `crates/phenotype-contracts/`
- `python/pheno-mcp/`
- `Settly/`
- `Stashly/`
- `phenotype-middleware-py/`

## Re-archive

After the gut PR merges, re-archive this repository:

```bash
gh api -X PATCH repos/KooshaPari/Pyron -f archived=true
```
