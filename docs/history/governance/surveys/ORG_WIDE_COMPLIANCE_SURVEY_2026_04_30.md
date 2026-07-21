# Org-Wide Compliance Survey — 2026-04-27

## Executive Summary

| Domain | Status | Coverage/Score | Actionable Gaps |
|---|---|---|---|
| **Cargo-Deny (Rust)** | 🟡 Infrastructure Ready | 100% enrolled | Billing wall blocks activation; ~4 repos lack `workflow_dispatch` |
| **Cargo Workspace Health** | 🔴 Failing | 3/8 clean | FocalPoint (25 errors), hwLedger (4), PhenoObservability (2), AgilePlus (1), PhenoPlugins (unresolvable) |
| **Agent Governance Docs** | 🟡 Partial | 83% AGENTS, 73% CLAUDE | 14 repos missing both; 18 repos missing AGENTS.md; 28 missing CLAUDE.md |
| **Changelog Coverage** | 🟡 Partial | 78.6% | 22 repos missing CHANGELOG.md entirely |
| **Actions Pinning (Security)** | 🔴 Critical | 16.7% SHA-pinned | 3,158 unpinned external actions; top offenders: Tracera (1.9%), AgilePlus (2.2%), PhenoLang (3.7%) |
| **Branch Protection** | 🔴 Gap | 78% covered | 23 repos with zero rulesets and no classic `main` protection |
| **Canonical Staleness** | 🔴 Stale | 29/112 repos | 29 repos stale on `main`; 33 additional with mixed local-only commits |
| **AgilePlus Backlog** | 🟡 Operational | 19 ready-to-implement | 19 feature specs planned but unstarted; 10 deferred; backlog queue has 7 unprocessed items |

---

## Actionable Items by Severity

### 🔴 Critical (Security & Policy Violations)

| # | Repo(s) | Gap | Impact | Remediation |
|---|---|---|---|---|
| 1 | **Tracera, heliosCLI, AgilePlus, PhenoLang** | <5% SHA-pinned actions | Supply chain attack surface; tags/branches mutable | Migrate all `uses:` refs to 40-char commit SHAs via `pin-dependencies` |
| 2 | **23 repos** (e.g., phenotype-journeys, phenotype-bus, foqos-private) | Zero branch protection rulesets | No enforcement of PR reviews, status checks, or force-push blocks | Apply org-wide ruleset or per-repo rules covering `main`/`master` with required reviewers + status checks |
| 3 | **phenotype-org-governance** (private) | Missing AGENTS.md + CLAUDE.md | Governance repo not following own AI agent standards | Add both files immediately; likely requires org-wide policy audit |

### 🟡 High (Technical Debt & Compliance Gaps)

| # | Repo(s) | Gap | Impact | Remediation |
|---|---|---|---|---|
| 4 | **FocalPoint** (Rust, 61 members) | 25 `cargo check` errors | Workspace unhealthy; likely broken builds | Triage errors by crate; fix `Cargo.toml` members or remove dead members |
| 5 | **hwLedger** (37 members) | 4 `cargo check` errors | Dependency or lint errors | Run `cargo clippy` + resolve reported diagnostics |
| 6 | **PhenoObservability** | 2 `cargo check` errors | Partial workspace breakage | Narrow to failing crates; fix imports or cfg mismatches |
| 7 | **PhenoPlugins** | 0 members; cannot load metadata | Missing workspace member reference | Remove phantom member from `Cargo.toml` or add actual path |
| 8 | **14 landing/ops repos** (agileplus-landing, byteport-landing, phenotype-ops-mcp, etc.) | Missing both AGENTS.md + CLAUDE.md | Agents operate without governance guidance | Generate from org template; prefer AGENTS.md for agent-first design |
| 9 | **22 repos** | Missing CHANGELOG.md | No version history; release hygiene non-compliant | Bootstrap CHANGELOG.md; enable `keep-a-changelog` or semantic-release |
| 10 | **Cargo-Deny billing** | All 41 workflows blocked | Advisory scanning not yet live | Resolve GitHub Actions billing; verify `workflow_dispatch` trigger for ~4 repos |

### 🟢 Medium (Hygiene & Maintenance)

| # | Repo(s) | Gap | Impact | Remediation |
|---|---|---|---|---|
| 11 | **29 repos** (e.g., phenoShared, phenodocs, PlatformKit) | Stale on `main` (>5 commits behind) | Local state diverged from remote | `git pull origin main` or reconcile; investigate automation gaps |
| 12 | **33 repos** | Mixed state (local-only commits) | Unpushed changes risk loss; CI blind spots | Enforce branch protection to require PRs; audit `git push --force` policies |
| 13 | **AgilePlus** | 19 ready-to-implement specs; 7 queue items stuck | Backlog accumulation | Process queue via `./agileplus` binary (move binary out of `./agileplus/` directory); prioritize DEFERRED (10) vs. new (7) |
| 14 | **14 repos** | AGENTS.md only (no CLAUDE.md) | Inconsistent agent guidance | Align all to dual-file standard; use CLAUDE.md for human-facing, AGENTS.md for agent behavior |

---

## Repository Hitlist

### Must Fix (Security/Compliance)

```
agileplus-landing         → Missing AGENTS+CLAUDE; Missing CHANGELOG; No branch protection
byteport-landing         → Missing AGENTS+CLAUDE; Missing CHANGELOG
phenotype-journeys       → Missing AGENTS+CLAUDE; No branch protection
phenotype-bus            → No branch protection
foqos-private            → Missing AGENTS+CLAUDE; Missing CHANGELOG; No branch protection
phenotype-org-governance → Missing AGENTS+CLAUDE (private)
Tracera                  → 1.9% action pinning; ~323 unpinned refs
AgilePlus                → 2.2% action pinning; 1 cargo check error
thegent-dispatch         → No branch protection
```

### Should Fix (Technical Debt)

```
FocalPoint               → 25 cargo check errors (largest workspace by members)
phenoShared              → Stale on main
phenodocs                → Stale on main; mixed commits
phenotype-auth-ts        → Stale on main; Missing CHANGELOG
phenotype-tooling        → Stale on main
PhenoPlugins             → Unresolvable workspace metadata
```

---

## Cross-Cutting Observations

1. **Pinning hygiene is the single largest security gap.** At 16.7% SHA-pinned, the org is exposed to third-party action substitution attacks. This should be the top remediation priority.
2. **Branch protection coverage is asymmetric.** 78% coverage sounds acceptable, but the 23 unprotected repos include high-value assets (phenotype-journeys, phenotype-bus, foqos-private).
3. **Cargo workspace health is concentrated.** FocalPoint alone accounts for 25/32 total errors across audited repos. Fixing one repo significantly moves the needle.
4. **Agent governance adoption is incomplete.** Even the governance repo itself (phenotype-org-governance) lacks AGENTS.md/CLAUDE.md — a policy violation of its own mandate.
5. **Staleness suggests CI/CD or developer workflow gaps.** 29 repos stale on `main` indicates either broken automation or developer habit issues worth investigating at the org level.
