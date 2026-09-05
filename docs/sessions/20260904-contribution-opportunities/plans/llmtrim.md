# fkiene/llmtrim: five bounded PR proposals

Read-only planning snapshot: 2026-09-05 06:53 UTC; main `0555a6acb9339ce0b88ec13fbfb05ce9a11ceddc`. No implementation, tests, or outreach performed. Source observations below are verified; proposed regression outcomes are hypotheses until reproduced.

Common upstream gate: [CONTRIBUTING.md](https://github.com/fkiene/llmtrim/blob/main/CONTRIBUTING.md) requires MPL-2.0 contributions **plus a separate grant allowing Francois Kiene and successors/assigns to relicense contributions commercially/proprietarily**. DCO sign-off is additional and does not substitute for that grant. Confirm sponsor alignment before submitting any proposal; retain copyright and provenance. No public core API change is proposed. New surfaces/large changes require maintainer direction first. These plans are reviewable drafts, not authority to contact maintainers.

Overlap sweep: all current open issues and PRs inspected. Do not duplicate assigned issues #261 (MiniMax), #156 (hot swapping), #273 / PR #280 (Codex gateway), #259 / PR #268 (Windows upstream roots), #271 (extra CAs), #269 (DeepSeek Harness Windows), #270 and #226 (pricing). Recheck immediately before claiming a task. Commands below are planned verification, not passing evidence.

## LLMTRIM01 - Read configured ports only from managed shell blocks

**Evidence:** [setup.rs](https://github.com/fkiene/llmtrim/blob/0555a6acb9339ce0b88ec13fbfb05ce9a11ceddc/crates/llmtrim-cli/src/setup.rs), `configured_port_in`, reads each complete profile and passes it to `parse_proxy_port`, which selects the first `127.0.0.1:` occurrence. This differs from the narrowly scoped BEGIN/END handling already used by `managed_block_needs_heal`. An unrelated commented localhost URL before llmtrim's block could therefore select the wrong port. This is a source-backed hypothesis, not an existing user report or reproduced defect.

**Scope:** Add a regression using a temporary profile containing an unrelated URL followed by a valid managed block; restrict discovery to that block while retaining existing supported profile dialects. Preserve comments and all unmanaged content. Exclude CA generation and Codex gateway work. No current open PR explicitly covers this port-discovery case.

**Verification:** `cargo nextest run --profile ci -p llmtrim-cli -E 'test(setup::)'`, then common fmt/clippy/full-nextest loop. Test missing, malformed, duplicate, and valid blocks. **Effort:** 3-5 hours after reproduction. **Alignment:** MPL-2.0, commercial grant, DCO gate above applies.

## LLMTRIM02 - Make cache conformance guard independent of blessed goldens

**Evidence:** [conformance.rs](https://github.com/fkiene/llmtrim/blob/0555a6acb9339ce0b88ec13fbfb05ce9a11ceddc/crates/llmtrim-core/tests/conformance.rs), `assert_cache_control_stable`, scans only direct entries of `system`, `messages`, and `tools`, comparing output to the golden. Nested `messages[].content[]` cache markers are not directly inspected; reblessing also replaces the golden. The comment promises protection against careless reblessing. This is an observed test-coverage mismatch, not proof the compressor corrupts cached input.

**Scope:** Add an independently input-anchored fixture for nested Anthropic cached blocks and a deliberate mutated-output unit case proving the guard detects a changed cached field. Extend only the conformance helper and fixtures, respecting legitimate output transformations outside frozen content. No production compression change.

**Overlap:** No matching open PR found; independent of MiniMax, hot swapping, gateway, roots, and pricing lanes. Coordinate fixture ownership with LLMTRIM03 if both proceed.

**Verification:** `cargo nextest run --profile ci -p llmtrim-core -E 'test(conformance)'`; full standard checks. **Effort:** 4-6 hours. **Alignment:** MPL-2.0, commercial grant, DCO gate applies even to tests.

## LLMTRIM03 - Run shared request fixtures through installed bindings

**Evidence:** [conformance.rs](https://github.com/fkiene/llmtrim/blob/main/crates/llmtrim-core/tests/conformance.rs) describes JS/Python loading identical request fixtures. The inspected [Python binding tests](https://github.com/fkiene/llmtrim/blob/main/crates/llmtrim-uniffi/tests/python/test_llmtrim.py) and [WASM smoke test](https://github.com/fkiene/llmtrim/blob/main/crates/llmtrim-wasm/smoke.mjs) instead contain independent hand-built examples. Confirm no additional generated/published harness already supplies parity before coding. This is an integration-coverage hypothesis, not a runtime failure.

**Scope:** Add table-driven loading of existing `crates/llmtrim-core/tests/conformance/*.json` to Python and the Node smoke runner; assert provider, output shaping, and parsed request JSON. Do not equate native exact token counts with WASM estimates. Add no new fixtures in this PR, keeping LLMTRIM02 separate.

**Verification:** Build/install the wheel using `crates/llmtrim-uniffi/scripts/build-wheel.sh` in an isolated environment, then `pytest crates/llmtrim-uniffi/tests/python`; build WASM per its README with nodejs bindings, then `node smoke.mjs` from `crates/llmtrim-wasm`. Standard Rust checks also apply. **Effort:** 1 day. **Alignment:** MPL-2.0/commercial grant/DCO; ask maintainer direction if CI packaging scope grows.

## LLMTRIM04 - Pin memo behavior when cache markers move or disappear

**Evidence:** The maintainer's [PR #258 review](https://github.com/fkiene/llmtrim/pull/258#pullrequestreview) explicitly identifies optional follow-up regressions: envelope-only marker moves, unchanged markers preserving bytes, and a marker on a compression-removed path. [memo.rs](https://github.com/fkiene/llmtrim/blob/main/crates/llmtrim-core/src/memo.rs) documents restoring stored semantic content while overlaying current-request `cache_control`. This is a maintainer-identified regression opportunity; no new production defect is asserted.

**Scope:** First inventory current memo tests to eliminate already-covered cases. Add only missing deterministic two-turn fixtures proving old markers disappear, current markers survive at valid retained paths, and unchanged requests preserve their existing cacheable serialization. Clarify expected handling when compression removes a marked path before writing an assertion. Avoid adding marker-storage optimization or public APIs.

**Overlap:** No open memo PR in the current sweep; unrelated to #261/#156. LLMTRIM02 covers adapter conformance; this covers stateful turn replay.

**Verification:** `cargo nextest run --profile ci -p llmtrim-core -E 'test(memo::)'`, then standard checks. **Effort:** 4-8 hours, conditional on remaining gaps. **Alignment:** MPL-2.0/commercial grant/DCO applies.

## LLMTRIM05 - Match the exact listening endpoint in Windows setup diagnostics

**Evidence:** [setup.rs](https://github.com/fkiene/llmtrim/blob/0555a6acb9339ce0b88ec13fbfb05ce9a11ceddc/crates/llmtrim-cli/src/setup.rs), Windows `port_holder`, selects netstat lines using `contains(LISTENING)` and `contains(":{port}")`. A requested port such as 4311 can match endpoint 43117. This is an observed substring matcher with a plausible false-match case; no Windows execution or resulting process action has been demonstrated.

**Scope:** Extract a tiny pure parser for the netstat local-address column and require exact numeric port equality. Test IPv4, bracketed IPv6, neighboring ports, non-listening rows, malformed PID fields, and multiple listeners. Preserve the existing best-effort diagnostic contract; do not change process termination behavior, proxy roots, installation privileges, or security policy.

**Overlap:** PR #268 concerns Windows TLS roots and #269 Harness integration; neither advertises this parser. Recheck their file diffs before changing shared setup code, and coordinate ownership with LLMTRIM01.

**Verification:** Pure parser tests via `cargo nextest run --profile ci -p llmtrim-cli -E 'test(setup::)'`; hosted Windows verification before declaring the platform fix complete, plus standard checks. **Effort:** 2-4 hours. **Alignment:** MPL-2.0/commercial grant/DCO applies.

Standard requested checks for every submitted code change: `cargo fmt`, `cargo clippy --all-targets`, `cargo nextest run --profile ci`, and changed-file coverage using `cargo llvm-cov nextest --features intercept,mcp --summary-only`. Add an Unreleased changelog entry for user-visible behavior. Do not report tests or hosted CI as passing before execution.
