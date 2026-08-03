# Specifications

## Functional requirements

1. Inventory all repository roots, worktrees, refs, stashes, dirty files, untracked files, and local-only commits.
2. Publish and verify a recoverable remote ref for every source-bearing local-only state.
3. Record canonical owner, provenance, overlap classification, and promotion status in this registry.
4. Reconcile PR heads against current remote `main` before merge.
5. Require green checks, resolved review feedback, focused tests, and dogfood before promotion.
6. Require semantic deduplication and contract/parity evidence for overlaps.
7. Create reversible archive/tombstone packets; sponsor approval is mandatory before retirement.
8. Keep AgilePlus parked unless explicitly reactivated.

## Acceptance criteria

- No source-bearing local-only state remains unclassified.
- Every preserved state has an exact SHA-verifiable remote ref.
- Every lane has a canonical parent or approved boundary spike.
- Every promoted PR has green required checks and dogfood evidence.
- Every tombstone/archive has reversible provenance.
- Registry main contains the authoritative final scorecard.

### TruffleHog workflow repair contract (2026-08-03)

- Pull requests scan only the base/head differential.
- Full-history scans run only on `main`, scheduled, and manual-dispatch events.
- The workflow uses only supported TruffleHog inputs.
- A verified Sentry finding remains an incident gate; preserve-first forbids history rewrite.

ARU: credential revocation proof is external to this repository and must be verified before any hosted-policy decision.
