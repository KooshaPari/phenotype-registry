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

## 2026-08-12 cockpit custody gates

- Parse `custody/cockpit/20260812/provenance-manifest.json` as strict JSON.
- Compile the copied builder, parse every copied `beads.jsonl` line as JSON, and recompute copied-file SHA256 and byte-size values against the manifest.
- Run `git diff --check`; do not run the builder or publish rendered HTML as part of this source-only custody gate.
