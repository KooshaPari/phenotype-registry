# CLAUDE.md — Phenotype-Org Governance

## Project Type

Documentation / organizational policy repository. No code, no build step.

## Remote

- **Repository:** `KooshaPari/phenotype-org-governance`
- **Clone URL:** `https://github.com/KooshaPari/phenotype-org-governance.git`

## Stack

- **Format:** Markdown (with frontmatter for policies)
- **Tools:** pre-commit hooks (linting/validation)
- **No build step** — editing Markdown directly

## Key Directories

| Directory | Purpose |
|-----------|---------|
| `governance/` | Live policies, domain standards, rollouts, templates |
| `org-audit-2026-04/` | April 2026 audit snapshots (reference only, do not edit) |
| `changes/` | Per-change proposals and design documents |
| `docs/` | General documentation |
| `scripts/` | Automation scripts (shell/python) |
| `.github/` | GitHub Actions workflows |

## Development Workflow

1. **Edit Markdown files directly** — no compilation needed
2. **Run pre-commit:** `pre-commit run --all-files`
3. **Commit style:** `docs(<area>): <verb> <noun>` (e.g., `docs(governance): add Codeberg mirror plan`)

## Document Standards

### Naming Convention
- Format: `<domain>-<action>-YYYY-MM-DD.md`
- Short form: `*-YYYY_MM_DD.md`

### Frontmatter (for policies)
```yaml
---
title: Policy Title
status: AUTHORITATIVE | SUPERSEDED | DRAFT
domain: <functional-area>
effective_date: YYYY-MM-DD
supersedes: <path-to-old-doc>
replaced_by: <path-to-new-doc>
---
```

### Status Indicators
- `STATUS: AUTHORITATIVE` — current source of truth
- `STATUS: SUPERSEDED` + `replaces:` pointer — archived, historical context only
- Dated filenames — superseded unless explicitly linked from current canonical

## Authority Rules

When conflicting guidance appears, the document with the **latest `effective_date:`** in `governance/` wins.

## Adding New Documents

1. Copy the appropriate template from `governance/templates/`
2. Fill frontmatter (title, status, domain, effective_date, see_also, supersedes, replaced_by)
3. Place in `governance/domains/<domain>/` or `governance/rollouts/`
4. Update `SUPERSEDED.md` if replacing an existing document
5. Commit with proper message format

## GitHub Actions Billing Constraint

This repo's CI workflows may fail due to GitHub Actions billing/spending limits on the KooshaPari account. Do not block PRs on CI status. Verify quality locally.
