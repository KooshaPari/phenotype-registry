# Specifications

## Functional requirements

1. Record exactly 20 candidate repositories.
2. Record canonical parent and non-destructive disposition for each candidate.
3. Preserve source SHA/ref provenance before imports.
4. Import only into namespaced archive or recovery refs.
5. Verify imported SHAs through the GitHub API.
6. Keep archive, rename, delete, and active-branch merge actions outside W0-W2.

## Acceptance criteria

- JSON parses with `jq` and contains 20 candidates.
- Every candidate has a target, disposition, gates, and W1/W2 status.
- Empty shells remain blocked on a local-payload search.
- No source repository settings or refs change during W0.

## Out of scope

Repository archival/deletion, consumer migrations, semantic feature merges, and cleanup of local
worktrees or recovery bundles.
