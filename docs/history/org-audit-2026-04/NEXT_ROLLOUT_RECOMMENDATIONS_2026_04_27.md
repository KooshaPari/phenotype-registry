# Next Rollout Recommendations - 2026-04-27

Scope: audit-of-audits synthesis after the cargo-deny rollout reached the
current 41/41 active Rust repo baseline in `83b85fd`.

## Ranking

| Rank | Candidate rollout | Evidence | ROI rationale | Estimated effort |
| ---: | --- | --- | --- | --- |
| 1 | PR templates + contributing + issue templates | `PR_TEMPLATE_COVERAGE_2026_04_27.md`: complete coverage is 32/113, PR template coverage 43/113, gap repos 81. | Largest visible governance gap and easiest templated rollout. Adds immediate review hygiene across every repo type without language-specific tuning. | 2-3 waves; low per-repo risk; about 1-2 days for active/local repos, longer only if reconciling stale local-only trees. |
| 2 | Explicit CodeQL Rust workflows | `CODEQL_GAP_2026_04_27.md`: 14/34 covered, 20 Rust repos missing explicit CodeQL workflow. | Highest security value per repo. Smaller scope than PR templates, but Rust workflow variance and billed-runner constraints make it slightly less turnkey. | 1 focused Rust wave; about 0.5-1 day to add workflows plus local validation and dispatch gating. |
| 3 | Pre-commit hook surface | `PRECOMMIT_COVERAGE_2026_04_27.md`: any hook surface is 48/103, with 55 repos missing. | Converts policy into local enforcement, but templates need per-language hook selection to avoid false failures. Best follow-up after PR/CodeQL surfaces are normalized. | 2-4 waves; about 1-3 days depending on repo language mix and legacy-hook compatibility. |

## Lower-Priority Candidates

- `LICENSE_COVERAGE_2026_04_27.md`: target license metadata is already 76/103
  and missing-file remediation is simple but lower operational value than review
  and security enforcement.
- `CHANGELOG_COVERAGE_2026_04_27.md`: 81/103 present and 79 current; not a
  top systemic gap.
- `AGENT_DOCS_COVERAGE_2026_04_27.md`: 71/103 have both AGENTS.md and CLAUDE.md;
  useful cleanup, but less urgent than PR workflow and security surfaces.
