# Release Automation Audit - 2026-04-27

- Owner scanned: `KooshaPari`
- Scope: non-archived repositories returned by `gh repo list KooshaPari`
- Repositories audited: 103
- Detection: default-branch root `.release-please-config.json`, `.releaserc`, `.releaserc.json`, `package.json` semantic-release signals, `.changeset/`, and `cliff.toml`.
- Verification: GitHub default-branch tree API; local checkouts were used only to clear the `helios-cli` package parse warning and confirm `Tracera` root release files after recursive tree truncation.

## Tool Breakdown

| Tool | Repo count |
| --- | ---: |
| NONE | 80 |
| release-please | 0 |
| semantic-release | 0 |
| changesets | 0 |
| git-cliff | 23 |

## Automation Classification

| Repo | Automation | release-please | semantic-release | changesets | git-cliff | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [agent-devops-setups](https://github.com/KooshaPari/agent-devops-setups) | NONE | no | no | no | no |  |
| [agent-user-status](https://github.com/KooshaPari/agent-user-status) | NONE | no | no | no | no |  |
| [agentapi-plusplus](https://github.com/KooshaPari/agentapi-plusplus) | NONE | no | no | no | no |  |
| [AgentMCP](https://github.com/KooshaPari/AgentMCP) | NONE | no | no | no | no |  |
| [Agentora](https://github.com/KooshaPari/Agentora) | NONE | no | no | no | no |  |
| [agileplus-landing](https://github.com/KooshaPari/agileplus-landing) | NONE | no | no | no | no |  |
| [AuthKit](https://github.com/KooshaPari/AuthKit) | NONE | no | no | no | no |  |
| [Benchora](https://github.com/KooshaPari/Benchora) | NONE | no | no | no | no |  |
| [BytePort](https://github.com/KooshaPari/BytePort) | NONE | no | no | no | no |  |
| [byteport-landing](https://github.com/KooshaPari/byteport-landing) | NONE | no | no | no | no |  |
| [cheap-llm-mcp](https://github.com/KooshaPari/cheap-llm-mcp) | NONE | no | no | no | no |  |
| [Civis](https://github.com/KooshaPari/Civis) | NONE | no | no | no | no |  |
| [cliproxyapi-plusplus](https://github.com/KooshaPari/cliproxyapi-plusplus) | NONE | no | no | no | no |  |
| [Configra](https://github.com/KooshaPari/Configra) | NONE | no | no | no | no |  |
| [Conft](https://github.com/KooshaPari/Conft) | NONE | no | no | no | no |  |
| [DataKit](https://github.com/KooshaPari/DataKit) | NONE | no | no | no | no |  |
| [DevHex](https://github.com/KooshaPari/DevHex) | NONE | no | no | no | no |  |
| [dinoforge-packs](https://github.com/KooshaPari/dinoforge-packs) | NONE | no | no | no | no |  |
| [DINOForge-UnityDoorstop](https://github.com/KooshaPari/DINOForge-UnityDoorstop) | NONE | no | no | no | no |  |
| [Eidolon](https://github.com/KooshaPari/Eidolon) | NONE | no | no | no | no |  |
| [eyetracker](https://github.com/KooshaPari/eyetracker) | NONE | no | no | no | no |  |
| [FocalPoint](https://github.com/KooshaPari/FocalPoint) | NONE | no | no | no | no |  |
| [foqos-private](https://github.com/KooshaPari/foqos-private) | NONE | no | no | no | no |  |
| [GDK](https://github.com/KooshaPari/GDK) | NONE | no | no | no | no |  |
| [helios-router](https://github.com/KooshaPari/helios-router) | NONE | no | no | no | no |  |
| [heliosApp](https://github.com/KooshaPari/heliosApp) | NONE | no | no | no | no |  |
| [heliosBench](https://github.com/KooshaPari/heliosBench) | NONE | no | no | no | no |  |
| [hwLedger](https://github.com/KooshaPari/hwLedger) | NONE | no | no | no | no |  |
| [hwledger-landing](https://github.com/KooshaPari/hwledger-landing) | NONE | no | no | no | no |  |
| [KDesktopVirt](https://github.com/KooshaPari/KDesktopVirt) | NONE | no | no | no | no |  |
| [MCPForge](https://github.com/KooshaPari/MCPForge) | NONE | no | no | no | no |  |
| [McpKit](https://github.com/KooshaPari/McpKit) | NONE | no | no | no | no |  |
| [Metron](https://github.com/KooshaPari/Metron) | NONE | no | no | no | no |  |
| [ObservabilityKit](https://github.com/KooshaPari/ObservabilityKit) | NONE | no | no | no | no |  |
| [Paginary](https://github.com/KooshaPari/Paginary) | NONE | no | no | no | no |  |
| [Parpoura](https://github.com/KooshaPari/Parpoura) | NONE | no | no | no | no |  |
| [PhenoAgent](https://github.com/KooshaPari/PhenoAgent) | NONE | no | no | no | no |  |
| [phenoAI](https://github.com/KooshaPari/phenoAI) | NONE | no | no | no | no |  |
| [phenoData](https://github.com/KooshaPari/phenoData) | NONE | no | no | no | no |  |
| [phenoDesign](https://github.com/KooshaPari/phenoDesign) | NONE | no | no | no | no |  |
| [PhenoDevOps](https://github.com/KooshaPari/PhenoDevOps) | NONE | no | no | no | no |  |
| [phenodocs](https://github.com/KooshaPari/phenodocs) | NONE | no | no | no | no |  |
| [PhenoHandbook](https://github.com/KooshaPari/PhenoHandbook) | NONE | no | no | no | no |  |
| [PhenoKits](https://github.com/KooshaPari/PhenoKits) | NONE | no | no | no | no |  |
| [phenokits-landing](https://github.com/KooshaPari/phenokits-landing) | NONE | no | no | no | no |  |
| [PhenoMCP](https://github.com/KooshaPari/PhenoMCP) | NONE | no | no | no | no |  |
| [PhenoObservability](https://github.com/KooshaPari/PhenoObservability) | NONE | no | no | no | no |  |
| [PhenoPlugins](https://github.com/KooshaPari/PhenoPlugins) | NONE | no | no | no | no |  |
| [PhenoProc](https://github.com/KooshaPari/PhenoProc) | NONE | no | no | no | no |  |
| [PhenoProject](https://github.com/KooshaPari/PhenoProject) | NONE | no | no | no | no |  |
| [PhenoRuntime](https://github.com/KooshaPari/PhenoRuntime) | NONE | no | no | no | no |  |
| [PhenoSpecs](https://github.com/KooshaPari/PhenoSpecs) | NONE | no | no | no | no |  |
| [phenotype-auth-ts](https://github.com/KooshaPari/phenotype-auth-ts) | NONE | no | no | no | no |  |
| [phenotype-bus](https://github.com/KooshaPari/phenotype-bus) | NONE | no | no | no | no |  |
| [phenotype-hub](https://github.com/KooshaPari/phenotype-hub) | NONE | no | no | no | no |  |
| [phenotype-infra](https://github.com/KooshaPari/phenotype-infra) | NONE | no | no | no | no |  |
| [phenotype-journeys](https://github.com/KooshaPari/phenotype-journeys) | NONE | no | no | no | no |  |
| [phenotype-omlx](https://github.com/KooshaPari/phenotype-omlx) | NONE | no | no | no | no |  |
| [phenotype-ops-mcp](https://github.com/KooshaPari/phenotype-ops-mcp) | NONE | no | no | no | no |  |
| [phenotype-org-audits](https://github.com/KooshaPari/phenotype-org-audits) | NONE | no | no | no | no |  |
| [phenotype-org-governance](https://github.com/KooshaPari/phenotype-org-governance) | NONE | no | no | no | no |  |
| [phenotype-registry](https://github.com/KooshaPari/phenotype-registry) | NONE | no | no | no | no |  |
| [phenotype-tooling](https://github.com/KooshaPari/phenotype-tooling) | NONE | no | no | no | no |  |
| [phenoUtils](https://github.com/KooshaPari/phenoUtils) | NONE | no | no | no | no |  |
| [PhenoVCS](https://github.com/KooshaPari/PhenoVCS) | NONE | no | no | no | no |  |
| [phenoXdd](https://github.com/KooshaPari/phenoXdd) | NONE | no | no | no | no |  |
| [Planify](https://github.com/KooshaPari/Planify) | NONE | no | no | no | no |  |
| [PlatformKit](https://github.com/KooshaPari/PlatformKit) | NONE | no | no | no | no |  |
| [PlayCua](https://github.com/KooshaPari/PlayCua) | NONE | no | no | no | no |  |
| [projects-landing](https://github.com/KooshaPari/projects-landing) | NONE | no | no | no | no |  |
| [QuadSGM](https://github.com/KooshaPari/QuadSGM) | NONE | no | no | no | no |  |
| [ResilienceKit](https://github.com/KooshaPari/ResilienceKit) | NONE | no | no | no | no |  |
| [rich-cli-kit](https://github.com/KooshaPari/rich-cli-kit) | NONE | no | no | no | no |  |
| [Sidekick](https://github.com/KooshaPari/Sidekick) | NONE | no | no | no | no |  |
| [TestingKit](https://github.com/KooshaPari/TestingKit) | NONE | no | no | no | no |  |
| [thegent-dispatch](https://github.com/KooshaPari/thegent-dispatch) | NONE | no | no | no | no |  |
| [thegent-landing](https://github.com/KooshaPari/thegent-landing) | NONE | no | no | no | no |  |
| [thegent-workspace](https://github.com/KooshaPari/thegent-workspace) | NONE | no | no | no | no |  |
| [Tracely](https://github.com/KooshaPari/Tracely) | NONE | no | no | no | no |  |
| [Tracera](https://github.com/KooshaPari/Tracera) | NONE | no | no | no | no |  |
| [AgilePlus](https://github.com/KooshaPari/AgilePlus) | git-cliff | no | no | no | yes |  |
| [Apisync](https://github.com/KooshaPari/Apisync) | git-cliff | no | no | no | yes |  |
| [argis-extensions](https://github.com/KooshaPari/argis-extensions) | git-cliff | no | no | no | yes |  |
| [Dino](https://github.com/KooshaPari/Dino) | git-cliff | no | no | no | yes |  |
| [helios-cli](https://github.com/KooshaPari/helios-cli) | git-cliff | no | no | no | yes |  |
| [heliosCLI](https://github.com/KooshaPari/heliosCLI) | git-cliff | no | no | no | yes |  |
| [HeliosLab](https://github.com/KooshaPari/HeliosLab) | git-cliff | no | no | no | yes |  |
| [HexaKit](https://github.com/KooshaPari/HexaKit) | git-cliff | no | no | no | yes |  |
| [Httpora](https://github.com/KooshaPari/Httpora) | git-cliff | no | no | no | yes |  |
| [nanovms](https://github.com/KooshaPari/nanovms) | git-cliff | no | no | no | yes |  |
| [pheno](https://github.com/KooshaPari/pheno) | git-cliff | no | no | no | yes |  |
| [PhenoCompose](https://github.com/KooshaPari/PhenoCompose) | git-cliff | no | no | no | yes |  |
| [PhenoLang](https://github.com/KooshaPari/PhenoLang) | git-cliff | no | no | no | yes |  |
| [phenoResearchEngine](https://github.com/KooshaPari/phenoResearchEngine) | git-cliff | no | no | no | yes |  |
| [phenoShared](https://github.com/KooshaPari/phenoShared) | git-cliff | no | no | no | yes |  |
| [PolicyStack](https://github.com/KooshaPari/PolicyStack) | git-cliff | no | no | no | yes |  |
| [portage](https://github.com/KooshaPari/portage) | git-cliff | no | no | no | yes |  |
| [Stashly](https://github.com/KooshaPari/Stashly) | git-cliff | no | no | no | yes |  |
| [Tasken](https://github.com/KooshaPari/Tasken) | git-cliff | no | no | no | yes |  |
| [thegent](https://github.com/KooshaPari/thegent) | git-cliff | no | no | no | yes |  |
| [Tokn](https://github.com/KooshaPari/Tokn) | git-cliff | no | no | no | yes |  |
| [vibeproxy](https://github.com/KooshaPari/vibeproxy) | git-cliff | no | no | no | yes |  |
| [vibeproxy-monitoring-unified](https://github.com/KooshaPari/vibeproxy-monitoring-unified) | git-cliff | no | no | no | yes |  |

## Gap Repositories

- agent-devops-setups
- agent-user-status
- agentapi-plusplus
- AgentMCP
- Agentora
- agileplus-landing
- AuthKit
- Benchora
- BytePort
- byteport-landing
- cheap-llm-mcp
- Civis
- cliproxyapi-plusplus
- Configra
- Conft
- DataKit
- DevHex
- dinoforge-packs
- DINOForge-UnityDoorstop
- Eidolon
- eyetracker
- FocalPoint
- foqos-private
- GDK
- helios-router
- heliosApp
- heliosBench
- hwLedger
- hwledger-landing
- KDesktopVirt
- MCPForge
- McpKit
- Metron
- ObservabilityKit
- Paginary
- Parpoura
- PhenoAgent
- phenoAI
- phenoData
- phenoDesign
- PhenoDevOps
- phenodocs
- PhenoHandbook
- PhenoKits
- phenokits-landing
- PhenoMCP
- PhenoObservability
- PhenoPlugins
- PhenoProc
- PhenoProject
- PhenoRuntime
- PhenoSpecs
- phenotype-auth-ts
- phenotype-bus
- phenotype-hub
- phenotype-infra
- phenotype-journeys
- phenotype-omlx
- phenotype-ops-mcp
- phenotype-org-audits
- phenotype-org-governance
- phenotype-registry
- phenotype-tooling
- phenoUtils
- PhenoVCS
- phenoXdd
- Planify
- PlatformKit
- PlayCua
- projects-landing
- QuadSGM
- ResilienceKit
- rich-cli-kit
- Sidekick
- TestingKit
- thegent-dispatch
- thegent-landing
- thegent-workspace
- Tracely
- Tracera
