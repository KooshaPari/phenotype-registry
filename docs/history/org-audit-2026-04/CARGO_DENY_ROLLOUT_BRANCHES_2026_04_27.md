# Cargo-Deny Rollout Branches — 2026-04-27

Source truth: `CARGO_DENY_TRUE_COVERAGE_2026_04_27.md` at commit `4a2a608`.
Template: `repos/BytePort/.github/workflows/cargo-deny.yml`.

## Pushed branches

| Repo | Branch | Result |
|---|---|---|
| GDK | `ci/cargo-deny-rollout-2026-04-27` | pushed `586c3c4`; copied workflow only |
| HeliosLab | `ci/cargo-deny-rollout-2026-04-27` | pushed `aa22904`; stashed pre-existing `README.md` edit first |
| pheno | `ci/cargo-deny-rollout-2026-04-27` | pushed `83d48a2`; copied workflow only |
| phenoShared | `ci/cargo-deny-rollout-2026-04-27` | pushed `74e634a`; copied workflow only |
| phenotype-tooling | `ci/cargo-deny-rollout-2026-04-27` | pushed `9092e28`; stashed pre-existing `docs/worklogs/` first |

Each pushed commit stages exactly `.github/workflows/cargo-deny.yml` and includes
`Co-authored-by: Codex <noreply@openai.com>`.

## Blockers / skips

| Repo | Status |
|---|---|
| AgilePlus | Local branch commit `9a4ef3e` exists, but push is blocked by pre-push hooks without bypass: TruffleHog has bare/worktree scan errors, and `agileplus-cli` integration tests fail in temp gitless dirs. Temporary worktree removed. |
| helios-router | skipped: no local `deny.toml`; starter `deny.toml` needed before workflow rollout |
| HexaKit | skipped: canonical path is not an active worktree (`git status` resolves to parent shelf and fails on submodule state); no local `deny.toml` |

PR creation deferred.
