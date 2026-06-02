# User Decisions Backlog v3 - 2026-04-27

Source v2: `governance/USER_DECISIONS_BACKLOG_2026_04_27_v2.md` from commit
`d1df00b`.

This is the post-victory, billing-blocked backlog. Scope is local governance
documentation only. Honest framing: several session wins landed, but GitHub
Actions billing now blocks live CI verification. Treat cargo-deny rollout state
as structurally enrolled until billing is resolved and workflows can actually
run.

## Summary

- **Resolved this session:** 5
- **P0:** 2
- **P1:** 8
- **P2:** 3

## Resolved This Session

### 1. Cargo-deny rollout reached 95% structural enrollment

- **Previous v2 state:** 24 repos missing coverage / broad rollout still open.
- **Current state:** 40/42 active Rust repos are structurally enrolled.
- **Honest caveat:** Live workflow verification is blocked by GitHub Actions
  billing, not by cargo-deny job failures.
- **Artifacts:** `org-audit-2026-04/CARGO_DENY_BILLING_BLOCK_NOTE_2026_04_27.md`,
  `governance/SESSION_2026_04_27_FINAL.md`.

### 2. Pages corrected to 7-LIVE

- **Previous v2 state:** Only 3 Pages surfaces expected/live in some notes.
- **Current state:** Tokn, thegent, PolicyStack, HexaKit, HeliosLab, FocalPoint,
  and AgilePlus returned HTTP 200 in the parent-direct probe.
- **Honest caveat:** Custom Cloudflare domains still have separate 530 SSL or
  provisioning work.
- **Artifact:** `governance/SESSION_FINAL_v2_2026_04_27.md`.

### 3. `helios-cli` `RUSTSEC-2025-0056` cleared

- **Previous v2 state:** Advisory still needed follow-up.
- **Current state:** `RUSTSEC-2025-0056` is suppressed in `deny.toml` at
  `afee0e47b`; cargo-deny advisory pressure is cleared for that finding.
- **Carry-over caveat:** Direct `rand 0.9` usage remains a P1 dependency hygiene
  choice, listed below.
- **Artifact:** `org-audit-2026-04/ORG_DASHBOARD_v65_2026_04_27_LATE3.md`.

### 4. Tokn Pages green

- **Previous v2 state:** Tokn Pages was not green and had source-scan failures.
- **Current state:** Tokn Pages is green after VitePress source exclusions for
  generated/problematic docs.
- **Artifact:** `org-audit-2026-04/ORG_DASHBOARD_v65_2026_04_27_LATE3.md`.

### 5. HeliosLab Pages green via PR #64

- **Previous v2 state:** HeliosLab PR #64 needed content/green-state review.
- **Current state:** PR #64 merged stub Pages work and docs deploy completed
  green at `1dc861b`.
- **Honest caveat:** The public content may still be scaffold-level; that is no
  longer a deploy blocker.
- **Artifact:** `org-audit-2026-04/ORG_DASHBOARD_v65_2026_04_27_LATE3.md`.

## P0 - Blocking next session

### 1. Resolve GitHub Actions billing for the KooshaPari org

- **Status:** BLOCKED - Account billing prevents Actions jobs from starting.
- **What's blocked:** All CI runs, including cargo-deny verification for the
  newly enrolled 40/42 Rust repos.
- **Evidence:** Triggered cargo-deny `workflow_dispatch` runs failed at the
  billing wall: jobs did not start because recent account payments failed or
  the spending limit needs to be increased.
- **User decision/action:** Resolve org billing, or explicitly accept that CI
  verification remains unavailable and future governance claims must be limited
  to file/PR/enrollment state.
- **Artifact:** `org-audit-2026-04/CARGO_DENY_BILLING_BLOCK_NOTE_2026_04_27.md`;
  memory reference `feedback_billing_blocked_rules.md`.

### 2. Optional permanent cargo-deny exclusions for bare/archived targets

- **Status:** NEEDS USER POLICY CHOICE - Optional but affects next-session scope.
- **What's blocked:** Whether future agents keep retrying cargo-deny enrollment
  for `bare-cua` plus archived/stub targets such as KlipDot and kmobile.
- **User decision/action:** Mark the documented exclusions permanent, or keep
  them in the active rollout queue for manual handling.
- **Artifact:** Late-session cargo-deny decision notes and final digest.

## P1 - Nice-to-have for next session

### 1. `helios-cli` direct `rand 0.9` usage

- **Status:** NEEDS DECISION - Advisory pressure cleared, but direct usage
  remains across 15+ call sites.
- **User decision/action:** Refactor call sites toward `thread_rng()` style
  usage, or accept current direct `rand 0.9` dependency state.

### 2. PolicyStack legacy-tooling-gate finding triage

- **Status:** NEEDS POLICY DECISION.
- **User decision/action:** Fix the finding, add a documented exception plus
  tracking ticket, or defer with an explicit owner.

### 3. `.mcp.json` embedded API keys in GDK + KlipDot

- **Status:** SECURITY FOLLOW-UP - Embedded keys need rotation or removal.
- **User decision/action:** Rotate any exposed keys, replace committed values
  with environment-variable placeholders, and repair schema drift.
- **Artifact:** `session_2026_04_27` user-decision notes.

### 4. `argis` recovery option choice

- **Status:** NEEDS USER CHOICE - Non-destructive options are documented.
- **User decision/action:** Choose graft, cherry-pick, or separate-branch
  recovery.
- **Artifact:** `governance/argis_recovery_options_2026_04_27.md`.

### 5. `/repos` pack-gc

- **Status:** LOCAL MAINTENANCE FOLLOW-UP.
- **User decision/action:** Run the documented pack/gc recovery sequence when
  local disk and repo state allow it.
- **Artifact:** `governance/pack_corruption_diagnosis_2026_04_26.md`; memory
  reference `feedback_repos_push_blockers.md`.

### 6. Cloudflare 530 SSL provisioning for 5 custom domains

- **Status:** EXTERNAL INFRA FOLLOW-UP.
- **What's blocked:** Custom domain availability for the affected Pages CNAMEs.
- **User decision/action:** Provision SSL/custom-domain state in Cloudflare or
  GitHub Pages for the five affected domains.

### 7. OmniRoute v3.7.0 darwin-arm64 build

- **Status:** WORKAROUND IN PLACE - v3.4.1 remains the safe pin.
- **User decision/action:** Stay pinned, file upstream, or retry after a fixed
  release.

### 8. PhenoProc submodule pointer move

- **Status:** NEEDS USER INTENT CONFIRMATION.
- **What's blocked:** Cleanly interpreting the `crates/phenotype-shared`
  submodule pointer move.
- **User decision/action:** Commit the pointer move, revert it intentionally, or
  document why it should remain local-only.

## P2 - Long-term governance cleanup

### 1. Branch dedup cleanup

- **Status:** HOUSEKEEPING.
- **What's needed:** Deduplicate mixed `20260427` and `2026-04-27` branch-date
  formats from the rollout wave.

### 2. v62-v66 dashboard archival

- **Status:** ARCHIVAL.
- **What's needed:** Mark v62-v66 dashboard files as historical reference only;
  do not cite their superseded cargo-deny coverage claims.

### 3. Test maturity to L3 across 25+ repos

- **Status:** LONG-TERM QUALITY GOAL.
- **What's needed:** Raise test maturity consistently across the repo fleet;
  current maturity varies by repo.

