# Fast-Editor/Lynkr: five contribution proposals

**Goal:** Five bounded useful contributions, offered separately after scope and ownership checks.

**Architecture:** Preserve current upstream boundaries. These are plans, not implemented changes; reported bugs still require reproduction.

**Tech stack:** Node.js.

Inspected September 5 UTC 2026. Refresh HEAD and issue/PR state before execution.

**Overlap and policy:** Latest 50 issue/PR titles screened. Closed #100/#101 and #91/#92 already cover broad policy/streaming work; additions need an actual gap. Manifest requires Node >=20.

**Repository checks:** `npm run lint && npm run test:unit`. Commands are proposed validation, not checks run on upstream changes in this session. 

## LY01: Correct contributor runtime and commands

- **Evidence/status:** [Source](https://github.com/Fast-Editor/Lynkr/blob/HEAD/documentation/contributing.md). Verified documentation/manifest mismatch in research.
- **Source paths:** `documentation/contributing.md`, `package.json`.
- **Scope:** Align Node minimum and testing instructions with package.json; do not add a fake script solely to match prose.
- **Non-goals:** Unrelated cleanup, dependency upgrades, and already implemented functionality.
- **Validation/acceptance:** Guide commands resolve to actual scripts; supported Node runs documented offline subset; no nonexistent test:coverage command. All stated scenarios must pass with preserved supported behavior and recorded reproduction evidence.
- **Effort:** 2-4 engineering hours after setup; excludes maintainer delay.
- **Dependencies/engagement:** Check current issue ownership and coordinate feature scope; no dependency on other planned PRs unless upstream overlap requires it.
- **Value:** Produces demonstrable correct contributor runtime and commands work useful to reliable local AI tooling and gateway operations; record shipped behavior and measured benefit for resume evidence.

- [ ] Inspect full source and current instructions, record SHA, and refresh overlapping work.
- [ ] Reproduce the concrete scenario; retire/re-scope if already addressed.
- [ ] Agree scope, implement one bounded change, and verify using the scenarios and repository checks above.
- [ ] Prepare a PR with before/after evidence and attribution when submission is authorized.

## LY02: Atomic-save watcher regression

- **Evidence/status:** [Source](https://github.com/Fast-Editor/Lynkr/blob/HEAD/src/config/watcher.js). Hypothesis; implementation only partially read.
- **Source paths:** `src/config/watcher.js`.
- **Scope:** Read full watcher, add missing fixture, fix only demonstrated rename/rearm failure.
- **Non-goals:** Unrelated cleanup, dependency upgrades, and already implemented functionality.
- **Validation/acceptance:** Atomically replace .env, edit it again, stop watcher; subsequent reload works and handles close. All stated scenarios must pass with preserved supported behavior and recorded reproduction evidence.
- **Effort:** 4-8 engineering hours after setup; excludes maintainer delay.
- **Dependencies/engagement:** Check current issue ownership and coordinate feature scope; no dependency on other planned PRs unless upstream overlap requires it.
- **Value:** Produces demonstrable atomic-save watcher regression work useful to reliable local AI tooling and gateway operations; record shipped behavior and measured benefit for resume evidence.

- [ ] Inspect full source and current instructions, record SHA, and refresh overlapping work.
- [ ] Reproduce the concrete scenario; retire/re-scope if already addressed.
- [ ] Agree scope, implement one bounded change, and verify using the scenarios and repository checks above.
- [ ] Prepare a PR with before/after evidence and attribution when submission is authorized.

## LY03: Missing-file watcher startup guidance

- **Evidence/status:** [Source](https://github.com/Fast-Editor/Lynkr/blob/HEAD/src/config/watcher.js). Source skips absent files; discovery behavior needs agreement.
- **Source paths:** `src/config/watcher.js`, `documentation/contributing.md`.
- **Scope:** First document actual startup contract; implement later-file discovery only if maintainer wants it.
- **Non-goals:** Unrelated cleanup, dependency upgrades, and already implemented functionality.
- **Validation/acceptance:** Start without .env, create later, observe reload versus restart requirement. All stated scenarios must pass with preserved supported behavior and recorded reproduction evidence.
- **Effort:** 3-6 engineering hours after setup; excludes maintainer delay.
- **Dependencies/engagement:** Check current issue ownership and coordinate feature scope; no dependency on other planned PRs unless upstream overlap requires it.
- **Value:** Produces demonstrable missing-file watcher startup guidance work useful to reliable local AI tooling and gateway operations; record shipped behavior and measured benefit for resume evidence.

- [ ] Inspect full source and current instructions, record SHA, and refresh overlapping work.
- [ ] Reproduce the concrete scenario; retire/re-scope if already addressed.
- [ ] Agree scope, implement one bounded change, and verify using the scenarios and repository checks above.
- [ ] Prepare a PR with before/after evidence and attribution when submission is authorized.

## LY04: Tenant-policy edge cases across ingress

- **Evidence/status:** [Source](https://github.com/Fast-Editor/Lynkr/pull/100). Coverage proposal after merged policy changes.
- **Source paths:** `test/tenant-policy-ingress-parity.test.js`, `src/api/openai-router.js`.
- **Scope:** Extend current parity tests; avoid reintroducing or duplicating policy feature.
- **Non-goals:** Unrelated cleanup, dependency upgrades, and already implemented functionality.
- **Validation/acceptance:** Absent tenant, malformed metadata and denied model behave consistently across ingress formats. All stated scenarios must pass with preserved supported behavior and recorded reproduction evidence.
- **Effort:** 4-8 engineering hours after setup; excludes maintainer delay.
- **Dependencies/engagement:** Check current issue ownership and coordinate feature scope; no dependency on other planned PRs unless upstream overlap requires it.
- **Value:** Produces demonstrable tenant-policy edge cases across ingress work useful to reliable local AI tooling and gateway operations; record shipped behavior and measured benefit for resume evidence.

- [ ] Inspect full source and current instructions, record SHA, and refresh overlapping work.
- [ ] Reproduce the concrete scenario; retire/re-scope if already addressed.
- [ ] Agree scope, implement one bounded change, and verify using the scenarios and repository checks above.
- [ ] Prepare a PR with before/after evidence and attribution when submission is authorized.

## LY05: Streaming client cancellation fixtures

- **Evidence/status:** [Source](https://github.com/Fast-Editor/Lynkr/pull/92). Coverage hypothesis.
- **Source paths:** `src/orchestrator/passthrough-stream.js`, `test/passthrough-stream.test.js`.
- **Scope:** Prove missing coverage, add fixture and minimal fix if failing.
- **Non-goals:** Unrelated cleanup, dependency upgrades, and already implemented functionality.
- **Validation/acceptance:** Disconnect before first chunk and during partial tool-call; upstream cancels, resources close, no double completion. All stated scenarios must pass with preserved supported behavior and recorded reproduction evidence.
- **Effort:** 4-8 engineering hours after setup; excludes maintainer delay.
- **Dependencies/engagement:** Check current issue ownership and coordinate feature scope; no dependency on other planned PRs unless upstream overlap requires it.
- **Value:** Produces demonstrable streaming client cancellation fixtures work useful to reliable local AI tooling and gateway operations; record shipped behavior and measured benefit for resume evidence.

- [ ] Inspect full source and current instructions, record SHA, and refresh overlapping work.
- [ ] Reproduce the concrete scenario; retire/re-scope if already addressed.
- [ ] Agree scope, implement one bounded change, and verify using the scenarios and repository checks above.
- [ ] Prepare a PR with before/after evidence and attribution when submission is authorized.


