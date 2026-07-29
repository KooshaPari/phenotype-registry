# ABSORPTION DOCKET — `UnityDoorstop-NexusPatched`

## State

| field | value |
|-------|-------|
| source | `KooshaPari/UnityDoorstop-NexusPatched` (Public, C, LGPL, Jun) |
| actual local fork | `AgilePlus/DINOForge-UnityDoorstop` (currently empty placeholder locally) |
| upstream | `NeighTools/doorstop` (3rd-party Unity injection tool) |
| classification | `I:NON_PHENOTYPE` (game modding tool) |
| status | `TOMBSTONE_LINKED_TO_FORK` |
| archived at | 2026-07-28 |
| domain | non-Phenotype (Unity doorstop / injection) |
| boundary doc | `phenotype-registry/docs/boundary/legacy-game-mods.md` |

## Migration works

`UnityDoorstop-NexusPatched` is a fork of `NeighTools/doorstop` with KooshaPari's
NexusPatched modifications. Per the user's standing fork rule
(*"forks are more important to keep as-is and consume into"*), the repo is
preserved as a tombstone referencing the actual linked fork repo and the
upstream source.

### What was done

1. Identified the "actual linked fork repo" as `AgilePlus/DINOForge-UnityDoorstop`
   per user note 2026-07-28.
2. No local clone present for `KooshaPari/UnityDoorstop-NexusPatched` (GH-archived).
3. Local `AgilePlus/DINOForge-UnityDoorstop/` directory exists but is empty
   (placeholder; needs population from upstream or UDNP).
4. Created this docket + registry row `repo-UnityDoorstop-NexusPatched-fork-link`
   (disposition-index.json v1.6.82, 2026-07-28).
5. Preserved 3rd-party fork attribution in registry row + boundary doc.

### What was NOT done

- No code merge into `AgilePlus/DINOForge-UnityDoorstop/` (placeholder empty;
  no source to merge without network clone).
- No upstream sync from `NeighTools/doorstop`.
- No force-push, no history rewrite.

## Supersedes chain

| from | to | reason |
|------|----|--------|
| `KooshaPari/UnityDoorstop-NexusPatched` | `AgilePlus/DINOForge-UnityDoorstop` | user-directed "actual linked fork repo"; preserve 3rd-party upstream attribution |

## User decision (2026-07-28)

> *"D UDNP to our actual linked fork repo Y"*

Captured in registry row `repo-UnityDoorstop-NexusPatched-fork-link.user_decision_2026-07-28`.

## Open items

1. `AgilePlus/DINOForge-UnityDoorstop/` is empty locally — needs population
   from `KooshaPari/UnityDoorstop-NexusPatched` (currently GH-archived; would
   require network clone) or upstream `NeighTools/doorstop`.
2. If population is desired, network access to `https://github.com/KooshaPari/UnityDoorstop-NexusPatched.git`
   (archived, read-only) is needed.
