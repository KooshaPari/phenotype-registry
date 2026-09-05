# API Relay Audit: five conditional contribution proposals

Repository: https://github.com/toby-bridges/api-relay-audit. Inspected September 5 UTC / September 4 Pacific. [CONTRIBUTING.md](https://github.com/toby-bridges/api-relay-audit/blob/main/CONTRIBUTING.md) explicitly welcomes deterministic tests, small fixes and clearer inconclusive results, while requiring an issue first for larger changes. Paths below exist in the inspected HEAD tree; stream_integrity.py and contribution instructions were read. No proposal is a reproduced defect. Five proposals are meaningful candidate scopes; gaps already covered at implementation time must be retired, not padded into PRs.

Overlap review: [open](https://github.com/toby-bridges/api-relay-audit/pulls?q=is%3Apr+is%3Aopen) and [recent closed PRs](https://github.com/toby-bridges/api-relay-audit/pulls?q=is%3Apr+is%3Aclosed+sort%3Aupdated-desc), September 5 UTC. Occupied: #95 structured tools, #73 curl/header handling, #76 zero latency, #74 leakage markers, #77 identity-table refactor, #90 insecure TLS authorization. Already merged: #87 refusal false positives, #89 incomplete-stream detection, #71 reproducibility metadata. Do not reopen those features under new titles. Sampling cannot establish absence; each proposal needs complete targeted issue/PR search and current test inspection before activation.

Shared actual commands from CONTRIBUTING: `python3 -m pytest tests/ -v`, `python3 scripts/collect-metrics.py --check`, `python3 scripts/build-standalone.py --check`, and `python3 -m pytest tests/test_dual_distribution_parity.py -v`. Any logic change must regenerate the standalone artifact using the repository builder and pass parity. Engineering effort excludes response time. All fixtures must use synthetic traffic and credentials.

## RELAY-01: Exercise SSE framing under fragmented transport

- Evidence: HYPOTHESIS requiring a missing-case demonstration; [#35](https://github.com/toby-bridges/api-relay-audit/issues/35) requests reproducible stream anomaly fixtures. Terminal completeness already landed in #89.
- Scope: `tests/test_client_stream.py`, `tests/test_stream_integrity.py`, and only if needed `api_relay_audit/client.py`. Test one valid stream delivered at every byte boundary, CRLF separators, multi-line data and UTF-8 split boundaries. No new verdict scoring or protocol expansion.
- Acceptance: all semantically identical valid chunkings produce identical signals; truncated payloads remain inconclusive rather than clean; malformed framing reports a bounded diagnostic. Run `python3 -m pytest tests/test_client_stream.py tests/test_stream_integrity.py -v` plus shared checks.
- Overlap: distinguish transport segmentation from merged #89 terminal event checks and closed #84. First candidate, 1-2 days. Confirm absent tests and fixture scope with owner. Value: gateway streaming regression harness reusable in OmniRoute.

## RELAY-02: Verify report redaction across nested error payloads

- Evidence: HYPOTHESIS; contribution policy prohibits publishing credentials and private traffic. This is a publication-safety contract opportunity, not a discovered leak.
- Scope: `api_relay_audit/reporter.py`, `tests/test_reporter.py`, `tests/test_example_report.py`, and `docs/examples/sanitized-audit-report.fixture.json`. Inspect existing sanitization first; propose only uncovered header/query/nested exception cases. No telemetry upload or public relay ranking.
- Acceptance: synthetic bearer keys, URL userinfo and sensitive query values never occur in rendered artifacts; benign diagnostic shape survives; redaction is deterministic and does not corrupt JSON. Run `python3 -m pytest tests/test_reporter.py tests/test_example_report.py -v` plus shared checks.
- Overlap: #71 already added provenance metadata; #65 concerns copy semantics. Keep separate from those changes and #73 request construction. Independent second candidate, 1-2 days; align exact redaction policy first. Value: safely publish auditable gateway evidence and improve enterprise support practice.

## RELAY-03: Preserve inconclusive context results for bounded transport failures

- Evidence: HYPOTHESIS; existing `api_relay_audit/context.py` and `tests/test_context.py` are inspected tree paths. Determine whether oversized-input, timeout and cancellation outcomes can be mistaken for model context limits before proposing behavior changes.
- Scope: context probe result classification and deterministic fake-client fixtures; `scripts/context-test.py` only if CLI presentation must change. No larger probes, real paid API load, or inferred provider limits.
- Acceptance: timeout, connection failure and response-size rejection remain distinguishable from validated context exhaustion; control success is required for any context-capacity conclusion; retries remain bounded. Run `python3 -m pytest tests/test_context.py tests/test_error_diagnosis.py -v` plus shared checks.
- Overlap: review full context-related search before activation; no named matching PR in sampled set. Third, 2-3 days, independent; owner agrees evidence semantics. Value: defensible capacity benchmarks for router policies without presenting transport failures as model facts.

## RELAY-04: Add a cross-language refusal calibration corpus

- Evidence: HYPOTHESIS following [#31](https://github.com/toby-bridges/api-relay-audit/issues/31); #79 refusal bug was partly superseded by merged #87. Do not repeat its apostrophe fix.
- Scope: `tests/test_refusal_detector.py` and `api_relay_audit/refusal.py` only for newly reproduced errors. Curate synthetic paired refusals and actual disclosure-shaped responses in two maintainer-approved languages; include mixed refusal plus disclosure to guard false negatives. No speculative model-fingerprint patterns or claim of broad multilingual accuracy.
- Acceptance: corpus labels justified individually, existing English behavior unchanged, pure refusal versus disclosed structural content remains distinct, unsupported examples are inconclusive where appropriate. Run `python3 -m pytest tests/test_refusal_detector.py -v` plus shared checks.
- Overlap: inspect #87 tests before collecting new cases; current owner alignment required on supported languages. Fourth, 2-3 days. Value: international gateway evaluation and measurable detector precision; reject proposal if no supported-language gap remains.

## RELAY-05: Produce deterministic local report comparisons

- Evidence: VERIFIED feature interest [#9](https://github.com/toby-bridges/api-relay-audit/issues/9) requests audit history/trends; proposed bounded CLI comparison is a HYPOTHESIS about acceptable scope, requiring agreement.
- Scope: consume the existing `docs/report-artifact-schema.md` and report fixture through a proposed new local comparison script/test; existing integration surfaces are `api_relay_audit/reporter.py` and `tests/test_reporter.py`. Proposed new paths must be agreed before coding. No hosted dashboard, database, uploads or safety ranking.
- Acceptance: compare compatible versions deterministically, list changed step verdicts/evidence, reject unsupported schemas clearly, do not interpret missing runs as improvement, and exclude secrets/raw payloads. Test clean-to-anomaly, inconclusive-to-clean, reordered keys and schema mismatch with offline fixtures; run shared checks plus the agreed new suite.
- Overlap: #71 metadata is a prerequisite format, not work to repeat. Fifth, 3-4 days; requires owner scope approval and RELAY-02 redaction contract agreement. Value: version-to-version OmniRoute regression evidence and repeatable business demonstrations.
