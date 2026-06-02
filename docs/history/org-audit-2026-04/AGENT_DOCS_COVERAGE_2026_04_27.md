# AGENTS/CLAUDE Governance Doc Coverage - 2026-04-27

Owner audited: `KooshaPari`

Method: live GitHub API checks against non-archived repositories. For each repo, `gh api repos/KooshaPari/<repo>/contents/AGENTS.md` and `gh api repos/KooshaPari/<repo>/contents/CLAUDE.md` returning HTTP 200 counted as present.

## Summary

| Metric | Count |
|---|---:|
| Non-archived repos audited | 103 |
| Has AGENTS.md | 85 |
| Has CLAUDE.md | 75 |
| Has both | 71 |
| AGENTS.md only | 14 |
| CLAUDE.md only | 4 |
| Missing both | 14 |

## Coverage Matrix

| Repo | AGENTS.md | CLAUDE.md | Coverage Gap | Visibility | Default Branch | Last Push |
|---|---:|---:|---|---|---|---|
| [agileplus-landing](https://github.com/KooshaPari/agileplus-landing) | no | no | missing both | PUBLIC | main | 2026-04-26T21:50:23Z |
| [byteport-landing](https://github.com/KooshaPari/byteport-landing) | no | no | missing both | PUBLIC | main | 2026-04-26T21:50:20Z |
| [DINOForge-UnityDoorstop](https://github.com/KooshaPari/DINOForge-UnityDoorstop) | no | no | missing both | PUBLIC | master | 2026-04-26T21:42:14Z |
| [hwledger-landing](https://github.com/KooshaPari/hwledger-landing) | no | no | missing both | PUBLIC | main | 2026-04-26T21:50:12Z |
| [phenokits-landing](https://github.com/KooshaPari/phenokits-landing) | no | no | missing both | PUBLIC | main | 2026-04-26T08:46:07Z |
| [phenotype-journeys](https://github.com/KooshaPari/phenotype-journeys) | no | no | missing both | PRIVATE | main | 2026-04-26T22:45:02Z |
| [phenotype-ops-mcp](https://github.com/KooshaPari/phenotype-ops-mcp) | no | no | missing both | PUBLIC | main | 2026-04-26T11:09:57Z |
| [phenotype-org-governance](https://github.com/KooshaPari/phenotype-org-governance) | no | no | missing both | PRIVATE | main | 2026-04-27T08:16:49Z |
| [phenotype-registry](https://github.com/KooshaPari/phenotype-registry) | no | no | missing both | PUBLIC | main | 2026-04-27T07:51:05Z |
| [projects-landing](https://github.com/KooshaPari/projects-landing) | no | no | missing both | PUBLIC | main | 2026-04-26T18:41:13Z |
| [rich-cli-kit](https://github.com/KooshaPari/rich-cli-kit) | no | no | missing both | PRIVATE | main | 2026-04-27T03:26:29Z |
| [thegent-dispatch](https://github.com/KooshaPari/thegent-dispatch) | no | no | missing both | PRIVATE | main | 2026-04-27T03:26:19Z |
| [thegent-landing](https://github.com/KooshaPari/thegent-landing) | no | no | missing both | PUBLIC | main | 2026-04-26T18:37:59Z |
| [thegent-workspace](https://github.com/KooshaPari/thegent-workspace) | no | no | missing both | PRIVATE | main | 2026-04-27T04:23:04Z |
| [AgilePlus](https://github.com/KooshaPari/AgilePlus) | no | yes | missing AGENTS.md | PUBLIC | main | 2026-04-27T08:15:38Z |
| [phenotype-auth-ts](https://github.com/KooshaPari/phenotype-auth-ts) | no | yes | missing AGENTS.md | PUBLIC | main | 2026-04-27T08:06:45Z |
| [phenotype-tooling](https://github.com/KooshaPari/phenotype-tooling) | no | yes | missing AGENTS.md | PUBLIC | main | 2026-04-27T07:47:27Z |
| [phenoXdd](https://github.com/KooshaPari/phenoXdd) | no | yes | missing AGENTS.md | PUBLIC | main | 2026-04-26T23:06:41Z |
| [agent-user-status](https://github.com/KooshaPari/agent-user-status) | yes | no | missing CLAUDE.md | PRIVATE | main | 2026-04-27T03:19:04Z |
| [Agentora](https://github.com/KooshaPari/Agentora) | yes | no | missing CLAUDE.md | PUBLIC | main | 2026-04-27T04:21:21Z |
| [Benchora](https://github.com/KooshaPari/Benchora) | yes | no | missing CLAUDE.md | PUBLIC | main | 2026-04-27T04:21:17Z |
| [foqos-private](https://github.com/KooshaPari/foqos-private) | yes | no | missing CLAUDE.md | PRIVATE | main | 2026-04-27T04:27:31Z |
| [hwLedger](https://github.com/KooshaPari/hwLedger) | yes | no | missing CLAUDE.md | PUBLIC | main | 2026-04-27T08:03:21Z |
| [MCPForge](https://github.com/KooshaPari/MCPForge) | yes | no | missing CLAUDE.md | PUBLIC | main | 2026-04-26T21:42:02Z |
| [McpKit](https://github.com/KooshaPari/McpKit) | yes | no | missing CLAUDE.md | PUBLIC | main | 2026-04-27T02:55:54Z |
| [phenoData](https://github.com/KooshaPari/phenoData) | yes | no | missing CLAUDE.md | PUBLIC | main | 2026-04-27T03:15:43Z |
| [PhenoMCP](https://github.com/KooshaPari/PhenoMCP) | yes | no | missing CLAUDE.md | PUBLIC | main | 2026-04-27T04:26:29Z |
| [PhenoProc](https://github.com/KooshaPari/PhenoProc) | yes | no | missing CLAUDE.md | PUBLIC | main | 2026-04-27T03:47:20Z |
| [PhenoSpecs](https://github.com/KooshaPari/PhenoSpecs) | yes | no | missing CLAUDE.md | PUBLIC | main | 2026-04-26T23:25:44Z |
| [phenotype-omlx](https://github.com/KooshaPari/phenotype-omlx) | yes | no | missing CLAUDE.md | PUBLIC | main | 2026-04-27T08:07:50Z |
| [Planify](https://github.com/KooshaPari/Planify) | yes | no | missing CLAUDE.md | PUBLIC | master | 2026-04-26T17:46:41Z |
| [PlatformKit](https://github.com/KooshaPari/PlatformKit) | yes | no | missing CLAUDE.md | PUBLIC | main | 2026-04-27T08:15:28Z |
| [agent-devops-setups](https://github.com/KooshaPari/agent-devops-setups) | yes | yes | none | PUBLIC | main | 2026-04-26T23:25:26Z |
| [agentapi-plusplus](https://github.com/KooshaPari/agentapi-plusplus) | yes | yes | none | PUBLIC | main | 2026-04-27T04:14:30Z |
| [AgentMCP](https://github.com/KooshaPari/AgentMCP) | yes | yes | none | PUBLIC | main | 2026-04-26T23:16:19Z |
| [Apisync](https://github.com/KooshaPari/Apisync) | yes | yes | none | PUBLIC | main | 2026-04-26T23:08:29Z |
| [argis-extensions](https://github.com/KooshaPari/argis-extensions) | yes | yes | none | PUBLIC | main | 2026-04-26T23:08:29Z |
| [AuthKit](https://github.com/KooshaPari/AuthKit) | yes | yes | none | PUBLIC | main | 2026-04-26T23:08:30Z |
| [BytePort](https://github.com/KooshaPari/BytePort) | yes | yes | none | PUBLIC | main | 2026-04-27T08:16:05Z |
| [cheap-llm-mcp](https://github.com/KooshaPari/cheap-llm-mcp) | yes | yes | none | PRIVATE | main | 2026-04-27T04:15:25Z |
| [Civis](https://github.com/KooshaPari/Civis) | yes | yes | none | PRIVATE | main | 2026-04-27T08:15:25Z |
| [cliproxyapi-plusplus](https://github.com/KooshaPari/cliproxyapi-plusplus) | yes | yes | none | PUBLIC | main | 2026-04-27T07:40:15Z |
| [Configra](https://github.com/KooshaPari/Configra) | yes | yes | none | PRIVATE | main | 2026-04-27T08:07:55Z |
| [Conft](https://github.com/KooshaPari/Conft) | yes | yes | none | PUBLIC | main | 2026-04-27T04:14:50Z |
| [DataKit](https://github.com/KooshaPari/DataKit) | yes | yes | none | PUBLIC | main | 2026-04-27T02:55:57Z |
| [DevHex](https://github.com/KooshaPari/DevHex) | yes | yes | none | PUBLIC | main | 2026-04-26T23:16:04Z |
| [Dino](https://github.com/KooshaPari/Dino) | yes | yes | none | PUBLIC | main | 2026-04-27T08:08:02Z |
| [dinoforge-packs](https://github.com/KooshaPari/dinoforge-packs) | yes | yes | none | PUBLIC | main | 2026-04-27T03:27:08Z |
| [Eidolon](https://github.com/KooshaPari/Eidolon) | yes | yes | none | PRIVATE | main | 2026-04-27T08:09:25Z |
| [eyetracker](https://github.com/KooshaPari/eyetracker) | yes | yes | none | PUBLIC | main | 2026-04-27T04:27:27Z |
| [FocalPoint](https://github.com/KooshaPari/FocalPoint) | yes | yes | none | PUBLIC | main | 2026-04-27T04:23:47Z |
| [GDK](https://github.com/KooshaPari/GDK) | yes | yes | none | PUBLIC | main | 2026-04-27T04:21:11Z |
| [helios-cli](https://github.com/KooshaPari/helios-cli) | yes | yes | none | PUBLIC | main | 2026-04-27T07:54:06Z |
| [helios-router](https://github.com/KooshaPari/helios-router) | yes | yes | none | PRIVATE | main | 2026-04-27T08:06:44Z |
| [heliosApp](https://github.com/KooshaPari/heliosApp) | yes | yes | none | PUBLIC | main | 2026-04-26T23:41:15Z |
| [heliosBench](https://github.com/KooshaPari/heliosBench) | yes | yes | none | PUBLIC | main | 2026-04-27T03:15:11Z |
| [heliosCLI](https://github.com/KooshaPari/heliosCLI) | yes | yes | none | PUBLIC | main | 2026-04-27T08:02:40Z |
| [HeliosLab](https://github.com/KooshaPari/HeliosLab) | yes | yes | none | PUBLIC | main | 2026-04-27T08:15:30Z |
| [HexaKit](https://github.com/KooshaPari/HexaKit) | yes | yes | none | PUBLIC | main | 2026-04-27T08:16:08Z |
| [Httpora](https://github.com/KooshaPari/Httpora) | yes | yes | none | PUBLIC | main | 2026-04-26T22:08:42Z |
| [KDesktopVirt](https://github.com/KooshaPari/KDesktopVirt) | yes | yes | none | PRIVATE | main | 2026-04-27T04:36:01Z |
| [Metron](https://github.com/KooshaPari/Metron) | yes | yes | none | PUBLIC | main | 2026-04-27T04:35:48Z |
| [nanovms](https://github.com/KooshaPari/nanovms) | yes | yes | none | PUBLIC | main | 2026-04-27T03:05:42Z |
| [ObservabilityKit](https://github.com/KooshaPari/ObservabilityKit) | yes | yes | none | PUBLIC | main | 2026-04-26T23:40:19Z |
| [Paginary](https://github.com/KooshaPari/Paginary) | yes | yes | none | PRIVATE | main | 2026-04-27T03:26:32Z |
| [Parpoura](https://github.com/KooshaPari/Parpoura) | yes | yes | none | PRIVATE | main | 2026-04-27T08:06:32Z |
| [pheno](https://github.com/KooshaPari/pheno) | yes | yes | none | PUBLIC | main | 2026-04-27T08:16:03Z |
| [PhenoAgent](https://github.com/KooshaPari/PhenoAgent) | yes | yes | none | PUBLIC | main | 2026-04-26T21:59:25Z |
| [phenoAI](https://github.com/KooshaPari/phenoAI) | yes | yes | none | PUBLIC | main | 2026-04-26T21:50:09Z |
| [PhenoCompose](https://github.com/KooshaPari/PhenoCompose) | yes | yes | none | PUBLIC | main | 2026-04-27T04:24:53Z |
| [phenoDesign](https://github.com/KooshaPari/phenoDesign) | yes | yes | none | PUBLIC | main | 2026-04-27T04:27:35Z |
| [PhenoDevOps](https://github.com/KooshaPari/PhenoDevOps) | yes | yes | none | PUBLIC | main | 2026-04-26T22:26:25Z |
| [phenodocs](https://github.com/KooshaPari/phenodocs) | yes | yes | none | PUBLIC | main | 2026-04-27T07:39:57Z |
| [PhenoHandbook](https://github.com/KooshaPari/PhenoHandbook) | yes | yes | none | PUBLIC | main | 2026-04-27T03:15:46Z |
| [PhenoKits](https://github.com/KooshaPari/PhenoKits) | yes | yes | none | PUBLIC | main | 2026-04-26T23:41:42Z |
| [PhenoLang](https://github.com/KooshaPari/PhenoLang) | yes | yes | none | PUBLIC | main | 2026-04-27T08:10:03Z |
| [PhenoObservability](https://github.com/KooshaPari/PhenoObservability) | yes | yes | none | PUBLIC | main | 2026-04-27T04:51:01Z |
| [PhenoPlugins](https://github.com/KooshaPari/PhenoPlugins) | yes | yes | none | PUBLIC | main | 2026-04-27T07:36:34Z |
| [PhenoProject](https://github.com/KooshaPari/PhenoProject) | yes | yes | none | PUBLIC | main | 2026-04-27T08:16:04Z |
| [phenoResearchEngine](https://github.com/KooshaPari/phenoResearchEngine) | yes | yes | none | PRIVATE | main | 2026-04-27T04:27:20Z |
| [PhenoRuntime](https://github.com/KooshaPari/PhenoRuntime) | yes | yes | none | PUBLIC | main | 2026-04-27T02:55:50Z |
| [phenoShared](https://github.com/KooshaPari/phenoShared) | yes | yes | none | PUBLIC | main | 2026-04-27T08:13:44Z |
| [phenotype-bus](https://github.com/KooshaPari/phenotype-bus) | yes | yes | none | PRIVATE | main | 2026-04-27T08:16:09Z |
| [phenotype-hub](https://github.com/KooshaPari/phenotype-hub) | yes | yes | none | PUBLIC | main | 2026-04-27T03:05:32Z |
| [phenotype-infra](https://github.com/KooshaPari/phenotype-infra) | yes | yes | none | PUBLIC | main | 2026-04-26T23:06:38Z |
| [phenotype-org-audits](https://github.com/KooshaPari/phenotype-org-audits) | yes | yes | none | PRIVATE | main | 2026-04-27T03:26:35Z |
| [phenoUtils](https://github.com/KooshaPari/phenoUtils) | yes | yes | none | PUBLIC | main | 2026-04-27T08:16:10Z |
| [PhenoVCS](https://github.com/KooshaPari/PhenoVCS) | yes | yes | none | PUBLIC | main | 2026-04-26T23:41:31Z |
| [PlayCua](https://github.com/KooshaPari/PlayCua) | yes | yes | none | PUBLIC | master | 2026-04-26T23:40:26Z |
| [PolicyStack](https://github.com/KooshaPari/PolicyStack) | yes | yes | none | PUBLIC | main | 2026-04-27T08:15:30Z |
| [portage](https://github.com/KooshaPari/portage) | yes | yes | none | PUBLIC | main | 2026-04-25T14:24:00Z |
| [QuadSGM](https://github.com/KooshaPari/QuadSGM) | yes | yes | none | PRIVATE | main | 2026-04-27T04:38:28Z |
| [ResilienceKit](https://github.com/KooshaPari/ResilienceKit) | yes | yes | none | PUBLIC | main | 2026-04-26T23:45:15Z |
| [Sidekick](https://github.com/KooshaPari/Sidekick) | yes | yes | none | PRIVATE | main | 2026-04-27T08:17:23Z |
| [Stashly](https://github.com/KooshaPari/Stashly) | yes | yes | none | PUBLIC | main | 2026-04-26T18:40:46Z |
| [Tasken](https://github.com/KooshaPari/Tasken) | yes | yes | none | PUBLIC | main | 2026-04-27T08:17:21Z |
| [TestingKit](https://github.com/KooshaPari/TestingKit) | yes | yes | none | PUBLIC | main | 2026-04-26T23:16:16Z |
| [thegent](https://github.com/KooshaPari/thegent) | yes | yes | none | PUBLIC | main | 2026-04-27T07:46:06Z |
| [Tokn](https://github.com/KooshaPari/Tokn) | yes | yes | none | PUBLIC | main | 2026-04-27T08:09:56Z |
| [Tracely](https://github.com/KooshaPari/Tracely) | yes | yes | none | PRIVATE | main | 2026-04-27T03:26:15Z |
| [Tracera](https://github.com/KooshaPari/Tracera) | yes | yes | none | PUBLIC | main | 2026-04-27T07:38:24Z |
| [vibeproxy](https://github.com/KooshaPari/vibeproxy) | yes | yes | none | PUBLIC | main | 2026-04-26T12:01:35Z |
| [vibeproxy-monitoring-unified](https://github.com/KooshaPari/vibeproxy-monitoring-unified) | yes | yes | none | PUBLIC | main | 2026-04-27T03:26:23Z |
