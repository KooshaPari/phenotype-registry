# Research

## Findings

- `phenotype-bus` is the shared event bus for Phenotype cross-collection
  messaging.
- Its README explicitly lists Sidekick agent dispatch and messaging as one of
  the integration surfaces.
- The canonical checkout was clean, but repo instructions require feature work
  in `repos/phenotype-bus-wtrees/<topic>/`.

## Decision

Treat `phenotype-bus` as in scope for the sladge governance rollout and land
the badge in an isolated worktree branch.
