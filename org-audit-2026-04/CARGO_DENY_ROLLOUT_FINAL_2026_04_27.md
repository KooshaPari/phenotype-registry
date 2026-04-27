# Cargo-Deny Rollout - 27 Branches Ready (Final 2026-04-27)

## Summary

27 repos now have cargo-deny rollout branches ready for PR creation:

- 21 full rollout branches add both `deny.toml` and `.github/workflows/cargo-deny.yml`.
- 6 workflow-dispatch branches add `workflow_dispatch` to existing cargo-deny workflows.

This supersedes the older 17-branch final note and the starter-only branch queue.

## Full rollout branches (21)

| Repo | Branch | Scope |
|---|---|---|
| AgilePlus | ci/cargo-deny-full-rollout-2026-04-27 | deny.toml + cargo-deny.yml |
| GDK | ci/cargo-deny-rollout-2026-04-27 | deny.toml + cargo-deny.yml |
| HeliosLab | ci/cargo-deny-rollout-2026-04-27 | deny.toml + cargo-deny.yml |
| HexaKit | ci/cargo-deny-rollout-20260427 | deny.toml + cargo-deny.yml |
| KDesktopVirt | ci/cargo-deny-full-rollout-2026-04-27 | deny.toml + cargo-deny.yml |
| pheno | ci/cargo-deny-rollout-2026-04-27 | deny.toml + cargo-deny.yml |
| phenoAI | ci/cargo-deny-full-rollout-2026-04-27 | deny.toml + cargo-deny.yml |
| phenoData | ci/cargo-deny-full-rollout-2026-04-27 | deny.toml + cargo-deny.yml |
| PhenoKits | ci/cargo-deny-full-rollout-2026-04-27 | deny.toml + cargo-deny.yml |
| PhenoProc | ci/cargo-deny-full-rollout-2026-04-27 | deny.toml + cargo-deny.yml |
| PhenoRuntime | ci/cargo-deny-full-rollout-2026-04-27 | deny.toml + cargo-deny.yml |
| phenoShared | ci/cargo-deny-rollout-2026-04-27 | deny.toml + cargo-deny.yml |
| phenotype-journeys | ci/cargo-deny-full-rollout-2026-04-27 | deny.toml + cargo-deny.yml |
| phenotype-tooling | ci/cargo-deny-full-rollout-2026-04-27 | deny.toml + cargo-deny.yml |
| PhenoVCS | ci/cargo-deny-full-rollout-2026-04-27 | deny.toml + cargo-deny.yml |
| PlayCua | ci/cargo-deny-full-rollout-2026-04-27 | deny.toml + cargo-deny.yml |
| rich-cli-kit | ci/cargo-deny-full-rollout-2026-04-27 | deny.toml + cargo-deny.yml |
| thegent-dispatch | ci/cargo-deny-full-rollout-2026-04-27 | deny.toml + cargo-deny.yml |
| thegent-workspace | ci/cargo-deny-full-rollout-2026-04-27 | deny.toml + cargo-deny.yml |
| Tokn | ci/cargo-deny-full-rollout-2026-04-27 | deny.toml + cargo-deny.yml |
| Tracely | ci/cargo-deny-full-rollout-2026-04-27 | deny.toml + cargo-deny.yml |

## Workflow_dispatch additions (6)

| Repo | Branch | Scope |
|---|---|---|
| Civis | ci/cargo-deny-add-workflow-dispatch-2026-04-27 | add workflow_dispatch |
| Configra | ci/cargo-deny-add-workflow-dispatch-2026-04-27 | add workflow_dispatch |
| Eidolon | ci/cargo-deny-add-workflow-dispatch-2026-04-27 | add workflow_dispatch |
| eyetracker | ci/cargo-deny-add-workflow-dispatch-2026-04-27 | add workflow_dispatch |
| heliosCLI | ci/cargo-deny-add-workflow-dispatch-2026-04-27 | add workflow_dispatch |
| Metron | ci/cargo-deny-add-workflow-dispatch-2026-04-27 | add workflow_dispatch |

## PR creation helper

Run the local helper from this repository after confirming GitHub rate limits are clear:

```bash
scripts/create_cargo_deny_prs_2026_04_27.sh
```

The helper uses explicit repo/branch/body tuples and sleeps 2 seconds between
`gh pr create` calls.
