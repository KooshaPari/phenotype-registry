# 2phenoEvents reconciliation — 2026-07-29

## Scope

Resolve the recovered recovery-variant project record `projects/2phenoEvents.json` against
current GitHub reality and canonical `phenoEvents` lineage.

## Remote evidence

```text
Repo: KooshaPari/2phenoEvents
Result: Not Found (404)
```

## Boundary decision

`2phenoEvents` is a recovery-era name variant with no resolvable remote repository.

- No local clone exists at `repos/2phenoEvents`.
- No source content can be absorbed.
- Keep only canonical `KooshaPari/phenoEvents` as the active lineage reference.

Record this row as a tombstoned/never-existed variant and preserve the closure in the
parent `phenoEvents` boundary history.

## Commands

```zsh
gh api repos/KooshaPari/2phenoEvents
rg -n '2phenoEvents' projects/2phenoEvents.json projects/phenoEvents.json
```
