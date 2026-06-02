# Repo Size + .gitignore Hygiene Audit - 2026-04-27

Scope: non-archived repositories under `KooshaPari`.

Data collection:
- `size_kb`: `gh api repos/KooshaPari/$repo --jq '.size'`
- `.gitignore`: `gh api repos/KooshaPari/$repo/contents/.gitignore`
- `gitignore_lines`: decoded `.gitignore` content counted with `wc -l` semantics

## Summary

- Repositories audited: 103
- Repositories over 100000 KB: 11
- Repositories missing `.gitignore`: 36
- Total flagged repositories: 47

## Flagged Repositories

| Repo | size_kb | has_gitignore | gitignore_lines | flags |
| --- | ---: | --- | ---: | --- |
| `PhenoKits` | 1085656 | yes | 42 | VERY_LARGE |
| `Tracera` | 1050733 | yes | 166 | VERY_LARGE |
| `thegent` | 993944 | yes | 156 | VERY_LARGE |
| `vibeproxy` | 764639 | yes | 304 | VERY_LARGE |
| `hwLedger` | 526532 | yes | 80 | VERY_LARGE |
| `Dino` | 525936 | yes | 152 | VERY_LARGE |
| `BytePort` | 285536 | yes | 23 | VERY_LARGE |
| `helios-cli` | 276466 | yes | 92 | VERY_LARGE |
| `GDK` | 249332 | yes | 19 | VERY_LARGE |
| `cliproxyapi-plusplus` | 244673 | yes | 83 | VERY_LARGE |
| `Planify` | 139454 | yes | 126 | VERY_LARGE |
| `PhenoProject` | 30351 | no | n/a | MISSING_GITIGNORE |
| `KDesktopVirt` | 29379 | no | n/a | MISSING_GITIGNORE |
| `PhenoProc` | 11155 | no | n/a | MISSING_GITIGNORE |
| `Paginary` | 1983 | no | n/a | MISSING_GITIGNORE |
| `PhenoSpecs` | 1601 | no | n/a | MISSING_GITIGNORE |
| `phenoXdd` | 729 | no | n/a | MISSING_GITIGNORE |
| `PhenoObservability` | 658 | no | n/a | MISSING_GITIGNORE |
| `phenotype-org-governance` | 433 | no | n/a | MISSING_GITIGNORE |
| `nanovms` | 228 | no | n/a | MISSING_GITIGNORE |
| `PhenoCompose` | 211 | no | n/a | MISSING_GITIGNORE |
| `PhenoHandbook` | 207 | no | n/a | MISSING_GITIGNORE |
| `PhenoAgent` | 199 | no | n/a | MISSING_GITIGNORE |
| `PhenoPlugins` | 165 | no | n/a | MISSING_GITIGNORE |
| `Tracely` | 158 | no | n/a | MISSING_GITIGNORE |
| `PhenoDevOps` | 157 | no | n/a | MISSING_GITIGNORE |
| `PhenoRuntime` | 144 | no | n/a | MISSING_GITIGNORE |
| `Conft` | 123 | no | n/a | MISSING_GITIGNORE |
| `PlatformKit` | 122 | no | n/a | MISSING_GITIGNORE |
| `PhenoMCP` | 109 | no | n/a | MISSING_GITIGNORE |
| `PhenoVCS` | 88 | no | n/a | MISSING_GITIGNORE |
| `eyetracker` | 60 | no | n/a | MISSING_GITIGNORE |
| `rich-cli-kit` | 54 | no | n/a | MISSING_GITIGNORE |
| `DevHex` | 50 | no | n/a | MISSING_GITIGNORE |
| `Sidekick` | 49 | no | n/a | MISSING_GITIGNORE |
| `Benchora` | 43 | no | n/a | MISSING_GITIGNORE |
| `phenoAI` | 40 | no | n/a | MISSING_GITIGNORE |
| `phenoData` | 37 | no | n/a | MISSING_GITIGNORE |
| `thegent-workspace` | 36 | no | n/a | MISSING_GITIGNORE |
| `dinoforge-packs` | 35 | no | n/a | MISSING_GITIGNORE |
| `phenoUtils` | 30 | no | n/a | MISSING_GITIGNORE |
| `phenotype-bus` | 29 | no | n/a | MISSING_GITIGNORE |
| `phenotype-registry` | 23 | no | n/a | MISSING_GITIGNORE |
| `vibeproxy-monitoring-unified` | 23 | no | n/a | MISSING_GITIGNORE |
| `AgentMCP` | 19 | no | n/a | MISSING_GITIGNORE |
| `phenotype-hub` | 17 | no | n/a | MISSING_GITIGNORE |
| `thegent-dispatch` | 13 | no | n/a | MISSING_GITIGNORE |

## All Non-Archived Repositories

Sorted largest first.

| Rank | Repo | size_kb | has_gitignore | gitignore_lines | flags |
| ---: | --- | ---: | --- | ---: | --- |
| 1 | `PhenoKits` | 1085656 | yes | 42 | VERY_LARGE |
| 2 | `Tracera` | 1050733 | yes | 166 | VERY_LARGE |
| 3 | `thegent` | 993944 | yes | 156 | VERY_LARGE |
| 4 | `vibeproxy` | 764639 | yes | 304 | VERY_LARGE |
| 5 | `hwLedger` | 526532 | yes | 80 | VERY_LARGE |
| 6 | `Dino` | 525936 | yes | 152 | VERY_LARGE |
| 7 | `BytePort` | 285536 | yes | 23 | VERY_LARGE |
| 8 | `helios-cli` | 276466 | yes | 92 | VERY_LARGE |
| 9 | `GDK` | 249332 | yes | 19 | VERY_LARGE |
| 10 | `cliproxyapi-plusplus` | 244673 | yes | 83 | VERY_LARGE |
| 11 | `Planify` | 139454 | yes | 126 | VERY_LARGE |
| 12 | `FocalPoint` | 67719 | yes | 39 |  |
| 13 | `phenotype-omlx` | 40610 | yes | 115 |  |
| 14 | `AgilePlus` | 35008 | yes | 21 |  |
| 15 | `PhenoProject` | 30351 | no | n/a | MISSING_GITIGNORE |
| 16 | `agentapi-plusplus` | 29527 | yes | 88 |  |
| 17 | `KDesktopVirt` | 29379 | no | n/a | MISSING_GITIGNORE |
| 18 | `heliosCLI` | 27246 | yes | 96 |  |
| 19 | `HexaKit` | 21126 | yes | 213 |  |
| 20 | `helios-router` | 19979 | yes | 15 |  |
| 21 | `foqos-private` | 17004 | yes | 62 |  |
| 22 | `pheno` | 14006 | yes | 213 |  |
| 23 | `PhenoLang` | 13711 | yes | 212 |  |
| 24 | `PolicyStack` | 11687 | yes | 15 |  |
| 25 | `PhenoProc` | 11155 | no | n/a | MISSING_GITIGNORE |
| 26 | `HeliosLab` | 11009 | yes | 55 |  |
| 27 | `Civis` | 9416 | yes | 38 |  |
| 28 | `portage` | 8894 | yes | 233 |  |
| 29 | `argis-extensions` | 7121 | yes | 309 |  |
| 30 | `heliosApp` | 6264 | yes | 37 |  |
| 31 | `QuadSGM` | 5636 | yes | 62 |  |
| 32 | `Parpoura` | 4348 | yes | 36 |  |
| 33 | `MCPForge` | 2562 | yes | 19 |  |
| 34 | `McpKit` | 2385 | yes | 52 |  |
| 35 | `Paginary` | 1983 | no | n/a | MISSING_GITIGNORE |
| 36 | `PhenoSpecs` | 1601 | no | n/a | MISSING_GITIGNORE |
| 37 | `Tokn` | 986 | yes | 24 |  |
| 38 | `phenoXdd` | 729 | no | n/a | MISSING_GITIGNORE |
| 39 | `PhenoObservability` | 658 | no | n/a | MISSING_GITIGNORE |
| 40 | `TestingKit` | 568 | yes | 3 |  |
| 41 | `DINOForge-UnityDoorstop` | 507 | yes | 13 |  |
| 42 | `phenoShared` | 483 | yes | 17 |  |
| 43 | `phenodocs` | 450 | yes | 54 |  |
| 44 | `phenotype-org-governance` | 433 | no | n/a | MISSING_GITIGNORE |
| 45 | `agent-user-status` | 427 | yes | 13 |  |
| 46 | `AuthKit` | 425 | yes | 52 |  |
| 47 | `agent-devops-setups` | 394 | yes | 12 |  |
| 48 | `phenotype-journeys` | 315 | yes | 5 |  |
| 49 | `phenoDesign` | 277 | yes | 20 |  |
| 50 | `nanovms` | 228 | no | n/a | MISSING_GITIGNORE |
| 51 | `phenotype-auth-ts` | 220 | yes | 3 |  |
| 52 | `Configra` | 218 | yes | 23 |  |
| 53 | `phenotype-infra` | 217 | yes | 86 |  |
| 54 | `PlayCua` | 212 | yes | 51 |  |
| 55 | `PhenoCompose` | 211 | no | n/a | MISSING_GITIGNORE |
| 56 | `PhenoHandbook` | 207 | no | n/a | MISSING_GITIGNORE |
| 57 | `PhenoAgent` | 199 | no | n/a | MISSING_GITIGNORE |
| 58 | `PhenoPlugins` | 165 | no | n/a | MISSING_GITIGNORE |
| 59 | `Tracely` | 158 | no | n/a | MISSING_GITIGNORE |
| 60 | `PhenoDevOps` | 157 | no | n/a | MISSING_GITIGNORE |
| 61 | `PhenoRuntime` | 144 | no | n/a | MISSING_GITIGNORE |
| 62 | `phenotype-tooling` | 140 | yes | 4 |  |
| 63 | `phenotype-org-audits` | 128 | yes | 24 |  |
| 64 | `ResilienceKit` | 125 | yes | 3 |  |
| 65 | `ObservabilityKit` | 124 | yes | 3 |  |
| 66 | `Conft` | 123 | no | n/a | MISSING_GITIGNORE |
| 67 | `PlatformKit` | 122 | no | n/a | MISSING_GITIGNORE |
| 68 | `PhenoMCP` | 109 | no | n/a | MISSING_GITIGNORE |
| 69 | `Tasken` | 109 | yes | 21 |  |
| 70 | `DataKit` | 103 | yes | 3 |  |
| 71 | `Stashly` | 99 | yes | 21 |  |
| 72 | `byteport-landing` | 98 | yes | 9 |  |
| 73 | `heliosBench` | 89 | yes | 3 |  |
| 74 | `PhenoVCS` | 88 | no | n/a | MISSING_GITIGNORE |
| 75 | `thegent-landing` | 88 | yes | 9 |  |
| 76 | `hwledger-landing` | 80 | yes | 9 |  |
| 77 | `phenokits-landing` | 75 | yes | 9 |  |
| 78 | `Apisync` | 71 | yes | 21 |  |
| 79 | `phenoResearchEngine` | 65 | yes | 11 |  |
| 80 | `Agentora` | 62 | yes | 26 |  |
| 81 | `eyetracker` | 60 | no | n/a | MISSING_GITIGNORE |
| 82 | `cheap-llm-mcp` | 59 | yes | 13 |  |
| 83 | `Httpora` | 59 | yes | 21 |  |
| 84 | `agileplus-landing` | 58 | yes | 8 |  |
| 85 | `rich-cli-kit` | 54 | no | n/a | MISSING_GITIGNORE |
| 86 | `projects-landing` | 52 | yes | 10 |  |
| 87 | `DevHex` | 50 | no | n/a | MISSING_GITIGNORE |
| 88 | `Eidolon` | 50 | yes | 9 |  |
| 89 | `Sidekick` | 49 | no | n/a | MISSING_GITIGNORE |
| 90 | `Metron` | 48 | yes | 21 |  |
| 91 | `phenotype-ops-mcp` | 48 | yes | 2 |  |
| 92 | `Benchora` | 43 | no | n/a | MISSING_GITIGNORE |
| 93 | `phenoAI` | 40 | no | n/a | MISSING_GITIGNORE |
| 94 | `phenoData` | 37 | no | n/a | MISSING_GITIGNORE |
| 95 | `thegent-workspace` | 36 | no | n/a | MISSING_GITIGNORE |
| 96 | `dinoforge-packs` | 35 | no | n/a | MISSING_GITIGNORE |
| 97 | `phenoUtils` | 30 | no | n/a | MISSING_GITIGNORE |
| 98 | `phenotype-bus` | 29 | no | n/a | MISSING_GITIGNORE |
| 99 | `phenotype-registry` | 23 | no | n/a | MISSING_GITIGNORE |
| 100 | `vibeproxy-monitoring-unified` | 23 | no | n/a | MISSING_GITIGNORE |
| 101 | `AgentMCP` | 19 | no | n/a | MISSING_GITIGNORE |
| 102 | `phenotype-hub` | 17 | no | n/a | MISSING_GITIGNORE |
| 103 | `thegent-dispatch` | 13 | no | n/a | MISSING_GITIGNORE |
