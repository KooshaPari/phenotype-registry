# Javis603/token-monitor: five contribution proposals

**Goal:** Five bounded contributions that improve real user workflows and can be offered independently after scope checks.

**Architecture:** Follow current upstream boundaries; reproduce reported behavior before changing code. Proposals are not implementations or verified defects unless explicitly stated.

**Tech stack:** Electron / JavaScript.

Inspected September 5 UTC 2026. Evidence links and paths reflect the planning snapshot. Refresh source SHA and issue/PR ownership at execution time.

**Overlap and policy:** Review open #600 dashboard, #589 provider-toggle, #243 pricing override; do not repeat merged #606 or #566.

**Repository checks:** `npm run lint && npm test`. Run focused scenarios first and then current upstream-required checks; commands here have not been run on proposed changes. If a test-package name changes, derive the current command from upstream manifests before implementation.

## TM01: Explain historical cost revisions

- **Evidence/status:** [Source discussion](https://github.com/Javis603/token-monitor/issues/603). Feature hypothesis; coordinate issue ownership.
- **Source:** `src/shared/dailyHistoryArchive.js`, `src/shared/exporter.js`.
- **Proposed change:** Add bounded observation metadata after confirming Tokscale source availability; retain existing export cost fields.
- **Non-goals:** Unrelated cleanup, dependency upgrades, architecture rewrites, and already merged functionality.
- **Validation and acceptance:** Equal usage/attribution with changed cost records previous/latest observation; changed usage split is not called pricing change; legacy archives remain unknown. Accept only when these scenarios pass and existing supported behavior remains unchanged; attach reproduction and verification results to the eventual PR.
- **Effort:** 8-16 engineering hours after setup, an estimate excluding review delays.
- **Dependencies/engagement:** Refresh overlapping PRs; agree any feature/API scope with the issue owner. No dependency on another proposed PR unless current upstream overlap requires one.
- **Value:** A demonstrable explain historical cost revisions contribution creates a specific shipped-outcome resume artifact and improves a tool used in the Phenotype workflow; impact must be measured after delivery.

- [ ] Read current upstream instructions, record HEAD, and check issue ownership/open PR overlap.
- [ ] Exercise the validation scenario; if already passing, identify an actual missing case or retire this proposal.
- [ ] Agree the bounded scope, implement it with focused regression evidence, and run repository checks above.
- [ ] Prepare one PR with before/after behavior, tests, and source attribution when upstream submission is authorized.

## TM02: Restore Linux floating-bubble size

- **Evidence/status:** [Source discussion](https://github.com/Javis603/token-monitor/issues/565). Reported bug; reproduction pending.
- **Source:** `src/electron/floatingBubble.js`, `src/electron/main.js`.
- **Proposed change:** Fix demonstrated window-state ordering and add regression coverage.
- **Non-goals:** Unrelated cleanup, dependency upgrades, architecture rewrites, and already merged functionality.
- **Validation and acceptance:** Repeat collapse, blur and expand on X11 and Wayland; mock BrowserWindow bounds/min/max/resizable order; full dashboard stays expanded. Accept only when these scenarios pass and existing supported behavior remains unchanged; attach reproduction and verification results to the eventual PR.
- **Effort:** 4-8 engineering hours after setup, an estimate excluding review delays.
- **Dependencies/engagement:** Refresh overlapping PRs; agree any feature/API scope with the issue owner. No dependency on another proposed PR unless current upstream overlap requires one.
- **Value:** A demonstrable restore linux floating-bubble size contribution creates a specific shipped-outcome resume artifact and improves a tool used in the Phenotype workflow; impact must be measured after delivery.

- [ ] Read current upstream instructions, record HEAD, and check issue ownership/open PR overlap.
- [ ] Exercise the validation scenario; if already passing, identify an actual missing case or retire this proposal.
- [ ] Agree the bounded scope, implement it with focused regression evidence, and run repository checks above.
- [ ] Prepare one PR with before/after behavior, tests, and source attribution when upstream submission is authorized.

## TM03: Explain quota cold-start waiting

- **Evidence/status:** [Source discussion](https://github.com/Javis603/token-monitor/issues/579). Presentation improvement proposal.
- **Source:** `src/shared/deviceState.js`, `src/electron/renderer/app.js`.
- **Proposed change:** Add bounded initialization status only; leave scanning order and credential probing unchanged.
- **Non-goals:** Unrelated cleanup, dependency upgrades, architecture rewrites, and already merged functionality.
- **Validation and acceptance:** Delayed usage baseline plus completed quota fetch shows initialization then quotas; failure and genuinely empty account remain distinct. Accept only when these scenarios pass and existing supported behavior remains unchanged; attach reproduction and verification results to the eventual PR.
- **Effort:** 3-6 engineering hours after setup, an estimate excluding review delays.
- **Dependencies/engagement:** Refresh overlapping PRs; agree any feature/API scope with the issue owner. No dependency on another proposed PR unless current upstream overlap requires one.
- **Value:** A demonstrable explain quota cold-start waiting contribution creates a specific shipped-outcome resume artifact and improves a tool used in the Phenotype workflow; impact must be measured after delivery.

- [ ] Read current upstream instructions, record HEAD, and check issue ownership/open PR overlap.
- [ ] Exercise the validation scenario; if already passing, identify an actual missing case or retire this proposal.
- [ ] Agree the bounded scope, implement it with focused regression evidence, and run repository checks above.
- [ ] Prepare one PR with before/after behavior, tests, and source attribution when upstream submission is authorized.

## TM04: Reversible model visibility filter

- **Evidence/status:** [Source discussion](https://github.com/Javis603/token-monitor/issues/404). Feature request; agree display-only scope.
- **Source:** `src/shared/config.js`, `src/shared/usage.js`, `src/electron/renderer/dashboard.js`.
- **Proposed change:** Add display-only filtering and visibly label filtered totals; coordinate occupied dashboard work.
- **Non-goals:** Unrelated cleanup, dependency upgrades, architecture rewrites, and already merged functionality.
- **Validation and acceptance:** Hide one local model, restore filter and original totals; equal IDs from different providers follow explicit matching; archives untouched. Accept only when these scenarios pass and existing supported behavior remains unchanged; attach reproduction and verification results to the eventual PR.
- **Effort:** 6-12 engineering hours after setup, an estimate excluding review delays.
- **Dependencies/engagement:** Refresh overlapping PRs; agree any feature/API scope with the issue owner. No dependency on another proposed PR unless current upstream overlap requires one.
- **Value:** A demonstrable reversible model visibility filter contribution creates a specific shipped-outcome resume artifact and improves a tool used in the Phenotype workflow; impact must be measured after delivery.

- [ ] Read current upstream instructions, record HEAD, and check issue ownership/open PR overlap.
- [ ] Exercise the validation scenario; if already passing, identify an actual missing case or retire this proposal.
- [ ] Agree the bounded scope, implement it with focused regression evidence, and run repository checks above.
- [ ] Prepare one PR with before/after behavior, tests, and source attribution when upstream submission is authorized.

## TM05: Explain exact local-day boundary

- **Evidence/status:** [Source discussion](https://github.com/Javis603/token-monitor/issues/376). Smaller documentation slice of rollover request.
- **Source:** `src/shared/usage.js`, `src/shared/dailyHistoryArchive.js`, `docs/configuration.md`.
- **Proposed change:** Expose current semantics through help/documentation; exclude configurable rollover and archive migration.
- **Non-goals:** Unrelated cleanup, dependency upgrades, architecture rewrites, and already merged functionality.
- **Validation and acceptance:** Local midnight and DST fixtures match displayed date labels; document calendar day versus rolling 24 hours. Accept only when these scenarios pass and existing supported behavior remains unchanged; attach reproduction and verification results to the eventual PR.
- **Effort:** 3-6 engineering hours after setup, an estimate excluding review delays.
- **Dependencies/engagement:** Refresh overlapping PRs; agree any feature/API scope with the issue owner. No dependency on another proposed PR unless current upstream overlap requires one.
- **Value:** A demonstrable explain exact local-day boundary contribution creates a specific shipped-outcome resume artifact and improves a tool used in the Phenotype workflow; impact must be measured after delivery.

- [ ] Read current upstream instructions, record HEAD, and check issue ownership/open PR overlap.
- [ ] Exercise the validation scenario; if already passing, identify an actual missing case or retire this proposal.
- [ ] Agree the bounded scope, implement it with focused regression evidence, and run repository checks above.
- [ ] Prepare one PR with before/after behavior, tests, and source attribution when upstream submission is authorized.


