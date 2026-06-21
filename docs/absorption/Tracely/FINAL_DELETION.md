# Tracely deletion-justification package

## EXECUTIVE_DECISION

DELETE_AFTER_REGISTRY_MERGE

Confidence: medium-high.

Tracely can be deleted after this registry package lands because its meaningful observability implementation is already present in KooshaPari/PhenoObservability, including matching crates/tracely-core and crates/tracely-sentinel source paths, plus broader active observability docs for tracing, metrics, logging, health, and alerting. Source-only or embedded work that is not proven as live parity is preserved here as a non-generated source snapshot rather than being discarded.

## SOURCE_INVENTORY

- Root docs: README.md, SPEC.md, PRD.md, FUNCTIONAL_REQUIREMENTS.md, ADR.md, CHANGELOG.md, STATUS.md, SECURITY.md.
- Rust workspace: Cargo.toml with crates/helix-tracing, crates/tracely-core, crates/tracely-sentinel.
- crates/tracely-core: unified logging/tracing crate named tracely, with logging and tracing modules.
- crates/tracely-sentinel: rate limiting, circuit breaker, bulkhead, config, validation, tests/bench/fuzz scaffolding.
- crates/helix-tracing: embedded archived tracing crate docs and source.
- target/: generated Rust build output, excluded from preservation snapshot.

## BRANCH_INVENTORY

Local git commands against the Tracely checkout were unreliable/slow, so this package uses the current local filesystem snapshot plus root repository docs as preservation evidence. No deletion should occur until this registry package is merged. If later branch-only evidence appears, preserve it in registry before deletion.

## TARGET_PARITY_SUMMARY

Primary target: KooshaPari/PhenoObservability.

Evidence observed locally:
- PhenoObservability/README.md describes comprehensive observability infrastructure: OpenTelemetry tracing, Prometheus metrics, structured JSON logging, alerting.
- PhenoObservability/crates/tracely-core/Cargo.toml defines package tracely version 0.2.0.
- PhenoObservability/crates/tracely-core/src/lib.rs, logging.rs, tracing.rs match the Tracely core source shape and are newer/maintained in the observability repo.
- PhenoObservability/crates/tracely-sentinel/README.md and source files cover rate limiting, circuit breaker, and bulkhead.
- PhenoObservability also contains adjacent observability crates such as pheno-otel, tracingkit, helix-logging, phenotype-observably-*, metrics, health, and alerting docs.

## ABSORPTION_MATRIX

| Source Item | Source Evidence | Category | Source State | Target Repo | Target Evidence | Status | Deletion Justification | Risk if Deleted | Required Action |
|-------------|-----------------|----------|--------------|-------------|-----------------|--------|------------------------|-----------------|-----------------|
| Canonical Rust observability intent | Tracely/README.md, SPEC.md, PRD.md, FUNCTIONAL_REQUIREMENTS.md | Product intent | docs + implemented | PhenoObservability | PhenoObservability/README.md, PRD.md, docs/FUNCTIONAL_REQUIREMENTS.md | SUPERSEDED_BETTER | Target owns broader active observability stack across tracing, metrics, logging, health, alerting. | low: duplicate repo intent | none |
| tracely-core unified logging/tracing crate | Tracely/crates/tracely-core/Cargo.toml, src/lib.rs, logging.rs, tracing.rs | Public crate/module | implemented | PhenoObservability | PhenoObservability/crates/tracely-core/Cargo.toml, src/lib.rs, logging.rs, tracing.rs | DONE | Matching crate exists in target with same package name and maintained target placement. | low: source duplicate | none |
| Logging helpers and JSON macro | Tracely/crates/tracely-core/src/logging.rs | User-facing feature | implemented + tested | PhenoObservability | PhenoObservability/crates/tracely-core/src/logging.rs | DONE | Same module exists in target crate. | low: duplicate logging helper | none |
| Trace context and subscriber init | Tracely/crates/tracely-core/src/tracing.rs | User-facing feature | implemented | PhenoObservability | PhenoObservability/crates/tracely-core/src/tracing.rs, pheno-otel/SPEC.md | DONE | Target keeps tracing implementation plus broader OTEL docs. | low: duplicate tracing helper | none |
| tracely-sentinel resilience primitives | Tracely/crates/tracely-sentinel/src/rate_limiter.rs, circuit_breaker.rs, bulkhead.rs, config.rs, validation.rs | Public crate/module | implemented | PhenoObservability | PhenoObservability/crates/tracely-sentinel/src/*, README.md | DONE | Matching source path and docs exist in target. | low: duplicate sentinel implementation | none |
| Sentinel tests/bench/fuzz scaffolding | Tracely/crates/tracely-sentinel/tests, benches/perf.rs, fuzz/Cargo.toml | Tests/examples | scaffold/partial | PhenoObservability | PhenoObservability/crates/tracely-sentinel/tests, benches/perf.rs, fuzz/Cargo.toml | DONE | Same scaffolding preserved in target; full validation not rerun in this audit. | medium: possible unvalidated scaffold | none |
| Embedded helix-tracing crate | Tracely/crates/helix-tracing/* | Embedded source | archived/embedded | PhenoObservability + registry package | PhenoObservability/crates/tracely-core comments cite absorbed helix tracing; this package preserves full source snapshot | PARTIAL | Core behavior is absorbed into tracely-core; original embedded source preserved here because exact independent target parity was not fully proven. | medium: historical source loss without package | archive |
| Root governance/security docs | AGENTS.md, CLAUDE.md, SECURITY.md, CODE_OF_CONDUCT.md, CONTRIBUTING.md | Governance artifacts | docs-only | PhenoObservability + registry package | PhenoObservability governance files; this package source snapshot | SUPERSEDED_PARITY | Target has active governance; original docs preserved in snapshot. | low: obsolete governance copy | archive |
| Generated Rust build artifacts | Tracely/target/ | Generated files | generated | none | n/a | NO_MERIT | Build output is reproducible, large, non-source, and excluded from preservation. | low: generated output loss | none |
| Local filesystem snapshot | docs/absorption/Tracely/source-snapshot/tracely-source-snapshot.tar.gz | Preservation artifact | preserved | phenotype-registry | this package | DONE | Non-generated source state is preserved before deletion. | low after merge | none |

## GAPS_AND_EXCEPTIONS

- Exact commit/branch-history inventory could not be completed from the local checkout because git operations against Tracely were unreliable/slow in this session.
- The embedded helix-tracing source is treated conservatively: core behavior appears absorbed, but the source is also preserved in this package.
- No tests were run; this was preservation and deletion-justification work only.

## LAST_RESORT_EXCEPTIONS

None after this package is merged, because non-generated source is preserved in registry. Before merge, the whole repo remains a deletion blocker.

## DELETION_JUSTIFICATION_ESSAY

PhenoObservability owns surviving Tracely responsibilities: Rust observability primitives, tracing, metrics, structured logging, sentinel/rate-limit/circuit-breaker/bulkhead utilities, and observability docs.

PhenoObservability is better than standalone Tracely because it consolidates Tracely with adjacent observability capabilities: OTEL, Prometheus, health, alerting, logging, tracing kits, and observability SDKs. This is a tighter domain boundary than keeping an independent observability micro-repo with duplicated crate names.

The sentinel tests/bench/fuzz artifacts have merit as attempted quality scaffolding. They are preserved in target and in the registry snapshot. Generated target/ output has no source merit and is explicitly excluded.

Final recommendation: delete KooshaPari/Tracely only after this registry package is merged. If merge cannot be completed, preserve the repository.
