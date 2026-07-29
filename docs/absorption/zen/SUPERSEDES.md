# ABSORPTION DOCKET — `zen`

## State

| field | value |
|-------|-------|
| source | `KooshaPari/zen` (Public, "Other", Apr 3, deprecated template) |
| target (proposed) | `HexaKit/governance/` |
| target (actual local) | **MISSING** — `HexaKit/` top-level dir does not exist locally |
| classification | `J:DEPRECATED_TEMPLATE` |
| status | `TOMBSTONE_ONLY_TARGET_MISSING` |
| archived at | 2026-07-28 |
| domain | deprecated minimal template |
| boundary doc | `phenotype-registry/docs/boundary/legacy-game-mods.md` |

## Migration works

`zen` is a deprecated minimal template whose functionality was already
consolidated into `HexaKit` (per `phenotype-registry/projects/zen.json:14`).
The proposed target `HexaKit/governance/` does not exist locally — the
`HexaKit/` top-level directory is absent from `~/CodeProjects/Phenotype/repos/`.

### What was done

1. Confirmed `HexaKit/` is missing locally (filesystem audit, 2026-07-28).
2. No fresh clone present for `KooshaPari/zen` (GH-archived).
3. Created this docket + registry row `repo-zen-tombstone`
   (disposition-index.json v1.6.82, 2026-07-28).
4. Captured tombstone state in `legacy-game-mods.md` boundary doc.

### What was NOT done

- No scaffold of `HexaKit/` repo (not approved; user said "zen Y" = tombstone).
- No code migration (deprecated template; functionality already in HexaKit per
  upstream notes).
- No source-clone fetched (private repo, GH-archived).

## Supersedes chain

| from | to | reason |
|------|----|--------|
| `KooshaPari/zen` (deprecated template) | `HexaKit/governance/` (target missing locally) | functionality already in HexaKit; tombstone-only since target not present |

## User decision (2026-07-28)

> *"zen Y"*

Captured in registry row `repo-zen-tombstone.user_decision_2026-07-28`.

## Open items

1. `HexaKit/` repo does not exist locally. If the user later wants to scaffold
   it, the `zen` content can be re-absorbed into `HexaKit/governance/`.
2. No fresh clone of `KooshaPari/zen` exists; if content is needed, network
   fetch required (repo is GH-archived).
