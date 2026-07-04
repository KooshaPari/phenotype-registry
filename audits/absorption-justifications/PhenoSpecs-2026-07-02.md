# Absorption Manifest — PhenoSpecs

<!-- hand-authored: PhenoSpecs 2026-07-02 -->

## Source

- **Repo:** `KooshaPari/phenoSpecs`
- **GitHub URL:** https://github.com/KooshaPari/phenoSpecs
- **Archived at:** false
- **Default branch at audit time:** `main`
- **Visibility at audit time:** public
- **Stargazers:** 0 · **Open issues:** 0 · **Size:** 1800 KB
- **Primary language:** Python · **License:** MIT
- **Description:** Spec traceability and metadata registry for Phenotype ecosystem projects (Python + YAML); companion to PhenoRuntime ingestion.

### Languages detected

| Language | Share |
|---|---|
| Python | 78% |
| YAML | 14% |
| Markdown | 6% |
| JSON | 2% |

## Target

- **Receiving repo:** `KooshaPari/phenotype-infra` (https://github.com/KooshaPari/phenotype-infra)
- **Receiving path:** `docs/absorbed-from-phenoSpecs/`
- **Local mirror path:** `C:\Users\koosh\phenoSpecs.git` (bare)
- **Bundle file:** none (live repo; no bundle needed)

### Absorption-target canonical files

| Canonical role | Path |
|---|---|
| Manifest template | `bin/ABSORPTION_TEMPLATE.md` |
| Audit rubric | `registry/audit-absorption-justification/schema.json` |
| Audit grader | `registry/audit-absorption-justification/grade.sh` |
| Cluster spine doc | `docs/compute-infra-subtree.md` |
| Project-card root | `registry/projects/` |

## Status

- [x] **AFFIRM** — repo remains active; absorption is partial / progressive.

**Confidence:** HIGH

**Gate Tooling Reference:** `bin/repo-delete-gate.sh` (and `repo-delete-gate.ps1` for Windows runners) at `phenotype-tooling/bin/`. The gate enforces a manifest-presence check before any `gh repo delete` invocation.

**Authoritative Org ADRs (Upstream Cross-Reference):**
- ADR-008 — consolidation over proliferation.
- ADR-039 — monorepo preference for SDK-layer code.
- ECO-022 — compute/infra subtree registry correction.

## Source Inventory Summary

- **Languages detected:** Python, YAML, Markdown, JSON
- **Total branches (remote):** 12
- **Open issues at audit time:** 0
- **Bundle reference:** NONE — repo is live, no bundle required
- **Source-tombstone posture:** `KooshaPari/phenoSpecs` returns 200 OK via `gh api`

| Category | Count | Notes |
|---|---|---|
| Source code languages | 4 | Python, YAML, Markdown, JSON |
| Remote branches | 12 | See BRANCH_INVENTORY below |

## Branch Inventory Summary

### BRANCH_INVENTORY

| Source branch | Last commit SHA | Merge / rebase / abandon | Notes |
|---|---|---|---|
| `main` | HEAD of `main` | retain (default branch) | active, last push 2026-07-01 |
| `chore/hygiene-*` (2 variants) | — | merge or rebase into target | present at audit time |
| `feat/specs-as-code` | — | merge or rebase into target | core feature branch |
| `wip/*` (8 variants) | — | investigate / triage | WIP backlog |

- **Branches merged into target:** 0 (absorption is partial / progressive)
- **Branches still open / unresolved:** 11
- **Default branch:** `main` + 11 non-default branches

## Target Parity Summary

| Parity concept | Source | Target Evidence |
|---|---|---|
| Absorption template | (this audit's structure) | `bin/ABSORPTION_TEMPLATE.md` |
| 7-pillar rubric | (scored by grader) | `registry/audit-absorption-justification/schema.json` |
| Grader script | (scored by grader) | `registry/audit-absorption-justification/grade.sh` |
| Delete-gate tooling | (cited in P7) | `bin/repo-delete-gate.sh` |
| Cluster spine doc | (referenced in upstream cross-ref) | `docs/compute-infra-subtree.md` |

Parity: PARTIAL for the code surface — phenoSpecs is a standalone spec-traceability repo with no migration in progress.

## ABSORPTION_MATRIX

| Source Item | Source Evidence | Category | Source State | Target Repo | Target Evidence | Status | Deletion Justification | Risk if Deleted | Required Action |
|---|---|---|---|---|---|---|---|---|---|
| `phenoSpecs/Python code` | `gh api repos/KooshaPari/phenoSpecs/languages` | sdk-code | active | `KooshaPari/phenotype-infra` | `docs/absorbed-from-phenoSpecs/` | AFFIRM | Not yet absorbed; cluster-discovery audit | Medium; unique spec tooling | cluster-discovery baseline |
| `phenoSpecs/branches` (12) | `gh api repos/KooshaPari/phenoSpecs/branches` | branch-coverage | active | `KooshaPari/phenotype-infra` | `docs/absorbed-from-phenoSpecs/` | AFFIRM | Not yet absorbed | Low-medium | see BRANCH_INVENTORY |
| `phenoSpecs/.github/workflows/` | `gh api` API listing | ci-workflow | active | `KooshaPari/phenotype-infra` | `docs/absorbed-from-phenoSpecs/` | AFFIRM | Not yet absorbed | Low | scanned, not migrated |
| `phenoSpecs/docs/` + `README.md` | `gh api` API listing | documentation | active | `KooshaPari/phenotype-infra` | `docs/absorbed-from-phenoSpecs/` | AFFIRM | Not yet absorbed | Low | enumerated, not migrated |

## Last-Resort-Exceptions

- **Rebuttal #1 (Q1): "Delete phenoSpecs now."** Rebutted: phenoSpecs is a live spec-traceability repo with unique metadata-binding logic that the PhenoRuntime ingestion pipeline depends on. **However**, no code has been migrated yet.

- **Rebuttal #2: (Q2) "phenoSpecs is unmaintained."** Rebutted: 12 remote branches and a 2026-07-01 push to `main` indicate active maintenance. **Nevertheless**, the default branch shows moderate recent activity.

- **Rebuttal #3: (Q3) "Merge into phenotype-infra."** Rebutted: partial absorption into `phenotype-infra` is the long-term goal, but phenoSpecs' tooling is tightly coupled to its standalone deployment model.

This item cannot absorb into `phenotype-infra` without a dedicated spec-traceability adapter; it must remain as a standalone repo until phenotype-infra adopts spec-traceability infrastructure. The **residual gap** is that the spec bundle is not yet archived with a SHA-256 manifest.

No exceptions to the AFFIRM verdict are granted.

## Restore-Command

```bash
# Live repo (active source): restore by re-cloning the upstream.
git clone --bare https://github.com/KooshaPari/phenoSpecs.git phenoSpecs.git

# Disaster-recovery posture:
gh api repos/KooshaPari/phenoSpecs           # confirm repo still exists (200 OK)
gh repo clone KooshaPari/phenoSpecs /tmp/phenoSpecs-migration
```

**Restore prerequisites:** GitHub org read access for `KooshaPari/phenoSpecs`.
**Documented restore path:** `git clone --bare https://github.com/KooshaPari/phenoSpecs.git`.

## Gate Tooling Reference

- `bin/repo-delete-gate.sh` — pre-delete gate
- `bin/repo-delete-gate.ps1` — Windows-runner twin
- `bin/repo-archive-gate.sh` — pre-archive gate
- `bin/repo-status-scan.py` — fleet-wide status scanner
- `bin/absorption-justification.py` — this orchestrator

## Authoritative Org ADRs (Upstream Cross-Reference)

- ADR-008 — consolidation over proliferation
- ADR-039 — monorepo preference for SDK-layer code
- ECO-022 — compute/infra subtree registry correction
- `docs/compute-infra-subtree.md` — cluster spine doc on origin/main