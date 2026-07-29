# ABSORPTION DOCKET — `Compound-Spheres-3D-Backup`

## State

| field | value |
|-------|-------|
| source | `KooshaPari/Compound-Spheres-3D-Backup` (Private, C#, Jun 24) |
| merge link | `KooshaPari/Compound-Spheres-3D` (FINAL variant, already in registry) |
| classification | `I:NON_PHENOTYPE` (game-engine C#) |
| status | `TOMBSTONE_MERGED_INTO_CS3D` |
| archived at | 2026-07-28 |
| domain | non-Phenotype (game mod / engine) |
| boundary doc | `phenotype-registry/docs/boundary/legacy-game-mods.md` |

## Migration works

This is a **non-phenotype** repo (game-engine C# Compound-Spheres-3D derivative).
Both `Compound-Spheres-3D` and `Compound-Spheres-3D-Backup` were GH-archived on
the same date. No functional code needs migration; the user directed that the
Backup variant's history be linked to the FINAL variant as a tombstone.

### What was done

1. Identified both variants in `phenotype-registry/registry/disposition-index.json`
   (FINAL row for `Compound-Spheres-3D` exists; this row records the merge-link
   for the Backup variant).
2. No local clone present for either variant — both are GH-archived.
3. Created this docket + registry row `repo-Compound-Spheres-3D-Backup-merge`
   (disposition-index.json v1.6.82, 2026-07-28).
4. Boundary doc `legacy-game-mods.md` aggregates tombstone for both variants.

### What was NOT done

- No code merge (both non-phenotype, no functional Phenotype content).
- No forks pulled (private repo, GH-archived).
- No source-code preservation beyond boundary-doc reference.

## Supersedes chain

| from | to | reason |
|------|----|--------|
| `Compound-Spheres-3D-Backup` (private, Jun 24) | `Compound-Spheres-3D` (FINAL) | both non-phenotype; both GH-archived; user-approved merge-link 2026-07-28 "cs3d-back -> cs3d Y" |

## User decision (2026-07-28)

> *"cs3d-back -> cs3d Y"*

Captured in registry row `repo-Compound-Spheres-3D-Backup-merge.user_decision_2026-07-28`.

## Open items

None. Tombstone is complete.
