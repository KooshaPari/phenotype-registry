# Cargo-Deny Dual Probe Validation - 2026-04-27 Late

## Summary

| Metric | Value |
|---|---:|
| Total probed repos | 41 |
| Probe agreement count | 41 |
| Probe disagreement count | 0 |
| Repos with `cargo-deny.yml` in both probes | 37 |
| Repos without `cargo-deny.yml` in both probes | 4 |
| Raw coverage on probed set | 37/41 (90.2%) |
| Active-only coverage after excluding archived repos | 37/39 (94.9%) |

## Methodology

- Probe set: the 41 root Cargo.toml repos under `/Users/kooshapari/CodeProjects/Phenotype/repos`.
- Probe A: `gh api repos/KooshaPari/<repo>/contents/.github/workflows --jq "any(.name==\"cargo-deny.yml\")"`
- Probe B: `git clone --depth 1 https://github.com/KooshaPari/<repo>.git` followed by `ls .github/workflows/cargo-deny.yml`
- Normalization: probe A errors were treated as `false` only when the workflow directory/file was absent; probe B used the fresh clone result directly.

## Disagreement List

None. Every repo produced the same answer from both probes.

## Coverage Verdict

The fresh-clone truth matches the GitHub contents API for all 41 repos in the probe set.

Current cargo-deny coverage on the audited set is **37/41 (90.2%)**.

Two repos in the probe set are archived in GitHub metadata:

- `KlipDot`
- `kmobile`

If you exclude those archived repos, the active-only coverage becomes **37/39 (94.9%)**.

## Repos Without `cargo-deny.yml`

| Repo | GitHub contents API | Fresh clone | Status |
|---|---|---|---|
| FocalPoint | `false` | `false` | missing |
| KlipDot | `false` | `false` | archived, missing |
| hwLedger | `false` | `false` | missing |
| kmobile | `false` | `false` | archived, missing |

