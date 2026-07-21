# Org Health Digest 2026-04-27

Source set: April 27 audit documents in `org-audit-2026-04/`. This is an audit-of-audits synthesis only; no new live repository scan was performed for this digest.

## Cargo-deny coverage

- Enrollment: 36/36 active Rust repos have `cargo-deny.yml` coverage, 100%.
- Dashboard state: latest v65 reports known-failing cargo-deny repos at 0.
- Green where live-verified: no. `CARGO_DENY_LIVE_VERIFICATION_2026_04_27.md` triggered zero workflows because 0/36 enrolled repos expose `workflow_dispatch`.
- Dispatch readiness: 0/36 have the on-demand trigger, so manual verification coverage is 0.0%.
- CI caveat: `CI_HEALTH_SUMMARY_2026_04_27_LATE.md` still observed one cargo-deny workflow failure in BytePort.

## Pages state

Five-site pages baseline:

| Site | State | Evidence |
|---|---|---|
| FocalPoint | LIVE | v65 Pages table |
| HeliosLab | LIVE | green at `1dc861b` after PR #64 |
| Tokn | LIVE | green at `53a97f4` after VitePress `srcExclude` fix |
| PolicyStack | NOT LIVE / not verified | workflow_dispatch `24983965583` queued; outDir fix awaiting verification |
| KDV | NOT LIVE | billing-blocked |

## Open Dependabot alerts

Open alert total in the late inventory is 58 across repos with numeric counts; `n/a` 404 endpoints are excluded.

Top 5 repos by open alert count:

| Rank | Repo | Open alerts | Severity mix |
|---:|---|---:|---|
| 1 | HexaKit | 19 | high: 2, medium: 17 |
| 2 | BytePort | 7 | low: 2, medium: 5 |
| 3 | hwLedger | 7 | high: 3, low: 2, medium: 2 |
| 4 | PhenoRuntime | 6 | high: 1, low: 4, medium: 1 |
| 5 | agentapi-plusplus | 5 | medium: 5 |

## Stale PRs

- Stale PR count: 0.
- Top 3 oldest stale PRs: none.
- Open PR backlog caveat: late backlog snapshot found 2 open PRs, both checks-failing: AgilePlus #435 and Civis #259.

## Test maturity Level 3+

- Level 3 proxy maturity: 5/32 repos, 15.6%.
- Inputs: tests directory, Codecov config, and `quality-gate.yml`.
- Level 3 repos: AgilePlus, HexaKit, PhenoProc, PolicyStack, Tokn.

## Pre-commit coverage

- `.pre-commit-config.yaml`: 47/103 repos, 45.6%.
- Any hook surface (`pre-commit`, lefthook, or husky): 48/103 repos, 46.6%.
- Gap count for any hook surface: 55 repos.

## License coverage

- Target license metadata (`MIT` or `Apache-2.0`): 76/103 repos, 73.8%.
- SPDX breakdown: MIT 61, Apache-2.0 15, NOASSERTION 8, NONE 16, other non-target 3.
- Missing LICENSE/LICENSE.md list size: 27 repos.

## Branch protection coverage

- Covered by active ruleset or classic `main` protection: 80/103 repos, 77.7%.
- Active ruleset coverage: 78/103 repos.
- Classic `main` protection: 4/103 repos.
- Protection gap: 23 repos.

## CodeQL Rust coverage

- Explicit CodeQL workflow coverage: 14/34 Rust repos, 41.2%.
- Gap count: 20/34.
- Several missing workflow-directory cases are structural repo hygiene gaps, not just CodeQL omissions.

## Actions pinning to SHA

- Not measured by the landed April 27 audit documents.
- Digest status: unknown / not auditable from this source set.
- Priority: add a dedicated action-pinning audit before treating this as a percentage-bearing metric.

## Submodule sanity orphan flags

- Archived remote default-branch orphan commits: 0 across six archived repos checked.
- Local post-archive orphan flags remain in archived checkouts: AtomsBot 11, chatta 18, KlipDot 1, kmobile 13.
- Evalora submodule blocker: `KooshaPari/Evalora.git` is deleted and returns 404; PhenoProc still lists it in `.gitmodules`, so fresh PhenoProc git-dep consumers can fail recursive submodule init.
- Phantom gitlink cleanup improved but is not fully closed in dashboards: 12,397 to about 5,000, a 58% reduction.

## Top 3 user-decisions backlog priorities

| Priority | Decision | Why it matters |
|---|---|---|
| P0 | Decide whether to add `workflow_dispatch` to all 36 cargo-deny workflows. | Without this, green-state verification cannot be safely triggered on demand. |
| P0 | Resolve Pages blockers: KDV billing and PolicyStack queued verification. | Pages is 3/5 live, 2/5 not live or not verified. |
| P1 | Choose the next broad hygiene rollout: branch protection gaps, hook gaps, license gaps, or CodeQL Rust gaps. | The biggest measured gaps are hooks at 46.6%, CodeQL Rust at 41.2%, license target at 73.8%, and branch protection at 77.7%. |

## Action items for next /loop fire

1. Patch the 36 cargo-deny workflows with `workflow_dispatch`, then rerun a live green verification wave.
2. Recheck PolicyStack Pages run `24983965583`; fix or mark live based on the final deploy result.
3. Escalate or unblock KDV Pages billing, then run the deploy verification.
4. Start the CodeQL Rust gap wave for the 20/34 repos without explicit workflows.
5. Open a dedicated Actions SHA-pinning audit and produce a real percentage baseline.

## SUPERSEDED

Cargo-deny completion/enrollment claims in this document are superseded by
[`CARGO_DENY_TRUE_COVERAGE_2026_04_27.md`](CARGO_DENY_TRUE_COVERAGE_2026_04_27.md)
and truth-correction commit `4a2a608`.
