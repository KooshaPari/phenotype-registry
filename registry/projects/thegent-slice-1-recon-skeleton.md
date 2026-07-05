# thegent Slice-1 Reconnaissance — README + Manifest Only

**Audit:** thegent-2026-07-02 (14/14 L4, 100.00%)
**Scope:** Reconnaissance only (no code changes). Reads the thegent repository metadata, dist.toml manifests, and produces a 1-page skeleton for the 4 remaining slices.

## Goal

Establish a reliable reconnaissance layer before any code is moved. This is
**slice 1 of 5** per `thegent-scope-partition.md` (1 GB / 5 slices).

## Slice-1 Deliverables

| Path | Purpose |
|---|---|
| `docs/thegent-recon/README.md` | High-level summary of the thegent codebase |
| `docs/thegent-recon/manifest.md` | List of dist.toml / Cargo.toml / pyproject.toml manifests |
| `docs/thegent-recon/crate-map.md` | Map of workspace crates → pheno-runtime target subdirs |
| `docs/thegent-recon/dependency-graph.md` | Crate-to-crate dependency edges (first 1000 lines) |

## Recon Procedure

The thegent repository is **NOT cloned locally** (1 GB). Use the GitHub
public API + bare metadata. Do **not** execute `git clone https://github.com/KooshaPari/thegent`.

```bash
# Public API (read-only)
gh api repos/KooshaPari/thegent/contents/ --jq '.[].name'
gh api repos/KooshaPari/thegent/contents/docs 2>/dev/null
gh api repos/KooshaPari/thegent/contents/dist.toml --jq '.content' | base64 -d
gh api repos/KooshaPari/thegent/git/trees/HEAD?recursive=1 --jq '.tree[].path' | head -2000
```

For each manifest file (dist.toml, Cargo.toml, pyproject.toml):
- Capture the package name and version
- Capture the workspace members / subdirs
- Capture the published artefacts
- Estimate LoC and language distribution

## Slice-1 Skeleton (1-page)

```markdown
# thegent Reconnaissance — Slice 1 of 5

## Repository

- **GitHub**: https://github.com/KooshaPari/thegent
- **Size**: 1 GB (per `size_kb=1025150` in audit_candidates_with_size.json)
- **Default branch**: main
- **Last push**: 2026-07-02T06:15:29Z
- **Status**: open / AFFIRM

## Manifest Snapshot (via public API)

[ to be filled in slice-1 execution ]

## Crate Map (slice-1)

| Crate | Target subdir | LoC est. | Notes |
|---|---|---|---|
| _pending_ | _pending_ | _pending_ | _pending_ |

## Dependency Graph (slice-1)

[ dependency diagram — first 1000 lines ]

## Risk Notes

- 1 GB on disk; not clonable on Windows without sparse checkout
- Remote-only recon is required (no local clone)

## Next Slices

- slice-2: surface map + asset extraction
- slice-3: PR-1 — first 5 crates absorbed under pheno-runtime/
- slice-4: PR-2 — bulk import + cross-crate refactor
- slice-5: archival of thegent upstream + dashboard PR
```

## Acceptance Criteria

- [ ] Slice-1 README + manifest + crate-map + dependency-graph committed under `docs/thegent-recon/`
- [ ] No code from thegent is imported in this slice
- [ ] GitHub public API only (no local clone)
- [ ] Slice-1 PR opened with all 4 files

## Risk

Slice-1 is reconnaissance-only. If the GitHub API rate-limits (60/h
unauthenticated), this slice pauses until reset. The orchestrator's
`bin/branch_inventory.py` includes a `--refresh-inventory` mode that may
need to run first to confirm thegent's `pushed_at` is fresh.