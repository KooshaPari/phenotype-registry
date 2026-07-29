# Dated snapshot duplicate reconciliation — 2026-07-29

## Scope
Date-stamped duplicate `projects/*-2026-*.json` rows that were shadow copies of already tracked active repos.

## Evidence summary
- `gh api repos/KooshaPari/AuthKit-2026-06-25` → 404 (no such repo)
- `gh api repos/KooshaPari/Civis-2026-06-25` → 404
- `gh api repos/KooshaPari/Eidolon-2026-06-25` → 404
- `gh api repos/KooshaPari/KodeVibe-2026-06-25` → 404
- `gh api repos/KooshaPari/PhenoSpecs-2026-06-25` → 404
- `gh api repos/KooshaPari/pheno-runtime-config-2026-06-29` → 404
- `KooshaPari/AuthKit`, `KooshaPari/Civis`, `KooshaPari/Eidolon`, `KooshaPari/KodeVibe`, `KooshaPari/PhenoSpecs`, `KooshaPari/pheno-runtime-config` still resolve as active/real remotes.

## Decision
For each date-suffixed row, set:
- `status = archived`
- `disposition = NEVER_EXISTED`
- `archived = true`
- `archived_reason` describing "recovery snapshot duplicate"

Canonical records remain untouched (`projects/AuthKit.json`, `projects/Civis.json`, etc.).
