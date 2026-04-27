# ORG_DASHBOARD v66 - 2026-04-27 Corrected Rust Repo Count

## Cargo-deny coverage CORRECTED 2026-04-27: 61 Rust repos (was 36), 100% file presence, 16% workflow_dispatch

Source: fresh live audit via `gh repo list KooshaPari --limit 1000 --json name,isArchived,languages` with Rust language filter, followed by `Cargo.toml` content checks and `.github/workflows/cargo-deny.yml` workflow content checks.

Correction: prior dashboards/memos that used 36 active Rust repos are stale and wrong. The corrected active Rust repo denominator is 61. All 61 have `.github/workflows/cargo-deny.yml` present; only 10 include `workflow_dispatch`, leaving 51 repos without on-demand cargo-deny verification.

## Summary

| Metric | Count | Share |
| --- | ---: | ---: |
| Active Rust repos | 61 | 100% |
| cargo-deny.yml present | 61 | 100% |
| HAS workflow_dispatch | 10 | 16% |
| NO workflow_dispatch | 51 | 84% |

## Per-Repo Cargo-Deny Dispatch Table

| Repo | cargo-deny.yml | workflow_dispatch | State |
| --- | --- | --- | --- |
| `Agentora` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `AgilePlus` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `Apisync` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `AuthKit` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `Benchora` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `BytePort` | HAS | HAS | HAS_FILE_AND_DISPATCH |
| `Civis` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `Configra` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `DataKit` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `Dino` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `Eidolon` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `eyetracker` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `FocalPoint` | HAS | HAS | HAS_FILE_AND_DISPATCH |
| `GDK` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `helios-cli` | HAS | HAS | HAS_FILE_AND_DISPATCH |
| `helios-router` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `heliosCLI` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `HeliosLab` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `HexaKit` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `hwLedger` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `KDesktopVirt` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `MCPForge` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `McpKit` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `Metron` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `ObservabilityKit` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `Paginary` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `pheno` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `PhenoAgent` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `phenoAI` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `PhenoCompose` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `phenoData` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `PhenoKits` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `PhenoLang` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `PhenoMCP` | HAS | HAS | HAS_FILE_AND_DISPATCH |
| `PhenoObservability` | HAS | HAS | HAS_FILE_AND_DISPATCH |
| `PhenoPlugins` | HAS | HAS | HAS_FILE_AND_DISPATCH |
| `PhenoProc` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `PhenoRuntime` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `phenoShared` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `phenotype-bus` | HAS | HAS | HAS_FILE_AND_DISPATCH |
| `phenotype-infra` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `phenotype-journeys` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `phenotype-org-audits` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `phenotype-tooling` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `phenoUtils` | HAS | HAS | HAS_FILE_AND_DISPATCH |
| `PhenoVCS` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `PlayCua` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `PolicyStack` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `ResilienceKit` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `rich-cli-kit` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `Sidekick` | HAS | HAS | HAS_FILE_AND_DISPATCH |
| `Stashly` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `Tasken` | HAS | HAS | HAS_FILE_AND_DISPATCH |
| `TestingKit` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `thegent` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `thegent-dispatch` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `thegent-workspace` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `Tokn` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `Tracely` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `Tracera` | HAS | NO | HAS_FILE_NO_DISPATCH |
| `vibeproxy` | HAS | NO | HAS_FILE_NO_DISPATCH |

## Action Items

- Open PRs to add `workflow_dispatch` to the 51 repos marked `HAS_FILE_NO_DISPATCH`.
- Cap rollout per session; do not attempt all 51 in one uncontrolled wave.
- Use the 61-repo denominator for all future Rust cargo-deny dashboard percentages.
- Treat earlier `36 active Rust repos` references as superseded by this correction.
