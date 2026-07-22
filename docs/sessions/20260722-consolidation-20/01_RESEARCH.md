# Research

## Evidence Summary

- All 20 named repositories exist and are unarchived.
- `PriceyApp`, `router-docs`, and `template-commons` are forks and must remain untouched.
- Historical scripts assume `main`, but eight source repositories have non-`main` default branches.
- Batch A contains placement errors; its conclusions cannot authorize mutation without correction.
- Disk pressure is critical: 98% used with about 22 GiB free. Evidence collection must use partial bare
  clones rather than full working clones.
- The ecosystem validator baseline is known to fail with 18 reachable repositories, 2 unreachable
  repositories, 17 drift findings, and 47 total items.
- The docs build baseline is blocked at
  `docs/specs/pheno-specs/specs/platform/build-system/PRD.md:65:60` by a Vue missing-end-tag error.

## Decision Rationale

Existence and unarchived state do not prove safe absorption or archival. Default-branch drift, Batch A
misplacements, and incomplete SHA/content parity require a preservation-first, verify-before-mutate
workflow.
