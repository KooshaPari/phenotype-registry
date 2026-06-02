# Submodule Sanity Audit - 2026-04-27

Scope: non-archived repositories under `KooshaPari`.

Method:
- `has_gitmodules`: `gh api repos/KooshaPari/<repo>/contents/.gitmodules` returns 200.
- `.gitmodules_entries`: decoded `.content` from that endpoint, counted like `grep -c "submodule"`.
- `tree_submodules`: `gh api repos/KooshaPari/<repo>/git/trees/HEAD?recursive=1 --jq '[.tree[] | select(.type=="commit")] | length'`.
- `orphan_delta`: `tree_submodules - .gitmodules_entries`; positive values are `ORPHAN_ALERT`.

Generated: 2026-04-27 America/Phoenix.

Summary: `103` repos audited; `20` orphan alerts; `0` tree API errors.

| Status | Repo | has_gitmodules | .gitmodules entries | tree_submodules | orphan_delta | default_branch | URL |
|---|---:|---:|---:|---:|---:|---|---|
| `ORPHAN_ALERT` | `PhenoLang` | `yes` | 1 | 118 | 117 | `main` | https://github.com/KooshaPari/PhenoLang |
| `ORPHAN_ALERT` | `pheno` | `yes` | 1 | 110 | 109 | `main` | https://github.com/KooshaPari/pheno |
| `ORPHAN_ALERT` | `HexaKit` | `yes` | 2 | 93 | 91 | `main` | https://github.com/KooshaPari/HexaKit |
| `ORPHAN_ALERT` | `PhenoProc` | `yes` | 2 | 31 | 29 | `main` | https://github.com/KooshaPari/PhenoProc |
| `ORPHAN_ALERT` | `heliosCLI` | `yes` | 4 | 29 | 25 | `main` | https://github.com/KooshaPari/heliosCLI |
| `ORPHAN_ALERT` | `helios-router` | `yes` | 3 | 24 | 21 | `main` | https://github.com/KooshaPari/helios-router |
| `ORPHAN_ALERT` | `thegent` | `yes` | 1 | 6 | 5 | `main` | https://github.com/KooshaPari/thegent |
| `ORPHAN_ALERT` | `AuthKit` | `no` | 0 | 4 | 4 | `main` | https://github.com/KooshaPari/AuthKit |
| `ORPHAN_ALERT` | `DataKit` | `no` | 0 | 4 | 4 | `main` | https://github.com/KooshaPari/DataKit |
| `ORPHAN_ALERT` | `ObservabilityKit` | `no` | 0 | 4 | 4 | `main` | https://github.com/KooshaPari/ObservabilityKit |
| `ORPHAN_ALERT` | `Sidekick` | `no` | 0 | 3 | 3 | `main` | https://github.com/KooshaPari/Sidekick |
| `ORPHAN_ALERT` | `Tracely` | `no` | 0 | 3 | 3 | `main` | https://github.com/KooshaPari/Tracely |
| `ORPHAN_ALERT` | `helios-cli` | `no` | 0 | 2 | 2 | `main` | https://github.com/KooshaPari/helios-cli |
| `ORPHAN_ALERT` | `PhenoObservability` | `no` | 0 | 2 | 2 | `main` | https://github.com/KooshaPari/PhenoObservability |
| `ORPHAN_ALERT` | `TestingKit` | `no` | 0 | 2 | 2 | `main` | https://github.com/KooshaPari/TestingKit |
| `ORPHAN_ALERT` | `Conft` | `no` | 0 | 1 | 1 | `main` | https://github.com/KooshaPari/Conft |
| `ORPHAN_ALERT` | `PhenoDevOps` | `no` | 0 | 1 | 1 | `main` | https://github.com/KooshaPari/PhenoDevOps |
| `ORPHAN_ALERT` | `portage` | `no` | 0 | 1 | 1 | `main` | https://github.com/KooshaPari/portage |
| `ORPHAN_ALERT` | `QuadSGM` | `no` | 0 | 1 | 1 | `main` | https://github.com/KooshaPari/QuadSGM |
| `ORPHAN_ALERT` | `ResilienceKit` | `no` | 0 | 1 | 1 | `main` | https://github.com/KooshaPari/ResilienceKit |
| `OK` | `agent-devops-setups` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/agent-devops-setups |
| `OK` | `agent-user-status` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/agent-user-status |
| `OK` | `AgentMCP` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/AgentMCP |
| `OK` | `Agentora` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/Agentora |
| `OK` | `agileplus-landing` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/agileplus-landing |
| `OK` | `Apisync` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/Apisync |
| `OK` | `argis-extensions` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/argis-extensions |
| `OK` | `Benchora` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/Benchora |
| `OK` | `BytePort` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/BytePort |
| `OK` | `byteport-landing` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/byteport-landing |
| `OK` | `cheap-llm-mcp` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/cheap-llm-mcp |
| `OK` | `Civis` | `yes` | 1 | 1 | 0 | `main` | https://github.com/KooshaPari/Civis |
| `OK` | `cliproxyapi-plusplus` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/cliproxyapi-plusplus |
| `OK` | `Configra` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/Configra |
| `OK` | `DevHex` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/DevHex |
| `OK` | `Dino` | `yes` | 1 | 1 | 0 | `main` | https://github.com/KooshaPari/Dino |
| `OK` | `dinoforge-packs` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/dinoforge-packs |
| `OK` | `DINOForge-UnityDoorstop` | `no` | 0 | 0 | 0 | `master` | https://github.com/KooshaPari/DINOForge-UnityDoorstop |
| `OK` | `Eidolon` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/Eidolon |
| `OK` | `eyetracker` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/eyetracker |
| `OK` | `FocalPoint` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/FocalPoint |
| `OK` | `foqos-private` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/foqos-private |
| `OK` | `GDK` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/GDK |
| `OK` | `heliosApp` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/heliosApp |
| `OK` | `heliosBench` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/heliosBench |
| `OK` | `HeliosLab` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/HeliosLab |
| `OK` | `Httpora` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/Httpora |
| `OK` | `hwLedger` | `yes` | 1 | 1 | 0 | `main` | https://github.com/KooshaPari/hwLedger |
| `OK` | `hwledger-landing` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/hwledger-landing |
| `OK` | `KDesktopVirt` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/KDesktopVirt |
| `OK` | `MCPForge` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/MCPForge |
| `OK` | `McpKit` | `yes` | 1 | 1 | 0 | `main` | https://github.com/KooshaPari/McpKit |
| `OK` | `Metron` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/Metron |
| `OK` | `nanovms` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/nanovms |
| `OK` | `Paginary` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/Paginary |
| `OK` | `Parpoura` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/Parpoura |
| `OK` | `PhenoAgent` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/PhenoAgent |
| `OK` | `phenoAI` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/phenoAI |
| `OK` | `PhenoCompose` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/PhenoCompose |
| `OK` | `phenoData` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/phenoData |
| `OK` | `phenoDesign` | `yes` | 1 | 1 | 0 | `main` | https://github.com/KooshaPari/phenoDesign |
| `OK` | `phenodocs` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/phenodocs |
| `OK` | `PhenoHandbook` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/PhenoHandbook |
| `OK` | `PhenoKits` | `yes` | 1 | 1 | 0 | `main` | https://github.com/KooshaPari/PhenoKits |
| `OK` | `phenokits-landing` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/phenokits-landing |
| `OK` | `PhenoMCP` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/PhenoMCP |
| `OK` | `PhenoPlugins` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/PhenoPlugins |
| `OK` | `PhenoProject` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/PhenoProject |
| `OK` | `phenoResearchEngine` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/phenoResearchEngine |
| `OK` | `PhenoRuntime` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/PhenoRuntime |
| `OK` | `phenoShared` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/phenoShared |
| `OK` | `PhenoSpecs` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/PhenoSpecs |
| `OK` | `phenotype-auth-ts` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/phenotype-auth-ts |
| `OK` | `phenotype-bus` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/phenotype-bus |
| `OK` | `phenotype-hub` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/phenotype-hub |
| `OK` | `phenotype-infra` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/phenotype-infra |
| `OK` | `phenotype-journeys` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/phenotype-journeys |
| `OK` | `phenotype-omlx` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/phenotype-omlx |
| `OK` | `phenotype-ops-mcp` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/phenotype-ops-mcp |
| `OK` | `phenotype-org-audits` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/phenotype-org-audits |
| `OK` | `phenotype-org-governance` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/phenotype-org-governance |
| `OK` | `phenotype-registry` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/phenotype-registry |
| `OK` | `phenotype-tooling` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/phenotype-tooling |
| `OK` | `phenoUtils` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/phenoUtils |
| `OK` | `PhenoVCS` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/PhenoVCS |
| `OK` | `phenoXdd` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/phenoXdd |
| `OK` | `Planify` | `no` | 0 | 0 | 0 | `master` | https://github.com/KooshaPari/Planify |
| `OK` | `PlatformKit` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/PlatformKit |
| `OK` | `PlayCua` | `no` | 0 | 0 | 0 | `master` | https://github.com/KooshaPari/PlayCua |
| `OK` | `PolicyStack` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/PolicyStack |
| `OK` | `projects-landing` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/projects-landing |
| `OK` | `rich-cli-kit` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/rich-cli-kit |
| `OK` | `Stashly` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/Stashly |
| `OK` | `Tasken` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/Tasken |
| `OK` | `thegent-dispatch` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/thegent-dispatch |
| `OK` | `thegent-landing` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/thegent-landing |
| `OK` | `thegent-workspace` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/thegent-workspace |
| `OK` | `Tokn` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/Tokn |
| `OK` | `Tracera` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/Tracera |
| `OK` | `vibeproxy` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/vibeproxy |
| `OK` | `vibeproxy-monitoring-unified` | `no` | 0 | 0 | 0 | `main` | https://github.com/KooshaPari/vibeproxy-monitoring-unified |
| `OK` | `agentapi-plusplus` | `yes` | 1 | 0 | -1 | `main` | https://github.com/KooshaPari/agentapi-plusplus |
| `OK` | `AgilePlus` | `yes` | 1 | 0 | -1 | `main` | https://github.com/KooshaPari/AgilePlus |
