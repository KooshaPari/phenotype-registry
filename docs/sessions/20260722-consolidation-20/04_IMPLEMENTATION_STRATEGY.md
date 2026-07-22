# Implementation Strategy

## Approach

1. Treat repository metadata as evidence, not authorization.
2. Resolve the actual default branch for each source before comparison; eight are not `main`.
3. Correct Batch A placement errors before reusing its conclusions.
4. Under 98% disk usage and about 22 GiB free, fetch only partial bare-clone objects needed for proof.
5. Compare source and destination commit SHAs, then compare content independently.
6. Preserve HOLD and VERIFY-ONLY states unless both proof classes satisfy binary acceptance.

## Safety Boundaries

- No repository deletion.
- No force-push or history rewrite.
- No remote mutation during this packet.
- No mutation of `PriceyApp`, `router-docs`, or `template-commons` fork remotes.
- No READY classification inferred from naming, reachability, or prior Batch A placement alone.
