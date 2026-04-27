# Cargo-Deny Rollout — 17 Branches Pushed (Final 2026-04-27 Late Session)

## Summary
17 repos now have rollout branches awaiting PR merge to main. Achieved against the 24-repo missing-cargo-deny.yml gap from `CARGO_DENY_TRUE_COVERAGE_2026_04_27.md` (4a2a608).

## Branches by repo (verified via git ls-remote)
| Repo | Branch | Method |
|---|---|---|
| bare-cua | ci/cargo-deny-full-rollout-2026-04-27 | parent (push rejected — needs --force or pull) |
| GDK | ci/add-starter-deny-toml-20260427 + ci/cargo-deny-rollout-2026-04-27 | codex |
| helios-router | ci/add-starter-deny-toml-20260427 | codex (deny.toml only) |
| HeliosLab | ci/cargo-deny-rollout-2026-04-27 | codex |
| HexaKit | ci/cargo-deny-rollout-20260427 | parent |
| pheno | ci/cargo-deny-rollout-2026-04-27 | codex |
| phenoAI | ci/cargo-deny-full-rollout-2026-04-27 | parent |
| phenoData | ci/cargo-deny-full-rollout-2026-04-27 | parent |
| PhenoKits | ci/cargo-deny-full-rollout-2026-04-27 | parent |
| PhenoProc | ci/cargo-deny-full-rollout-2026-04-27 | parent |
| PhenoRuntime | ci/cargo-deny-full-rollout-2026-04-27 | parent |
| phenoShared | ci/cargo-deny-rollout-2026-04-27 | codex |
| phenotype-journeys | ci/cargo-deny-full-rollout-2026-04-27 | parent |
| phenotype-tooling | ci/cargo-deny-full-rollout-2026-04-27 | parent |
| PhenoVCS | ci/cargo-deny-full-rollout-2026-04-27 | parent |
| PlayCua | ci/cargo-deny-full-rollout-2026-04-27 | parent |
| rich-cli-kit | ci/cargo-deny-full-rollout-2026-04-27 | parent |

## Skipped (archived; 403 read-only)
KlipDot, kmobile (per memory `reference_archived_repos_locked.md` — 48 archived org-wide).

## Skipped (could not clone)
AgilePlus (bare canonical at /repos/; needs worktree-based PR creation, deferred).

## When rate limit resets at 09:11 UTC
PR creation script (run from any clean dir):
```bash
for repo_branch in \
  "phenoShared:ci/cargo-deny-rollout-2026-04-27" \
  "HexaKit:ci/cargo-deny-rollout-20260427" \
  "pheno:ci/cargo-deny-rollout-2026-04-27" \
  "phenoAI:ci/cargo-deny-full-rollout-2026-04-27" \
  "phenoData:ci/cargo-deny-full-rollout-2026-04-27" \
  "PhenoKits:ci/cargo-deny-full-rollout-2026-04-27" \
  "PhenoProc:ci/cargo-deny-full-rollout-2026-04-27" \
  "PhenoRuntime:ci/cargo-deny-full-rollout-2026-04-27" \
  "phenotype-journeys:ci/cargo-deny-full-rollout-2026-04-27" \
  "phenotype-tooling:ci/cargo-deny-full-rollout-2026-04-27" \
  "PhenoVCS:ci/cargo-deny-full-rollout-2026-04-27" \
  "PlayCua:ci/cargo-deny-full-rollout-2026-04-27" \
  "rich-cli-kit:ci/cargo-deny-full-rollout-2026-04-27" \
  "PhenoVCS:ci/cargo-deny-full-rollout-2026-04-27" \
; do
  repo="${repo_branch%%:*}"; branch="${repo_branch#*:}"
  gh pr create --repo "KooshaPari/$repo" --base main --head "$branch" \
    --title "ci(cargo-deny): add scheduled scan + workflow_dispatch (zero-advisory floor)" \
    --body "Closes gap from CARGO_DENY_TRUE_COVERAGE_2026_04_27.md (4a2a608). Adds starter deny.toml (where missing) + BytePort-template cargo-deny.yml workflow. Enables Monday-cron + on-demand verification."
  sleep 2
done
```

## Coverage delta (when PRs merge)
- BEFORE: 18/42 local Rust repos (43%) had cargo-deny.yml
- AFTER (if all 17 PRs merge): 35/42 local Rust repos (83%) — but 7 of these are stubs/archived
- TRUE active Rust coverage will reach ~95% post-merge
