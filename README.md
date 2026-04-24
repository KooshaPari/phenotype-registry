# phenotype-org-audits

Longitudinal audit-history home for the Phenotype organization. Tracks systemic issues, governance velocity, and quarterly refresh baselines across all Phenotype repos.

## Purpose

This repository serves as the canonical archive for:
- **Quarterly audits** — Organization-wide scans (LOC, dependencies, complexity, governance adoption)
- **Systemic issues** — Cross-repo duplication, build failures, policy gaps
- **Governance velocity** — Adoption rate of CLAUDE.md, AGENTS.md, AgilePlus integration, test coverage
- **Longitudinal trends** — Drift in LOC, tech stack changes, architectural decisions

## Structure

```
audits/<YYYY-MM-DD>/          # Timestamped audit snapshots
├── INDEX.md                   # Master index for the audit
├── STATUS_AT_<date>.md        # Complete repo status
├── SYSTEMIC_ISSUES.md         # Cross-org duplication, governance gaps
├── full_dep_matrix.md         # Dependency alignment snapshot
├── fr_scaffolding.md          # Functional requirement traceability
├── governance_adoption.md     # CLAUDE.md, AGENTS.md, AgilePlus coverage
└── <repo-name>.md             # Per-repo summary

tooling/
├── aggregator/                # Audit collection scripts (symlink to phenotype-tooling)
└── worklog-aggregator.sh      # Cross-repo worklog aggregation

CHANGELOG.md                   # Release history with audit entries
```

## Quarterly Audit Schedule

Audits run automatically via GitHub Actions CI on:
- **Q1**: 1st January, 9am ET
- **Q2**: 1st April, 9am ET
- **Q3**: 1st July, 9am ET
- **Q4**: 1st October, 9am ET

Cron: `0 14 1 1,4,7,10 *`

## Retention Policy

- **Current quarter**: Full detail (all artifacts preserved)
- **Past 4 quarters**: Summary only (INDEX.md + SYSTEMIC_ISSUES.md)
- **Older than 1 year**: Archived to `.archive/` (monthly pruning)

## Governance Integration

- Audits feed systemic-issue tracking in AgilePlus
- Test-traceability (FR scaffolding) informs Specification traceability system
- Dependency snapshots drive quarterly version-alignment waves
- Governance adoption metrics drive policy updates

## Related

- **Worklog aggregation**: `/Users/kooshapari/CodeProjects/Phenotype/repos/worklogs/`
- **Aggregator tooling**: `/Users/kooshapari/CodeProjects/Phenotype/repos/phenotype-tooling/`
- **Organization docs**: `/Users/kooshapari/CodeProjects/Phenotype/repos/docs/governance/`
