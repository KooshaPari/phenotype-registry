# Branch Protection and Ruleset Audit - 2026-04-27

Read-only audit of non-archived `KooshaPari` repositories.

## Method

For each non-archived repo:

```bash
gh api repos/KooshaPari/$r/rulesets --jq '.[] | {n:.name, t:.target, en:.enforcement}' 2>/dev/null
gh api repos/KooshaPari/$r/branches/main/protection 2>/dev/null > /dev/null && echo "main_protected=true" || echo "main_protected=false"
```

## Coverage

| Metric | Count |
|---|---:|
| Non-archived repos audited | 103 |
| Repos with >=1 active ruleset | 78 |
| Repos with no active rulesets | 25 |
| Repos with classic `main` protection | 4 |
| Covered by active ruleset or classic `main` protection | 80 |
| No active ruleset and no classic `main` protection | 23 |

## Gap Repos

cheap-llm-mcp, Configra, DINOForge-UnityDoorstop, Eidolon, foqos-private, KDesktopVirt, MCPForge, Paginary, phenoResearchEngine, phenotype-bus, phenotype-journeys, phenotype-omlx, phenotype-ops-mcp, phenotype-org-audits, phenotype-org-governance, Planify, rich-cli-kit, Sidekick, thegent-dispatch, thegent-landing, thegent-workspace, Tracely, vibeproxy

## Repository Detail

| Status | Repo | Active rulesets | Total rulesets | main_protected | Rulesets |
|---|---|---:|---:|---|---|
| `NO_RULES` | `agent-user-status` | 0 | 0 | `true` | - |
| `NO_RULES` | `cheap-llm-mcp` | 0 | 0 | `false` | - |
| `NO_RULES` | `Configra` | 0 | 0 | `false` | - |
| `NO_RULES` | `DINOForge-UnityDoorstop` | 0 | 0 | `false` | - |
| `NO_RULES` | `Eidolon` | 0 | 0 | `false` | - |
| `NO_RULES` | `foqos-private` | 0 | 0 | `false` | - |
| `NO_RULES` | `KDesktopVirt` | 0 | 0 | `false` | - |
| `NO_RULES` | `MCPForge` | 0 | 0 | `false` | - |
| `NO_RULES` | `Paginary` | 0 | 0 | `false` | - |
| `NO_RULES` | `phenoResearchEngine` | 0 | 0 | `false` | - |
| `NO_RULES` | `phenotype-bus` | 0 | 0 | `false` | - |
| `NO_RULES` | `phenotype-journeys` | 0 | 0 | `false` | - |
| `NO_RULES` | `phenotype-omlx` | 0 | 0 | `false` | - |
| `NO_RULES` | `phenotype-ops-mcp` | 0 | 0 | `false` | - |
| `NO_RULES` | `phenotype-org-audits` | 0 | 0 | `false` | - |
| `NO_RULES` | `phenotype-org-governance` | 0 | 0 | `false` | - |
| `NO_RULES` | `Planify` | 0 | 0 | `false` | - |
| `NO_RULES` | `QuadSGM` | 0 | 0 | `true` | - |
| `NO_RULES` | `rich-cli-kit` | 0 | 0 | `false` | - |
| `NO_RULES` | `Sidekick` | 0 | 0 | `false` | - |
| `NO_RULES` | `thegent-dispatch` | 0 | 0 | `false` | - |
| `NO_RULES` | `thegent-landing` | 0 | 0 | `false` | - |
| `NO_RULES` | `thegent-workspace` | 0 | 0 | `false` | - |
| `NO_RULES` | `Tracely` | 0 | 0 | `false` | - |
| `NO_RULES` | `vibeproxy` | 0 | 0 | `false` | - |
| `RULES` | `agent-devops-setups` | 2 | 2 | `false` | `Main` (branch/active)<br>`Main Governance Baseline` (branch/active) |
| `RULES` | `agentapi-plusplus` | 1 | 1 | `true` | `Main` (branch/active) |
| `RULES` | `AgentMCP` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `Agentora` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `AgilePlus` | 2 | 2 | `false` | `Main` (branch/active)<br>`Main Governance Baseline` (branch/active) |
| `RULES` | `agileplus-landing` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `Apisync` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `argis-extensions` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `AuthKit` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `Benchora` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `BytePort` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `byteport-landing` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `Civis` | 2 | 2 | `false` | `Main` (branch/active)<br>`Mainm` (branch/active) |
| `RULES` | `cliproxyapi-plusplus` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `Conft` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `DataKit` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `DevHex` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `Dino` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `dinoforge-packs` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `eyetracker` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `FocalPoint` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `GDK` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `helios-cli` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `helios-router` | 1 | 1 | `true` | `Main` (branch/active) |
| `RULES` | `heliosApp` | 2 | 2 | `false` | `Main` (branch/active)<br>`Main Governance Baseline` (branch/active) |
| `RULES` | `heliosBench` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `heliosCLI` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `HeliosLab` | 1 | 1 | `false` | `Main Governance Baseline` (branch/active) |
| `RULES` | `HexaKit` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `Httpora` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `hwLedger` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `hwledger-landing` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `McpKit` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `Metron` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `nanovms` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `ObservabilityKit` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `Parpoura` | 2 | 2 | `false` | `Main` (branch/active)<br>`Mainm` (branch/active) |
| `RULES` | `pheno` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `PhenoAgent` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `phenoAI` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `PhenoCompose` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `phenoData` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `phenoDesign` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `PhenoDevOps` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `phenodocs` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `PhenoHandbook` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `PhenoKits` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `phenokits-landing` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `PhenoLang` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `PhenoMCP` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `PhenoObservability` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `PhenoPlugins` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `PhenoProc` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `PhenoProject` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `PhenoRuntime` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `phenoShared` | 2 | 2 | `false` | `Main` (branch/active)<br>`Main Governance Baseline` (branch/active) |
| `RULES` | `PhenoSpecs` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `phenotype-auth-ts` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `phenotype-hub` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `phenotype-infra` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `phenotype-registry` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `phenotype-tooling` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `phenoUtils` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `PhenoVCS` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `phenoXdd` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `PlatformKit` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `PlayCua` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `PolicyStack` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `portage` | 2 | 2 | `false` | `Main` (branch/active)<br>`Mainm` (branch/active) |
| `RULES` | `projects-landing` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `ResilienceKit` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `Stashly` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `Tasken` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `TestingKit` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `thegent` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `Tokn` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `Tracera` | 1 | 1 | `false` | `Main` (branch/active) |
| `RULES` | `vibeproxy-monitoring-unified` | 1 | 1 | `false` | `Main` (branch/active) |
