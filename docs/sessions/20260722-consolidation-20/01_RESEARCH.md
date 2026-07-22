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
- `AgilePlus-recovery-20260714` has a sole head, `recovery/isolated-20260714`, at exact commit
  `0aafdf9692c11abb6e426f36857aeec7bb6cd942`; canonical AgilePlus contains that exact commit and
  tree `eb82ced16353219d85aa83c925819ae48cb36c16` with the exact head. It is the sole READY source.
- `AgilePlus-recovery-evidence-20260714` remains HOLD as unique preservation evidence.

## Decision Rationale

Existence and unarchived state do not prove safe absorption or archival. Default-branch drift, Batch A
misplacements, and incomplete SHA/content parity require a preservation-first, verify-before-mutate
workflow. The one proven exception is `AgilePlus-recovery-20260714`: after an immediate preflight,
rename it to `zz-archive-AgilePlus-recovery-20260714` and archive it; never delete it.
