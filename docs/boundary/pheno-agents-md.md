---
repo: "pheno-agents-md"
role: tooling
status: archived
last_boundary_review: 2026-07-29
review_cadence: dormant
in_scope:
  - "AGENTS.md parser and validator utility surfaced on the AGENTS governance stack"
  - "Remote read-only lineage preservation in registry"
out_of_scope:
  - "Any new merge attempt into phenotype-tooling (no target runbook completion in this cycle)"
depends_on: []
depended_on_by: []
---

# Boundary — pheno-agents-md

## Decision (2026-07-29)

`pheno-agents-md` is recorded as `ARCHIVE_ONLY` evidence-only. The source is
already archived on GitHub and no local source checkout exists in this workspace for
safe code extraction in this cycle. Registry records were corrected to reflect this
state and preserve the repo for provenance-only retention.

## Evidence summary

- `gh repo view KooshaPari/pheno-agents-md` reports `isArchived=true` and
  `archivedAt=2026-07-29T07:50:57Z`.
- Local workspace does not contain `repos/pheno-agents-md`.
- `registry/disposition-index.json` row `AUTO-IMPORT-pheno-agents-md` now points
  to `ARCHIVE_ONLY` and `target=phenotype-registry` with this audit artifact.

## Restoration / recovery

- Restore command: `gh repo restore KooshaPari/pheno-agents-md`
- Branches are visible via GitHub API for manual reconstruction if required.
