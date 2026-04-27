# phenotype-org-governance

Phenotype organization governance, audits, dashboards, and policy — a canonical reference repository for cross-project governance artifacts extracted from the monorepo canonical `/repos` directory.

## Contents

| Directory | Purpose |
|-----------|---------|
| `governance/` | Policy, decision records, and governance frameworks |
| `org-audit-2026-04/` | Org-wide audit snapshots and compliance dashboards |
| `changes/` | Significant change documentation and archived tasks |

## Structure

```
governance/
  - decision-records/      # ADRs and architectural decisions
  - policies/              # Governance policies and rules
  - frameworks/            # Governance frameworks and models
  
org-audit-2026-04/
  - dashboards/            # Cross-org metrics and KPIs
  - repos/                 # Per-repo audit snapshots
  
changes/
  - active/                # In-progress changes
  - archive/               # Completed changes
```

## Usage

This repository serves as:
1. **Reference**: Canonical governance docs for the Phenotype org
2. **History**: Audit snapshots and change records
3. **Isolation**: Breaks the canonical-subdir-inheritance trap from monorepo structure

## Integration

To reference governance from other repos, use:
```
gh repo view KooshaPari/phenotype-org-governance --json url
# https://github.com/KooshaPari/phenotype-org-governance
```

See `governance/` for detailed policies and frameworks.
