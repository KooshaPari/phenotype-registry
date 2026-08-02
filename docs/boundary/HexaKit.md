---
repo: "KooshaPari/HexaKit"
role: unknown
status: absorbed
last_boundary_review: 2026-07-30
review_cadence: 30d
in_scope:
  - "crates in pheno/crates/hexa-kit"
  - "de-duplication follow-up against existing pheno crates"
out_of_scope:
  - "AgilePlus platform-level consolidation"
target_repo: "KooshaPari/pheno"
target_path: "crates/hexa-kit"
---

# Boundary — HexaKit

## In Scope

- Rust crates and service adapters from `HexaKit/` were mirrored into
  `pheno/crates/hexa-kit/` with preservation metadata.
- Non-canonical overlap cleanup and canonical path realignment are still pending.

## Out of Scope

| Not here | Lives in | Reason |
| -------- | -------- | ------ |
| AgilePlus platform spine | `AgilePlus` | `HexaKit` mirrors are not a substitute for AgilePlus spine promotion. |

## Absorption Evidence

- Source local path: `../HexaKit`
- Target local path: `../pheno/crates/hexa-kit`
- Result artifact: `../pheno/crates/hexa-kit/ABSORPTION_META.json`
- Transfer method: `rsync -a --delete --exclude='.git' --exclude='.airlock'`

## Boundary Crossings

| Crossing | Direction | Surface | Status |
| -------- | --------- | ------- | ------ |
| HexaKit crate inventory | HexaKit → pheno/crates/hexa-kit | crate files | green |
| Duplicate-reduction follow-up | pheno/crates/hexa-kit → pheno | ownership & import dedupe | amber |

## Last Boundary Review

**Date:** 2026-07-30
**Reviewer:** forge/automation lane (`proc` continuation)
**Worklog / finding:** `phenotype-registry/audits/absorption-justifications/absorb-wave-hitl-20260729-21.md`
**Decisions:**
- Non-destructive mirror performed for the active de-duplication target (`pheno/crates/hexa-kit`).
- Source `.git` preserved for provenance.

**Next review:** after de-duplication pass in next wave
