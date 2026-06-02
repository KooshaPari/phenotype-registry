# Pre-commit Hooks Rollout — 2026-04-27

## Status
12 PRs merged adding standard pre-commit config to repos previously lacking it.

## Merged this session
| Repo | PR |
|---|---|
| phenoAI | #16 |
| phenoData | #17 |
| PhenoVCS | #32 |
| Tracely | #12 |
| PlayCua | #46 |
| Eidolon | #16 |
| eyetracker | #20 |
| thegent-dispatch | #10 |
| thegent-workspace | #11 |
| phenotype-bus | #8 |
| phenotype-journeys | #17 |
| phenoUtils | #12 |

## Template (standardized)
- pre-commit-hooks v5.0.0: trailing-whitespace, end-of-file-fixer, check-yaml/toml, large-file guard
- gitleaks v8.21.2: secret detection
- pre-commit-rust v1.0: cargo fmt + cargo-check

## Cross-references
- Pre-rollout audit: 275600f
