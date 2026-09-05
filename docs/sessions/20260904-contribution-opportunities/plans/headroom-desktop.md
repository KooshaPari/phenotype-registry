# Headroom Desktop: five conditional proposals

Repository: https://github.com/gglucass/headroom-desktop. Inspected September 5 UTC: HEAD tree, README/AGENTS/CLAUDE guidance, package.json, storage.rs, appUpdate.ts, [open issues](https://github.com/gglucass/headroom-desktop/issues?q=is%3Aopen) and [recent closed PRs](https://github.com/gglucass/headroom-desktop/pulls?q=is%3Apr+is%3Aclosed+sort%3Aupdated-desc). Existing paths below were verified. Only #31 and #14 were open non-PR issues. Accordingly these are conditional proposals, not five established bugs. First inspect current tests and reproduce a missing behavior; retire already-covered proposals rather than manufacturing a change.

Actual commands: `npm run test:frontend`, `npx tsc --noEmit`, `cargo test --manifest-path src-tauri/Cargo.toml --lib`, and cross-module `cargo check --manifest-path src-tauri/Cargo.toml`. CSS changes additionally require `npm run check:colors` and light/dark inspection. [CLAUDE.md](https://github.com/gglucass/headroom-desktop/blob/main/CLAUDE.md) requires atomic persistent writes, schema defaults, parse-failure backups, bounded logs and process identity checks. Compression changes have a full-day staging/fleet gate; these five avoid compression-engine changes. Estimates exclude review time.

Overlap: merged #50 already adds Windows; #77 handles App Control DLL detection; #78 exposes inactive output reduction; #84 vendors prefix-floor behavior; #85 supplies provider picker; #76 addresses stats timeout/bootstrap issues. Do not repeat them. Open #80 handles documentation links. Full targeted issue/PR search and owner alignment are still required before implementation.

## HEADROOM-01: Explain unsupported Claude Desktop traffic during setup

- Evidence: VERIFIED user report [#31](https://github.com/gglucass/headroom-desktop/issues/31) expects savings from Claude App usage; root cause/current support status unverified.
- Scope: `src/components/LauncherShell.tsx`, its existing test, `src/lib/launcherHelpers.ts`, and `src-tauri/src/client_adapters.rs` only if existing capability data is insufficient. Present accurate detected-client/routing status. No interception of unsupported app traffic or promise of desktop support.
- Acceptance: supported CLI connected, supported CLI idle and unsupported client states have distinct actionable explanations; idle is not falsely diagnosed as unsupported. Run frontend suite/types and Rust tests if adapter changes.
- Overlap: distinguish #78 optimization-status messaging from client routing. First, 1-2 days; owner confirms supported client contract. Value: prevents misleading savings expectations and improves agent-tool onboarding.

## HEADROOM-02: Make interrupted updater recovery deterministic

- Evidence: HYPOTHESIS grounded in inspected `src/lib/appUpdate.ts`, which registers progress and updater state; no updater failure was reproduced.
- Scope: `src/lib/appUpdate.ts`, `src/lib/appUpdate.test.ts`; inspect existing retry/listener cleanup coverage before selecting a missing case. Only adjust frontend state transitions proven incorrect. No release signing, automatic downgrade or installer redesign.
- Acceptance: failed download permits a clean retry; stale progress from a previous attempt cannot overwrite current state; listener teardown occurs once; unavailable updates do not leave a restart-ready false positive. Run `npm run test:frontend` and `npx tsc --noEmit`.
- Overlap: recent release PRs #87/#88 are not evidence of an updater defect; check full updater search. Second, independent, 1-2 days. Maintainer confirms missing-case value. Value: desktop lifecycle reliability and precise asynchronous testing experience.

## HEADROOM-03: Add an explicitly redacted local support bundle

- Evidence: HYPOTHESIS; `docs/support-triage.md` exists and must first be checked for equivalent export support. No private-data leak is alleged.
- Scope: existing `src-tauri/src/logging.rs`, `src-tauri/src/storage.rs`, and support UI after locating actual export entrypoint. Proposed new helper/test paths require agreement. Bundle bounded diagnostic metadata with a visible preview and explicit local save.
- Acceptance: synthetic keys, auth headers, prompts and personal paths are excluded/redacted; size limits apply; export never transmits data; cancellation leaves persistent settings untouched. Test redactor adversarial fixtures and run Rust tests/check; frontend gates if UI changes.
- Overlap: #77 already removes raw learn titles; this must add a distinct support workflow. Third, 2-3 days, owner scope approval required. Value: practical enterprise troubleshooting and privacy-aware desktop engineering.

## HEADROOM-04: Make persisted-state recovery visible to the user

- Evidence: HYPOTHESIS. Inspected `storage.rs` already snapshots state around upgrades; CLAUDE mandates backup on parse failure. Do not propose adding backups as if absent.
- Scope: `src-tauri/src/storage.rs`, `src-tauri/src/state.rs`, and `src/lib/setupHealthAlert.ts` with its existing test, only if corruption recovery currently lacks an actionable user outcome. Preserve actual backed-up data; no automatic reset or history deletion.
- Acceptance: malformed legacy fixture is retained, valid salvage remains available, UI accurately reports recovery/backups without repeated alerts, successful later load clears the condition. Run Rust tests/check and frontend suite/types as touched.
- Overlap: inspect existing storage recovery tests and #76 before activation. Fourth, 2-3 days; agree disclosure and restore semantics. Value: durable session-history handling and responsible migration work.

## HEADROOM-05: Add timezone-boundary accounting contract fixtures

- Evidence: HYPOTHESIS. Inspected `storage.rs` already centralizes user_day_key and distinguishes UTC backend rollups. This proposal validates uncovered DST/travel boundaries, not a claimed missing timezone function.
- Scope: `src-tauri/src/usage_counters.rs`, `src-tauri/src/storage.rs`, `src/lib/dashboardHelpers.test.ts`; select a missing cross-source fixture after examining existing tests. No savings formula changes or client historical-rate canary (explicitly prohibited).
- Acceptance: synthetic DST transitions, local midnight and timezone changes neither double-count nor lose usage; UTC aggregate labels remain UTC; local day totals follow documented semantics. Run Rust tests and frontend suite/types.
- Overlap: distinguish timezone aggregation from #84 compression and existing local-day fixes. Fifth, independent, 1-2 days; owner must approve test gap and semantics. Value: trustworthy cost dashboards and financial-telemetry edge-case experience.
