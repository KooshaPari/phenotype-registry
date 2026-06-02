# CHANGELOG Coverage Audit - 2026-04-27

API-only audit of non-archived `KooshaPari/*` repositories.

## Method

- Repository source: `gh repo list KooshaPari --limit 1000 --json name,isArchived,visibility,updatedAt,pushedAt` with `isArchived == false`.
- Presence: `gh api repos/KooshaPari/<repo>/contents/CHANGELOG.md`; HTTP 200 means present.
- Recency: `gh api repos/KooshaPari/<repo>/commits?path=CHANGELOG.md --jq '.[0].commit.author.date'`.
- Stale cutoff: last modified before `2026-02-26T08:22:19Z` (>60 days before generation).
- Generated at: `2026-04-27T08:22:19Z`.
- Sorting: missing first, then stale, unknown, current; alphabetical within each status.

## Summary

| Metric | Count |
|---|---:|
| Non-archived repos audited | 103 |
| `CHANGELOG.md` present | 81 |
| `CHANGELOG.md` missing | 22 |
| Coverage | 78.6% |
| Current (<=60 days) | 79 |
| Stale (>60 days) | 2 |
| Unknown last modified | 0 |

## Repositories

| Status | Repository | has_CHANGELOG | last_modified | age_days | Visibility |
|---|---|---:|---|---:|---|
| MISSING | `KooshaPari/agent-devops-setups` | no | - | - | PUBLIC |
| MISSING | `KooshaPari/agileplus-landing` | no | - | - | PUBLIC |
| MISSING | `KooshaPari/byteport-landing` | no | - | - | PUBLIC |
| MISSING | `KooshaPari/dinoforge-packs` | no | - | - | PUBLIC |
| MISSING | `KooshaPari/DINOForge-UnityDoorstop` | no | - | - | PUBLIC |
| MISSING | `KooshaPari/eyetracker` | no | - | - | PUBLIC |
| MISSING | `KooshaPari/foqos-private` | no | - | - | PRIVATE |
| MISSING | `KooshaPari/hwledger-landing` | no | - | - | PUBLIC |
| MISSING | `KooshaPari/MCPForge` | no | - | - | PUBLIC |
| MISSING | `KooshaPari/phenokits-landing` | no | - | - | PUBLIC |
| MISSING | `KooshaPari/PhenoProject` | no | - | - | PUBLIC |
| MISSING | `KooshaPari/PhenoSpecs` | no | - | - | PUBLIC |
| MISSING | `KooshaPari/phenotype-auth-ts` | no | - | - | PUBLIC |
| MISSING | `KooshaPari/phenotype-hub` | no | - | - | PUBLIC |
| MISSING | `KooshaPari/phenotype-omlx` | no | - | - | PUBLIC |
| MISSING | `KooshaPari/phenotype-ops-mcp` | no | - | - | PUBLIC |
| MISSING | `KooshaPari/phenotype-org-governance` | no | - | - | PRIVATE |
| MISSING | `KooshaPari/phenotype-registry` | no | - | - | PUBLIC |
| MISSING | `KooshaPari/Planify` | no | - | - | PUBLIC |
| MISSING | `KooshaPari/projects-landing` | no | - | - | PUBLIC |
| MISSING | `KooshaPari/thegent-landing` | no | - | - | PUBLIC |
| MISSING | `KooshaPari/vibeproxy-monitoring-unified` | no | - | - | PUBLIC |
| STALE | `KooshaPari/GDK` | yes | 2025-07-10T21:32:25Z | 290 | PUBLIC |
| STALE | `KooshaPari/helios-router` | yes | 2026-02-23T10:56:09Z | 62 | PRIVATE |
| CURRENT | `KooshaPari/agent-user-status` | yes | 2026-04-27T03:15:03Z | 0 | PRIVATE |
| CURRENT | `KooshaPari/agentapi-plusplus` | yes | 2026-03-29T15:32:39Z | 28 | PUBLIC |
| CURRENT | `KooshaPari/AgentMCP` | yes | 2026-04-26T21:57:50Z | 0 | PUBLIC |
| CURRENT | `KooshaPari/Agentora` | yes | 2026-04-26T22:44:50Z | 0 | PUBLIC |
| CURRENT | `KooshaPari/AgilePlus` | yes | 2026-03-31T03:23:45Z | 27 | PUBLIC |
| CURRENT | `KooshaPari/Apisync` | yes | 2026-04-26T22:44:52Z | 0 | PUBLIC |
| CURRENT | `KooshaPari/argis-extensions` | yes | 2026-04-26T22:44:57Z | 0 | PUBLIC |
| CURRENT | `KooshaPari/AuthKit` | yes | 2026-04-24T22:32:28Z | 2 | PUBLIC |
| CURRENT | `KooshaPari/Benchora` | yes | 2026-04-26T21:59:21Z | 0 | PUBLIC |
| CURRENT | `KooshaPari/BytePort` | yes | 2026-04-24T22:50:58Z | 2 | PUBLIC |
| CURRENT | `KooshaPari/cheap-llm-mcp` | yes | 2026-04-23T04:35:24Z | 4 | PRIVATE |
| CURRENT | `KooshaPari/Civis` | yes | 2026-04-24T22:50:00Z | 2 | PRIVATE |
| CURRENT | `KooshaPari/cliproxyapi-plusplus` | yes | 2026-03-29T15:44:32Z | 28 | PUBLIC |
| CURRENT | `KooshaPari/Configra` | yes | 2026-04-24T22:50:32Z | 2 | PRIVATE |
| CURRENT | `KooshaPari/Conft` | yes | 2026-04-24T20:29:23Z | 2 | PUBLIC |
| CURRENT | `KooshaPari/DataKit` | yes | 2026-04-26T00:36:19Z | 1 | PUBLIC |
| CURRENT | `KooshaPari/DevHex` | yes | 2026-04-26T21:57:44Z | 0 | PUBLIC |
| CURRENT | `KooshaPari/Dino` | yes | 2026-04-24T05:22:57Z | 3 | PUBLIC |
| CURRENT | `KooshaPari/Eidolon` | yes | 2026-04-24T20:45:48Z | 2 | PRIVATE |
| CURRENT | `KooshaPari/FocalPoint` | yes | 2026-04-26T03:03:33Z | 1 | PUBLIC |
| CURRENT | `KooshaPari/helios-cli` | yes | 2026-03-25T07:59:43Z | 33 | PUBLIC |
| CURRENT | `KooshaPari/heliosApp` | yes | 2026-04-26T01:05:32Z | 1 | PUBLIC |
| CURRENT | `KooshaPari/heliosBench` | yes | 2026-04-27T03:15:09Z | 0 | PUBLIC |
| CURRENT | `KooshaPari/heliosCLI` | yes | 2026-04-25T15:23:36Z | 1 | PUBLIC |
| CURRENT | `KooshaPari/HeliosLab` | yes | 2026-04-25T15:57:13Z | 1 | PUBLIC |
| CURRENT | `KooshaPari/HexaKit` | yes | 2026-03-30T22:15:32Z | 27 | PUBLIC |
| CURRENT | `KooshaPari/Httpora` | yes | 2026-04-02T21:20:34Z | 24 | PUBLIC |
| CURRENT | `KooshaPari/hwLedger` | yes | 2026-04-24T22:52:08Z | 2 | PUBLIC |
| CURRENT | `KooshaPari/KDesktopVirt` | yes | 2026-04-26T02:55:24Z | 1 | PRIVATE |
| CURRENT | `KooshaPari/McpKit` | yes | 2026-04-24T22:51:13Z | 2 | PUBLIC |
| CURRENT | `KooshaPari/Metron` | yes | 2026-04-26T22:44:55Z | 0 | PUBLIC |
| CURRENT | `KooshaPari/nanovms` | yes | 2026-04-26T21:59:13Z | 0 | PUBLIC |
| CURRENT | `KooshaPari/ObservabilityKit` | yes | 2026-04-26T21:57:35Z | 0 | PUBLIC |
| CURRENT | `KooshaPari/Paginary` | yes | 2026-04-24T20:44:37Z | 2 | PRIVATE |
| CURRENT | `KooshaPari/Parpoura` | yes | 2026-04-24T22:50:40Z | 2 | PRIVATE |
| CURRENT | `KooshaPari/pheno` | yes | 2026-03-30T22:15:32Z | 27 | PUBLIC |
| CURRENT | `KooshaPari/PhenoAgent` | yes | 2026-04-26T21:59:24Z | 0 | PUBLIC |
| CURRENT | `KooshaPari/phenoAI` | yes | 2026-04-24T22:52:00Z | 2 | PUBLIC |
| CURRENT | `KooshaPari/PhenoCompose` | yes | 2026-04-24T19:54:55Z | 2 | PUBLIC |
| CURRENT | `KooshaPari/phenoData` | yes | 2026-04-26T22:45:12Z | 0 | PUBLIC |
| CURRENT | `KooshaPari/phenoDesign` | yes | 2026-04-26T22:45:04Z | 0 | PUBLIC |
| CURRENT | `KooshaPari/PhenoDevOps` | yes | 2026-04-24T22:35:53Z | 2 | PUBLIC |
| CURRENT | `KooshaPari/phenodocs` | yes | 2026-04-05T13:52:16Z | 21 | PUBLIC |
| CURRENT | `KooshaPari/PhenoHandbook` | yes | 2026-04-24T22:35:53Z | 2 | PUBLIC |
| CURRENT | `KooshaPari/PhenoKits` | yes | 2026-04-24T22:51:21Z | 2 | PUBLIC |
| CURRENT | `KooshaPari/PhenoLang` | yes | 2026-03-30T22:15:32Z | 27 | PUBLIC |
| CURRENT | `KooshaPari/PhenoMCP` | yes | 2026-04-26T21:59:26Z | 0 | PUBLIC |
| CURRENT | `KooshaPari/PhenoObservability` | yes | 2026-04-26T07:59:07Z | 1 | PUBLIC |
| CURRENT | `KooshaPari/PhenoPlugins` | yes | 2026-04-24T22:35:55Z | 2 | PUBLIC |
| CURRENT | `KooshaPari/PhenoProc` | yes | 2026-04-26T04:41:27Z | 1 | PUBLIC |
| CURRENT | `KooshaPari/phenoResearchEngine` | yes | 2026-04-26T22:45:09Z | 0 | PRIVATE |
| CURRENT | `KooshaPari/PhenoRuntime` | yes | 2026-04-24T22:52:16Z | 2 | PUBLIC |
| CURRENT | `KooshaPari/phenoShared` | yes | 2026-03-29T14:04:18Z | 28 | PUBLIC |
| CURRENT | `KooshaPari/phenotype-bus` | yes | 2026-04-24T22:35:58Z | 2 | PRIVATE |
| CURRENT | `KooshaPari/phenotype-infra` | yes | 2026-04-24T22:52:51Z | 2 | PUBLIC |
| CURRENT | `KooshaPari/phenotype-journeys` | yes | 2026-04-26T22:45:00Z | 0 | PRIVATE |
| CURRENT | `KooshaPari/phenotype-org-audits` | yes | 2026-04-24T22:18:53Z | 2 | PRIVATE |
| CURRENT | `KooshaPari/phenotype-tooling` | yes | 2026-04-24T22:52:44Z | 2 | PUBLIC |
| CURRENT | `KooshaPari/phenoUtils` | yes | 2026-04-26T22:45:06Z | 0 | PUBLIC |
| CURRENT | `KooshaPari/PhenoVCS` | yes | 2026-04-24T22:52:24Z | 2 | PUBLIC |
| CURRENT | `KooshaPari/phenoXdd` | yes | 2026-04-24T22:52:31Z | 2 | PUBLIC |
| CURRENT | `KooshaPari/PlatformKit` | yes | 2026-04-27T03:15:06Z | 0 | PUBLIC |
| CURRENT | `KooshaPari/PlayCua` | yes | 2026-04-24T22:36:02Z | 2 | PUBLIC |
| CURRENT | `KooshaPari/PolicyStack` | yes | 2026-04-26T03:55:14Z | 1 | PUBLIC |
| CURRENT | `KooshaPari/portage` | yes | 2026-03-25T01:51:37Z | 33 | PUBLIC |
| CURRENT | `KooshaPari/QuadSGM` | yes | 2026-04-24T22:50:49Z | 2 | PRIVATE |
| CURRENT | `KooshaPari/ResilienceKit` | yes | 2026-04-24T22:36:02Z | 2 | PUBLIC |
| CURRENT | `KooshaPari/rich-cli-kit` | yes | 2026-04-24T22:36:03Z | 2 | PRIVATE |
| CURRENT | `KooshaPari/Sidekick` | yes | 2026-04-24T18:14:49Z | 2 | PRIVATE |
| CURRENT | `KooshaPari/Stashly` | yes | 2026-04-02T10:26:18Z | 24 | PUBLIC |
| CURRENT | `KooshaPari/Tasken` | yes | 2026-03-25T15:58:19Z | 32 | PUBLIC |
| CURRENT | `KooshaPari/TestingKit` | yes | 2026-04-26T21:59:29Z | 0 | PUBLIC |
| CURRENT | `KooshaPari/thegent-dispatch` | yes | 2026-04-24T22:36:03Z | 2 | PRIVATE |
| CURRENT | `KooshaPari/thegent-workspace` | yes | 2026-04-24T22:36:04Z | 2 | PRIVATE |
| CURRENT | `KooshaPari/thegent` | yes | 2026-03-31T02:09:16Z | 27 | PUBLIC |
| CURRENT | `KooshaPari/Tokn` | yes | 2026-04-26T03:55:33Z | 1 | PUBLIC |
| CURRENT | `KooshaPari/Tracely` | yes | 2026-04-24T22:36:04Z | 2 | PRIVATE |
| CURRENT | `KooshaPari/Tracera` | yes | 2026-02-27T08:18:19Z | 59 | PUBLIC |
| CURRENT | `KooshaPari/vibeproxy` | yes | 2026-03-29T11:32:55Z | 28 | PUBLIC |
