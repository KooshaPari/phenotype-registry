# GitHub Pages Live Status - 2026-04-27

Scope: non-archived `KooshaPari` repositories from the local same-day inventory in `CHANGELOG_COVERAGE_2026_04_27.md` (103 repos).

Method: GitHub API core rate limit was exhausted before this audit (`remaining: 0`, reset `2026-04-27 02:11:15 MST`), so `gh api repos/KooshaPari/<repo>/pages` source checks were not run. Per fallback instruction, each repo was probed locally with:

`curl -s -o /dev/null -w "%{http_code}" https://kooshapari.github.io/<repo>/`

## Summary

| Metric | Count |
| --- | ---: |
| Non-archived repos audited | 103 |
| Live Pages URLs (HTTP 200) | 14 |
| Gap / not live at project URL | 89 |
| Public gaps | 70 |
| Private gaps | 19 |

Top failure mode: HTTP 404 for all 89 non-live project URLs. This means the fallback probe found no published project Pages site at the canonical `kooshapari.github.io/<repo>/` path for those repos.

## Status Table

| Status | Repo | Visibility | Pages source | Live URL | HTTP |
| --- | --- | --- | --- | --- | ---: |
| GREEN | `KooshaPari/AgilePlus` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/AgilePlus/ | 200 |
| GREEN | `KooshaPari/Civis` | PRIVATE | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/Civis/ | 200 |
| GREEN | `KooshaPari/cliproxyapi-plusplus` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/cliproxyapi-plusplus/ | 200 |
| GREEN | `KooshaPari/Dino` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/Dino/ | 200 |
| GREEN | `KooshaPari/FocalPoint` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/FocalPoint/ | 200 |
| GREEN | `KooshaPari/heliosApp` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/heliosApp/ | 200 |
| GREEN | `KooshaPari/HeliosLab` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/HeliosLab/ | 200 |
| GREEN | `KooshaPari/HexaKit` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/HexaKit/ | 200 |
| GREEN | `KooshaPari/hwLedger` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/hwLedger/ | 200 |
| GREEN | `KooshaPari/Parpoura` | PRIVATE | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/Parpoura/ | 200 |
| GREEN | `KooshaPari/PolicyStack` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/PolicyStack/ | 200 |
| GREEN | `KooshaPari/thegent` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/thegent/ | 200 |
| GREEN | `KooshaPari/Tokn` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/Tokn/ | 200 |
| GREEN | `KooshaPari/Tracera` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/Tracera/ | 200 |
| GAP | `KooshaPari/agent-devops-setups` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/agent-devops-setups/ | 404 |
| GAP | `KooshaPari/agent-user-status` | PRIVATE | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/agent-user-status/ | 404 |
| GAP | `KooshaPari/agentapi-plusplus` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/agentapi-plusplus/ | 404 |
| GAP | `KooshaPari/AgentMCP` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/AgentMCP/ | 404 |
| GAP | `KooshaPari/Agentora` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/Agentora/ | 404 |
| GAP | `KooshaPari/agileplus-landing` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/agileplus-landing/ | 404 |
| GAP | `KooshaPari/Apisync` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/Apisync/ | 404 |
| GAP | `KooshaPari/argis-extensions` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/argis-extensions/ | 404 |
| GAP | `KooshaPari/AuthKit` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/AuthKit/ | 404 |
| GAP | `KooshaPari/Benchora` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/Benchora/ | 404 |
| GAP | `KooshaPari/byteport-landing` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/byteport-landing/ | 404 |
| GAP | `KooshaPari/BytePort` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/BytePort/ | 404 |
| GAP | `KooshaPari/cheap-llm-mcp` | PRIVATE | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/cheap-llm-mcp/ | 404 |
| GAP | `KooshaPari/Configra` | PRIVATE | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/Configra/ | 404 |
| GAP | `KooshaPari/Conft` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/Conft/ | 404 |
| GAP | `KooshaPari/DataKit` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/DataKit/ | 404 |
| GAP | `KooshaPari/DevHex` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/DevHex/ | 404 |
| GAP | `KooshaPari/dinoforge-packs` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/dinoforge-packs/ | 404 |
| GAP | `KooshaPari/DINOForge-UnityDoorstop` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/DINOForge-UnityDoorstop/ | 404 |
| GAP | `KooshaPari/Eidolon` | PRIVATE | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/Eidolon/ | 404 |
| GAP | `KooshaPari/eyetracker` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/eyetracker/ | 404 |
| GAP | `KooshaPari/foqos-private` | PRIVATE | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/foqos-private/ | 404 |
| GAP | `KooshaPari/GDK` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/GDK/ | 404 |
| GAP | `KooshaPari/helios-cli` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/helios-cli/ | 404 |
| GAP | `KooshaPari/helios-router` | PRIVATE | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/helios-router/ | 404 |
| GAP | `KooshaPari/heliosBench` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/heliosBench/ | 404 |
| GAP | `KooshaPari/heliosCLI` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/heliosCLI/ | 404 |
| GAP | `KooshaPari/Httpora` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/Httpora/ | 404 |
| GAP | `KooshaPari/hwledger-landing` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/hwledger-landing/ | 404 |
| GAP | `KooshaPari/KDesktopVirt` | PRIVATE | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/KDesktopVirt/ | 404 |
| GAP | `KooshaPari/MCPForge` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/MCPForge/ | 404 |
| GAP | `KooshaPari/McpKit` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/McpKit/ | 404 |
| GAP | `KooshaPari/Metron` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/Metron/ | 404 |
| GAP | `KooshaPari/nanovms` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/nanovms/ | 404 |
| GAP | `KooshaPari/ObservabilityKit` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/ObservabilityKit/ | 404 |
| GAP | `KooshaPari/Paginary` | PRIVATE | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/Paginary/ | 404 |
| GAP | `KooshaPari/pheno` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/pheno/ | 404 |
| GAP | `KooshaPari/PhenoAgent` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/PhenoAgent/ | 404 |
| GAP | `KooshaPari/phenoAI` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/phenoAI/ | 404 |
| GAP | `KooshaPari/PhenoCompose` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/PhenoCompose/ | 404 |
| GAP | `KooshaPari/phenoData` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/phenoData/ | 404 |
| GAP | `KooshaPari/phenoDesign` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/phenoDesign/ | 404 |
| GAP | `KooshaPari/PhenoDevOps` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/PhenoDevOps/ | 404 |
| GAP | `KooshaPari/phenodocs` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/phenodocs/ | 404 |
| GAP | `KooshaPari/PhenoHandbook` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/PhenoHandbook/ | 404 |
| GAP | `KooshaPari/phenokits-landing` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/phenokits-landing/ | 404 |
| GAP | `KooshaPari/PhenoKits` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/PhenoKits/ | 404 |
| GAP | `KooshaPari/PhenoLang` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/PhenoLang/ | 404 |
| GAP | `KooshaPari/PhenoMCP` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/PhenoMCP/ | 404 |
| GAP | `KooshaPari/PhenoObservability` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/PhenoObservability/ | 404 |
| GAP | `KooshaPari/PhenoPlugins` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/PhenoPlugins/ | 404 |
| GAP | `KooshaPari/PhenoProc` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/PhenoProc/ | 404 |
| GAP | `KooshaPari/PhenoProject` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/PhenoProject/ | 404 |
| GAP | `KooshaPari/phenoResearchEngine` | PRIVATE | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/phenoResearchEngine/ | 404 |
| GAP | `KooshaPari/PhenoRuntime` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/PhenoRuntime/ | 404 |
| GAP | `KooshaPari/phenoShared` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/phenoShared/ | 404 |
| GAP | `KooshaPari/PhenoSpecs` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/PhenoSpecs/ | 404 |
| GAP | `KooshaPari/phenotype-auth-ts` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/phenotype-auth-ts/ | 404 |
| GAP | `KooshaPari/phenotype-bus` | PRIVATE | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/phenotype-bus/ | 404 |
| GAP | `KooshaPari/phenotype-hub` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/phenotype-hub/ | 404 |
| GAP | `KooshaPari/phenotype-infra` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/phenotype-infra/ | 404 |
| GAP | `KooshaPari/phenotype-journeys` | PRIVATE | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/phenotype-journeys/ | 404 |
| GAP | `KooshaPari/phenotype-omlx` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/phenotype-omlx/ | 404 |
| GAP | `KooshaPari/phenotype-ops-mcp` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/phenotype-ops-mcp/ | 404 |
| GAP | `KooshaPari/phenotype-org-audits` | PRIVATE | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/phenotype-org-audits/ | 404 |
| GAP | `KooshaPari/phenotype-org-governance` | PRIVATE | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/phenotype-org-governance/ | 404 |
| GAP | `KooshaPari/phenotype-registry` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/phenotype-registry/ | 404 |
| GAP | `KooshaPari/phenotype-tooling` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/phenotype-tooling/ | 404 |
| GAP | `KooshaPari/phenoUtils` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/phenoUtils/ | 404 |
| GAP | `KooshaPari/PhenoVCS` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/PhenoVCS/ | 404 |
| GAP | `KooshaPari/phenoXdd` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/phenoXdd/ | 404 |
| GAP | `KooshaPari/Planify` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/Planify/ | 404 |
| GAP | `KooshaPari/PlatformKit` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/PlatformKit/ | 404 |
| GAP | `KooshaPari/PlayCua` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/PlayCua/ | 404 |
| GAP | `KooshaPari/portage` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/portage/ | 404 |
| GAP | `KooshaPari/projects-landing` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/projects-landing/ | 404 |
| GAP | `KooshaPari/QuadSGM` | PRIVATE | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/QuadSGM/ | 404 |
| GAP | `KooshaPari/ResilienceKit` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/ResilienceKit/ | 404 |
| GAP | `KooshaPari/rich-cli-kit` | PRIVATE | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/rich-cli-kit/ | 404 |
| GAP | `KooshaPari/Sidekick` | PRIVATE | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/Sidekick/ | 404 |
| GAP | `KooshaPari/Stashly` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/Stashly/ | 404 |
| GAP | `KooshaPari/Tasken` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/Tasken/ | 404 |
| GAP | `KooshaPari/TestingKit` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/TestingKit/ | 404 |
| GAP | `KooshaPari/thegent-dispatch` | PRIVATE | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/thegent-dispatch/ | 404 |
| GAP | `KooshaPari/thegent-landing` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/thegent-landing/ | 404 |
| GAP | `KooshaPari/thegent-workspace` | PRIVATE | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/thegent-workspace/ | 404 |
| GAP | `KooshaPari/Tracely` | PRIVATE | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/Tracely/ | 404 |
| GAP | `KooshaPari/vibeproxy-monitoring-unified` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/vibeproxy-monitoring-unified/ | 404 |
| GAP | `KooshaPari/vibeproxy` | PUBLIC | not_checked_rate_limit_exhausted_raw_probe | https://kooshapari.github.io/vibeproxy/ | 404 |
