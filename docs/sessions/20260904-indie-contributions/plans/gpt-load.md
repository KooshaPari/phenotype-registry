# tbphp/gpt-load: five contribution proposals

**Goal:** Five bounded useful contributions, offered separately after scope and ownership checks.

**Architecture:** Preserve current upstream boundaries. These are plans, not implemented changes; reported bugs still require reproduction.

**Tech stack:** Go / Vue.

Inspected September 5 UTC 2026. Refresh HEAD and issue/PR state before execution.

**Overlap and policy:** Targets 2.x; do not reuse 1.x architecture. Open issues and open PR endpoint checked September 5; no open PRs returned at that instant. Runtime reports still require current reproduction.

**Repository checks:** `make test && make check`. Commands are proposed validation, not checks run on upstream changes in this session. 

## GL01: Recover transient subscription refresh failures

- **Evidence/status:** [Source](https://github.com/tbphp/gpt-load/issues/571). Reported 2.x bug; not reproduced.
- **Source paths:** `internal/subscription/credential_manager.go`, `internal/subscription/runtime/network.go`.
- **Scope:** Distinguish transient state and expose existing safe retry path; no auth bypass.
- **Non-goals:** Unrelated cleanup, dependency upgrades, and already implemented functionality.
- **Validation/acceptance:** Transient network refresh failure permits safe retry without reimport; actual invalid credentials stay invalid; concurrent retries coalesce. All stated scenarios must pass with preserved supported behavior and recorded reproduction evidence.
- **Effort:** 6-12 engineering hours after setup; excludes maintainer delay.
- **Dependencies/engagement:** Check current issue ownership and coordinate feature scope; no dependency on other planned PRs unless upstream overlap requires it.
- **Value:** Produces demonstrable recover transient subscription refresh failures work useful to reliable local AI tooling and gateway operations; record shipped behavior and measured benefit for resume evidence.

- [ ] Inspect full source and current instructions, record SHA, and refresh overlapping work.
- [ ] Reproduce the concrete scenario; retire/re-scope if already addressed.
- [ ] Agree scope, implement one bounded change, and verify using the scenarios and repository checks above.
- [ ] Prepare a PR with before/after evidence and attribution when submission is authorized.

## GL02: Preserve OpenCode session identity

- **Evidence/status:** [Source](https://github.com/tbphp/gpt-load/issues/542). Compatibility request; upstream deadline unverified.
- **Source paths:** `internal/channel/modules/openai_compatible.go`, `internal/affinity/key.go`.
- **Scope:** Agree session-header forwarding contract and source of identity; do not synthesize arbitrary per-request sessions.
- **Non-goals:** Unrelated cleanup, dependency upgrades, and already implemented functionality.
- **Validation/acceptance:** Same caller session survives streaming/unary/retries; different sessions isolated; unrelated upstreams unchanged. All stated scenarios must pass with preserved supported behavior and recorded reproduction evidence.
- **Effort:** 6-12 engineering hours after setup; excludes maintainer delay.
- **Dependencies/engagement:** Check current issue ownership and coordinate feature scope; no dependency on other planned PRs unless upstream overlap requires it.
- **Value:** Produces demonstrable preserve opencode session identity work useful to reliable local AI tooling and gateway operations; record shipped behavior and measured benefit for resume evidence.

- [ ] Inspect full source and current instructions, record SHA, and refresh overlapping work.
- [ ] Reproduce the concrete scenario; retire/re-scope if already addressed.
- [ ] Agree scope, implement one bounded change, and verify using the scenarios and repository checks above.
- [ ] Prepare a PR with before/after evidence and attribution when submission is authorized.

## GL03: Quick group enable/disable

- **Evidence/status:** [Source](https://github.com/tbphp/gpt-load/issues/554). Feature request; coordinate duplicate #555.
- **Source paths:** `web/src/features/groups/GroupsView.vue`, `web/src/features/groups/GroupHeader.vue`.
- **Scope:** Reuse existing update API for a single quick action; no backend schema change.
- **Non-goals:** Unrelated cleanup, dependency upgrades, and already implemented functionality.
- **Validation/acceptance:** Authorized toggle persists; API failure restores visible state; disabled state clearly shown; concurrent clicks do not race. All stated scenarios must pass with preserved supported behavior and recorded reproduction evidence.
- **Effort:** 4-8 engineering hours after setup; excludes maintainer delay.
- **Dependencies/engagement:** Check current issue ownership and coordinate feature scope; no dependency on other planned PRs unless upstream overlap requires it.
- **Value:** Produces demonstrable quick group enable/disable work useful to reliable local AI tooling and gateway operations; record shipped behavior and measured benefit for resume evidence.

- [ ] Inspect full source and current instructions, record SHA, and refresh overlapping work.
- [ ] Reproduce the concrete scenario; retire/re-scope if already addressed.
- [ ] Agree scope, implement one bounded change, and verify using the scenarios and repository checks above.
- [ ] Prepare a PR with before/after evidence and attribution when submission is authorized.

## GL04: Subscription-account weight editor

- **Evidence/status:** [Source](https://github.com/tbphp/gpt-load/issues/535). Reported UI omission; verify current HEAD.
- **Source paths:** `web/src/features/groups/credentials/SubscriptionAccountCard.vue`, `web/src/features/groups/credentials/GroupCredentialRecord.vue`.
- **Scope:** Reuse current credential weight update contract in subscription cards; no scheduler redesign.
- **Non-goals:** Unrelated cleanup, dependency upgrades, and already implemented functionality.
- **Validation/acceptance:** Auto/manual weight 1-100 persists; invalid values rejected; failed update preserves old value; API-key UI unchanged. All stated scenarios must pass with preserved supported behavior and recorded reproduction evidence.
- **Effort:** 4-8 engineering hours after setup; excludes maintainer delay.
- **Dependencies/engagement:** Check current issue ownership and coordinate feature scope; no dependency on other planned PRs unless upstream overlap requires it.
- **Value:** Produces demonstrable subscription-account weight editor work useful to reliable local AI tooling and gateway operations; record shipped behavior and measured benefit for resume evidence.

- [ ] Inspect full source and current instructions, record SHA, and refresh overlapping work.
- [ ] Reproduce the concrete scenario; retire/re-scope if already addressed.
- [ ] Agree scope, implement one bounded change, and verify using the scenarios and repository checks above.
- [ ] Prepare a PR with before/after evidence and attribution when submission is authorized.

## GL05: Quota-query interoperability example

- **Evidence/status:** [Source](https://github.com/tbphp/gpt-load/issues/563). Integration request; agree read-only contract.
- **Source paths:** `internal/subscription/passive_quota.go`, `README.md`.
- **Scope:** Start with a ccswitch-compatible documented query example if existing API suffices; separate new API design.
- **Non-goals:** Unrelated cleanup, dependency upgrades, and already implemented functionality.
- **Validation/acceptance:** Document supported quota endpoint using redacted fixture; expired/unavailable quota distinguished from zero; no credential exposure. All stated scenarios must pass with preserved supported behavior and recorded reproduction evidence.
- **Effort:** 3-6 engineering hours after setup; excludes maintainer delay.
- **Dependencies/engagement:** Check current issue ownership and coordinate feature scope; no dependency on other planned PRs unless upstream overlap requires it.
- **Value:** Produces demonstrable quota-query interoperability example work useful to reliable local AI tooling and gateway operations; record shipped behavior and measured benefit for resume evidence.

- [ ] Inspect full source and current instructions, record SHA, and refresh overlapping work.
- [ ] Reproduce the concrete scenario; retire/re-scope if already addressed.
- [ ] Agree scope, implement one bounded change, and verify using the scenarios and repository checks above.
- [ ] Prepare a PR with before/after evidence and attribution when submission is authorized.


