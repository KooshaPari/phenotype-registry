# Cargo-deny Branch Dedup Audit - 2026-04-27

## Scope

Audit requested for `phenoShared`, `pheno`, `HexaKit`, and the rollout-final repo
set from `governance/SESSION_FINAL_DIGEST_2026_04_27_LATE_LATE.md`.

Command pattern used per repo:

```bash
git ls-remote https://github.com/KooshaPari/<repo> 2>&1 | grep "ci/cargo-deny" | head -3
```

The full `--heads` ref set was also inspected for `ci/cargo-deny` branches so
refs beyond the first three could not be hidden by ordering.

## Result

No audited repo has both `20260427` and `2026-04-27` date-format variants for the
same `ci/cargo-deny` rollout branch content. No branch deletion is recommended
from this audit.

## Remote Ref Evidence

| Repo | `ci/cargo-deny` refs observed | Dedup recommendation |
| --- | --- | --- |
| `phenoShared` | `74e634a4b626c2611ffa0bbdd5b968b574ba8706` `ci/cargo-deny-rollout-2026-04-27` | None |
| `pheno` | `83d48a2c6e7f9bddd34e6a7ba1f1a899887c3cdf` `ci/cargo-deny-rollout-2026-04-27` | None |
| `HexaKit` | `447d8eede630f995e26d48bb6ee54ce6fef8d81d` `ci/cargo-deny-rollout-20260427` | None |
| `bare-cua` | `d2370482d60226fb59899edc437bb6df55610c86` `ci/cargo-deny-full-rollout-2026-04-27` | None |
| `GDK` | `586c3c42af04cd697f85b397012625f232493279` `ci/cargo-deny-rollout-2026-04-27` | None |
| `helios-router` | No `ci/cargo-deny` ref observed; rollout-final lists only `ci/add-starter-deny-toml-20260427` | None |
| `HeliosLab` | `aa2290464131bc801bab9003bc72375431c40f73` `ci/cargo-deny-rollout-2026-04-27` | None |
| `phenoAI` | `3ac84855e8be3720f73506d26bd126d41669d33a` `ci/cargo-deny-full-rollout-2026-04-27` | None |
| `phenoData` | `25024f0d632e445488bad785e3a4579d49fb1721` `ci/cargo-deny-full-rollout-2026-04-27` | None |
| `PhenoKits` | `9c0db31102f311b4431a298c92e6b30a5476aca5` `ci/cargo-deny-full-rollout-2026-04-27` | None |
| `PhenoProc` | `8ae1fa84041fab5f4789387b68e8a73c7c6c9494` `ci/cargo-deny-full-rollout-2026-04-27` | None |
| `PhenoRuntime` | `80daae924a0d144e8b650800a1b6a0a1ea76341c` `ci/cargo-deny-full-rollout-2026-04-27` | None |
| `phenotype-journeys` | `e26300703f2d468cbb630597bdde7683b9832d51` `ci/cargo-deny-full-rollout-2026-04-27` | None |
| `phenotype-tooling` | `47c9eecc2961b5fe8be290a23db759e10394cb2e` `ci/cargo-deny-full-rollout-2026-04-27`; `9092e280ec0e55e0f5223556ba15ce91c589cdd9` `ci/cargo-deny-rollout-2026-04-27` | None; two distinct branch names and different tip SHAs, not a date-format duplicate pair |
| `PhenoVCS` | `b8fc68f6d454c2d3ad4c36ce37b443b48afb404e` `ci/cargo-deny-full-rollout-2026-04-27` | None |
| `PlayCua` | `d2370482d60226fb59899edc437bb6df55610c86` `ci/cargo-deny-full-rollout-2026-04-27` | None |
| `rich-cli-kit` | `71c7a92df7140e9dd22419d941e497f39e5dc592` `ci/cargo-deny-full-rollout-2026-04-27` | None |

## Deletion Plan

No deletion plan is proposed. The audit found zero same-content duplicate
`ci/cargo-deny` branch pairs split only by compact versus ISO date formatting.
