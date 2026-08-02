# Local Estate Inventory and Next Cohort

Evidence timestamp: 2026-08-01 10:42 UTC.

## Coverage

The container currently exposes 51 direct Git roots at depth three. Airlock's registered
estate contains 173 paths; its dry-run cleanup pass visited all 173, recovered 29 stash
payloads, and reported no execution errors. Registered paths include stale/missing checkout
records, so the two counts are intentionally kept separate until each path is reconciled.

No repository deletion, reset, clean, force-push, or archive operation was performed in this
inventory slice.

## Preservation tranche

The following recovery refs are cloud-visible. A `HEAD` snapshot preserves the committed tip;
it does not claim that still-dirty files are captured. Stash-applied refs are called out
separately.

| Repo | Local state | Cloud evidence | Dirty payload status |
|---|---|---|---|
| AgilePlus | `main@16da102a`, clean after Airlock stash recovery | `wip/preserve-20260801/agileplus-dirty-0605` and Airlock `wip/20260801T0622-18c79a33f7004e48` | captured in committed recovery tip |
| Tracera | `preserve/tracera-dirty-wave-20260729@9be786f7d`, 57 tracked + 19 untracked dirty | `wip/20260801T0834-18c7a16c00a168a8` -> `d334cd5`; recovery `wip/preserve-20260801/tracera-dirty-capture-0955` -> `47ef7f41` | 62 source/docs/test/manifest paths captured from current tip; original checkout remains dirty |
| SessionLedger | `main@7b1c243e`, 19 tracked + 4 untracked entries (17 files) | `wip/20260801T0545-18c7982ff4167f78` -> `7b1c243e`; recovery `wip/preserve-20260801/sessionledger-dirty-capture-0902` -> `ec278e3c`; immutable `a5d315ba` Airlock ref | 21 source paths captured; 15 generated coverage/mutation files excluded; original checkout remains dirty |
| pheno-harness | `fix/pheno-harness-runner-provenance@4131b7c`, 2 tracked + 52 untracked entries | `wip/20260801T0545-18c798307b9e40c0` -> `4131b7c`; recovery `wip/preserve-20260801/pheno-harness-dirty-capture-0902` -> `9fdef790` | 90 source/spec/test/kernel/evidence paths captured; `PRESERVATION_EXCLUSIONS.md` records generated/cache/worktree exclusions; original checkout remains dirty |
| pheno | `main@be5da947`, 14 tracked + 2 untracked entries | `wip/20260801T0545-18c79831061b87d0` -> `be5da947`; recovery `wip/preserve-20260801/pheno-dirty-capture-0955` -> `6140133` | 5,236 source/spec/test/config paths captured; generated/cache/worktree exclusions recorded; original checkout remains dirty |
| sharecli | `fix/runtime-openapi-drift@b8eeeb2`, 22 dirty and 8 stashes | `wip/20260801T0545-18c798318ac38d70` -> `b8eeeb2`; recovery `wip/preserve-20260801/sharecli-dirty-capture-0955` -> `08ad5d10` | 23 tracked/source/doc/manifest paths captured; original stash refs remain untouched |
| forgecode | `preserve/workflow-schema-wave-20260729@aa25f50e`, clean after Airlock stash recovery | `wip/preserve-20260801/forgecode-dirty-0605` and Airlock `wip/20260801T0622-18c79a346ecd6370` | captured in committed recovery tip; fork remote used because origin is upstream-only |

The seven `HEAD` refs are continuity evidence, not a completion claim for the dirty working
trees. The next preservation action is to capture source-bearing dirty/untracked payloads in
isolated recovery commits or stash bundles, after excluding generated caches and secrets.

## Next boundary cohort (triage, not merge authorization)

These small or medium surfaces are candidates for parent-boundary review after their source
refs are preserved. Existing registry boundary documents remain authoritative; the proposed
parent is a hypothesis until code/spec parity is proven.

| Candidate | Initial parent hypothesis | Evidence to collect before mutation | Initial disposition |
|---|---|---|---|
| Agentora | AgilePlus satellite or standalone agent runtime | `main@c7edae8`, 10 commits behind origin; only local state is `.trunk` conflict/generated tool metadata; registry audit says embedded pheno-agent crates do not prove migration | HOLD / preserve source separately; exclude `.trunk` runtime state |
| Benchora | phenotype-tooling `crates/benchora/` | verify absorbed tree and remote refs | PARITY CHECK |
| Grapheon | Tracera data/trace layer | live repo role, shared crates, unique history | HOLD / keep distinct until proven |
| HexaKit | substrate/library boundary | compare with `pheno` and phenotype-tooling ports | HOLD |
| Melosviz | observability/UI support | language/build surface and consumers | HOLD |
| PhenoObservability | canonical observability parent | Sidekick/curated-traces parity and current main | PARENT CANDIDATE |
| PhenoPlugins | `pheno` plugin crates | verify archived source and tree parity | ARCHIVE-ONLY pending proof |
| Planify2 | AgilePlus governance consumer | compare specs/tasks and parent ownership | HOLD |
| PlayCua | desktop/browser automation | consumer graph and standalone release boundary | KEEP-STANDALONE candidate |
| RepoLedger | registry/AgilePlus governance evidence | exact source refs and target contract | HOLD |
| ResearchLedger | research/session artifact boundary | relation to SessionLedger/phenoAI | HOLD |
| Tokn | standalone Rust token library | consumer and API parity with `pheno` | KEEP-STANDALONE candidate |
| asset-engine | phenotype-apps/graphics boundary | package graph and deployment ownership | HOLD |
| hfscope | observability/tooling | source size, consumers, duplicate APIs | HOLD |
| hwLedger | app-plane hardware runtime | existing boundary and OMLX sidecar provenance | KEEP-STANDALONE / archive-only review |
| nanovms | thegent/PhenoCompose integration | runtime ownership and unique history | HOLD |
| pheno-rt-spec-probe | pheno spec/test boundary | source refs and consumer contracts | HOLD |
| phenotype-apps | app-plane parent | deployment surfaces and duplicate sites | KEEP-PARENT candidate |
| phenotype-hub | integration/product surface | role taxonomy and consumers | HOLD |
| phenotype-python-sdk | SDK boundary | API compatibility and package ownership | KEEP-STANDALONE candidate |
| phenotype-journeys | product/workflow surface | relation to AgilePlus and phenotype-apps | HOLD |

## Boundary-audit results (no mutation authorized)

| Surface | Evidence-backed disposition | Remaining proof gate |
|---|---|---|
| Tracera | KEEP standalone durable trace/evidence/audit consumer; interoperate with PhenoObservability producer and Agentora envelopes by explicit contracts | producer metadata/envelope schema, SQLite+PG route/store parity, replay provenance, consumer inventory, then sponsor gate |
| sharecli | KEEP Rust runtime as canonical; preserve `thegent-sharecli` as archive-only lineage and label `thegent/sharecli` as an unproven Python facade | run `coordination-lock-queue-v1` parity fixture; reconcile archived-repo and registry boundary-doc contradiction; sponsor gate before extraction/archive |
| pheno nested AgilePlus | HOLD duplicate shelf; canonical parent remains standalone `AgilePlus` (2,012 of 2,016 captured paths path-identical) | recover ignored Cargo manifests/locks and compare source SHA/API/test provenance before any branch or tombstone action |
| pheno nested HexaKit | HOLD blanket absorption; canonical parent remains standalone `HexaKit` bootstrap/template workspace; route 14 overlapping crate names individually | recover ignored manifests and prove API/dependency/test parity per crate; reconcile source `BOUNDARY.md` with registry disposition |

This cohort is a research queue only. No archive or merge action is authorized by this table.

## Immediate gates

1. All five dirty lanes now have cloud recovery refs: SessionLedger (`ec278e3c`), pheno-harness
   (`9fdef790`), Tracera (`47ef7f41`), sharecli (`08ad5d10`), and pheno (`6140133`). Classify
   residual generated/local state and parent-boundary semantics before any merge/archive action.
   The pheno ref is preservation-only: 119 of 151 nested Cargo manifests/locks are absent and
   must be force-added in a follow-up source capture before build or absorption claims.
2. Revalidate PR #442's ordering fix at head `33e0cdf`; Kilo review passes and all review threads are resolved, but required contexts are absent and docs/secret-guard fail (current trufflehog passes).
3. Repair the concrete #443 blockers (VitePress parse error and unpinned actions), then
   only then synchronize #441/#442 to materialize `ci / lint` and `ci / test` on their heads.
4. Keep PR #432 held until the unresolved OMLX gitlink `a7118ed9...` has an immutable,
   cloud-resolvable owner or is split into an evidence-only packet.
5. ShareCLI post-capture source is now preserved at `fd2a4eea`; pheno still needs a
   source-only manifest capture because `6140133` omitted ignored Cargo manifests.
