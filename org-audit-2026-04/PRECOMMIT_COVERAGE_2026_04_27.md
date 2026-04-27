# Pre-commit Hook Coverage Audit - 2026-04-27

Scope: all non-archived `KooshaPari` repositories returned by `gh repo list KooshaPari --json name,isArchived --limit 300`.

Method: for each repository, queried these GitHub Contents API paths and treated a successful response as `yes`:

```bash
gh api repos/KooshaPari/$repo/contents/.pre-commit-config.yaml
gh api repos/KooshaPari/$repo/contents/lefthook.yml
gh api repos/KooshaPari/$repo/contents/.husky
```

## Summary

| Tool type | Present | Total | Coverage |
| --- | ---: | ---: | ---: |
| pre-commit | 47 | 103 | 45.6% |
| lefthook | 3 | 103 | 2.9% |
| husky | 1 | 103 | 1.0% |
| any hook surface | 48 | 103 | 46.6% |

Gap repos (55):

- `agent-user-status`
- `AgentMCP`
- `Agentora`
- `agileplus-landing`
- `byteport-landing`
- `cheap-llm-mcp`
- `Conft`
- `DataKit`
- `DevHex`
- `dinoforge-packs`
- `DINOForge-UnityDoorstop`
- `Eidolon`
- `eyetracker`
- `foqos-private`
- `heliosBench`
- `hwledger-landing`
- `KDesktopVirt`
- `MCPForge`
- `McpKit`
- `nanovms`
- `Paginary`
- `phenoAI`
- `PhenoCompose`
- `phenoData`
- `PhenoDevOps`
- `PhenoHandbook`
- `PhenoKits`
- `phenokits-landing`
- `PhenoPlugins`
- `PhenoProject`
- `PhenoSpecs`
- `phenotype-auth-ts`
- `phenotype-bus`
- `phenotype-hub`
- `phenotype-infra`
- `phenotype-journeys`
- `phenotype-omlx`
- `phenotype-ops-mcp`
- `phenotype-org-audits`
- `phenotype-org-governance`
- `phenotype-registry`
- `phenoUtils`
- `PhenoVCS`
- `phenoXdd`
- `PlatformKit`
- `PlayCua`
- `projects-landing`
- `ResilienceKit`
- `rich-cli-kit`
- `Sidekick`
- `TestingKit`
- `thegent-dispatch`
- `thegent-landing`
- `thegent-workspace`
- `Tracely`

## Repo Coverage

| Repo | .pre-commit-config.yaml | lefthook.yml | .husky | Any hook |
| --- | --- | --- | --- | --- |
| `agent-devops-setups` | yes | no | no | yes |
| `agent-user-status` | no | no | no | no |
| `agentapi-plusplus` | yes | no | no | yes |
| `AgentMCP` | no | no | no | no |
| `Agentora` | no | no | no | no |
| `AgilePlus` | yes | no | no | yes |
| `agileplus-landing` | no | no | no | no |
| `Apisync` | yes | no | no | yes |
| `argis-extensions` | yes | no | no | yes |
| `AuthKit` | yes | no | no | yes |
| `Benchora` | yes | no | no | yes |
| `BytePort` | yes | no | no | yes |
| `byteport-landing` | no | no | no | no |
| `cheap-llm-mcp` | no | no | no | no |
| `Civis` | yes | no | no | yes |
| `cliproxyapi-plusplus` | yes | no | no | yes |
| `Configra` | yes | no | no | yes |
| `Conft` | no | no | no | no |
| `DataKit` | no | no | no | no |
| `DevHex` | no | no | no | no |
| `Dino` | yes | yes | no | yes |
| `dinoforge-packs` | no | no | no | no |
| `DINOForge-UnityDoorstop` | no | no | no | no |
| `Eidolon` | no | no | no | no |
| `eyetracker` | no | no | no | no |
| `FocalPoint` | yes | yes | no | yes |
| `foqos-private` | no | no | no | no |
| `GDK` | yes | no | no | yes |
| `helios-cli` | yes | no | no | yes |
| `helios-router` | yes | no | no | yes |
| `heliosApp` | yes | no | no | yes |
| `heliosBench` | no | no | no | no |
| `heliosCLI` | yes | no | no | yes |
| `HeliosLab` | yes | no | no | yes |
| `HexaKit` | yes | no | no | yes |
| `Httpora` | yes | no | no | yes |
| `hwLedger` | yes | yes | no | yes |
| `hwledger-landing` | no | no | no | no |
| `KDesktopVirt` | no | no | no | no |
| `MCPForge` | no | no | no | no |
| `McpKit` | no | no | no | no |
| `Metron` | yes | no | no | yes |
| `nanovms` | no | no | no | no |
| `ObservabilityKit` | yes | no | no | yes |
| `Paginary` | no | no | no | no |
| `Parpoura` | yes | no | no | yes |
| `pheno` | yes | no | no | yes |
| `PhenoAgent` | yes | no | no | yes |
| `phenoAI` | no | no | no | no |
| `PhenoCompose` | no | no | no | no |
| `phenoData` | no | no | no | no |
| `phenoDesign` | yes | no | no | yes |
| `PhenoDevOps` | no | no | no | no |
| `phenodocs` | yes | no | no | yes |
| `PhenoHandbook` | no | no | no | no |
| `PhenoKits` | no | no | no | no |
| `phenokits-landing` | no | no | no | no |
| `PhenoLang` | yes | no | no | yes |
| `PhenoMCP` | yes | no | no | yes |
| `PhenoObservability` | yes | no | no | yes |
| `PhenoPlugins` | no | no | no | no |
| `PhenoProc` | yes | no | no | yes |
| `PhenoProject` | no | no | no | no |
| `phenoResearchEngine` | yes | no | no | yes |
| `PhenoRuntime` | yes | no | no | yes |
| `phenoShared` | yes | no | no | yes |
| `PhenoSpecs` | no | no | no | no |
| `phenotype-auth-ts` | no | no | no | no |
| `phenotype-bus` | no | no | no | no |
| `phenotype-hub` | no | no | no | no |
| `phenotype-infra` | no | no | no | no |
| `phenotype-journeys` | no | no | no | no |
| `phenotype-omlx` | no | no | no | no |
| `phenotype-ops-mcp` | no | no | no | no |
| `phenotype-org-audits` | no | no | no | no |
| `phenotype-org-governance` | no | no | no | no |
| `phenotype-registry` | no | no | no | no |
| `phenotype-tooling` | yes | no | no | yes |
| `phenoUtils` | no | no | no | no |
| `PhenoVCS` | no | no | no | no |
| `phenoXdd` | no | no | no | no |
| `Planify` | no | no | yes | yes |
| `PlatformKit` | no | no | no | no |
| `PlayCua` | no | no | no | no |
| `PolicyStack` | yes | no | no | yes |
| `portage` | yes | no | no | yes |
| `projects-landing` | no | no | no | no |
| `QuadSGM` | yes | no | no | yes |
| `ResilienceKit` | no | no | no | no |
| `rich-cli-kit` | no | no | no | no |
| `Sidekick` | no | no | no | no |
| `Stashly` | yes | no | no | yes |
| `Tasken` | yes | no | no | yes |
| `TestingKit` | no | no | no | no |
| `thegent` | yes | no | no | yes |
| `thegent-dispatch` | no | no | no | no |
| `thegent-landing` | no | no | no | no |
| `thegent-workspace` | no | no | no | no |
| `Tokn` | yes | no | no | yes |
| `Tracely` | no | no | no | no |
| `Tracera` | yes | no | no | yes |
| `vibeproxy` | yes | no | no | yes |
| `vibeproxy-monitoring-unified` | yes | no | no | yes |
