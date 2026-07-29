# pheno-agents-md absorption packet (reconciliation)

| Property | Value |
| --- | --- |
| Source | `KooshaPari/pheno-agents-md` |
| Remote state | `isArchived: true` (2026-07-29T07:50:57Z) |
| Default branch | `main` |
| Branches | `main`, `chore/T8-prep`, `feat/ci-workflows-2026-06-21`, `audit/ownership-20260722-pheno-agents-md` |
| Decision | `ARCHIVE_ONLY` (failsafe: no safe merge path completed in this cycle) |
| Target | `phenotype-registry` (tombstone lineage only) |

## Evidence

- `gh repo view KooshaPari/pheno-agents-md`
- `gh api repos/KooshaPari/pheno-agents-md/git/trees/main?recursive=1`
- `gh api repos/KooshaPari/pheno-agents-md/commits?per_page=5`

The source tree includes AGENTS parser/runtime files plus CI metadata, but no local
clone/target workspace was present in this turn to perform a verified merge. The
repo is already archived and thus read-only.

## Decision rationale

- `projects/pheno-agents-md.json` and `registry/disposition-index.json` were
  updated to canonical `ARCHIVE_ONLY` with `target=phenotype-registry`.
- No deletion, force-push, or branch rewrite is performed.
- Preservation command (for emergency reactivation):
  `gh repo restore KooshaPari/pheno-agents-md`.
