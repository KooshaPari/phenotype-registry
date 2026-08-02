# Local Estate Inventory and Next Cohort

Evidence timestamp: 2026-08-02 22:12 UTC.

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
| pheno | `main@a3c9dde`, 14 tracked + 2 untracked entries | `wip/20260801T0545-18c79831061b87d0` -> `be5da947`; recovery `wip/preserve-20260801/pheno-dirty-capture-0955` -> `6140133`; follow-up `wip/preserve-20260802/pheno-source-manifest-capture` -> `ee890798` | 5,236 source/spec/test/config paths plus 119 missing manifests and six whitelisted metadata files captured; generated/cache/worktree exclusions recorded; original checkout remains dirty |
| sharecli | `fix/runtime-openapi-drift@b8eeeb2`, 22 dirty and 8 stashes | `wip/20260801T0545-18c798318ac38d70` -> `b8eeeb2`; recovery `wip/preserve-20260801/sharecli-dirty-capture-0955` -> `08ad5d10` | 23 tracked/source/doc/manifest paths captured; original stash refs remain untouched |
| OmniRoute | `fix/stray-brace-mitm-manager@03c6b8a`; source tree clean after auto-commit; six stashes remain | source capture `03c6b8a`; stash refs `wip/preserve-20260802/omniroute-stash-0..5` | nine source/config/test/workflow paths and all six stash commits are cloud-preserved; original stash stack remains untouched |
| ResearchLedger | `main@0c207459`, 25 dirty source/docs entries | `wip/preserve-20260802/researchledger-dirty-capture` -> `3b3facc` | 25 source/docs paths captured in isolated ref; original checkout remains dirty |
| hfscope | `fix/preserve-search-kind@f119063`, one tracked source delta | `wip/preserve-20260802/hfscope-dirty-capture` -> `865670b` | `internal/hfapi/client.go` captured in isolated ref; original checkout remains dirty |
| forgecode | `preserve/workflow-schema-wave-20260729@4fe8aaf0`, 3 dirty source/docs files | prior recovery `wip/preserve-20260801/forgecode-dirty-0605`; follow-up `wip/preserve-20260802/forgecode-dirty-capture` -> `ab49d70` on fork remote | current `update.rs` and two packaging docs captured; original checkout remains dirty |
| thegent | `chore/thegent-governance-integration-wave@d0f31a2`, one tracked post-capture delta; 5 stashes remain | `wip/preserve-20260802/thegent-postcapture` -> `b9ce6c1`; `thegent-stash-0..4` exact remote refs | current source delta and all five stash commits are cloud-preserved; classify payloads before cleanup |

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
| Planify2 | AgilePlus/phenotype-apps frontend boundary | clean `main@e6b8e235`, 5,402 tracked files; original `origin` returns repository-not-found; preserved to `KooshaPari/Planify:wip/preserve-20260802/planify2-local-main` at the same SHA; README identifies Plane AGPL upstream plus Phenotype `site/` and `infra/` layers | HOLD / preservation branch only; sponsor-approved parent/new-repo decision |
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

## Verified next-20 cohort scan

Read-only scan of 45 direct roots, cross-checked against current GitHub metadata on
2026-08-02. Ranking is an evidence queue, not merge authorization.

| Rank | Repo | Local SHA | GH size/state | Parent hypothesis | Immediate proof gate |
|---:|---|---|---:|---|---|
| 1 | RepoLedger | `7dabedc` | 79 KB/live | registry governance satellite | preserve 53 local-only commits; map registry consumers |
| 2 | asset-engine | `41ade55` | 293 KB/archived | phenotype-apps asset pipeline | prove scripts/assets landed in parent |
| 3 | Benchora | `main@5dff436` (documented `b4fd146` remains an ancestor) | 342 KB/live | phenotype-tooling `crates/benchora` | reconcile live repo vs absorbed registry row |
| 4 | PhenoPlugins | `e57ee79` | 633 KB/live | pheno plugin crates | prove all five crate hashes/builds before tombstone |
| 5 | ResearchLedger | `0c207459` | 795 KB/live | standalone research/session boundary | compare SessionLedger/phenoAI ownership |
| 6 | PlayCua | `29c6c66` | 889 KB/live | standalone browser/desktop automation | complete boundary and consumer inventory |
| 7 | nanovms | `9a0e286` | 985 KB/live | standalone sandbox/VMM | reconcile stale archive wording and Go consumers |
| 8 | Tokn | `d51262f` | 2.5 MB/live | standalone token substrate | reconcile upstream vs Airlock mirror and OmniRoute API |
| 9 | phenotype-python-sdk | `e270d0a` | 5.9 MB/live | standalone Python SDK | map public API ownership and four local commits |
| 10 | PhenoObservability | `9192f73` | 8.5 MB/live | canonical observability parent | rebase 31 local commits and prove consumers |
| 11 | Agentora | `main@18ac868` (WIP `53d370c` preserved at `wip/20260802T0756-18c7edef121191d8`) | 9.5 MB/live | standalone agent runtime | preserve stash; compare embedded agentkit contracts |
| 12 | hfscope | `f119063` | 10.3 MB/private | observability/tooling satellite | test search-kind delta and consumer overlap |
| 13 | HexaKit | `b47132a` | 23 MB/live | standalone scaffold/library | review four metadata divergences and mirror hash |
| 14 | Melosviz | `4a9f195` | 55 MB/live | phenotype-apps UI/observability | reconcile recovery branch and target tree |
| 15 | Planify2 | `e6b8e23` | origin 404 | AgilePlus/phenotype-apps frontend | prove fork ancestry and unique site/infra |
| 16 | Grapheon | `8a15328` | 775 MB/private | standalone Tracera-derived runtime | compare route/store/API lineage |
| 17 | hwLedger | `08a83db` | 543 MB/live | standalone hardware/fleet runtime | reconcile ten local commits and OMLX sidecar |
| 18 | phenotype-apps | `5a06720` | 1.7 GB/live | canonical app-plane parent | publish missing remote provenance and map duplicates |
| 19 | phenotype-hub | `667d77c` | archived/0 KB | registry/integration surface | preserve local commits and prove redirect target |
| 20 | pheno-rt-spec-probe | `5b043a1` | remote 404 | pheno spec/test boundary | publish to live owner or create evidence collection |

Remote default refs and 404/archived states are recorded in the agent audit; no archive,
merge, or tombstone action is authorized by this table.

## Boundary-audit results (no mutation authorized)

| Surface | Evidence-backed disposition | Remaining proof gate |
|---|---|---|
| Tracera | KEEP standalone durable trace/evidence/audit consumer; interoperate with PhenoObservability producer and Agentora envelopes by explicit contracts | producer metadata/envelope schema, SQLite+PG route/store parity, replay provenance, consumer inventory, then sponsor gate |
| Grapheon | KEEP standalone pending boundary review; current recovery checkout is clean at `523b67d` and owns the private Tracera-derived graph runtime | compare route/store/API lineage against current Tracera and `pheno/crates/agileplus-graph`; no proven absorption mapping |
| sharecli | KEEP Rust runtime as canonical; preserve `thegent-sharecli` as archive-only lineage and label `thegent/sharecli` as an unproven Python facade | run `coordination-lock-queue-v1` parity fixture; reconcile archived-repo and registry boundary-doc contradiction; sponsor gate before extraction/archive |
| pheno nested AgilePlus | HOLD duplicate shelf; canonical parent remains standalone `AgilePlus` (`ee890798` vs `main@3b61d0d`: 1,812 of 1,846 common paths byte-identical, 34 divergent) | review the 34 divergent paths plus nested-only/standalone-only surfaces for API/dependency/test provenance before any branch or tombstone action |
| pheno nested HexaKit | HOLD duplicate shelf; canonical parent remains standalone `HexaKit@b47132a`; archive comparison against `ee890798` finds 3,209 common paths, four byte-divergent metadata/docs files, one nested-only path, 529 standalone-only paths, and no differing Cargo manifests/locks | review `.github/workflows/scorecard.yml`, `.pre-commit-config.yaml`, `BOUNDARY.md`, and the two differing docs; sponsor gate before any duplicate-shelf tombstone or absorption action |

This cohort is a research queue only. No archive or merge action is authorized by this table.

## Source-capture wave (2026-08-02)

| Repository | Exact source-bearing capture | Remote/provenance note | Exclusions or gate |
|---|---|---|---|
| OmniRoute | merge sweep `ac631202`; native SQLite `355f0b9`; PR481 review fixes `98102bf`; preservation packet `d8ab8ac`; raw stashes `omniroute-stash-0..5` | `KooshaPari/OmniRoute` `wip/preserve-20260802/*` refs verified with `ls-remote` | merge sweep contains labeled conflict markers and is preservation-only; `.trunk` generated state excluded |
| forgecode | dirty source `64c9a337`; stash `0e091475` | `KooshaPari/forgecode` fork refs verified; tailcallhq Airlock push denied | fork refs are authoritative additive captures; no origin/config rewrite attempted |
| ResearchLedger | `3b3facc` (25 source files, including `chunking.rs` and `reference_fetch.rs`) | `wip/preserve-20260802/researchledger-dirty-capture` verified | generated/ignored paths and secrets excluded |
| hfscope | `865670b` (stash-derived `internal/hfapi/client.go`) | `wip/preserve-20260802/hfscope-dirty-capture` verified | source-only; original stash retained |
| thegent | stash refs `04cfa56`, `116a774`, `e9e54a1`, `9de9c68`, `64162a4` | `KooshaPari/thegent` `wip/preserve-20260802/thegent-stash-0..4` verified | classify payloads before any boundary decision |
| pheno-harness | existing baseline `9fdef790`; four newer worktree scopes pending capture | no new `wip/preserve-20260802` refs verified yet | generated `bench/results/sota/2026-08-02/snapshot.sha256` excluded; do not claim complete |

These refs preserve source provenance only. They do not establish merge readiness,
quality, ownership, or archive/tombstone authorization.

## Immediate gates

1. All five dirty lanes now have cloud recovery refs: SessionLedger (`ec278e3c`), pheno-harness
   (`9fdef790`), Tracera (`47ef7f41`), sharecli (`08ad5d10`), and pheno (`6140133`). Classify
   residual generated/local state and parent-boundary semantics before any merge/archive action.
   The pheno recovery ref is preservation-only. Follow-up source capture
   `wip/preserve-20260802/pheno-source-manifest-capture` -> `ee890798` now adds the 119
   previously missing manifests and six whitelisted metadata files; build, parity, and
   absorption claims remain gated on API/dependency/test evidence.
2. Revalidate PR #442's ordering fix at head `33e0cdf`; Kilo review passes and all review threads are resolved, but required contexts are absent and docs/secret-guard fail (current trufflehog passes).
3. Repair the concrete #443 blockers (VitePress parse error and unpinned actions), then
   only then synchronize #441/#442 to materialize `ci / lint` and `ci / test` on their heads.
4. Keep PR #432 held until sponsor review selects the pointer-only candidate
   `wip/preserve-20260802/registry-omlx-pointer-repair` -> `a407839` (which replaces
   `a7118ed9...` with cloud-resolvable `52682309...`) and Kilo/protected checks are green.
5. ShareCLI post-capture source is now preserved at `fd2a4eea`; pheno source-only manifest
   follow-up is now preserved at `ee890798`. Remaining work is the API/dependency/test
   parity audit for overlapping AgilePlus and HexaKit crates.
6. ResearchLedger source/docs payload is now preserved at `3b3facc` and hfscope's tracked
   client delta at `865670b`; compare their consumers and ownership before any parent,
   archive, or tombstone action.
7. The 2026-08-02 source-capture wave is recorded above: OmniRoute, forgecode,
   ResearchLedger, hfscope, and thegent have exact remote refs; pheno-harness's four
   newer worktree scopes still require additive capture and verification.
