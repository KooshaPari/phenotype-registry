# AgilePlus Backlog Audit - 2026-04-27

Scope: read-only audit of `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus`.

## Summary

- `kitty-specs/` top-level directories: 42, including the `archive/` bucket.
- Open top-level feature specs counted for this audit: 41, excluding the `archive/` bucket.
- Archived nested specs under `kitty-specs/archive/`: 3.
- `.agileplus/agileplus.db` feature rows: 23.
- Queue size from `backlog_items`: 7 rows, all `new`.
- In-flight state: 6 active cycles, 16 active cycle-feature assignments, 1 work package in `doing` or `review`.
- Ready-to-implement: 19 feature specs have a plan and no implementation evidence, excluding `ARCHIVED` specs.

`./agileplus queue list` and `./agileplus cycle list` could not run as requested because
`./agileplus` is a directory in this checkout, not an executable binary. The attempted
invocation returned `permission denied`.

## Feature Artifact Status Counts

Status is read from the top-level status marker in each `kitty-specs/<feature>/spec.md`.

| Status | Count |
|---|---:|
| ARCHIVED | 8 |
| SCAFFOLDED | 16 |
| CANCELLED | 1 |
| specified | 4 |
| DONE | 2 |
| DEFERRED | 10 |

## Database Status Counts

From `.agileplus/agileplus.db`.

### Features

| State | Count |
|---|---:|
| planned | 1 |
| retrospected | 1 |
| specified | 18 |
| validated | 3 |

### Queue

| Status | Count |
|---|---:|
| new | 7 |

### Cycles

| State | Count |
|---|---:|
| Active | 6 |
| Draft | 1 |

## Artifact-Derived Gates

Definitions:

- Planned: `plan.md` exists or DB state is at least `planned`.
- Validated: `validation-report.md` has `PASS`, or DB state is `validated`, `shipped`, or `retrospected`.
- Implemented: checked tasks exist, DB state is `implementing`, `validated`, `shipped`, or `retrospected`, or DB work packages are done.
- Ready-to-implement: planned, not implemented, and not `ARCHIVED`.

| Gate | Count |
|---|---:|
| Planned | 27 |
| Validated | 4 |
| Implemented | 4 |
| Ready-to-implement | 19 |

## Ready-to-Implement Features

- `004-modules-and-cycles`
- `013-phenotype-infrakit-stabilization`
- `015-plugin-system-completion`
- `016-agent-framework-expansion`
- `017-cli-tools-consolidation`
- `018-template-repo-cleanup`
- `021-polyrepo-ecosystem-stabilization`
- `codeprojects-archive-manifest`
- `consolidate-cache-adapter-crate`
- `consolidate-event-sourcing-crate`
- `consolidate-policy-engine-crate`
- `consolidate-state-machine-crate`
- `kooshapari-stale-repo-triage`
- `phenosdk-decompose-core`
- `phenosdk-decompose-mcp`
- `phenosdk-fix-notimplemented`
- `phenosdk-sanitize-atoms`
- `phenosdk-wave-a-contracts`
- `portfolio-audit-kooshapari-2026`

## Queue Rows

| ID | Priority | Status | Feature | Title |
|---:|---|---|---|---|
| 1 | high | new | `003-agileplus-platform-completion` | Restore AgilePlus event trail for active recovery cycles |
| 2 | high | new | `006-helioscli-completion` | Reconcile heliosCLI active worklog against AgilePlus runtime |
| 3 | high | new | `007-thegent-completion` | Normalize thegent control surface and backlog links |
| 4 | high | new | `002-org-wide-release-governance-dx-automation` | Normalize active-repo CI gate tooling and billing exception handling |
| 5 | high | new | `002-org-wide-release-governance-dx-automation` | Apply strict Git ruleset baseline to active repos |
| 6 | high | new | `002-org-wide-release-governance-dx-automation` | Triage stash and worktree recovery before PR prep |
| 7 | high | new | `006-helioscli-completion` | Prepare heliosCLI governance branch for reviewable PR |

## Per-Feature Check

| Feature | Spec Status | DB State | Planned | Validated | Implemented | Ready |
|---|---|---|---|---|---|---|
| `001-spec-driven-development-engine` | ARCHIVED | validated | yes | yes | yes | no |
| `002-org-wide-release-governance-dx-automation` | SCAFFOLDED | validated | yes | yes | yes | no |
| `003-agileplus-platform-completion` | ARCHIVED | validated | yes | yes | yes | no |
| `004-modules-and-cycles` | SCAFFOLDED | planned | yes | no | no | yes |
| `008-temporal-deployment-workflow-migration` | SCAFFOLDED | retrospected | yes | yes | yes | no |
| `012-github-portfolio-triage` | ARCHIVED | specified | yes | no | no | no |
| `013-phenotype-infrakit-stabilization` | CANCELLED | specified | yes | no | no | yes |
| `014-observability-stack-completion` | ARCHIVED | specified | yes | no | no | no |
| `015-plugin-system-completion` | SCAFFOLDED | specified | yes | no | no | yes |
| `016-agent-framework-expansion` | SCAFFOLDED | specified | yes | no | no | yes |
| `017-cli-tools-consolidation` | SCAFFOLDED | specified | yes | no | no | yes |
| `018-template-repo-cleanup` | SCAFFOLDED | specified | yes | no | no | yes |
| `019-private-repo-catalog` | ARCHIVED | specified | yes | no | no | no |
| `020-portfolio-and-web-apps` | ARCHIVED | specified | yes | no | no | no |
| `021-polyrepo-ecosystem-stabilization` | SCAFFOLDED | not-in-db | yes | no | no | yes |
| `022-batch13-repo-remediation` | ARCHIVED | not-in-db | no | no | no | no |
| `codeprojects-archive-manifest` | SCAFFOLDED | not-in-db | yes | no | no | yes |
| `consolidate-cache-adapter-crate` | specified | not-in-db | yes | no | no | yes |
| `consolidate-event-sourcing-crate` | specified | not-in-db | yes | no | no | yes |
| `consolidate-policy-engine-crate` | specified | not-in-db | yes | no | no | yes |
| `consolidate-state-machine-crate` | specified | not-in-db | yes | no | no | yes |
| `eco-001-worktree-remediation` | ARCHIVED | not-in-db | no | no | no | no |
| `eco-002-branch-consolidation` | DONE | not-in-db | no | no | no | no |
| `eco-003-circular-dep-resolution` | DONE | not-in-db | no | no | no | no |
| `eco-004-hexagonal-migration` | DEFERRED | not-in-db | no | no | no | no |
| `eco-005-xdd-quality` | DEFERRED | not-in-db | no | no | no | no |
| `eco-006-governance-sync` | DEFERRED | not-in-db | no | no | no | no |
| `eco-012-orgops-capital-ledger` | DEFERRED | not-in-db | no | no | no | no |
| `feature-specification-template-platform-completion` | DEFERRED | specified | no | no | no | no |
| `kooshapari-stale-repo-triage` | SCAFFOLDED | not-in-db | yes | no | no | yes |
| `oci-lottery-daemon` | DEFERRED | specified | no | no | no | no |
| `oci-post-acquire-hooks` | DEFERRED | specified | no | no | no | no |
| `phenosdk-decompose-core` | SCAFFOLDED | not-in-db | yes | no | no | yes |
| `phenosdk-decompose-llm` | DEFERRED | not-in-db | no | no | no | no |
| `phenosdk-decompose-mcp` | SCAFFOLDED | not-in-db | yes | no | no | yes |
| `phenosdk-fix-notimplemented` | SCAFFOLDED | not-in-db | yes | no | no | yes |
| `phenosdk-sanitize-atoms` | SCAFFOLDED | not-in-db | yes | no | no | yes |
| `phenosdk-wave-a-contracts` | SCAFFOLDED | not-in-db | yes | no | no | yes |
| `portfolio-audit-kooshapari-2026` | SCAFFOLDED | not-in-db | yes | no | no | yes |
| `snyk-phase-1-deploy` | DEFERRED | specified | no | no | no | no |
| `thegent-dotfiles-consolidation` | DEFERRED | not-in-db | no | no | no | no |
