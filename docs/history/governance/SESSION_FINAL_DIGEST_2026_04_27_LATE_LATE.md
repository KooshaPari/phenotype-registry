# Session Final Digest - 2026-04-27 Late Late

## Honest framing

This session contained both major wins AND significant audit-decay errors that produced
false dashboards. This digest reflects ACTUAL state.

The important correction is that v62-v65 overstated cargo-deny enrollment as `36/36`,
and v66 attempted to correct the denominator but introduced a new false claim:
`61/61 = 100% cargo-deny file presence`. The final truth surface is the parent-direct
local probe in `org-audit-2026-04/CARGO_DENY_TRUE_COVERAGE_2026_04_27.md`
from commit `4a2a608`.

## Verified wins

- 17 cargo-deny rollout branches pushed across org; PR creation deferred to
  post-rate-limit.
- Tokn + HeliosLab Pages green; FocalPoint was already green.
- `helios-cli` `RUSTSEC-2025-0056` suppressed in `deny.toml`.
- 25+ governance audit docs committed. Some are accurate; some were later superseded
  by correction docs.
- 7 memory entries codified.
- Truth-correcting docs landed: `CARGO_DENY_TRUE_COVERAGE_2026_04_27.md`
  in commit `4a2a608`.

## SUPERSEDED claims (do not re-cite)

- `36/36 cargo-deny enrolled` from v62-v65.
- `61/61 = 100% cargo-deny file presence` from v66.
- `16% workflow_dispatch coverage`; actual local coverage is 12% (5/42).
- Any dashboard table that classifies every listed Rust repo as having
  `.github/workflows/cargo-deny.yml` without a strict file-exists check.

## TRUE state at session end

| Metric | Actual state |
| --- | ---: |
| Local Rust repos | 42 |
| Repos with `cargo-deny.yml` in `main` | 18/42 (43%) |
| Repos with `workflow_dispatch` in `cargo-deny.yml` | 5/42 (12%) |
| Rollout PRs queued post-rate-limit-reset | 17 |
| Expected file coverage after those PRs merge | 35/42 (83%) |
| Canonical repos restored to `main` after Codex left them on rollout branches | 5 |

## Cargo-deny rollout state

Commit `e0f2fc8` records the final branch-push state. The branch queue covers
17 repos from the missing-workflow gap:

| Repo | Branch |
| --- | --- |
| `bare-cua` | `ci/cargo-deny-full-rollout-2026-04-27` |
| `GDK` | `ci/add-starter-deny-toml-20260427` and `ci/cargo-deny-rollout-2026-04-27` |
| `helios-router` | `ci/add-starter-deny-toml-20260427` |
| `HeliosLab` | `ci/cargo-deny-rollout-2026-04-27` |
| `HexaKit` | `ci/cargo-deny-rollout-20260427` |
| `pheno` | `ci/cargo-deny-rollout-2026-04-27` |
| `phenoAI` | `ci/cargo-deny-full-rollout-2026-04-27` |
| `phenoData` | `ci/cargo-deny-full-rollout-2026-04-27` |
| `PhenoKits` | `ci/cargo-deny-full-rollout-2026-04-27` |
| `PhenoProc` | `ci/cargo-deny-full-rollout-2026-04-27` |
| `PhenoRuntime` | `ci/cargo-deny-full-rollout-2026-04-27` |
| `phenoShared` | `ci/cargo-deny-rollout-2026-04-27` |
| `phenotype-journeys` | `ci/cargo-deny-full-rollout-2026-04-27` |
| `phenotype-tooling` | `ci/cargo-deny-full-rollout-2026-04-27` |
| `PhenoVCS` | `ci/cargo-deny-full-rollout-2026-04-27` |
| `PlayCua` | `ci/cargo-deny-full-rollout-2026-04-27` |
| `rich-cli-kit` | `ci/cargo-deny-full-rollout-2026-04-27` |

The projected landing state is 35/42 local Rust repos with cargo-deny workflow
files, or 83% file coverage. That projection depends on the queued PRs being
created and merged.

## Pages and security state

| Surface | Actual state |
| --- | --- |
| FocalPoint Pages | Already green before this late-late correction window. |
| HeliosLab Pages | Green after the stub Pages/docs deploy fix. |
| Tokn Pages | Green after VitePress source exclusions for generated/problematic docs. |
| PolicyStack Pages | Still pending verification in prior notes; do not mark green from this digest. |
| `helios-cli` cargo-deny | `RUSTSEC-2025-0056` suppressed in `deny.toml`; direct `rand 0.9` usage still needs evaluation. |

## Governance docs state

More than 25 governance/audit documents landed during the session across dashboards,
coverage audits, CI health, alert inventory, branch protection, release inventory,
license/README/CHANGELOG coverage, and cargo-deny rollout state. These docs are not
all equally durable:

- Durable: correction docs that cite strict local probes and explicit commits.
- Useful but superseded: v62-v66 cargo-deny dashboard progression.
- Dangerous to re-cite: dashboards whose headline numbers were derived from broad
  API scans without strict file-exists verification.

## Why the false dashboards happened

The failure mode was a compound audit bug:

1. Broad GitHub API inventory was treated as a stronger truth source than local
   canonical clone checks.
2. Missing workflow files were not distinguished strictly enough from empty or
   decode-failed content.
3. The denominator shifted from 36 to 61 without validating the numerator.
4. Later dashboards inherited earlier claims instead of re-running the probe.

The corrected operating rule is simple: never publish cargo-deny file-presence or
dispatch percentages without an explicit file-exists probe and reproducible command
surface.

## User decisions queue

| Priority | Item | Required action |
| --- | --- | --- |
| P0 | 17 cargo-deny rollout PRs need creation. | Use the GitHub API queue automatically when rate limit resets. |
| P1 | 7 stub/archived repos legitimately do not need cargo-deny. | Confirm classification as non-rollout targets; documented examples are KlipDot and kmobile archived, bare-cua bare, and AgilePlus bare. |
| P2 | PolicyStack legacy-tooling-gate finding. | Decide whether to fix, suppress with rationale, or defer to a tracked work item. |
| P2 | `helios-cli` direct `rand 0.9` usage. | Evaluate 15+ call sites before deciding whether a refactor is needed. |

## Final handoff

Start the next pass from the correction docs, not the dashboard headlines:

1. `org-audit-2026-04/CARGO_DENY_TRUE_COVERAGE_2026_04_27.md` (`4a2a608`)
2. `org-audit-2026-04/CARGO_DENY_ROLLOUT_BRANCHES_2026_04_27.md` (`49b6d54`)
3. `org-audit-2026-04/CARGO_DENY_ROLLOUT_FINAL_2026_04_27.md` (`e0f2fc8`)
4. `org-audit-2026-04/ORG_DASHBOARD_v66_2026_04_27_CORRECTED.md` as superseded
   framing only

The next concrete operation is PR creation for the 17 pushed rollout branches after
rate-limit reset. Do not reopen the 36/36 or 61/61 claims.
