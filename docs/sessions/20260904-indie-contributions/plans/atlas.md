# pacifio/atlas: five contribution proposals

**Goal:** Five bounded contributions that improve real user workflows and can be offered independently after scope checks.

**Architecture:** Follow current upstream boundaries; reproduce reported behavior before changing code. Proposals are not implementations or verified defects unless explicitly stated.

**Tech stack:** TypeScript / Rust desktop.

Inspected September 5 UTC 2026. Evidence links and paths reflect the planning snapshot. Refresh source SHA and issue/PR ownership at execution time.

**Overlap and policy:** Native changes add bun run test:rust. Exclude implemented #69 anonymity, #195 aria-label work, open #227 keybindings/#237 streaming/#214 dark themes.

**Repository checks:** `bun run test && bun run typecheck && bun run lint`. Run focused scenarios first and then current upstream-required checks; commands here have not been run on proposed changes. If a test-package name changes, derive the current command from upstream manifests before implementation.

## AT01: One supported light palette

- **Evidence/status:** [Source discussion](https://github.com/pacifio/atlas/issues/238). Feature request; dark primitives require agreement.
- **Source:** `src/features/theme/themes.ts`, `src/features/theme/apply-atlas-theme.ts`, `src/features/settings/components/atlas-themes-settings.tsx`.
- **Proposed change:** Agree one bounded palette migration, not a theme-system rewrite.
- **Non-goals:** Unrelated cleanup, dependency upgrades, architecture rewrites, and already merged functionality.
- **Validation and acceptance:** Palette persists; settings/overlays/disabled text/selection readable in screenshots; dark palettes unchanged. Accept only when these scenarios pass and existing supported behavior remains unchanged; attach reproduction and verification results to the eventual PR.
- **Effort:** 10-18 engineering hours after setup, an estimate excluding review delays.
- **Dependencies/engagement:** Refresh overlapping PRs; agree any feature/API scope with the issue owner. No dependency on another proposed PR unless current upstream overlap requires one.
- **Value:** A demonstrable one supported light palette contribution creates a specific shipped-outcome resume artifact and improves a tool used in the Phenotype workflow; impact must be measured after delivery.

- [ ] Read current upstream instructions, record HEAD, and check issue ownership/open PR overlap.
- [ ] Exercise the validation scenario; if already passing, identify an actual missing case or retire this proposal.
- [ ] Agree the bounded scope, implement it with focused regression evidence, and run repository checks above.
- [ ] Prepare one PR with before/after behavior, tests, and source attribution when upstream submission is authorized.

## AT02: Opt-in idle-sleep prevention

- **Evidence/status:** [Source discussion](https://github.com/pacifio/atlas/issues/68). Feature request; new native module path to agree.
- **Source:** `src/features/chat/stores/chat-store.ts`, `src/features/settings/lib/app-settings.ts`.
- **Proposed change:** Start macOS with opt-in setting and document other-platform gap; agree native module location before code.
- **Non-goals:** Unrelated cleanup, dependency upgrades, architecture rewrites, and already merged functionality.
- **Validation and acceptance:** Two runs acquire one ref-counted assertion; completion/cancel/error/disable release correctly; waiting-user policy explicit; exit releases. Accept only when these scenarios pass and existing supported behavior remains unchanged; attach reproduction and verification results to the eventual PR.
- **Effort:** 8-16 engineering hours after setup, an estimate excluding review delays.
- **Dependencies/engagement:** Refresh overlapping PRs; agree any feature/API scope with the issue owner. No dependency on another proposed PR unless current upstream overlap requires one.
- **Value:** A demonstrable opt-in idle-sleep prevention contribution creates a specific shipped-outcome resume artifact and improves a tool used in the Phenotype workflow; impact must be measured after delivery.

- [ ] Read current upstream instructions, record HEAD, and check issue ownership/open PR overlap.
- [ ] Exercise the validation scenario; if already passing, identify an actual missing case or retire this proposal.
- [ ] Agree the bounded scope, implement it with focused regression evidence, and run repository checks above.
- [ ] Prepare one PR with before/after behavior, tests, and source attribution when upstream submission is authorized.

## AT03: Quote completed-agent text into draft

- **Evidence/status:** [Source discussion](https://github.com/pacifio/atlas/issues/74). Feature request; old issue path obsolete.
- **Source:** `src/features/chat/components/transcript.tsx`, `src/features/chat/components/transcript-rows.tsx`, `src/features/chat/components/message-input.tsx`.
- **Proposed change:** Implement in current transcript architecture, not obsolete message-item.tsx.
- **Non-goals:** Unrelated cleanup, dependency upgrades, architecture rewrites, and already merged functionality.
- **Validation and acceptance:** Multiline/code selection inserted exactly while preserving draft; exclude streaming/user rows; keyboard and scrolling work. Accept only when these scenarios pass and existing supported behavior remains unchanged; attach reproduction and verification results to the eventual PR.
- **Effort:** 6-12 engineering hours after setup, an estimate excluding review delays.
- **Dependencies/engagement:** Refresh overlapping PRs; agree any feature/API scope with the issue owner. No dependency on another proposed PR unless current upstream overlap requires one.
- **Value:** A demonstrable quote completed-agent text into draft contribution creates a specific shipped-outcome resume artifact and improves a tool used in the Phenotype workflow; impact must be measured after delivery.

- [ ] Read current upstream instructions, record HEAD, and check issue ownership/open PR overlap.
- [ ] Exercise the validation scenario; if already passing, identify an actual missing case or retire this proposal.
- [ ] Agree the bounded scope, implement it with focused regression evidence, and run repository checks above.
- [ ] Prepare one PR with before/after behavior, tests, and source attribution when upstream submission is authorized.

## AT04: Focused workspace-control help

- **Evidence/status:** [Source discussion](https://github.com/pacifio/atlas/issues/71). Scoped UX proposal; some tooltips intentionally removed.
- **Source:** `src/components/titlebar.tsx`.
- **Proposed change:** Agree exact controls before adding help; preserve existing aria labels and avoid blanket tooltip restoration.
- **Non-goals:** Unrelated cleanup, dependency upgrades, architecture rewrites, and already merged functionality.
- **Validation and acceptance:** Chosen controls expose destination on hover/focus; dismissal works; tooltip stays in viewport. Accept only when these scenarios pass and existing supported behavior remains unchanged; attach reproduction and verification results to the eventual PR.
- **Effort:** 3-6 engineering hours after setup, an estimate excluding review delays.
- **Dependencies/engagement:** Refresh overlapping PRs; agree any feature/API scope with the issue owner. No dependency on another proposed PR unless current upstream overlap requires one.
- **Value:** A demonstrable focused workspace-control help contribution creates a specific shipped-outcome resume artifact and improves a tool used in the Phenotype workflow; impact must be measured after delivery.

- [ ] Read current upstream instructions, record HEAD, and check issue ownership/open PR overlap.
- [ ] Exercise the validation scenario; if already passing, identify an actual missing case or retire this proposal.
- [ ] Agree the bounded scope, implement it with focused regression evidence, and run repository checks above.
- [ ] Prepare one PR with before/after behavior, tests, and source attribution when upstream submission is authorized.

## AT05: Preserve manual chat titles

- **Evidence/status:** [Source discussion](https://github.com/pacifio/atlas/issues/70). Regression hypothesis; auto-title already exists.
- **Source:** `src/features/chat/stores/chat-store.ts`.
- **Proposed change:** Only implement if fixture demonstrates overwrite; do not claim auto-title is absent.
- **Non-goals:** Unrelated cleanup, dependency upgrades, architecture rewrites, and already merged functionality.
- **Validation and acceptance:** Rename survives later title_updated; untouched default adopts generated title; events idempotent and sessions isolated. Accept only when these scenarios pass and existing supported behavior remains unchanged; attach reproduction and verification results to the eventual PR.
- **Effort:** 4-8 engineering hours after setup, an estimate excluding review delays.
- **Dependencies/engagement:** Refresh overlapping PRs; agree any feature/API scope with the issue owner. No dependency on another proposed PR unless current upstream overlap requires one.
- **Value:** A demonstrable preserve manual chat titles contribution creates a specific shipped-outcome resume artifact and improves a tool used in the Phenotype workflow; impact must be measured after delivery.

- [ ] Read current upstream instructions, record HEAD, and check issue ownership/open PR overlap.
- [ ] Exercise the validation scenario; if already passing, identify an actual missing case or retire this proposal.
- [ ] Agree the bounded scope, implement it with focused regression evidence, and run repository checks above.
- [ ] Prepare one PR with before/after behavior, tests, and source attribution when upstream submission is authorized.
