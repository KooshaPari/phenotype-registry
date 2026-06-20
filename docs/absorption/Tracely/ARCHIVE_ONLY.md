# Tracely archive-only package

Date: 2026-06-20
Source: KooshaPari/Tracely
Decision: ARCHIVE_ONLY
Confidence: low

| Source Item | Source Evidence | Category | Source State | Target Repo | Target Evidence | Status | Deletion Justification | Risk if Deleted | Required Action |
|---|---|---|---|---|---|---|---|---|---|
| Tracing/logging primitives | crates/tracely-core/src/lib.rs, logging.rs, tracing.rs | Public crates/modules | implemented | pheno-tracing, PhenoObservability | pheno-tracing/src/lib.rs, port.rs, adapters.rs; PhenoObservability/tracing/otel.go | PARTIAL | Target owners exist, but exact API parity for tracely-core was not proven in this quick pass. | high - could lose concrete logging/tracing helper API | deep branch/code parity audit |
| Sentinel resilience primitives | crates/tracely-sentinel/src/rate_limiter.rs, circuit_breaker.rs, bulkhead.rs, validation.rs, config.rs | Public crates/modules | implemented | phenotype-resilience / Quillr | likely resilience/http targets, not proven here | NOT_COVERED | Deletion cannot be justified until sentinel is mapped or intentionally retired. | high - could lose retry/bulkhead/circuit-breaker implementation details | migrate or preserve |
| Helix tracing embedded repo | crates/helix-tracing/.git, src/lib.rs, ARCHIVED.md | Submodule/nested repo | branch/nested | pheno-tracing | not proven | BRANCH_ONLY | Nested git repo requires separate absorption decision. | high - nested history/code may be lost | preserve nested repo or map to pheno-tracing |
| Branch-only Tracely work | many local/remote branches including feat/tracely-*, bench/tracely-*, wip/* | Branch-only work | branch-only | mixed | not proven | BRANCH_ONLY | Branch matrix is incomplete; no deletion. | high - many feature branches indicate meaningful attempted work | full branch audit |
| Staged intent-doc reorder | staged diff in docs/intent/Tracely.md swaps prompt-row order only | Docs/governance | staged local | none | this package notes the delta | NO_MERIT | Row-order-only staged change has no semantic content. | low - no useful artifact lost | document/no action |

Executive decision: ARCHIVE_ONLY. Tracely is not deletion-ready. It needs a full branch/history and nested-repo parity audit before any delete recommendation.
