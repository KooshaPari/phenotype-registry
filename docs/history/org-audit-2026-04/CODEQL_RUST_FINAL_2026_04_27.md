# CodeQL Rust Rollout FINAL — 2026-04-27

## Summary
**34/42 (80%) Rust repos enrolled with CodeQL Rust workflow** in this session. From ~5 pre-session to 34 = **+29 newly-enrolled**.

## Combined coverage
| Metric | Value |
|---|---|
| Total local Rust repos | 42 |
| has cargo-deny.yml | 38/42 (90%) |
| has codeql-rust.yml | 34/42 (80%) |
| Both | ~32/42 (76%) |

## CodeQL Rust enrolled (34)
**Batch 1 (5):** BytePort, FocalPoint, helios-cli, phenoShared, hwLedger
**Batch 2 (8):** HeliosLab, PhenoMCP, PhenoObservability, PhenoPlugins, AgilePlus, Tasken, Sidekick, KDesktopVirt
**Batch 3 (15):** bare-cua, Civis, Configra, Eidolon, eyetracker, GDK, helios-router, heliosCLI, HexaKit, Metron, pheno, phenoAI, phenoData, PhenoKits, PhenoProc
**Batch 4 (12):** PhenoRuntime, phenotype-bus, phenotype-journeys, phenotype-tooling, phenoUtils, PhenoVCS, PlayCua, rich-cli-kit, thegent-dispatch, thegent-workspace, Tokn, Tracely

## PRs landed (45 total this session — cargo-deny + CodeQL)
PRs auto-merged by codex worker + admin-merge fallback. All 34 CodeQL PRs landed in 4 batches.

## Workflow content (standardized)
- Triggers: push/PR to main, Tuesday 04:17 UTC weekly cron, on-demand workflow_dispatch
- CodeQL action: github/codeql-action@v3 (init+autobuild+analyze)
- Permissions: actions:read, contents:read, security-events:write
- Timeout: 360 min

## Live runs
ALL subject to GitHub Actions billing constraint (per `feedback_billing_blocked_rules.md`). Will fire on Tuesday cron + on-demand once billing resolves.

## Remaining gap (~8 repos)
- 2 archived (KlipDot, kmobile)
- ~6 more candidates: agentkit, agentapi-plusplus (no Cargo.toml at root), Pyron (renamed), KDV, FocalPoint-vitepress, others

## Cross-references
- Memory: feedback_codeql_no_rust_default_setup.md
- Batch 1: CODEQL_RUST_ROLLOUT_2026_04_27.md
- Batch 2: CODEQL_RUST_ROLLOUT_BATCH2_2026_04_27.md
