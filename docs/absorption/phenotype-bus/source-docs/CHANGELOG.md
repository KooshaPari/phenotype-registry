# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added

- Wave-2 libification of the event bus: split the flat `lib.rs` into
  `src/events/{mod,bus,subscription}.rs` and `src/observability.rs`.
- `Event` trait with `Uuid` correlation id, `kind`, `source`, and
  `DateTime<Utc>` timestamp (in `phenotype_bus::events::Event`).
- `EventBus` async trait with `publish`, `subscribe`, `subscribe_to`,
  and `handler_count` (in `phenotype_bus::events::EventBus`).
- `InMemoryBus` implementation with at-least-once delivery (`RetryPolicy`)
  and topic routing via `HashMap<String, Vec<Box<dyn Handler>>>`.
- `IdempotentHandler<H>` wrapper for consumer-side dedup by `event.id`.
- `Subscription` handle with `Uuid` id, topic, and oneshot cancel.
- `observability::init_tracing()` (EnvFilter + RUST_LOG) and
  `observability::make_span(event_id, kind, source)` for per-event spans.
- `impl_event!` macro supporting `kind = ..., source = ...` form.
- 4 new tests: `publish_subscribe_wave2`, `at_least_once_retry_wave2`,
  `idempotency_dedup_wave2`, `multiple_handlers_wave2`.

### Changed

### Deprecated

### Removed

### Fixed

### Security

## 🐛 Bug Fixes
- Fix: complete phenotype-bus implementation (tests passing, formatting clean) (`40bd375`)
## 📚 Documentation
- Docs(fr): scaffold FUNCTIONAL_REQUIREMENTS.md

Add FR traceability framework to enable test+spec integration. Wave-5 systemic push.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com> (`c8ccf80`)
## 🔨 Other
- Test(integration): cross-collection bus flow — 5 integration tests + CI

Add integration test suite for phenotype-bus event pipeline:
- test_sidekick_emits_user_status_event
- test_eidolon_responds_to_status_event_with_screenshot
- test_stashly_caches_screenshot_artifact
- test_observably_records_trace_for_pipeline
- test_sidekick_messaging_notifies_on_completion

Each test exercises a collection handler responding to published events,
verifying the complete Sidekick→Eidolon→Stashly→Observably→Messaging pipeline.
All 5 tests pass, all 8 total tests (3 unit + 5 integration) pass locally.

Update CI workflow (quality-gate.yml) to run cargo test + clippy + fmt.
Update FUNCTIONAL_REQUIREMENTS.md with test coverage.
Add docs/integration_tests.md documenting event flow and patterns.

Traces to: FR-ORG-AUDIT-2026-04-002

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com> (`7a55826`)
- Chore(deps): align tokio + serde to org baseline (phenotype-versions.toml)

- tokio: unified to 1.39
- serde: unified to 1.0
- Verified: cargo check passed

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com> (`e4bbb06`)
- Test(smoke): add smoke test scaffolding

Seed test infrastructure for Rust crate. Wave-5 test coverage push.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com> (`f1aa5d1`)
- Init: phenotype-bus micro-repo (155 LOC, pub/sub event bus) (`aaa4972`)
