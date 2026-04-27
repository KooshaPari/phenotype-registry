# CodeQL Rust Rollout — 2026-04-27 (Foundational Batch)

## Context
GitHub's default CodeQL setup excludes Rust (per memory `feedback_codeql_no_rust_default_setup.md`). Phenotype Rust repos need explicit CodeQL workflow config.

## Batch 1 — Merged (2026-04-27 09:55 UTC)
| Repo | PR | Status |
|---|---|---|
| BytePort | #70 | ✅ MERGED |
| FocalPoint | #19 | ✅ MERGED |
| helios-cli | #536 | ✅ MERGED |
| phenoShared | #134 | ✅ MERGED |
| hwLedger | #49 | ✅ MERGED |

## Workflow content
- Triggers: push/PR to main, Tuesday 04:17 UTC weekly cron, on-demand workflow_dispatch
- CodeQL action: github/codeql-action@v3 (init, autobuild, analyze with /language:rust)
- Permissions: actions:read, contents:read, security-events:write
- Timeout: 360 min (allows full Rust build + analysis)

## Live runs
Workflows will trigger on next push to main + weekly cron + on-demand. Will be subject to GitHub Actions billing constraint per `feedback_billing_blocked_rules.md`.

## Next batch candidates (~12 repos)
HeliosLab, PhenoMCP, PhenoObservability, PhenoPlugins, agentkit, agentapi-plusplus, Pyron, AgilePlus, Tasken, Sidekick, KDV, KDesktopVirt — foundational repos with active dev.

## Cross-references
- Memory: feedback_codeql_no_rust_default_setup.md (canonical)
- Audit: phenotype-org-governance/org-audit-2026-04/CODEQL_GAP_2026_04_27.md (dada8c7) — pre-rollout 5+/41 had Rust CodeQL

## Coverage delta
- Pre-rollout (this batch): unknown but likely ≤5/41 had Rust CodeQL  
- Post-rollout: at least 5/41 confirmed; needs full re-audit
