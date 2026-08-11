# Research

## Findings

- GitHub owner is `KooshaPari`; 291 owned repositories were enumerated.
- `AgilePlus` is the canonical spec-lifecycle platform spine, not a catch-all archive owner.
- Seven source remotes are empty shells; emptiness does not prove namesake local work reached cloud.
- `AgilePlus-recovery-20260714` is already reachable from canonical AgilePlus.
- The harmonizer implementation was absorbed by AgilePlus PR 756; only provenance remains.
- `zz-archive-phenotype-omlx-tmp` has 28 of 29 heads represented; its default `main` is missing.
- `omniroute-rust` is a 13-crate workspace and requires crate-level ownership review.

## Authority order

`BOUNDARY_OWNERS.md` and accepted ADRs override stale absorption rows and July 21 catch-all runbooks.

## Cockpit source-boundary evidence (2026-08-11)

### Observed chain

| Role | Path | Git state | Snapshot evidence |
|---|---|---|---|
| Bead input | `phenotype-dag/beads.jsonl` | Non-Git directory | SHA-256 `9f681cd9694e7582c6adb0a04b522bc623beacf126c4c13d7023694506ce06c8` |
| Renderer | `beads/bead-cockpit.py` | Non-Git directory | SHA-256 `82f4ffa438839510cf2dc4dfce2c17ba919a92a73df457db2341dbc7215bb3a4` |
| Rendered cockpit | `cockpit/bead-cockpit-20260809-191131-f5ca38f7.html` | Non-Git directory | SHA-256 `004be4719d9b3fce533c47ce22ee50bb2567718a8b737b74e0b548384c495c26` |

The snapshot was generated at `2026-08-11T06:53:33Z` and reported 594 beads, 444 targets, and
237 agents. `~/.agileplus/cockpit.ndjson` is a stale July 5 score stream, not the cockpit source
of truth and not a substitute for either the bead ledger or renderer.

### Revalidation and drift handling

At `2026-08-11T07:32Z`, direct SHA-256 revalidation still found all three directories non-Git,
but found different live bytes: `beads.jsonl` `6bf1a480db69c243aa3e55152ee993698fb363e8c4b45c01871f9b6ba259577b`,
`bead-cockpit.py` `d98cc8570e91b6c49ea05f7aa622e838c75227b6a9a4c9d33e5db81d59e8221c`, and the HTML
`d7092ef96069bfa88b2a8fad137bc6d72c906dd5011dc61dc96f8082d9491483`.

The later observation does not supersede or invalidate the 06:53 evidence. It demonstrates why
an atomic writer and renderer migration is required before any boundary cutover.

### Boundary decision

| Capability | Canonical role | Decision |
|---|---|---|
| Operational workflow and lifecycle | AgilePlus | Successor once it atomically owns writes and rendering |
| Schema, governance, and preservation evidence | phenotype-registry | Canonical boundary and decision ledger |
| Read model and future consumption | Tracera | Future consumer after stable source contract |
