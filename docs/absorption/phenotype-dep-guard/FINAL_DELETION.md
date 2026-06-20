# phenotype-dep-guard deletion package

Date: 2026-06-20
Decision: DELETE
Confidence: medium-high

## Executive decision

phenotype-dep-guard can be deleted. The repo is archived and contains no product implementation, no crate/package manifest, no tests, no concrete spec, and no filled boundary. Its docs do not trump code because the docs are unfilled registry intent/boundary stubs. The only meaningful local work is governance scaffolding and a generic Rust justfile for a nonexistent Rust workspace; the local ahead commit has already been preserved remotely on wip/2026-06-20-local-ahead-preserve and is also represented in this package.

## Absorption matrix

| Source Item | Source Evidence | Category | Source State | Target Repo | Target Evidence | Status | Deletion Justification | Risk if Deleted | Required Action |
|-------------|-----------------|----------|--------------|-------------|-----------------|--------|------------------------|-----------------|-----------------|
| Dependency guard product | Repo description: Dependency guard for pheno repos | Product intent | title-only | none | none | NO_MERIT | No concrete spec, implementation, tests, or API exists in source | low; only repo-name idea lost | none |
| Generic Rust justfile | phenotype-dep-guard/justfile | Tooling scaffold | scaffold/misaligned | none | source-docs/justfile | NO_MERIT | Generic cargo commands for a repo with no Cargo.toml; not a product artifact | low | none |
| Governance templates | .github templates, CODEOWNERS, CHANGELOG.md | Governance | scaffold | phenotype-registry | source-docs plus WIP branch record PR #307 | NO_MERIT | Generic templates have no unique dependency-guard semantics | low | none |
| Intent/boundary docs | docs/intent/phenotype-dep-guard.md, docs/boundary/phenotype-dep-guard.md | Docs | untracked stub docs | phenotype-registry | patches/local-untracked-docs.patch and PR #307 WIP record | NO_MERIT | Stubs are unfilled and explicitly point back to registry regeneration | low | none |
| Local ahead commit | main ahead origin/main, preserved branch wip/2026-06-20-local-ahead-preserve | Historical local work | local-only | phenotype-registry/GitHub branch | patches/local-ahead.patch and registry PR #307 | DONE | WIP is preserved; no standalone repo needed | low-medium | none |
| Archived remote state | gh repo archived true | Governance | archived | phenotype-registry | this package | INTENTIONALLY_DEPRECATED | No remaining meaningful source item requires repo retention | low | none |

## Gaps and exceptions

No LAST_RESORT_EXCEPTION remains. If dependency-guard functionality is needed later, it should be specified fresh in the actual supply-chain/CI substrate, not recovered from this empty scaffold.

## Final deletion recommendation

DELETE phenotype-dep-guard after this registry PR merges.
