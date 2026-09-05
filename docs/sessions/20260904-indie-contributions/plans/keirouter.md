# mydisha/keirouter: five contribution proposals

**Goal:** Five bounded contributions that improve real user workflows and can be offered independently after scope checks.

**Architecture:** Follow current upstream boundaries; reproduce reported behavior before changing code. Proposals are not implementations or verified defects unless explicitly stated.

**Tech stack:** Go / TypeScript.

Inspected September 5 UTC 2026. Evidence links and paths reflect the planning snapshot. Refresh source SHA and issue/PR ownership at execution time.

**Overlap and policy:** Coordinate with #65; do not duplicate merged #55/#64 or existing backup work #44.

**Repository checks:** `cd backend && go test ./... && go vet ./...`. Run focused scenarios first and then current upstream-required checks; commands here have not been run on proposed changes. If a test-package name changes, derive the current command from upstream manifests before implementation.

## KR01: Budget reservation isolation

- **Evidence/status:** [Source discussion](https://github.com/mydisha/keirouter/pull/65). Hypothesis: concurrency regression coverage.
- **Source:** `backend/internal/budget/budget.go`.
- **Proposed change:** Add a focused regression only if existing tests miss request isolation; repair the smallest demonstrated defect.
- **Non-goals:** Unrelated cleanup, dependency upgrades, architecture rewrites, and already merged functionality.
- **Validation and acceptance:** Interleave equal tenant/project identifiers, failed dispatch and cancellation; each request releases only its own reservation. Accept only when these scenarios pass and existing supported behavior remains unchanged; attach reproduction and verification results to the eventual PR.
- **Effort:** 4-8 engineering hours after setup, an estimate excluding review delays.
- **Dependencies/engagement:** Refresh overlapping PRs; agree any feature/API scope with the issue owner. No dependency on another proposed PR unless current upstream overlap requires one.
- **Value:** A demonstrable budget reservation isolation contribution creates a specific shipped-outcome resume artifact and improves a tool used in the Phenotype workflow; impact must be measured after delivery.

- [ ] Read current upstream instructions, record HEAD, and check issue ownership/open PR overlap.
- [ ] Exercise the validation scenario; if already passing, identify an actual missing case or retire this proposal.
- [ ] Agree the bounded scope, implement it with focused regression evidence, and run repository checks above.
- [ ] Prepare one PR with before/after behavior, tests, and source attribution when upstream submission is authorized.

## KR02: Budget cache invalidation ordering

- **Evidence/status:** [Source discussion](https://github.com/mydisha/keirouter/pull/65). Hypothesis: concurrent update coverage.
- **Source:** `backend/internal/budget/budget.go`.
- **Proposed change:** Add a missing concurrency fixture; change invalidation only if the fixture fails.
- **Non-goals:** Unrelated cleanup, dependency upgrades, architecture rewrites, and already merged functionality.
- **Validation and acceptance:** Interleave cached reads, an administrative limit update and invalidation; subsequent requests use the new limit. Accept only when these scenarios pass and existing supported behavior remains unchanged; attach reproduction and verification results to the eventual PR.
- **Effort:** 4-8 engineering hours after setup, an estimate excluding review delays.
- **Dependencies/engagement:** Refresh overlapping PRs; agree any feature/API scope with the issue owner. No dependency on another proposed PR unless current upstream overlap requires one.
- **Value:** A demonstrable budget cache invalidation ordering contribution creates a specific shipped-outcome resume artifact and improves a tool used in the Phenotype workflow; impact must be measured after delivery.

- [ ] Read current upstream instructions, record HEAD, and check issue ownership/open PR overlap.
- [ ] Exercise the validation scenario; if already passing, identify an actual missing case or retire this proposal.
- [ ] Agree the bounded scope, implement it with focused regression evidence, and run repository checks above.
- [ ] Prepare one PR with before/after behavior, tests, and source attribution when upstream submission is authorized.

## KR03: Provider throttling classification fixtures

- **Evidence/status:** [Source discussion](https://github.com/mydisha/keirouter/pull/55). Compatibility coverage proposal.
- **Source:** `backend/internal/connectors/classify429.go`, `backend/internal/connectors/classify429_test.go`.
- **Proposed change:** Add real sanitized provider fixtures, preserving existing backoff behavior.
- **Non-goals:** Unrelated cleanup, dependency upgrades, architecture rewrites, and already merged functionality.
- **Validation and acceptance:** Sanitized transient-throttle and exhausted-credit payloads classify distinctly; retries remain bounded. Accept only when these scenarios pass and existing supported behavior remains unchanged; attach reproduction and verification results to the eventual PR.
- **Effort:** 3-6 engineering hours after setup, an estimate excluding review delays.
- **Dependencies/engagement:** Refresh overlapping PRs; agree any feature/API scope with the issue owner. No dependency on another proposed PR unless current upstream overlap requires one.
- **Value:** A demonstrable provider throttling classification fixtures contribution creates a specific shipped-outcome resume artifact and improves a tool used in the Phenotype workflow; impact must be measured after delivery.

- [ ] Read current upstream instructions, record HEAD, and check issue ownership/open PR overlap.
- [ ] Exercise the validation scenario; if already passing, identify an actual missing case or retire this proposal.
- [ ] Agree the bounded scope, implement it with focused regression evidence, and run repository checks above.
- [ ] Prepare one PR with before/after behavior, tests, and source attribution when upstream submission is authorized.

## KR04: Reasoning/tool streaming regression matrix

- **Evidence/status:** [Source discussion](https://github.com/mydisha/keirouter/pull/64). Coverage proposal after merged fix.
- **Source:** `backend/internal/transform/openai_strip_reasoning_test.go`, `backend/internal/transform/openai_stream.go`.
- **Proposed change:** Extend current transform tests, fixing only demonstrated residual cases.
- **Non-goals:** Unrelated cleanup, dependency upgrades, architecture rewrites, and already merged functionality.
- **Validation and acceptance:** Fragment reasoning then tool calls, empty reasoning and rejection of reasoning fields; reconstructed responses preserve protocol behavior. Accept only when these scenarios pass and existing supported behavior remains unchanged; attach reproduction and verification results to the eventual PR.
- **Effort:** 4-8 engineering hours after setup, an estimate excluding review delays.
- **Dependencies/engagement:** Refresh overlapping PRs; agree any feature/API scope with the issue owner. No dependency on another proposed PR unless current upstream overlap requires one.
- **Value:** A demonstrable reasoning/tool streaming regression matrix contribution creates a specific shipped-outcome resume artifact and improves a tool used in the Phenotype workflow; impact must be measured after delivery.

- [ ] Read current upstream instructions, record HEAD, and check issue ownership/open PR overlap.
- [ ] Exercise the validation scenario; if already passing, identify an actual missing case or retire this proposal.
- [ ] Agree the bounded scope, implement it with focused regression evidence, and run repository checks above.
- [ ] Prepare one PR with before/after behavior, tests, and source attribution when upstream submission is authorized.

## KR05: Backup and restore operator drill

- **Evidence/status:** [Source discussion](https://github.com/mydisha/keirouter/pull/44). Documentation proposal.
- **Source:** `backend/internal/gateway/sqlite_backup.go`, `deploy/README.md`.
- **Proposed change:** Document exact versioned backup/restore commands after testing them; no backup-engine redesign.
- **Non-goals:** Unrelated cleanup, dependency upgrades, architecture rewrites, and already merged functionality.
- **Validation and acceptance:** Back up and restore into a separate temporary instance; compare configuration and usage counts and redact secrets. Accept only when these scenarios pass and existing supported behavior remains unchanged; attach reproduction and verification results to the eventual PR.
- **Effort:** 3-6 engineering hours after setup, an estimate excluding review delays.
- **Dependencies/engagement:** Refresh overlapping PRs; agree any feature/API scope with the issue owner. No dependency on another proposed PR unless current upstream overlap requires one.
- **Value:** A demonstrable backup and restore operator drill contribution creates a specific shipped-outcome resume artifact and improves a tool used in the Phenotype workflow; impact must be measured after delivery.

- [ ] Read current upstream instructions, record HEAD, and check issue ownership/open PR overlap.
- [ ] Exercise the validation scenario; if already passing, identify an actual missing case or retire this proposal.
- [ ] Agree the bounded scope, implement it with focused regression evidence, and run repository checks above.
- [ ] Prepare one PR with before/after behavior, tests, and source attribution when upstream submission is authorized.


