# Phenotype Org Policy (Enforcement Surface)

This repo is the **ENFORCEMENT** member of the spec/governance spine. It owns **POLICY** — the canonical [`deny.toml`](deny.toml) / license baseline. The reusable workflow **MECHANISM** lives in [phenotype-tooling](https://github.com/KooshaPari/phenotype-tooling) and *consumes* this policy. Split: **governance owns WHAT (policy), tooling owns HOW (the workflow).** Forward-looking; past audits live under [`docs/history/`](docs/history/).

## The 4-role spine

| Repo | Role |
|------|------|
| [phenotype-registry](https://github.com/KooshaPari/phenotype-registry) | **INDEX** — canonical ecosystem map ([ECOSYSTEM_MAP.md](https://github.com/KooshaPari/phenotype-registry/blob/main/ECOSYSTEM_MAP.md)) |
| [PhenoSpecs](https://github.com/KooshaPari/PhenoSpecs) | **ADRs / API contracts / specs** |
| [PhenoHandbook](https://github.com/KooshaPari/PhenoHandbook) | **CONVENTIONS / patterns** |
| **phenotype-org-governance** (this repo) | **ENFORCEMENT** — `deny.toml`/license + advisory policy baseline (workflow mechanism lives in phenotype-tooling) |

## Enforced policies

| Policy | Owner (this repo) | Mechanism (where siblings call) |
|--------|-------------------|----------------------------------|
| Supply-chain (cargo-deny: advisories/bans/licenses/sources) | [`deny.toml`](deny.toml) — canonical license/advisory baseline | `uses: KooshaPari/phenotype-tooling/.github/workflows/reusable/cargo-deny.yml@main` (fetches this `deny.toml` by default) |
| Secret scanning | (config/policy) | `uses: KooshaPari/phenotype-tooling/.github/workflows/reusable/trufflehog.yml@main` — governance's own [`trufflehog.yml`](.github/workflows/trufflehog.yml) consumes it |
| OpenSSF Scorecard | [`.github/workflows/scorecard.yml`](.github/workflows/scorecard.yml) | runs here; pattern copied per repo |
| Org-wide local sweep (billing-free) | [`scripts/cargo-deny-org-weekly.sh`](scripts/cargo-deny-org-weekly.sh) | run locally across all repos |

### Consuming the cargo-deny baseline

The reusable workflow lives in **phenotype-tooling** and pulls this repo's `deny.toml` as the default policy (a caller that ships its own `deny.toml` overrides it):

```yaml
# .github/workflows/policy.yml in a sibling Rust repo
jobs:
  cargo-deny:
    uses: KooshaPari/phenotype-tooling/.github/workflows/reusable/cargo-deny.yml@main
    # use-org-policy defaults true → fetches phenotype-org-governance /deny.toml @ main
```

This repo's [`deny.toml`](deny.toml) is the **single policy source** (kept at repo root so the raw-URL fetch is stable). The license allowlist is permissive-only (MIT/Apache-2.0/BSD/ISC/Unicode/Zlib/CC0); adding a license is a deliberate, reviewed change **here** — not per repo. There is intentionally **no** reusable-cargo-deny workflow in this repo: the mechanism is owned by phenotype-tooling to avoid competing copies.

## CI hygiene baseline

All workflows: pin `ubuntu-24.04`, SHA-pin third-party actions, least-privilege `permissions`, `concurrency` cancel-in-progress, and avoid billable minutes. See PhenoHandbook `patterns/ci/never-billable-ci.md`.

## History

Past audit waves, session logs, and dashboards are archived under [`docs/history/`](docs/history/) — kept for reference, not active policy.
