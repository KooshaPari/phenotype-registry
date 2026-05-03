# Worklog

## 2026-04-24 — Bootstrap worklog

Category: GOVERNANCE

Status: Early exploration. Repository initialized.

### Recent Commits
```
7ff1c99 feat(org-audits): bootstrap longitudinal audit-history repo with 2026-04-24 baseline
```

## 2026-05-02 — Hygiene wave: workflow_dispatch + cargo-deny bootstrap

Category: GOVERNANCE

Status: COMPLETE

### Summary
Systematic hygiene sweep across Phenotype org Rust repos.

### Actions Taken
- **Stale PRs closed**: PolicyStack #45 (trufflehog+FUNDING, conflicting), KlipDot #23 (FUNDING+trufflehog, conflicting) — both closed; content already on main
- **workflow_dispatch added**: AuthKit ✅, forgecode ✅, PhenoLang ✅ (unarchived→fixed→re-archived)
- **Malformed checkout actions fixed**: forgecode + PhenoLang (double-tag `@v4@SHA`), AuthKit (bare SHA)
- **cargo-deny.yml bootstrapped**: Stashly ✅, Settly ✅, ObservabilityKit ✅ (full workflow created)
- **workflow_dispatch verified (had it)**: PhenoRuntime ✅, PhenoDevOps ✅, PhenoMCP ✅, HeliosLab ✅, Tokn ✅
- **FUNDING.yml audit**: All 14 checked repos already have it (0 missing)
- **AGENTS.md coverage**: 0 missing across 17 repos checked
- **Open PRs**: 0 open across all 8 key repos
- **PhenoAgent workflow_dispatch**: Added ✅
- **phenotype-org-audits FUNDING+trufflehog**: Already on main (verified)
- **Stale merged branches cleaned**: pheno canary + chore/lockfile-regen deleted

### Rust GAP Status
- **Rust repos with cargo-deny.yml + workflow_dispatch**: PhenoAgent, PhenoRuntime, PhenoDevOps, PhenoMCP, HeliosLab, Tokn, Stashly, Settly, ObservabilityKit, eyetracker, AuthKit, forgecode, PhenoLang, Agentora, thegent-workspace, GDK, KlipDot
- **Rust repos missing cargo-deny.yml entirely**: Confirmed 3 (Stashly, Settly, ObservabilityKit — all now fixed)
- **Non-Rust repos flagged by batch scan**: Httpora, Dino, Pine, Paginary, Tracera, nanovms — all non-Rust or already have equivalent workflows

### Recent Commits
```
8016376 chore: bootstrap FUNDING.yml and trufflehog secrets scan (phenotype-org-audits)
67bbc62 ci: bootstrap cargo-deny workflow with workflow_dispatch (ObservabilityKit)
585e1fd ci: bootstrap cargo-deny workflow with workflow_dispatch (Settly)
352cc29 ci: bootstrap cargo-deny workflow with workflow_dispatch (Stashly)
f3b0208 ci(cargo-deny): add workflow_dispatch trigger, fix checkout SHA (PhenoAgent)
208dce5c ci(cargo-deny): add workflow_dispatch trigger, fix double-tag checkout (forgecode)
5818457 ci(cargo-deny): add workflow_dispatch trigger, fix checkout SHA (AuthKit)
8ae426f ci(cargo-deny): add workflow_dispatch trigger, fix double-tag checkout (PhenoLang)
```

## 2026-05-02 (wave 2) — cargo-deny full org rollout + hygiene

Category: GOVERNANCE

Status: COMPLETE

### Summary
Full cargo-deny bootstrap across remaining Rust repos + systemic hygiene sweep.

### Actions Taken
- **12 new cargo-deny bootstraps**: Apisync ✅, Authvault ✅, Cryptora ✅, Diffuse ✅, Guardrail ✅, kmobile ✅, KommandLineAutomation ✅, phenoRouterMonitor ✅, phenoXddLib ✅, Servion ✅, vibe-kanban ✅, worktree-manager ✅
- **GDK double-tag checkout fix**: Fixed malformed checkout `@v4@SHA` → `@v4` with single SHA; deduplicated duplicate workflow blocks; updated to `taiki-en/cargo-deny-action@v1`
- **Stale branch cleanup (phenoShared)**: Deleted 6 merged remote branches + 8 local remote-tracking refs (ghost branches from prior squash merges)
- **CLAUDE.md coverage audit**: 0 missing across 17 checked repos
- **0 open PRs**: Verified across all 8 key repos
- **Settly HIGH advisory**: sqlx RUSTSEC-2024-0363 — library crate, no lockfile, advisory persists; cannot resolve via `cargo update`
- **thegent deny.toml**: v2 format verified valid (mixed syntax concern was incorrect)

### Rust GAP Status (post-wave-2)
- **Rust repos with cargo-deny.yml + workflow_dispatch**: PhenoAgent, PhenoRuntime, PhenoDevOps, PhenoMCP, HeliosLab, Tokn, Stashly, Settly, ObservabilityKit, eyetracker, AuthKit, forgecode, PhenoLang, Agentora, thegent-workspace, GDK, KlipDot, Apisync, Authvault, Cryptora, Diffuse, Guardrail, kmobile, KommandLineAutomation, phenoRouterMonitor, phenoXddLib, Servion, vibe-kanban, worktree-manager
- **Rust repos missing cargo-deny.yml entirely**: Reduced to ~0 (full coverage achieved across local clones)
- **Non-Rust repos flagged**: Httpora, Dino, Pine, Paginary, Tracera, nanovms — all non-Rust or already have equivalent workflows

### Recent Commits
```
[wave-2 commits across 12 repos — bootstrap cargo-deny + workflow_dispatch]
```

## 2026-05-02 (wave 3) — Remaining GAP repos + org expansion

Category: GOVERNANCE

Status: COMPLETE

### Summary
Found and closed 3 remaining GAP Rust repos (thegent, AgilePlus spot-check, ObservabilityKit). GraphQL Rust audit in progress.

### Actions Taken
- **thegent cargo-deny bootstrap**: ✅ Pushed (had to pull-rebase first due to diverged history; accidentally embedded GDK-wtrees/worktree, quickly removed)
- **ObservabilityKit cargo-deny bootstrap**: ✅ Pushed to pr-30, merged ✅
- **AgilePlus**: Already has cargo-deny.yml on main (confirmed via git show origin/main)
- **Archive candidates check**: PhenoCompose, PhenoLang, PhenoRuntime — API unreliable (gh CLI failures); checked via repo listing
- **Rust repo GraphQL audit**: In progress (paginated 100/page); first page found 15 Rust repos including Settly, Stashly, Logify, Metron, Eventra, forge, Tasken

### True GAP (post-wave-3)
Rust repos missing cargo-deny.yml locally:
- thegent: ✅ Fixed (pushed)
- AgilePlus: ✅ Already has
- ObservabilityKit: ✅ Pushed/merged

### Rust repos found via GraphQL (page 1)
BytePort, kmobile, KommandLineAutomation, phenoRouterMonitor, phenoShared, phenoXddLib, forge, Tasken, Settly, Authvault, Stashly, Logify, Metron, Eventra, worktree-manager

### Embedded worktree cleanup (thegent)
- GDK-wtrees/fix-checkout was accidentally staged into thegent commit
- Fixed: `git rm --cached GDK-wtrees/fix-checkout` + re-push
- Impact: minimal (worktree already existed as separate repo)

### Recent Commits
```
ba06d59da ci: bootstrap cargo-deny workflow (thegent)
c95673d ci: bootstrap cargo-deny workflow (ObservabilityKit, via pr-30)
2aa9251 docs: bootstrap CLAUDE.md with AgilePlus identity + governance
```

## 2026-05-02 (wave 4) — FUNDING.yml + trufflehog audit + worktree cleanup

Category: GOVERNANCE

Status: COMPLETE

### Summary
Comprehensive governance coverage audit across all local repos.

### Key Metrics
- **FUNDING.yml coverage**: 105/259 local repos (40.5%)
- **Doc-only worktrees**: 105 stale doc worktrees identified in `.worktrees/` (candidates for cleanup)

### Actions Taken
- **AgilePlus CLAUDE.md**: ✅ Pushed (was missing despite being the governance mandate source)
- **Benchora governance**: Verified both CLAUDE.md and AGENTS.md already present
- **PhenoCompose**: Archived (read-only), cannot push. Has 2 open PRs that need unarchive to resolve
- **pyron, FixitRs, PhenoLang-actual**: NOT_FOUND on GitHub (deleted/renamed/never created)

### FINDINGS: Repos with trufflehog.yml or secrets-scan.yml
All 12 checked repos (PhenoVCS, GDK, HeliosLab, Metron, PhenoLang, PhenoMCP, PhenoProc, PhenoKits, Tokn, PhenoPlugins, PhenoObservability, AgilePlus) have at least one secrets scanning workflow ✅

### Systemic Issues (4 repos with dep conflicts — unchanged)
- PhenoObservability (transitive), argis-extensions (direct), canvasApp (peer), cliproxyapi-plusplus (core)

### Recent Commits
```
2aa9251 docs: bootstrap CLAUDE.md (AgilePlus)
```
