# Cargo Deny PR Status - 2026-04-27

Audit generated at 2026-04-27 02:38:06 MST from `/tmp/cargo_deny_pr_creation.log`.

The PR-creator wait reached the 30 minute cap without a `==SUMMARY==` marker. This dashboard uses the `OK <repo>: <url>` lines present in the log at audit time.

| Repo | PR# | Mergeable | ChecksPassing | MergeReady? |
|---|---:|---|---|---|
| AgilePlus | [#440](https://github.com/KooshaPari/AgilePlus/pull/440) | UNKNOWN | No | No |
| GDK | [#32](https://github.com/KooshaPari/GDK/pull/32) | UNKNOWN | No | No |
| HeliosLab | [#66](https://github.com/KooshaPari/HeliosLab/pull/66) | UNKNOWN | No | No |
| HexaKit | [#105](https://github.com/KooshaPari/HexaKit/pull/105) | UNKNOWN | No | No |

## Blockers

- AgilePlus #440: review required; non-passing or queued checks include `Kilo Code Review`, `Rust Security Audit`, `SonarCloud Code Analysis`, `pr-governance-gate`, and `security/snyk (kooshapari)`.
- GDK #32: non-passing or queued checks include `CodeRabbit`, `Kilo Code Review`, and `Legacy Tooling Anti-Pattern Scan`.
- HeliosLab #66: non-passing or queued checks include `Kilo Code Review`, `SonarCloud Code Analysis`, `Unit Tests`, and `codeql`.
- HexaKit #105: non-passing or queued checks include `CodeRabbit`, `Config Lint`, `Core Build`, `Core Documentation`, `Core MSRV (1.86)`, `Core Workspace Quality`, `Kilo Code Review`, `License Compliance`, `Python Quality`, `Rust Build`, `Rust Coverage`, `Rust Extras (machete, semver, typos)`, `Rust Lint`, `Rust MSRV (stable)`, `Rust Quality`, `Semgrep Scan`, `Snyk Dependency Check`, `Snyk Vulnerability Test (18)`, `Snyk Vulnerability Test (20)`, `SonarCloud Code Analysis`, `policy-gate`, `validate-traceability`, and `verify`.

## Method

- Parsed PR URLs from `/tmp/cargo_deny_pr_creation.log` lines matching `OK <repo>: <url>`.
- Queried each PR with `gh pr view <num> --repo <repo> --json mergeable,mergeStateStatus,reviewDecision,isDraft,statusCheckRollup`.
- Checked branch protection review requirements with `gh api repos/<repo>/branches/main/protection`; all four audited repos returned no protected-branch review requirement for `main` through that endpoint.
- Classified `MergeReady?` as `Yes` only when the PR is not draft, `mergeable == MERGEABLE`, checks are all passing/non-blocking, and review requirements are satisfied.
