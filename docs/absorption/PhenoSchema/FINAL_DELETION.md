# PhenoSchema deletion package

Date: 2026-06-20
Decision: DELETE
Confidence: high

## Executive decision

PhenoSchema can be deleted. Its meaningful source item is the Rust hexagonal schema port crate under ports/. That code is now absorbed into phenoUtils as crates/pheno-schema-port via phenoUtils PR #71. The archived source repo was described as preserved local WIP; its local-ahead governance/snapshot commits are preserved here as a patchset.

## Absorption matrix

| Source Item | Source Evidence | Category | Source State | Target Repo | Target Evidence | Status | Deletion Justification | Risk if Deleted | Required Action |
|-------------|-----------------|----------|--------------|-------------|-----------------|--------|------------------------|-----------------|-----------------|
| Schema trait and validation data types | PhenoSchema/ports/src/schema.rs | Public Rust crate | implemented | phenoUtils | crates/pheno-schema-port/src/schema.rs, phenoUtils PR #71 | DONE | Code moved into active Rust utility target | low | none |
| JsonSchema/Zod stub adapters | PhenoSchema/ports/src/adapters/*.rs | Adapter scaffold | scaffold/implemented stub | phenoUtils | crates/pheno-schema-port/src/adapters/*.rs, PR #71 | DONE | Stub adapters preserved exactly as utility crate scaffold | low | none |
| Schema tests | PhenoSchema/ports/tests/schema.rs | Tests | implemented | phenoUtils | crates/pheno-schema-port/tests/schema.rs, PR #71 | DONE | Tests preserved with crate | low | none |
| Workspace/package metadata | PhenoSchema/Cargo.toml, ports/Cargo.toml | Manifest | implemented | phenoUtils | workspace Cargo.toml and crates/pheno-schema-port/Cargo.toml, PR #71 | SUPERSEDED_PARITY | Target normalizes package name/deps to phenoUtils workspace | low | none |
| Governance/docs | PhenoSchema/CHANGELOG.md, SECURITY.md, templates | Governance | docs-only | phenotype-registry | source-docs/ plus ORIGIN.md in target | DONE | Relevant source docs preserved; generic templates have low standalone value | low | none |
| Local ahead commits | PhenoSchema chore/dependabot-2026-06-08 ahead origin | Historical local work | local-only | phenotype-registry | patches/local-ahead.patch | DONE | Local snapshot/governance work preserved before deletion | medium | none |
| Archived WIP repo status | GitHub description: Preserved local WIP from PhenoSchema | Governance | deprecated | phenoUtils/phenotype-registry | PR #71 and this package | INTENTIONALLY_DEPRECATED | WIP source is now moved and documented | low | none |

## Gaps and exceptions

No LAST_RESORT_EXCEPTION remains.

## Final deletion recommendation

DELETE PhenoSchema after this registry PR merges.
