# Canonical Staleness Audit - 2026-04-27

Scope: local-only audit of primary checkouts matching `/Users/kooshapari/CodeProjects/Phenotype/repos/<repo>/.git`. Worktrees with `.git` files were skipped.

Method: for each repo, ran `git fetch origin --quiet`, measured `HEAD..origin/main` as behind and `origin/main..HEAD` as ahead, and flagged stale when on `main` with behind > 5. No audited repo was pulled or modified.

## Summary

- Repositories audited: 112
- Stale on main: 29
- Mixed on main with local-only commits: 33
- Fetch failures: 3

## Results

| Repo | Branch | Behind origin/main | Ahead origin/main | Stale | Mixed | Fetch |
| --- | --- | ---: | ---: | --- | --- | --- |
| `Tracera-recovered` | `fix/main-workflow-syntax` | 48 | 9 | no | no | ok |
| `McpKit` | `chore/gitignore-worktrees-2026-04-26` | 31 | 3 | no | no | ok |
| `AuthKit` | `chore/gitignore-worktrees-2026-04-26` | 29 | 1 | no | no | ok |
| `PhenoVCS` | `chore/sync-state` | 28 | 9 | no | no | ok |
| `phenoShared` | `main` | 24 | 0 | yes | no | ok |
| `AgilePlus` | `spec/013-cancelled` | 23 | 2 | no | no | ok |
| `artifacts` | `chore/gitignore-worktrees-2026-04-26` | 22 | 174 | no | no | ok |
| `phench` | `chore/gitignore-worktrees-2026-04-26` | 22 | 174 | no | no | ok |
| `PhenoKits` | `chore/gitignore-worktrees-2026-04-26` | 22 | 4 | no | no | ok |
| `phenodocs` | `main` | 21 | 3 | yes | yes | ok |
| `ObservabilityKit` | `chore/gitignore-worktrees-2026-04-26` | 20 | 1 | no | no | ok |
| `PlatformKit` | `main` | 19 | 4 | yes | yes | ok |
| `QuadSGM` | `main` | 19 | 4 | yes | yes | ok |
| `PhenoProject` | `main` | 18 | 3 | yes | yes | ok |
| `phenotype-auth-ts` | `main` | 17 | 4 | yes | yes | ok |
| `phenotype-tooling` | `main` | 16 | 6 | yes | yes | ok |
| `phenotype-infra` | `audit/cross-repo-loc-dedup-followup` | 15 | 2 | no | no | ok |
| `Conft` | `main` | 14 | 10 | yes | yes | ok |
| `heliosCLI` | `fix/deps-handlebars-critical-2026-04-26` | 14 | 7 | no | no | ok |
| `TestingKit` | `chore/gitignore-worktrees-2026-04-26` | 14 | 2 | no | no | ok |
| `argis-extensions` | `main` | 12 | 24 | yes | yes | ok |
| `cliproxyapi-plusplus` | `main` | 12 | 0 | yes | no | ok |
| `GDK` | `main` | 12 | 6 | yes | yes | ok |
| `PhenoDevOps` | `main` | 12 | 0 | yes | no | ok |
| `portage` | `fix/integration-test-utils` | 12 | 5 | no | no | ok |
| `ResilienceKit` | `chore/gitignore-worktrees-2026-04-26` | 12 | 1 | no | no | ok |
| `AgentMCP` | `HEAD` | 10 | 2 | no | no | ok |
| `DevHex` | `main` | 10 | 0 | yes | no | ok |
| `heliosBench` | `chore/gitignore-worktrees-2026-04-26` | 10 | 2 | no | no | ok |
| `phenotype-ops-mcp` | `chore/fork-attribution` | 10 | 7 | no | no | ok |
| `agent-user-status` | `user-status-next-dag-hardening` | 9 | 53 | no | no | ok |
| `phenoDesign` | `main` | 9 | 2 | yes | yes | ok |
| `phenotype-journeys` | `main` | 9 | 5 | yes | yes | ok |
| `Httpora` | `main` | 8 | 0 | yes | no | ok |
| `Parpoura` | `main` | 8 | 4 | yes | yes | ok |
| `PhenoAgent` | `main` | 8 | 0 | yes | no | ok |
| `PhenoSpecs` | `main` | 8 | 0 | yes | no | ok |
| `thegent` | `fix/deps-python-high-2026-04-26` | 8 | 4 | no | no | ok |
| `agentapi-plusplus` | `fix/critical-next-cve-2025-55182` | 7 | 1 | no | no | ok |
| `helios-router` | `chore/gitignore-worktrees-2026-04-26` | 7 | 1 | no | no | ok |
| `PhenoProc` | `main` | 7 | 0 | yes | no | ok |
| `phenoResearchEngine` | `main` | 7 | 3 | yes | yes | ok |
| `vibeproxy` | `main` | 7 | 1 | yes | yes | ok |
| `vibeproxy-monitoring-unified` | `main` | 7 | 1 | yes | yes | ok |
| `agent-devops-setups` | `main` | 6 | 3 | yes | yes | ok |
| `Dino` | `main` | 6 | 0 | yes | no | ok |
| `HeliosLab` | `main` | 6 | 0 | yes | no | ok |
| `KDesktopVirt` | `chore/bump-bollard-0-20` | 6 | 2 | no | no | ok |
| `phenoData` | `main` | 6 | 0 | yes | no | ok |
| `PhenoRuntime` | `main` | 6 | 0 | yes | no | ok |
| `phenotype-hub` | `main` | 6 | 2 | yes | yes | ok |
| `cheap-llm-mcp` | `main` | 5 | 0 | no | no | ok |
| `dinoforge-packs` | `main` | 5 | 0 | no | no | ok |
| `foqos-private` | `main` | 5 | 1 | no | yes | ok |
| `nanovms` | `docs` | 5 | 39 | no | no | ok |
| `pheno` | `main` | 5 | 0 | no | no | ok |
| `PhenoHandbook` | `main` | 5 | 0 | no | no | ok |
| `phenotype-ops-mcp-fix` | `main` | 5 | 0 | no | no | ok |
| `thegent-workspace` | `main` | 5 | 1 | no | yes | ok |
| `Tracely` | `chore/dead-code-phase1-tracely` | 5 | 6 | no | no | ok |
| `agileplus-landing` | `fix/p0-readme-qa-fallbacks` | 4 | 1 | no | no | ok |
| `DataKit` | `chore/gitignore-worktrees-2026-04-26` | 4 | 1 | no | no | ok |
| `PhenoCompose` | `main` | 4 | 0 | no | no | ok |
| `Tasken` | `codex/worklog-doc-links` | 4 | 3 | no | no | ok |
| `thegent-dispatch` | `main` | 4 | 2 | no | yes | ok |
| `byteport-landing` | `main` | 3 | 0 | no | no | ok |
| `Civis` | `main` | 3 | 0 | no | no | ok |
| `MCPForge` | `main` | 3 | 0 | no | no | ok |
| `Paginary` | `main` | 3 | 0 | no | no | ok |
| `phenoAI` | `main` | 3 | 0 | no | no | ok |
| `PhenoObservability` | `main` | 3 | 0 | no | no | ok |
| `phenotype-omlx` | `main` | 3 | 1 | no | yes | ok |
| `Sidekick` | `codex/worklog-scaffold` | 3 | 3 | no | no | ok |
| `hwLedger` | `main` | 2 | 0 | no | no | ok |
| `hwledger-landing` | `main` | 2 | 0 | no | no | ok |
| `rich-cli-kit` | `main` | 2 | 2 | no | yes | ok |
| `FocalPoint` | `main` | 1 | 0 | no | no | ok |
| `helios-cli` | `main` | 1 | 0 | no | no | ok |
| `PhenoMCP` | `main` | 1 | 0 | no | no | ok |
| `PhenoPlugins` | `main` | 1 | 0 | no | no | ok |
| `phenotype-org-audits` | `main` | 1 | 0 | no | no | ok |
| `phenotype-registry` | `codex/license-baseline` | 1 | 1 | no | no | ok |
| `agslag-docs` | `main` | 0 | 13 | no | yes | ok |
| `AppGen` | `main` | 0 | 11 | no | yes | ok |
| `atoms.tech` | `main` | 0 | 12 | no | yes | ok |
| `AtomsBot` | `main` | 0 | 11 | no | yes | ok |
| `bare-cua` | `master` | NA | NA | no | no | ok |
| `BytePort` | `main` | 0 | 0 | no | no | ok |
| `chatta` | `main` | 0 | 17 | no | yes | ok |
| `cloud` | `main` | 0 | 25 | no | yes | fetch_failed |
| `Configra` | `main` | 0 | 0 | no | no | ok |
| `DINOForge-UnityDoorstop` | `master` | NA | NA | no | no | ok |
| `Eidolon` | `main` | 0 | 0 | no | no | ok |
| `eyetracker` | `main` | 0 | 0 | no | no | ok |
| `heliosApp` | `main` | 0 | 0 | no | no | ok |
| `KlipDot` | `main` | 0 | 13 | no | yes | ok |
| `kmobile` | `chore/dead-code-phase1-kmobile` | 0 | 13 | no | no | ok |
| `kwality` | `main` | 0 | 8 | no | yes | ok |
| `localbase3` | `main` | 0 | 11 | no | yes | ok |
| `Metron` | `main` | 0 | 0 | no | no | ok |
| `netweave-final2` | `main` | 0 | 12 | no | yes | fetch_failed |
| `org-github` | `main` | 0 | 11 | no | yes | fetch_failed |
| `phenokits-landing` | `main` | 0 | 0 | no | no | ok |
| `phenotype-bus` | `main` | 0 | 0 | no | no | ok |
| `phenoUtils` | `main` | 0 | 0 | no | no | ok |
| `phenoXdd` | `docs/productization` | NA | NA | no | no | ok |
| `Planify` | `codex/fix-avatar-ssrf` | NA | NA | no | no | ok |
| `PlayCua` | `master` | NA | NA | no | no | ok |
| `PolicyStack` | `main` | 0 | 0 | no | no | ok |
| `projects-landing` | `main` | 0 | 0 | no | no | ok |
| `thegent-landing` | `main` | 0 | 0 | no | no | ok |
| `Tokn` | `main` | 0 | 0 | no | no | ok |
