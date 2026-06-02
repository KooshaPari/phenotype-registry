# Rust Coverage Tooling Audit - 2026-04-27

Scope: non-archived GitHub repositories under `KooshaPari` whose primary language is `Rust`.

Audit checks:
- `.codecov.yml` presence at repository root.
- Coverage workflow presence in `.github/workflows/*.yml` or `.yaml`, including similar filenames or workflow content references to coverage tooling.
- `grcov` / `tarpaulin` references in `Cargo.toml` or `deny.toml` files.

## Summary

- Repositories audited: 41
- NONE: 14
- PARTIAL: 27
- COMPLETE: 0
- `.codecov.yml`: 0
- Coverage workflow: 27
- grcov/tarpaulin in Cargo.toml or deny.toml: 0
- Tool references: none

## Results

| Status | Repo | `.codecov.yml` | Coverage workflow | grcov/tarpaulin | Evidence |
|---|---|---:|---:|---:|---|
| NONE | [Agentora](https://github.com/KooshaPari/Agentora) | no | no | no | - |
| NONE | [Benchora](https://github.com/KooshaPari/Benchora) | no | no | no | - |
| NONE | [Configra](https://github.com/KooshaPari/Configra) | no | no | no | - |
| NONE | [FocalPoint](https://github.com/KooshaPari/FocalPoint) | no | no | no | - |
| NONE | [helios-cli](https://github.com/KooshaPari/helios-cli) | no | no | no | - |
| NONE | [heliosCLI](https://github.com/KooshaPari/heliosCLI) | no | no | no | - |
| NONE | [HexaKit](https://github.com/KooshaPari/HexaKit) | no | no | no | - |
| NONE | [hwLedger](https://github.com/KooshaPari/hwLedger) | no | no | no | - |
| NONE | [pheno](https://github.com/KooshaPari/pheno) | no | no | no | - |
| NONE | [PhenoLang](https://github.com/KooshaPari/PhenoLang) | no | no | no | - |
| NONE | [PhenoMCP](https://github.com/KooshaPari/PhenoMCP) | no | no | no | - |
| NONE | [phenotype-journeys](https://github.com/KooshaPari/phenotype-journeys) | no | no | no | - |
| NONE | [phenotype-org-audits](https://github.com/KooshaPari/phenotype-org-audits) | no | no | no | - |
| NONE | [PhenoVCS](https://github.com/KooshaPari/PhenoVCS) | no | no | no | - |
| PARTIAL | [AgilePlus](https://github.com/KooshaPari/AgilePlus) | no | yes | no | workflow: .github/workflows/fr-coverage.yml |
| PARTIAL | [Apisync](https://github.com/KooshaPari/Apisync) | no | yes | no | workflow: .github/workflows/coverage.yml |
| PARTIAL | [AuthKit](https://github.com/KooshaPari/AuthKit) | no | yes | no | workflow: .github/workflows/fr-coverage.yml |
| PARTIAL | [Eidolon](https://github.com/KooshaPari/Eidolon) | no | yes | no | workflow: .github/workflows/fr-coverage.yml |
| PARTIAL | [GDK](https://github.com/KooshaPari/GDK) | no | yes | no | workflow: .github/workflows/coverage.yml<br>.github/workflows/fr-coverage.yml |
| PARTIAL | [KDesktopVirt](https://github.com/KooshaPari/KDesktopVirt) | no | yes | no | workflow: .github/workflows/fr-coverage.yml |
| PARTIAL | [Metron](https://github.com/KooshaPari/Metron) | no | yes | no | workflow: .github/workflows/fr-coverage.yml |
| PARTIAL | [ObservabilityKit](https://github.com/KooshaPari/ObservabilityKit) | no | yes | no | workflow: .github/workflows/fr-coverage.yml |
| PARTIAL | [Paginary](https://github.com/KooshaPari/Paginary) | no | yes | no | workflow: .github/workflows/fr-coverage.yml |
| PARTIAL | [PhenoAgent](https://github.com/KooshaPari/PhenoAgent) | no | yes | no | workflow: .github/workflows/fr-coverage.yml |
| PARTIAL | [phenoAI](https://github.com/KooshaPari/phenoAI) | no | yes | no | workflow: .github/workflows/fr-coverage.yml |
| PARTIAL | [phenoData](https://github.com/KooshaPari/phenoData) | no | yes | no | workflow: .github/workflows/fr-coverage.yml |
| PARTIAL | [PhenoObservability](https://github.com/KooshaPari/PhenoObservability) | no | yes | no | workflow: .github/workflows/coverage.yml<br>.github/workflows/fr-coverage.yml |
| PARTIAL | [PhenoRuntime](https://github.com/KooshaPari/PhenoRuntime) | no | yes | no | workflow: .github/workflows/fr-coverage.yml |
| PARTIAL | [phenoShared](https://github.com/KooshaPari/phenoShared) | no | yes | no | workflow: .github/workflows/reusable/coverage.yml |
| PARTIAL | [phenotype-bus](https://github.com/KooshaPari/phenotype-bus) | no | yes | no | workflow: .github/workflows/fr-coverage.yml |
| PARTIAL | [phenotype-infra](https://github.com/KooshaPari/phenotype-infra) | no | yes | no | workflow: .github/workflows/fr-coverage.yml |
| PARTIAL | [phenotype-tooling](https://github.com/KooshaPari/phenotype-tooling) | no | yes | no | workflow: .github/workflows/fr-coverage.yml |
| PARTIAL | [phenoUtils](https://github.com/KooshaPari/phenoUtils) | no | yes | no | workflow: .github/workflows/fr-coverage.yml |
| PARTIAL | [PlayCua](https://github.com/KooshaPari/PlayCua) | no | yes | no | workflow: .github/workflows/fr-coverage.yml |
| PARTIAL | [rich-cli-kit](https://github.com/KooshaPari/rich-cli-kit) | no | yes | no | workflow: .github/workflows/fr-coverage.yml |
| PARTIAL | [Sidekick](https://github.com/KooshaPari/Sidekick) | no | yes | no | workflow: .github/workflows/fr-coverage.yml |
| PARTIAL | [Stashly](https://github.com/KooshaPari/Stashly) | no | yes | no | workflow: .github/workflows/coverage.yml |
| PARTIAL | [Tasken](https://github.com/KooshaPari/Tasken) | no | yes | no | workflow: .github/workflows/coverage.yml |
| PARTIAL | [thegent-dispatch](https://github.com/KooshaPari/thegent-dispatch) | no | yes | no | workflow: .github/workflows/fr-coverage.yml |
| PARTIAL | [thegent-workspace](https://github.com/KooshaPari/thegent-workspace) | no | yes | no | workflow: .github/workflows/fr-coverage.yml |
| PARTIAL | [Tokn](https://github.com/KooshaPari/Tokn) | no | yes | no | workflow: .github/workflows/coverage.yml<br>.github/workflows/fr-coverage.yml |

Generated from GitHub default-branch tree queries and GitHub code search on 2026-04-27.
