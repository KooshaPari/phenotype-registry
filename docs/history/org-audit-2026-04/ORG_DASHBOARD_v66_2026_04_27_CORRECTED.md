# ORG_DASHBOARD v66 - 2026-04-27 SUPERSEDED Correction

## Honest framing

This dashboard originally attempted to correct the v62-v65 cargo-deny denominator, but it
introduced another false state: `61/61 = 100% cargo-deny file presence` and `16%
workflow_dispatch` coverage. That was audit decay, not truth.

Use `CARGO_DENY_TRUE_COVERAGE_2026_04_27.md` from commit `4a2a608` as the corrected
local truth surface.

## Superseded claims in this file

Do not re-cite these as current state:

- `61` active Rust repos as the cargo-deny denominator.
- `61/61 = 100%` cargo-deny workflow file presence.
- `10/61 = 16%` workflow_dispatch coverage.
- `51` repos lacking workflow_dispatch as the next cargo-deny queue.

## True state at session end

| Metric | True value | Source |
| --- | ---: | --- |
| Local Rust repos | 42 | parent-direct local probe |
| Repos with `cargo-deny.yml` on `main` | 18/42 (43%) | `4a2a608` |
| Repos with `workflow_dispatch` in `cargo-deny.yml` | 5/42 (12%) | `4a2a608` |
| Rollout branches pushed for missing coverage | 17 | `e0f2fc8` |
| Projected coverage after queued PRs merge | 35/42 (83%) | `e0f2fc8` |

## What remains useful from v66

The durable lesson is not the old table. The durable lesson is that GitHub Contents API
checks and decoded empty content can produce false positives when file absence is not
handled strictly. Future cargo-deny dashboards must verify local canonical clones or
explicit 404/file-exists semantics before publishing coverage percentages.

## User decisions queue

| Priority | Item | State |
| --- | --- | --- |
| P0 | Create 17 queued cargo-deny rollout PRs after GitHub API rate limit reset. | Pending |
| P1 | Seven stub/archived/bare repos legitimately do not need cargo-deny; examples include KlipDot and kmobile archived, bare-cua bare, AgilePlus bare. | Pending |
| P2 | PolicyStack legacy-tooling-gate finding. | Pending |
| P2 | Evaluate helios-cli direct `rand 0.9` usage before refactor. | Pending |
