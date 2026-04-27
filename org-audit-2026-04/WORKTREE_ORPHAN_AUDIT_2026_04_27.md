# Worktree Orphan Audit - 2026-04-27

Scope: local-only audit under `/Users/kooshapari/CodeProjects/Phenotype/repos`. No files were removed.

Method:
1. Ran `find /Users/kooshapari/CodeProjects/Phenotype/repos -maxdepth 3 -type d -name ".worktrees"`.
2. Counted immediate subdirectories inside each `.worktrees` directory.
3. Recorded the oldest immediate subdirectory by filesystem mtime.
4. Compared immediate subdirectory real paths with `git -C <repo> worktree list --porcelain`.
5. Marked filesystem entries absent from Git registration as ORPHAN. If `git worktree list` failed for the parent, all immediate entries are listed as unregistered candidates with the Git error.

## Summary

- `.worktrees` directories found: 28
- Directories with orphan/unregistered candidates: 23
- Total orphan/unregistered immediate entries: 489
- Sorted below by orphan count descending.

## Sorted Results

| Rank | Repo | `.worktrees` subdirs | Orphans | Oldest mtime | Oldest path | Git registered | Git status |
|---:|---|---:|---:|---|---|---:|---|
| 1 | `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold` | 124 | 124 | 2026-04-23 20:30:41 -0700 | `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/AgilePlus-docs` | 8 | ok |
| 2 | `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys` | 124 | 124 | 2026-04-23 20:45:44 -0700 | `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/AgilePlus-docs` | 8 | ok |
| 3 | `/Users/kooshapari/CodeProjects/Phenotype/repos` | 111 | 109 | 2026-04-02 06:20:29 -0700 | `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/AgilePlus` | 12 | ok |
| 4 | `/Users/kooshapari/CodeProjects/Phenotype/repos/.archive/p1-test-fixes-2026-04-27-merged-ghost` | 10 | 10 | 2026-04-25 16:05:04 -0700 | `/Users/kooshapari/CodeProjects/Phenotype/repos/.archive/p1-test-fixes-2026-04-27-merged-ghost/.worktrees/chore-governance-baseline` | 33 | ok |
| 5 | `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtr/fix-hooks-canonical` | 10 | 10 | 2026-04-25 12:45:05 -0700 | `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtr/fix-hooks-canonical/.worktrees/chore-governance-baseline` | 33 | ok |
| 6 | `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-cross-bump` | 10 | 10 | 2026-04-25 11:30:23 -0700 | `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-cross-bump/.worktrees/chore-governance-baseline` | 33 | ok |
| 7 | `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-sweep-residual` | 10 | 10 | 2026-04-25 12:21:37 -0700 | `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-sweep-residual/.worktrees/chore-governance-baseline` | 33 | ok |
| 8 | `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dup-route-fix` | 10 | 10 | 2026-04-25 15:08:39 -0700 | `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dup-route-fix/.worktrees/chore-governance-baseline` | 33 | ok |
| 9 | `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/eco-batch-supersede` | 10 | 10 | 2026-04-25 15:14:54 -0700 | `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/eco-batch-supersede/.worktrees/chore-governance-baseline` | 0 | git worktree list failed |
| 10 | `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/pyjwt-fix` | 10 | 10 | 2026-04-25 13:43:54 -0700 | `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/pyjwt-fix/.worktrees/chore-governance-baseline` | 33 | ok |
| 11 | `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/release-cut-adopt` | 10 | 10 | 2026-04-24 16:14:19 -0700 | `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/release-cut-adopt/.worktrees/chore-governance-baseline` | 33 | ok |
| 12 | `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-crate-consolidation` | 10 | 10 | 2026-04-25 15:44:30 -0700 | `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-crate-consolidation/.worktrees/chore-governance-baseline` | 33 | ok |
| 13 | `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-plans-015-019` | 10 | 10 | 2026-04-25 17:45:23 -0700 | `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-plans-015-019/.worktrees/chore-governance-baseline` | 33 | ok |
| 14 | `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dep-high` | 8 | 8 | 2026-04-23 20:45:23 -0700 | `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dep-high/.worktrees/chore-governance-baseline` | 33 | ok |
| 15 | `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dep-pyjwt-lodash` | 8 | 8 | 2026-04-23 21:13:28 -0700 | `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dep-pyjwt-lodash/.worktrees/chore-governance-baseline` | 33 | ok |
| 16 | `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/agileplus-high-npm` | 8 | 8 | 2026-04-23 23:33:49 -0700 | `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/agileplus-high-npm/.worktrees/chore-governance-baseline` | 33 | ok |
| 17 | `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/agentapi-plusplus-docs` | 2 | 2 | 2026-04-02 14:46:01 -0700 | `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/agentapi-plusplus-docs/.worktrees/chore-sast-pin-governance` | 6 | ok |
| 18 | `/Users/kooshapari/CodeProjects/Phenotype/repos/ResilienceKit` | 1 | 1 | 2026-04-25 20:04:42 -0700 | `/Users/kooshapari/CodeProjects/Phenotype/repos/ResilienceKit/.worktrees/fix` | 3 | ok |
| 19 | `/Users/kooshapari/CodeProjects/Phenotype/repos/TestingKit` | 1 | 1 | 2026-04-25 20:05:00 -0700 | `/Users/kooshapari/CodeProjects/Phenotype/repos/TestingKit/.worktrees/fix` | 3 | ok |
| 20 | `/Users/kooshapari/CodeProjects/Phenotype/repos/heliosCLI` | 1 | 1 | 2026-04-24 15:43:27 -0700 | `/Users/kooshapari/CodeProjects/Phenotype/repos/heliosCLI/.worktrees/chore-govern-pi` | 3 | ok |
| 21 | `/Users/kooshapari/CodeProjects/Phenotype/repos/heliosCLI-wtrees/cve-sweep-high` | 1 | 1 | 2026-04-25 10:54:26 -0700 | `/Users/kooshapari/CodeProjects/Phenotype/repos/heliosCLI-wtrees/cve-sweep-high/.worktrees/chore-govern-pi` | 3 | ok |
| 22 | `/Users/kooshapari/CodeProjects/Phenotype/repos/heliosCLI-wtrees/lockfile-regen-2026-04-27` | 1 | 1 | 2026-04-26 21:37:39 -0700 | `/Users/kooshapari/CodeProjects/Phenotype/repos/heliosCLI-wtrees/lockfile-regen-2026-04-27/.worktrees/chore-govern-pi` | 3 | ok |
| 23 | `/Users/kooshapari/CodeProjects/Phenotype/repos/heliosCLI/heliosCLI` | 1 | 1 | 2026-04-24 15:43:32 -0700 | `/Users/kooshapari/CodeProjects/Phenotype/repos/heliosCLI/heliosCLI/.worktrees/governance-pr-ready` | 3 | ok |
| 24 | `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus` | 7 | 0 | 2026-04-02 15:01:03 -0700 | `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus/.worktrees/dashboard-extraction` | 33 | ok |
| 25 | `/Users/kooshapari/CodeProjects/Phenotype/repos/agentapi-plusplus` | 2 | 0 | 2026-04-25 00:36:55 -0700 | `/Users/kooshapari/CodeProjects/Phenotype/repos/agentapi-plusplus/.worktrees/chore-sast-pin-governance` | 6 | ok |
| 26 | `/Users/kooshapari/CodeProjects/Phenotype/repos/cliproxyapi-plusplus` | 2 | 0 | 2026-04-02 15:02:28 -0700 | `/Users/kooshapari/CodeProjects/Phenotype/repos/cliproxyapi-plusplus/.worktrees/pr942-import-surface-fix` | 9 | ok |
| 27 | `/Users/kooshapari/CodeProjects/Phenotype/repos/HeliosLab` | 1 | 0 | 2026-04-27 01:13:22 -0700 | `/Users/kooshapari/CodeProjects/Phenotype/repos/HeliosLab/.worktrees/pages-deadlinks-fix` | 4 | ok |
| 28 | `/Users/kooshapari/CodeProjects/Phenotype/repos/thegent` | 0 | 0 | n/a | n/a | 21 | ok |

## Repos With Orphans

### `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold`

- `.worktrees`: `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees`
- Immediate subdirs: 124
- Orphans/unregistered candidates: 124
- Oldest by mtime: `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/AgilePlus-docs` (2026-04-23 20:30:41 -0700)
- Git registered worktrees: 8

<details><summary>Orphan/unregistered entries</summary>

- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/AgilePlus`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/AgilePlus-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/Apisync-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/Authvault-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/BytePort-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/Cmdra-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/Cursora-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/Datamold-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/Dino-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/Docuverse-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/HexaPy-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/HexaType-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/Httpora-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/KodeVibeGo-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/Kogito-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/Logify`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/Logify-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/Metron`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/Metron-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/Planify-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/PolicyStack-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/Portalis`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/Portalis-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/Profila-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/Queris-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/Quillr-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/Schemaforge-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/Seedloom-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/Settly-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/Stashly-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/Tasken-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/Tokn-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/Tossy-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/Tracera-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/Zerokit-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/agent-devops-setups-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/agent-wave-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/agentapi-plusplus-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/agentops-policy-federation-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/agileplus-agents-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/agileplus-mcp-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/agileplus-plugin-core-clippyfix`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/agileplus-plugin-core-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/agileplus-plugin-git-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/agileplus-plugin-sqlite-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/apps-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/artifacts-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/bare-cua`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/bare-cua-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/bifrost-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/bifrost-extensions-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/clikit-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/cliproxyapi-plusplus-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/cloud-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/cmdra`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/colab-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/cursora`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/devenv-abstraction-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/docuverse`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/feat`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/heliosApp`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/heliosCLI`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/heliosapp-pr362-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/helioscli-pr179-policy-fix`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/hexago`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/hexagon-ts-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/hexagonal-ports`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/integration-015-helioscli-nanovms`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/modules`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/nanovms-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/omniroute-temp-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/org-github-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenodocs-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-agent-core-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-auth-ts-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-cipher-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-cli-extensions-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-config-ts-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-dep-guard-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-design-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-docs-engine-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-evaluation-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-forge-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-gauge-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-go-kit-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-hub-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-infrakit`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-logging-zig-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-middleware-py`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-middleware-py-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-nexus-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-patch-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-research-engine-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-sentinel-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-shared-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-skills-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-task-engine-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-templates-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-tier2-telemetry`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-tier2-testing`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-tier3-infrastructure`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-types-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-vessel-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-xdd-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotype-xdd-lib-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/phenotypeActions-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/portage`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/portage-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/repos-llms-context`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/repos-root-policy-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/sharecli-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/src-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/template-commons-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/template-program-ops-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/tests-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/thegent-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/thegent-pr908-policy-fix`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/thegent-sharecli-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/tooling-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/tools-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/tracely-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/vibeproxy-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/vibeproxy-monitoring-unified-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold/.worktrees/zen-docs`

</details>

### `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys`

- `.worktrees`: `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees`
- Immediate subdirs: 124
- Orphans/unregistered candidates: 124
- Oldest by mtime: `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/AgilePlus-docs` (2026-04-23 20:45:44 -0700)
- Git registered worktrees: 8

<details><summary>Orphan/unregistered entries</summary>

- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/AgilePlus`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/AgilePlus-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/Apisync-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/Authvault-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/BytePort-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/Cmdra-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/Cursora-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/Datamold-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/Dino-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/Docuverse-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/HexaPy-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/HexaType-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/Httpora-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/KodeVibeGo-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/Kogito-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/Logify`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/Logify-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/Metron`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/Metron-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/Planify-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/PolicyStack-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/Portalis`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/Portalis-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/Profila-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/Queris-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/Quillr-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/Schemaforge-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/Seedloom-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/Settly-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/Stashly-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/Tasken-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/Tokn-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/Tossy-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/Tracera-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/Zerokit-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/agent-devops-setups-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/agent-wave-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/agentapi-plusplus-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/agentops-policy-federation-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/agileplus-agents-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/agileplus-mcp-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/agileplus-plugin-core-clippyfix`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/agileplus-plugin-core-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/agileplus-plugin-git-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/agileplus-plugin-sqlite-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/apps-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/artifacts-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/bare-cua`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/bare-cua-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/bifrost-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/bifrost-extensions-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/clikit-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/cliproxyapi-plusplus-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/cloud-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/cmdra`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/colab-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/cursora`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/devenv-abstraction-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/docuverse`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/feat`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/heliosApp`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/heliosCLI`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/heliosapp-pr362-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/helioscli-pr179-policy-fix`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/hexago`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/hexagon-ts-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/hexagonal-ports`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/integration-015-helioscli-nanovms`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/modules`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/nanovms-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/omniroute-temp-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/org-github-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenodocs-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-agent-core-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-auth-ts-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-cipher-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-cli-extensions-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-config-ts-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-dep-guard-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-design-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-docs-engine-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-evaluation-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-forge-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-gauge-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-go-kit-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-hub-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-infrakit`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-logging-zig-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-middleware-py`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-middleware-py-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-nexus-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-patch-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-research-engine-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-sentinel-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-shared-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-skills-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-task-engine-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-templates-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-tier2-telemetry`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-tier2-testing`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-tier3-infrastructure`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-types-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-vessel-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-xdd-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotype-xdd-lib-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/phenotypeActions-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/portage`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/portage-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/repos-llms-context`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/repos-root-policy-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/sharecli-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/src-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/template-commons-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/template-program-ops-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/tests-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/thegent-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/thegent-pr908-policy-fix`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/thegent-sharecli-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/tooling-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/tools-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/tracely-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/vibeproxy-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/vibeproxy-monitoring-unified-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/dep-nkeys/.worktrees/zen-docs`

</details>

### `/Users/kooshapari/CodeProjects/Phenotype/repos`

- `.worktrees`: `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees`
- Immediate subdirs: 111
- Orphans/unregistered candidates: 109
- Oldest by mtime: `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/AgilePlus` (2026-04-02 06:20:29 -0700)
- Git registered worktrees: 12

<details><summary>Orphan/unregistered entries</summary>

- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/AgilePlus`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/AgilePlus-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/Apisync-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/Authvault-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/BytePort-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/Cmdra-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/Cursora-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/Datamold-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/Dino-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/Docuverse-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/HexaPy-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/HexaType-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/Httpora-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/KodeVibeGo-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/Kogito-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/Logify`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/Logify-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/Metron`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/Metron-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-fix-dependabot`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-forced-adoption-reality`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PhenoKits-tracera-fr-scaffold`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/Planify-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/PolicyStack-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/Portalis`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/Portalis-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/Profila-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/Queris-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/Quillr-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/Schemaforge-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/Seedloom-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/Settly-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/Stashly-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/Tasken-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/Tokn-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/Tossy-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/Tracera-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/Zerokit-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/agent-devops-setups-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/agent-wave-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/agentapi-plusplus-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/agentops-policy-federation-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/agileplus-plugin-core-clippyfix`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/agileplus-plugin-core-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/agileplus-plugin-git-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/agileplus-plugin-sqlite-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/bare-cua`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/bare-cua-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/bifrost-extensions-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/cliproxyapi-plusplus-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/cloud-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/cmdra`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/cursora`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/devenv-abstraction-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/docuverse`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/feat`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/heliosApp`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/heliosapp-pr362-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/helioscli-pr179-policy-fix`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/hexago`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/hexagon-ts-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/modules`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/nanovms-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/omniroute-temp-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/org-github-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenodocs-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-agent-core-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-auth-ts-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-cipher-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-cli-extensions-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-config-ts-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-dep-guard-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-design-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-docs-engine-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-evaluation-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-forge-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-gauge-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-go-kit-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-hub-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-infra-oci-hooks`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-infrakit`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-logging-zig-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-middleware-py`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-middleware-py-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-nexus-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-patch-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-research-engine-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-sentinel-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-shared-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-skills-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-task-engine-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-templates-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-types-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-vessel-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-xdd-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotype-xdd-lib-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/phenotypeActions-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/portage`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/portage-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/sharecli-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/template-commons-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/template-program-ops-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/thegent-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/thegent-pr908-policy-fix`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/thegent-sharecli-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/tracely-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/vibeproxy-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/vibeproxy-monitoring-unified-docs`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/zen-docs`

</details>

### `/Users/kooshapari/CodeProjects/Phenotype/repos/.archive/p1-test-fixes-2026-04-27-merged-ghost`

- `.worktrees`: `/Users/kooshapari/CodeProjects/Phenotype/repos/.archive/p1-test-fixes-2026-04-27-merged-ghost/.worktrees`
- Immediate subdirs: 10
- Orphans/unregistered candidates: 10
- Oldest by mtime: `/Users/kooshapari/CodeProjects/Phenotype/repos/.archive/p1-test-fixes-2026-04-27-merged-ghost/.worktrees/chore-governance-baseline` (2026-04-25 16:05:04 -0700)
- Git registered worktrees: 33

<details><summary>Orphan/unregistered entries</summary>

- `/Users/kooshapari/CodeProjects/Phenotype/repos/.archive/p1-test-fixes-2026-04-27-merged-ghost/.worktrees/chore-governance-baseline`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.archive/p1-test-fixes-2026-04-27-merged-ghost/.worktrees/chore-governance-baseline-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.archive/p1-test-fixes-2026-04-27-merged-ghost/.worktrees/chore-runtime-local-deploy`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.archive/p1-test-fixes-2026-04-27-merged-ghost/.worktrees/chore-runtime-local-deploy-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.archive/p1-test-fixes-2026-04-27-merged-ghost/.worktrees/dashboard-extraction`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.archive/p1-test-fixes-2026-04-27-merged-ghost/.worktrees/dashboard-extraction-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.archive/p1-test-fixes-2026-04-27-merged-ghost/.worktrees/docs-worklog-and-spec-backfill`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.archive/p1-test-fixes-2026-04-27-merged-ghost/.worktrees/docs-worklog-and-spec-backfill-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.archive/p1-test-fixes-2026-04-27-merged-ghost/.worktrees/refactor-cli-event-flow`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.archive/p1-test-fixes-2026-04-27-merged-ghost/.worktrees/refactor-cli-event-flow-clean`

</details>

### `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtr/fix-hooks-canonical`

- `.worktrees`: `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtr/fix-hooks-canonical/.worktrees`
- Immediate subdirs: 10
- Orphans/unregistered candidates: 10
- Oldest by mtime: `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtr/fix-hooks-canonical/.worktrees/chore-governance-baseline` (2026-04-25 12:45:05 -0700)
- Git registered worktrees: 33

<details><summary>Orphan/unregistered entries</summary>

- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtr/fix-hooks-canonical/.worktrees/chore-governance-baseline`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtr/fix-hooks-canonical/.worktrees/chore-governance-baseline-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtr/fix-hooks-canonical/.worktrees/chore-runtime-local-deploy`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtr/fix-hooks-canonical/.worktrees/chore-runtime-local-deploy-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtr/fix-hooks-canonical/.worktrees/dashboard-extraction`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtr/fix-hooks-canonical/.worktrees/dashboard-extraction-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtr/fix-hooks-canonical/.worktrees/docs-worklog-and-spec-backfill`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtr/fix-hooks-canonical/.worktrees/docs-worklog-and-spec-backfill-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtr/fix-hooks-canonical/.worktrees/refactor-cli-event-flow`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtr/fix-hooks-canonical/.worktrees/refactor-cli-event-flow-clean`

</details>

### `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-cross-bump`

- `.worktrees`: `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-cross-bump/.worktrees`
- Immediate subdirs: 10
- Orphans/unregistered candidates: 10
- Oldest by mtime: `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-cross-bump/.worktrees/chore-governance-baseline` (2026-04-25 11:30:23 -0700)
- Git registered worktrees: 33

<details><summary>Orphan/unregistered entries</summary>

- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-cross-bump/.worktrees/chore-governance-baseline`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-cross-bump/.worktrees/chore-governance-baseline-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-cross-bump/.worktrees/chore-runtime-local-deploy`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-cross-bump/.worktrees/chore-runtime-local-deploy-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-cross-bump/.worktrees/dashboard-extraction`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-cross-bump/.worktrees/dashboard-extraction-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-cross-bump/.worktrees/docs-worklog-and-spec-backfill`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-cross-bump/.worktrees/docs-worklog-and-spec-backfill-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-cross-bump/.worktrees/refactor-cli-event-flow`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-cross-bump/.worktrees/refactor-cli-event-flow-clean`

</details>

### `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-sweep-residual`

- `.worktrees`: `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-sweep-residual/.worktrees`
- Immediate subdirs: 10
- Orphans/unregistered candidates: 10
- Oldest by mtime: `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-sweep-residual/.worktrees/chore-governance-baseline` (2026-04-25 12:21:37 -0700)
- Git registered worktrees: 33

<details><summary>Orphan/unregistered entries</summary>

- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-sweep-residual/.worktrees/chore-governance-baseline`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-sweep-residual/.worktrees/chore-governance-baseline-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-sweep-residual/.worktrees/chore-runtime-local-deploy`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-sweep-residual/.worktrees/chore-runtime-local-deploy-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-sweep-residual/.worktrees/dashboard-extraction`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-sweep-residual/.worktrees/dashboard-extraction-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-sweep-residual/.worktrees/docs-worklog-and-spec-backfill`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-sweep-residual/.worktrees/docs-worklog-and-spec-backfill-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-sweep-residual/.worktrees/refactor-cli-event-flow`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/cve-sweep-residual/.worktrees/refactor-cli-event-flow-clean`

</details>

### `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dup-route-fix`

- `.worktrees`: `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dup-route-fix/.worktrees`
- Immediate subdirs: 10
- Orphans/unregistered candidates: 10
- Oldest by mtime: `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dup-route-fix/.worktrees/chore-governance-baseline` (2026-04-25 15:08:39 -0700)
- Git registered worktrees: 33

<details><summary>Orphan/unregistered entries</summary>

- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dup-route-fix/.worktrees/chore-governance-baseline`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dup-route-fix/.worktrees/chore-governance-baseline-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dup-route-fix/.worktrees/chore-runtime-local-deploy`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dup-route-fix/.worktrees/chore-runtime-local-deploy-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dup-route-fix/.worktrees/dashboard-extraction`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dup-route-fix/.worktrees/dashboard-extraction-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dup-route-fix/.worktrees/docs-worklog-and-spec-backfill`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dup-route-fix/.worktrees/docs-worklog-and-spec-backfill-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dup-route-fix/.worktrees/refactor-cli-event-flow`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dup-route-fix/.worktrees/refactor-cli-event-flow-clean`

</details>

### `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/eco-batch-supersede`

- `.worktrees`: `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/eco-batch-supersede/.worktrees`
- Immediate subdirs: 10
- Orphans/unregistered candidates: 10
- Oldest by mtime: `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/eco-batch-supersede/.worktrees/chore-governance-baseline` (2026-04-25 15:14:54 -0700)
- Git registered worktrees: 0
- Git error: `fatal: not a git repository: /Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus/.git/worktrees/eco-batch-supersede`

<details><summary>Orphan/unregistered entries</summary>

- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/eco-batch-supersede/.worktrees/chore-governance-baseline`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/eco-batch-supersede/.worktrees/chore-governance-baseline-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/eco-batch-supersede/.worktrees/chore-runtime-local-deploy`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/eco-batch-supersede/.worktrees/chore-runtime-local-deploy-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/eco-batch-supersede/.worktrees/dashboard-extraction`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/eco-batch-supersede/.worktrees/dashboard-extraction-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/eco-batch-supersede/.worktrees/docs-worklog-and-spec-backfill`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/eco-batch-supersede/.worktrees/docs-worklog-and-spec-backfill-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/eco-batch-supersede/.worktrees/refactor-cli-event-flow`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/eco-batch-supersede/.worktrees/refactor-cli-event-flow-clean`

</details>

### `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/pyjwt-fix`

- `.worktrees`: `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/pyjwt-fix/.worktrees`
- Immediate subdirs: 10
- Orphans/unregistered candidates: 10
- Oldest by mtime: `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/pyjwt-fix/.worktrees/chore-governance-baseline` (2026-04-25 13:43:54 -0700)
- Git registered worktrees: 33

<details><summary>Orphan/unregistered entries</summary>

- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/pyjwt-fix/.worktrees/chore-governance-baseline`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/pyjwt-fix/.worktrees/chore-governance-baseline-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/pyjwt-fix/.worktrees/chore-runtime-local-deploy`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/pyjwt-fix/.worktrees/chore-runtime-local-deploy-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/pyjwt-fix/.worktrees/dashboard-extraction`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/pyjwt-fix/.worktrees/dashboard-extraction-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/pyjwt-fix/.worktrees/docs-worklog-and-spec-backfill`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/pyjwt-fix/.worktrees/docs-worklog-and-spec-backfill-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/pyjwt-fix/.worktrees/refactor-cli-event-flow`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/pyjwt-fix/.worktrees/refactor-cli-event-flow-clean`

</details>

### `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/release-cut-adopt`

- `.worktrees`: `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/release-cut-adopt/.worktrees`
- Immediate subdirs: 10
- Orphans/unregistered candidates: 10
- Oldest by mtime: `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/release-cut-adopt/.worktrees/chore-governance-baseline` (2026-04-24 16:14:19 -0700)
- Git registered worktrees: 33

<details><summary>Orphan/unregistered entries</summary>

- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/release-cut-adopt/.worktrees/chore-governance-baseline`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/release-cut-adopt/.worktrees/chore-governance-baseline-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/release-cut-adopt/.worktrees/chore-runtime-local-deploy`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/release-cut-adopt/.worktrees/chore-runtime-local-deploy-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/release-cut-adopt/.worktrees/dashboard-extraction`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/release-cut-adopt/.worktrees/dashboard-extraction-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/release-cut-adopt/.worktrees/docs-worklog-and-spec-backfill`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/release-cut-adopt/.worktrees/docs-worklog-and-spec-backfill-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/release-cut-adopt/.worktrees/refactor-cli-event-flow`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/release-cut-adopt/.worktrees/refactor-cli-event-flow-clean`

</details>

### `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-crate-consolidation`

- `.worktrees`: `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-crate-consolidation/.worktrees`
- Immediate subdirs: 10
- Orphans/unregistered candidates: 10
- Oldest by mtime: `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-crate-consolidation/.worktrees/chore-governance-baseline` (2026-04-25 15:44:30 -0700)
- Git registered worktrees: 33

<details><summary>Orphan/unregistered entries</summary>

- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-crate-consolidation/.worktrees/chore-governance-baseline`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-crate-consolidation/.worktrees/chore-governance-baseline-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-crate-consolidation/.worktrees/chore-runtime-local-deploy`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-crate-consolidation/.worktrees/chore-runtime-local-deploy-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-crate-consolidation/.worktrees/dashboard-extraction`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-crate-consolidation/.worktrees/dashboard-extraction-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-crate-consolidation/.worktrees/docs-worklog-and-spec-backfill`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-crate-consolidation/.worktrees/docs-worklog-and-spec-backfill-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-crate-consolidation/.worktrees/refactor-cli-event-flow`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-crate-consolidation/.worktrees/refactor-cli-event-flow-clean`

</details>

### `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-plans-015-019`

- `.worktrees`: `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-plans-015-019/.worktrees`
- Immediate subdirs: 10
- Orphans/unregistered candidates: 10
- Oldest by mtime: `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-plans-015-019/.worktrees/chore-governance-baseline` (2026-04-25 17:45:23 -0700)
- Git registered worktrees: 33

<details><summary>Orphan/unregistered entries</summary>

- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-plans-015-019/.worktrees/chore-governance-baseline`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-plans-015-019/.worktrees/chore-governance-baseline-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-plans-015-019/.worktrees/chore-runtime-local-deploy`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-plans-015-019/.worktrees/chore-runtime-local-deploy-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-plans-015-019/.worktrees/dashboard-extraction`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-plans-015-019/.worktrees/dashboard-extraction-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-plans-015-019/.worktrees/docs-worklog-and-spec-backfill`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-plans-015-019/.worktrees/docs-worklog-and-spec-backfill-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-plans-015-019/.worktrees/refactor-cli-event-flow`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/specs-plans-015-019/.worktrees/refactor-cli-event-flow-clean`

</details>

### `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dep-high`

- `.worktrees`: `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dep-high/.worktrees`
- Immediate subdirs: 8
- Orphans/unregistered candidates: 8
- Oldest by mtime: `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dep-high/.worktrees/chore-governance-baseline` (2026-04-23 20:45:23 -0700)
- Git registered worktrees: 33

<details><summary>Orphan/unregistered entries</summary>

- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dep-high/.worktrees/chore-governance-baseline`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dep-high/.worktrees/chore-governance-baseline-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dep-high/.worktrees/chore-runtime-local-deploy`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dep-high/.worktrees/chore-runtime-local-deploy-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dep-high/.worktrees/docs-worklog-and-spec-backfill`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dep-high/.worktrees/docs-worklog-and-spec-backfill-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dep-high/.worktrees/refactor-cli-event-flow`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dep-high/.worktrees/refactor-cli-event-flow-clean`

</details>

### `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dep-pyjwt-lodash`

- `.worktrees`: `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dep-pyjwt-lodash/.worktrees`
- Immediate subdirs: 8
- Orphans/unregistered candidates: 8
- Oldest by mtime: `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dep-pyjwt-lodash/.worktrees/chore-governance-baseline` (2026-04-23 21:13:28 -0700)
- Git registered worktrees: 33

<details><summary>Orphan/unregistered entries</summary>

- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dep-pyjwt-lodash/.worktrees/chore-governance-baseline`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dep-pyjwt-lodash/.worktrees/chore-governance-baseline-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dep-pyjwt-lodash/.worktrees/chore-runtime-local-deploy`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dep-pyjwt-lodash/.worktrees/chore-runtime-local-deploy-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dep-pyjwt-lodash/.worktrees/docs-worklog-and-spec-backfill`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dep-pyjwt-lodash/.worktrees/docs-worklog-and-spec-backfill-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dep-pyjwt-lodash/.worktrees/refactor-cli-event-flow`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus-wtrees/dep-pyjwt-lodash/.worktrees/refactor-cli-event-flow-clean`

</details>

### `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/agileplus-high-npm`

- `.worktrees`: `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/agileplus-high-npm/.worktrees`
- Immediate subdirs: 8
- Orphans/unregistered candidates: 8
- Oldest by mtime: `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/agileplus-high-npm/.worktrees/chore-governance-baseline` (2026-04-23 23:33:49 -0700)
- Git registered worktrees: 33

<details><summary>Orphan/unregistered entries</summary>

- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/agileplus-high-npm/.worktrees/chore-governance-baseline`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/agileplus-high-npm/.worktrees/chore-governance-baseline-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/agileplus-high-npm/.worktrees/chore-runtime-local-deploy`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/agileplus-high-npm/.worktrees/chore-runtime-local-deploy-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/agileplus-high-npm/.worktrees/docs-worklog-and-spec-backfill`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/agileplus-high-npm/.worktrees/docs-worklog-and-spec-backfill-clean`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/agileplus-high-npm/.worktrees/refactor-cli-event-flow`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/repos-wtrees/agileplus-high-npm/.worktrees/refactor-cli-event-flow-clean`

</details>

### `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/agentapi-plusplus-docs`

- `.worktrees`: `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/agentapi-plusplus-docs/.worktrees`
- Immediate subdirs: 2
- Orphans/unregistered candidates: 2
- Oldest by mtime: `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/agentapi-plusplus-docs/.worktrees/chore-sast-pin-governance` (2026-04-02 14:46:01 -0700)
- Git registered worktrees: 6

<details><summary>Orphan/unregistered entries</summary>

- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/agentapi-plusplus-docs/.worktrees/chore-sast-pin-governance`
- `/Users/kooshapari/CodeProjects/Phenotype/repos/.worktrees/agentapi-plusplus-docs/.worktrees/chore-sast-pin-governance-clean`

</details>

### `/Users/kooshapari/CodeProjects/Phenotype/repos/ResilienceKit`

- `.worktrees`: `/Users/kooshapari/CodeProjects/Phenotype/repos/ResilienceKit/.worktrees`
- Immediate subdirs: 1
- Orphans/unregistered candidates: 1
- Oldest by mtime: `/Users/kooshapari/CodeProjects/Phenotype/repos/ResilienceKit/.worktrees/fix` (2026-04-25 20:04:42 -0700)
- Git registered worktrees: 3

<details><summary>Orphan/unregistered entries</summary>

- `/Users/kooshapari/CodeProjects/Phenotype/repos/ResilienceKit/.worktrees/fix`

</details>

### `/Users/kooshapari/CodeProjects/Phenotype/repos/TestingKit`

- `.worktrees`: `/Users/kooshapari/CodeProjects/Phenotype/repos/TestingKit/.worktrees`
- Immediate subdirs: 1
- Orphans/unregistered candidates: 1
- Oldest by mtime: `/Users/kooshapari/CodeProjects/Phenotype/repos/TestingKit/.worktrees/fix` (2026-04-25 20:05:00 -0700)
- Git registered worktrees: 3

<details><summary>Orphan/unregistered entries</summary>

- `/Users/kooshapari/CodeProjects/Phenotype/repos/TestingKit/.worktrees/fix`

</details>

### `/Users/kooshapari/CodeProjects/Phenotype/repos/heliosCLI`

- `.worktrees`: `/Users/kooshapari/CodeProjects/Phenotype/repos/heliosCLI/.worktrees`
- Immediate subdirs: 1
- Orphans/unregistered candidates: 1
- Oldest by mtime: `/Users/kooshapari/CodeProjects/Phenotype/repos/heliosCLI/.worktrees/chore-govern-pi` (2026-04-24 15:43:27 -0700)
- Git registered worktrees: 3

<details><summary>Orphan/unregistered entries</summary>

- `/Users/kooshapari/CodeProjects/Phenotype/repos/heliosCLI/.worktrees/chore-govern-pi`

</details>

### `/Users/kooshapari/CodeProjects/Phenotype/repos/heliosCLI-wtrees/cve-sweep-high`

- `.worktrees`: `/Users/kooshapari/CodeProjects/Phenotype/repos/heliosCLI-wtrees/cve-sweep-high/.worktrees`
- Immediate subdirs: 1
- Orphans/unregistered candidates: 1
- Oldest by mtime: `/Users/kooshapari/CodeProjects/Phenotype/repos/heliosCLI-wtrees/cve-sweep-high/.worktrees/chore-govern-pi` (2026-04-25 10:54:26 -0700)
- Git registered worktrees: 3

<details><summary>Orphan/unregistered entries</summary>

- `/Users/kooshapari/CodeProjects/Phenotype/repos/heliosCLI-wtrees/cve-sweep-high/.worktrees/chore-govern-pi`

</details>

### `/Users/kooshapari/CodeProjects/Phenotype/repos/heliosCLI-wtrees/lockfile-regen-2026-04-27`

- `.worktrees`: `/Users/kooshapari/CodeProjects/Phenotype/repos/heliosCLI-wtrees/lockfile-regen-2026-04-27/.worktrees`
- Immediate subdirs: 1
- Orphans/unregistered candidates: 1
- Oldest by mtime: `/Users/kooshapari/CodeProjects/Phenotype/repos/heliosCLI-wtrees/lockfile-regen-2026-04-27/.worktrees/chore-govern-pi` (2026-04-26 21:37:39 -0700)
- Git registered worktrees: 3

<details><summary>Orphan/unregistered entries</summary>

- `/Users/kooshapari/CodeProjects/Phenotype/repos/heliosCLI-wtrees/lockfile-regen-2026-04-27/.worktrees/chore-govern-pi`

</details>

### `/Users/kooshapari/CodeProjects/Phenotype/repos/heliosCLI/heliosCLI`

- `.worktrees`: `/Users/kooshapari/CodeProjects/Phenotype/repos/heliosCLI/heliosCLI/.worktrees`
- Immediate subdirs: 1
- Orphans/unregistered candidates: 1
- Oldest by mtime: `/Users/kooshapari/CodeProjects/Phenotype/repos/heliosCLI/heliosCLI/.worktrees/governance-pr-ready` (2026-04-24 15:43:32 -0700)
- Git registered worktrees: 3

<details><summary>Orphan/unregistered entries</summary>

- `/Users/kooshapari/CodeProjects/Phenotype/repos/heliosCLI/heliosCLI/.worktrees/governance-pr-ready`

</details>

## No-Orphan `.worktrees` Directories

- `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus`: 7 immediate subdirs, oldest `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus/.worktrees/dashboard-extraction` (2026-04-02 15:01:03 -0700)
- `/Users/kooshapari/CodeProjects/Phenotype/repos/agentapi-plusplus`: 2 immediate subdirs, oldest `/Users/kooshapari/CodeProjects/Phenotype/repos/agentapi-plusplus/.worktrees/chore-sast-pin-governance` (2026-04-25 00:36:55 -0700)
- `/Users/kooshapari/CodeProjects/Phenotype/repos/cliproxyapi-plusplus`: 2 immediate subdirs, oldest `/Users/kooshapari/CodeProjects/Phenotype/repos/cliproxyapi-plusplus/.worktrees/pr942-import-surface-fix` (2026-04-02 15:02:28 -0700)
- `/Users/kooshapari/CodeProjects/Phenotype/repos/HeliosLab`: 1 immediate subdirs, oldest `/Users/kooshapari/CodeProjects/Phenotype/repos/HeliosLab/.worktrees/pages-deadlinks-fix` (2026-04-27 01:13:22 -0700)
- `/Users/kooshapari/CodeProjects/Phenotype/repos/thegent`: 0 immediate subdirs, oldest `n/a` (n/a)
