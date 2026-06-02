# Phenotype Governance Index

**Forward (active policy):** start at [`POLICY.md`](POLICY.md) — enforced policies + reusable workflows.
**Backward (history):** past audits, session logs, and dashboards now live under [`docs/history/`](docs/history/).
**Ecosystem index:** the canonical map of all repos is [phenotype-registry/ECOSYSTEM_MAP.md](https://github.com/KooshaPari/phenotype-registry/blob/main/ECOSYSTEM_MAP.md) — this repo enforces, the registry indexes.

This is the top-level navigation map for `phenotype-org-governance`. The retrospective sections below now resolve under `docs/history/` (the former `governance/` and `org-audit-2026-04/` trees were moved there).

Current local document count:

```bash
find . -name "*.md" -not -path "./node_modules/*" -not -path "./.git/*" 2>/dev/null | wc -l
# 283
```

Use this file first, then follow the directory-level indexes for detail.

## Org Audits

### 2026-03

No `org-audit-2026-03/` directory exists in this checkout. If a future agent is
looking for March governance work, search the historical governance docs and
git history before assuming the audit was lost:

```bash
git log --all --name-only -- '*2026*03*.md' 'org-audit-2026-03/**'
rg -n "2026-03|March|W-[0-9]+" governance/ org-audit-*/ changes/
```

### 2026-04

Primary directory: [`org-audit-2026-04/`](org-audit-2026-04/)

Start with:

- [`org-audit-2026-04/INDEX.md`](org-audit-2026-04/INDEX.md) - short audit
  index and dashboard entrypoint.
- [`org-audit-2026-04/INDEX_2026_04_27.md`](org-audit-2026-04/INDEX_2026_04_27.md)
  - category catalog for the 2026-04-27 audit session.
- [`org-audit-2026-04/ORG_DASHBOARD_v67_2026_04_27_FINAL.md`](org-audit-2026-04/ORG_DASHBOARD_v67_2026_04_27_FINAL.md)
  - latest tracked dashboard closeout in the v62-v67 sequence.
- [`org-audit-2026-04/CARGO_DENY_TRUE_COVERAGE_2026_04_27.md`](org-audit-2026-04/CARGO_DENY_TRUE_COVERAGE_2026_04_27.md)
  - strict local cargo-deny coverage truth surface; prefer this over older
  dashboard claims.
- [`org-audit-2026-04/CARGO_DENY_ROLLOUT_BRANCHES_2026_04_27.md`](org-audit-2026-04/CARGO_DENY_ROLLOUT_BRANCHES_2026_04_27.md)
  and [`org-audit-2026-04/CARGO_DENY_ROLLOUT_FINAL_2026_04_27.md`](org-audit-2026-04/CARGO_DENY_ROLLOUT_FINAL_2026_04_27.md)
  - rollout branch queue and final cargo-deny handoff.
- [`org-audit-2026-04/HEALTH_DIGEST_2026_04_27.md`](org-audit-2026-04/HEALTH_DIGEST_2026_04_27.md)
  - cross-org health summary.
- [`org-audit-2026-04/PR_BACKLOG_2026_04_27_LATE.md`](org-audit-2026-04/PR_BACKLOG_2026_04_27_LATE.md),
  [`org-audit-2026-04/PR_CONFLICTS_2026_04_27.md`](org-audit-2026-04/PR_CONFLICTS_2026_04_27.md),
  and [`org-audit-2026-04/STALE_PRS_2026_04_27.md`](org-audit-2026-04/STALE_PRS_2026_04_27.md)
  - PR backlog, conflict, and stale-PR state.

Important subdirectories:

- [`org-audit-2026-04/aggregator/`](org-audit-2026-04/aggregator/) - audit
  aggregation helpers and generated support files.
- [`org-audit-2026-04/proposals/`](org-audit-2026-04/proposals/) - proposal
  material associated with the audit wave.

## Governance Docs

Primary directory: [`governance/`](governance/)

Start with:

- [`governance/README.md`](governance/README.md) - directory-level index for
  2026-04-26 user-story verification, archive audits, investigations, and
  recurring policy docs.
- [`governance/USER_DECISIONS_BACKLOG_2026_04_27.md`](governance/USER_DECISIONS_BACKLOG_2026_04_27.md)
  and [`governance/USER_DECISIONS_BACKLOG_2026_04_27_v2.md`](governance/USER_DECISIONS_BACKLOG_2026_04_27_v2.md)
  - blocked items requiring user decisions.
- [`governance/user_decisions_runbook_2026_04_26.md`](governance/user_decisions_runbook_2026_04_26.md)
  - runbook for decision follow-up.
- [`governance/SESSION_FINAL_DIGEST_2026_04_27_LATE_LATE.md`](governance/SESSION_FINAL_DIGEST_2026_04_27_LATE_LATE.md)
  - final digest with superseded-claim warnings and corrected cargo-deny truth.
- [`governance/SESSION_FINAL_RECAP_2026_04_27.md`](governance/SESSION_FINAL_RECAP_2026_04_27.md),
  [`governance/SESSION_SCORECARD_2026_04_27.md`](governance/SESSION_SCORECARD_2026_04_27.md),
  and [`governance/TOMORROW_START_HANDOFF_2026_04_27.md`](governance/TOMORROW_START_HANDOFF_2026_04_27.md)
  - closeout, scorecard, and next-session entrypoints.
- [`governance/shared-crates-canonical-home-adr-2026-04.md`](governance/shared-crates-canonical-home-adr-2026-04.md)
  - ADR-style record for shared-crate canonical-home decisions.

Policy and recurring governance records:

- [`governance/alert-sync-policy.md`](governance/alert-sync-policy.md) -
  Dependabot/alert synchronization policy.
- [`governance/sbom_automation.md`](governance/sbom_automation.md) and
  [`governance/sbom_tracking_policy_2026_04_27.md`](governance/sbom_tracking_policy_2026_04_27.md)
  - SBOM automation and tracking.
- [`governance/scope-expansion-policy.md`](governance/scope-expansion-policy.md)
  - policy for expanding scope instead of idling.
- [`governance/canonical_commit_strategy_2026_04_27.md`](governance/canonical_commit_strategy_2026_04_27.md)
  and [`governance/nested_workspaces.md`](governance/nested_workspaces.md)
  - repo identity, canonical-subdir inheritance, and nested workspace handling.
- [`governance/memory_drift_recheck_2026_04_27.md`](governance/memory_drift_recheck_2026_04_27.md)
  and [`governance/memory-drift-recheck-2026-04-26.md`](governance/memory-drift-recheck-2026-04-26.md)
  - memory freshness checks.

Audit families in `governance/`:

- Security: `codeql-*`, `secret-scanning-*`, `dependabot-*`,
  `scorecard-*`, `tokenpermissions-*`.
- Repository metadata: `repo-*`, `readme-*`, `changelog-*`,
  `codeowners-*`, `contributing-*`, `license-*`.
- Runtime and local state: `disk_*`, `pack_corruption_*`,
  `lockfile-*`, `rust-toolchain-*`, `msrv-*`, `workflow-*`.
- User-story verification: `userstory-*-2026-04-26.md`.
- Repo-specific triage: `agileplus-*`, `helios*`, `thegent-*`,
  `tracera-*`, `phenoshared-*`, `phenomcp-*`, `argis_*`.

## Changes / Migrations

Primary directory: [`changes/`](changes/)

Each change directory contains a `proposal.md`. Current tracked proposals:

- [`changes/2026-04-26-templates-registry-axum-migration/proposal.md`](changes/2026-04-26-templates-registry-axum-migration/proposal.md)
  - templates-registry multipart/dotenv migration.
- [`changes/2026-04-26-focalpoint-reqwest-12/proposal.md`](changes/2026-04-26-focalpoint-reqwest-12/proposal.md)
  - FocalPoint reqwest 0.11 to 0.12 scope.
- [`changes/2026-04-26-focalpoint-starlark-15/proposal.md`](changes/2026-04-26-focalpoint-starlark-15/proposal.md)
  - FocalPoint starlark upgrade scope.
- [`changes/2026-04-26-focalpoint-uniffi-31/proposal.md`](changes/2026-04-26-focalpoint-uniffi-31/proposal.md)
  - FocalPoint uniffi 0.31 risk assessment.
- [`changes/2026-04-26-focalpoint-final-5/proposal.md`](changes/2026-04-26-focalpoint-final-5/proposal.md)
  - final five FocalPoint advisory proposal.
- [`changes/2026-04-27-agileplus-utoipa-axum-paste/proposal.md`](changes/2026-04-27-agileplus-utoipa-axum-paste/proposal.md)
  - AgilePlus `paste` via `utoipa-axum` scope.
- [`changes/2026-04-27-eyetracker-uniffi-cluster/proposal.md`](changes/2026-04-27-eyetracker-uniffi-cluster/proposal.md)
  - eyetracker uniffi advisory cluster.
- [`changes/2026-04-27-final-low-advisories/proposal.md`](changes/2026-04-27-final-low-advisories/proposal.md)
  - final low-advisory closure proposal.
- [`changes/2026-04-27-kdv-bollard-cluster/proposal.md`](changes/2026-04-27-kdv-bollard-cluster/proposal.md)
  - KDesktopVirt bollard/rustls-webpki cluster.
- [`changes/2026-04-27-phenomcp-deps/proposal.md`](changes/2026-04-27-phenomcp-deps/proposal.md)
  - PhenoMCP Dependabot/dependency verification.
- [`changes/2026-04-27-phenoobservability-surrealdb/proposal.md`](changes/2026-04-27-phenoobservability-surrealdb/proposal.md)
  - PhenoObservability surrealdb/bincode advisory.

Local-only note: `changes/2026-04-27-agileplus-release-cut-adopt-10-commits/`
exists in this checkout but has no tracked `proposal.md` at the time this index
was written.

## Memory Cross-References

There are no `feedback_*.md` files in this repo tree. The docs reference memory
files stored outside this repository, mainly under operator memory/worklog
locations. When a doc cites `feedback_*.md`, treat it as a memory dependency and
verify current repo state before acting.

Most important referenced memory patterns:

- `feedback_cargo_deny_real_coverage_2026_04_27.md`,
  `feedback_audit_decode_false_positives.md`,
  `feedback_audit_freshness_decay.md` - cited by
  [`org-audit-2026-04/CARGO_DENY_TRUE_COVERAGE_2026_04_27.md`](org-audit-2026-04/CARGO_DENY_TRUE_COVERAGE_2026_04_27.md).
- `feedback_dashboard_actuals_only.md` - cited by
  [`org-audit-2026-04/ORG_DASHBOARD_v58_2026_04_27_actual_post_protobuf.md`](org-audit-2026-04/ORG_DASHBOARD_v58_2026_04_27_actual_post_protobuf.md).
- `feedback_dispatch_worker_text_only.md` - cited by
  [`org-audit-2026-04/ORG_DASHBOARD_v63_2026_04_27_LATE.md`](org-audit-2026-04/ORG_DASHBOARD_v63_2026_04_27_LATE.md).
- `feedback_codex_dispatch_pattern.md` - cited by
  [`org-audit-2026-04/ORG_DASHBOARD_v65_2026_04_27_LATE3.md`](org-audit-2026-04/ORG_DASHBOARD_v65_2026_04_27_LATE3.md).
- `feedback_repo_identity_verification.md` and
  `feedback_verify_origin_not_canonical.md` - cited by archive, readme, and
  canonical commit docs.
- `feedback_canonical_subdir_inheritance.md` - cited by
  [`governance/canonical_commit_strategy_2026_04_27.md`](governance/canonical_commit_strategy_2026_04_27.md)
  and [`governance/nested_workspaces.md`](governance/nested_workspaces.md).
- `feedback_repos_push_blockers.md`, `feedback_disk_crisis_round3.md`, and
  `feedback_pruner_atime_limitation.md` - cited by
  [`governance/pack_corruption_diagnosis_2026_04_26.md`](governance/pack_corruption_diagnosis_2026_04_26.md)
  and disk/mesh planning docs.
- `feedback_readme_verify_then_write.md` and `feedback_fork_aware_readme.md` -
  cited by readme quality and dashboard docs.

Find all memory references with:

```bash
rg -n "feedback_.*\\.md|feedback" . --glob "*.md" --glob "!node_modules/**" --glob "!.git/**"
```

## How To Find

Looking for the current state of the org? See
[`org-audit-2026-04/ORG_DASHBOARD_v67_2026_04_27_FINAL.md`](org-audit-2026-04/ORG_DASHBOARD_v67_2026_04_27_FINAL.md)
and then confirm critical numbers against stricter audit docs.

Looking for cargo-deny truth? See
[`org-audit-2026-04/CARGO_DENY_TRUE_COVERAGE_2026_04_27.md`](org-audit-2026-04/CARGO_DENY_TRUE_COVERAGE_2026_04_27.md).

Looking for cargo-deny rollout branches? See
[`org-audit-2026-04/CARGO_DENY_ROLLOUT_BRANCHES_2026_04_27.md`](org-audit-2026-04/CARGO_DENY_ROLLOUT_BRANCHES_2026_04_27.md)
and [`org-audit-2026-04/CARGO_DENY_ROLLOUT_FINAL_2026_04_27.md`](org-audit-2026-04/CARGO_DENY_ROLLOUT_FINAL_2026_04_27.md).

Looking for decisions blocked on Koosha? See
[`governance/USER_DECISIONS_BACKLOG_2026_04_27.md`](governance/USER_DECISIONS_BACKLOG_2026_04_27.md).

Looking for session handoff and warnings about superseded claims? See
[`governance/SESSION_FINAL_DIGEST_2026_04_27_LATE_LATE.md`](governance/SESSION_FINAL_DIGEST_2026_04_27_LATE_LATE.md).

Looking for governance policy? Start with [`governance/README.md`](governance/README.md),
then inspect `*-policy.md`, `*-coverage-*.md`, and `*-audit-*.md` by concern.

Looking for repo metadata hygiene? See `governance/repo-*`,
`governance/readme-*`, `governance/codeowners-*`,
`governance/changelog-*`, and `governance/contributing-*`.

Looking for security coverage? See `governance/codeql-*`,
`governance/dependabot-*`, `governance/secret-scanning-*`,
`governance/scorecard-*`, and `governance/tokenpermissions-*`.

Looking for PR backlog and stale PRs? See
[`org-audit-2026-04/PR_BACKLOG_2026_04_27_LATE.md`](org-audit-2026-04/PR_BACKLOG_2026_04_27_LATE.md),
[`org-audit-2026-04/PR_CONFLICTS_2026_04_27.md`](org-audit-2026-04/PR_CONFLICTS_2026_04_27.md),
and [`org-audit-2026-04/STALE_PRS_2026_04_27.md`](org-audit-2026-04/STALE_PRS_2026_04_27.md).

Looking for archive/deprecation state? See
[`governance/archive-state-canonical-2026-04-26.md`](governance/archive-state-canonical-2026-04-26.md),
[`governance/archive-state-recheck-2026-04-26-late.md`](governance/archive-state-recheck-2026-04-26-late.md),
and `org-audit-2026-04/archived_repo_triage_2026_04_26.md`.

Looking for Pages or custom-domain status? See
[`governance/org_pages_enabled_2026_04_27.md`](governance/org_pages_enabled_2026_04_27.md)
and `org-audit-2026-04/org_pages_status_2026_04_26_late.md` if present locally.

Looking for proposals/migrations? See [`changes/`](changes/) and read the
target change directory's `proposal.md`.

Looking for local disk, pack, or workspace health? See
[`governance/pack_corruption_diagnosis_2026_04_26.md`](governance/pack_corruption_diagnosis_2026_04_26.md),
[`governance/disk_creep_audit_2026_04_26.md`](governance/disk_creep_audit_2026_04_26.md),
[`governance/nested_workspaces.md`](governance/nested_workspaces.md),
and `org-audit-2026-04/*DISK*`.

Looking for agent docs coverage? See
[`governance/agent-docs-coverage-2026-04-27.md`](governance/agent-docs-coverage-2026-04-27.md)
and [`org-audit-2026-04/AGENT_DOCS_COVERAGE_2026_04_27.md`](org-audit-2026-04/AGENT_DOCS_COVERAGE_2026_04_27.md).

Looking for user-story walkthroughs? See `governance/userstory-*-2026-04-26.md`.

## Maintenance Commands

```bash
# Count docs
find . -name "*.md" -not -path "./node_modules/*" -not -path "./.git/*" 2>/dev/null | wc -l

# List audit directories
find org-audit-* -maxdepth 1 -type d | sort

# List governance docs
find governance -maxdepth 2 -type f -name "*.md" | sort

# List change proposals
find changes -maxdepth 2 -type f -name "proposal.md" | sort

# Find memory cross-references
rg -n "feedback_.*\\.md|feedback" . --glob "*.md" --glob "!node_modules/**" --glob "!.git/**"
```
