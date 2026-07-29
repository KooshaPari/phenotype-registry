---
repo: "KooshaPari/thegent-sharecli"
status: absorbed
last_boundary_review: 2026-07-29
review_cadence: 30d
source_repo: "KooshaPari/thegent-sharecli"
source_local_path: "thegent-sharecli"
target_repo: "KooshaPari/thegent"
target_path: "sharecli/"
---

# Boundary — thegent-sharecli

## Decision

**2026-07-29:** `KooshaPari/thegent-sharecli` is a deprecated duplicate helper and is absorbed into `KooshaPari/thegent` at `sharecli/`.

## Absorption evidence

- Source local path: `../thegent-sharecli`
- Target local path: `../thegent/sharecli`
- Result artifact: `thegent/sharecli/ABSORPTION_META.json` (created)
- Move action: non-destructive content sync using `rsync -a --delete --exclude='.git'`

## Scope

- Scope retained in target:
  - CLI share helper implementation
  - Tests and docs for helper behavior
  - CI and repository metadata
- Remains in source for provenance:
  - `.git` history and remote origin
  - source repo state preserved (no destructive delete)

## Validation

- `test -d thegent/sharecli` (true after execution)
- `ls thegent/sharecli` contains expected Python package/test/docs surface
- Airlock snapshot pending before turn handoff (per global workflow)
