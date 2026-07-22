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
