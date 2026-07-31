# Testing Strategy

## Focused gates

- Tracera fixture: `CARGO_TARGET_DIR=/private/tmp/tracera-ledger-consumer-v1-target cargo test -p tracera-server tests::observability_ledger_consumer_v1_fixture_round_trip -- --exact --nocapture`.
- Validate changed-file formatting and `git diff --check` before publication.
- Verify JSON fixtures parse independently.
- Run repository-specific CLI/lint/type/test commands only after checking disk and repo instructions.

The corrected Tracera command uses the module-qualified exact test name and reports `1 passed, 0 failed, 52 filtered out`. An earlier unqualified exact filter collected zero tests and is not counted as evidence.

The fixture now carries deterministic `trace_id`, `span_id`, `parent_span_id`, and `correlation_id` metadata with `producer=PhenoObservability`; the focused test asserts these fields round-trip.

AgilePlus validation is intentionally red at this checkpoint: `0/6` required CI/review evidence items are attached and the feature remains Planned. This is a governance blocker, not a release result.

## Promotion gates

1. Focused test passes.
2. Relevant integration/e2e or installed dogfood passes.
3. Required hosted checks are green on the exact PR head.
4. Review comments and bot feedback are resolved.
5. Evidence packet records command, output, SHA, and environment.

## Negative evidence policy

Pending, stale, historical, projected, or local-only checks do not count as release evidence. Workspace-wide failures are separated from focused changed-surface results.
