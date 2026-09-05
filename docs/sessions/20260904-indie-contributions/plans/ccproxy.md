# starbaser/ccproxy: five contribution proposals

**Goal:** Five bounded useful contributions, offered separately after scope and ownership checks.

**Architecture:** Preserve current upstream boundaries. These are plans, not implemented changes; reported bugs still require reproduction.

**Tech stack:** Python 3.13.

Inspected September 5 UTC 2026. Refresh HEAD and issue/PR state before execution.

**Overlap and policy:** All five HOLD for maintainer responsiveness and architecture alignment with #16. Open #20 MiniMax, #19 Requesty, #12 num_workers and #5 thinking-budget are occupied. Current pyproject version 2.0.0 is AGPL-3.0-or-later, not an AGPL version-2 license; coverage floor 86%.

**Repository checks:** `uv run pytest && uv run ruff check src tests`. Commands are proposed validation, not checks run on upstream changes in this session.

## CP01: Publish current v2 validation quickstart

- **Evidence/status:** [Source](https://github.com/starbaser/ccproxy/pull/16). Documentation hypothesis pending architecture agreement.
- **Source paths:** `README.md`, `pyproject.toml`, `docs/configuration.md`.
- **Scope:** Provide one current quickstart only after comparing existing docs; no architecture changes.
- **Non-goals:** Unrelated cleanup, dependency upgrades, and already implemented functionality.
- **Validation/acceptance:** Clean Python 3.13 dev environment executes documented non-e2e command; config loads; instructions match actual CLI and coverage policy. All stated scenarios must pass with preserved supported behavior and recorded reproduction evidence.
- **Effort:** 3-6 engineering hours after setup; excludes maintainer delay.
- **Dependencies/engagement:** HOLD until maintainer confirms responsiveness and compatibility with #16.
- **Value:** Produces demonstrable publish current v2 validation quickstart work useful to reliable local AI tooling and gateway operations; record shipped behavior and measured benefit for resume evidence.

- [ ] Inspect full source and current instructions, record SHA, and refresh overlapping work.
- [ ] Reproduce the concrete scenario; retire/re-scope if already addressed.
- [ ] Agree scope, implement one bounded change, and verify using the scenarios and repository checks above.
- [ ] Prepare a PR with before/after evidence and attribution when submission is authorized.

## CP02: Redacted inspection-export fixtures

- **Evidence/status:** [Source](https://github.com/starbaser/ccproxy/blob/HEAD/docs/privacy.md). Regression hypothesis, not vulnerability claim.
- **Source paths:** `src/ccproxy/inspector/egress_sanitizer_addon.py`, `docs/privacy.md`.
- **Scope:** Add only missing sanitizer/export regression cases after inspecting existing tests.
- **Non-goals:** Unrelated cleanup, dependency upgrades, and already implemented functionality.
- **Validation/acceptance:** Synthetic authorization/API-key/cookie sentinels absent from supported exports; useful request metadata preserved. All stated scenarios must pass with preserved supported behavior and recorded reproduction evidence.
- **Effort:** 4-8 engineering hours after setup; excludes maintainer delay.
- **Dependencies/engagement:** HOLD until maintainer confirms responsiveness and compatibility with #16.
- **Value:** Produces demonstrable redacted inspection-export fixtures work useful to reliable local AI tooling and gateway operations; record shipped behavior and measured benefit for resume evidence.

- [ ] Inspect full source and current instructions, record SHA, and refresh overlapping work.
- [ ] Reproduce the concrete scenario; retire/re-scope if already addressed.
- [ ] Agree scope, implement one bounded change, and verify using the scenarios and repository checks above.
- [ ] Prepare a PR with before/after evidence and attribution when submission is authorized.

## CP03: Auth-source backward-compatibility matrix

- **Evidence/status:** [Source](https://github.com/starbaser/ccproxy/blob/HEAD/src/ccproxy/auth/sources.py). Coverage hypothesis.
- **Source paths:** `src/ccproxy/auth/sources.py`, `tests/issues/regression/test_auth_source_backward_compat.py`.
- **Scope:** Extend existing auth-source tests and docs; no new provider or credential extraction mechanism.
- **Non-goals:** Unrelated cleanup, dependency upgrades, and already implemented functionality.
- **Validation/acceptance:** Supported legacy/current credential fixtures resolve consistently; absent source yields useful diagnostic; errors never include secret values. All stated scenarios must pass with preserved supported behavior and recorded reproduction evidence.
- **Effort:** 4-8 engineering hours after setup; excludes maintainer delay.
- **Dependencies/engagement:** HOLD until maintainer confirms responsiveness and compatibility with #16.
- **Value:** Produces demonstrable auth-source backward-compatibility matrix work useful to reliable local AI tooling and gateway operations; record shipped behavior and measured benefit for resume evidence.

- [ ] Inspect full source and current instructions, record SHA, and refresh overlapping work.
- [ ] Reproduce the concrete scenario; retire/re-scope if already addressed.
- [ ] Agree scope, implement one bounded change, and verify using the scenarios and repository checks above.
- [ ] Prepare a PR with before/after evidence and attribution when submission is authorized.

## CP04: Usage accounting stream parity

- **Evidence/status:** [Source](https://github.com/starbaser/ccproxy/blob/HEAD/src/ccproxy/lightllm/graph/_usage.py). Coverage hypothesis; architecture gated.
- **Source paths:** `src/ccproxy/lightllm/graph/_usage.py`, `tests/issues/regression/test_issue_usage_accounting.py`.
- **Scope:** Find actual uncovered accounting case; preserve existing canonical graph model.
- **Non-goals:** Unrelated cleanup, dependency upgrades, and already implemented functionality.
- **Validation/acceptance:** Identical logical response in buffered/streamed forms yields equal known counts; missing usage stays unknown; duplicate frames do not double-count. All stated scenarios must pass with preserved supported behavior and recorded reproduction evidence.
- **Effort:** 6-12 engineering hours after setup; excludes maintainer delay.
- **Dependencies/engagement:** HOLD until maintainer confirms responsiveness and compatibility with #16.
- **Value:** Produces demonstrable usage accounting stream parity work useful to reliable local AI tooling and gateway operations; record shipped behavior and measured benefit for resume evidence.

- [ ] Inspect full source and current instructions, record SHA, and refresh overlapping work.
- [ ] Reproduce the concrete scenario; retire/re-scope if already addressed.
- [ ] Agree scope, implement one bounded change, and verify using the scenarios and repository checks above.
- [ ] Prepare a PR with before/after evidence and attribution when submission is authorized.

## CP05: Packaged CLI configuration portability

- **Evidence/status:** [Source](https://github.com/starbaser/ccproxy/issues/8). Portability documentation/regression proposal.
- **Source paths:** `src/ccproxy/cli.py`, `tests/test_cli.py`, `docs/configuration.md`.
- **Scope:** Bound support matrix and path fixture; do not promise full native Windows support or duplicate open #12.
- **Non-goals:** Unrelated cleanup, dependency upgrades, and already implemented functionality.
- **Validation/acceptance:** Config path with spaces works on supported platform; missing path diagnostic useful; supported WSL procedure documented separately from native Windows. All stated scenarios must pass with preserved supported behavior and recorded reproduction evidence.
- **Effort:** 4-8 engineering hours after setup; excludes maintainer delay.
- **Dependencies/engagement:** HOLD until maintainer confirms responsiveness and compatibility with #16.
- **Value:** Produces demonstrable packaged cli configuration portability work useful to reliable local AI tooling and gateway operations; record shipped behavior and measured benefit for resume evidence.

- [ ] Inspect full source and current instructions, record SHA, and refresh overlapping work.
- [ ] Reproduce the concrete scenario; retire/re-scope if already addressed.
- [ ] Agree scope, implement one bounded change, and verify using the scenarios and repository checks above.
- [ ] Prepare a PR with before/after evidence and attribution when submission is authorized.
