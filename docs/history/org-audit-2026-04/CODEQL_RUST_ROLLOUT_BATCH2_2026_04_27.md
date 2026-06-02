# CodeQL Rust Rollout Batch 2 — 2026-04-27 (13 Foundational Repos)

## Status
**13/13 foundational Rust repos enrolled with CodeQL Rust workflow.**

| Repo | Workflow Present | Method |
|---|---|---|
| BytePort | ✅ | PR #70 merged (batch 1) |
| FocalPoint | ✅ | PR #19 merged (batch 1) |
| helios-cli | ✅ | PR #536 merged (batch 1) |
| phenoShared | ✅ | PR #134 merged (batch 1) |
| hwLedger | ✅ | PR #49 merged (batch 1) |
| HeliosLab | ✅ | merged (batch 2) |
| PhenoMCP | ✅ | merged (batch 2) |
| PhenoObservability | ✅ | merged (batch 2) |
| PhenoPlugins | ✅ | merged (batch 2) |
| AgilePlus | ✅ | merged (batch 2) |
| Tasken | ✅ | PR #12 (batch 2) |
| Sidekick | ✅ | merged (batch 2) |
| KDesktopVirt | ✅ | merged (batch 2) |

## Skipped
- agentkit, Pyron, KDV — repos not found (renamed/archived)
- agentapi-plusplus — no Cargo.toml at root

## Workflow content
- Triggers: push/PR to main, Tuesday 04:17 UTC weekly cron, on-demand workflow_dispatch
- CodeQL action: github/codeql-action@v3 (init, autobuild, analyze with /language:rust)
- Permissions: actions:read, contents:read, security-events:write
- Timeout: 360 min

## Live runs
Subject to GitHub Actions billing constraint per `feedback_billing_blocked_rules.md`. Will trigger Tuesday 04:17 UTC + on-demand once billing resolves.

## Next batch candidates (~28 repos)
All remaining cargo-deny-enrolled Rust repos that don't yet have codeql-rust.yml.

## Cross-references
- Memory: feedback_codeql_no_rust_default_setup.md
- Batch 1 doc: CODEQL_RUST_ROLLOUT_2026_04_27.md (fc99183)
