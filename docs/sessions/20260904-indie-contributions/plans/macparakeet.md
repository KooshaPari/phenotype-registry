# moona3k/macparakeet: five contribution proposals

**Goal:** Five bounded contributions that improve real user workflows and can be offered independently after scope checks.

**Architecture:** Follow current upstream boundaries; reproduce reported behavior before changing code. Proposals are not implementations or verified defects unless explicitly stated.

**Tech stack:** Swift / macOS.

Inspected September 5 UTC 2026. Evidence links and paths reflect the planning snapshot. Refresh source SHA and issue/PR ownership at execution time.

**Overlap and policy:** Exclude merged #946, microphone #950, open silence work #913 and preference work #876. Compare #728 for meeting titles. Use appropriate swift test --filter suites listed per scenario.

**Repository checks:** `swift test`. Run focused scenarios first and then current upstream-required checks; commands here have not been run on proposed changes. If a test-package name changes, derive the current command from upstream manifests before implementation.

## MP01: Stable OpenCode Go session headers

- **Evidence/status:** [Source discussion](https://github.com/moona3k/macparakeet/issues/948). Provider compatibility request.
- **Source:** `Sources/MacParakeetCore/Services/LLM/OpenAICompatibleLLMHTTPAdapter.swift`, `Sources/MacParakeetCore/Services/LLM/LLMExecutionContext.swift`.
- **Proposed change:** Carry session identity through provider-specific requests; independently verify reporter's claimed September 6 enforcement deadline.
- **Non-goals:** Unrelated cleanup, dependency upgrades, architecture rewrites, and already merged functionality.
- **Validation and acceptance:** LLMHTTPAdapterTests: same conversation shares x-opencode-session across streaming/unary/retries; different conversation differs; other endpoints get no header. Accept only when these scenarios pass and existing supported behavior remains unchanged; attach reproduction and verification results to the eventual PR.
- **Effort:** 4-8 engineering hours after setup, an estimate excluding review delays.
- **Dependencies/engagement:** Refresh overlapping PRs; agree any feature/API scope with the issue owner. No dependency on another proposed PR unless current upstream overlap requires one.
- **Value:** A demonstrable stable opencode go session headers contribution creates a specific shipped-outcome resume artifact and improves a tool used in the Phenotype workflow; impact must be measured after delivery.

- [ ] Read current upstream instructions, record HEAD, and check issue ownership/open PR overlap.
- [ ] Exercise the validation scenario; if already passing, identify an actual missing case or retire this proposal.
- [ ] Agree the bounded scope, implement it with focused regression evidence, and run repository checks above.
- [ ] Prepare one PR with before/after behavior, tests, and source attribution when upstream submission is authorized.

## MP02: Clarify local HTTP opt-in validation

- **Evidence/status:** [Source discussion](https://github.com/moona3k/macparakeet/issues/922). Reported behavior may be intentional.
- **Source:** `Sources/MacParakeetViewModels/LLMSettingsDraft.swift`, `Sources/MacParakeetViewModels/LLMSettingsViewModel.swift`.
- **Proposed change:** Reproduce first; improve precise error text/tests if current local-network restriction is intentional.
- **Non-goals:** Unrelated cleanup, dependency upgrades, architecture rewrites, and already merged functionality.
- **Validation and acceptance:** LLMSettingsDraftTests: local IP HTTP only with opt-in, public HTTP rejected, HTTPS accepted, setting persists. Accept only when these scenarios pass and existing supported behavior remains unchanged; attach reproduction and verification results to the eventual PR.
- **Effort:** 3-6 engineering hours after setup, an estimate excluding review delays.
- **Dependencies/engagement:** Refresh overlapping PRs; agree any feature/API scope with the issue owner. No dependency on another proposed PR unless current upstream overlap requires one.
- **Value:** A demonstrable clarify local http opt-in validation contribution creates a specific shipped-outcome resume artifact and improves a tool used in the Phenotype workflow; impact must be measured after delivery.

- [ ] Read current upstream instructions, record HEAD, and check issue ownership/open PR overlap.
- [ ] Exercise the validation scenario; if already passing, identify an actual missing case or retire this proposal.
- [ ] Agree the bounded scope, implement it with focused regression evidence, and run repository checks above.
- [ ] Prepare one PR with before/after behavior, tests, and source attribution when upstream submission is authorized.

## MP03: Refresh meeting title after rename

- **Evidence/status:** [Source discussion](https://github.com/moona3k/macparakeet/issues/904). Older version report; current reproduction required.
- **Source:** `Sources/MacParakeetViewModels/MeetingsWorkspaceViewModel.swift`, `Sources/MacParakeet/Views/Meetings/MeetingsView.swift`.
- **Proposed change:** Fix residual state propagation only after comparing merged #728.
- **Non-goals:** Unrelated cleanup, dependency upgrades, architecture rewrites, and already merged functionality.
- **Validation and acceptance:** MeetingsWorkspaceViewModelTests: list/detail agree after rename and relaunch; persistence rejection keeps prior title; stale refresh cannot overwrite rename. Accept only when these scenarios pass and existing supported behavior remains unchanged; attach reproduction and verification results to the eventual PR.
- **Effort:** 4-8 engineering hours after setup, an estimate excluding review delays.
- **Dependencies/engagement:** Refresh overlapping PRs; agree any feature/API scope with the issue owner. No dependency on another proposed PR unless current upstream overlap requires one.
- **Value:** A demonstrable refresh meeting title after rename contribution creates a specific shipped-outcome resume artifact and improves a tool used in the Phenotype workflow; impact must be measured after delivery.

- [ ] Read current upstream instructions, record HEAD, and check issue ownership/open PR overlap.
- [ ] Exercise the validation scenario; if already passing, identify an actual missing case or retire this proposal.
- [ ] Agree the bounded scope, implement it with focused regression evidence, and run repository checks above.
- [ ] Prepare one PR with before/after behavior, tests, and source attribution when upstream submission is authorized.

## MP04: Strip CLI terminal controls from prose

- **Evidence/status:** [Source discussion](https://github.com/moona3k/macparakeet/issues/888). Reported artifact; cause unproven.
- **Source:** `Sources/MacParakeetCore/Services/LLM/LocalCLIExecutor.swift`, `Sources/MacParakeetCore/Services/LLM/LocalCLILLMClient.swift`.
- **Proposed change:** Agree normalization in prose adapter; preserve generic executor's documented verbatim stdout contract.
- **Non-goals:** Unrelated cleanup, dependency upgrades, architecture rewrites, and already merged functionality.
- **Validation and acceptance:** LocalCLILLMClientTests: ESC (B and CSI m around Unicode prose disappear; text/newlines remain; plain output unchanged; stderr diagnostic. Accept only when these scenarios pass and existing supported behavior remains unchanged; attach reproduction and verification results to the eventual PR.
- **Effort:** 4-8 engineering hours after setup, an estimate excluding review delays.
- **Dependencies/engagement:** Refresh overlapping PRs; agree any feature/API scope with the issue owner. No dependency on another proposed PR unless current upstream overlap requires one.
- **Value:** A demonstrable strip cli terminal controls from prose contribution creates a specific shipped-outcome resume artifact and improves a tool used in the Phenotype workflow; impact must be measured after delivery.

- [ ] Read current upstream instructions, record HEAD, and check issue ownership/open PR overlap.
- [ ] Exercise the validation scenario; if already passing, identify an actual missing case or retire this proposal.
- [ ] Agree the bounded scope, implement it with focused regression evidence, and run repository checks above.
- [ ] Prepare one PR with before/after behavior, tests, and source attribution when upstream submission is authorized.

## MP05: Self-speaker name in new exports

- **Evidence/status:** [Source discussion](https://github.com/moona3k/macparakeet/issues/938). Feature request.
- **Source:** `Sources/MacParakeetCore/Services/MeetingRecording/MeetingMarkdownRenderer.swift`, `Sources/MacParakeetCore/Services/MeetingRecording/MeetingTitleGenerator.swift`.
- **Proposed change:** Add configured display label for new exports; exclude voice identification and historical transcript rewriting.
- **Non-goals:** Unrelated cleanup, dependency upgrades, architecture rewrites, and already merged functionality.
- **Validation and acceptance:** MeetingMarkdownRendererClipboardTests: default Me, Unicode configured name, blank fallback, safe Markdown characters, other speakers unchanged. Accept only when these scenarios pass and existing supported behavior remains unchanged; attach reproduction and verification results to the eventual PR.
- **Effort:** 6-12 engineering hours after setup, an estimate excluding review delays.
- **Dependencies/engagement:** Refresh overlapping PRs; agree any feature/API scope with the issue owner. No dependency on another proposed PR unless current upstream overlap requires one.
- **Value:** A demonstrable self-speaker name in new exports contribution creates a specific shipped-outcome resume artifact and improves a tool used in the Phenotype workflow; impact must be measured after delivery.

- [ ] Read current upstream instructions, record HEAD, and check issue ownership/open PR overlap.
- [ ] Exercise the validation scenario; if already passing, identify an actual missing case or retire this proposal.
- [ ] Agree the bounded scope, implement it with focused regression evidence, and run repository checks above.
- [ ] Prepare one PR with before/after behavior, tests, and source attribution when upstream submission is authorized.


