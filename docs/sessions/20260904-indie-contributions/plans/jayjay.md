# hewigovens/jayjay: five contribution proposals

**Goal:** Five bounded contributions that improve real user workflows and can be offered independently after scope checks.

**Architecture:** Follow current upstream boundaries; reproduce reported behavior before changing code. Proposals are not implementations or verified defects unless explicitly stated.

**Tech stack:** Rust / Swift / GPUI.

Inspected September 5 UTC 2026. Evidence links and paths reflect the planning snapshot. Refresh source SHA and issue/PR ownership at execution time.

**Overlap and policy:** GPUI manifest declares BUSL-1.1; do not infer commercial reuse rights. Avoid DAG #202/hunk #218. #187 description work overlaps merged #194.

**Repository checks:** `cargo test -p jayjay-core && cargo test -p jayjay-gpui`. Run focused scenarios first and then current upstream-required checks; commands here have not been run on proposed changes. If a test-package name changes, derive the current command from upstream manifests before implementation.

## JJ01: Restore recent repository on pathless launch

- **Evidence/status:** [Source discussion](https://github.com/hewigovens/jayjay/issues/215). Source-backed hypothesis; runtime reproduction pending.
- **Source:** `shell/gpui/src/main.rs`.
- **Proposed change:** Correct fallback/recording ordering without changing explicit path behavior.
- **Non-goals:** Unrelated cleanup, dependency upgrades, architecture rewrites, and already merged functionality.
- **Validation and acceptance:** Explicit path wins, valid cwd works, invalid cwd restores valid recent, invalid recent opens picker; failed opens never enter recents. Accept only when these scenarios pass and existing supported behavior remains unchanged; attach reproduction and verification results to the eventual PR.
- **Effort:** 4-8 engineering hours after setup, an estimate excluding review delays.
- **Dependencies/engagement:** Refresh overlapping PRs; agree any feature/API scope with the issue owner. No dependency on another proposed PR unless current upstream overlap requires one.
- **Value:** A demonstrable restore recent repository on pathless launch contribution creates a specific shipped-outcome resume artifact and improves a tool used in the Phenotype workflow; impact must be measured after delivery.

- [ ] Read current upstream instructions, record HEAD, and check issue ownership/open PR overlap.
- [ ] Exercise the validation scenario; if already passing, identify an actual missing case or retire this proposal.
- [ ] Agree the bounded scope, implement it with focused regression evidence, and run repository checks above.
- [ ] Prepare one PR with before/after behavior, tests, and source attribution when upstream submission is authorized.

## JJ02: Restore evolog into a mutable change

- **Evidence/status:** [Source discussion](https://github.com/hewigovens/jayjay/issues/166). Feature request; agree core/macOS slice.
- **Source:** `crates/jayjay-core/src/repo/mutations_files.rs`, `shell/mac/Sources/JayJay/Detail/Evolog/EvologViewModel.swift`.
- **Proposed change:** Implement agreed whole-tree restore; GPUI parity remains explicit before closing entire issue.
- **Non-goals:** Unrelated cleanup, dependency upgrades, architecture rewrites, and already merged functionality.
- **Validation and acceptance:** Selected historical tree restored exactly; immutable target disabled; operation undoable; view refreshes. Accept only when these scenarios pass and existing supported behavior remains unchanged; attach reproduction and verification results to the eventual PR.
- **Effort:** 12-20 engineering hours after setup, an estimate excluding review delays.
- **Dependencies/engagement:** Refresh overlapping PRs; agree any feature/API scope with the issue owner. No dependency on another proposed PR unless current upstream overlap requires one.
- **Value:** A demonstrable restore evolog into a mutable change contribution creates a specific shipped-outcome resume artifact and improves a tool used in the Phenotype workflow; impact must be measured after delivery.

- [ ] Read current upstream instructions, record HEAD, and check issue ownership/open PR overlap.
- [ ] Exercise the validation scenario; if already passing, identify an actual missing case or retire this proposal.
- [ ] Agree the bounded scope, implement it with focused regression evidence, and run repository checks above.
- [ ] Prepare one PR with before/after behavior, tests, and source attribution when upstream submission is authorized.

## JJ03: Single-revision rebase mode

- **Evidence/status:** [Source discussion](https://github.com/hewigovens/jayjay/issues/169). First slice of shared feature request.
- **Source:** `crates/jayjay-core/src/repo/mutations.rs`, `shell/mac/Sources/JayJay/Repo/ViewModel/Actions/RepoViewModel+Rebase.swift`.
- **Proposed change:** Add explicit mode through core and macOS UI after agreeing semantics.
- **Non-goals:** Unrelated cleanup, dependency upgrades, architecture rewrites, and already merged functionality.
- **Validation and acceptance:** Move middle revision in three-change stack; children reattach to prior parent; default mode unchanged; conflict/immutable guards retained. Accept only when these scenarios pass and existing supported behavior remains unchanged; attach reproduction and verification results to the eventual PR.
- **Effort:** 10-18 engineering hours after setup, an estimate excluding review delays.
- **Dependencies/engagement:** Refresh overlapping PRs; agree any feature/API scope with the issue owner. No dependency on another proposed PR unless current upstream overlap requires one.
- **Value:** A demonstrable single-revision rebase mode contribution creates a specific shipped-outcome resume artifact and improves a tool used in the Phenotype workflow; impact must be measured after delivery.

- [ ] Read current upstream instructions, record HEAD, and check issue ownership/open PR overlap.
- [ ] Exercise the validation scenario; if already passing, identify an actual missing case or retire this proposal.
- [ ] Agree the bounded scope, implement it with focused regression evidence, and run repository checks above.
- [ ] Prepare one PR with before/after behavior, tests, and source attribution when upstream submission is authorized.

## JJ04: Rebase branch onto trunk action

- **Evidence/status:** [Source discussion](https://github.com/hewigovens/jayjay/issues/169). Second slice; depends on JJ03 API agreement.
- **Source:** `crates/jayjay-core/src/repo/git/sync.rs`, `crates/jayjay-core/src/repo/mutations.rs`.
- **Proposed change:** Expose separate explicit action; coordinate same issue owner to avoid duplicate submissions.
- **Non-goals:** Unrelated cleanup, dependency upgrades, architecture rewrites, and already merged functionality.
- **Validation and acceptance:** Stale stack moves to resolved trunk; current stack no-ops; missing trunk gives useful error; no fetch/push side effects. Accept only when these scenarios pass and existing supported behavior remains unchanged; attach reproduction and verification results to the eventual PR.
- **Effort:** 8-14 engineering hours after setup, an estimate excluding review delays.
- **Dependencies/engagement:** Refresh overlapping PRs; agree any feature/API scope with the issue owner. Depends on JJ03 mode API agreement.
- **Value:** A demonstrable rebase branch onto trunk action contribution creates a specific shipped-outcome resume artifact and improves a tool used in the Phenotype workflow; impact must be measured after delivery.

- [ ] Read current upstream instructions, record HEAD, and check issue ownership/open PR overlap.
- [ ] Exercise the validation scenario; if already passing, identify an actual missing case or retire this proposal.
- [ ] Agree the bounded scope, implement it with focused regression evidence, and run repository checks above.
- [ ] Prepare one PR with before/after behavior, tests, and source attribution when upstream submission is authorized.

## JJ05: Local Markdown images in GPUI

- **Evidence/status:** [Source discussion](https://github.com/hewigovens/jayjay/issues/165). Source confirms placeholder-only image block.
- **Source:** `shell/gpui/src/diff/markdown_diff/blocks.rs`.
- **Proposed change:** Render bounded repository-local images; retain fallback for unsupported inputs.
- **Non-goals:** Unrelated cleanup, dependency upgrades, architecture rewrites, and already merged functionality.
- **Validation and acceptance:** Read relative PNG from selected revision despite differing worktree; missing/unsupported retains placeholder; size bounded; no automatic URL fetch. Accept only when these scenarios pass and existing supported behavior remains unchanged; attach reproduction and verification results to the eventual PR.
- **Effort:** 8-14 engineering hours after setup, an estimate excluding review delays.
- **Dependencies/engagement:** Refresh overlapping PRs; agree any feature/API scope with the issue owner. No dependency on another proposed PR unless current upstream overlap requires one.
- **Value:** A demonstrable local markdown images in gpui contribution creates a specific shipped-outcome resume artifact and improves a tool used in the Phenotype workflow; impact must be measured after delivery.

- [ ] Read current upstream instructions, record HEAD, and check issue ownership/open PR overlap.
- [ ] Exercise the validation scenario; if already passing, identify an actual missing case or retire this proposal.
- [ ] Agree the bounded scope, implement it with focused regression evidence, and run repository checks above.
- [ ] Prepare one PR with before/after behavior, tests, and source attribution when upstream submission is authorized.
