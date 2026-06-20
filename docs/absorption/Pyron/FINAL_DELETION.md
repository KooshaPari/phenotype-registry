# Pyron final deletion package

Date: 2026-06-20
Decision: DELETE_AFTER_PRESERVATION
Source repo: KooshaPari/Pyron
Source state: archived tombstone, local branch chore/pyron-deps-audit-2026-06-19
Registry package: docs/absorption/Pyron/source-snapshot/

## Executive decision

DELETE.

Pyron is no longer a boundary owner. Its current default branch is a tombstone and its remaining local value is historical: archive crates, tombstone docs, and generated boundary/intent archived-marker edits. The full historical source snapshot is preserved in this registry package before deletion, while known active responsibilities map to canonical target repos.

## Absorption matrix

| Source Item | Source Evidence | Category | Source State | Target Repo | Target Evidence | Status | Deletion Justification | Risk if Deleted | Required Action |
|-------------|-----------------|----------|--------------|-------------|-----------------|--------|------------------------|-----------------|-----------------|
| Pyron repo boundary | README.md, TOMBSTONE.md, MIGRATED.md | Product intent | deprecated | phenotype-registry | docs/absorption/Pyron/source-snapshot/ | DONE | Tombstone intent preserved; repo is not canonical owner | low: redirect history loss | none |
| AgilePlus archived crates | .archive/crates/agileplus-* | Public crates / app framework | archived source | AgilePlus | AgilePlus/crates/agileplus-* and AgilePlus/archive/PhenoLang-crates-2026-06-20/ | DONE | Active/preserved AgilePlus owner exists; Pyron copy is duplicate shelf | medium: historical byte state | preserved in registry snapshot |
| Config/shared config | .archive/crates/phenotype-shared-config, tombstone Config/settly rows | Public crate / config | archived source | Configra | Configra/archive/PhenoLang-config-2026-06-20/crates/phenotype-shared-config | DONE | Configra owns config boundary; Pyron copy preserved | low: old config utility loss | none |
| Rust MCP crate | .archive/crates/phenotype-mcp, tombstone MCP row | Public crate / MCP | archived source | PhenoFastMCP-rust | PhenoFastMCP-rust/archive/PhenoLang-mcp-2026-06-20/crates/phenotype-mcp | DONE | MCP Rust history already preserved in target archive; Pyron copy preserved | low: old MCP crate history | none |
| Primitive utility crates | .archive/crates/phenotype-cache-adapter, phenotype-cost-core, phenotype-crypto, phenotype-git-core, phenotype-macros, phenotype-process, phenotype-rate-limit | Shared Rust utilities | archived source | phenoUtils / Authvault | phenoUtils/archive/PhenoLang-primitives-2026-06-20/crates/*, Authvault/rust/phenotype-crypto | DONE | Utility responsibility is in narrowed utility/security owners; Pyron copy preserved | medium: exact historical deltas | none |
| Observability/logging | .archive/crates/phenotype-logging, tombstone observability row | Observability | archived source | PhenoObservability / phenotype-python-sdk | PhenoObservability/rust/phenotype-logging, phenotype-python-sdk/packages/phenotype-logging | DONE | Observability owners exist and are stronger boundaries | low: old logging scaffold | none |
| Contracts/domain slices | tombstone crates/phenotype-contracts row | Contracts | tombstone redirect | phenotype-rust-sdk / Authvault / Eventra / Agentora | tombstone canonical-owner table | PARTIAL | Redirect evidence exists; exact historical Pyron contracts tree was already removed from default branch; snapshot preserves current evidence | medium: removed pre-gut history not present locally | archive-only provenance |
| Pyron-only generic/scaffold crates | .archive/crates/bifrost-routing*, forgecode-core, phenotype-bdd, phenotype-casbin-wrapper, phenotype-compliance-scanner, phenotype-config-loader, phenotype-core, phenotype-event-bus, phenotype-infrastructure, phenotype-mock, phenotype-policy-engine, phenotype-ports-canonical, phenotype-project-registry, phenotype-security-aggregator, phenotype-test-fixtures, phenotype-testing | Broken/scaffold/branch-era source | archived source | phenotype-registry | docs/absorption/Pyron/source-snapshot/archive/crates/* | LAST_RESORT_EXCEPTION | No live parity proven quickly; full source is preserved in registry before deleting Pyron | high if not preserved: unique historical scaffolds | preserve snapshot |
| Local archived-marker docs | docs/boundary/Pyron.md, docs/intent/Pyron.md local dirty diff | Governance docs | local dirty docs-only | phenotype-registry | docs/absorption/Pyron/source-snapshot/docs/* | DONE | Docs were generated archived-marker updates; copied into registry snapshot | low: metadata reorder/status loss | none |
| Branch-only hygiene/governance branches | local branch list: chore/*, feat/*, wip/* | Branch-only work | branch-only / historical | phenotype-registry | this deletion package and source snapshot | PARTIAL | Branch names/intent captured; no deletion relies on ignoring branches | medium: unique branch commits not exhaustively cherry-picked | accept archive snapshot; restore from GitHub only if future need |

## Branch inventory summary

Pyron has hygiene/governance/dependency branches including ci cache, cliff, editorconfig, license, renovate, feature stubs, and WIP snapshots. They do not re-establish Pyron as an owner. The current default branch is a tombstone and the remaining local archive snapshot is preserved here.

## Absorption target mapping

| Responsibility | Owner |
|----------------|-------|
| AgilePlus runtime/API/CLI/sync/triage crates | AgilePlus |
| Config/shared config | Configra |
| Rust MCP | PhenoFastMCP-rust |
| Utility primitives | phenoUtils |
| Cryptography/security primitive | Authvault / phenoUtils archive |
| Observability/logging | PhenoObservability and phenotype-python-sdk |
| Domain contracts | phenotype-rust-sdk plus Authvault/Eventra/Agentora |
| Unmapped historical scaffolds | phenotype-registry preservation snapshot |

## Last-resort exceptions

The Pyron-only generic/scaffold crates are preserved as a last-resort exception in docs/absorption/Pyron/source-snapshot/archive/crates/. This justifies deleting the repo without asserting target parity for those crates.

## Final deletion recommendation

Delete KooshaPari/Pyron after this registry package merges. The matrix supports deletion because every known meaningful current source item is either mapped to a target owner or preserved as an explicit registry exception.
