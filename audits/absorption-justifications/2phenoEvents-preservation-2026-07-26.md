# 2phenoEvents — Preservation Evidence

**Date:** 2026-07-26  
**Source:** `KooshaPari/2phenoEvents`  
**Canonical comparison target:** `KooshaPari/phenoEvents`  
**Disposition:** preserve as historical provenance; no code lift

## Exact ref preservation

The source `main` ref was verified before mutation:

| Remote ref | SHA |
|---|---|
| `refs/heads/main` | `5bb0c894e44a50079035b3d5ab5d31946fc445c1` |
| `refs/heads/archive/2phenoEvents/main` | `5bb0c894e44a50079035b3d5ab5d31946fc445c1` |

The archive ref was created as an additive branch on the source repository. No
existing ref was deleted, rewritten, or force-pushed.

Verification command:

```sh
git ls-remote https://github.com/KooshaPari/2phenoEvents.git \
  refs/heads/main refs/heads/archive/2phenoEvents/main
```

## Boundary decision

The `2phenoEvents` and `phenoEvents` source trees were byte-identical for the
runtime EventBus implementation during the boundary audit. `phenoEvents` is the
larger canonical parent and already has the absorption record at
`audits/absorption-justifications/phenoEvents-2026-07-17.md`. No additional
source, tests, or dependencies should be lifted from `2phenoEvents`.

The frozen 2026-07-22 preservation manifest does not contain this later
candidate and has `archive=false`; therefore this evidence packet deliberately
does not alter that historical manifest or the frozen disposition index.

## Safety checks

- Source `main` SHA was checked against the requested value before push.
- Archive branch points to the exact same commit.
- No delete, rename, force-push, or working-tree cleanup was performed.
- Registry change is documentation-only.
