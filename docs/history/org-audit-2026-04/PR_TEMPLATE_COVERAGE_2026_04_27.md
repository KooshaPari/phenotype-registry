# PR Template Coverage Audit - 2026-04-27

Scope: local-only audit of visible Git working trees under `/Users/kooshapari/CodeProjects/Phenotype/repos/<name>/`. Local presence is used as the non-archived repository proxy.

Checks:
- `has_PULL_REQUEST_TEMPLATE`: `.github/PULL_REQUEST_TEMPLATE.md` or `.github/pull_request_template.md` exists
- `has_CONTRIBUTING`: `CONTRIBUTING.md` or `.github/CONTRIBUTING.md` exists
- `has_ISSUE_TEMPLATE`: `ls .github/ISSUE_TEMPLATE/ 2>/dev/null | wc -l`

## Summary

- Repositories audited: 113
- Complete coverage: 32/113 (28.3%)
- Pull request template coverage: 43/113 (38.1%)
- Contributing guide coverage: 57/113 (50.4%)
- Issue template coverage: 38/113 (33.6%)
- Gap repositories: 81

## Missing-Most-First Matrix

| Repo | Missing Count | has_PULL_REQUEST_TEMPLATE | has_CONTRIBUTING | has_ISSUE_TEMPLATE | Missing |
| --- | ---: | --- | --- | ---: | --- |
| `AgentMCP` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `agileplus-landing` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `agslag-docs` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `AppGen` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `artifacts` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `atoms.tech` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `AtomsBot` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `AuthKit` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `byteport-landing` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `chatta` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `cheap-llm-mcp` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `Conft` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `DevHex` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `dinoforge-packs` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `DINOForge-UnityDoorstop` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `foqos-private` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `heliosBench` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `hwledger-landing` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `KlipDot` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `kmobile` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `kwality` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `localbase3` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `MCPForge` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `McpKit` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `netweave-final2` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `ObservabilityKit` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `Paginary` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `PhenoAgent` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `PhenoDevOps` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `phenodocs` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `phenodocs-scorecard-remediation` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `PhenoHandbook` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `phenokits-landing` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `PhenoProject` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `PhenoSpecs` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `phenotype-auth-ts` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `phenotype-hub` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `phenotype-journeys` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `phenotype-ops-mcp` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `phenotype-ops-mcp-fix` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `phenotype-org-audits` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `PhenoVCS` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `PlatformKit` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `PlayCua` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `projects-landing` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `ResilienceKit` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `rich-cli-kit` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `TestingKit` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `thegent-dispatch` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `thegent-landing` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `thegent-workspace` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `Tracely` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `vibeproxy-monitoring-unified` | 3 | no | no | 0 | pull request template, contributing guide, issue template |
| `GDK` | 2 | no | yes | 0 | pull request template, issue template |
| `KDesktopVirt` | 2 | no | yes | 0 | pull request template, issue template |
| `org-github` | 2 | no | yes | 0 | pull request template, issue template |
| `phenoAI` | 2 | no | yes | 0 | pull request template, issue template |
| `PhenoCompose` | 2 | no | yes | 0 | pull request template, issue template |
| `phenoData` | 2 | no | yes | 0 | pull request template, issue template |
| `phenoDesign` | 2 | no | yes | 0 | pull request template, issue template |
| `PhenoKits` | 2 | no | yes | 0 | pull request template, issue template |
| `PhenoProc` | 2 | no | yes | 0 | pull request template, issue template |
| `PhenoRuntime` | 2 | no | yes | 0 | pull request template, issue template |
| `phenotype-infra` | 2 | no | yes | 0 | pull request template, issue template |
| `phenotype-omlx` | 2 | no | no | 2 | pull request template, contributing guide |
| `phenotype-registry` | 2 | no | yes | 0 | pull request template, issue template |
| `phenotype-tooling` | 2 | no | yes | 0 | pull request template, issue template |
| `agent-devops-setups` | 1 | no | yes | 2 | pull request template |
| `bare-cua` | 1 | yes | no | 2 | contributing guide |
| `cliproxyapi-plusplus` | 1 | no | yes | 3 | pull request template |
| `eyetracker` | 1 | yes | yes | 0 | issue template |
| `helios-cli` | 1 | yes | no | 6 | contributing guide |
| `heliosCLI` | 1 | no | yes | 11 | pull request template |
| `Httpora` | 1 | yes | yes | 0 | issue template |
| `hwLedger` | 1 | yes | yes | 0 | issue template |
| `Metron` | 1 | yes | yes | 0 | issue template |
| `PhenoObservability` | 1 | yes | yes | 0 | issue template |
| `PhenoPlugins` | 1 | yes | yes | 0 | issue template |
| `phenotype-bus` | 1 | yes | yes | 0 | issue template |
| `phenoUtils` | 1 | yes | yes | 0 | issue template |
| `vibeproxy` | 1 | yes | yes | 0 | issue template |
| `agent-user-status` | 0 | yes | yes | 3 | none |
| `agentapi-plusplus` | 0 | yes | yes | 2 | none |
| `AgilePlus` | 0 | yes | yes | 5 | none |
| `argis-extensions` | 0 | yes | yes | 2 | none |
| `BytePort` | 0 | yes | yes | 3 | none |
| `Civis` | 0 | yes | yes | 2 | none |
| `cloud` | 0 | yes | yes | 3 | none |
| `Configra` | 0 | yes | yes | 2 | none |
| `DataKit` | 0 | yes | yes | 3 | none |
| `Dino` | 0 | yes | yes | 7 | none |
| `Eidolon` | 0 | yes | yes | 3 | none |
| `FocalPoint` | 0 | yes | yes | 4 | none |
| `helios-router` | 0 | yes | yes | 5 | none |
| `heliosApp` | 0 | yes | yes | 4 | none |
| `HeliosLab` | 0 | yes | yes | 2 | none |
| `nanovms` | 0 | yes | yes | 4 | none |
| `Parpoura` | 0 | yes | yes | 2 | none |
| `phench` | 0 | yes | yes | 4 | none |
| `pheno` | 0 | yes | yes | 5 | none |
| `PhenoMCP` | 0 | yes | yes | 3 | none |
| `phenoResearchEngine` | 0 | yes | yes | 4 | none |
| `phenoShared` | 0 | yes | yes | 4 | none |
| `phenoXdd` | 0 | yes | yes | 4 | none |
| `Planify` | 0 | yes | yes | 3 | none |
| `PolicyStack` | 0 | yes | yes | 4 | none |
| `portage` | 0 | yes | yes | 4 | none |
| `QuadSGM` | 0 | yes | yes | 2 | none |
| `Sidekick` | 0 | yes | yes | 3 | none |
| `Tasken` | 0 | yes | yes | 2 | none |
| `thegent` | 0 | yes | yes | 4 | none |
| `Tokn` | 0 | yes | yes | 2 | none |
| `Tracera-recovered` | 0 | yes | yes | 1 | none |

## Gap Repositories

- `AgentMCP`
- `agileplus-landing`
- `agslag-docs`
- `AppGen`
- `artifacts`
- `atoms.tech`
- `AtomsBot`
- `AuthKit`
- `byteport-landing`
- `chatta`
- `cheap-llm-mcp`
- `Conft`
- `DevHex`
- `dinoforge-packs`
- `DINOForge-UnityDoorstop`
- `foqos-private`
- `heliosBench`
- `hwledger-landing`
- `KlipDot`
- `kmobile`
- `kwality`
- `localbase3`
- `MCPForge`
- `McpKit`
- `netweave-final2`
- `ObservabilityKit`
- `Paginary`
- `PhenoAgent`
- `PhenoDevOps`
- `phenodocs`
- `phenodocs-scorecard-remediation`
- `PhenoHandbook`
- `phenokits-landing`
- `PhenoProject`
- `PhenoSpecs`
- `phenotype-auth-ts`
- `phenotype-hub`
- `phenotype-journeys`
- `phenotype-ops-mcp`
- `phenotype-ops-mcp-fix`
- `phenotype-org-audits`
- `PhenoVCS`
- `PlatformKit`
- `PlayCua`
- `projects-landing`
- `ResilienceKit`
- `rich-cli-kit`
- `TestingKit`
- `thegent-dispatch`
- `thegent-landing`
- `thegent-workspace`
- `Tracely`
- `vibeproxy-monitoring-unified`
- `GDK`
- `KDesktopVirt`
- `org-github`
- `phenoAI`
- `PhenoCompose`
- `phenoData`
- `phenoDesign`
- `PhenoKits`
- `PhenoProc`
- `PhenoRuntime`
- `phenotype-infra`
- `phenotype-omlx`
- `phenotype-registry`
- `phenotype-tooling`
- `agent-devops-setups`
- `bare-cua`
- `cliproxyapi-plusplus`
- `eyetracker`
- `helios-cli`
- `heliosCLI`
- `Httpora`
- `hwLedger`
- `Metron`
- `PhenoObservability`
- `PhenoPlugins`
- `phenotype-bus`
- `phenoUtils`
- `vibeproxy`
