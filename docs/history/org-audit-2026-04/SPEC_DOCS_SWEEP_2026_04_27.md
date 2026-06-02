# Spec Docs Sweep - 2026-04-27

Scope: local-only sweep of live Rust repos under `/Users/kooshapari/CodeProjects/Phenotype/repos/<name>/`.
I used the local filesystem as the non-archived proxy and excluded hidden shelf metadata, `.archive`,
`*-wtrees`, and `*-wtr` paths.

Checks:
- `has_PRD = [ -f PRD.md ]`
- `has_ADR = [ -f ADR.md ] or any docs/adr/*.md file exists`
- `has_FR = [ -f FUNCTIONAL_REQUIREMENTS.md ]`
- `has_PLAN = [ -f PLAN.md ] || [ -f docs/PLAN.md ]`
- `has_USER_JOURNEYS = [ -f USER_JOURNEYS.md ]`

## Summary

- Repositories audited: 41
- Complete coverage: 6/41 (14.6%)
- Repositories missing all five surfaces: 7
- Gap repositories: 35

| Document surface | Present | Missing | Coverage |
| --- | ---: | ---: | ---: |
| `PRD.md` | 26 | 15 | 63.4% |
| `ADR.md or docs/adr/*.md` | 24 | 17 | 58.5% |
| `FUNCTIONAL_REQUIREMENTS.md` | 29 | 12 | 70.7% |
| `PLAN.md or docs/PLAN.md` | 28 | 13 | 68.3% |
| `USER_JOURNEYS.md` | 7 | 34 | 17.1% |

## Missing-Most-First Matrix

| Repo | PRD | ADR | FR | PLAN | UJ |
| --- | --- | --- | --- | --- | --- |
| `phenoData` | no | no | no | no | no |
| `PhenoKits` | no | no | no | no | no |
| `phenotype-journeys` | no | no | no | no | no |
| `phenotype-tooling` | no | no | no | no | no |
| `rich-cli-kit` | no | no | no | no | no |
| `Sidekick` | no | no | no | no | no |
| `thegent-dispatch` | no | no | no | no | no |
| `Eidolon` | no | no | yes | no | no |
| `eyetracker` | no | no | yes | no | no |
| `Metron` | no | no | yes | no | no |
| `phenoAI` | no | no | yes | no | no |
| `PhenoPlugins` | no | no | no | yes | no |
| `phenotype-bus` | no | no | yes | no | no |
| `phenoUtils` | no | no | yes | no | no |
| `GDK` | no | no | yes | yes | no |
| `hwLedger` | yes | yes | no | yes | no |
| `PhenoObservability` | yes | yes | no | yes | no |
| `PlayCua` | yes | yes | no | yes | no |
| `Tasken` | yes | no | yes | yes | no |
| `thegent-workspace` | yes | yes | no | yes | no |
| `bare-cua` | yes | yes | yes | yes | no |
| `BytePort` | yes | yes | yes | yes | no |
| `Configra` | yes | yes | yes | yes | no |
| `helios-cli` | yes | yes | yes | yes | no |
| `heliosCLI` | yes | no | yes | yes | yes |
| `HeliosLab` | yes | yes | yes | yes | no |
| `KDesktopVirt` | yes | yes | yes | yes | no |
| `KlipDot` | yes | yes | yes | yes | no |
| `kmobile` | yes | yes | yes | yes | no |
| `PhenoMCP` | yes | yes | yes | yes | no |
| `PhenoProc` | yes | yes | yes | yes | no |
| `PhenoRuntime` | yes | yes | yes | yes | no |
| `PhenoVCS` | yes | yes | yes | yes | no |
| `Tokn` | yes | yes | yes | yes | no |
| `Tracely` | yes | yes | yes | yes | no |
| `AgilePlus` | yes | yes | yes | yes | yes |
| `Civis` | yes | yes | yes | yes | yes |
| `FocalPoint` | yes | yes | yes | yes | yes |
| `helios-router` | yes | yes | yes | yes | yes |
| `pheno` | yes | yes | yes | yes | yes |
| `phenoShared` | yes | yes | yes | yes | yes |

## Top 5 Most Documented

- `AgilePlus`
- `Civis`
- `FocalPoint`
- `helios-router`
- `pheno`

## Top 5 Least Documented

- `phenoData`
- `PhenoKits`
- `phenotype-journeys`
- `phenotype-tooling`
- `rich-cli-kit`
