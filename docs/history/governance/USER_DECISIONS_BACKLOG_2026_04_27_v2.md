# User Decisions Backlog v2 - 2026-04-27

Source v1: `governance/USER_DECISIONS_BACKLOG_2026_04_27.md` from commit `f4ebde9`.

This is the end-of-session merged backlog of items still blocked on user input,
manual approval, external access, or a user-owned policy choice. Scope is
AUDIT + DOC only.

## Summary

- **Total items:** 14
- **P0:** 4
- **P1:** 8
- **P2:** 2

## P0 - Blocks active automation, secrets, or user-visible availability

### 1. GDK + KlipDot `.mcp.json` repair

- **Status:** BLOCKED - Edit/write permission denied to subagent; secret rotation also required.
- **What's blocked:** Forge sessions in GDK and KlipDot error on "Context7 unknown field". Both `.mcp.json` files are invalid for Claude Code's schema because they contain Cline/Roo fields such as `autoApprove`, `disabled`, `timeout`, and `transportType`.
- **User decision/action:** Approve the prepared write fix or apply it manually. Before any commit/push, rotate the embedded GDK `coda` `API_KEY` and replace it with `${CODA_API_KEY}`.
- **Artifact:** Subagent-prepared diff held in session context, not yet written.

### 2. PhenoProc dirty tree

- **Status:** BLOCKED - Unknown-provenance local changes need intent confirmation.
- **What's blocked:** PhenoProc cargo-deny enrollment and any clean governance automation in that checkout.
- **Evidence:** `crates/phenotype-shared` submodule pointer moved locally from `8369060` to `03c92be`; around 70 untracked root files are present (`ADR.md`, `AGENTS.md`, `Duple/`, `Finalis/`, etc.).
- **User decision/action:** Decide whether to commit the submodule bump or discard it, and decide whether the untracked root files should be committed, archived, or removed.
- **Artifact:** `git status` in `/Users/kooshapari/CodeProjects/Phenotype/repos/PhenoProc/`.

### 3. `/repos` canonical pack-gc

- **Status:** BLOCKED - Bash sandbox permission was denied in prior run.
- **What's blocked:** Pack corruption recovery on the canonical `/repos` worktree.
- **User decision/action:** Run the documented gc sequence manually or grant one-time bash permission for the documented commands.
- **Artifact:** `phenotype-org-governance/governance/pack_corruption_diagnosis_2026_04_26.md`.

### 4. Custom-domain Cloudflare 530s

- **Status:** BLOCKED - Cloudflare-side provisioning required.
- **What's blocked:** Custom domains return HTTP 530 for Pages CNAMEs under `*.kooshapari.com`: `focalpoint`, `kdv`, `helioslab`, `policystack`, and `tokn`. GitHub Pages URLs work where deploys succeeded.
- **User decision/action:** Provision custom-domain SSL at the Pages level or DNS layer for the affected `*.kooshapari.com` Pages CNAMEs.

## P1 - Policy, security, or repo-health decisions needed soon

### 5. argis-extensions recovery option choice

- **Status:** BLOCKED - Three non-destructive options documented; user must pick.
- **What's blocked:** Local branch has 24 Bifrost API commits, while `origin/main` has 11 mixed Dependabot/governance commits. The histories are unrelated with no merge base; direct merge produces 34 conflicts.
- **User decision/action:** Choose one path: `(A)` `git replace --graft`, `(B)` cherry-pick local commits onto upstream, or `(C)` keep both as separate branches.
- **Artifact:** `phenotype-org-governance/governance/argis_recovery_options_2026_04_27.md`.

### 6. PhenoObservability + PhenoProc cargo-deny enrollment

- **Status:** PARTIAL - PhenoObservability enrolled upstream; PhenoProc is gated on item 2.
- **What's blocked:** PhenoProc cargo-deny enrollment.
- **User decision/action:** Resolve the PhenoProc dirty tree in item 2; enrollment can then proceed autonomously.

### 7. Tokn pre-push hook cargo-on-main bug

- **Status:** BLOCKED - User-gated local behavior choice.
- **What's blocked:** `hooks/pre-push.sh` runs cargo on `main` despite the stated intent. The bug is at the line 38 `elif` branch.
- **User decision/action:** Approve a direct fix to the hook logic, or leave it user-triggered/manual only.
- **Artifact:** Tokn `hooks/pre-push.sh`.

### 8. HeliosLab PR #64 stub-page content quality review

- **Status:** NEEDS USER REVIEW - PR merged, but content quality was not validated beyond mergeability.
- **What's blocked:** Confidence that the merged pages are acceptable public/project content rather than minimal generated stubs.
- **User decision/action:** Decide whether to accept the stub pages as temporary scaffolding or request a content-quality pass.
- **Artifact:** HeliosLab PR `#64`.

### 9. PolicyStack run `24983965583` post-dispatch verification

- **Status:** NEEDS VERIFICATION - Post-dispatch run needs confirmation.
- **What's blocked:** Closing the loop on the PolicyStack dispatch outcome.
- **User decision/action:** Approve follow-up verification or manually inspect the run result.
- **Artifact:** PolicyStack Actions run `24983965583`.

### 10. Org-wide cargo-deny `workflow_dispatch` gap

- **Status:** PARTIAL - Worker opened up to 5 PRs; remaining roughly 30 repos are user-gated.
- **What's blocked:** Full org-wide manual dispatch coverage for cargo-deny workflows across the 35-repo gap.
- **User decision/action:** Approve the next PR wave, cap the number of repos per wave, or defer the remaining repos.
- **Artifact:** `governance/cargo-deny-coverage-2026-04-27.md` and related late cargo-deny audit notes.

### 11. helios-cli `rand` RUSTSEC-2026-0097 follow-up

- **Status:** BLOCKED - Security advisory transitively addressed, but direct usage remains.
- **What's blocked:** Final dependency hygiene direction for codex-rs usage sites. `rand` 0.9 remains directly used in 15+ call sites.
- **User decision/action:** Choose whether to refactor call sites to `thread_rng()` style usage or continue with `rand` 0.9 as the accepted direct dependency.
- **Artifact:** helios-cli / codex-rs call sites using `rand`.

### 12. PolicyStack legacy-tooling-gate finding

- **Status:** BLOCKED - Needs exception policy or remediation.
- **What's blocked:** Closing the legacy-tooling-gate finding cleanly.
- **User decision/action:** Add an anti-pattern-exception comment plus tracking ticket, or approve a fix that removes the finding.
- **Artifact:** PolicyStack legacy-tooling-gate output.

## P2 - Follow-up governance or dependency choices

### 13. OmniRoute v3.7.0 broken on darwin-arm64

- **Status:** WORKAROUND IN PLACE - Rolled back to v3.4.1.
- **What's blocked:** Upgrading OmniRoute beyond the working v3.4.1 pin.
- **Evidence:** v3.7.0 ships with missing `wreq-js` native module for darwin-arm64.
- **User decision/action:** Stay on v3.4.1, or file an upstream issue and wait for v3.7.1+.

### 14. Civis direct-push ruleset bypass

- **Status:** FOLLOW-UP - PR path succeeded, but direct-push automation may still be blocked.
- **What's blocked:** Future direct pushes may still require a ruleset bypass fix.
- **Evidence:** Civis PR `#258` was merged via PR path due to ruleset behavior; memory points to `feedback_ruleset_bypass_actor_type.md` for the likely `bypass_actor` `RepositoryRole=5` fix.
- **User decision/action:** Decide whether to patch the ruleset bypass actor so approved automation can direct-push when intended, or keep the PR-only path.
