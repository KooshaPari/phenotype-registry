# Testing Strategy

## W0

- `jq empty preservation-manifest.json`
- Assert candidate count equals 20.
- Run `scripts/validate-ecosystem.sh` when executable.
- Confirm no source repository was mutated.

## W1-W2

- Compare source and target ref SHAs before and after push.
- Query target commits through GitHub API.
- Verify branch and tag counts match the manifest.
- Treat missing reachability as a hard failure; do not proceed to archive review.

## Cockpit evidence checks

```sh
shasum -a 256 phenotype-dag/beads.jsonl
shasum -a 256 beads/bead-cockpit.py
shasum -a 256 cockpit/bead-cockpit-20260809-191131-f5ca38f7.html
git -C phenotype-dag rev-parse --is-inside-work-tree
git -C beads rev-parse --is-inside-work-tree
git -C cockpit rev-parse --is-inside-work-tree
```

- Verify the recorded 06:53 snapshot hash chain as a historical observation, not a live-current
  assertion.
- Rehash live bytes immediately before a migration proposal; record any mismatch as drift.
- Confirm no source directory was initialized, moved, deleted, or replaced.
- Validate this registry documentation diff is limited to the existing preservation-wave session.
