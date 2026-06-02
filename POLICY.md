# Phenotype Org Policy (Enforcement Surface)

This repo is the **ENFORCEMENT** member of the spec/governance spine. It is the home of the **shared/reusable policy workflows** and the **`deny.toml` / license baseline** that sibling repos consume. It is forward-looking; past audits live under [`docs/history/`](docs/history/).

## The 4-role spine

| Repo | Role |
|------|------|
| [phenotype-registry](https://github.com/KooshaPari/phenotype-registry) | **INDEX** — canonical ecosystem map ([ECOSYSTEM_MAP.md](https://github.com/KooshaPari/phenotype-registry/blob/main/ECOSYSTEM_MAP.md)) |
| [PhenoSpecs](https://github.com/KooshaPari/PhenoSpecs) | **ADRs / API contracts / specs** |
| [PhenoHandbook](https://github.com/KooshaPari/PhenoHandbook) | **CONVENTIONS / patterns** |
| **phenotype-org-governance** (this repo) | **ENFORCEMENT** — reusable policy workflows + deny baseline |

## Enforced policies

| Policy | Surface | How siblings consume it |
|--------|---------|--------------------------|
| Supply-chain (cargo-deny: advisories/bans/licenses/sources) | [`.github/workflows/reusable-cargo-deny.yml`](.github/workflows/reusable-cargo-deny.yml) + [`deny.toml`](deny.toml) | `uses: KooshaPari/phenotype-org-governance/.github/workflows/reusable-cargo-deny.yml@main` |
| OpenSSF Scorecard | [`.github/workflows/scorecard.yml`](.github/workflows/scorecard.yml) | runs here; pattern copied per repo |
| Secret scanning | [`.github/workflows/trufflehog.yml`](.github/workflows/trufflehog.yml) | runs here; pattern copied per repo |
| Org-wide local sweep (billing-free) | [`scripts/cargo-deny-org-weekly.sh`](scripts/cargo-deny-org-weekly.sh) | run locally across all repos |

### Consuming the cargo-deny baseline

```yaml
# .github/workflows/policy.yml in a sibling Rust repo
jobs:
  cargo-deny:
    uses: KooshaPari/phenotype-org-governance/.github/workflows/reusable-cargo-deny.yml@main
```

The license allowlist (`deny.toml`) is permissive-only (MIT/Apache-2.0/BSD/ISC/Unicode/Zlib/CC0). Adding a license is a deliberate, reviewed change here — not per repo.

## CI hygiene baseline

All workflows: pin `ubuntu-24.04`, SHA-pin third-party actions, least-privilege `permissions`, `concurrency` cancel-in-progress, and avoid billable minutes. See PhenoHandbook `patterns/ci/never-billable-ci.md`.

## History

Past audit waves, session logs, and dashboards are archived under [`docs/history/`](docs/history/) — kept for reference, not active policy.
