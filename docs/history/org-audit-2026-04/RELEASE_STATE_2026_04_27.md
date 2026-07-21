# Release State Audit - 2026-04-27

Scope: all non-archived repositories returned by `gh repo list KooshaPari --limit 200 --json name,isArchived`, filtered with `isArchived == false`.

Method per repo:

```bash
gh api repos/KooshaPari/$r/tags --jq '. | length'
gh api repos/KooshaPari/$r/releases/latest --jq '.tag_name + " " + .published_at' 2>/dev/null
```

Summary: 103 non-archived repos audited; 80 repos have no latest release; 0 repos have a stale latest release (>90 days as of 2026-04-27 UTC).

## Top 5 Most Recent Releases

| Repo | Latest release | Published | Age days |
| --- | --- | --- | ---: |
| AgilePlus | v0.2.1 | 2026-04-26T07:38:25Z | 0 |
| HeliosLab | v0.2.2 | 2026-04-26T04:06:08Z | 0 |
| Tokn | v0.1.1 | 2026-04-26T04:05:40Z | 0 |
| cliproxyapi-plusplus | v0.2.0 | 2026-04-26T03:56:08Z | 0 |
| PolicyStack | v0.1.0 | 2026-04-26T03:55:33Z | 0 |

## Release Table

Sorted with no-release repositories first, then released repositories by oldest latest release first.

| Repo | Tags | Latest release | Published | Age days | Status |
| --- | ---: | --- | --- | ---: | --- |
| agent-devops-setups | 0 | - | - | - | NO_RELEASE |
| agent-user-status | 0 | - | - | - | NO_RELEASE |
| AgentMCP | 0 | - | - | - | NO_RELEASE |
| Agentora | 0 | - | - | - | NO_RELEASE |
| agileplus-landing | 0 | - | - | - | NO_RELEASE |
| Apisync | 0 | - | - | - | NO_RELEASE |
| argis-extensions | 0 | - | - | - | NO_RELEASE |
| AuthKit | 0 | - | - | - | NO_RELEASE |
| Benchora | 0 | - | - | - | NO_RELEASE |
| BytePort | 0 | - | - | - | NO_RELEASE |
| byteport-landing | 0 | - | - | - | NO_RELEASE |
| cheap-llm-mcp | 0 | - | - | - | NO_RELEASE |
| Configra | 0 | - | - | - | NO_RELEASE |
| Conft | 0 | - | - | - | NO_RELEASE |
| DataKit | 0 | - | - | - | NO_RELEASE |
| DevHex | 0 | - | - | - | NO_RELEASE |
| dinoforge-packs | 0 | - | - | - | NO_RELEASE |
| Eidolon | 0 | - | - | - | NO_RELEASE |
| eyetracker | 2 | - | - | - | NO_RELEASE |
| foqos-private | 30 | - | - | - | NO_RELEASE |
| GDK | 0 | - | - | - | NO_RELEASE |
| HexaKit | 0 | - | - | - | NO_RELEASE |
| Httpora | 0 | - | - | - | NO_RELEASE |
| hwledger-landing | 0 | - | - | - | NO_RELEASE |
| MCPForge | 0 | - | - | - | NO_RELEASE |
| McpKit | 0 | - | - | - | NO_RELEASE |
| Metron | 0 | - | - | - | NO_RELEASE |
| nanovms | 0 | - | - | - | NO_RELEASE |
| ObservabilityKit | 0 | - | - | - | NO_RELEASE |
| Paginary | 0 | - | - | - | NO_RELEASE |
| pheno | 0 | - | - | - | NO_RELEASE |
| PhenoAgent | 0 | - | - | - | NO_RELEASE |
| phenoAI | 0 | - | - | - | NO_RELEASE |
| PhenoCompose | 0 | - | - | - | NO_RELEASE |
| phenoData | 0 | - | - | - | NO_RELEASE |
| phenoDesign | 0 | - | - | - | NO_RELEASE |
| PhenoDevOps | 0 | - | - | - | NO_RELEASE |
| phenodocs | 0 | - | - | - | NO_RELEASE |
| PhenoHandbook | 0 | - | - | - | NO_RELEASE |
| phenokits-landing | 0 | - | - | - | NO_RELEASE |
| PhenoLang | 0 | - | - | - | NO_RELEASE |
| PhenoMCP | 0 | - | - | - | NO_RELEASE |
| PhenoObservability | 0 | - | - | - | NO_RELEASE |
| PhenoPlugins | 0 | - | - | - | NO_RELEASE |
| PhenoProc | 0 | - | - | - | NO_RELEASE |
| PhenoProject | 0 | - | - | - | NO_RELEASE |
| phenoResearchEngine | 0 | - | - | - | NO_RELEASE |
| PhenoRuntime | 0 | - | - | - | NO_RELEASE |
| PhenoSpecs | 0 | - | - | - | NO_RELEASE |
| phenotype-auth-ts | 0 | - | - | - | NO_RELEASE |
| phenotype-bus | 0 | - | - | - | NO_RELEASE |
| phenotype-hub | 0 | - | - | - | NO_RELEASE |
| phenotype-infra | 0 | - | - | - | NO_RELEASE |
| phenotype-journeys | 0 | - | - | - | NO_RELEASE |
| phenotype-omlx | 30 | - | - | - | NO_RELEASE |
| phenotype-ops-mcp | 1 | - | - | - | NO_RELEASE |
| phenotype-org-audits | 0 | - | - | - | NO_RELEASE |
| phenotype-org-governance | 0 | - | - | - | NO_RELEASE |
| phenotype-registry | 0 | - | - | - | NO_RELEASE |
| phenotype-tooling | 0 | - | - | - | NO_RELEASE |
| phenoUtils | 0 | - | - | - | NO_RELEASE |
| PhenoVCS | 0 | - | - | - | NO_RELEASE |
| phenoXdd | 0 | - | - | - | NO_RELEASE |
| Planify | 30 | - | - | - | NO_RELEASE |
| PlatformKit | 0 | - | - | - | NO_RELEASE |
| PlayCua | 0 | - | - | - | NO_RELEASE |
| portage | 1 | - | - | - | NO_RELEASE |
| projects-landing | 0 | - | - | - | NO_RELEASE |
| QuadSGM | 1 | - | - | - | NO_RELEASE |
| ResilienceKit | 0 | - | - | - | NO_RELEASE |
| rich-cli-kit | 0 | - | - | - | NO_RELEASE |
| Sidekick | 0 | - | - | - | NO_RELEASE |
| Stashly | 0 | - | - | - | NO_RELEASE |
| Tasken | 0 | - | - | - | NO_RELEASE |
| TestingKit | 0 | - | - | - | NO_RELEASE |
| thegent-dispatch | 0 | - | - | - | NO_RELEASE |
| thegent-landing | 0 | - | - | - | NO_RELEASE |
| thegent-workspace | 0 | - | - | - | NO_RELEASE |
| Tracely | 0 | - | - | - | NO_RELEASE |
| vibeproxy-monitoring-unified | 0 | - | - | - | NO_RELEASE |
| thegent | 7 | v0.1.2 | 2026-02-23T03:45:06Z | 62 | CURRENT |
| DINOForge-UnityDoorstop | 30 | v4.5.1-multiasm | 2026-03-18T06:41:09Z | 39 | CURRENT |
| agentapi-plusplus | 21 | v0.10.0 | 2026-03-29T16:41:41Z | 28 | CURRENT |
| Civis | 1 | v0.1.0 | 2026-03-29T16:41:37Z | 28 | CURRENT |
| Parpoura | 1 | v0.1.0 | 2026-03-29T16:41:39Z | 28 | CURRENT |
| phenoShared | 1 | v0.1.0 | 2026-03-29T14:14:26Z | 28 | CURRENT |
| Tracera | 6 | v2.0.1 | 2026-03-29T15:08:36Z | 28 | CURRENT |
| vibeproxy | 16 | v1.5.0 | 2026-03-29T16:41:46Z | 28 | CURRENT |
| hwLedger | 1 | v0.1.0-alpha | 2026-04-19T10:31:10Z | 7 | CURRENT |
| Dino | 21 | v0.23.0 | 2026-04-23T09:36:33Z | 3 | CURRENT |
| helios-cli | 30 | v0.2.0 | 2026-04-25T13:31:05Z | 1 | CURRENT |
| helios-router | 2 | v0.2.0 | 2026-04-25T13:31:42Z | 1 | CURRENT |
| heliosBench | 1 | v0.2.0 | 2026-04-25T13:31:43Z | 1 | CURRENT |
| heliosCLI | 3 | v0.2.1 | 2026-04-25T15:23:44Z | 1 | CURRENT |
| AgilePlus | 4 | v0.2.1 | 2026-04-26T07:38:25Z | 0 | CURRENT |
| cliproxyapi-plusplus | 30 | v0.2.0 | 2026-04-26T03:56:08Z | 0 | CURRENT |
| FocalPoint | 6 | v0.0.12 | 2026-04-26T03:03:42Z | 0 | CURRENT |
| heliosApp | 9 | v2026.05B.0 | 2026-04-26T02:39:43Z | 0 | CURRENT |
| HeliosLab | 30 | v0.2.2 | 2026-04-26T04:06:08Z | 0 | CURRENT |
| KDesktopVirt | 3 | v0.2.1 | 2026-04-26T02:55:41Z | 0 | CURRENT |
| PhenoKits | 2 | v0.1.1 | 2026-04-26T02:57:20Z | 0 | CURRENT |
| PolicyStack | 1 | v0.1.0 | 2026-04-26T03:55:33Z | 0 | CURRENT |
| Tokn | 1 | v0.1.1 | 2026-04-26T04:05:40Z | 0 | CURRENT |
