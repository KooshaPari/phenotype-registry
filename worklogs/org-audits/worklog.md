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
