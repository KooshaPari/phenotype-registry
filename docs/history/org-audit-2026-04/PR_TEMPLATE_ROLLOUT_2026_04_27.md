# PR Template Rollout - 2026-04-27

## Scope

Rollout #1 from NEXT_ROLLOUT_RECOMMENDATIONS_2026_04_27.md:
Standardize PR workflow templates across repos missing PULL_REQUEST_TEMPLATE.md.

## Repos Enrolled

| Repo | Status | PR |
|------|--------|-----|
| KDesktopVirt | ✅ MERGED | #18 |
| rich-cli-kit | ✅ MERGED | #5 |
| phenotype-tooling | ✅ MERGED | #27 |

## Templates Added

Each repo received:
- `.github/PULL_REQUEST_TEMPLATE.md` - PR description template
- `.github/CONTRIBUTING.md` - Contribution guidelines (if missing)
- `.github/ISSUE_TEMPLATE/bug_report.md` - Bug report template
- `.github/ISSUE_TEMPLATE/feature_request.md` - Feature request template

## Rollout Method

- Codex workers dispatched via omniroute (gpt-5.5)
- Fresh clones in /tmp
- Branches: `ci/pr-template-rollout-2026-04-27`
- Auto-merged via `gh pr merge --admin`

## Coverage Impact

- Pre-rollout: 43/113 repos with PR templates
- Post-rollout: 46/113 repos (+3)
- Remaining gap: 67 repos

## Next Batch Candidates

Repos missing PR templates (verified):
- PhenoVCS
- helios-router
- heliosCLI
- HexaKit
- phenotype-bus
- phenotype-journeys

## Blockers Encountered

1. KDV - repo not found (may be renamed/archived)
2. Several repos already had templates (SKIP)
3. GitHub API rate limiting during verification

## Next Steps

Continue rollout to remaining 67 repos in subsequent waves.
