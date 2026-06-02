# Actions Pinning Hygiene Audit - 2026-04-27

Scope: non-archived `KooshaPari` repositories. Workflow contents were fetched from live GitHub repository contents through API surfaces and `uses:` references were classified by ref form.

Scorecard target: third-party GitHub Actions should be pinned to immutable 40-character commit SHAs. Local actions (`./`, `../`) and `docker://` references are counted separately and excluded from the org pinning percentage.

## Summary

- Non-archived repos scanned: 103
- Repos with workflows: 101
- Workflow files scanned: 1006
- External `uses:` references: 3790
- Pinned to commit SHA: 632
- Unpinned refs: 3158
- Org pinning percentage: 16.7%

## Classification Totals

| Classification | Count |
| --- | ---: |
| pinned-to-sha | 632 |
| pinned-to-tag | 2771 |
| pinned-to-branch | 126 |
| unpinned-other-ref | 261 |
| unpinned-missing-ref | 0 |

## Repository Counts

Sorted by most unpinned external action references first.

| Repo | Workflows | External uses | SHA | Tag | Branch | Other ref | Missing ref | Local/docker | Pinned % |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| [Tracera](https://github.com/KooshaPari/Tracera) | 37 | 323 | 6 | 316 | 1 | 0 | 0 | 0 | 1.9% |
| [heliosCLI](https://github.com/KooshaPari/heliosCLI) | 47 | 227 | 17 | 188 | 1 | 21 | 0 | 6 | 7.5% |
| [PhenoLang](https://github.com/KooshaPari/PhenoLang) | 43 | 187 | 7 | 161 | 0 | 19 | 0 | 15 | 3.7% |
| [HexaKit](https://github.com/KooshaPari/HexaKit) | 42 | 183 | 7 | 153 | 4 | 19 | 0 | 15 | 3.8% |
| [pheno](https://github.com/KooshaPari/pheno) | 41 | 178 | 8 | 148 | 3 | 19 | 0 | 15 | 4.5% |
| [helios-cli](https://github.com/KooshaPari/helios-cli) | 33 | 168 | 16 | 137 | 2 | 13 | 0 | 8 | 9.5% |
| [AgilePlus](https://github.com/KooshaPari/AgilePlus) | 33 | 136 | 3 | 109 | 7 | 17 | 0 | 10 | 2.2% |
| [thegent](https://github.com/KooshaPari/thegent) | 21 | 113 | 8 | 96 | 5 | 4 | 0 | 0 | 7.1% |
| [portage](https://github.com/KooshaPari/portage) | 28 | 101 | 9 | 86 | 4 | 2 | 0 | 3 | 8.9% |
| [heliosApp](https://github.com/KooshaPari/heliosApp) | 29 | 91 | 2 | 84 | 5 | 0 | 0 | 1 | 2.2% |
| [FocalPoint](https://github.com/KooshaPari/FocalPoint) | 18 | 76 | 1 | 59 | 1 | 15 | 0 | 0 | 1.3% |
| [QuadSGM](https://github.com/KooshaPari/QuadSGM) | 18 | 68 | 5 | 60 | 3 | 0 | 0 | 0 | 7.4% |
| [Stashly](https://github.com/KooshaPari/Stashly) | 14 | 69 | 8 | 48 | 5 | 8 | 0 | 0 | 11.6% |
| [agentapi-plusplus](https://github.com/KooshaPari/agentapi-plusplus) | 27 | 64 | 9 | 52 | 1 | 2 | 0 | 0 | 14.1% |
| [Tasken](https://github.com/KooshaPari/Tasken) | 14 | 60 | 5 | 43 | 3 | 9 | 0 | 0 | 8.3% |
| [vibeproxy](https://github.com/KooshaPari/vibeproxy) | 11 | 53 | 3 | 44 | 1 | 5 | 0 | 3 | 5.7% |
| [HeliosLab](https://github.com/KooshaPari/HeliosLab) | 12 | 51 | 1 | 42 | 1 | 7 | 0 | 0 | 2.0% |
| [argis-extensions](https://github.com/KooshaPari/argis-extensions) | 8 | 50 | 2 | 43 | 2 | 3 | 0 | 0 | 4.0% |
| [Apisync](https://github.com/KooshaPari/Apisync) | 9 | 49 | 6 | 35 | 4 | 4 | 0 | 0 | 12.2% |
| [Civis](https://github.com/KooshaPari/Civis) | 19 | 43 | 3 | 34 | 3 | 3 | 0 | 0 | 7.0% |
| [phenoResearchEngine](https://github.com/KooshaPari/phenoResearchEngine) | 8 | 43 | 6 | 32 | 2 | 3 | 0 | 0 | 14.0% |
| [hwLedger](https://github.com/KooshaPari/hwLedger) | 11 | 39 | 2 | 28 | 0 | 9 | 0 | 0 | 5.1% |
| [KDesktopVirt](https://github.com/KooshaPari/KDesktopVirt) | 7 | 35 | 1 | 32 | 0 | 2 | 0 | 0 | 2.9% |
| [phenodocs](https://github.com/KooshaPari/phenodocs) | 13 | 33 | 0 | 31 | 0 | 2 | 0 | 0 | 0.0% |
| [nanovms](https://github.com/KooshaPari/nanovms) | 8 | 38 | 6 | 28 | 3 | 1 | 0 | 0 | 15.8% |
| [helios-router](https://github.com/KooshaPari/helios-router) | 7 | 30 | 0 | 30 | 0 | 0 | 0 | 0 | 0.0% |
| [BytePort](https://github.com/KooshaPari/BytePort) | 8 | 28 | 1 | 25 | 1 | 1 | 0 | 0 | 3.6% |
| [phenoShared](https://github.com/KooshaPari/phenoShared) | 12 | 28 | 1 | 25 | 1 | 1 | 0 | 0 | 3.6% |
| [Tokn](https://github.com/KooshaPari/Tokn) | 25 | 87 | 64 | 6 | 8 | 9 | 0 | 0 | 73.6% |
| [phenoDesign](https://github.com/KooshaPari/phenoDesign) | 7 | 24 | 1 | 22 | 1 | 0 | 0 | 0 | 4.2% |
| [MCPForge](https://github.com/KooshaPari/MCPForge) | 7 | 24 | 2 | 22 | 0 | 0 | 0 | 0 | 8.3% |
| [phenotype-infra](https://github.com/KooshaPari/phenotype-infra) | 9 | 23 | 1 | 19 | 0 | 3 | 0 | 0 | 4.3% |
| [vibeproxy-monitoring-unified](https://github.com/KooshaPari/vibeproxy-monitoring-unified) | 8 | 26 | 5 | 19 | 2 | 0 | 0 | 0 | 19.2% |
| [Configra](https://github.com/KooshaPari/Configra) | 14 | 22 | 1 | 15 | 4 | 2 | 0 | 2 | 4.5% |
| [PhenoProc](https://github.com/KooshaPari/PhenoProc) | 8 | 20 | 1 | 15 | 4 | 0 | 0 | 0 | 5.0% |
| [Tracely](https://github.com/KooshaPari/Tracely) | 6 | 19 | 0 | 13 | 3 | 3 | 0 | 0 | 0.0% |
| [agent-devops-setups](https://github.com/KooshaPari/agent-devops-setups) | 10 | 19 | 1 | 15 | 3 | 0 | 0 | 0 | 5.3% |
| [GDK](https://github.com/KooshaPari/GDK) | 9 | 19 | 2 | 14 | 2 | 1 | 0 | 0 | 10.5% |
| [DINOForge-UnityDoorstop](https://github.com/KooshaPari/DINOForge-UnityDoorstop) | 2 | 17 | 0 | 16 | 0 | 1 | 0 | 0 | 0.0% |
| [Parpoura](https://github.com/KooshaPari/Parpoura) | 9 | 19 | 3 | 16 | 0 | 0 | 0 | 0 | 15.8% |
| [Httpora](https://github.com/KooshaPari/Httpora) | 6 | 18 | 2 | 14 | 2 | 0 | 0 | 0 | 11.1% |
| [phenoAI](https://github.com/KooshaPari/phenoAI) | 7 | 17 | 1 | 12 | 0 | 4 | 0 | 0 | 5.9% |
| [PhenoHandbook](https://github.com/KooshaPari/PhenoHandbook) | 5 | 16 | 0 | 13 | 0 | 3 | 0 | 0 | 0.0% |
| [PhenoObservability](https://github.com/KooshaPari/PhenoObservability) | 10 | 16 | 0 | 10 | 4 | 2 | 0 | 0 | 0.0% |
| [Agentora](https://github.com/KooshaPari/Agentora) | 2 | 15 | 0 | 11 | 0 | 4 | 0 | 0 | 0.0% |
| [AuthKit](https://github.com/KooshaPari/AuthKit) | 5 | 15 | 0 | 14 | 0 | 1 | 0 | 0 | 0.0% |
| [PhenoPlugins](https://github.com/KooshaPari/PhenoPlugins) | 6 | 15 | 0 | 11 | 3 | 1 | 0 | 0 | 0.0% |
| [PhenoVCS](https://github.com/KooshaPari/PhenoVCS) | 4 | 15 | 0 | 11 | 3 | 1 | 0 | 0 | 0.0% |
| [McpKit](https://github.com/KooshaPari/McpKit) | 4 | 16 | 2 | 13 | 0 | 1 | 0 | 0 | 12.5% |
| [PhenoCompose](https://github.com/KooshaPari/PhenoCompose) | 6 | 15 | 1 | 12 | 0 | 2 | 0 | 0 | 6.7% |
| [PhenoKits](https://github.com/KooshaPari/PhenoKits) | 8 | 15 | 1 | 9 | 5 | 0 | 0 | 0 | 6.7% |
| [agent-user-status](https://github.com/KooshaPari/agent-user-status) | 4 | 14 | 2 | 12 | 0 | 0 | 0 | 0 | 14.3% |
| [Metron](https://github.com/KooshaPari/Metron) | 7 | 14 | 2 | 10 | 0 | 2 | 0 | 0 | 14.3% |
| [PlayCua](https://github.com/KooshaPari/PlayCua) | 4 | 12 | 0 | 9 | 0 | 3 | 0 | 0 | 0.0% |
| [phenotype-journeys](https://github.com/KooshaPari/phenotype-journeys) | 5 | 14 | 3 | 11 | 0 | 0 | 0 | 0 | 21.4% |
| [DataKit](https://github.com/KooshaPari/DataKit) | 5 | 13 | 2 | 9 | 0 | 2 | 0 | 0 | 15.4% |
| [DevHex](https://github.com/KooshaPari/DevHex) | 6 | 13 | 2 | 9 | 0 | 2 | 0 | 0 | 15.4% |
| [PhenoRuntime](https://github.com/KooshaPari/PhenoRuntime) | 7 | 13 | 2 | 9 | 0 | 2 | 0 | 0 | 15.4% |
| [PhenoSpecs](https://github.com/KooshaPari/PhenoSpecs) | 4 | 13 | 2 | 11 | 0 | 0 | 0 | 0 | 15.4% |
| [Eidolon](https://github.com/KooshaPari/Eidolon) | 6 | 11 | 0 | 9 | 1 | 1 | 0 | 0 | 0.0% |
| [phenotype-bus](https://github.com/KooshaPari/phenotype-bus) | 4 | 11 | 0 | 9 | 0 | 2 | 0 | 0 | 0.0% |
| [Sidekick](https://github.com/KooshaPari/Sidekick) | 6 | 11 | 0 | 9 | 1 | 1 | 0 | 0 | 0.0% |
| [phenotype-ops-mcp](https://github.com/KooshaPari/phenotype-ops-mcp) | 4 | 11 | 1 | 10 | 0 | 0 | 0 | 0 | 9.1% |
| [cheap-llm-mcp](https://github.com/KooshaPari/cheap-llm-mcp) | 4 | 10 | 0 | 7 | 0 | 3 | 0 | 0 | 0.0% |
| [phenotype-registry](https://github.com/KooshaPari/phenotype-registry) | 2 | 10 | 0 | 10 | 0 | 0 | 0 | 0 | 0.0% |
| [foqos-private](https://github.com/KooshaPari/foqos-private) | 6 | 11 | 2 | 9 | 0 | 0 | 0 | 0 | 18.2% |
| [phenotype-tooling](https://github.com/KooshaPari/phenotype-tooling) | 7 | 11 | 2 | 8 | 0 | 1 | 0 | 0 | 18.2% |
| [PhenoMCP](https://github.com/KooshaPari/PhenoMCP) | 3 | 9 | 0 | 7 | 0 | 2 | 0 | 0 | 0.0% |
| [cliproxyapi-plusplus](https://github.com/KooshaPari/cliproxyapi-plusplus) | 26 | 113 | 105 | 0 | 3 | 5 | 0 | 0 | 92.9% |
| [Benchora](https://github.com/KooshaPari/Benchora) | 4 | 10 | 2 | 5 | 3 | 0 | 0 | 0 | 20.0% |
| [Paginary](https://github.com/KooshaPari/Paginary) | 5 | 8 | 0 | 7 | 1 | 0 | 0 | 0 | 0.0% |
| [dinoforge-packs](https://github.com/KooshaPari/dinoforge-packs) | 6 | 9 | 2 | 7 | 0 | 0 | 0 | 0 | 22.2% |
| [ObservabilityKit](https://github.com/KooshaPari/ObservabilityKit) | 6 | 9 | 2 | 7 | 0 | 0 | 0 | 0 | 22.2% |
| [PhenoProject](https://github.com/KooshaPari/PhenoProject) | 6 | 9 | 2 | 7 | 0 | 0 | 0 | 0 | 22.2% |
| [phenotype-hub](https://github.com/KooshaPari/phenotype-hub) | 5 | 9 | 2 | 7 | 0 | 0 | 0 | 0 | 22.2% |
| [PhenoAgent](https://github.com/KooshaPari/PhenoAgent) | 4 | 7 | 0 | 7 | 0 | 0 | 0 | 0 | 0.0% |
| [rich-cli-kit](https://github.com/KooshaPari/rich-cli-kit) | 4 | 7 | 0 | 7 | 0 | 0 | 0 | 0 | 0.0% |
| [thegent-dispatch](https://github.com/KooshaPari/thegent-dispatch) | 4 | 7 | 0 | 7 | 0 | 0 | 0 | 0 | 0.0% |
| [thegent-workspace](https://github.com/KooshaPari/thegent-workspace) | 4 | 7 | 0 | 7 | 0 | 0 | 0 | 0 | 0.0% |
| [PhenoDevOps](https://github.com/KooshaPari/PhenoDevOps) | 6 | 6 | 0 | 3 | 3 | 0 | 0 | 0 | 0.0% |
| [TestingKit](https://github.com/KooshaPari/TestingKit) | 3 | 6 | 0 | 4 | 2 | 0 | 0 | 0 | 0.0% |
| [Dino](https://github.com/KooshaPari/Dino) | 24 | 117 | 112 | 0 | 1 | 4 | 0 | 0 | 95.7% |
| [phenotype-auth-ts](https://github.com/KooshaPari/phenotype-auth-ts) | 3 | 7 | 2 | 5 | 0 | 0 | 0 | 0 | 28.6% |
| [phenotype-omlx](https://github.com/KooshaPari/phenotype-omlx) | 2 | 5 | 0 | 5 | 0 | 0 | 0 | 0 | 0.0% |
| [phenoUtils](https://github.com/KooshaPari/phenoUtils) | 3 | 5 | 0 | 4 | 0 | 1 | 0 | 0 | 0.0% |
| [Conft](https://github.com/KooshaPari/Conft) | 5 | 8 | 4 | 4 | 0 | 0 | 0 | 0 | 50.0% |
| [heliosBench](https://github.com/KooshaPari/heliosBench) | 1 | 4 | 0 | 4 | 0 | 0 | 0 | 0 | 0.0% |
| [phenotype-org-audits](https://github.com/KooshaPari/phenotype-org-audits) | 1 | 4 | 0 | 3 | 0 | 1 | 0 | 0 | 0.0% |
| [phenoXdd](https://github.com/KooshaPari/phenoXdd) | 1 | 4 | 0 | 4 | 0 | 0 | 0 | 0 | 0.0% |
| [PlatformKit](https://github.com/KooshaPari/PlatformKit) | 1 | 4 | 0 | 4 | 0 | 0 | 0 | 0 | 0.0% |
| [eyetracker](https://github.com/KooshaPari/eyetracker) | 1 | 3 | 0 | 2 | 0 | 1 | 0 | 0 | 0.0% |
| [PolicyStack](https://github.com/KooshaPari/PolicyStack) | 16 | 81 | 79 | 0 | 1 | 1 | 0 | 0 | 97.5% |
| [agileplus-landing](https://github.com/KooshaPari/agileplus-landing) | 1 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0.0% |
| [byteport-landing](https://github.com/KooshaPari/byteport-landing) | 1 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0.0% |
| [hwledger-landing](https://github.com/KooshaPari/hwledger-landing) | 1 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0.0% |
| [phenokits-landing](https://github.com/KooshaPari/phenokits-landing) | 1 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0.0% |
| [projects-landing](https://github.com/KooshaPari/projects-landing) | 1 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0.0% |
| [ResilienceKit](https://github.com/KooshaPari/ResilienceKit) | 2 | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 0.0% |
| [thegent-landing](https://github.com/KooshaPari/thegent-landing) | 1 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0.0% |
| [phenoData](https://github.com/KooshaPari/phenoData) | 7 | 16 | 15 | 0 | 1 | 0 | 0 | 0 | 93.8% |
| [Planify](https://github.com/KooshaPari/Planify) | 11 | 54 | 54 | 0 | 0 | 0 | 0 | 0 | 100.0% |
| [AgentMCP](https://github.com/KooshaPari/AgentMCP) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 100.0% |
| [phenotype-org-governance](https://github.com/KooshaPari/phenotype-org-governance) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 100.0% |

## Unpinned References

### Tracera (317 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `architecture.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `architecture.yml` | 21 | pinned-to-tag | `astral-sh/setup-uv@v2` |
| `architecture.yml` | 26 | pinned-to-tag | `actions/setup-python@v5` |
| `architecture.yml` | 40 | pinned-to-tag | `actions/upload-artifact@v4` |
| `architecture.yml` | 48 | pinned-to-tag | `actions/github-script@v7` |
| `benchmarks.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `benchmarks.yml` | 20 | pinned-to-tag | `actions/setup-go@v5` |
| `benchmarks.yml` | 28 | pinned-to-tag | `actions/upload-artifact@v4` |
| `canary-deploy.yml` | 47 | pinned-to-tag | `actions/checkout@v4` |
| `canary-deploy.yml` | 82 | pinned-to-tag | `actions/checkout@v4` |
| `canary-deploy.yml` | 142 | pinned-to-tag | `actions/checkout@v4` |
| `canary-deploy.yml` | 213 | pinned-to-tag | `actions/checkout@v4` |
| `canary-deploy.yml` | 270 | pinned-to-tag | `actions/checkout@v4` |
| `canary-deploy.yml` | 344 | pinned-to-tag | `actions/checkout@v4` |
| `chaos-tests.yml` | 83 | pinned-to-tag | `actions/checkout@v4` |
| `chaos-tests.yml` | 86 | pinned-to-tag | `actions/setup-python@v5` |
| `chaos-tests.yml` | 193 | pinned-to-tag | `actions/upload-artifact@v4` |
| `chaos-tests.yml` | 202 | pinned-to-tag | `8398a7/action-slack@v3` |
| `chaos-tests.yml` | 220 | pinned-to-tag | `actions/checkout@v4` |
| `chaos-tests.yml` | 223 | pinned-to-tag | `azure/setup-kubectl@v4` |
| `chromatic.yml` | 38 | pinned-to-tag | `actions/checkout@v4` |
| `chromatic.yml` | 43 | pinned-to-tag | `actions/setup-node@v4` |
| `chromatic.yml` | 49 | pinned-to-tag | `oven-sh/setup-bun@v1` |
| `chromatic.yml` | 54 | pinned-to-tag | `actions/cache@v3` |
| `chromatic.yml` | 77 | pinned-to-tag | `actions/upload-artifact@v4` |
| `chromatic.yml` | 85 | pinned-to-tag | `actions/github-script@v7` |
| `ci-cd.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `ci-cd.yml` | 59 | pinned-to-tag | `actions/checkout@v3` |
| `ci-cd.yml` | 64 | pinned-to-tag | `actions/setup-python@v4` |
| `ci-cd.yml` | 81 | pinned-to-tag | `codecov/codecov-action@v3` |
| `ci-cd.yml` | 91 | pinned-to-tag | `actions/checkout@v3` |
| `ci-cd.yml` | 94 | pinned-to-tag | `actions/setup-python@v4` |
| `ci-cd.yml` | 167 | pinned-to-tag | `actions/checkout@v3` |
| `ci-cd.yml` | 170 | pinned-to-tag | `docker/setup-buildx-action@v2` |
| `ci-cd.yml` | 173 | pinned-to-tag | `docker/build-push-action@v4` |
| `ci-cd.yml` | 185 | pinned-to-tag | `actions/checkout@v3` |
| `ci.yml` | 61 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 104 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 145 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 148 | pinned-to-tag | `actions/setup-python@v5` |
| `ci.yml` | 159 | pinned-to-tag | `actions/cache@v4` |
| `ci.yml` | 209 | pinned-to-tag | `actions/upload-artifact@v4` |
| `ci.yml` | 322 | pinned-to-tag | `codecov/codecov-action@v4` |
| `ci.yml` | 331 | pinned-to-tag | `actions/upload-artifact@v4` |
| `ci.yml` | 341 | pinned-to-tag | `actions/upload-artifact@v4` |
| `ci.yml` | 385 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 388 | pinned-to-tag | `actions/setup-python@v5` |
| `ci.yml` | 463 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 466 | pinned-to-tag | `actions/setup-go@v5` |
| `ci.yml` | 472 | pinned-to-tag | `actions/cache@v4` |
| `ci.yml` | 486 | pinned-to-tag | `golangci/golangci-lint-action@v9` |
| `ci.yml` | 511 | pinned-to-tag | `actions/upload-artifact@v4` |
| `ci.yml` | 658 | pinned-to-tag | `actions/download-artifact@v4` |
| `ci.yml` | 697 | pinned-to-tag | `actions/upload-artifact@v4` |
| `ci.yml` | 718 | pinned-to-tag | `codecov/codecov-action@v4` |
| `ci.yml` | 727 | pinned-to-tag | `actions/upload-artifact@v4` |
| `ci.yml` | 736 | pinned-to-tag | `actions/upload-artifact@v4` |
| `ci.yml` | 750 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 753 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `ci.yml` | 758 | pinned-to-tag | `actions/cache@v4` |
| `ci.yml` | 801 | pinned-to-tag | `actions/upload-artifact@v4` |
| `ci.yml` | 859 | pinned-to-tag | `actions/upload-artifact@v4` |
| `ci.yml` | 899 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 902 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `ci.yml` | 907 | pinned-to-tag | `actions/cache@v4` |
| `ci.yml` | 919 | pinned-to-tag | `actions/cache@v4` |
| `ci.yml` | 972 | pinned-to-tag | `actions/upload-artifact@v4` |
| `ci.yml` | 980 | pinned-to-tag | `actions/upload-artifact@v4` |
| `ci.yml` | 990 | pinned-to-tag | `actions/upload-artifact@v4` |
| `ci.yml` | 998 | pinned-to-tag | `actions/upload-artifact@v4` |
| `ci.yml` | 1011 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 1014 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `ci.yml` | 1019 | pinned-to-tag | `actions/cache@v4` |
| `ci.yml` | 1048 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 1051 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `ci.yml` | 1056 | pinned-to-tag | `actions/cache@v4` |
| `ci.yml` | 1073 | pinned-to-tag | `actions/upload-artifact@v4` |
| `ci.yml` | 1086 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 1089 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `ci.yml` | 1094 | pinned-to-tag | `actions/cache@v4` |
| `ci.yml` | 1111 | pinned-to-tag | `actions/upload-artifact@v4` |
| `ci.yml` | 1124 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 1127 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `ci.yml` | 1132 | pinned-to-tag | `actions/cache@v4` |
| `ci.yml` | 1149 | pinned-to-tag | `actions/upload-artifact@v4` |
| `ci.yml` | 1162 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 1165 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `ci.yml` | 1170 | pinned-to-tag | `actions/cache@v4` |
| `ci.yml` | 1191 | pinned-to-tag | `actions/upload-artifact@v4` |
| `ci.yml` | 1204 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 1207 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `ci.yml` | 1226 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `ci.yml` | 1233 | pinned-to-tag | `returntocorp/semgrep-action@v1` |
| `ci.yml` | 1245 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 1248 | pinned-to-tag | `actions/download-artifact@v4` |
| `ci.yml` | 1254 | pinned-to-tag | `actions/download-artifact@v4` |
| `ci.yml` | 1437 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 1440 | pinned-to-tag | `docker/setup-buildx-action@v3` |
| `ci.yml` | 1443 | pinned-to-tag | `docker/login-action@v3` |
| `ci.yml` | 1451 | pinned-to-tag | `docker/metadata-action@v5` |
| `ci.yml` | 1463 | pinned-to-tag | `docker/build-push-action@v5` |
| `ci.yml` | 1478 | pinned-to-tag | `docker/metadata-action@v5` |
| `ci.yml` | 1490 | pinned-to-tag | `docker/build-push-action@v5` |
| `ci.yml` | 1516 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 1525 | pinned-to-tag | `pulumi/actions@v5` |
| `ci.yml` | 1546 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 1549 | pinned-to-tag | `azure/setup-kubectl@v4` |
| `ci.yml` | 1585 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 1588 | pinned-to-tag | `azure/setup-kubectl@v4` |
| `contract-tests.yml` | 37 | pinned-to-tag | `actions/checkout@v4` |
| `contract-tests.yml` | 40 | pinned-to-tag | `oven-sh/setup-bun@v1` |
| `contract-tests.yml` | 55 | pinned-to-tag | `actions/upload-artifact@v4` |
| `contract-tests.yml` | 63 | pinned-to-tag | `dorny/test-reporter@v1` |
| `contract-tests.yml` | 92 | pinned-to-tag | `actions/checkout@v4` |
| `contract-tests.yml` | 95 | pinned-to-tag | `actions/setup-go@v5` |
| `contract-tests.yml` | 101 | pinned-to-tag | `actions/download-artifact@v4` |
| `contract-tests.yml` | 124 | pinned-to-tag | `dorny/test-reporter@v1` |
| `contract-tests.yml` | 139 | pinned-to-tag | `actions/checkout@v4` |
| `contract-tests.yml` | 142 | pinned-to-tag | `actions/download-artifact@v4` |
| `contract-tests.yml` | 189 | pinned-to-tag | `actions/checkout@v4` |
| `contract-tests.yml` | 192 | pinned-to-tag | `actions/download-artifact@v4` |
| `contract-tests.yml` | 203 | pinned-to-tag | `actions/upload-artifact@v4` |
| `contract-tests.yml` | 211 | pinned-to-tag | `actions/github-script@v7` |
| `contracts.yml` | 43 | pinned-to-tag | `actions/checkout@v4` |
| `contracts.yml` | 46 | pinned-to-tag | `actions/setup-go@v5` |
| `contracts.yml` | 54 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `contracts.yml` | 59 | pinned-to-tag | `astral-sh/setup-uv@v2` |
| `contracts.yml` | 64 | pinned-to-tag | `actions/setup-python@v5` |
| `contracts.yml` | 69 | pinned-to-tag | `actions/cache@v4` |
| `dependabot-auto-merge.yml` | 23 | pinned-to-tag | `actions/checkout@v4` |
| `dependabot-auto-merge.yml` | 29 | pinned-to-tag | `dependabot/fetch-metadata@v2` |
| `dependabot-auto-merge.yml` | 49 | pinned-to-tag | `actions/setup-node@v4` |
| `dependabot-auto-merge.yml` | 55 | pinned-to-tag | `actions/setup-python@v5` |
| `dependabot-auto-merge.yml` | 62 | pinned-to-tag | `actions/setup-go@v5` |
| `dependabot-auto-merge.yml` | 112 | pinned-to-tag | `dependabot/fetch-metadata@v2` |
| `dependabot-auto-merge.yml` | 138 | pinned-to-tag | `dependabot/fetch-metadata@v2` |
| `deployment-rollback.yml` | 41 | pinned-to-tag | `actions/checkout@v4` |
| `deployment-rollback.yml` | 69 | pinned-to-tag | `actions/github-script@v7` |
| `deployment-rollback.yml` | 137 | pinned-to-tag | `actions/checkout@v4` |
| `deployment-rollback.yml` | 217 | pinned-to-tag | `actions/checkout@v4` |
| `deployment-rollback.yml` | 266 | pinned-to-tag | `actions/github-script@v7` |
| `deployment-rollback.yml` | 324 | pinned-to-tag | `actions/github-script@v7` |
| `docs-deploy.yml` | 47 | pinned-to-tag | `actions/checkout@v4` |
| `docs-deploy.yml` | 73 | pinned-to-tag | `actions/setup-go@v5` |
| `docs-deploy.yml` | 121 | pinned-to-tag | `actions/upload-artifact@v4` |
| `docs-deploy.yml` | 138 | pinned-to-tag | `actions/checkout@v4` |
| `docs-deploy.yml` | 141 | pinned-to-tag | `oven-sh/setup-bun@v1` |
| `docs-deploy.yml` | 146 | pinned-to-tag | `actions/download-artifact@v4` |
| `docs-deploy.yml` | 174 | pinned-to-tag | `actions/upload-artifact@v4` |
| `docs-deploy.yml` | 192 | pinned-to-tag | `actions/checkout@v4` |
| `docs-deploy.yml` | 195 | pinned-to-tag | `oven-sh/setup-bun@v1` |
| `docs-deploy.yml` | 200 | pinned-to-tag | `actions/download-artifact@v4` |
| `docs-deploy.yml` | 228 | pinned-to-tag | `actions/github-script@v7` |
| `docs-deploy.yml` | 262 | pinned-to-tag | `actions/checkout@v4` |
| `docs-deploy.yml` | 265 | pinned-to-tag | `oven-sh/setup-bun@v1` |
| `docs-deploy.yml` | 270 | pinned-to-tag | `actions/download-artifact@v4` |
| `docs-performance.yml` | 29 | pinned-to-tag | `actions/checkout@v4` |
| `docs-performance.yml` | 32 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `docs-performance.yml` | 61 | pinned-to-tag | `actions/upload-artifact@v4` |
| `docs-performance.yml` | 69 | pinned-to-tag | `actions/upload-artifact@v4` |
| `docs-performance.yml` | 77 | pinned-to-tag | `actions/github-script@v7` |
| `docs-performance.yml` | 121 | pinned-to-tag | `actions/checkout@v4` |
| `docs-performance.yml` | 124 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `docs-performance.yml` | 155 | pinned-to-tag | `actions/upload-artifact@v4` |
| `go-tests.yml` | 36 | pinned-to-tag | `actions/checkout@v4` |
| `go-tests.yml` | 39 | pinned-to-tag | `actions/setup-go@v5` |
| `go-tests.yml` | 45 | pinned-to-tag | `actions/cache@v3` |
| `go-tests.yml` | 78 | pinned-to-tag | `codecov/codecov-action@v4` |
| `go-tests.yml` | 87 | pinned-to-tag | `actions/upload-artifact@v4` |
| `go-tests.yml` | 139 | pinned-to-tag | `actions/checkout@v4` |
| `go-tests.yml` | 142 | pinned-to-tag | `actions/setup-go@v5` |
| `go-tests.yml` | 148 | pinned-to-tag | `actions/cache@v3` |
| `go-tests.yml` | 203 | pinned-to-tag | `codecov/codecov-action@v4` |
| `go-tests.yml` | 212 | pinned-to-tag | `actions/upload-artifact@v4` |
| `go-tests.yml` | 243 | pinned-to-tag | `actions/checkout@v4` |
| `go-tests.yml` | 246 | pinned-to-tag | `actions/setup-go@v5` |
| `go-tests.yml` | 252 | pinned-to-tag | `actions/cache@v3` |
| `go-tests.yml` | 304 | pinned-to-tag | `codecov/codecov-action@v4` |
| `go-tests.yml` | 313 | pinned-to-tag | `actions/upload-artifact@v4` |
| `go-tests.yml` | 329 | pinned-to-tag | `actions/checkout@v4` |
| `go-tests.yml` | 332 | pinned-to-tag | `actions/setup-go@v5` |
| `go-tests.yml` | 338 | pinned-to-tag | `docker/setup-buildx-action@v3` |
| `go-tests.yml` | 404 | pinned-to-tag | `codecov/codecov-action@v4` |
| `go-tests.yml` | 413 | pinned-to-tag | `actions/upload-artifact@v4` |
| `go-tests.yml` | 429 | pinned-to-tag | `actions/checkout@v4` |
| `go-tests.yml` | 432 | pinned-to-tag | `actions/setup-go@v5` |
| `go-tests.yml` | 438 | pinned-to-tag | `actions/cache@v3` |
| `go-tests.yml` | 466 | pinned-to-tag | `codecov/codecov-action@v4` |
| `go-tests.yml` | 475 | pinned-to-tag | `actions/upload-artifact@v4` |
| `go-tests.yml` | 492 | pinned-to-tag | `actions/checkout@v4` |
| `go-tests.yml` | 495 | pinned-to-tag | `actions/setup-go@v5` |
| `go-tests.yml` | 500 | pinned-to-tag | `actions/download-artifact@v4` |
| `go-tests.yml` | 516 | pinned-to-tag | `codecov/codecov-action@v4` |
| `go-tests.yml` | 540 | pinned-to-tag | `actions/upload-artifact@v4` |
| `load-test.yml` | 23 | pinned-to-tag | `actions/checkout@v4` |
| `load-test.yml` | 28 | pinned-to-tag | `grafana/setup-k6-action@v1` |
| `load-test.yml` | 181 | pinned-to-tag | `actions/upload-artifact@v4` |
| `load-test.yml` | 189 | pinned-to-tag | `actions/github-script@v7` |
| `load-test.yml` | 226 | pinned-to-tag | `actions/upload-artifact@v4` |
| `naming-guard.yml` | 45 | pinned-to-tag | `actions/checkout@v3` |
| `openapi-docs.yml` | 33 | pinned-to-tag | `actions/checkout@v4` |
| `openapi-docs.yml` | 36 | pinned-to-tag | `actions/setup-go@v5` |
| `openapi-docs.yml` | 105 | pinned-to-tag | `actions/upload-artifact@v4` |
| `openapi-docs.yml` | 116 | pinned-to-tag | `actions/github-script@v7` |
| `openapi-docs.yml` | 139 | pinned-to-tag | `actions/checkout@v4` |
| `openapi-docs.yml` | 146 | pinned-to-tag | `actions/download-artifact@v4` |
| `openapi-docs.yml` | 184 | pinned-to-tag | `actions/checkout@v4` |
| `openapi-docs.yml` | 187 | pinned-to-tag | `actions/download-artifact@v4` |
| `openapi-docs.yml` | 204 | pinned-to-tag | `actions/upload-artifact@v4` |
| `performance-regression.yml` | 66 | pinned-to-tag | `actions/checkout@v4` |
| `performance-regression.yml` | 145 | pinned-to-tag | `actions/checkout@v4` |
| `performance-regression.yml` | 148 | pinned-to-tag | `actions/setup-python@v5` |
| `performance-regression.yml` | 154 | pinned-to-tag | `actions/setup-go@v5` |
| `performance-regression.yml` | 243 | pinned-to-tag | `actions/upload-artifact@v4` |
| `performance-regression.yml` | 316 | pinned-to-tag | `actions/checkout@v4` |
| `performance-regression.yml` | 319 | pinned-to-tag | `actions/setup-python@v5` |
| `performance-regression.yml` | 325 | pinned-to-tag | `actions/setup-go@v5` |
| `performance-regression.yml` | 404 | pinned-to-tag | `actions/upload-artifact@v4` |
| `performance-regression.yml` | 431 | pinned-to-tag | `actions/checkout@v4` |
| `performance-regression.yml` | 435 | pinned-to-tag | `actions/download-artifact@v4` |
| `performance-regression.yml` | 442 | pinned-to-tag | `actions/download-artifact@v4` |
| `performance-regression.yml` | 448 | pinned-to-tag | `actions/setup-python@v5` |
| `performance-regression.yml` | 464 | pinned-to-tag | `actions/upload-artifact@v4` |
| `performance-regression.yml` | 471 | pinned-to-tag | `actions/github-script@v7` |
| `policy-gate.yml` | 17 | pinned-to-tag | `actions/checkout@v4` |
| `pre-commit.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |
| `pre-commit.yml` | 21 | pinned-to-tag | `actions/setup-python@v5` |
| `pre-commit.yml` | 46 | pinned-to-tag | `actions/upload-artifact@v4` |
| `qa-governance.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `quality.yml` | 20 | pinned-to-tag | `actions/checkout@v4` |
| `quality.yml` | 25 | pinned-to-tag | `astral-sh/setup-uv@v2` |
| `quality.yml` | 30 | pinned-to-tag | `actions/setup-python@v5` |
| `quality.yml` | 35 | pinned-to-tag | `actions/cache@v3` |
| `quality.yml` | 177 | pinned-to-tag | `actions/upload-artifact@v4` |
| `release-drafter.yml` | 14 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/release-drafter.yml@main` |
| `release.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 19 | pinned-to-tag | `astral-sh/setup-uv@v2` |
| `release.yml` | 24 | pinned-to-tag | `actions/setup-python@v5` |
| `release.yml` | 39 | pinned-to-tag | `softprops/action-gh-release@v1` |
| `release.yml` | 53 | pinned-to-tag | `actions/upload-artifact@v4` |
| `schema-validation.yml` | 52 | pinned-to-tag | `actions/checkout@v4` |
| `schema-validation.yml` | 55 | pinned-to-tag | `actions/setup-go@v5` |
| `schema-validation.yml` | 100 | pinned-to-tag | `actions/upload-artifact@v4` |
| `schema-validation.yml` | 113 | pinned-to-tag | `actions/checkout@v4` |
| `schema-validation.yml` | 116 | pinned-to-tag | `actions/setup-go@v5` |
| `schema-validation.yml` | 173 | pinned-to-tag | `actions/checkout@v4` |
| `schema-validation.yml` | 258 | pinned-to-tag | `actions/checkout@v4` |
| `schema-validation.yml` | 319 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 28 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 34 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 40 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `secret-scanning.yml` | 15 | pinned-to-tag | `actions/checkout@v4` |
| `security-guard.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `security-guard.yml` | 23 | pinned-to-tag | `pre-commit/action@v3.0.1` |
| `security-scans.yml` | 23 | pinned-to-tag | `actions/checkout@v4` |
| `security-scans.yml` | 49 | pinned-to-tag | `actions/upload-artifact@v4` |
| `security-scans.yml` | 99 | pinned-to-tag | `actions/checkout@v4` |
| `security-scans.yml` | 102 | pinned-to-tag | `github/codeql-action/init@v3` |
| `security-scans.yml` | 107 | pinned-to-tag | `github/codeql-action/analyze@v3` |
| `security-scans.yml` | 117 | pinned-to-tag | `actions/dependency-review-action@v4` |
| `test-pyramid.yml` | 21 | pinned-to-tag | `actions/checkout@v4` |
| `test-pyramid.yml` | 24 | pinned-to-tag | `actions/setup-go@v5` |
| `test-pyramid.yml` | 29 | pinned-to-tag | `actions/setup-node@v4` |
| `test-pyramid.yml` | 34 | pinned-to-tag | `actions/setup-python@v5` |
| `test-pyramid.yml` | 56 | pinned-to-tag | `actions/github-script@v7` |
| `test-validation.yml` | 31 | pinned-to-tag | `actions/checkout@v4` |
| `test-validation.yml` | 32 | pinned-to-tag | `actions/setup-node@v4` |
| `test-validation.yml` | 37 | pinned-to-tag | `actions/setup-go@v5` |
| `test-validation.yml` | 54 | pinned-to-tag | `actions/checkout@v4` |
| `test-validation.yml` | 55 | pinned-to-tag | `actions/setup-node@v4` |
| `test-validation.yml` | 62 | pinned-to-tag | `oven-sh/setup-bun@v1` |
| `test-validation.yml` | 83 | pinned-to-tag | `actions/upload-artifact@v4` |
| `test-validation.yml` | 94 | pinned-to-tag | `actions/checkout@v4` |
| `test-validation.yml` | 95 | pinned-to-tag | `actions/setup-node@v4` |
| `test-validation.yml` | 102 | pinned-to-tag | `oven-sh/setup-bun@v1` |
| `test-validation.yml` | 118 | pinned-to-tag | `actions/upload-artifact@v4` |
| `test-validation.yml` | 129 | pinned-to-tag | `actions/checkout@v4` |
| `test-validation.yml` | 130 | pinned-to-tag | `actions/setup-go@v5` |
| `test-validation.yml` | 147 | pinned-to-tag | `actions/upload-artifact@v4` |
| `test-validation.yml` | 160 | pinned-to-tag | `actions/checkout@v4` |
| `test-validation.yml` | 161 | pinned-to-tag | `actions/setup-python@v5` |
| `test-validation.yml` | 167 | pinned-to-tag | `astral-sh/setup-uv@v2` |
| `test-validation.yml` | 183 | pinned-to-tag | `actions/upload-artifact@v4` |
| `test-validation.yml` | 201 | pinned-to-tag | `actions/checkout@v4` |
| `test-validation.yml` | 204 | pinned-to-tag | `actions/download-artifact@v4` |
| `test-validation.yml` | 243 | pinned-to-tag | `actions/github-script@v7` |
| `test-validation.yml` | 257 | pinned-to-tag | `actions/upload-artifact@v4` |
| `test.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `test.yml` | 70 | pinned-to-tag | `actions/checkout@v4` |
| `test.yml` | 73 | pinned-to-tag | `actions/setup-go@v5` |
| `test.yml` | 93 | pinned-to-tag | `codecov/codecov-action@v4` |
| `test.yml` | 108 | pinned-to-tag | `actions/checkout@v4` |
| `test.yml` | 123 | pinned-to-tag | `actions/setup-python@v5` |
| `test.yml` | 142 | pinned-to-tag | `codecov/codecov-action@v4` |
| `test.yml` | 154 | pinned-to-tag | `actions/checkout@v4` |
| `test.yml` | 157 | pinned-to-tag | `oven-sh/setup-bun@v1` |
| `test.yml` | 170 | pinned-to-tag | `codecov/codecov-action@v4` |
| `test.yml` | 182 | pinned-to-tag | `actions/checkout@v4` |
| `test.yml` | 185 | pinned-to-tag | `docker/setup-buildx-action@v3` |
| `tests.yml` | 53 | pinned-to-tag | `actions/checkout@v4` |
| `tests.yml` | 80 | pinned-to-tag | `astral-sh/setup-uv@v2` |
| `tests.yml` | 86 | pinned-to-tag | `actions/setup-python@v5` |
| `tests.yml` | 92 | pinned-to-tag | `actions/cache@v3` |
| `tests.yml` | 152 | pinned-to-tag | `codecov/codecov-action@v3` |
| `tests.yml` | 161 | pinned-to-tag | `actions/upload-artifact@v4` |
| `tests.yml` | 202 | pinned-to-tag | `actions/checkout@v4` |
| `tests.yml` | 229 | pinned-to-tag | `astral-sh/setup-uv@v2` |
| `tests.yml` | 235 | pinned-to-tag | `actions/setup-python@v5` |
| `tests.yml` | 241 | pinned-to-tag | `actions/cache@v3` |
| `tests.yml` | 304 | pinned-to-tag | `codecov/codecov-action@v3` |
| `tests.yml` | 313 | pinned-to-tag | `actions/upload-artifact@v4` |
| `vitepress-pages.yml` | 25 | pinned-to-tag | `actions/checkout@v4` |
| `vitepress-pages.yml` | 28 | pinned-to-tag | `actions/setup-node@v4` |
| `vitepress-pages.yml` | 35 | pinned-to-tag | `actions/configure-pages@v5` |
| `vitepress-pages.yml` | 48 | pinned-to-tag | `actions/upload-pages-artifact@v3` |
| `vitepress-pages.yml` | 61 | pinned-to-tag | `actions/deploy-pages@v4` |

### heliosCLI (210 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `alert-sync-issues.yml` | 12 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/alert-sync-issues.yml@main` |
| `bazel.yml` | 54 | pinned-to-tag | `actions/checkout@v6` |
| `bazel.yml` | 57 | pinned-to-tag | `actions/setup-node@v6` |
| `bazel.yml` | 64 | pinned-to-tag | `facebook/install-dotslash@v2` |
| `bazel.yml` | 77 | pinned-to-tag | `bazelbuild/setup-bazelisk@v3` |
| `cargo-deny.yml` | 20 | pinned-to-tag | `actions/checkout@v6` |
| `cargo-deny.yml` | 23 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `cargo-deny.yml` | 26 | pinned-to-tag | `EmbarkStudios/cargo-deny-action@v2` |
| `ci.yml` | 17 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 20 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `ci.yml` | 25 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 46 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 49 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `cla.yml` | 21 | pinned-to-tag | `contributor-assistant/github-action@v2.6.1` |
| `close-stale-contributor-prs.yml` | 20 | pinned-to-tag | `actions/github-script@v8` |
| `codespell.yml` | 21 | pinned-to-tag | `actions/checkout@v6` |
| `cpu-profiling.yml` | 13 | pinned-to-tag | `actions/checkout@v4` |
| `cpu-profiling.yml` | 16 | pinned-to-tag | `actions/setup-python@v5` |
| `cpu-profiling.yml` | 64 | pinned-to-tag | `actions/checkout@v4` |
| `cpu-profiling.yml` | 67 | pinned-to-tag | `actions/setup-python@v5` |
| `cpu-profiling.yml` | 100 | pinned-to-tag | `actions/checkout@v4` |
| `cpu-profiling.yml` | 103 | pinned-to-tag | `actions/setup-python@v5` |
| `docs-site.yml` | 13 | pinned-to-tag | `actions/checkout@v4` |
| `docs-site.yml` | 14 | pinned-to-tag | `actions/setup-node@v4` |
| `fuzzing.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `fuzzing.yml` | 20 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `helios-cli-release.yml` | 36 | pinned-to-tag | `actions/checkout@v4` |
| `helios-cli-release.yml` | 39 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `helios-cli-release.yml` | 42 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `helios-cli-release.yml` | 67 | pinned-to-tag | `actions/upload-artifact@v4` |
| `helios-cli-release.yml` | 78 | pinned-to-tag | `actions/checkout@v4` |
| `helios-cli-release.yml` | 79 | pinned-to-tag | `actions/download-artifact@v4` |
| `helios-cli.yml` | 31 | pinned-to-tag | `actions/checkout@v4` |
| `helios-cli.yml` | 32 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `helios-cli.yml` | 35 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `helios-cli.yml` | 42 | pinned-to-tag | `actions/checkout@v4` |
| `helios-cli.yml` | 43 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `helios-cli.yml` | 46 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `helios-cli.yml` | 53 | pinned-to-tag | `actions/checkout@v4` |
| `helios-cli.yml` | 54 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `helios-cli.yml` | 55 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `helios-cli.yml` | 62 | pinned-to-tag | `actions/checkout@v4` |
| `helios-cli.yml` | 63 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `helios-cli.yml` | 64 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `iac-scan.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `iac-scan.yml` | 31 | pinned-to-tag | `actions/checkout@v4` |
| `issue-deduplicator.yml` | 23 | pinned-to-tag | `actions/checkout@v6` |
| `issue-deduplicator.yml` | 303 | pinned-to-tag | `actions/github-script@v8` |
| `issue-labeler.yml` | 23 | pinned-to-tag | `actions/checkout@v6` |
| `leak-detection.yml` | 13 | pinned-to-tag | `actions/checkout@v4` |
| `leak-detection.yml` | 16 | pinned-to-tag | `actions/setup-python@v5` |
| `leak-detection.yml` | 60 | pinned-to-tag | `actions/checkout@v4` |
| `leak-detection.yml` | 63 | pinned-to-tag | `actions/setup-python@v5` |
| `leak-detection.yml` | 106 | pinned-to-tag | `actions/checkout@v4` |
| `leak-detection.yml` | 109 | pinned-to-tag | `actions/setup-python@v5` |
| `license-compliance.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `license-compliance.yml` | 29 | pinned-to-tag | `actions/checkout@v4` |
| `network-optimization.yml` | 13 | pinned-to-tag | `actions/checkout@v4` |
| `network-optimization.yml` | 16 | pinned-to-tag | `actions/setup-python@v5` |
| `network-optimization.yml` | 54 | pinned-to-tag | `actions/checkout@v4` |
| `network-optimization.yml` | 57 | pinned-to-tag | `actions/setup-python@v5` |
| `network-optimization.yml` | 95 | pinned-to-tag | `actions/checkout@v4` |
| `network-optimization.yml` | 98 | pinned-to-tag | `actions/setup-python@v5` |
| `pages.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `pages.yml` | 20 | pinned-to-tag | `actions/setup-node@v4` |
| `pages.yml` | 25 | pinned-to-tag | `actions/configure-pages@v5` |
| `pages.yml` | 32 | pinned-to-tag | `actions/upload-pages-artifact@v3` |
| `pages.yml` | 44 | pinned-to-tag | `actions/deploy-pages@v4` |
| `policy-gate.yml` | 17 | pinned-to-tag | `actions/checkout@v4` |
| `pr-babysit-watch.yml` | 30 | pinned-to-tag | `actions/checkout@v4` |
| `quality.yml` | 13 | pinned-to-tag | `actions/checkout@v4` |
| `quality.yml` | 14 | pinned-to-tag | `actions/setup-node@v4` |
| `rust-ci.yml` | 32 | pinned-to-tag | `actions/checkout@v6` |
| `rust-ci.yml` | 108 | pinned-to-tag | `actions/checkout@v6` |
| `rust-ci.yml` | 109 | unpinned-other-ref | `dtolnay/rust-toolchain@1.93.0` |
| `rust-ci.yml` | 158 | pinned-to-tag | `actions/checkout@v6` |
| `rust-ci.yml` | 159 | unpinned-other-ref | `dtolnay/rust-toolchain@1.93.0` |
| `rust-ci.yml` | 174 | pinned-to-tag | `actions/checkout@v6` |
| `rust-ci.yml` | 175 | unpinned-other-ref | `dtolnay/rust-toolchain@1.93.0` |
| `rust-ci.yml` | 232 | pinned-to-tag | `actions/checkout@v6` |
| `rust-ci.yml` | 246 | unpinned-other-ref | `dtolnay/rust-toolchain@1.93.0` |
| `rust-ci.yml` | 275 | pinned-to-tag | `actions/cache/restore@v5` |
| `rust-ci.yml` | 320 | pinned-to-tag | `actions/cache/restore@v5` |
| `rust-ci.yml` | 347 | pinned-to-tag | `actions/cache/restore@v5` |
| `rust-ci.yml` | 355 | pinned-to-tag | `mlugg/setup-zig@v2` |
| `rust-ci.yml` | 442 | pinned-to-tag | `actions/upload-artifact@v6` |
| `rust-ci.yml` | 453 | pinned-to-tag | `actions/cache/save@v5` |
| `rust-ci.yml` | 469 | pinned-to-tag | `actions/cache/save@v5` |
| `rust-ci.yml` | 494 | pinned-to-tag | `actions/cache/save@v5` |
| `rust-ci.yml` | 530 | pinned-to-tag | `actions/checkout@v6` |
| `rust-ci.yml` | 532 | pinned-to-tag | `actions/setup-node@v6` |
| `rust-ci.yml` | 547 | pinned-to-tag | `facebook/install-dotslash@v2` |
| `rust-ci.yml` | 548 | unpinned-other-ref | `dtolnay/rust-toolchain@1.93.0` |
| `rust-ci.yml` | 564 | pinned-to-tag | `actions/cache/restore@v5` |
| `rust-ci.yml` | 604 | pinned-to-tag | `actions/cache/restore@v5` |
| `rust-ci.yml` | 637 | pinned-to-tag | `actions/upload-artifact@v6` |
| `rust-ci.yml` | 646 | pinned-to-tag | `actions/cache/save@v5` |
| `rust-ci.yml` | 658 | pinned-to-tag | `actions/cache/save@v5` |
| `rust-release-prepare.yml` | 21 | pinned-to-tag | `actions/checkout@v6` |
| `rust-release-prepare.yml` | 46 | pinned-to-tag | `peter-evans/create-pull-request@v8` |
| `rust-release-windows.yml` | 70 | pinned-to-tag | `actions/checkout@v6` |
| `rust-release-windows.yml` | 85 | unpinned-other-ref | `dtolnay/rust-toolchain@1.93.0` |
| `rust-release-windows.yml` | 95 | pinned-to-tag | `actions/upload-artifact@v6` |
| `rust-release-windows.yml` | 115 | pinned-to-tag | `actions/upload-artifact@v6` |
| `rust-release-windows.yml` | 150 | pinned-to-tag | `actions/checkout@v6` |
| `rust-release-windows.yml` | 153 | pinned-to-tag | `actions/download-artifact@v7` |
| `rust-release-windows.yml` | 159 | pinned-to-tag | `actions/download-artifact@v7` |
| `rust-release-windows.yml` | 196 | pinned-to-tag | `facebook/install-dotslash@v2` |
| `rust-release-windows.yml` | 259 | pinned-to-tag | `actions/upload-artifact@v6` |
| `rust-release.yml` | 22 | pinned-to-tag | `actions/checkout@v6` |
| `rust-release.yml` | 23 | unpinned-other-ref | `dtolnay/rust-toolchain@1.92` |
| `rust-release.yml` | 80 | pinned-to-tag | `actions/checkout@v6` |
| `rust-release.yml` | 126 | unpinned-other-ref | `dtolnay/rust-toolchain@1.93.0` |
| `rust-release.yml` | 143 | pinned-to-tag | `mlugg/setup-zig@v2` |
| `rust-release.yml` | 217 | pinned-to-tag | `actions/upload-artifact@v6` |
| `rust-release.yml` | 355 | pinned-to-tag | `actions/upload-artifact@v6` |
| `rust-release.yml` | 398 | pinned-to-tag | `actions/checkout@v6` |
| `rust-release.yml` | 419 | pinned-to-tag | `actions/download-artifact@v7` |
| `rust-release.yml` | 473 | pinned-to-tag | `pnpm/action-setup@v4` |
| `rust-release.yml` | 478 | pinned-to-tag | `actions/setup-node@v6` |
| `rust-release.yml` | 486 | pinned-to-tag | `facebook/install-dotslash@v2` |
| `rust-release.yml` | 502 | pinned-to-tag | `softprops/action-gh-release@v2` |
| `rust-release.yml` | 511 | pinned-to-tag | `facebook/dotslash-publish-release@v2` |
| `rust-release.yml` | 547 | pinned-to-tag | `actions/setup-node@v6` |
| `sast-full.yml` | 21 | pinned-to-tag | `actions/checkout@v4` |
| `sast-full.yml` | 24 | pinned-to-tag | `github/codeql-action/init@v3` |
| `sast-full.yml` | 29 | pinned-to-tag | `github/codeql-action/analyze@v3` |
| `sast-full.yml` | 35 | pinned-to-tag | `actions/checkout@v4` |
| `sast-full.yml` | 54 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `sast-full.yml` | 65 | pinned-to-tag | `actions/checkout@v4` |
| `sast-full.yml` | 66 | pinned-to-tag | `returntocorp/semgrep-action@v1` |
| `sast-full.yml` | 86 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `sast-full.yml` | 96 | pinned-to-tag | `actions/checkout@v4` |
| `sast-quick.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `sast-quick.yml` | 20 | pinned-to-tag | `returntocorp/semgrep-action@v1` |
| `sast-quick.yml` | 40 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `sast-quick.yml` | 51 | pinned-to-tag | `actions/checkout@v4` |
| `sast-quick.yml` | 65 | pinned-to-tag | `actions/checkout@v4` |
| `sast-quick.yml` | 66 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `sast-quick.yml` | 69 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `sast-quick.yml` | 76 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `sdk.yml` | 17 | pinned-to-tag | `actions/checkout@v6` |
| `sdk.yml` | 27 | pinned-to-tag | `pnpm/action-setup@v4` |
| `sdk.yml` | 32 | pinned-to-tag | `actions/setup-node@v6` |
| `sdk.yml` | 36 | unpinned-other-ref | `dtolnay/rust-toolchain@1.93.0` |
| `security-guard-hook-audit.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `security-guard.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `security-guard.yml` | 23 | pinned-to-tag | `pre-commit/action@v3.0.1` |
| `sentry-error-tracking.yml` | 41 | pinned-to-tag | `actions/checkout@v4` |
| `sentry-error-tracking.yml` | 46 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `sentry-error-tracking.yml` | 51 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `sentry-error-tracking.yml` | 92 | pinned-to-tag | `actions/checkout@v4` |
| `sentry-error-tracking.yml` | 127 | pinned-to-tag | `actions/github-script@v7` |
| `shell-tool-mcp-ci.yml` | 28 | pinned-to-tag | `actions/checkout@v6` |
| `shell-tool-mcp-ci.yml` | 31 | pinned-to-tag | `pnpm/action-setup@v4` |
| `shell-tool-mcp-ci.yml` | 36 | pinned-to-tag | `actions/setup-node@v6` |
| `shell-tool-mcp.yml` | 145 | pinned-to-tag | `actions/checkout@v6` |
| `shell-tool-mcp.yml` | 163 | pinned-to-tag | `actions/upload-artifact@v6` |
| `shell-tool-mcp.yml` | 187 | pinned-to-tag | `actions/checkout@v6` |
| `shell-tool-mcp.yml` | 205 | pinned-to-tag | `actions/upload-artifact@v6` |
| `shell-tool-mcp.yml` | 285 | pinned-to-tag | `actions/checkout@v6` |
| `shell-tool-mcp.yml` | 331 | pinned-to-tag | `actions/upload-artifact@v6` |
| `shell-tool-mcp.yml` | 363 | pinned-to-tag | `actions/checkout@v6` |
| `shell-tool-mcp.yml` | 409 | pinned-to-tag | `actions/upload-artifact@v6` |
| `shell-tool-mcp.yml` | 429 | pinned-to-tag | `actions/checkout@v6` |
| `shell-tool-mcp.yml` | 432 | pinned-to-tag | `pnpm/action-setup@v4` |
| `shell-tool-mcp.yml` | 437 | pinned-to-tag | `actions/setup-node@v6` |
| `shell-tool-mcp.yml` | 448 | pinned-to-tag | `actions/download-artifact@v7` |
| `shell-tool-mcp.yml` | 506 | pinned-to-tag | `actions/upload-artifact@v6` |
| `shell-tool-mcp.yml` | 525 | pinned-to-tag | `actions/setup-node@v6` |
| `shell-tool-mcp.yml` | 536 | pinned-to-tag | `actions/download-artifact@v7` |
| `snyk-scan.yml` | 24 | pinned-to-tag | `actions/checkout@v4` |
| `snyk-scan.yml` | 29 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `snyk-scan.yml` | 51 | pinned-to-tag | `github/codeql-action/upload-sarif@v2` |
| `snyk-scan.yml` | 58 | pinned-to-tag | `actions/github-script@v7` |
| `snyk-scan.yml` | 80 | pinned-to-tag | `actions/checkout@v4` |
| `sonarcloud.yml` | 15 | pinned-to-tag | `actions/checkout@v4` |
| `sonarcloud.yml` | 17 | pinned-to-tag | `actions/setup-java@v3` |
| `stage-gates.yml` | 25 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 98 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 117 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 128 | pinned-to-tag | `golangci/golangci-lint-action@v4` |
| `stage-gates.yml` | 141 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 156 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 180 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 204 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 246 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 265 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 284 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 295 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 309 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 323 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 337 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 351 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 364 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 382 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 384 | pinned-to-tag | `anchore/sbom-action@v0` |
| `stage-gates.yml` | 393 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 404 | pinned-to-tag | `actions/upload-artifact@v4` |
| `stage-gates.yml` | 414 | pinned-to-tag | `actions/checkout@v4` |
| `trivy-scan.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `trivy-scan.yml` | 28 | pinned-to-tag | `github/codeql-action/upload-sarif@v2` |
| `workflow-maintenance.yml` | 20 | pinned-to-tag | `actions/checkout@v4` |
| `workflow-maintenance.yml` | 45 | pinned-to-tag | `actions/checkout@v4` |
| `workflow-sync.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `zap-dast.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |

### PhenoLang (180 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ai-testing-orchestration.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `ai-testing-orchestration.yml` | 34 | pinned-to-tag | `actions/checkout@v4` |
| `ai-testing-orchestration.yml` | 40 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `ai-testing-orchestration.yml` | 58 | pinned-to-tag | `actions/checkout@v4` |
| `ai-testing-orchestration.yml` | 64 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `ai-testing-orchestration.yml` | 81 | pinned-to-tag | `actions/checkout@v4` |
| `ai-testing-orchestration.yml` | 87 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `ai-testing-orchestration.yml` | 90 | pinned-to-tag | `astral-sh/setup-uv@v4` |
| `audit.yml` | 19 | pinned-to-tag | `actions/checkout@v6` |
| `audit.yml` | 22 | pinned-to-tag | `jdx/mise-action@v4` |
| `audit.yml` | 32 | pinned-to-tag | `actions/upload-artifact@v4` |
| `benchmark.yml` | 28 | pinned-to-tag | `actions/checkout@v6` |
| `benchmark.yml` | 29 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `benchmark.yml` | 30 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `benchmark.yml` | 33 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `benchmark.yml` | 51 | pinned-to-tag | `benchmark-action/github-action-benchmark@v1` |
| `changelog.yml` | 19 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 32 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 35 | pinned-to-tag | `bufbuild/buf-action@v1` |
| `ci.yml` | 47 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 48 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `ci.yml` | 51 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 54 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 71 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 72 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `ci.yml` | 73 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 76 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 87 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 88 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `ci.yml` | 89 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 92 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 107 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 108 | pinned-to-tag | `rustsec/audit-check@v2.0.0` |
| `ci.yml` | 121 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 122 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `ci.yml` | 123 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 126 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 137 | pinned-to-tag | `crate-ci/typos@v1` |
| `ci.yml` | 144 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 145 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `ci.yml` | 146 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 149 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 158 | pinned-to-tag | `codecov/codecov-action@v4` |
| `ci.yml` | 172 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 173 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `ci.yml` | 176 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 177 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 194 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 195 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `ci.yml` | 196 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 197 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 208 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 209 | unpinned-other-ref | `dtolnay/rust-toolchain@1.86.0` |
| `ci.yml` | 210 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 211 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 222 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 223 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `ci.yml` | 224 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 225 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 236 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 254 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 255 | pinned-to-tag | `actions/setup-python@v5` |
| `ci.yml` | 273 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 274 | pinned-to-tag | `actions/setup-python@v5` |
| `ci.yml` | 287 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 293 | pinned-to-tag | `reviewdog/action-actionlint@v1` |
| `ci.yml` | 301 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 304 | pinned-to-tag | `wagoid/commitlint-github-action@v6` |
| `codeql.yml` | 23 | pinned-to-tag | `actions/checkout@v4` |
| `codeql.yml` | 24 | pinned-to-tag | `github/codeql-action/init@v3` |
| `codeql.yml` | 27 | pinned-to-tag | `github/codeql-action/autobuild@v3` |
| `codeql.yml` | 28 | pinned-to-tag | `github/codeql-action/analyze@v3` |
| `deploy-docs.yml` | 12 | pinned-to-tag | `actions/checkout@v4` |
| `deploy-docs.yml` | 14 | pinned-to-tag | `actions/setup-node@v4` |
| `deploy-docs.yml` | 19 | pinned-to-tag | `peaceiris/actions-gh-pages@v4` |
| `deploy.yml` | 25 | pinned-to-tag | `actions/checkout@v4` |
| `deploy.yml` | 28 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `deploy.yml` | 31 | pinned-to-tag | `actions/configure-pages@v5` |
| `deploy.yml` | 44 | pinned-to-tag | `actions/upload-pages-artifact@v4` |
| `deploy.yml` | 57 | pinned-to-tag | `actions/deploy-pages@v4` |
| `docs.yml` | 30 | pinned-to-tag | `actions/checkout@v4` |
| `docs.yml` | 31 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `evidence-capture.yml` | 27 | pinned-to-tag | `actions/checkout@v4` |
| `evidence-capture.yml` | 30 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `evidence-capture.yml` | 35 | pinned-to-tag | `actions/cache@v4` |
| `evidence-capture.yml` | 107 | pinned-to-tag | `actions/upload-artifact@v4` |
| `fuzzing.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `fuzzing.yml` | 20 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `gate-check.yml` | 29 | pinned-to-tag | `actions/checkout@v6` |
| `gate-check.yml` | 32 | pinned-to-tag | `jdx/mise-action@v4` |
| `iac-scan.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `iac-scan.yml` | 31 | pinned-to-tag | `actions/checkout@v4` |
| `libs-activation-ci.yml` | 17 | pinned-to-tag | `actions/checkout@v4` |
| `libs-activation-ci.yml` | 18 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `license-compliance.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `license-compliance.yml` | 29 | pinned-to-tag | `actions/checkout@v4` |
| `policy-gate.yml` | 17 | pinned-to-tag | `actions/checkout@v6` |
| `publish.yml` | 35 | pinned-to-tag | `actions/checkout@v6` |
| `publish.yml` | 38 | pinned-to-tag | `jdx/mise-action@v4` |
| `quality-gate.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |
| `release-drafter.yml` | 15 | pinned-to-tag | `release-drafter/release-drafter@v6` |
| `release.yml` | 39 | pinned-to-tag | `actions/checkout@v6` |
| `release.yml` | 40 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `release.yml` | 41 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `release.yml` | 42 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `release.yml` | 62 | pinned-to-tag | `actions/upload-artifact@v4` |
| `release.yml` | 155 | pinned-to-tag | `actions/checkout@v6` |
| `release.yml` | 156 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `release.yml` | 160 | pinned-to-tag | `taiki-e/install-action@v2` |
| `release.yml` | 168 | pinned-to-tag | `actions/upload-artifact@v4` |
| `release.yml` | 180 | pinned-to-tag | `actions/checkout@v6` |
| `release.yml` | 201 | pinned-to-tag | `actions/upload-artifact@v4` |
| `release.yml` | 224 | pinned-to-tag | `actions/checkout@v6` |
| `release.yml` | 228 | pinned-to-tag | `actions/download-artifact@v4` |
| `release.yml` | 259 | pinned-to-tag | `ncipollo/release-action@v1` |
| `sast-full.yml` | 21 | pinned-to-tag | `actions/checkout@v4` |
| `sast-full.yml` | 24 | pinned-to-tag | `github/codeql-action/init@v3` |
| `sast-full.yml` | 29 | pinned-to-tag | `github/codeql-action/analyze@v3` |
| `sast-full.yml` | 35 | pinned-to-tag | `actions/checkout@v4` |
| `sast-full.yml` | 45 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `sast-full.yml` | 56 | pinned-to-tag | `actions/checkout@v4` |
| `sast-full.yml` | 57 | pinned-to-tag | `returntocorp/semgrep-action@v1` |
| `sast-full.yml` | 68 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `sast-full.yml` | 78 | pinned-to-tag | `actions/checkout@v4` |
| `sast-quick.yml` | 23 | pinned-to-tag | `actions/checkout@v4` |
| `sast-quick.yml` | 24 | pinned-to-tag | `returntocorp/semgrep-action@v1` |
| `sast-quick.yml` | 35 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `sast-quick.yml` | 46 | pinned-to-tag | `actions/checkout@v4` |
| `sast-quick.yml` | 65 | pinned-to-tag | `actions/checkout@v4` |
| `sast-quick.yml` | 66 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `sast-quick.yml` | 69 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `sast-quick.yml` | 79 | pinned-to-tag | `actions/checkout@v4` |
| `sast-quick.yml` | 80 | pinned-to-tag | `licensefinder/license_finder_action@v2` |
| `sbom.yml` | 28 | pinned-to-tag | `actions/checkout@v4` |
| `sbom.yml` | 31 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `sbom.yml` | 34 | pinned-to-tag | `taiki-e/install-action@v2` |
| `sbom.yml` | 42 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 27 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 30 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 36 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 42 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `security-guard.yml` | 18 | pinned-to-tag | `actions/checkout@v6` |
| `security-guard.yml` | 23 | pinned-to-tag | `pre-commit/action@v3.0.1` |
| `security.yml` | 31 | pinned-to-tag | `actions/checkout@v6` |
| `security.yml` | 32 | pinned-to-tag | `rustsec/audit-check@v2.0.0` |
| `security.yml` | 41 | pinned-to-tag | `actions/checkout@v6` |
| `security.yml` | 42 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `security.yml` | 57 | pinned-to-tag | `actions/checkout@v6` |
| `security.yml` | 77 | pinned-to-tag | `actions/checkout@v6` |
| `security.yml` | 78 | pinned-to-tag | `github/codeql-action/init@v3` |
| `security.yml` | 81 | pinned-to-tag | `github/codeql-action/analyze@v3` |
| `security.yml` | 88 | pinned-to-tag | `actions/checkout@v6` |
| `security.yml` | 89 | pinned-to-tag | `actions/setup-python@v5` |
| `security.yml` | 108 | pinned-to-tag | `actions/checkout@v6` |
| `security.yml` | 109 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `security.yml` | 126 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `snyk-scan.yml` | 49 | pinned-to-tag | `actions/checkout@v4` |
| `snyk-scan.yml` | 54 | pinned-to-tag | `actions/setup-node@v4` |
| `snyk-scan.yml` | 87 | pinned-to-tag | `github/codeql-action/upload-sarif@v2` |
| `snyk-scan.yml` | 105 | pinned-to-tag | `actions/github-script@v7` |
| `snyk-scan.yml` | 133 | pinned-to-tag | `actions/checkout@v4` |
| `snyk-scan.yml` | 138 | pinned-to-tag | `actions/setup-node@v4` |
| `snyk-scan.yml` | 168 | pinned-to-tag | `peter-evans/create-pull-request@v5` |
| `snyk-scan.yml` | 201 | pinned-to-tag | `actions/checkout@v4` |
| `snyk-scan.yml` | 213 | pinned-to-tag | `actions/upload-artifact@v3` |
| `sonarcloud.yml` | 15 | pinned-to-tag | `actions/checkout@v4` |
| `sonarcloud.yml` | 17 | pinned-to-tag | `actions/setup-java@v3` |
| `spec-validation.yml` | 23 | pinned-to-tag | `actions/checkout@v4` |
| `spec-validation.yml` | 28 | pinned-to-tag | `actions/setup-python@v4` |
| `spec-validation.yml` | 141 | pinned-to-tag | `actions/github-script@v6` |
| `sync-canary.yml` | 20 | pinned-to-tag | `actions/checkout@v6` |
| `tag-automation.yml` | 13 | pinned-to-tag | `actions/checkout@v4` |
| `traceability-gate.yml` | 16 | pinned-to-tag | `actions/checkout@v6` |
| `traceability-gate.yml` | 19 | pinned-to-tag | `actions/setup-python@v5` |
| `trivy-scan.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `trivy-scan.yml` | 28 | pinned-to-tag | `github/codeql-action/upload-sarif@v2` |
| `workflow-maintenance.yml` | 20 | pinned-to-tag | `actions/checkout@v4` |
| `workflow-maintenance.yml` | 45 | pinned-to-tag | `actions/checkout@v4` |
| `workflow-sync.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `zap-dast.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |

### HexaKit (176 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ai-testing-orchestration.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `ai-testing-orchestration.yml` | 34 | pinned-to-tag | `actions/checkout@v4` |
| `ai-testing-orchestration.yml` | 40 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `ai-testing-orchestration.yml` | 58 | pinned-to-tag | `actions/checkout@v4` |
| `ai-testing-orchestration.yml` | 64 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `ai-testing-orchestration.yml` | 81 | pinned-to-tag | `actions/checkout@v4` |
| `ai-testing-orchestration.yml` | 87 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `ai-testing-orchestration.yml` | 90 | pinned-to-tag | `astral-sh/setup-uv@v4` |
| `audit.yml` | 19 | pinned-to-tag | `actions/checkout@v6` |
| `audit.yml` | 22 | pinned-to-tag | `jdx/mise-action@v4` |
| `audit.yml` | 32 | pinned-to-tag | `actions/upload-artifact@v4` |
| `benchmark.yml` | 28 | pinned-to-tag | `actions/checkout@v6` |
| `benchmark.yml` | 29 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `benchmark.yml` | 30 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `benchmark.yml` | 33 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `benchmark.yml` | 51 | pinned-to-tag | `benchmark-action/github-action-benchmark@v1` |
| `changelog.yml` | 19 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 29 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 32 | pinned-to-tag | `bufbuild/buf-action@v1` |
| `ci.yml` | 44 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 45 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `ci.yml` | 48 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 51 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 68 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 69 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `ci.yml` | 70 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 73 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 84 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 85 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `ci.yml` | 86 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 89 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 104 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 105 | pinned-to-tag | `rustsec/audit-check@v2.0.0` |
| `ci.yml` | 118 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 119 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `ci.yml` | 120 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 123 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 134 | pinned-to-tag | `crate-ci/typos@v1` |
| `ci.yml` | 141 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 142 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `ci.yml` | 143 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 146 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 155 | pinned-to-tag | `codecov/codecov-action@v4` |
| `ci.yml` | 169 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 170 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `ci.yml` | 173 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 174 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 191 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 192 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `ci.yml` | 193 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 194 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 205 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 206 | unpinned-other-ref | `dtolnay/rust-toolchain@1.86.0` |
| `ci.yml` | 207 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 208 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 219 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 220 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `ci.yml` | 221 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 222 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 233 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 251 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 252 | pinned-to-tag | `actions/setup-python@v5` |
| `ci.yml` | 270 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 271 | pinned-to-tag | `actions/setup-python@v5` |
| `ci.yml` | 284 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 290 | pinned-to-tag | `reviewdog/action-actionlint@v1` |
| `ci.yml` | 298 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 301 | pinned-to-tag | `wagoid/commitlint-github-action@v6` |
| `deploy.yml` | 25 | pinned-to-tag | `actions/checkout@v4` |
| `deploy.yml` | 28 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `deploy.yml` | 31 | pinned-to-tag | `actions/configure-pages@v5` |
| `deploy.yml` | 44 | pinned-to-tag | `actions/upload-pages-artifact@v4` |
| `deploy.yml` | 61 | pinned-to-tag | `actions/deploy-pages@v4` |
| `docs.yml` | 30 | pinned-to-tag | `actions/checkout@v4` |
| `docs.yml` | 31 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `evidence-capture.yml` | 27 | pinned-to-tag | `actions/checkout@v4` |
| `evidence-capture.yml` | 30 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `evidence-capture.yml` | 35 | pinned-to-tag | `actions/cache@v4` |
| `evidence-capture.yml` | 107 | pinned-to-tag | `actions/upload-artifact@v4` |
| `fuzzing.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `fuzzing.yml` | 20 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `gate-check.yml` | 29 | pinned-to-tag | `actions/checkout@v6` |
| `gate-check.yml` | 32 | pinned-to-tag | `jdx/mise-action@v4` |
| `iac-scan.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `iac-scan.yml` | 31 | pinned-to-tag | `actions/checkout@v4` |
| `legacy-tooling-gate.yml` | 18 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/legacy-tooling-gate.yml@main` |
| `libs-activation-ci.yml` | 17 | pinned-to-tag | `actions/checkout@v4` |
| `libs-activation-ci.yml` | 18 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `license-compliance.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `license-compliance.yml` | 29 | pinned-to-tag | `actions/checkout@v4` |
| `policy-gate.yml` | 17 | pinned-to-tag | `actions/checkout@v6` |
| `publish.yml` | 35 | pinned-to-tag | `actions/checkout@v6` |
| `publish.yml` | 38 | pinned-to-tag | `jdx/mise-action@v4` |
| `quality-gate.yml` | 10 | pinned-to-tag | `actions/checkout@v4` |
| `release-drafter.yml` | 12 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/release-drafter.yml@main` |
| `release.yml` | 39 | pinned-to-tag | `actions/checkout@v6` |
| `release.yml` | 40 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `release.yml` | 41 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `release.yml` | 42 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `release.yml` | 62 | pinned-to-tag | `actions/upload-artifact@v4` |
| `release.yml` | 155 | pinned-to-tag | `actions/checkout@v6` |
| `release.yml` | 156 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `release.yml` | 160 | pinned-to-tag | `taiki-e/install-action@v2` |
| `release.yml` | 168 | pinned-to-tag | `actions/upload-artifact@v4` |
| `release.yml` | 180 | pinned-to-tag | `actions/checkout@v6` |
| `release.yml` | 201 | pinned-to-tag | `actions/upload-artifact@v4` |
| `release.yml` | 224 | pinned-to-tag | `actions/checkout@v6` |
| `release.yml` | 228 | pinned-to-tag | `actions/download-artifact@v4` |
| `release.yml` | 259 | pinned-to-tag | `ncipollo/release-action@v1` |
| `sast-full.yml` | 21 | pinned-to-tag | `actions/checkout@v4` |
| `sast-full.yml` | 24 | pinned-to-tag | `github/codeql-action/init@v3` |
| `sast-full.yml` | 29 | pinned-to-tag | `github/codeql-action/analyze@v3` |
| `sast-full.yml` | 35 | pinned-to-tag | `actions/checkout@v4` |
| `sast-full.yml` | 45 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `sast-full.yml` | 56 | pinned-to-tag | `actions/checkout@v4` |
| `sast-full.yml` | 57 | pinned-to-tag | `returntocorp/semgrep-action@v1` |
| `sast-full.yml` | 68 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `sast-full.yml` | 78 | pinned-to-tag | `actions/checkout@v4` |
| `sast-quick.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `sast-quick.yml` | 20 | pinned-to-tag | `returntocorp/semgrep-action@v1` |
| `sast-quick.yml` | 31 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `sast-quick.yml` | 42 | pinned-to-tag | `actions/checkout@v4` |
| `sast-quick.yml` | 56 | pinned-to-tag | `actions/checkout@v4` |
| `sast-quick.yml` | 57 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `sast-quick.yml` | 60 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `sast-quick.yml` | 67 | pinned-to-tag | `actions/checkout@v4` |
| `sast-quick.yml` | 68 | pinned-to-tag | `licensefinder/license_finder_action@v2` |
| `sbom.yml` | 23 | pinned-to-tag | `actions/checkout@v4` |
| `sbom.yml` | 26 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `sbom.yml` | 29 | pinned-to-tag | `taiki-e/install-action@v2` |
| `sbom.yml` | 37 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `security-guard.yml` | 18 | pinned-to-tag | `actions/checkout@v6` |
| `security-guard.yml` | 23 | pinned-to-tag | `pre-commit/action@v3.0.1` |
| `security.yml` | 31 | pinned-to-tag | `actions/checkout@v6` |
| `security.yml` | 32 | pinned-to-tag | `rustsec/audit-check@v2.0.0` |
| `security.yml` | 41 | pinned-to-tag | `actions/checkout@v6` |
| `security.yml` | 42 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `security.yml` | 57 | pinned-to-tag | `actions/checkout@v6` |
| `security.yml` | 60 | pinned-to-tag | `gitleaks/gitleaks-action@v2` |
| `security.yml` | 75 | pinned-to-tag | `actions/checkout@v6` |
| `security.yml` | 76 | pinned-to-tag | `github/codeql-action/init@v3` |
| `security.yml` | 79 | pinned-to-tag | `github/codeql-action/analyze@v3` |
| `security.yml` | 86 | pinned-to-tag | `actions/checkout@v6` |
| `security.yml` | 87 | pinned-to-tag | `actions/setup-python@v5` |
| `security.yml` | 106 | pinned-to-tag | `actions/checkout@v6` |
| `security.yml` | 107 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `security.yml` | 124 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `self-merge-gate.yml` | 13 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/self-merge-gate.yml@main` |
| `snyk-scan.yml` | 49 | pinned-to-tag | `actions/checkout@v4` |
| `snyk-scan.yml` | 54 | pinned-to-tag | `actions/setup-node@v4` |
| `snyk-scan.yml` | 87 | pinned-to-tag | `github/codeql-action/upload-sarif@v2` |
| `snyk-scan.yml` | 105 | pinned-to-tag | `actions/github-script@v7` |
| `snyk-scan.yml` | 133 | pinned-to-tag | `actions/checkout@v4` |
| `snyk-scan.yml` | 138 | pinned-to-tag | `actions/setup-node@v4` |
| `snyk-scan.yml` | 168 | pinned-to-tag | `peter-evans/create-pull-request@v5` |
| `snyk-scan.yml` | 201 | pinned-to-tag | `actions/checkout@v4` |
| `snyk-scan.yml` | 213 | pinned-to-tag | `actions/upload-artifact@v3` |
| `sonarcloud.yml` | 15 | pinned-to-tag | `actions/checkout@v4` |
| `sonarcloud.yml` | 17 | pinned-to-tag | `actions/setup-java@v3` |
| `spec-validation.yml` | 23 | pinned-to-tag | `actions/checkout@v4` |
| `spec-validation.yml` | 28 | pinned-to-tag | `actions/setup-python@v4` |
| `spec-validation.yml` | 141 | pinned-to-tag | `actions/github-script@v6` |
| `sync-canary.yml` | 20 | pinned-to-tag | `actions/checkout@v6` |
| `tag-automation.yml` | 16 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/tag-automation.yml@main` |
| `traceability-gate.yml` | 16 | pinned-to-tag | `actions/checkout@v6` |
| `traceability-gate.yml` | 19 | pinned-to-tag | `actions/setup-python@v5` |
| `trivy-scan.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `trivy-scan.yml` | 28 | pinned-to-tag | `github/codeql-action/upload-sarif@v2` |
| `workflow-maintenance.yml` | 20 | pinned-to-tag | `actions/checkout@v4` |
| `workflow-maintenance.yml` | 45 | pinned-to-tag | `actions/checkout@v4` |
| `workflow-sync.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `zap-dast.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |

### pheno (170 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ai-testing-orchestration.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `ai-testing-orchestration.yml` | 34 | pinned-to-tag | `actions/checkout@v4` |
| `ai-testing-orchestration.yml` | 40 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `ai-testing-orchestration.yml` | 58 | pinned-to-tag | `actions/checkout@v4` |
| `ai-testing-orchestration.yml` | 64 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `ai-testing-orchestration.yml` | 81 | pinned-to-tag | `actions/checkout@v4` |
| `ai-testing-orchestration.yml` | 87 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `ai-testing-orchestration.yml` | 90 | pinned-to-tag | `astral-sh/setup-uv@v4` |
| `audit.yml` | 19 | pinned-to-tag | `actions/checkout@v6` |
| `audit.yml` | 22 | pinned-to-tag | `jdx/mise-action@v4` |
| `audit.yml` | 32 | pinned-to-tag | `actions/upload-artifact@v4` |
| `benchmark.yml` | 28 | pinned-to-tag | `actions/checkout@v6` |
| `benchmark.yml` | 29 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `benchmark.yml` | 30 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `benchmark.yml` | 33 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `benchmark.yml` | 51 | pinned-to-tag | `benchmark-action/github-action-benchmark@v1` |
| `changelog.yml` | 19 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 32 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 35 | pinned-to-tag | `bufbuild/buf-action@v1` |
| `ci.yml` | 47 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 48 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `ci.yml` | 51 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 54 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 71 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 72 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `ci.yml` | 73 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 76 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 87 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 88 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `ci.yml` | 89 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 92 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 107 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 108 | pinned-to-tag | `rustsec/audit-check@v2.0.0` |
| `ci.yml` | 121 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 122 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `ci.yml` | 123 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 126 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 137 | pinned-to-tag | `crate-ci/typos@v1` |
| `ci.yml` | 144 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 145 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `ci.yml` | 146 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 149 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 158 | pinned-to-tag | `codecov/codecov-action@v4` |
| `ci.yml` | 172 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 173 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `ci.yml` | 176 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 177 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 194 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 195 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `ci.yml` | 196 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 197 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 208 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 209 | unpinned-other-ref | `dtolnay/rust-toolchain@1.86.0` |
| `ci.yml` | 210 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 211 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 222 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 223 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `ci.yml` | 224 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 225 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 236 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 254 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 255 | pinned-to-tag | `actions/setup-python@v5` |
| `ci.yml` | 273 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 274 | pinned-to-tag | `actions/setup-python@v5` |
| `ci.yml` | 287 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 293 | pinned-to-tag | `reviewdog/action-actionlint@v1` |
| `ci.yml` | 301 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 304 | pinned-to-tag | `wagoid/commitlint-github-action@v6` |
| `docs.yml` | 30 | pinned-to-tag | `actions/checkout@v4` |
| `docs.yml` | 31 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `evidence-capture.yml` | 27 | pinned-to-tag | `actions/checkout@v4` |
| `evidence-capture.yml` | 30 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `evidence-capture.yml` | 35 | pinned-to-tag | `actions/cache@v4` |
| `evidence-capture.yml` | 107 | pinned-to-tag | `actions/upload-artifact@v4` |
| `fuzzing.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `fuzzing.yml` | 20 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `gate-check.yml` | 29 | pinned-to-tag | `actions/checkout@v6` |
| `gate-check.yml` | 32 | pinned-to-tag | `jdx/mise-action@v4` |
| `iac-scan.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `iac-scan.yml` | 31 | pinned-to-tag | `actions/checkout@v4` |
| `libs-activation-ci.yml` | 17 | pinned-to-tag | `actions/checkout@v4` |
| `libs-activation-ci.yml` | 18 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `license-compliance.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `license-compliance.yml` | 29 | pinned-to-tag | `actions/checkout@v4` |
| `policy-gate.yml` | 17 | pinned-to-tag | `actions/checkout@v6` |
| `publish.yml` | 35 | pinned-to-tag | `actions/checkout@v6` |
| `publish.yml` | 38 | pinned-to-tag | `jdx/mise-action@v4` |
| `quality-gate.yml` | 10 | pinned-to-tag | `actions/checkout@v4` |
| `release-drafter.yml` | 12 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/release-drafter.yml@main` |
| `release.yml` | 39 | pinned-to-tag | `actions/checkout@v6` |
| `release.yml` | 40 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `release.yml` | 41 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `release.yml` | 42 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `release.yml` | 62 | pinned-to-tag | `actions/upload-artifact@v4` |
| `release.yml` | 155 | pinned-to-tag | `actions/checkout@v6` |
| `release.yml` | 156 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `release.yml` | 160 | pinned-to-tag | `taiki-e/install-action@v2` |
| `release.yml` | 168 | pinned-to-tag | `actions/upload-artifact@v4` |
| `release.yml` | 180 | pinned-to-tag | `actions/checkout@v6` |
| `release.yml` | 201 | pinned-to-tag | `actions/upload-artifact@v4` |
| `release.yml` | 224 | pinned-to-tag | `actions/checkout@v6` |
| `release.yml` | 228 | pinned-to-tag | `actions/download-artifact@v4` |
| `release.yml` | 259 | pinned-to-tag | `ncipollo/release-action@v1` |
| `sast-full.yml` | 21 | pinned-to-tag | `actions/checkout@v4` |
| `sast-full.yml` | 24 | pinned-to-tag | `github/codeql-action/init@v3` |
| `sast-full.yml` | 29 | pinned-to-tag | `github/codeql-action/analyze@v3` |
| `sast-full.yml` | 35 | pinned-to-tag | `actions/checkout@v4` |
| `sast-full.yml` | 45 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `sast-full.yml` | 56 | pinned-to-tag | `actions/checkout@v4` |
| `sast-full.yml` | 57 | pinned-to-tag | `returntocorp/semgrep-action@v1` |
| `sast-full.yml` | 68 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `sast-full.yml` | 78 | pinned-to-tag | `actions/checkout@v4` |
| `sast-quick.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `sast-quick.yml` | 20 | pinned-to-tag | `returntocorp/semgrep-action@v1` |
| `sast-quick.yml` | 31 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `sast-quick.yml` | 42 | pinned-to-tag | `actions/checkout@v4` |
| `sast-quick.yml` | 56 | pinned-to-tag | `actions/checkout@v4` |
| `sast-quick.yml` | 57 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `sast-quick.yml` | 60 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `sast-quick.yml` | 67 | pinned-to-tag | `actions/checkout@v4` |
| `sast-quick.yml` | 68 | pinned-to-tag | `licensefinder/license_finder_action@v2` |
| `sbom.yml` | 23 | pinned-to-tag | `actions/checkout@v4` |
| `sbom.yml` | 26 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `sbom.yml` | 29 | pinned-to-tag | `taiki-e/install-action@v2` |
| `sbom.yml` | 37 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `security-guard.yml` | 18 | pinned-to-tag | `actions/checkout@v6` |
| `security-guard.yml` | 23 | pinned-to-tag | `pre-commit/action@v3.0.1` |
| `security.yml` | 31 | pinned-to-tag | `actions/checkout@v6` |
| `security.yml` | 32 | pinned-to-tag | `rustsec/audit-check@v2.0.0` |
| `security.yml` | 41 | pinned-to-tag | `actions/checkout@v6` |
| `security.yml` | 42 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `security.yml` | 57 | pinned-to-tag | `actions/checkout@v6` |
| `security.yml` | 60 | pinned-to-tag | `gitleaks/gitleaks-action@v2` |
| `security.yml` | 75 | pinned-to-tag | `actions/checkout@v6` |
| `security.yml` | 76 | pinned-to-tag | `github/codeql-action/init@v3` |
| `security.yml` | 79 | pinned-to-tag | `github/codeql-action/analyze@v3` |
| `security.yml` | 86 | pinned-to-tag | `actions/checkout@v6` |
| `security.yml` | 87 | pinned-to-tag | `actions/setup-python@v5` |
| `security.yml` | 106 | pinned-to-tag | `actions/checkout@v6` |
| `security.yml` | 107 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `security.yml` | 124 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `self-merge-gate.yml` | 13 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/self-merge-gate.yml@main` |
| `snyk-scan.yml` | 49 | pinned-to-tag | `actions/checkout@v4` |
| `snyk-scan.yml` | 54 | pinned-to-tag | `actions/setup-node@v4` |
| `snyk-scan.yml` | 87 | pinned-to-tag | `github/codeql-action/upload-sarif@v2` |
| `snyk-scan.yml` | 105 | pinned-to-tag | `actions/github-script@v7` |
| `snyk-scan.yml` | 133 | pinned-to-tag | `actions/checkout@v4` |
| `snyk-scan.yml` | 138 | pinned-to-tag | `actions/setup-node@v4` |
| `snyk-scan.yml` | 168 | pinned-to-tag | `peter-evans/create-pull-request@v5` |
| `snyk-scan.yml` | 201 | pinned-to-tag | `actions/checkout@v4` |
| `snyk-scan.yml` | 213 | pinned-to-tag | `actions/upload-artifact@v3` |
| `sonarcloud.yml` | 15 | pinned-to-tag | `actions/checkout@v4` |
| `sonarcloud.yml` | 17 | pinned-to-tag | `actions/setup-java@v3` |
| `spec-validation.yml` | 23 | pinned-to-tag | `actions/checkout@v4` |
| `spec-validation.yml` | 28 | pinned-to-tag | `actions/setup-python@v4` |
| `spec-validation.yml` | 141 | pinned-to-tag | `actions/github-script@v6` |
| `sync-canary.yml` | 20 | pinned-to-tag | `actions/checkout@v6` |
| `tag-automation.yml` | 16 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/tag-automation.yml@main` |
| `traceability-gate.yml` | 16 | pinned-to-tag | `actions/checkout@v6` |
| `traceability-gate.yml` | 19 | pinned-to-tag | `actions/setup-python@v5` |
| `trivy-scan.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `trivy-scan.yml` | 28 | pinned-to-tag | `github/codeql-action/upload-sarif@v2` |
| `workflow-maintenance.yml` | 20 | pinned-to-tag | `actions/checkout@v4` |
| `workflow-maintenance.yml` | 45 | pinned-to-tag | `actions/checkout@v4` |
| `workflow-sync.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `zap-dast.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |

### helios-cli (152 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `bazel.yml` | 115 | pinned-to-tag | `actions/checkout@v6` |
| `bazel.yml` | 118 | pinned-to-tag | `actions/setup-node@v6` |
| `bazel.yml` | 125 | pinned-to-tag | `facebook/install-dotslash@v2` |
| `bazel.yml` | 138 | pinned-to-tag | `bazelbuild/setup-bazelisk@v3` |
| `blob-size-policy.yml` | 11 | pinned-to-tag | `actions/checkout@v6` |
| `cargo-deny.yml` | 18 | pinned-to-tag | `actions/checkout@v6` |
| `cargo-deny.yml` | 21 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `cargo-deny.yml` | 24 | pinned-to-tag | `EmbarkStudios/cargo-deny-action@v2` |
| `ci.yml` | 15 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 18 | pinned-to-tag | `pnpm/action-setup@v5` |
| `ci.yml` | 23 | pinned-to-tag | `actions/setup-node@v6` |
| `ci.yml` | 31 | pinned-to-tag | `facebook/install-dotslash@v2` |
| `ci.yml` | 57 | pinned-to-tag | `actions/upload-artifact@v6` |
| `ci.yml` | 59 | pinned-to-tag | `actions/upload-artifact@v7` |
| `cla.yml` | 21 | pinned-to-tag | `contributor-assistant/github-action@v2.6.1` |
| `close-stale-contributor-prs.yml` | 20 | pinned-to-tag | `actions/github-script@v8` |
| `codespell.yml` | 21 | pinned-to-tag | `actions/checkout@v6` |
| `docs-deploy.yml` | 21 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/vitepress-pages.yml@main` |
| `issue-deduplicator.yml` | 22 | pinned-to-tag | `actions/checkout@v6` |
| `issue-deduplicator.yml` | 158 | pinned-to-tag | `actions/checkout@v6` |
| `issue-deduplicator.yml` | 345 | pinned-to-tag | `actions/github-script@v8` |
| `issue-labeler.yml` | 20 | pinned-to-tag | `actions/checkout@v6` |
| `namespace-audit-retro.yml` | 23 | pinned-to-tag | `actions/checkout@v4` |
| `namespace-audit-retro.yml` | 47 | pinned-to-tag | `actions/upload-artifact@v4` |
| `policy-gate.yml` | 17 | pinned-to-tag | `actions/checkout@v4` |
| `pr-babysit-watch.yml` | 27 | pinned-to-tag | `actions/checkout@v4` |
| `rust-ci.yml` | 39 | pinned-to-tag | `actions/checkout@v6` |
| `rust-ci.yml` | 194 | pinned-to-tag | `actions/checkout@v6` |
| `rust-ci.yml` | 195 | unpinned-other-ref | `dtolnay/rust-toolchain@1.93.0` |
| `rust-ci.yml` | 244 | pinned-to-tag | `actions/checkout@v6` |
| `rust-ci.yml` | 245 | unpinned-other-ref | `dtolnay/rust-toolchain@1.93.0` |
| `rust-ci.yml` | 260 | pinned-to-tag | `actions/checkout@v6` |
| `rust-ci.yml` | 261 | unpinned-other-ref | `dtolnay/rust-toolchain@1.93.0` |
| `rust-ci.yml` | 275 | pinned-to-tag | `actions/checkout@v6` |
| `rust-ci.yml` | 276 | unpinned-other-ref | `dtolnay/rust-toolchain@1.93.0` |
| `rust-ci.yml` | 282 | pinned-to-tag | `actions/cache@v5` |
| `rust-ci.yml` | 319 | pinned-to-tag | `actions/checkout@v6` |
| `rust-ci.yml` | 326 | unpinned-other-ref | `dtolnay/rust-toolchain@1.93.0` |
| `rust-ci.yml` | 330 | pinned-to-tag | `facebook/install-dotslash@v2` |
| `rust-ci.yml` | 361 | pinned-to-tag | `actions/checkout@v6` |
| `rust-ci.yml` | 375 | unpinned-other-ref | `dtolnay/rust-toolchain@1.93.0` |
| `rust-ci.yml` | 404 | pinned-to-tag | `actions/cache/restore@v5` |
| `rust-ci.yml` | 449 | pinned-to-tag | `actions/cache/restore@v5` |
| `rust-ci.yml` | 476 | pinned-to-tag | `actions/cache/restore@v5` |
| `rust-ci.yml` | 589 | pinned-to-tag | `actions/upload-artifact@v7` |
| `rust-ci.yml` | 600 | pinned-to-tag | `actions/cache/save@v5` |
| `rust-ci.yml` | 616 | pinned-to-tag | `actions/cache/save@v5` |
| `rust-ci.yml` | 641 | pinned-to-tag | `actions/cache/save@v5` |
| `rust-ci.yml` | 702 | pinned-to-tag | `actions/checkout@v6` |
| `rust-ci.yml` | 704 | pinned-to-tag | `actions/setup-node@v6` |
| `rust-ci.yml` | 720 | pinned-to-tag | `facebook/install-dotslash@v2` |
| `rust-ci.yml` | 721 | unpinned-other-ref | `dtolnay/rust-toolchain@1.93.0` |
| `rust-ci.yml` | 737 | pinned-to-tag | `actions/cache/restore@v5` |
| `rust-ci.yml` | 777 | pinned-to-tag | `actions/cache/restore@v5` |
| `rust-ci.yml` | 819 | pinned-to-tag | `actions/upload-artifact@v7` |
| `rust-ci.yml` | 828 | pinned-to-tag | `actions/cache/save@v5` |
| `rust-ci.yml` | 840 | pinned-to-tag | `actions/cache/save@v5` |
| `rust-release-argument-comment-lint.yml` | 56 | pinned-to-tag | `actions/checkout@v6` |
| `rust-release-argument-comment-lint.yml` | 57 | unpinned-other-ref | `dtolnay/rust-toolchain@1.93.0` |
| `rust-release-argument-comment-lint.yml` | 99 | pinned-to-tag | `actions/upload-artifact@v7` |
| `rust-release-prepare.yml` | 21 | pinned-to-tag | `actions/checkout@v6` |
| `rust-release-prepare.yml` | 46 | pinned-to-tag | `peter-evans/create-pull-request@v8` |
| `rust-release-windows.yml` | 70 | pinned-to-tag | `actions/checkout@v6` |
| `rust-release-windows.yml` | 85 | unpinned-other-ref | `dtolnay/rust-toolchain@1.93.0` |
| `rust-release-windows.yml` | 95 | pinned-to-tag | `actions/upload-artifact@v7` |
| `rust-release-windows.yml` | 115 | pinned-to-tag | `actions/upload-artifact@v7` |
| `rust-release-windows.yml` | 150 | pinned-to-tag | `actions/checkout@v6` |
| `rust-release-windows.yml` | 153 | pinned-to-tag | `actions/download-artifact@v8` |
| `rust-release-windows.yml` | 159 | pinned-to-tag | `actions/download-artifact@v8` |
| `rust-release-windows.yml` | 196 | pinned-to-tag | `facebook/install-dotslash@v2` |
| `rust-release-windows.yml` | 259 | pinned-to-tag | `actions/upload-artifact@v7` |
| `rust-release-zsh.yml` | 47 | pinned-to-tag | `actions/checkout@v6` |
| `rust-release-zsh.yml` | 55 | pinned-to-tag | `actions/upload-artifact@v7` |
| `rust-release-zsh.yml` | 83 | pinned-to-tag | `actions/checkout@v6` |
| `rust-release-zsh.yml` | 91 | pinned-to-tag | `actions/upload-artifact@v7` |
| `rust-release.yml` | 29 | pinned-to-tag | `actions/checkout@v6` |
| `rust-release.yml` | 30 | unpinned-other-ref | `dtolnay/rust-toolchain@1.92` |
| `rust-release.yml` | 124 | pinned-to-tag | `actions/checkout@v6` |
| `rust-release.yml` | 170 | unpinned-other-ref | `dtolnay/rust-toolchain@1.93.0` |
| `rust-release.yml` | 280 | pinned-to-tag | `actions/upload-artifact@v7` |
| `rust-release.yml` | 418 | pinned-to-tag | `actions/upload-artifact@v7` |
| `rust-release.yml` | 479 | pinned-to-tag | `actions/checkout@v6` |
| `rust-release.yml` | 500 | pinned-to-tag | `actions/download-artifact@v8` |
| `rust-release.yml` | 551 | pinned-to-tag | `pnpm/action-setup@v5` |
| `rust-release.yml` | 556 | pinned-to-tag | `actions/setup-node@v6` |
| `rust-release.yml` | 564 | pinned-to-tag | `facebook/install-dotslash@v2` |
| `rust-release.yml` | 588 | pinned-to-tag | `softprops/action-gh-release@v2` |
| `rust-release.yml` | 597 | pinned-to-tag | `facebook/dotslash-publish-release@v2` |
| `rust-release.yml` | 604 | pinned-to-tag | `facebook/dotslash-publish-release@v2` |
| `rust-release.yml` | 611 | pinned-to-tag | `facebook/dotslash-publish-release@v2` |
| `rust-release.yml` | 647 | pinned-to-tag | `actions/setup-node@v6` |
| `rusty-v8-release.yml` | 28 | pinned-to-tag | `actions/checkout@v6` |
| `rusty-v8-release.yml` | 31 | pinned-to-tag | `actions/setup-python@v6` |
| `rusty-v8-release.yml` | 78 | pinned-to-tag | `actions/checkout@v6` |
| `rusty-v8-release.yml` | 81 | pinned-to-tag | `bazelbuild/setup-bazelisk@v3` |
| `rusty-v8-release.yml` | 84 | pinned-to-tag | `actions/setup-python@v6` |
| `rusty-v8-release.yml` | 138 | pinned-to-tag | `actions/upload-artifact@v7` |
| `rusty-v8-release.yml` | 176 | pinned-to-tag | `actions/download-artifact@v8` |
| `rusty-v8-release.yml` | 182 | pinned-to-tag | `softprops/action-gh-release@v2` |
| `sbom-refresh.yml` | 9 | pinned-to-branch | `KooshaPari/phenotype-tooling/.github/workflows/sbom-monthly.yml@main` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `sdk.yml` | 16 | pinned-to-tag | `actions/checkout@v6` |
| `sdk.yml` | 26 | pinned-to-tag | `pnpm/action-setup@v5` |
| `sdk.yml` | 31 | pinned-to-tag | `actions/setup-node@v6` |
| `sdk.yml` | 35 | unpinned-other-ref | `dtolnay/rust-toolchain@1.93.0` |
| `shell-tool-mcp.yml` | 212 | pinned-to-tag | `actions/checkout@v6` |
| `shell-tool-mcp.yml` | 230 | pinned-to-tag | `actions/upload-artifact@v6` |
| `shell-tool-mcp.yml` | 250 | pinned-to-tag | `actions/checkout@v6` |
| `shell-tool-mcp.yml` | 268 | pinned-to-tag | `actions/upload-artifact@v6` |
| `shell-tool-mcp.yml` | 348 | pinned-to-tag | `actions/checkout@v6` |
| `shell-tool-mcp.yml` | 394 | pinned-to-tag | `actions/upload-artifact@v6` |
| `shell-tool-mcp.yml` | 422 | pinned-to-tag | `actions/checkout@v6` |
| `shell-tool-mcp.yml` | 468 | pinned-to-tag | `actions/upload-artifact@v6` |
| `shell-tool-mcp.yml` | 488 | pinned-to-tag | `actions/checkout@v6` |
| `shell-tool-mcp.yml` | 491 | pinned-to-tag | `pnpm/action-setup@v4` |
| `shell-tool-mcp.yml` | 496 | pinned-to-tag | `actions/setup-node@v6` |
| `shell-tool-mcp.yml` | 507 | pinned-to-tag | `actions/download-artifact@v7` |
| `shell-tool-mcp.yml` | 565 | pinned-to-tag | `actions/upload-artifact@v6` |
| `shell-tool-mcp.yml` | 584 | pinned-to-tag | `actions/setup-node@v6` |
| `shell-tool-mcp.yml` | 595 | pinned-to-tag | `actions/download-artifact@v7` |
| `stage-gates.yml` | 24 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 97 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 116 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 127 | pinned-to-tag | `golangci/golangci-lint-action@v4` |
| `stage-gates.yml` | 140 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 143 | pinned-to-tag | `gitleaks/gitleaks-action@v2` |
| `stage-gates.yml` | 152 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 176 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 200 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 242 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 261 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 280 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 291 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 305 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 319 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 333 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 347 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 360 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 378 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 380 | pinned-to-tag | `anchore/sbom-action@v0` |
| `stage-gates.yml` | 389 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 400 | pinned-to-tag | `actions/upload-artifact@v4` |
| `stage-gates.yml` | 410 | pinned-to-tag | `actions/checkout@v4` |
| `v8-canary.yml` | 41 | pinned-to-tag | `actions/checkout@v6` |
| `v8-canary.yml` | 44 | pinned-to-tag | `actions/setup-python@v6` |
| `v8-canary.yml` | 75 | pinned-to-tag | `actions/checkout@v6` |
| `v8-canary.yml` | 78 | pinned-to-tag | `bazelbuild/setup-bazelisk@v3` |
| `v8-canary.yml` | 81 | pinned-to-tag | `actions/setup-python@v6` |
| `v8-canary.yml` | 129 | pinned-to-tag | `actions/upload-artifact@v7` |

### AgilePlus (133 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `alert-sync-issues.yml` | 12 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/alert-sync-issues.yml@main` |
| `audit.yml` | 20 | pinned-to-tag | `actions/checkout@v6` |
| `audit.yml` | 23 | pinned-to-tag | `jdx/mise-action@v4` |
| `audit.yml` | 33 | pinned-to-tag | `actions/upload-artifact@v4` |
| `changelog.yml` | 20 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 29 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 32 | pinned-to-tag | `bufbuild/buf-action@v1` |
| `ci.yml` | 44 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 45 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `ci.yml` | 48 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 51 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 68 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 69 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `ci.yml` | 70 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 73 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 84 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 85 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `ci.yml` | 86 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 89 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 104 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 105 | pinned-to-tag | `rustsec/audit-check@v2.0.0` |
| `ci.yml` | 118 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 119 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `ci.yml` | 120 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 123 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 134 | pinned-to-tag | `crate-ci/typos@v1` |
| `ci.yml` | 142 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 143 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `ci.yml` | 144 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 147 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 156 | pinned-to-tag | `codecov/codecov-action@v6` |
| `ci.yml` | 170 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 171 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `ci.yml` | 174 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 175 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 192 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 193 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `ci.yml` | 194 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 195 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 206 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 207 | unpinned-other-ref | `dtolnay/rust-toolchain@1.86.0` |
| `ci.yml` | 208 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 209 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 220 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 221 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `ci.yml` | 222 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 223 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `ci.yml` | 234 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 252 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 253 | pinned-to-tag | `actions/setup-python@v5` |
| `ci.yml` | 278 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 279 | pinned-to-tag | `actions/setup-python@v5` |
| `ci.yml` | 292 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 298 | pinned-to-tag | `reviewdog/action-actionlint@v1` |
| `ci.yml` | 306 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 309 | pinned-to-tag | `wagoid/commitlint-github-action@v6` |
| `code-scanning-results.yml` | 17 | pinned-to-tag | `actions/checkout@v6` |
| `code-scanning-results.yml` | 20 | pinned-to-tag | `actions/github-script@v9` |
| `codeql.yml` | 36 | pinned-to-tag | `actions/checkout@v6` |
| `codeql.yml` | 39 | pinned-to-tag | `github/codeql-action/init@v4` |
| `codeql.yml` | 45 | pinned-to-tag | `github/codeql-action/autobuild@v4` |
| `codeql.yml` | 48 | pinned-to-tag | `github/codeql-action/analyze@v4` |
| `deploy.yml` | 13 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/vitepress-pages.yml@main` |
| `doc-links.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `evidence-capture.yml` | 27 | pinned-to-tag | `actions/checkout@v6` |
| `evidence-capture.yml` | 30 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `evidence-capture.yml` | 35 | pinned-to-tag | `actions/cache@v5` |
| `evidence-capture.yml` | 107 | pinned-to-tag | `actions/upload-artifact@v4` |
| `fr-coverage.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `gate-check.yml` | 30 | pinned-to-tag | `actions/checkout@v6` |
| `gate-check.yml` | 33 | pinned-to-tag | `jdx/mise-action@v4` |
| `openapi-check.yml` | 31 | pinned-to-tag | `actions/checkout@v6` |
| `policy-gate.yml` | 17 | pinned-to-tag | `actions/checkout@v6` |
| `pr-governance-gate.yml` | 21 | pinned-to-tag | `actions/github-script@v9` |
| `publish.yml` | 40 | pinned-to-tag | `actions/checkout@v6` |
| `publish.yml` | 43 | pinned-to-tag | `jdx/mise-action@v4` |
| `quality-gate.yml` | 10 | pinned-to-tag | `actions/checkout@v6` |
| `quality-gate.yml` | 11 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 12 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `quality-gate.yml` | 17 | pinned-to-tag | `actions/cache@v5` |
| `quality-gate.yml` | 22 | pinned-to-tag | `actions/cache@v5` |
| `quality-gate.yml` | 27 | pinned-to-tag | `actions/cache@v5` |
| `regen-docs-specs.yml` | 31 | pinned-to-tag | `actions/checkout@v6` |
| `release-drafter.yml` | 12 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable-release-drafter.yml@main` |
| `rust-security.yml` | 19 | pinned-to-tag | `actions/checkout@v6` |
| `rust-security.yml` | 21 | pinned-to-tag | `taiki-e/install-action@v2` |
| `rust-security.yml` | 31 | pinned-to-tag | `actions/checkout@v6` |
| `rust-security.yml` | 32 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `rust-security.yml` | 35 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `rust-security.yml` | 36 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `rust-security.yml` | 46 | pinned-to-tag | `actions/checkout@v6` |
| `rust-security.yml` | 47 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `sast-full.yml` | 21 | pinned-to-tag | `actions/checkout@v6` |
| `sast-full.yml` | 24 | pinned-to-tag | `github/codeql-action/init@v4` |
| `sast-full.yml` | 29 | pinned-to-tag | `github/codeql-action/analyze@v4` |
| `sast-full.yml` | 35 | pinned-to-tag | `actions/checkout@v6` |
| `sast-full.yml` | 45 | pinned-to-tag | `github/codeql-action/upload-sarif@v4` |
| `sast-full.yml` | 56 | pinned-to-tag | `actions/checkout@v6` |
| `sast-full.yml` | 57 | pinned-to-tag | `returntocorp/semgrep-action@v1` |
| `sast-full.yml` | 68 | pinned-to-tag | `github/codeql-action/upload-sarif@v4` |
| `sast-full.yml` | 78 | pinned-to-tag | `actions/checkout@v6` |
| `sast-quick.yml` | 19 | pinned-to-tag | `actions/checkout@v6` |
| `sast-quick.yml` | 20 | pinned-to-tag | `returntocorp/semgrep-action@v1` |
| `sast-quick.yml` | 31 | pinned-to-tag | `github/codeql-action/upload-sarif@v4` |
| `sast-quick.yml` | 42 | pinned-to-tag | `actions/checkout@v6` |
| `sast-quick.yml` | 56 | pinned-to-tag | `actions/checkout@v6` |
| `sast-quick.yml` | 57 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `sast-quick.yml` | 60 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `sast-quick.yml` | 61 | pinned-to-tag | `arduino/setup-protoc@v3` |
| `sast-quick.yml` | 71 | pinned-to-tag | `actions/checkout@v6` |
| `sast-quick.yml` | 72 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `sast-quick.yml` | 74 | pinned-to-tag | `taiki-e/install-action@v2` |
| `sbom-refresh.yml` | 12 | pinned-to-branch | `KooshaPari/phenotype-tooling/.github/workflows/sbom-monthly.yml@main` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v6` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.3` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v4` |
| `security-guard-hook-audit.yml` | 15 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/security-guard-hook-audit.yml@main` |
| `security-guard.yml` | 18 | pinned-to-tag | `actions/checkout@v6` |
| `security-guard.yml` | 23 | pinned-to-tag | `pre-commit/action@v3.0.1` |
| `self-merge-gate.yml` | 13 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/self-merge-gate.yml@main` |
| `sentry-error-tracking.yml` | 42 | pinned-to-tag | `actions/checkout@v6` |
| `sentry-error-tracking.yml` | 47 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `sentry-error-tracking.yml` | 52 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `sentry-error-tracking.yml` | 95 | pinned-to-tag | `actions/checkout@v6` |
| `sentry-error-tracking.yml` | 132 | pinned-to-tag | `actions/github-script@v9` |
| `snyk-scan.yml` | 24 | pinned-to-tag | `actions/checkout@v6` |
| `snyk-scan.yml` | 29 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `snyk-scan.yml` | 48 | pinned-to-tag | `github/codeql-action/upload-sarif@v4` |
| `snyk-scan.yml` | 55 | pinned-to-tag | `actions/github-script@v9` |
| `snyk-scan.yml` | 92 | pinned-to-tag | `actions/checkout@v6` |
| `sync-canary.yml` | 20 | pinned-to-tag | `actions/checkout@v6` |
| `tag-automation.yml` | 13 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/tag-automation.yml@main` |

### thegent (105 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ai-testing.yml` | 24 | pinned-to-tag | `actions/checkout@v4` |
| `ai-testing.yml` | 27 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `ai-testing.yml` | 38 | pinned-to-tag | `actions/checkout@v4` |
| `ai-testing.yml` | 41 | pinned-to-tag | `astral-sh/setup-uv@v7` |
| `ai-testing.yml` | 52 | pinned-to-tag | `actions/checkout@v4` |
| `ai-testing.yml` | 55 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `ai-testing.yml` | 67 | pinned-to-tag | `actions/checkout@v4` |
| `ai-testing.yml` | 70 | pinned-to-tag | `astral-sh/setup-uv@v7` |
| `ci.yml` | 9 | pinned-to-branch | `phenotype-dev/.github/.github/workflows/rust-ci.yml@main` |
| `coverage.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `coverage.yml` | 13 | pinned-to-tag | `codecov/codecov-action@v6` |
| `fuzzing.yml` | 15 | pinned-to-tag | `actions/checkout@v6` |
| `fuzzing.yml` | 17 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `iac-scan.yml` | 16 | pinned-to-tag | `actions/checkout@v6` |
| `iac-scan.yml` | 28 | pinned-to-tag | `actions/checkout@v6` |
| `license-compliance.yml` | 16 | pinned-to-tag | `actions/checkout@v6` |
| `license-compliance.yml` | 26 | pinned-to-tag | `actions/checkout@v6` |
| `pages-deploy.yml` | 26 | pinned-to-tag | `actions/checkout@v6` |
| `pages-deploy.yml` | 31 | pinned-to-tag | `actions/setup-node@v6` |
| `pages-deploy.yml` | 37 | pinned-to-tag | `actions/configure-pages@v6` |
| `pages-deploy.yml` | 40 | pinned-to-tag | `actions/cache@v5` |
| `pages-deploy.yml` | 57 | pinned-to-tag | `actions/upload-pages-artifact@v5` |
| `pages-deploy.yml` | 71 | pinned-to-tag | `actions/deploy-pages@v5` |
| `policy-gate.yml` | 17 | pinned-to-tag | `actions/checkout@v4` |
| `policy-gate.yml` | 49 | pinned-to-tag | `actions/github-script@v7` |
| `pr-governance-gate.yml` | 21 | pinned-to-tag | `actions/github-script@v7` |
| `quality-gate.yml` | 19 | pinned-to-tag | `actions/checkout@v6` |
| `quality-gate.yml` | 35 | pinned-to-tag | `actions/checkout@v6` |
| `quality-gate.yml` | 38 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 41 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `quality-gate.yml` | 52 | pinned-to-tag | `codecov/codecov-action@v6` |
| `quality-gate.yml` | 72 | pinned-to-tag | `actions/checkout@v6` |
| `quality-gate.yml` | 75 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 78 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `quality-gate.yml` | 89 | pinned-to-tag | `actions/checkout@v6` |
| `quality-gate.yml` | 92 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 95 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `quality-gate.yml` | 104 | pinned-to-tag | `actions/checkout@v6` |
| `quality-gate.yml` | 142 | pinned-to-tag | `actions/checkout@v6` |
| `quality-gate.yml` | 185 | pinned-to-tag | `actions/github-script@v9` |
| `release.yml` | 19 | pinned-to-tag | `actions/checkout@v6` |
| `release.yml` | 22 | pinned-to-tag | `actions/setup-node@v6` |
| `release.yml` | 46 | pinned-to-tag | `actions/checkout@v6` |
| `release.yml` | 52 | pinned-to-tag | `orhun/git-cliff-action@v4` |
| `release.yml` | 65 | pinned-to-tag | `actions/checkout@v6` |
| `release.yml` | 68 | pinned-to-tag | `actions/setup-node@v6` |
| `release.yml` | 90 | pinned-to-tag | `softprops/action-gh-release@v3` |
| `sast-full.yml` | 21 | pinned-to-tag | `actions/checkout@v4` |
| `sast-full.yml` | 24 | pinned-to-tag | `github/codeql-action/init@v3` |
| `sast-full.yml` | 29 | pinned-to-tag | `github/codeql-action/analyze@v3` |
| `sast-full.yml` | 35 | pinned-to-tag | `actions/checkout@v4` |
| `sast-full.yml` | 44 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `sast-full.yml` | 55 | pinned-to-tag | `actions/checkout@v4` |
| `sast-full.yml` | 67 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `sast-full.yml` | 77 | pinned-to-tag | `actions/checkout@v4` |
| `sast-quick.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `sast-quick.yml` | 31 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `sast-quick.yml` | 42 | pinned-to-tag | `actions/checkout@v4` |
| `sast-quick.yml` | 55 | pinned-to-tag | `actions/checkout@v4` |
| `sast-quick.yml` | 66 | pinned-to-tag | `actions/checkout@v4` |
| `sast-quick.yml` | 67 | pinned-to-tag | `licensefinder/license_finder_action@v2` |
| `sast.yml` | 17 | pinned-to-tag | `actions/checkout@v4` |
| `sast.yml` | 18 | pinned-to-tag | `github/codeql-action/init@v4` |
| `sast.yml` | 21 | pinned-to-tag | `github/codeql-action/autobuild@v4` |
| `sast.yml` | 22 | pinned-to-tag | `github/codeql-action/analyze@v4` |
| `sast.yml` | 34 | pinned-to-tag | `actions/checkout@v4` |
| `sast.yml` | 35 | pinned-to-tag | `returntocorp/semgrep-action@v1` |
| `sast.yml` | 40 | pinned-to-tag | `github/codeql-action/upload-sarif@v4` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v6` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.3` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v7` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v4` |
| `security-deep-scan.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 19 | pinned-to-branch | `aquasecurity/trivy-action@master` |
| `security-deep-scan.yml` | 28 | pinned-to-tag | `github/codeql-action/upload-sarif@v2` |
| `security-deep-scan.yml` | 36 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 41 | pinned-to-tag | `gitleaks/gitleaks-action@v2` |
| `security-deep-scan.yml` | 53 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 56 | pinned-to-tag | `github/codeql-action/init@v2` |
| `security-deep-scan.yml` | 61 | pinned-to-tag | `github/codeql-action/autobuild@v2` |
| `security-deep-scan.yml` | 64 | pinned-to-tag | `github/codeql-action/analyze@v2` |
| `security-deep-scan.yml` | 71 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 77 | pinned-to-branch | `aquasecurity/trivy-action@master` |
| `security-deep-scan.yml` | 84 | pinned-to-tag | `github/codeql-action/upload-sarif@v2` |
| `security-guard.yml` | 12 | pinned-to-tag | `actions/checkout@v4` |
| `security-guard.yml` | 14 | pinned-to-branch | `aquasecurity/trivy-action@master` |
| `security.yml` | 27 | pinned-to-tag | `actions/checkout@v4` |
| `security.yml` | 32 | pinned-to-tag | `gitleaks/gitleaks-action@v2` |
| `security.yml` | 47 | pinned-to-tag | `actions/checkout@v4` |
| `security.yml` | 50 | pinned-to-tag | `fsfe/reuse-action@v4` |
| `security.yml` | 68 | pinned-to-tag | `actions/checkout@v4` |
| `security.yml` | 71 | pinned-to-tag | `actions/setup-node@v6` |
| `security.yml` | 80 | pinned-to-tag | `returntocorp/semgrep-action@v1` |
| `security.yml` | 91 | pinned-to-tag | `github/codeql-action/upload-sarif@v4` |
| `security.yml` | 100 | pinned-to-tag | `github/codeql-action/analyze@v4` |
| `security.yml` | 112 | pinned-to-tag | `actions/checkout@v4` |
| `security.yml` | 116 | pinned-to-tag | `actions/setup-node@v6` |
| `security.yml` | 134 | pinned-to-tag | `actions/checkout@v4` |
| `security.yml` | 140 | pinned-to-branch | `aquasecurity/trivy-action@master` |
| `security.yml` | 147 | pinned-to-tag | `github/codeql-action/upload-sarif@v4` |
| `sonarcloud.yml` | 12 | pinned-to-tag | `actions/checkout@v6` |
| `sonarcloud.yml` | 14 | pinned-to-tag | `actions/setup-java@v5` |
| `trivy-scan.yml` | 14 | pinned-to-tag | `actions/checkout@v6` |
| `trivy-scan.yml` | 24 | pinned-to-tag | `github/codeql-action/upload-sarif@v4` |
| `zap-dast.yml` | 13 | pinned-to-tag | `actions/checkout@v6` |

### portage (92 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ci.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 22 | pinned-to-tag | `actions/setup-python@v4` |
| `ci.yml` | 42 | pinned-to-branch | `KooshaPari/phenotypeActions/.github/workflows/validate-governance.yml@main` |
| `claude-code-review.yml` | 31 | pinned-to-tag | `actions/checkout@v4` |
| `claude-code-review.yml` | 37 | unpinned-other-ref | `anthropics/claude-code-action@beta` |
| `claude.yml` | 29 | pinned-to-tag | `actions/checkout@v4` |
| `claude.yml` | 35 | unpinned-other-ref | `anthropics/claude-code-action@beta` |
| `coverage.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `coverage.yml` | 13 | pinned-to-tag | `codecov/codecov-action@v4` |
| `docs-deploy.yml` | 21 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/vitepress-pages.yml@main` |
| `legacy-tooling-gate.yml` | 20 | pinned-to-tag | `actions/checkout@v4` |
| `legacy-tooling-gate.yml` | 23 | pinned-to-tag | `actions/checkout@v4` |
| `legacy-tooling-gate.yml` | 30 | pinned-to-tag | `actions/setup-python@v5` |
| `legacy-tooling-gate.yml` | 48 | pinned-to-tag | `actions/upload-artifact@v4` |
| `legacy-tooling-gate.yml` | 55 | pinned-to-tag | `actions/upload-artifact@v4` |
| `legacy-tooling-gate.yml` | 63 | pinned-to-tag | `actions/github-script@v7` |
| `lint-test.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |
| `lint-test.yml` | 17 | pinned-to-branch | `KooshaPari/phenotypeActions/actions/lint-test@main` |
| `pytest.yml` | 20 | pinned-to-tag | `actions/checkout@v4` |
| `pytest.yml` | 23 | pinned-to-tag | `astral-sh/setup-uv@v5` |
| `pytest.yml` | 45 | pinned-to-tag | `codecov/codecov-action@v4` |
| `quality-gate.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 8 | pinned-to-tag | `astral-sh/setup-uv@v5` |
| `release.yml` | 21 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 27 | pinned-to-tag | `actions/setup-python@v4` |
| `release.yml` | 54 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 57 | pinned-to-branch | `KooshaPari/phenotypeActions/promote@main` |
| `reusable-policy-gate.yml` | 28 | pinned-to-tag | `actions/checkout@v4` |
| `reusable-policy-gate.yml` | 32 | pinned-to-tag | `actions/github-script@v7` |
| `reusable-policy-gate.yml` | 89 | pinned-to-tag | `actions/upload-artifact@v4` |
| `reusable-policy-gate.yml` | 99 | pinned-to-tag | `actions/checkout@v4` |
| `reusable-policy-gate.yml` | 102 | pinned-to-tag | `errata-ai/vale-action@v2` |
| `ruff-format.yml` | 14 | pinned-to-tag | `actions/checkout@v4` |
| `ruff-format.yml` | 22 | pinned-to-tag | `astral-sh/setup-uv@v5` |
| `sast.yml` | 11 | pinned-to-tag | `actions/checkout@v4` |
| `sast.yml` | 12 | pinned-to-tag | `github/codeql-action/init-action@v3` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `security-deep-scan.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 28 | pinned-to-tag | `github/codeql-action/upload-sarif@v2` |
| `security-deep-scan.yml` | 36 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 41 | pinned-to-tag | `gitleaks/gitleaks-action@v2` |
| `security-deep-scan.yml` | 53 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 56 | pinned-to-tag | `github/codeql-action/init@v2` |
| `security-deep-scan.yml` | 61 | pinned-to-tag | `github/codeql-action/autobuild@v2` |
| `security-deep-scan.yml` | 64 | pinned-to-tag | `github/codeql-action/analyze@v2` |
| `security-deep-scan.yml` | 71 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 84 | pinned-to-tag | `github/codeql-action/upload-sarif@v2` |
| `security-guard-hook-audit.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 24 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 98 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 99 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `stage-gates.yml` | 103 | pinned-to-tag | `astral-sh/setup-uv@v5` |
| `stage-gates.yml` | 125 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 126 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `stage-gates.yml` | 130 | pinned-to-tag | `astral-sh/setup-uv@v5` |
| `stage-gates.yml` | 139 | pinned-to-tag | `golangci/golangci-lint-action@v4` |
| `stage-gates.yml` | 155 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 158 | pinned-to-tag | `gitleaks/gitleaks-action@v2` |
| `stage-gates.yml` | 167 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 168 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `stage-gates.yml` | 172 | pinned-to-tag | `astral-sh/setup-uv@v5` |
| `stage-gates.yml` | 194 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 195 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `stage-gates.yml` | 199 | pinned-to-tag | `astral-sh/setup-uv@v5` |
| `stage-gates.yml` | 221 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 222 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `stage-gates.yml` | 226 | pinned-to-tag | `astral-sh/setup-uv@v5` |
| `stage-gates.yml` | 266 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 267 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `stage-gates.yml` | 289 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 290 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `stage-gates.yml` | 314 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 325 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 339 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 353 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 367 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 381 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 394 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 412 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 414 | pinned-to-tag | `anchore/sbom-action@v0` |
| `stage-gates.yml` | 423 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 434 | pinned-to-tag | `actions/upload-artifact@v4` |
| `stage-gates.yml` | 444 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 445 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `sync-registry.yml` | 20 | pinned-to-tag | `actions/checkout@v4` |
| `sync-registry.yml` | 23 | pinned-to-tag | `astral-sh/setup-uv@v5` |
| `tag-automation.yml` | 10 | pinned-to-tag | `actions/checkout@v4` |
| `ty.yml` | 19 | pinned-to-tag | `actions/checkout@v6` |
| `ty.yml` | 22 | pinned-to-tag | `astral-sh/setup-uv@v7` |

### heliosApp (89 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `agent-dir-guard.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |
| `alert-sync-issues.yml` | 13 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/alert-sync-issues.yml@main` |
| `ci.yml` | 23 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 26 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `ci.yml` | 42 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 45 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `ci.yml` | 61 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 64 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `ci.yml` | 80 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 83 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `ci.yml` | 98 | pinned-to-tag | `actions/checkout@v4` |
| `compliance-check.yml` | 23 | pinned-to-tag | `actions/checkout@v4` |
| `compliance-check.yml` | 29 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `compliance-check.yml` | 38 | pinned-to-tag | `actions/github-script@v9` |
| `compliance-check.yml` | 51 | pinned-to-tag | `anchore/sbom-action@v0` |
| `compliance-check.yml` | 72 | pinned-to-tag | `actions/github-script@v9` |
| `compliance-check.yml` | 88 | pinned-to-tag | `actions/github-script@v9` |
| `compliance-check.yml` | 125 | pinned-to-tag | `actions/github-script@v9` |
| `compliance-check.yml.bak` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `compliance-check.yml.bak` | 25 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `compliance-check.yml.bak` | 34 | pinned-to-tag | `actions/github-script@v7` |
| `compliance-check.yml.bak` | 47 | pinned-to-tag | `anchore/sbom-action@v0` |
| `compliance-check.yml.bak` | 74 | pinned-to-tag | `actions/github-script@v7` |
| `compliance-check.yml.bak` | 90 | pinned-to-tag | `actions/github-script@v7` |
| `compliance-check.yml.bak` | 127 | pinned-to-tag | `actions/github-script@v7` |
| `doc-links.yml` | 10 | pinned-to-tag | `actions/checkout@v4` |
| `format-check.yml` | 14 | pinned-to-tag | `actions/checkout@v4` |
| `format-check.yml` | 15 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `fr-coverage.yml` | 10 | pinned-to-tag | `actions/checkout@v4` |
| `gca.yml` | 24 | pinned-to-tag | `actions/checkout@v4` |
| `gca.yml` | 29 | pinned-to-tag | `actions/setup-node@v6` |
| `gca.yml` | 97 | pinned-to-tag | `actions/github-script@v9` |
| `lint-test.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |
| `lint-test.yml` | 19 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `policy-gate.yml` | 17 | pinned-to-tag | `actions/checkout@v4` |
| `pr-governance-gate.yml` | 14 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 11 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gates.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gates.yml` | 25 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `quality-gates.yml` | 30 | pinned-to-tag | `actions/cache@v4` |
| `quality-gates.yml` | 138 | pinned-to-tag | `actions/upload-artifact@v7` |
| `quality-gates.yml.bak` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gates.yml.bak` | 22 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `quality-gates.yml.bak` | 27 | pinned-to-tag | `actions/cache@v4` |
| `quality-gates.yml.bak` | 140 | pinned-to-tag | `actions/upload-artifact@v4` |
| `quality-gates.yml.bak` | 142 | pinned-to-tag | `actions/upload-artifact@v7` |
| `release-drafter.yml` | 12 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable-release-drafter.yml@main` |
| `required-check-names-guard.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |
| `required-checks-bridge.yml` | 21 | pinned-to-tag | `actions/github-script@v9` |
| `sbom-refresh.yml` | 12 | pinned-to-branch | `KooshaPari/phenotype-tooling/.github/workflows/sbom-monthly.yml@main` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `security-guard-hook-audit.yml` | 15 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/security-guard-hook-audit.yml@main` |
| `security-guard.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `security-guard.yml` | 23 | pinned-to-tag | `pre-commit/action@v3.0.1` |
| `self-merge-gate.yml` | 24 | pinned-to-tag | `actions/github-script@v9` |
| `self-merge-gate.yml` | 141 | pinned-to-tag | `actions/github-script@v9` |
| `self-merge-gate.yml` | 169 | pinned-to-tag | `actions/github-script@v9` |
| `self-merge-gate.yml.bak` | 21 | pinned-to-tag | `actions/github-script@v7` |
| `self-merge-gate.yml.bak` | 148 | pinned-to-tag | `actions/github-script@v7` |
| `self-merge-gate.yml.bak` | 176 | pinned-to-tag | `actions/github-script@v7` |
| `stage-gates.yml` | 66 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 68 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `stage-gates.yml` | 81 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 83 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `stage-gates.yml` | 96 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 98 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `stage-gates.yml` | 111 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 113 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `stage-gates.yml` | 126 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 142 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 144 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `strict-quality.yml` | 17 | pinned-to-tag | `actions/checkout@v4` |
| `strict-quality.yml` | 18 | pinned-to-tag | `oven-sh/setup-bun@v1` |
| `tag-automation.yml` | 16 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/tag-automation.yml@main` |
| `vitepress-pages.yml` | 36 | pinned-to-tag | `actions/checkout@v4` |
| `vitepress-pages.yml` | 41 | pinned-to-tag | `actions/checkout@v4` |
| `vitepress-pages.yml` | 47 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `vitepress-pages.yml` | 72 | pinned-to-tag | `actions/upload-pages-artifact@v5` |
| `vitepress-pages.yml` | 86 | pinned-to-tag | `actions/configure-pages@v6` |
| `vitepress-pages.yml` | 90 | pinned-to-tag | `actions/deploy-pages@v4` |
| `vitepress-pages.yml.bak` | 35 | pinned-to-tag | `actions/checkout@v4` |
| `vitepress-pages.yml.bak` | 40 | pinned-to-tag | `actions/checkout@v4` |
| `vitepress-pages.yml.bak` | 46 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `vitepress-pages.yml.bak` | 74 | pinned-to-tag | `actions/upload-pages-artifact@v3` |
| `vitepress-pages.yml.bak` | 88 | pinned-to-tag | `actions/configure-pages@v5` |
| `vitepress-pages.yml.bak` | 92 | pinned-to-tag | `actions/deploy-pages@v4` |

### FocalPoint (75 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `cargo-deny.yml` | 23 | pinned-to-tag | `actions/checkout@v6` |
| `cargo-deny.yml` | 26 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `cargo-deny.yml` | 29 | pinned-to-tag | `EmbarkStudios/cargo-deny-action@v2` |
| `cargo-doc.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `cargo-doc.yml` | 20 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `cargo-doc.yml` | 38 | pinned-to-tag | `peaceiris/actions-gh-pages@v3` |
| `cli-demo.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `cli-demo.yml` | 22 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `cli-demo.yml` | 27 | pinned-to-tag | `actions/cache@v5` |
| `cli-demo.yml` | 33 | pinned-to-tag | `actions/cache@v5` |
| `cli-demo.yml` | 39 | pinned-to-tag | `actions/cache@v5` |
| `cli-demo.yml` | 52 | pinned-to-tag | `actions/github-script@v7` |
| `cli-demo.yml` | 66 | pinned-to-tag | `actions/upload-artifact@v7` |
| `connector-manifest.yml` | 27 | pinned-to-tag | `actions/checkout@v4` |
| `connector-manifest.yml` | 30 | pinned-to-tag | `actions/setup-node@v4` |
| `dco.yml` | 14 | pinned-to-tag | `actions/checkout@v4` |
| `dco.yml` | 19 | pinned-to-tag | `tim-actions/dco@v1.1.0` |
| `disk-budget-weekly.yml` | 27 | pinned-to-tag | `actions/checkout@v4` |
| `disk-budget-weekly.yml` | 30 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `docs.yml` | 32 | pinned-to-tag | `actions/checkout@v4` |
| `docs.yml` | 35 | pinned-to-tag | `oven-sh/setup-bun@v1` |
| `docs.yml` | 48 | pinned-to-tag | `actions/upload-pages-artifact@v5` |
| `docs.yml` | 67 | pinned-to-tag | `actions/deploy-pages@v5` |
| `e2e-smoke.yml` | 21 | pinned-to-tag | `actions/checkout@v4` |
| `e2e-smoke.yml` | 24 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `e2e-smoke.yml` | 29 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `fuzz.yml` | 25 | pinned-to-tag | `actions/checkout@v4` |
| `fuzz.yml` | 26 | unpinned-other-ref | `dtolnay/rust-toolchain@nightly` |
| `fuzz.yml` | 46 | pinned-to-tag | `actions/upload-artifact@v7` |
| `fuzz.yml` | 62 | pinned-to-tag | `actions/checkout@v4` |
| `fuzz.yml` | 63 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `perf-guard.yml` | 17 | pinned-to-tag | `actions/checkout@v4` |
| `perf-guard.yml` | 18 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `perf-guard.yml` | 22 | pinned-to-tag | `actions/cache@v5` |
| `perf-guard.yml` | 28 | pinned-to-tag | `actions/cache@v5` |
| `perf-guard.yml` | 34 | pinned-to-tag | `actions/cache@v5` |
| `perf-guard.yml` | 52 | pinned-to-tag | `actions/github-script@v6` |
| `pr-checks.yml` | 21 | pinned-to-tag | `actions/checkout@v4` |
| `pr-checks.yml` | 65 | pinned-to-tag | `actions/checkout@v4` |
| `pr-checks.yml` | 97 | pinned-to-tag | `actions/checkout@v4` |
| `pr-checks.yml` | 130 | pinned-to-tag | `actions/checkout@v4` |
| `pr-checks.yml` | 155 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 24 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 27 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `release-dry-run.yml` | 20 | pinned-to-tag | `actions/checkout@v4` |
| `release-dry-run.yml` | 21 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `release-dry-run.yml` | 25 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `release-dry-run.yml` | 38 | pinned-to-tag | `actions/github-script@v7` |
| `rust.yml` | 29 | pinned-to-tag | `actions/checkout@v4` |
| `rust.yml` | 30 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `rust.yml` | 38 | pinned-to-tag | `actions/checkout@v4` |
| `rust.yml` | 39 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `rust.yml` | 42 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `rust.yml` | 48 | pinned-to-tag | `actions/checkout@v4` |
| `rust.yml` | 49 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `rust.yml` | 50 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `rust.yml` | 57 | pinned-to-tag | `actions/checkout@v4` |
| `sbom-refresh.yml` | 12 | pinned-to-branch | `KooshaPari/phenotype-tooling/.github/workflows/sbom-monthly.yml@main` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.3` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v7` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `supply-chain.yml` | 23 | pinned-to-tag | `actions/checkout@v4` |
| `supply-chain.yml` | 24 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `supply-chain.yml` | 28 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `supply-chain.yml` | 52 | pinned-to-tag | `actions/upload-artifact@v7` |
| `supply-chain.yml` | 64 | pinned-to-tag | `actions/checkout@v4` |
| `supply-chain.yml` | 65 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `supply-chain.yml` | 69 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `supply-chain.yml` | 92 | pinned-to-tag | `actions/upload-artifact@v7` |
| `supply-chain.yml` | 104 | pinned-to-tag | `actions/checkout@v4` |
| `supply-chain.yml` | 107 | pinned-to-tag | `actions/download-artifact@v4` |
| `traceability.yml` | 21 | pinned-to-tag | `actions/checkout@v4` |
| `traceability.yml` | 44 | pinned-to-tag | `actions/checkout@v4` |

### QuadSGM (63 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `auto-merge.yml` | 30 | pinned-to-tag | `peter-evans/enable-pull-request-automerge@v3` |
| `coverage.yml` | 43 | pinned-to-tag | `actions/checkout@v4` |
| `coverage.yml` | 46 | pinned-to-tag | `actions/setup-python@v5` |
| `coverage.yml` | 51 | pinned-to-tag | `astral-sh/setup-uv@v4` |
| `coverage.yml` | 92 | pinned-to-tag | `actions/upload-artifact@v4` |
| `coverage.yml` | 116 | pinned-to-tag | `actions/checkout@v4` |
| `coverage.yml` | 119 | pinned-to-tag | `actions/setup-python@v5` |
| `coverage.yml` | 124 | pinned-to-tag | `astral-sh/setup-uv@v4` |
| `coverage.yml` | 136 | pinned-to-tag | `returntocorp/semgrep-action@v1` |
| `coverage.yml` | 142 | pinned-to-tag | `actions/upload-artifact@v4` |
| `coverage.yml` | 159 | pinned-to-tag | `actions/checkout@v4` |
| `coverage.yml` | 192 | pinned-to-tag | `actions/checkout@v4` |
| `docs-site.yml` | 25 | pinned-to-tag | `actions/checkout@v4` |
| `pages-deploy.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |
| `pages-deploy.yml` | 17 | pinned-to-tag | `actions/configure-pages@v4` |
| `pages-deploy.yml` | 18 | pinned-to-tag | `actions/upload-pages-artifact@v3` |
| `pages-deploy.yml` | 22 | pinned-to-tag | `actions/deploy-pages@v4` |
| `pages.yml` | 36 | pinned-to-tag | `actions/checkout@v4` |
| `pages.yml` | 101 | pinned-to-tag | `actions/upload-pages-artifact@v3` |
| `pages.yml` | 118 | pinned-to-tag | `actions/deploy-pages@v4` |
| `policy-gate.yml` | 17 | pinned-to-tag | `actions/checkout@v4` |
| `qa-governance.yml` | 27 | pinned-to-tag | `actions/checkout@v4` |
| `qa-governance.yml` | 105 | pinned-to-tag | `actions/checkout@v4` |
| `qa-governance.yml` | 176 | pinned-to-tag | `actions/checkout@v4` |
| `qa-governance.yml` | 211 | pinned-to-tag | `actions/checkout@v4` |
| `qa-governance.yml` | 214 | pinned-to-tag | `actions/setup-python@v5` |
| `qa-governance.yml` | 219 | pinned-to-tag | `astral-sh/setup-uv@v4` |
| `qa-governance.yml` | 260 | pinned-to-tag | `actions/checkout@v4` |
| `qa-governance.yml` | 263 | pinned-to-tag | `actions/setup-python@v5` |
| `qa-governance.yml` | 268 | pinned-to-tag | `astral-sh/setup-uv@v4` |
| `qa-governance.yml` | 314 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `release-drafter.yml` | 12 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/release-drafter.yml@main` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `security-guard.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `security-guard.yml` | 23 | pinned-to-tag | `pre-commit/action@v3.0.1` |
| `self-merge-gate.yml` | 10 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/self-merge-gate.yml@main` |
| `stage-gates.yml` | 24 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 97 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 116 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 122 | pinned-to-tag | `golangci/golangci-lint-action@v4` |
| `stage-gates.yml` | 135 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 149 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 168 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 187 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 224 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 243 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 262 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 273 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 287 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 301 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 315 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 329 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 342 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 360 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 362 | pinned-to-tag | `anchore/sbom-action@v0` |
| `stage-gates.yml` | 371 | pinned-to-tag | `actions/checkout@v4` |
| `stage-gates.yml` | 382 | pinned-to-tag | `actions/upload-artifact@v4` |
| `stage-gates.yml` | 392 | pinned-to-tag | `actions/checkout@v4` |
| `tag-automation.yml` | 13 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/tag-automation.yml@main` |

### Stashly (61 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `auto-merge.yml` | 14 | pinned-to-tag | `actions/checkout@v4` |
| `auto-merge.yml` | 17 | pinned-to-tag | `actions/github-script@v7` |
| `benchmarks.yml` | 20 | pinned-to-tag | `actions/checkout@v4` |
| `benchmarks.yml` | 23 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `benchmarks.yml` | 28 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `benchmarks.yml` | 35 | pinned-to-tag | `actions/upload-artifact@v4` |
| `benchmarks.yml` | 43 | pinned-to-tag | `benchmark-action/github-action-benchmark@v1` |
| `ci.yml` | 17 | pinned-to-branch | `KooshaPari/template-commons/.github/workflows/reusable-rust-ci.yml@main` |
| `ci.yml` | 24 | pinned-to-branch | `KooshaPari/template-commons/.github/workflows/reusable-security-scan.yml@main` |
| `ci.yml` | 32 | pinned-to-branch | `KooshaPari/phenotypeActions/.github/workflows/validate-governance.yml@main` |
| `coverage.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `coverage.yml` | 13 | pinned-to-tag | `codecov/codecov-action@v4` |
| `pages-deploy.yml` | 17 | pinned-to-tag | `actions/checkout@v4` |
| `pages-deploy.yml` | 18 | pinned-to-tag | `actions/setup-node@v4` |
| `pages-deploy.yml` | 23 | pinned-to-tag | `actions/upload-pages-artifact@v3` |
| `pages-deploy.yml` | 26 | pinned-to-tag | `actions/deploy-pages@v4` |
| `pre-commit.yml` | 13 | pinned-to-tag | `actions/checkout@v4` |
| `pre-commit.yml` | 16 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 35 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 38 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 41 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `quality-gate.yml` | 52 | pinned-to-tag | `codecov/codecov-action@v4` |
| `quality-gate.yml` | 72 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 75 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 78 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `quality-gate.yml` | 89 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 92 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 95 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `quality-gate.yml` | 104 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 142 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 185 | pinned-to-tag | `actions/github-script@v7` |
| `release-drafter.yml` | 14 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/release-drafter.yml@main` |
| `release.yml` | 21 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 27 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `release.yml` | 50 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 53 | pinned-to-branch | `KooshaPari/phenotypeActions/promote@main` |
| `sast.yml` | 11 | pinned-to-tag | `actions/checkout@v4` |
| `sast.yml` | 12 | pinned-to-tag | `github/codeql-action/init-action@v3` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `security-deep-scan.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 28 | pinned-to-tag | `github/codeql-action/upload-sarif@v2` |
| `security-deep-scan.yml` | 36 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 54 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 57 | pinned-to-tag | `github/codeql-action/init@v2` |
| `security-deep-scan.yml` | 62 | pinned-to-tag | `github/codeql-action/autobuild@v2` |
| `security-deep-scan.yml` | 65 | pinned-to-tag | `github/codeql-action/analyze@v2` |
| `security-deep-scan.yml` | 72 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 85 | pinned-to-tag | `github/codeql-action/upload-sarif@v2` |
| `security-guard.yml` | 12 | pinned-to-tag | `actions/checkout@v4` |
| `security.yml` | 27 | pinned-to-tag | `actions/checkout@v4` |
| `security.yml` | 45 | pinned-to-tag | `actions/checkout@v4` |
| `security.yml` | 49 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `security.yml` | 55 | pinned-to-tag | `actions-rust-lang/audit@v1` |
| `security.yml` | 67 | pinned-to-tag | `actions/checkout@v4` |
| `security.yml` | 71 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `security.yml` | 87 | pinned-to-tag | `actions/checkout@v4` |
| `security.yml` | 100 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |

### agentapi-plusplus (55 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ci.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 23 | pinned-to-tag | `actions/checkout@v4` |
| `codeql.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `codeql.yml` | 23 | pinned-to-tag | `github/codeql-action/init@v3` |
| `codeql.yml` | 26 | pinned-to-tag | `github/codeql-action/analyze@v3` |
| `coderabbit-rate-limit-retry.yml` | 22 | pinned-to-tag | `actions/github-script@v7` |
| `docs-site.yml` | 29 | pinned-to-tag | `actions/checkout@v4` |
| `docs-site.yml` | 32 | pinned-to-tag | `actions/setup-node@v4` |
| `docs-site.yml` | 49 | pinned-to-tag | `actions/upload-pages-artifact@v3` |
| `docs-site.yml` | 63 | pinned-to-tag | `actions/deploy-pages@v4` |
| `fuzzing.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `fuzzing.yml` | 20 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `generate-sdks.yaml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `generate-sdks.yaml` | 21 | pinned-to-tag | `actions/setup-python@v5` |
| `generate-sdks.yaml` | 26 | pinned-to-tag | `actions/setup-node@v4` |
| `generate-sdks.yaml` | 31 | pinned-to-tag | `actions/setup-go@v5` |
| `generate-sdks.yaml` | 36 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `go-test.yml` | 15 | pinned-to-tag | `actions/checkout@v4` |
| `go-test.yml` | 18 | pinned-to-tag | `actions/setup-go@v5` |
| `go-test.yml` | 28 | pinned-to-tag | `actions/checkout@v4` |
| `go-test.yml` | 31 | pinned-to-tag | `actions/setup-go@v5` |
| `go-test.yml` | 36 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `iac-scan.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `iac-scan.yml` | 31 | pinned-to-tag | `actions/checkout@v4` |
| `license-compliance.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `license-compliance.yml` | 29 | pinned-to-tag | `actions/checkout@v4` |
| `lint-test.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |
| `pages-deploy.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |
| `pages-deploy.yml` | 17 | pinned-to-tag | `actions/configure-pages@v4` |
| `pages-deploy.yml` | 18 | pinned-to-tag | `actions/upload-pages-artifact@v3` |
| `pages-deploy.yml` | 22 | pinned-to-tag | `actions/deploy-pages@v4` |
| `policy-gate.yml` | 17 | pinned-to-tag | `actions/checkout@v4` |
| `policy-gate.yml` | 20 | pinned-to-branch | `KooshaPari/phenotypeActions/actions/policy-gate@main` |
| `pr-preview-build.yml` | 25 | pinned-to-tag | `actions/checkout@v4` |
| `pr-preview-build.yml` | 28 | pinned-to-tag | `actions/setup-go@v5` |
| `pr-preview-build.yml` | 33 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `pr-preview-release.yml` | 21 | pinned-to-tag | `actions/download-artifact@v4` |
| `pr-preview-release.yml` | 32 | pinned-to-tag | `actions/download-artifact@v4` |
| `pr-preview-release.yml` | 64 | pinned-to-tag | `actions/github-script@v7` |
| `quality-gate.yml` | 10 | pinned-to-tag | `actions/checkout@v4` |
| `release-drafter.yml` | 13 | pinned-to-tag | `release-drafter/release-drafter@v6` |
| `release.yml` | 26 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 29 | pinned-to-tag | `actions/setup-go@v5` |
| `release.yml` | 34 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `secrets-scan.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |
| `sonarcloud.yml` | 15 | pinned-to-tag | `actions/checkout@v4` |
| `sonarcloud.yml` | 17 | pinned-to-tag | `actions/setup-java@v3` |
| `tag-automation.yml` | 13 | pinned-to-tag | `actions/checkout@v4` |
| `trivy-scan.yml` | 17 | pinned-to-tag | `actions/checkout@v4` |
| `trivy-scan.yml` | 27 | pinned-to-tag | `github/codeql-action/upload-sarif@v2` |
| `zap-dast.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |

### Tasken (55 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `auto-merge.yml` | 14 | pinned-to-tag | `actions/checkout@v4` |
| `auto-merge.yml` | 17 | pinned-to-tag | `actions/github-script@v7` |
| `benchmarks.yml` | 20 | pinned-to-tag | `actions/checkout@v4` |
| `benchmarks.yml` | 23 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `benchmarks.yml` | 28 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `benchmarks.yml` | 35 | pinned-to-tag | `actions/upload-artifact@v4` |
| `benchmarks.yml` | 43 | pinned-to-tag | `benchmark-action/github-action-benchmark@v1` |
| `cargo-deny.yml` | 23 | pinned-to-tag | `actions/checkout@v6` |
| `cargo-deny.yml` | 26 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `cargo-deny.yml` | 29 | pinned-to-tag | `EmbarkStudios/cargo-deny-action@v2` |
| `ci.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 38 | pinned-to-branch | `KooshaPari/phenotypeActions/.github/workflows/validate-governance.yml@main` |
| `coverage.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `coverage.yml` | 13 | pinned-to-tag | `codecov/codecov-action@v4` |
| `pages-deploy.yml` | 17 | pinned-to-tag | `actions/checkout@v4` |
| `pages-deploy.yml` | 18 | pinned-to-tag | `actions/setup-node@v4` |
| `pages-deploy.yml` | 23 | pinned-to-tag | `actions/upload-pages-artifact@v3` |
| `pages-deploy.yml` | 26 | pinned-to-tag | `actions/deploy-pages@v4` |
| `pre-commit.yml` | 13 | pinned-to-tag | `actions/checkout@v4` |
| `pre-commit.yml` | 16 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 35 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 38 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 41 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `quality-gate.yml` | 52 | pinned-to-tag | `codecov/codecov-action@v4` |
| `quality-gate.yml` | 72 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 75 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 78 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `quality-gate.yml` | 89 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 92 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 95 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `quality-gate.yml` | 104 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 142 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 185 | pinned-to-tag | `actions/github-script@v7` |
| `release-drafter.yml` | 14 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/release-drafter.yml@main` |
| `release.yml` | 21 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 27 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `release.yml` | 50 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 53 | pinned-to-branch | `KooshaPari/phenotypeActions/promote@main` |
| `sast.yml` | 11 | pinned-to-tag | `actions/checkout@v4` |
| `sast.yml` | 12 | pinned-to-tag | `github/codeql-action/init-action@v3` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `security-guard.yml` | 13 | pinned-to-tag | `actions/checkout@v4` |
| `security-guard.yml` | 36 | pinned-to-tag | `actions/dependency-review-action@v4` |
| `security.yml` | 27 | pinned-to-tag | `actions/checkout@v4` |
| `security.yml` | 45 | pinned-to-tag | `actions/checkout@v4` |
| `security.yml` | 49 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `security.yml` | 55 | pinned-to-tag | `actions-rust-lang/audit@v1` |
| `security.yml` | 67 | pinned-to-tag | `actions/checkout@v4` |
| `security.yml` | 71 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `security.yml` | 87 | pinned-to-tag | `actions/checkout@v4` |
| `security.yml` | 100 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |

### vibeproxy (50 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `auto-release.yml` | 21 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 20 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 36 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 45 | pinned-to-tag | `codecov/codecov-action@v4` |
| `ci.yml` | 54 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 65 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 66 | pinned-to-branch | `KooshaPari/phenotypeActions/.github/workflows/validate-governance.yml@main` |
| `codeql.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `codeql.yml` | 23 | pinned-to-tag | `github/codeql-action/init@v3` |
| `codeql.yml` | 26 | pinned-to-tag | `github/codeql-action/analyze@v3` |
| `cross-platform-test.yml` | 17 | pinned-to-tag | `actions/checkout@v4` |
| `cross-platform-test.yml` | 20 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `cross-platform-test.yml` | 41 | pinned-to-tag | `actions/checkout@v4` |
| `cross-platform-test.yml` | 44 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `cross-platform-test.yml` | 47 | pinned-to-tag | `actions/setup-dotnet@v3` |
| `cross-platform-test.yml` | 70 | pinned-to-tag | `actions/checkout@v4` |
| `cross-platform-test.yml` | 85 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `cross-platform-test.yml` | 107 | pinned-to-tag | `actions/checkout@v4` |
| `linux-build.yml` | 20 | pinned-to-tag | `actions/checkout@v4` |
| `linux-build.yml` | 35 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `linux-build.yml` | 40 | pinned-to-tag | `actions/cache@v3` |
| `linux-build.yml` | 84 | pinned-to-tag | `actions/checkout@v4` |
| `linux-build.yml` | 99 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `release-drafter.yml` | 17 | pinned-to-tag | `release-drafter/release-drafter@v6` |
| `release.yml` | 50 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 55 | pinned-to-tag | `swift-actions/setup-swift@v2` |
| `release.yml` | 60 | pinned-to-tag | `apple-actions/import-codesign-certs@v2` |
| `release.yml` | 220 | pinned-to-tag | `actions/upload-artifact@v4` |
| `release.yml` | 236 | pinned-to-tag | `actions/upload-artifact@v4` |
| `release.yml` | 252 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 263 | pinned-to-tag | `actions/download-artifact@v4` |
| `release.yml` | 275 | pinned-to-tag | `actions/download-artifact@v4` |
| `release.yml` | 364 | pinned-to-tag | `softprops/action-gh-release@v1` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `secrets-scan.yml` | 15 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 28 | pinned-to-tag | `github/codeql-action/upload-sarif@v2` |
| `security-deep-scan.yml` | 36 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 41 | pinned-to-tag | `gitleaks/gitleaks-action@v2` |
| `security-deep-scan.yml` | 53 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 56 | pinned-to-tag | `github/codeql-action/init@v2` |
| `security-deep-scan.yml` | 61 | pinned-to-tag | `github/codeql-action/autobuild@v2` |
| `security-deep-scan.yml` | 64 | pinned-to-tag | `github/codeql-action/analyze@v2` |
| `security-deep-scan.yml` | 71 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 84 | pinned-to-tag | `github/codeql-action/upload-sarif@v2` |
| `update-cliproxyapi.yml` | 21 | pinned-to-tag | `actions/checkout@v4` |
| `update-cliproxyapi.yml` | 191 | pinned-to-tag | `peter-evans/create-pull-request@v6` |

### HeliosLab (50 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `build-release.yml` | 33 | pinned-to-tag | `actions/checkout@v4` |
| `build-release.yml` | 47 | pinned-to-tag | `actions/cache@v4` |
| `build-release.yml` | 56 | pinned-to-tag | `actions/cache@v4` |
| `build-release.yml` | 78 | pinned-to-tag | `actions/checkout@v4` |
| `build-release.yml` | 92 | pinned-to-tag | `actions/cache@v4` |
| `build-release.yml` | 108 | pinned-to-tag | `actions/cache@v4` |
| `build-release.yml` | 244 | pinned-to-tag | `actions/checkout@v4` |
| `build-release.yml` | 247 | pinned-to-tag | `actions/setup-node@v4` |
| `ci.yml` | 17 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 19 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `ci.yml` | 27 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 29 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `ci.yml` | 44 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 46 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `ci.yml` | 54 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 62 | pinned-to-tag | `actions/checkout@v4` |
| `coverage.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `coverage.yml` | 13 | pinned-to-tag | `codecov/codecov-action@v4` |
| `deploy-docs.yml` | 10 | pinned-to-tag | `actions/checkout@v4` |
| `deploy-docs.yml` | 11 | pinned-to-tag | `actions/setup-node@v4` |
| `deploy-docs.yml` | 15 | pinned-to-tag | `peaceiris/actions-gh-pages@v4` |
| `quality-gate.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 35 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 38 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 41 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `quality-gate.yml` | 52 | pinned-to-tag | `codecov/codecov-action@v4` |
| `quality-gate.yml` | 72 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 75 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 78 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `quality-gate.yml` | 89 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 92 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 95 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `quality-gate.yml` | 104 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 142 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 185 | pinned-to-tag | `actions/github-script@v7` |
| `release.yml` | 21 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 27 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `release.yml` | 50 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 53 | pinned-to-branch | `KooshaPari/phenotypeActions/promote@main` |
| `required-check-names-guard.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |
| `sast.yml` | 11 | pinned-to-tag | `actions/checkout@v4` |
| `sast.yml` | 12 | pinned-to-tag | `github/codeql-action/init@v3` |
| `sast.yml` | 15 | pinned-to-tag | `github/codeql-action/analyze@v3` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `security-guard-hook-audit.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `security-guard.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `security-guard.yml` | 23 | pinned-to-tag | `pre-commit/action@v3.0.1` |

### argis-extensions (48 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `cd.yml` | 35 | pinned-to-tag | `actions/checkout@v4` |
| `cd.yml` | 38 | pinned-to-tag | `docker/setup-buildx-action@v3` |
| `cd.yml` | 41 | pinned-to-tag | `docker/login-action@v3` |
| `cd.yml` | 49 | pinned-to-tag | `docker/metadata-action@v5` |
| `cd.yml` | 61 | pinned-to-tag | `docker/build-push-action@v5` |
| `cd.yml` | 81 | pinned-to-tag | `actions/checkout@v4` |
| `cd.yml` | 84 | pinned-to-tag | `johnbeynon/render-deploy-action@v0.0.8` |
| `cd.yml` | 90 | pinned-to-tag | `bervProject/railway-deploy@v0.2.4` |
| `cd.yml` | 106 | pinned-to-tag | `actions/checkout@v4` |
| `cd.yml` | 109 | pinned-to-tag | `johnbeynon/render-deploy-action@v0.0.8` |
| `cd.yml` | 115 | pinned-to-tag | `bervProject/railway-deploy@v0.2.4` |
| `cd.yml` | 122 | pinned-to-tag | `actions/create-release@v1` |
| `ci.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 22 | pinned-to-tag | `actions/setup-go@v4` |
| `ci.yml` | 36 | pinned-to-tag | `codecov/codecov-action@v3` |
| `ci.yml` | 43 | pinned-to-branch | `KooshaPari/phenotypeActions/.github/workflows/validate-governance.yml@main` |
| `coverage.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `coverage.yml` | 13 | pinned-to-tag | `codecov/codecov-action@v4` |
| `legacy-tooling-gate.yml` | 20 | pinned-to-tag | `actions/checkout@v4` |
| `legacy-tooling-gate.yml` | 23 | pinned-to-tag | `actions/checkout@v4` |
| `legacy-tooling-gate.yml` | 30 | pinned-to-tag | `actions/setup-python@v5` |
| `legacy-tooling-gate.yml` | 48 | pinned-to-tag | `actions/upload-artifact@v4` |
| `legacy-tooling-gate.yml` | 55 | pinned-to-tag | `actions/upload-artifact@v4` |
| `legacy-tooling-gate.yml` | 63 | pinned-to-tag | `actions/github-script@v7` |
| `quality-gate.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 35 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 38 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 41 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `quality-gate.yml` | 52 | pinned-to-tag | `codecov/codecov-action@v4` |
| `quality-gate.yml` | 72 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 75 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 78 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `quality-gate.yml` | 89 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 92 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 95 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `quality-gate.yml` | 104 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 142 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 185 | pinned-to-tag | `actions/github-script@v7` |
| `release.yml` | 21 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 27 | pinned-to-tag | `actions/setup-go@v4` |
| `release.yml` | 54 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 57 | pinned-to-branch | `KooshaPari/phenotypeActions/promote@main` |
| `sast.yml` | 11 | pinned-to-tag | `actions/checkout@v4` |
| `sast.yml` | 12 | pinned-to-tag | `github/codeql-action/init-action@v3` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |

### Apisync (43 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ci.yml` | 17 | pinned-to-branch | `KooshaPari/template-commons/.github/workflows/reusable-rust-ci.yml@main` |
| `ci.yml` | 24 | pinned-to-branch | `KooshaPari/template-commons/.github/workflows/reusable-security-scan.yml@main` |
| `ci.yml` | 32 | pinned-to-branch | `KooshaPari/phenotypeActions/.github/workflows/validate-governance.yml@main` |
| `coverage.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `coverage.yml` | 13 | pinned-to-tag | `codecov/codecov-action@v4` |
| `pages-deploy.yml` | 24 | pinned-to-tag | `actions/checkout@v4` |
| `pages-deploy.yml` | 29 | pinned-to-tag | `actions/configure-pages@v4` |
| `pages-deploy.yml` | 46 | pinned-to-tag | `actions/upload-pages-artifact@v3` |
| `pages-deploy.yml` | 60 | pinned-to-tag | `actions/deploy-pages@v4` |
| `quality-gate.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 35 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 38 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 41 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `quality-gate.yml` | 52 | pinned-to-tag | `codecov/codecov-action@v4` |
| `quality-gate.yml` | 72 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 75 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 78 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `quality-gate.yml` | 89 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 92 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 95 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `quality-gate.yml` | 104 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 142 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 185 | pinned-to-tag | `actions/github-script@v7` |
| `release.yml` | 21 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 27 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `release.yml` | 50 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 53 | pinned-to-branch | `KooshaPari/phenotypeActions/promote@main` |
| `sast.yml` | 11 | pinned-to-tag | `actions/checkout@v4` |
| `sast.yml` | 12 | pinned-to-tag | `github/codeql-action/init-action@v3` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `security-deep-scan.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 28 | pinned-to-tag | `github/codeql-action/upload-sarif@v2` |
| `security-deep-scan.yml` | 36 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 54 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 57 | pinned-to-tag | `github/codeql-action/init@v2` |
| `security-deep-scan.yml` | 62 | pinned-to-tag | `github/codeql-action/autobuild@v2` |
| `security-deep-scan.yml` | 65 | pinned-to-tag | `github/codeql-action/analyze@v2` |
| `security-deep-scan.yml` | 72 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 85 | pinned-to-tag | `github/codeql-action/upload-sarif@v2` |
| `security-guard.yml` | 12 | pinned-to-tag | `actions/checkout@v4` |

### Civis (40 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `cargo-deny.yml` | 22 | pinned-to-tag | `actions/checkout@v6` |
| `cargo-deny.yml` | 25 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `cargo-deny.yml` | 28 | pinned-to-tag | `EmbarkStudios/cargo-deny-action@v2` |
| `doc-links.yml` | 10 | pinned-to-tag | `actions/checkout@v4` |
| `docs-site.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `docs-site.yml` | 19 | pinned-to-tag | `actions/setup-node@v4` |
| `fr-coverage.yml` | 10 | pinned-to-tag | `actions/checkout@v4` |
| `legacy-tooling-gate.yml` | 23 | pinned-to-tag | `actions/checkout@v4` |
| `legacy-tooling-gate.yml` | 26 | pinned-to-tag | `actions/checkout@v4` |
| `legacy-tooling-gate.yml` | 33 | pinned-to-tag | `actions/setup-python@v5` |
| `legacy-tooling-gate.yml` | 51 | pinned-to-tag | `actions/upload-artifact@v4` |
| `legacy-tooling-gate.yml` | 58 | pinned-to-tag | `actions/upload-artifact@v4` |
| `legacy-tooling-gate.yml` | 66 | pinned-to-tag | `actions/github-script@v7` |
| `pages-deploy.yml` | 14 | pinned-to-tag | `actions/checkout@v4` |
| `pages-deploy.yml` | 15 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `pages-deploy.yml` | 22 | pinned-to-tag | `actions/configure-pages@v4` |
| `pages-deploy.yml` | 23 | pinned-to-tag | `actions/upload-pages-artifact@v3` |
| `pages-deploy.yml` | 34 | pinned-to-tag | `actions/deploy-pages@v4` |
| `pages.yml` | 26 | pinned-to-tag | `actions/checkout@v4` |
| `pages.yml` | 27 | pinned-to-tag | `actions/setup-node@v4` |
| `pages.yml` | 31 | pinned-to-tag | `actions/configure-pages@v5` |
| `pages.yml` | 36 | pinned-to-tag | `actions/upload-pages-artifact@v3` |
| `pages.yml` | 48 | pinned-to-tag | `actions/deploy-pages@v4` |
| `policy-gate.yml` | 17 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 11 | pinned-to-tag | `actions/checkout@v4` |
| `quality.yml` | 15 | pinned-to-tag | `actions/checkout@v4` |
| `quality.yml` | 16 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality.yml` | 27 | pinned-to-tag | `actions/checkout@v4` |
| `quality.yml` | 28 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `release-drafter.yml` | 12 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/release-drafter.yml@main` |
| `release.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 20 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `security-guard.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `security-guard.yml` | 23 | pinned-to-tag | `pre-commit/action@v3.0.1` |
| `self-merge-gate.yml` | 13 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/self-merge-gate.yml@main` |
| `tag-automation.yml` | 13 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/tag-automation.yml@main` |

### phenoResearchEngine (37 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ci.yml` | 9 | pinned-to-branch | `phenotype-dev/.github/.github/workflows/python-ci.yml@main` |
| `coverage.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `coverage.yml` | 13 | pinned-to-tag | `codecov/codecov-action@v4` |
| `quality-gate.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 35 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 38 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 41 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `quality-gate.yml` | 52 | pinned-to-tag | `codecov/codecov-action@v4` |
| `quality-gate.yml` | 72 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 75 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 78 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `quality-gate.yml` | 89 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 92 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 95 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `quality-gate.yml` | 104 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 142 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 185 | pinned-to-tag | `actions/github-script@v7` |
| `release.yml` | 21 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 27 | pinned-to-tag | `actions/setup-python@v4` |
| `release.yml` | 54 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 57 | pinned-to-branch | `KooshaPari/phenotypeActions/promote@main` |
| `sast.yml` | 11 | pinned-to-tag | `actions/checkout@v4` |
| `sast.yml` | 12 | pinned-to-tag | `github/codeql-action/init-action@v3` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `security-deep-scan.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 28 | pinned-to-tag | `github/codeql-action/upload-sarif@v2` |
| `security-deep-scan.yml` | 36 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 54 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 57 | pinned-to-tag | `github/codeql-action/init@v2` |
| `security-deep-scan.yml` | 62 | pinned-to-tag | `github/codeql-action/autobuild@v2` |
| `security-deep-scan.yml` | 65 | pinned-to-tag | `github/codeql-action/analyze@v2` |
| `security-deep-scan.yml` | 72 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 85 | pinned-to-tag | `github/codeql-action/upload-sarif@v2` |
| `security-guard.yml` | 12 | pinned-to-tag | `actions/checkout@v4` |

### hwLedger (37 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `agileplus.yml` | 25 | pinned-to-tag | `actions/checkout@v4` |
| `agileplus.yml` | 30 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `agileplus.yml` | 33 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `attestation-gate.yml` | 29 | pinned-to-tag | `actions/checkout@v4` |
| `attestation-gate.yml` | 33 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `attestation-gate.yml` | 35 | pinned-to-tag | `actions/cache@v4` |
| `cargo-deny.yml` | 22 | pinned-to-tag | `actions/checkout@v6` |
| `cargo-deny.yml` | 25 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `cargo-deny.yml` | 28 | pinned-to-tag | `EmbarkStudios/cargo-deny-action@v2` |
| `ci-local.yml` | 27 | pinned-to-tag | `actions/checkout@v4` |
| `docs.yml` | 32 | pinned-to-tag | `actions/checkout@v4` |
| `docs.yml` | 35 | pinned-to-tag | `oven-sh/setup-bun@v1` |
| `docs.yml` | 52 | pinned-to-tag | `actions/upload-pages-artifact@v3` |
| `docs.yml` | 71 | pinned-to-tag | `actions/deploy-pages@v4` |
| `journey-rich-render.yml` | 37 | pinned-to-tag | `actions/checkout@v4` |
| `journey-rich-render.yml` | 43 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `journey-rich-render.yml` | 52 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `journey-rich-render.yml` | 55 | pinned-to-tag | `actions/cache@v4` |
| `journey-rich-render.yml` | 81 | pinned-to-tag | `actions/upload-artifact@v4` |
| `journey-rich-render.yml` | 93 | pinned-to-tag | `peter-evans/create-pull-request@v6` |
| `openapi-check.yml` | 26 | pinned-to-tag | `actions/checkout@v4` |
| `openapi-check.yml` | 27 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `release.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 20 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `rust.yml` | 26 | pinned-to-tag | `actions/checkout@v4` |
| `rust.yml` | 27 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `rust.yml` | 35 | pinned-to-tag | `actions/checkout@v4` |
| `rust.yml` | 36 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `rust.yml` | 39 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `rust.yml` | 45 | pinned-to-tag | `actions/checkout@v4` |
| `rust.yml` | 46 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `rust.yml` | 47 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `rust.yml` | 56 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |

### KDesktopVirt (34 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ci.yml` | 32 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 41 | pinned-to-tag | `actions/cache@v4` |
| `ci.yml` | 88 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 91 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `ci.yml` | 108 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 111 | pinned-to-tag | `docker/setup-buildx-action@v3` |
| `ci.yml` | 115 | pinned-to-tag | `docker/login-action@v3` |
| `ci.yml` | 123 | pinned-to-tag | `docker/metadata-action@v5` |
| `ci.yml` | 134 | pinned-to-tag | `docker/build-push-action@v5` |
| `ci.yml` | 151 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 156 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `ci.yml` | 179 | pinned-to-tag | `softprops/action-gh-release@v1` |
| `ci.yml` | 197 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 200 | pinned-to-tag | `actions/setup-node@v4` |
| `ci.yml` | 215 | pinned-to-tag | `peaceiris/actions-gh-pages@v3` |
| `doc-links.yml` | 11 | pinned-to-tag | `actions/checkout@v4` |
| `fr-coverage.yml` | 11 | pinned-to-tag | `actions/checkout@v4` |
| `legacy-tooling-gate.yml` | 23 | pinned-to-tag | `actions/checkout@v4` |
| `legacy-tooling-gate.yml` | 26 | pinned-to-tag | `actions/checkout@v4` |
| `legacy-tooling-gate.yml` | 33 | pinned-to-tag | `actions/setup-python@v5` |
| `legacy-tooling-gate.yml` | 51 | pinned-to-tag | `actions/upload-artifact@v4` |
| `legacy-tooling-gate.yml` | 58 | pinned-to-tag | `actions/upload-artifact@v4` |
| `legacy-tooling-gate.yml` | 66 | pinned-to-tag | `actions/github-script@v7` |
| `pages-deploy.yml` | 27 | pinned-to-tag | `actions/checkout@v4` |
| `pages-deploy.yml` | 32 | pinned-to-tag | `actions/setup-node@v4` |
| `pages-deploy.yml` | 37 | pinned-to-tag | `actions/configure-pages@v5` |
| `pages-deploy.yml` | 40 | pinned-to-tag | `actions/cache@v4` |
| `pages-deploy.yml` | 62 | pinned-to-tag | `actions/upload-pages-artifact@v3` |
| `pages-deploy.yml` | 76 | pinned-to-tag | `actions/deploy-pages@v4` |
| `quality-gate.yml` | 12 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |

### phenodocs (33 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `alert-sync-issues.yml` | 21 | pinned-to-tag | `actions/github-script@v9` |
| `codeql.yml` | 24 | pinned-to-tag | `actions/checkout@v6` |
| `codeql.yml` | 27 | pinned-to-tag | `github/codeql-action/init@v4` |
| `codeql.yml` | 33 | pinned-to-tag | `github/codeql-action/analyze@v4` |
| `deploy.yml` | 25 | pinned-to-tag | `actions/checkout@v6` |
| `deploy.yml` | 28 | pinned-to-tag | `actions/setup-python@v6` |
| `deploy.yml` | 33 | pinned-to-tag | `astral-sh/setup-uv@v7` |
| `deploy.yml` | 41 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `deploy.yml` | 57 | pinned-to-tag | `actions/upload-pages-artifact@v5` |
| `deploy.yml` | 75 | pinned-to-tag | `actions/deploy-pages@v5` |
| `doc-links.yml` | 11 | pinned-to-tag | `actions/checkout@v6` |
| `doc-links.yml` | 12 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `fr-coverage.yml` | 11 | pinned-to-tag | `actions/checkout@v6` |
| `fr-coverage.yml` | 12 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `legacy-tooling-gate.yml` | 22 | pinned-to-tag | `actions/checkout@v6` |
| `legacy-tooling-gate.yml` | 25 | pinned-to-tag | `actions/checkout@v6` |
| `legacy-tooling-gate.yml` | 33 | pinned-to-tag | `actions/setup-python@v6` |
| `legacy-tooling-gate.yml` | 62 | pinned-to-tag | `actions/upload-artifact@v7` |
| `legacy-tooling-gate.yml` | 69 | pinned-to-tag | `actions/upload-artifact@v7` |
| `legacy-tooling-gate.yml` | 77 | pinned-to-tag | `actions/github-script@v9` |
| `policy-gate.yml` | 17 | pinned-to-tag | `actions/checkout@v6` |
| `publish-package.yml` | 19 | pinned-to-tag | `actions/checkout@v6` |
| `publish-package.yml` | 20 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `quality-gate.yml` | 12 | pinned-to-tag | `actions/checkout@v6` |
| `quality-gate.yml` | 13 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v6` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.3` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v7` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v4` |
| `security-guard-hook-audit.yml` | 18 | pinned-to-tag | `actions/checkout@v6` |
| `security-guard.yml` | 18 | pinned-to-tag | `actions/checkout@v6` |
| `security-guard.yml` | 23 | pinned-to-tag | `actions/setup-python@v6` |
| `security-guard.yml` | 28 | pinned-to-tag | `astral-sh/setup-uv@v7` |

### nanovms (32 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ai-testing.yml` | 27 | pinned-to-tag | `actions/checkout@v4` |
| `ai-testing.yml` | 30 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `ai-testing.yml` | 39 | pinned-to-tag | `actions/checkout@v4` |
| `ai-testing.yml` | 42 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `ai-testing.yml` | 50 | pinned-to-tag | `actions/upload-artifact@v4` |
| `ai-testing.yml` | 59 | pinned-to-tag | `actions/checkout@v4` |
| `ai-testing.yml` | 62 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `ai-testing.yml` | 74 | pinned-to-tag | `actions/checkout@v4` |
| `ai-testing.yml` | 77 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `ai-testing.yml` | 89 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 20 | pinned-to-branch | `KooshaPari/template-commons/.github/workflows/reusable-typescript-ci.yml@main` |
| `ci.yml` | 27 | pinned-to-branch | `KooshaPari/template-commons/.github/workflows/reusable-security-scan.yml@main` |
| `ci.yml` | 35 | pinned-to-branch | `KooshaPari/phenotypeActions/.github/workflows/validate-governance.yml@main` |
| `coverage.yml` | 10 | pinned-to-tag | `actions/checkout@v4` |
| `coverage.yml` | 16 | pinned-to-tag | `codecov/codecov-action@v4` |
| `pages-deploy.yml` | 20 | pinned-to-tag | `actions/checkout@v4` |
| `pages-deploy.yml` | 21 | pinned-to-tag | `actions/setup-node@v4` |
| `pages-deploy.yml` | 26 | pinned-to-tag | `actions/upload-pages-artifact@v3` |
| `pages-deploy.yml` | 29 | pinned-to-tag | `actions/deploy-pages@v4` |
| `quality-gate.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |
| `sast.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `sast.yml` | 19 | pinned-to-tag | `github/codeql-action/init-action@v3` |
| `security-deep-scan.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 34 | pinned-to-tag | `github/codeql-action/upload-sarif@v2` |
| `security-deep-scan.yml` | 42 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 64 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 67 | pinned-to-tag | `github/codeql-action/init@v2` |
| `security-deep-scan.yml` | 72 | pinned-to-tag | `github/codeql-action/autobuild@v2` |
| `security-deep-scan.yml` | 75 | pinned-to-tag | `github/codeql-action/analyze@v2` |
| `security-deep-scan.yml` | 85 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 98 | pinned-to-tag | `github/codeql-action/upload-sarif@v2` |
| `security-guard.yml` | 15 | pinned-to-tag | `actions/checkout@v4` |

### helios-router (30 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `cpu-profiling.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |
| `cpu-profiling.yml` | 19 | pinned-to-tag | `actions/setup-python@v5` |
| `cpu-profiling.yml` | 64 | pinned-to-tag | `actions/checkout@v4` |
| `cpu-profiling.yml` | 67 | pinned-to-tag | `actions/setup-python@v5` |
| `cpu-profiling.yml` | 100 | pinned-to-tag | `actions/checkout@v4` |
| `cpu-profiling.yml` | 103 | pinned-to-tag | `actions/setup-python@v5` |
| `docs-site.yml` | 21 | pinned-to-tag | `actions/checkout@v4` |
| `docs-site.yml` | 22 | pinned-to-tag | `actions/setup-node@v4` |
| `leak-detection.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `leak-detection.yml` | 22 | pinned-to-tag | `actions/setup-python@v5` |
| `leak-detection.yml` | 65 | pinned-to-tag | `actions/checkout@v4` |
| `leak-detection.yml` | 68 | pinned-to-tag | `actions/setup-python@v5` |
| `leak-detection.yml` | 108 | pinned-to-tag | `actions/checkout@v4` |
| `leak-detection.yml` | 111 | pinned-to-tag | `actions/setup-python@v5` |
| `network-optimization.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |
| `network-optimization.yml` | 19 | pinned-to-tag | `actions/setup-python@v5` |
| `network-optimization.yml` | 56 | pinned-to-tag | `actions/checkout@v4` |
| `network-optimization.yml` | 59 | pinned-to-tag | `actions/setup-python@v5` |
| `network-optimization.yml` | 97 | pinned-to-tag | `actions/checkout@v4` |
| `network-optimization.yml` | 100 | pinned-to-tag | `actions/setup-python@v5` |
| `pages.yml` | 26 | pinned-to-tag | `actions/checkout@v4` |
| `pages.yml` | 27 | pinned-to-tag | `actions/setup-node@v4` |
| `pages.yml` | 32 | pinned-to-tag | `actions/configure-pages@v5` |
| `pages.yml` | 39 | pinned-to-tag | `actions/upload-pages-artifact@v3` |
| `pages.yml` | 51 | pinned-to-tag | `actions/deploy-pages@v4` |
| `policy-gate.yml` | 17 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |

### BytePort (27 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `cargo-deny.yml` | 23 | pinned-to-tag | `actions/checkout@v6` |
| `cargo-deny.yml` | 26 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `cargo-deny.yml` | 29 | pinned-to-tag | `EmbarkStudios/cargo-deny-action@v2` |
| `ci.yaml` | 26 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yaml` | 28 | pinned-to-tag | `actions/setup-go@v6` |
| `ci.yaml` | 49 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yaml` | 51 | pinned-to-tag | `actions/setup-go@v6` |
| `ci.yaml` | 67 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yaml` | 69 | pinned-to-tag | `actions/setup-go@v6` |
| `codeql.yml` | 27 | pinned-to-tag | `actions/checkout@v6` |
| `codeql.yml` | 28 | pinned-to-tag | `github/codeql-action/init@v4` |
| `codeql.yml` | 31 | pinned-to-tag | `github/codeql-action/autobuild@v4` |
| `codeql.yml` | 32 | pinned-to-tag | `github/codeql-action/analyze@v4` |
| `go-ci.yml` | 22 | pinned-to-tag | `actions/checkout@v6` |
| `go-ci.yml` | 23 | pinned-to-tag | `actions/setup-go@v6` |
| `legacy-tooling-gate.yml` | 23 | pinned-to-tag | `actions/checkout@v6` |
| `legacy-tooling-gate.yml` | 26 | pinned-to-tag | `actions/checkout@v6` |
| `legacy-tooling-gate.yml` | 33 | pinned-to-tag | `actions/setup-python@v6` |
| `legacy-tooling-gate.yml` | 51 | pinned-to-tag | `actions/upload-artifact@v7` |
| `legacy-tooling-gate.yml` | 58 | pinned-to-tag | `actions/upload-artifact@v7` |
| `legacy-tooling-gate.yml` | 66 | pinned-to-tag | `actions/github-script@v9` |
| `sbom-refresh.yml` | 12 | pinned-to-branch | `KooshaPari/phenotype-tooling/.github/workflows/sbom-monthly.yml@main` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v6` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.3` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v7` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v4` |
| `secrets-scan.yml` | 15 | pinned-to-tag | `actions/checkout@v6` |

### phenoShared (27 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `alert-sync-issues.yml` | 32 | pinned-to-tag | `actions/github-script@v7` |
| `codeql.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `codeql.yml` | 23 | pinned-to-tag | `github/codeql-action/init@v3` |
| `codeql.yml` | 26 | pinned-to-tag | `github/codeql-action/analyze@v3` |
| `docs-deploy.yml` | 21 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/vitepress-pages.yml@main` |
| `legacy-tooling-gate.yml` | 93 | pinned-to-tag | `actions/checkout@v4` |
| `legacy-tooling-gate.yml` | 108 | pinned-to-tag | `actions/checkout@v4` |
| `legacy-tooling-gate.yml` | 117 | pinned-to-tag | `actions/setup-python@v5` |
| `legacy-tooling-gate.yml` | 165 | pinned-to-tag | `actions/upload-artifact@v4` |
| `legacy-tooling-gate.yml` | 177 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `legacy-tooling-gate.yml` | 184 | pinned-to-tag | `actions/github-script@v7` |
| `release.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 20 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `reusable-release-drafter.yml` | 33 | pinned-to-tag | `release-drafter/release-drafter@v6` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `secrets-scan.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |
| `security-guard-hook-audit.yml` | 30 | pinned-to-tag | `actions/checkout@v6` |
| `self-merge-gate.yml` | 29 | pinned-to-tag | `actions/checkout@v4` |
| `tag-automation.yml` | 36 | pinned-to-tag | `actions/checkout@v4` |
| `vitepress-pages.yml` | 40 | pinned-to-tag | `actions/checkout@v4` |
| `vitepress-pages.yml` | 43 | pinned-to-tag | `oven-sh/setup-bun@v2` |
| `vitepress-pages.yml` | 46 | pinned-to-tag | `actions/configure-pages@v5` |
| `vitepress-pages.yml` | 59 | pinned-to-tag | `actions/upload-pages-artifact@v4` |
| `vitepress-pages.yml` | 72 | pinned-to-tag | `actions/deploy-pages@v4` |

### Tokn (23 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `bench-perf-gate.yml` | 37 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `benchmark.yml` | 24 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `ci.yml` | 20 | pinned-to-branch | `KooshaPari/template-commons/.github/workflows/reusable-rust-ci.yml@main` |
| `ci.yml` | 27 | pinned-to-branch | `KooshaPari/template-commons/.github/workflows/reusable-security-scan.yml@main` |
| `ci.yml` | 35 | pinned-to-branch | `KooshaPari/phenotypeActions/.github/workflows/validate-governance.yml@main` |
| `pages-deploy.yml` | 25 | pinned-to-tag | `actions/checkout@v4` |
| `pages-deploy.yml` | 30 | pinned-to-tag | `actions/setup-node@v4` |
| `pages-deploy.yml` | 35 | pinned-to-tag | `actions/configure-pages@v5` |
| `pages-deploy.yml` | 38 | pinned-to-tag | `actions/cache@v4` |
| `pages-deploy.yml` | 57 | pinned-to-tag | `actions/upload-pages-artifact@v3` |
| `pages-deploy.yml` | 71 | pinned-to-tag | `actions/deploy-pages@v4` |
| `pricing-governance-check.yml` | 41 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 23 | unpinned-other-ref | `dtolnay/rust-action@stable` |
| `quality-gate.yml` | 45 | unpinned-other-ref | `dtolnay/rust-action@stable` |
| `release-drafter.yml` | 14 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/release-drafter.yml@main` |
| `release.yml` | 26 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `release.yml` | 50 | pinned-to-branch | `KooshaPari/phenotypeActions/promote@main` |
| `sbom-refresh.yml` | 12 | pinned-to-branch | `KooshaPari/phenotype-tooling/.github/workflows/sbom-monthly.yml@main` |
| `security-deep-scan.yml` | 21 | pinned-to-branch | `aquasecurity/trivy-action@master` |
| `security-deep-scan.yml` | 67 | pinned-to-branch | `aquasecurity/trivy-action@master` |
| `security.yml` | 23 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `security.yml` | 26 | unpinned-other-ref | `rustsec/audit-check@{"message":"Not` |
| `security.yml` | 30 | unpinned-other-ref | `cargo-bins/cargo-deny-action@{"message":"Not` |

### phenoDesign (23 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ci.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |
| `legacy-tooling-gate.yml` | 23 | pinned-to-tag | `actions/checkout@v4` |
| `legacy-tooling-gate.yml` | 26 | pinned-to-tag | `actions/checkout@v4` |
| `legacy-tooling-gate.yml` | 33 | pinned-to-tag | `actions/setup-python@v5` |
| `legacy-tooling-gate.yml` | 51 | pinned-to-tag | `actions/upload-artifact@v4` |
| `legacy-tooling-gate.yml` | 58 | pinned-to-tag | `actions/upload-artifact@v4` |
| `legacy-tooling-gate.yml` | 66 | pinned-to-tag | `actions/github-script@v7` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `security-guard.yml` | 14 | pinned-to-tag | `actions/checkout@v6` |
| `security-guard.yml` | 19 | pinned-to-tag | `pre-commit/action@v3.0.1` |
| `security.yml` | 27 | pinned-to-tag | `actions/checkout@v4` |
| `security.yml` | 32 | pinned-to-tag | `gitleaks/gitleaks-action@v2` |
| `security.yml` | 46 | pinned-to-tag | `actions/checkout@v4` |
| `security.yml` | 50 | pinned-to-tag | `actions/setup-node@v5` |
| `security.yml` | 61 | pinned-to-tag | `returntocorp/semgrep-action@v1` |
| `security.yml` | 76 | pinned-to-tag | `actions/checkout@v4` |
| `security.yml` | 80 | pinned-to-tag | `actions/setup-node@v5` |
| `security.yml` | 98 | pinned-to-tag | `actions/checkout@v4` |
| `security.yml` | 104 | pinned-to-branch | `aquasecurity/trivy-action@master` |
| `security.yml` | 111 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |

### MCPForge (22 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `doc-links.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `fr-coverage.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `go.yml` | 15 | pinned-to-tag | `actions/checkout@v4` |
| `go.yml` | 18 | pinned-to-tag | `actions/setup-go@v5` |
| `go.yml` | 43 | pinned-to-tag | `actions/checkout@v4` |
| `go.yml` | 46 | pinned-to-tag | `actions/setup-go@v5` |
| `go.yml` | 62 | pinned-to-tag | `actions/checkout@v4` |
| `go.yml` | 65 | pinned-to-tag | `actions/setup-go@v5` |
| `go.yml` | 72 | pinned-to-tag | `actions/setup-python@v5` |
| `go.yml` | 86 | pinned-to-tag | `actions/checkout@v4` |
| `go.yml` | 89 | pinned-to-tag | `actions/setup-go@v5` |
| `go.yml` | 96 | pinned-to-tag | `actions-rs/toolchain@v1` |
| `go.yml` | 115 | pinned-to-tag | `actions/checkout@v4` |
| `go.yml` | 118 | pinned-to-tag | `actions/setup-go@v5` |
| `go.yml` | 125 | pinned-to-tag | `actions/setup-node@v4` |
| `go.yml` | 139 | pinned-to-tag | `actions/checkout@v4` |
| `go.yml` | 142 | pinned-to-tag | `actions/setup-go@v5` |
| `quality-gate.yml` | 8 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |

### phenotype-infra (22 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ansible-lint.yml` | 16 | pinned-to-tag | `actions/checkout@v6` |
| `doc-links.yml` | 7 | pinned-to-tag | `actions/checkout@v6` |
| `docs-check.yml` | 17 | pinned-to-tag | `actions/checkout@v6` |
| `docs-check.yml` | 18 | pinned-to-tag | `DavidAnson/markdownlint-cli2-action@v23` |
| `docs-check.yml` | 27 | pinned-to-tag | `actions/checkout@v6` |
| `docs-lint.yml` | 14 | pinned-to-tag | `actions/checkout@v6` |
| `docs-lint.yml` | 17 | unpinned-other-ref | `errata-ai/vale-action@reviewdog` |
| `docs-lint.yml` | 30 | pinned-to-tag | `actions/checkout@v6` |
| `fr-coverage.yml` | 7 | pinned-to-tag | `actions/checkout@v6` |
| `iac-rust.yml` | 37 | pinned-to-tag | `actions/checkout@v6` |
| `iac-rust.yml` | 40 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `iac-rust.yml` | 45 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `iac-rust.yml` | 66 | pinned-to-tag | `actions/checkout@v6` |
| `iac-rust.yml` | 69 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `iac-rust.yml` | 74 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `quality-gate.yml` | 8 | pinned-to-tag | `actions/checkout@v6` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v6` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.3` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v7` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v4` |
| `terraform-plan.yml` | 26 | pinned-to-tag | `actions/checkout@v6` |
| `terraform-plan.yml` | 29 | pinned-to-tag | `hashicorp/setup-terraform@v4` |

### vibeproxy-monitoring-unified (21 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ci.yml` | 14 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 20 | pinned-to-branch | `KooshaPari/phenotypeActions/.github/workflows/validate-governance.yml@main` |
| `doc-links.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `fr-coverage.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 21 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 31 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 34 | pinned-to-branch | `KooshaPari/phenotypeActions/promote@main` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `secrets-scan.yml` | 15 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 28 | pinned-to-tag | `github/codeql-action/upload-sarif@v2` |
| `security-deep-scan.yml` | 36 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 54 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 57 | pinned-to-tag | `github/codeql-action/init@v2` |
| `security-deep-scan.yml` | 62 | pinned-to-tag | `github/codeql-action/autobuild@v2` |
| `security-deep-scan.yml` | 65 | pinned-to-tag | `github/codeql-action/analyze@v2` |
| `security-deep-scan.yml` | 72 | pinned-to-tag | `actions/checkout@v4` |
| `security-deep-scan.yml` | 85 | pinned-to-tag | `github/codeql-action/upload-sarif@v2` |

### Configra (21 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `cargo-deny.yml` | 22 | pinned-to-tag | `actions/checkout@v6` |
| `cargo-deny.yml` | 25 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `cargo-deny.yml` | 28 | pinned-to-tag | `EmbarkStudios/cargo-deny-action@v2` |
| `docs-deploy.yml` | 21 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/vitepress-pages.yml@main` |
| `policy-gate.yml` | 17 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `release-drafter.yml` | 12 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/release-drafter.yml@main` |
| `release.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 20 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `reusable-policy-gate.yml` | 28 | pinned-to-tag | `actions/checkout@v4` |
| `reusable-policy-gate.yml` | 32 | pinned-to-tag | `actions/github-script@v7` |
| `reusable-policy-gate.yml` | 89 | pinned-to-tag | `actions/upload-artifact@v4` |
| `reusable-policy-gate.yml` | 99 | pinned-to-tag | `actions/checkout@v4` |
| `reusable-policy-gate.yml` | 102 | pinned-to-tag | `errata-ai/vale-action@v2` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `security-guard.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `self-merge-gate.yml` | 10 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/self-merge-gate.yml@main` |
| `tag-automation.yml` | 13 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/tag-automation.yml@main` |

### PhenoProc (19 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ci.yml` | 17 | pinned-to-branch | `KooshaPari/template-commons/.github/workflows/reusable-rust-ci.yml@main` |
| `ci.yml` | 24 | pinned-to-branch | `KooshaPari/template-commons/.github/workflows/reusable-security-scan.yml@main` |
| `ci.yml` | 32 | pinned-to-branch | `KooshaPari/phenotypeActions/.github/workflows/validate-governance.yml@main` |
| `doc-links.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `fr-coverage.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `legacy-tooling-gate.yml` | 20 | pinned-to-tag | `actions/checkout@v4` |
| `legacy-tooling-gate.yml` | 23 | pinned-to-tag | `actions/checkout@v4` |
| `legacy-tooling-gate.yml` | 30 | pinned-to-tag | `actions/setup-python@v5` |
| `legacy-tooling-gate.yml` | 48 | pinned-to-tag | `actions/upload-artifact@v4` |
| `legacy-tooling-gate.yml` | 55 | pinned-to-tag | `actions/upload-artifact@v4` |
| `legacy-tooling-gate.yml` | 63 | pinned-to-tag | `actions/github-script@v7` |
| `pages-deploy.yml` | 20 | pinned-to-tag | `actions/checkout@v4` |
| `pages-deploy.yml` | 21 | pinned-to-tag | `actions/configure-pages@v5` |
| `pages-deploy.yml` | 22 | pinned-to-tag | `actions/setup-node@v4` |
| `pages-deploy.yml` | 31 | pinned-to-tag | `actions/upload-pages-artifact@v3` |
| `pages-deploy.yml` | 35 | pinned-to-tag | `actions/deploy-pages@v4` |
| `quality-gate.yml` | 8 | pinned-to-tag | `actions/checkout@v4` |
| `secrets-scan.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |
| `secrets-scan.yml` | 19 | pinned-to-branch | `trufflesecurity/trufflehog@main` |

### Tracely (19 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ci.yml` | 20 | pinned-to-branch | `KooshaPari/template-commons/.github/workflows/reusable-rust-ci.yml@main` |
| `ci.yml` | 27 | pinned-to-branch | `KooshaPari/template-commons/.github/workflows/reusable-security-scan.yml@main` |
| `ci.yml` | 35 | pinned-to-branch | `KooshaPari/phenotypeActions/.github/workflows/validate-governance.yml@main` |
| `doc-links.yml` | 11 | pinned-to-tag | `actions/checkout@v4` |
| `doc-links.yml` | 12 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `fr-coverage.yml` | 11 | pinned-to-tag | `actions/checkout@v4` |
| `fr-coverage.yml` | 12 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `legacy-tooling-gate.yml` | 23 | pinned-to-tag | `actions/checkout@v4` |
| `legacy-tooling-gate.yml` | 26 | pinned-to-tag | `actions/checkout@v4` |
| `legacy-tooling-gate.yml` | 33 | pinned-to-tag | `actions/setup-python@v5` |
| `legacy-tooling-gate.yml` | 51 | pinned-to-tag | `actions/upload-artifact@v4` |
| `legacy-tooling-gate.yml` | 58 | pinned-to-tag | `actions/upload-artifact@v4` |
| `legacy-tooling-gate.yml` | 66 | pinned-to-tag | `actions/github-script@v7` |
| `quality-gate.yml` | 12 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 13 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |

### agent-devops-setups (18 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `pages-deploy.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |
| `pages-deploy.yml` | 17 | pinned-to-tag | `actions/configure-pages@v4` |
| `pages-deploy.yml` | 18 | pinned-to-tag | `actions/upload-pages-artifact@v3` |
| `pages-deploy.yml` | 22 | pinned-to-tag | `actions/deploy-pages@v4` |
| `policy-gate.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `release-drafter.yml` | 12 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/release-drafter.yml@main` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `security-guard.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `security-guard.yml` | 23 | pinned-to-tag | `pre-commit/action@v3` |
| `security-guard.yml` | 31 | pinned-to-tag | `actions/checkout@v4` |
| `security-guard.yml` | 40 | pinned-to-tag | `pre-commit/action@v3` |
| `self-merge-gate.yml` | 10 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/self-merge-gate.yml@main` |
| `tag-automation.yml` | 13 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/tag-automation.yml@main` |
| `validate-policy.yml` | 12 | pinned-to-tag | `actions/checkout@v4` |

### GDK (17 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `coverage.yml` | 15 | pinned-to-branch | `KooshaPari/phenotype-infrakit/.github/workflows/coverage.yml@main` |
| `doc-links.yml` | 10 | pinned-to-tag | `actions/checkout@v4` |
| `fr-coverage.yml` | 10 | pinned-to-tag | `actions/checkout@v4` |
| `legacy-tooling-gate.yml` | 23 | pinned-to-tag | `actions/checkout@v6` |
| `legacy-tooling-gate.yml` | 26 | pinned-to-tag | `actions/checkout@v6` |
| `legacy-tooling-gate.yml` | 33 | pinned-to-tag | `actions/setup-python@v6` |
| `legacy-tooling-gate.yml` | 51 | pinned-to-tag | `actions/upload-artifact@v7` |
| `legacy-tooling-gate.yml` | 58 | pinned-to-tag | `actions/upload-artifact@v7` |
| `legacy-tooling-gate.yml` | 66 | pinned-to-tag | `actions/github-script@v9` |
| `quality-gate.yml` | 13 | pinned-to-branch | `KooshaPari/phenotype-infrakit/.github/workflows/quality-gate.yml@main` |
| `release.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 20 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `secrets-scan.yml` | 15 | pinned-to-tag | `actions/checkout@v4` |

### DINOForge-UnityDoorstop (17 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `build-be.yml` | 11 | pinned-to-tag | `actions/checkout@v4` |
| `build-be.yml` | 39 | pinned-to-tag | `actions/upload-artifact@v4` |
| `build-be.yml` | 45 | pinned-to-tag | `actions/upload-artifact@v4` |
| `build-be.yml` | 60 | pinned-to-tag | `actions/checkout@v4` |
| `build-be.yml` | 97 | pinned-to-tag | `actions/upload-artifact@v4` |
| `build-be.yml` | 103 | pinned-to-tag | `actions/upload-artifact@v4` |
| `build-be.yml` | 109 | pinned-to-tag | `actions/upload-artifact@v4` |
| `build-be.yml` | 120 | pinned-to-tag | `actions/checkout@v4` |
| `build-be.yml` | 146 | pinned-to-tag | `actions/upload-artifact@v4` |
| `build-be.yml` | 152 | pinned-to-tag | `actions/upload-artifact@v4` |
| `build-be.yml` | 158 | pinned-to-tag | `actions/upload-artifact@v4` |
| `build-be.yml` | 174 | pinned-to-tag | `actions/download-artifact@v4` |
| `build-be.yml` | 191 | unpinned-other-ref | `marvinpinto/action-automatic-releases@latest` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |

### Parpoura (16 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `docs-site.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `docs-site.yml` | 19 | pinned-to-tag | `actions/setup-node@v4` |
| `pages.yml` | 26 | pinned-to-tag | `actions/checkout@v4` |
| `pages.yml` | 27 | pinned-to-tag | `actions/setup-node@v4` |
| `pages.yml` | 31 | pinned-to-tag | `actions/configure-pages@v6` |
| `pages.yml` | 36 | pinned-to-tag | `actions/upload-pages-artifact@v5` |
| `pages.yml` | 48 | pinned-to-tag | `actions/deploy-pages@v5` |
| `policy-gate.yml` | 17 | pinned-to-tag | `actions/checkout@v4` |
| `quality.yml` | 12 | pinned-to-tag | `actions/checkout@v4` |
| `quality.yml` | 13 | pinned-to-tag | `actions/setup-node@v4` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `security-guard.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `security-guard.yml` | 23 | pinned-to-tag | `pre-commit/action@v3.0.1` |

### Httpora (16 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ci.yml` | 21 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 25 | pinned-to-tag | `actions/setup-python@v6` |
| `ci.yml` | 45 | pinned-to-branch | `KooshaPari/phenotypeActions/.github/workflows/validate-governance.yml@main` |
| `pages-deploy.yml` | 24 | pinned-to-tag | `actions/checkout@v6` |
| `pages-deploy.yml` | 29 | pinned-to-tag | `actions/configure-pages@v4` |
| `pages-deploy.yml` | 46 | pinned-to-tag | `actions/upload-pages-artifact@v5` |
| `pages-deploy.yml` | 60 | pinned-to-tag | `actions/deploy-pages@v5` |
| `release.yml` | 21 | pinned-to-tag | `actions/checkout@v6` |
| `release.yml` | 27 | pinned-to-tag | `actions/setup-python@v6` |
| `release.yml` | 54 | pinned-to-tag | `actions/checkout@v6` |
| `release.yml` | 57 | pinned-to-branch | `KooshaPari/phenotypeActions/promote@main` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v6` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.3` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `secrets-scan.yml` | 18 | pinned-to-tag | `actions/checkout@v6` |

### phenoAI (16 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `codeql.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `codeql.yml` | 23 | pinned-to-tag | `github/codeql-action/init@v3` |
| `codeql.yml` | 26 | pinned-to-tag | `github/codeql-action/analyze@v3` |
| `doc-links.yml` | 11 | pinned-to-tag | `actions/checkout@v4` |
| `doc-links.yml` | 12 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `fr-coverage.yml` | 11 | pinned-to-tag | `actions/checkout@v4` |
| `fr-coverage.yml` | 12 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 12 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 13 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `release.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 20 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `secrets-scan.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |

### PhenoHandbook (16 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `doc-links.yml` | 11 | pinned-to-tag | `actions/checkout@v4` |
| `doc-links.yml` | 12 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `fr-coverage.yml` | 11 | pinned-to-tag | `actions/checkout@v4` |
| `fr-coverage.yml` | 12 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `legacy-tooling-gate.yml` | 23 | pinned-to-tag | `actions/checkout@v6` |
| `legacy-tooling-gate.yml` | 26 | pinned-to-tag | `actions/checkout@v6` |
| `legacy-tooling-gate.yml` | 33 | pinned-to-tag | `actions/setup-python@v6` |
| `legacy-tooling-gate.yml` | 51 | pinned-to-tag | `actions/upload-artifact@v7` |
| `legacy-tooling-gate.yml` | 58 | pinned-to-tag | `actions/upload-artifact@v7` |
| `legacy-tooling-gate.yml` | 66 | pinned-to-tag | `actions/github-script@v9` |
| `quality-gate.yml` | 12 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 13 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v6` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.3` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v7` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v4` |

### PhenoObservability (16 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `cargo-deny.yml` | 62 | pinned-to-tag | `EmbarkStudios/cargo-deny-action@v2` |
| `ci.yml` | 15 | pinned-to-branch | `KooshaPari/phenotype-infrakit/.github/workflows/ci.yaml@main` |
| `coverage.yml` | 15 | pinned-to-branch | `KooshaPari/phenotype-infrakit/.github/workflows/coverage.yml@main` |
| `doc-links.yml` | 10 | pinned-to-tag | `actions/checkout@v4` |
| `fr-coverage.yml` | 10 | pinned-to-tag | `actions/checkout@v4` |
| `publish.yml` | 19 | pinned-to-branch | `KooshaPari/phenotype-infrakit/.github/workflows/publish-crate.yml@main` |
| `quality-gate.yml` | 11 | pinned-to-tag | `actions/checkout@v4` |
| `sbom-refresh.yml` | 12 | pinned-to-branch | `KooshaPari/phenotype-tooling/.github/workflows/sbom-monthly.yml@main` |
| `scorecard.yml` | 27 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 30 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 36 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 42 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `test.yml` | 59 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `test.yml` | 60 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `test.yml` | 114 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `test.yml` | 118 | pinned-to-tag | `codecov/codecov-action@v4` |

### Agentora (15 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ci.yml` | 20 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 22 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `ci.yml` | 24 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 32 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 34 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `ci.yml` | 38 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 46 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 48 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `ci.yml` | 50 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `ci.yml` | 58 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 60 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `pages-deploy.yml` | 24 | pinned-to-tag | `actions/checkout@v6` |
| `pages-deploy.yml` | 29 | pinned-to-tag | `actions/configure-pages@v6` |
| `pages-deploy.yml` | 47 | pinned-to-tag | `actions/upload-pages-artifact@v5` |
| `pages-deploy.yml` | 61 | pinned-to-tag | `actions/deploy-pages@v5` |

### AuthKit (15 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ci.yml` | 17 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 19 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `ci.yml` | 30 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 32 | pinned-to-tag | `actions/setup-python@v6` |
| `ci.yml` | 36 | pinned-to-tag | `snok/install-poetry@v1` |
| `ci.yml` | 44 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 46 | pinned-to-tag | `actions/setup-go@v6` |
| `ci.yml` | 56 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 58 | pinned-to-tag | `actions/setup-node@v6` |
| `codeql.yml` | 40 | pinned-to-tag | `actions/checkout@v6` |
| `codeql.yml` | 41 | pinned-to-tag | `github/codeql-action/init@v4` |
| `codeql.yml` | 51 | pinned-to-tag | `github/codeql-action/analyze@v4` |
| `doc-links.yml` | 10 | pinned-to-tag | `actions/checkout@v6` |
| `fr-coverage.yml` | 10 | pinned-to-tag | `actions/checkout@v6` |
| `quality-gate.yml` | 11 | pinned-to-tag | `actions/checkout@v6` |

### PhenoPlugins (15 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `cargo-deny.yml` | 23 | pinned-to-tag | `actions/checkout@v6` |
| `cargo-deny.yml` | 26 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `cargo-deny.yml` | 29 | pinned-to-tag | `EmbarkStudios/cargo-deny-action@v2` |
| `ci.yml` | 20 | pinned-to-branch | `KooshaPari/template-commons/.github/workflows/reusable-rust-ci.yml@main` |
| `ci.yml` | 27 | pinned-to-branch | `KooshaPari/template-commons/.github/workflows/reusable-security-scan.yml@main` |
| `ci.yml` | 35 | pinned-to-branch | `KooshaPari/phenotypeActions/.github/workflows/validate-governance.yml@main` |
| `doc-links.yml` | 10 | pinned-to-tag | `actions/checkout@v6` |
| `fr-coverage.yml` | 10 | pinned-to-tag | `actions/checkout@v6` |
| `legacy-tooling-gate.yml` | 23 | pinned-to-tag | `actions/checkout@v6` |
| `legacy-tooling-gate.yml` | 26 | pinned-to-tag | `actions/checkout@v6` |
| `legacy-tooling-gate.yml` | 33 | pinned-to-tag | `actions/setup-python@v6` |
| `legacy-tooling-gate.yml` | 51 | pinned-to-tag | `actions/upload-artifact@v7` |
| `legacy-tooling-gate.yml` | 58 | pinned-to-tag | `actions/upload-artifact@v7` |
| `legacy-tooling-gate.yml` | 66 | pinned-to-tag | `actions/github-script@v9` |
| `quality-gate.yml` | 11 | pinned-to-tag | `actions/checkout@v6` |

### PhenoVCS (15 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ci.yml` | 20 | pinned-to-branch | `KooshaPari/template-commons/.github/workflows/reusable-rust-ci.yml@main` |
| `ci.yml` | 27 | pinned-to-branch | `KooshaPari/template-commons/.github/workflows/reusable-security-scan.yml@main` |
| `ci.yml` | 35 | pinned-to-branch | `KooshaPari/phenotypeActions/.github/workflows/validate-governance.yml@main` |
| `legacy-tooling-gate.yml` | 23 | pinned-to-tag | `actions/checkout@v6` |
| `legacy-tooling-gate.yml` | 26 | pinned-to-tag | `actions/checkout@v6` |
| `legacy-tooling-gate.yml` | 33 | pinned-to-tag | `actions/setup-python@v6` |
| `legacy-tooling-gate.yml` | 51 | pinned-to-tag | `actions/upload-artifact@v7` |
| `legacy-tooling-gate.yml` | 58 | pinned-to-tag | `actions/upload-artifact@v7` |
| `legacy-tooling-gate.yml` | 66 | pinned-to-tag | `actions/github-script@v9` |
| `release.yml` | 19 | pinned-to-tag | `actions/checkout@v6` |
| `release.yml` | 20 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v6` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.3` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v7` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v4` |

### McpKit (14 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ci.yml` | 17 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 19 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `ci.yml` | 30 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 32 | pinned-to-tag | `actions/setup-python@v6` |
| `ci.yml` | 36 | pinned-to-tag | `snok/install-poetry@v1` |
| `ci.yml` | 44 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 46 | pinned-to-tag | `actions/setup-go@v6` |
| `ci.yml` | 56 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 58 | pinned-to-tag | `actions/setup-node@v6` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v6` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.3` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v7` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v4` |
| `secrets-scan.yml` | 15 | pinned-to-tag | `actions/checkout@v6` |

### PhenoCompose (14 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `codeql.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `codeql.yml` | 23 | pinned-to-tag | `github/codeql-action/init@v3` |
| `codeql.yml` | 26 | pinned-to-tag | `github/codeql-action/analyze@v3` |
| `doc-links.yml` | 11 | pinned-to-tag | `actions/checkout@v4` |
| `doc-links.yml` | 12 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `fr-coverage.yml` | 11 | pinned-to-tag | `actions/checkout@v4` |
| `fr-coverage.yml` | 12 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 12 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 13 | pinned-to-tag | `oven-sh/setup-bun@v1` |
| `scorecard.yml` | 27 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 30 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 36 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 42 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `secrets-scan.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |

### PhenoKits (14 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ci.yml` | 12 | pinned-to-branch | `KooshaPari/phenotype-infrakit/.github/workflows/ci.yaml@main` |
| `codeql.yml` | 27 | pinned-to-tag | `actions/checkout@v4` |
| `codeql.yml` | 28 | pinned-to-tag | `github/codeql-action/init@v3` |
| `codeql.yml` | 31 | pinned-to-tag | `github/codeql-action/autobuild@v3` |
| `codeql.yml` | 32 | pinned-to-tag | `github/codeql-action/analyze@v3` |
| `coverage.yml` | 12 | pinned-to-branch | `KooshaPari/phenotype-infrakit/.github/workflows/coverage.yml@main` |
| `docs-deploy.yml` | 21 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/vitepress-pages.yml@main` |
| `publish.yml` | 19 | pinned-to-branch | `KooshaPari/phenotype-infrakit/.github/workflows/publish-crate.yml@main` |
| `quality-gate.yml` | 10 | pinned-to-branch | `KooshaPari/phenotype-infrakit/.github/workflows/quality-gate.yml@main` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `secrets-scan.yml` | 15 | pinned-to-tag | `actions/checkout@v4` |

### agent-user-status (12 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ci.yml` | 14 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 17 | pinned-to-tag | `actions/setup-python@v5` |
| `ci.yml` | 36 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 52 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 55 | pinned-to-tag | `actions/setup-python@v5` |
| `ci.yml` | 74 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 77 | pinned-to-tag | `actions/setup-python@v5` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `secrets-scan.yml` | 15 | pinned-to-tag | `actions/checkout@v4` |

### Metron (12 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `cargo-deny.yml` | 22 | pinned-to-tag | `actions/checkout@v6` |
| `cargo-deny.yml` | 25 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `cargo-deny.yml` | 28 | pinned-to-tag | `EmbarkStudios/cargo-deny-action@v2` |
| `ci.yml` | 15 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 17 | unpinned-other-ref | `dtolnay/rust-action@stable` |
| `doc-links.yml` | 7 | pinned-to-tag | `actions/checkout@v6` |
| `fr-coverage.yml` | 7 | pinned-to-tag | `actions/checkout@v6` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `secrets-scan.yml` | 16 | pinned-to-tag | `actions/checkout@v6` |

### PlayCua (12 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `doc-links.yml` | 11 | pinned-to-tag | `actions/checkout@v6` |
| `doc-links.yml` | 12 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `fr-coverage.yml` | 11 | pinned-to-tag | `actions/checkout@v6` |
| `fr-coverage.yml` | 12 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `legacy-tooling-gate.yml` | 23 | pinned-to-tag | `actions/checkout@v6` |
| `legacy-tooling-gate.yml` | 26 | pinned-to-tag | `actions/checkout@v6` |
| `legacy-tooling-gate.yml` | 33 | pinned-to-tag | `actions/setup-python@v6` |
| `legacy-tooling-gate.yml` | 51 | pinned-to-tag | `actions/upload-artifact@v7` |
| `legacy-tooling-gate.yml` | 58 | pinned-to-tag | `actions/upload-artifact@v7` |
| `legacy-tooling-gate.yml` | 66 | pinned-to-tag | `actions/github-script@v9` |
| `quality-gate.yml` | 12 | pinned-to-tag | `actions/checkout@v6` |
| `quality-gate.yml` | 13 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |

### phenotype-journeys (11 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `codeql.yml` | 23 | pinned-to-tag | `actions/checkout@v4` |
| `codeql.yml` | 24 | pinned-to-tag | `github/codeql-action/init@v3` |
| `codeql.yml` | 27 | pinned-to-tag | `github/codeql-action/autobuild@v3` |
| `codeql.yml` | 28 | pinned-to-tag | `github/codeql-action/analyze@v3` |
| `publish-npm.yml` | 41 | pinned-to-tag | `actions/checkout@v4` |
| `publish-npm.yml` | 57 | pinned-to-tag | `actions/setup-node@v4` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `secrets-scan.yml` | 12 | pinned-to-tag | `actions/checkout@v4` |

### DataKit (11 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ci.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `ci.yml` | 23 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `ci.yml` | 26 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `release.yml` | 38 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 39 | pinned-to-tag | `actions/setup-python@v5` |
| `release.yml` | 51 | unpinned-other-ref | `pypa/gh-action-pypi-publish@release/v1` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `secrets-scan.yml` | 15 | pinned-to-tag | `actions/checkout@v4` |

### DevHex (11 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `doc-links.yml` | 11 | pinned-to-tag | `actions/checkout@v4` |
| `doc-links.yml` | 12 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `fr-coverage.yml` | 11 | pinned-to-tag | `actions/checkout@v4` |
| `fr-coverage.yml` | 12 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 12 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 13 | pinned-to-tag | `actions/setup-go@v5` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `secrets-scan.yml` | 15 | pinned-to-tag | `actions/checkout@v4` |

### PhenoRuntime (11 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ci.yml` | 10 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 11 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `doc-links.yml` | 10 | pinned-to-tag | `actions/checkout@v6` |
| `fr-coverage.yml` | 10 | pinned-to-tag | `actions/checkout@v6` |
| `release.yml` | 19 | pinned-to-tag | `actions/checkout@v6` |
| `release.yml` | 20 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `secrets-scan.yml` | 15 | pinned-to-tag | `actions/checkout@v6` |

### PhenoSpecs (11 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `legacy-tooling-gate.yml` | 24 | pinned-to-tag | `actions/checkout@v6` |
| `legacy-tooling-gate.yml` | 27 | pinned-to-tag | `actions/checkout@v6` |
| `legacy-tooling-gate.yml` | 34 | pinned-to-tag | `actions/setup-python@v6` |
| `legacy-tooling-gate.yml` | 52 | pinned-to-tag | `actions/upload-artifact@v7` |
| `legacy-tooling-gate.yml` | 59 | pinned-to-tag | `actions/upload-artifact@v7` |
| `legacy-tooling-gate.yml` | 67 | pinned-to-tag | `actions/github-script@v9` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v6` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.3` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v7` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `secrets-scan.yml` | 15 | pinned-to-tag | `actions/checkout@v6` |

### Eidolon (11 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `cargo-deny.yml` | 22 | pinned-to-tag | `actions/checkout@v6` |
| `cargo-deny.yml` | 25 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `cargo-deny.yml` | 28 | pinned-to-tag | `EmbarkStudios/cargo-deny-action@v2` |
| `doc-links.yml` | 10 | pinned-to-tag | `actions/checkout@v4` |
| `fr-coverage.yml` | 10 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 11 | pinned-to-tag | `actions/checkout@v4` |
| `sbom-refresh.yml` | 12 | pinned-to-branch | `KooshaPari/phenotype-tooling/.github/workflows/sbom-monthly.yml@main` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |

### phenotype-bus (11 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `cargo-deny.yml` | 23 | pinned-to-tag | `actions/checkout@v6` |
| `cargo-deny.yml` | 26 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `cargo-deny.yml` | 29 | pinned-to-tag | `EmbarkStudios/cargo-deny-action@v2` |
| `fr-coverage.yml` | 8 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 8 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 9 | pinned-to-tag | `Swatinem/rust-cache@v2` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |

### Sidekick (11 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `cargo-deny.yml` | 23 | pinned-to-tag | `actions/checkout@v6` |
| `cargo-deny.yml` | 26 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `cargo-deny.yml` | 29 | pinned-to-tag | `EmbarkStudios/cargo-deny-action@v2` |
| `doc-links.yml` | 10 | pinned-to-tag | `actions/checkout@v4` |
| `fr-coverage.yml` | 10 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 11 | pinned-to-tag | `actions/checkout@v4` |
| `sbom-refresh.yml` | 12 | pinned-to-branch | `KooshaPari/phenotype-tooling/.github/workflows/sbom-monthly.yml@main` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |

### phenotype-ops-mcp (10 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `codeql.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `codeql.yml` | 23 | pinned-to-tag | `github/codeql-action/init@v3` |
| `codeql.yml` | 26 | pinned-to-tag | `github/codeql-action/analyze@v3` |
| `manifest-check.yml` | 12 | pinned-to-tag | `actions/checkout@v4` |
| `manifest-check.yml` | 13 | pinned-to-tag | `actions/setup-go@v5` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `secrets-scan.yml` | 16 | pinned-to-tag | `actions/checkout@v4` |

### cheap-llm-mcp (10 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `doc-links.yml` | 11 | pinned-to-tag | `actions/checkout@v4` |
| `doc-links.yml` | 12 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `fr-coverage.yml` | 11 | pinned-to-tag | `actions/checkout@v4` |
| `fr-coverage.yml` | 12 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quality-gate.yml` | 12 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 13 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |

### phenotype-registry (10 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `legacy-tooling-gate.yml` | 20 | pinned-to-tag | `actions/checkout@v4` |
| `legacy-tooling-gate.yml` | 23 | pinned-to-tag | `actions/checkout@v4` |
| `legacy-tooling-gate.yml` | 30 | pinned-to-tag | `actions/setup-python@v5` |
| `legacy-tooling-gate.yml` | 48 | pinned-to-tag | `actions/upload-artifact@v4` |
| `legacy-tooling-gate.yml` | 55 | pinned-to-tag | `actions/upload-artifact@v4` |
| `legacy-tooling-gate.yml` | 63 | pinned-to-tag | `actions/github-script@v7` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |

### foqos-private (9 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `bump-build-number.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `bump-version.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `bump-version.yml` | 120 | pinned-to-tag | `actions/upload-artifact@v4` |
| `pr-check.yml` | 14 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `secrets-scan.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |

### phenotype-tooling (9 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `doc-links.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `fr-coverage.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 8 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 19 | pinned-to-tag | `actions/checkout@v4` |
| `release.yml` | 20 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |

### PhenoMCP (9 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `cargo-deny.yml` | 23 | pinned-to-tag | `actions/checkout@v6` |
| `cargo-deny.yml` | 26 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `cargo-deny.yml` | 29 | pinned-to-tag | `EmbarkStudios/cargo-deny-action@v2` |
| `ci.yml` | 10 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 11 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v6` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.3` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v7` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v4` |

### cliproxyapi-plusplus (8 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `alert-sync-issues.yml` | 13 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/alert-sync-issues.yml@main` |
| `ci.yml` | 54 | pinned-to-branch | `KooshaPari/phenotypeActions/.github/workflows/validate-governance.yml@main` |
| `pr-test-build.yml` | 82 | unpinned-other-ref | `arduino/setup-task@{"message":"Not` |
| `pr-test-build.yml` | 106 | unpinned-other-ref | `arduino/setup-task@{"message":"Not` |
| `pr-test-build.yml` | 124 | unpinned-other-ref | `arduino/setup-task@{"message":"Not` |
| `pr-test-build.yml` | 236 | unpinned-other-ref | `arduino/setup-task@{"message":"Not` |
| `pr-test-build.yml` | 252 | unpinned-other-ref | `arduino/setup-task@{"message":"Not` |
| `sast-quick.yml` | 67 | pinned-to-branch | `aquasecurity/trivy-action@master` |

### Benchora (8 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ci.yml` | 20 | pinned-to-branch | `KooshaPari/template-commons/.github/workflows/reusable-rust-ci.yml@main` |
| `ci.yml` | 27 | pinned-to-branch | `KooshaPari/template-commons/.github/workflows/reusable-security-scan.yml@main` |
| `ci.yml` | 35 | pinned-to-branch | `KooshaPari/phenotypeActions/.github/workflows/validate-governance.yml@main` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `secrets-scan.yml` | 18 | pinned-to-tag | `actions/checkout@v6` |

### Paginary (8 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `doc-links.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `fr-coverage.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 8 | pinned-to-tag | `actions/checkout@v4` |
| `sbom-refresh.yml` | 9 | pinned-to-branch | `KooshaPari/phenotype-tooling/.github/workflows/sbom-monthly.yml@main` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |

### dinoforge-packs (7 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `doc-links.yml` | 10 | pinned-to-tag | `actions/checkout@v4` |
| `fr-coverage.yml` | 10 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 11 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |

### ObservabilityKit (7 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `doc-links.yml` | 10 | pinned-to-tag | `actions/checkout@v6` |
| `fr-coverage.yml` | 10 | pinned-to-tag | `actions/checkout@v6` |
| `quality-gate.yml` | 11 | pinned-to-tag | `actions/checkout@v6` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v6` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.3` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v7` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v4` |

### PhenoProject (7 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `doc-links.yml` | 10 | pinned-to-tag | `actions/checkout@v4` |
| `fr-coverage.yml` | 10 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 11 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |

### phenotype-hub (7 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `doc-links.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `fr-coverage.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `secrets-scan.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |

### PhenoAgent (7 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `doc-links.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `fr-coverage.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 8 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |

### rich-cli-kit (7 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `doc-links.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `fr-coverage.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 8 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |

### thegent-dispatch (7 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `doc-links.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `fr-coverage.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 8 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |

### thegent-workspace (7 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `doc-links.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `fr-coverage.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `quality-gate.yml` | 8 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |

### PhenoDevOps (6 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ci.yml` | 15 | pinned-to-branch | `KooshaPari/phenotype-infrakit/.github/workflows/ci.yaml@main` |
| `coverage.yml` | 15 | pinned-to-branch | `KooshaPari/phenotype-infrakit/.github/workflows/coverage.yml@main` |
| `doc-links.yml` | 10 | pinned-to-tag | `actions/checkout@v6` |
| `fr-coverage.yml` | 10 | pinned-to-tag | `actions/checkout@v6` |
| `publish.yml` | 12 | pinned-to-branch | `KooshaPari/phenotype-infrakit/.github/workflows/publish-go.yml@main` |
| `quality-gate.yml` | 11 | pinned-to-tag | `actions/checkout@v6` |

### TestingKit (6 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ci.yml` | 12 | pinned-to-branch | `KooshaPari/phenotype-infrakit/.github/workflows/ci.yaml@main` |
| `coverage.yml` | 12 | pinned-to-branch | `KooshaPari/phenotype-infrakit/.github/workflows/coverage.yml@main` |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |

### Dino (5 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `polyglot-build.yml` | 52 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `polyglot-build.yml` | 178 | unpinned-other-ref | `goto-bus-stop/setup-zig@{"message":"Not` |
| `polyglot-build.yml` | 270 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `release-drafter.yml` | 12 | pinned-to-branch | `KooshaPari/phenoShared/.github/workflows/reusable/release-drafter.yml@main` |
| `release.yml` | 411 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |

### phenotype-auth-ts (5 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v6` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.3` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v7` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v4` |
| `secrets-scan.yml` | 15 | pinned-to-tag | `actions/checkout@v6` |

### phenotype-omlx (5 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |
| `update-formula.yml` | 14 | pinned-to-tag | `actions/checkout@v4` |

### phenoUtils (5 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `cargo-deny.yml` | 23 | pinned-to-tag | `actions/checkout@v6` |
| `cargo-deny.yml` | 26 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `cargo-deny.yml` | 29 | pinned-to-tag | `EmbarkStudios/cargo-deny-action@v2` |
| `doc-links.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |
| `fr-coverage.yml` | 7 | pinned-to-tag | `actions/checkout@v4` |

### Conft (4 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |

### heliosBench (4 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v4` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.2` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v4` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v3` |

### phenotype-org-audits (4 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `quarterly-audit.yml` | 18 | pinned-to-tag | `actions/checkout@v4` |
| `quarterly-audit.yml` | 21 | pinned-to-tag | `actions/checkout@v4` |
| `quarterly-audit.yml` | 27 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `quarterly-audit.yml` | 55 | pinned-to-tag | `peter-evans/create-pull-request@v5` |

### phenoXdd (4 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v6` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.3` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v7` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v4` |

### PlatformKit (4 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `scorecard.yml` | 22 | pinned-to-tag | `actions/checkout@v6` |
| `scorecard.yml` | 25 | pinned-to-tag | `ossf/scorecard-action@v2.4.3` |
| `scorecard.yml` | 31 | pinned-to-tag | `actions/upload-artifact@v7` |
| `scorecard.yml` | 37 | pinned-to-tag | `github/codeql-action/upload-sarif@v4` |

### eyetracker (3 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `cargo-deny.yml` | 22 | pinned-to-tag | `actions/checkout@v6` |
| `cargo-deny.yml` | 25 | unpinned-other-ref | `dtolnay/rust-toolchain@stable` |
| `cargo-deny.yml` | 28 | pinned-to-tag | `EmbarkStudios/cargo-deny-action@v2` |

### PolicyStack (2 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `release.yml` | 56 | pinned-to-branch | `KooshaPari/phenotypeActions/promote@main` |
| `security.yml` | 28 | unpinned-other-ref | `paambaati/action-pip-audit@{"message":"Not` |

### agileplus-landing (2 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ci.yml` | 11 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 12 | pinned-to-tag | `oven-sh/setup-bun@v2` |

### byteport-landing (2 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ci.yml` | 11 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 12 | pinned-to-tag | `oven-sh/setup-bun@v2` |

### hwledger-landing (2 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ci.yml` | 11 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 12 | pinned-to-tag | `oven-sh/setup-bun@v2` |

### phenokits-landing (2 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ci.yml` | 11 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 12 | pinned-to-tag | `oven-sh/setup-bun@v2` |

### projects-landing (2 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ci.yml` | 11 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 12 | pinned-to-tag | `oven-sh/setup-bun@v2` |

### ResilienceKit (2 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ci.yml` | 15 | pinned-to-branch | `KooshaPari/phenotype-infrakit/.github/workflows/ci.yaml@main` |
| `coverage.yml` | 15 | pinned-to-branch | `KooshaPari/phenotype-infrakit/.github/workflows/coverage.yml@main` |

### thegent-landing (2 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `ci.yml` | 11 | pinned-to-tag | `actions/checkout@v6` |
| `ci.yml` | 12 | pinned-to-tag | `oven-sh/setup-bun@v2` |

### phenoData (1 unpinned)

| Workflow | Line | Classification | uses |
| --- | ---: | --- | --- |
| `sbom-refresh.yml` | 9 | pinned-to-branch | `KooshaPari/phenotype-tooling/.github/workflows/sbom-monthly.yml@main` |

## Repos Without External Workflow Actions

- `AgentMCP`: no workflows
- `phenotype-org-governance`: no workflows

## Method

1. Listed repositories with `gh repo list KooshaPari --limit 1000 --json name,isArchived,visibility,url`; after REST quota was exhausted, completed the same live inventory through GitHub GraphQL and excluded archived repos.
2. Listed workflows using the GitHub contents/tree API for `.github/workflows`.
3. Fetched each workflow blob from live GitHub and scanned `uses:` lines.
4. Classified refs as `pinned-to-sha` for `@[0-9a-fA-F]{40}`, `pinned-to-tag` for `@v\d...`, `pinned-to-branch` for `@main` or `@master`, and separate unpinned buckets for other or missing refs.

