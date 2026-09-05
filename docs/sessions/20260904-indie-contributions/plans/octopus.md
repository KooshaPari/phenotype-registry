# bestruirui/octopus: five contribution proposals

**Goal:** Five bounded useful contributions, offered separately after scope and ownership checks.

**Architecture:** Preserve current upstream boundaries. These are plans, not implemented changes; reported bugs still require reproduction.

**Tech stack:** Go / TypeScript.

Inspected September 5 UTC 2026. Refresh HEAD and issue/PR state before execution.

**Overlap and policy:** CONTRIBUTING prohibits test files in submitted PRs; manually review AI-assisted content and keep fixture harnesses outside the patch. Confirm current #339/#376 overlap. No runtime reproduction in this planning session.

**Repository checks:** `go vet ./...`. Commands are proposed validation, not checks run on upstream changes in this session. Use external fixtures/manual replay; do not submit test files.

## OC01: Model context-window metadata

- **Evidence/status:** [Source](https://github.com/bestruirui/octopus/issues/377). Feature request; agree metadata meaning.
- **Source paths:** `internal/model/llm.go`, `web/src/components/modules/model/Item.tsx`.
- **Scope:** Add agreed metadata/UI field only; no automatic prompt truncation.
- **Non-goals:** Unrelated cleanup, dependency upgrades, and already implemented functionality.
- **Validation/acceptance:** Set/clear/save/reload limit; show correct value; reject negatives without changing routing implicitly. All stated scenarios must pass with preserved supported behavior and recorded reproduction evidence.
- **Effort:** 6-12 engineering hours after setup; excludes maintainer delay.
- **Dependencies/engagement:** Check current issue ownership and coordinate feature scope; no dependency on other planned PRs unless upstream overlap requires it.
- **Value:** Produces demonstrable model context-window metadata work useful to reliable local AI tooling and gateway operations; record shipped behavior and measured benefit for resume evidence.

- [ ] Inspect full source and current instructions, record SHA, and refresh overlapping work.
- [ ] Reproduce the concrete scenario; retire/re-scope if already addressed.
- [ ] Agree scope, implement one bounded change, and verify using the scenarios and repository checks above.
- [ ] Prepare a PR with before/after evidence and attribution when submission is authorized.

## OC02: Bound failed attempts per request

- **Evidence/status:** [Source](https://github.com/bestruirui/octopus/issues/374). Feature request overlapping #339/#376.
- **Source paths:** `internal/relay/state.go`, `internal/relay/handler.go`.
- **Scope:** Agree one request-level cap and extend existing logic, not a parallel retry engine.
- **Non-goals:** Unrelated cleanup, dependency upgrades, and already implemented functionality.
- **Validation/acceptance:** Repeated upstream errors stop at configured limit; eventual success passes; cancellation and committed response never retry. All stated scenarios must pass with preserved supported behavior and recorded reproduction evidence.
- **Effort:** 6-12 engineering hours after setup; excludes maintainer delay.
- **Dependencies/engagement:** Check current issue ownership and coordinate feature scope; no dependency on other planned PRs unless upstream overlap requires it.
- **Value:** Produces demonstrable bound failed attempts per request work useful to reliable local AI tooling and gateway operations; record shipped behavior and measured benefit for resume evidence.

- [ ] Inspect full source and current instructions, record SHA, and refresh overlapping work.
- [ ] Reproduce the concrete scenario; retire/re-scope if already addressed.
- [ ] Agree scope, implement one bounded change, and verify using the scenarios and repository checks above.
- [ ] Prepare a PR with before/after evidence and attribution when submission is authorized.

## OC03: Reasoning effort in request logs

- **Evidence/status:** [Source](https://github.com/bestruirui/octopus/issues/337). Feature request.
- **Source paths:** `internal/relay/state.go`, `web/src/components/modules/log/Item.tsx`.
- **Scope:** Propagate bounded effort metadata into existing log UI.
- **Non-goals:** Unrelated cleanup, dependency upgrades, and already implemented functionality.
- **Validation/acceptance:** Explicit supported effort appears; absent values omitted; payload text and secrets never enter metadata. All stated scenarios must pass with preserved supported behavior and recorded reproduction evidence.
- **Effort:** 4-8 engineering hours after setup; excludes maintainer delay.
- **Dependencies/engagement:** Check current issue ownership and coordinate feature scope; no dependency on other planned PRs unless upstream overlap requires it.
- **Value:** Produces demonstrable reasoning effort in request logs work useful to reliable local AI tooling and gateway operations; record shipped behavior and measured benefit for resume evidence.

- [ ] Inspect full source and current instructions, record SHA, and refresh overlapping work.
- [ ] Reproduce the concrete scenario; retire/re-scope if already addressed.
- [ ] Agree scope, implement one bounded change, and verify using the scenarios and repository checks above.
- [ ] Prepare a PR with before/after evidence and attribution when submission is authorized.

## OC04: Reverse-proxy subpath deployment

- **Evidence/status:** [Source](https://github.com/bestruirui/octopus/issues/353). Feature request; reproduce current limits.
- **Source paths:** `web/vite.config.ts`, `web/src/api/client.ts`, `internal/server/middleware/static.go`.
- **Scope:** Agree one configurable base-path contract across web/API; avoid unrelated proxy changes.
- **Non-goals:** Unrelated cleanup, dependency upgrades, and already implemented functionality.
- **Validation/acceptance:** Serve /octopus/; login, reload, API, assets and log streaming work; root deployment unchanged. All stated scenarios must pass with preserved supported behavior and recorded reproduction evidence.
- **Effort:** 8-16 engineering hours after setup; excludes maintainer delay.
- **Dependencies/engagement:** Check current issue ownership and coordinate feature scope; no dependency on other planned PRs unless upstream overlap requires it.
- **Value:** Produces demonstrable reverse-proxy subpath deployment work useful to reliable local AI tooling and gateway operations; record shipped behavior and measured benefit for resume evidence.

- [ ] Inspect full source and current instructions, record SHA, and refresh overlapping work.
- [ ] Reproduce the concrete scenario; retire/re-scope if already addressed.
- [ ] Agree scope, implement one bounded change, and verify using the scenarios and repository checks above.
- [ ] Prepare a PR with before/after evidence and attribution when submission is authorized.

## OC05: Slow log-subscriber recovery drill

- **Evidence/status:** [Source](https://github.com/bestruirui/octopus/pull/364). Operational hypothesis after merged SSE fix.
- **Source paths:** `internal/relay/state.go`, `internal/server/handlers/log.go`.
- **Scope:** Document observed recovery; submit code only for a demonstrated missing behavior, excluding merged flush fix.
- **Non-goals:** Unrelated cleanup, dependency upgrades, and already implemented functionality.
- **Validation/acceptance:** Fill 16-message buffer; observe disconnect/reconnect snapshot, ordering and cleanup. All stated scenarios must pass with preserved supported behavior and recorded reproduction evidence.
- **Effort:** 3-6 engineering hours after setup; excludes maintainer delay.
- **Dependencies/engagement:** Check current issue ownership and coordinate feature scope; no dependency on other planned PRs unless upstream overlap requires it.
- **Value:** Produces demonstrable slow log-subscriber recovery drill work useful to reliable local AI tooling and gateway operations; record shipped behavior and measured benefit for resume evidence.

- [ ] Inspect full source and current instructions, record SHA, and refresh overlapping work.
- [ ] Reproduce the concrete scenario; retire/re-scope if already addressed.
- [ ] Agree scope, implement one bounded change, and verify using the scenarios and repository checks above.
- [ ] Prepare a PR with before/after evidence and attribution when submission is authorized.


