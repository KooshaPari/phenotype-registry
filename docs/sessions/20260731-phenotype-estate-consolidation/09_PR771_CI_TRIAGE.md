# Tracera PR #771 CI Triage

## Candidate

- PR: https://github.com/KooshaPari/Tracera/pull/771
- Head: `3abfa031b92d653bb1050a0a7d18875c94684861`
- Candidate diff: the focused router test and one JSON fixture only.

## Current hosted results

| Check | Result | Evidence | Classification |
|---|---|---|---|
| Security audit | pass | GitHub Actions run 30616471651 | pass |
| Secret scan | pass | GitHub Actions run 30616471705 | pass |
| CodeQL/Sonar/Semgrep | pass | PR rollup | pass |
| Runtime smoke | fail | `@tracertm/web` build exits 1; no candidate-file error emitted | baseline/unattributed |
| Preflight | fail | formatting diffs in `crates/tracera-cli/*` | pre-existing baseline |
| Lint & Format | fail | `trunk-io/trunk-action@d90b916...` cannot resolve | workflow infrastructure |
| Vercel | fail | deployment failure; no candidate-file diagnostic | deployment/baseline |

## Decision

The focused Rust fixture remains locally green (`1 passed, 0 failed, 52 filtered out`). Hosted failures are not evidence that the fixture is incorrect, but they block merge because branch protection requires the full check set. Keep PR #771 draft and repair or explicitly quarantine baseline failures through the repository's normal governance path.
