# Httpora Final Deletion Package

Date: 2026-06-20
Decision: DELETE_AFTER_PATCHES -> DELETE
Source repo: KooshaPari/Httpora
Target repo: KooshaPari/Quillr
Target package: crates/httpora-core

## Executive decision

Httpora is deletion-ready after Quillr PR #28. The source repository contained a valuable Rust/Tower HTTP toolkit specification and a later Python scaffold. The better end product is the Rust httpora-core crate inside Quillr, because it matches the documented product boundary and now covers the remaining spec-level promises that were not covered by the first absorption.

## Traceability matrix

| Source Item | Source Evidence | Category | Source State | Target Repo | Target Evidence | Status | Deletion Justification | Risk if Deleted | Required Action |
|-------------|-----------------|----------|--------------|-------------|-----------------|--------|------------------------|-----------------|-----------------|
| Rust/Tower HTTP toolkit intent | Httpora README.md, SPEC.md, PRD.md, ADR.md | Product intent | docs-only plus partial Python scaffold | Quillr | README.md, crates/httpora-core/Cargo.toml, Quillr#27, Quillr#28 | SUPERSEDED_BETTER | Target is the Rust crate the source docs promised, not the mismatched Python scaffold. | low: intent lost only if target docs removed | none |
| Rate limiting: token bucket and fixed window | FUNCTIONAL_REQUIREMENTS.md FR-RL-001..003, FRs/FR-HTTP-003.md, FRs/FR-HTTP-004.md, src/httpora/middleware/rate_limiter.py | implemented in Python, docs intended Rust | Quillr | crates/httpora-core/src/middleware/rate_limit.rs, tests/rate_limit_test.rs | SUPERSEDED_BETTER | Rust target implements both strategies and 429 Retry-After support. | low: source Python behavior obsolete | none |
| Retry with exponential backoff and jitter | FUNCTIONAL_REQUIREMENTS.md FR-RETRY-001..003, FRs/FR-HTTP-005.md, FRs/FR-HTTP-007.md, src/httpora/middleware/retry.py | implemented in Python, docs intended Rust | Quillr | crates/httpora-core/src/middleware/retry.rs, tests/retry_test.rs, Quillr#28 | SUPERSEDED_BETTER | Target adds idempotent-method default and opt-in non-idempotent retry policy. | low: source tests obsolete | none |
| Circuit breaker closed/open/half-open | FUNCTIONAL_REQUIREMENTS.md FR-CB-001..003, FRs/FR-HTTP-008.md, FRs/FR-HTTP-009.md, src/httpora/middleware/circuit_breaker.py | implemented in Python, docs intended Rust | Quillr | crates/httpora-core/src/middleware/circuit_breaker.rs, tests/circuit_breaker_test.rs | SUPERSEDED_BETTER | Target provides Rust state machine with half-open probes. | low | none |
| CORS helper | README.md, SPEC.md, PRD.md, CHANGELOG.md | docs-only in main; branch-only Python WIP in wip snapshots | Quillr | crates/httpora-core/src/middleware/cors.rs, tests/cors_test.rs, Quillr#28 | DONE | Missing source-doc promise was patched into target. | low | none |
| Request/response helpers | SPEC.md ResponseBuilder/RequestExtractor, src/httpora/builder.py, tests/test_builder.py | implemented in Python, docs intended Rust | Quillr | crates/httpora-core/src/builder.rs | SUPERSEDED_BETTER | Rust target preserves JSON/text/no-content/rate-limited response and request extraction helpers. | low | none |
| Deterministic clock injection | ADR.md ADR-002, FUNCTIONAL_REQUIREMENTS.md FR-TEST-002, tests/test_rate_limiter.py, tests/test_circuit_breaker.py | implemented/tested in Python | Quillr | crates/httpora-core/src/middleware/clock.rs, rate_limit.rs, circuit_breaker.rs, Quillr#28 | DONE | Target now supports injected clocks for time-dependent middleware. | low | none |
| Tower-compatible middleware direction | ADR.md ADR-001, FUNCTIONAL_REQUIREMENTS.md FR-MW-001, SPEC.md | docs-only | Quillr | crates/httpora-core/Cargo.toml tower feature, retry.rs tower-gated execution | PARTIAL | Target has Tower dependency/feature and Rust crate home; full Layer/Service wrappers remain a future enhancement but source had no Rust implementation to preserve. | medium: aspirational API not fully implemented | document |
| Zero unsafe policy | ADR.md ADR-003 | docs-only | Quillr | Rust target has no unsafe requirement; source policy preserved in this package | INTENTIONALLY_DEPRECATED | Policy is standard for target; no source implementation exists. | low | none |
| Python scaffold package | pyproject.toml, src/httpora, tests/*.py | implemented but stack-mismatched | Quillr | crates/httpora-core plus README product boundary | INTENTIONALLY_DEPRECATED | Python scaffold conflicts with the source docs; Rust target is the better end product. | low: Python-only consumers unlikely and not documented as target | none |
| Branch-only Python CORS/client/server WIP | origin/wip/2026-06-17-cleanup-Httpora-dirty, origin/wip/2026-06-17-httpora-dirty-full-snapshot | branch-only scaffold | Quillr | Quillr#28 CORS; httpora-core core helpers | SUPERSEDED_BETTER | Useful intent is folded into Rust target; server/client scaffold had no stronger product claim than Rust docs. | low | none |
| CI/hygiene branches | origin/chore/*, origin/ci/*, origin/codex/*, dependabot branches | branch-only governance | phenotype-registry / Quillr | existing Quillr CI plus registry row | NO_MERIT | Workflow-only drift has no standalone product value after source deletion. | low | none |
| Journey/iconography/worklog docs | docs/journeys/*, docs/operations/*, docs/worklogs/*, origin/feat/journey-impl | docs-only governance | phenotype-registry | registry rationalization docs and this final package | DONE | Product-specific claims are represented in this package; generic governance belongs to registry. | low | none |

## Gaps and exceptions

No last-resort exception remains. The only partial row is Tower Layer/Service wrapper parity: it is documented as a future enhancement because Httpora never had Rust code implementing it. Deletion is still justified because the target end product is better and the unimplemented source promise is traceably documented here.

## Final recommendation

DELETE. The useful source intent and branch-only attempted work are either implemented in Quillr httpora-core, patched by Quillr#28, or preserved in this final deletion package.
