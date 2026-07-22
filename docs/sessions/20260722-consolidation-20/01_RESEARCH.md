# Research

## Evidence Summary

- All 20 named repositories existed and were unarchived at intake.
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
  tree `eb82ced16353219d85aa83c925819ae48cb36c16` with the exact head. It was the sole source to
  reach READY and is now `ARCHIVED-PRESERVED / complete`.
- `AgilePlus-recovery-evidence-20260714` remains HOLD as unique preservation evidence.
- The authorized transaction completed for docket #1. The source is now
  `KooshaPari/zz-archive-AgilePlus-recovery-20260714`, with `archived=true`, `private=true`,
  `fork=false`, default branch `recovery/isolated-20260714`, one branch, zero tags, and unchanged
  `pushed_at=2026-07-16T00:20:23Z`.
- Postverification confirmed exact commit `0aafdf9692c11abb6e426f36857aeec7bb6cd942` and tree
  `eb82ced16353219d85aa83c925819ae48cb36c16`; canonical AgilePlus retains the exact recovery ref,
  commit, and tree. The old name redirects to the renamed archived repository. No deletion occurred.

## Decision Rationale

Existence and unarchived state do not prove safe absorption or archival. Default-branch drift, Batch A
misplacements, and incomplete SHA/content parity require a preservation-first, verify-before-mutate
workflow. The one proven exception, `AgilePlus-recovery-20260714`, passed immediate preflight and
was renamed to `zz-archive-AgilePlus-recovery-20260714` and archived. It is preserved, not deleted;
the other 19 docket entries remain HOLD or VERIFY-ONLY.
