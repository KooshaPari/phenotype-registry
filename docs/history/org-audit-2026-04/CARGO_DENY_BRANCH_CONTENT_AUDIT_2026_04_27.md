# Cargo-Deny Branch Content Audit - 2026-04-27

**Scope:** first 10 of 27 rollout branch tuples from
`org-audit-2026-04/CARGO_DENY_ROLLOUT_FINAL_2026_04_27.md`; cap applied to
avoid disk thrashing. Source lineage references: `e0f2fc8` and `e8275b3`;
current expanded list is at `1b9856b`.

**Method:** `git ls-remote --heads https://github.com/KooshaPari/$repo $branch`,
then shallow `git fetch --depth=2` of that branch into a temporary local repo,
followed by `git show $SHA --stat` and `git show $SHA --name-only`.

## Summary

| Metric | Value |
|---|---:|
| Branch tuples in source rollout | 27 |
| Branch tuples audited in this run | 10 |
| Branch heads resolved | 10 |
| Suspicious findings | 0 |
| Informational PR-helper title variances | 9 |

## Expected Message Families

- Full/starter rollout:
  `ci(cargo-deny): add starter deny.toml + scheduled scan workflow (zero-advisory floor)`
- Workflow rollout:
  `ci(cargo-deny): add scheduled scan + workflow_dispatch (zero-advisory floor)`
  or `ci(cargo-deny): add scheduled scan + workflow_dispatch trigger (zero-advisory floor)`

## Results

| Repo | Branch | SHA | Subject | Files changed | File names | Status |
|---|---|---|---|---:|---|---|
| `AgilePlus` | `ci/cargo-deny-full-rollout-2026-04-27` | `c637549ba77fb987db40b00150be56fc95009a3f` | `ci(cargo-deny): add starter deny.toml + scheduled scan workflow (zero-advisory floor)` | 1 | `.github/workflows/cargo-deny.yml` | OK |
| `GDK` | `ci/cargo-deny-rollout-2026-04-27` | `586c3c42af04cd697f85b397012625f232493279` | `ci(cargo-deny): add scheduled scan + workflow_dispatch trigger (zero-advisory floor)` | 1 | `.github/workflows/cargo-deny.yml` | OK |
| `HeliosLab` | `ci/cargo-deny-rollout-2026-04-27` | `aa2290464131bc801bab9003bc72375431c40f73` | `ci(cargo-deny): add scheduled scan + workflow_dispatch trigger (zero-advisory floor)` | 1 | `.github/workflows/cargo-deny.yml` | OK |
| `HexaKit` | `ci/cargo-deny-rollout-20260427` | `447d8eede630f995e26d48bb6ee54ce6fef8d81d` | `ci(cargo-deny): add scheduled scan + workflow_dispatch (zero-advisory floor)` | 1 | `.github/workflows/cargo-deny.yml` | OK |
| `KDesktopVirt` | `ci/cargo-deny-full-rollout-2026-04-27` | `40d6a1f62b420de0c61ed1be6ebe9fd44ec0564b` | `ci(cargo-deny): add starter deny.toml + scheduled scan workflow (zero-advisory floor)` | 1 | `.github/workflows/cargo-deny.yml` | OK |
| `pheno` | `ci/cargo-deny-rollout-2026-04-27` | `83d48a2c6e7f9bddd34e6a7ba1f1a899887c3cdf` | `ci(cargo-deny): add scheduled scan + workflow_dispatch trigger (zero-advisory floor)` | 1 | `.github/workflows/cargo-deny.yml` | OK |
| `phenoAI` | `ci/cargo-deny-full-rollout-2026-04-27` | `3ac84855e8be3720f73506d26bd126d41669d33a` | `ci(cargo-deny): add starter deny.toml + scheduled scan workflow (zero-advisory floor)` | 2 | `.github/workflows/cargo-deny.yml`, `deny.toml` | OK |
| `phenoData` | `ci/cargo-deny-full-rollout-2026-04-27` | `25024f0d632e445488bad785e3a4579d49fb1721` | `ci(cargo-deny): add starter deny.toml + scheduled scan workflow (zero-advisory floor)` | 2 | `.github/workflows/cargo-deny.yml`, `deny.toml` | OK |
| `PhenoKits` | `ci/cargo-deny-full-rollout-2026-04-27` | `9c0db31102f311b4431a298c92e6b30a5476aca5` | `ci(cargo-deny): add starter deny.toml + scheduled scan workflow (zero-advisory floor)` | 2 | `.github/workflows/cargo-deny.yml`, `deny.toml` | OK |
| `PhenoProc` | `ci/cargo-deny-full-rollout-2026-04-27` | `8ae1fa84041fab5f4789387b68e8a73c7c6c9494` | `ci(cargo-deny): add starter deny.toml + scheduled scan workflow (zero-advisory floor)` | 2 | `.github/workflows/cargo-deny.yml`, `deny.toml` | OK |

## Commit Details

### AgilePlus

```text
c637549 ci(cargo-deny): add starter deny.toml + scheduled scan workflow (zero-advisory floor)
 .github/workflows/cargo-deny.yml | 31 +++++++++++++++++++++++++++++++
 1 file changed, 31 insertions(+)

Files:
.github/workflows/cargo-deny.yml
```

### GDK

```text
586c3c4 ci(cargo-deny): add scheduled scan + workflow_dispatch trigger (zero-advisory floor)
 .github/workflows/cargo-deny.yml | 31 +++++++++++++++++++++++++++++++
 1 file changed, 31 insertions(+)

Files:
.github/workflows/cargo-deny.yml
```

### HeliosLab

```text
aa22904 ci(cargo-deny): add scheduled scan + workflow_dispatch trigger (zero-advisory floor)
 .github/workflows/cargo-deny.yml | 31 +++++++++++++++++++++++++++++++
 1 file changed, 31 insertions(+)

Files:
.github/workflows/cargo-deny.yml
```

### HexaKit

```text
447d8ee ci(cargo-deny): add scheduled scan + workflow_dispatch (zero-advisory floor)
 .github/workflows/cargo-deny.yml | 31 +++++++++++++++++++++++++++++++
 1 file changed, 31 insertions(+)

Files:
.github/workflows/cargo-deny.yml
```

### KDesktopVirt

```text
40d6a1f ci(cargo-deny): add starter deny.toml + scheduled scan workflow (zero-advisory floor)
 .github/workflows/cargo-deny.yml | 31 +++++++++++++++++++++++++++++++
 1 file changed, 31 insertions(+)

Files:
.github/workflows/cargo-deny.yml
```

### pheno

```text
83d48a2 ci(cargo-deny): add scheduled scan + workflow_dispatch trigger (zero-advisory floor)
 .github/workflows/cargo-deny.yml | 31 +++++++++++++++++++++++++++++++
 1 file changed, 31 insertions(+)

Files:
.github/workflows/cargo-deny.yml
```

### phenoAI

```text
3ac8485 ci(cargo-deny): add starter deny.toml + scheduled scan workflow (zero-advisory floor)
 .github/workflows/cargo-deny.yml | 31 +++++++++++++++++++++++++++++++
 deny.toml                        | 16 ++++++++++++++++
 2 files changed, 47 insertions(+)

Files:
.github/workflows/cargo-deny.yml
deny.toml
```

### phenoData

```text
25024f0 ci(cargo-deny): add starter deny.toml + scheduled scan workflow (zero-advisory floor)
 .github/workflows/cargo-deny.yml | 31 +++++++++++++++++++++++++++++++
 deny.toml                        | 16 ++++++++++++++++
 2 files changed, 47 insertions(+)

Files:
.github/workflows/cargo-deny.yml
deny.toml
```

### PhenoKits

```text
9c0db31 ci(cargo-deny): add starter deny.toml + scheduled scan workflow (zero-advisory floor)
 .github/workflows/cargo-deny.yml | 31 +++++++++++++++++++++++++++++++
 deny.toml                        | 16 ++++++++++++++++
 2 files changed, 47 insertions(+)

Files:
.github/workflows/cargo-deny.yml
deny.toml
```

### PhenoProc

```text
8ae1fa8 ci(cargo-deny): add starter deny.toml + scheduled scan workflow (zero-advisory floor)
 .github/workflows/cargo-deny.yml | 31 +++++++++++++++++++++++++++++++
 deny.toml                        | 16 ++++++++++++++++
 2 files changed, 47 insertions(+)

Files:
.github/workflows/cargo-deny.yml
deny.toml
```

## Notes

- The request capped this run at the first 10 branch tuples, so the remaining 17
  rollout branches were not fetched or inspected here.
- The nine PR-helper title variances are not suspicious branch-content findings:
  `scripts/create_cargo_deny_prs_2026_04_27.sh` maps some branches to PR titles
  that differ from already-pushed commit subjects.
