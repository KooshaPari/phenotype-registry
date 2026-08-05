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
| PhenoObservability | canonical `KooshaPari/PhenoObservability` remote | local clean WIP and live-main parity/gate evidence | KEEP_STANDALONE/HOLD |
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
| 1 | RepoLedger | `7dabedc` | 79 KB/live | registry governance satellite | reconcile local 2-ahead/54-behind divergence with `origin/main=f6b90b8`; map registry consumers |
| 2 | asset-engine | `41ade55` | 293 KB/archived | phenotype-apps asset pipeline | prove scripts/assets landed in parent |
| 3 | Benchora | `main@5dff436` (documented `b4fd146` remains an ancestor) | 342 KB/live | phenotype-tooling `crates/benchora` | reconcile live repo vs absorbed registry row |
| 4 | PhenoPlugins | `e57ee79` | 633 KB/live | pheno plugin crates | prove all five crate hashes/builds before tombstone |
| 5 | ResearchLedger | `0c207459` | 795 KB/live | standalone research/session boundary | compare SessionLedger/phenoAI ownership |
| 6 | PlayCua | `29c6c66` | 889 KB/live | standalone browser/desktop automation | complete boundary and consumer inventory |
| 7 | nanovms | `9a0e286` | 985 KB/live | standalone sandbox/VMM | reconcile stale archive wording and Go consumers |
| 8 | Tokn | `d51262f` | 2.5 MB/live | standalone token substrate | reconcile upstream vs Airlock mirror and OmniRoute API |
| 9 | phenotype-python-sdk | `e270d0a` | 5.9 MB/live | standalone Python SDK | map public API ownership and four local commits |
| 10 | PhenoObservability | clean `wip/2026-07-22-phenoobservability-worklog@9192f73` | 8.5 MB/live | canonical observability remote | KEEP_STANDALONE/HOLD; reconcile stale/diverged PR #209, strict protection, and consumer proof |
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
| pheno-harness | main Harbor gate/test `1ee490d`; core intent `9c3d030`; fix-gen sources `961e662`; prefer-314t docs `a79bbd0`; existing baseline `9fdef790` | dedicated recovery/Airlock refs verified at `wip/20260802T2300-18c81f441c2eada0`, `wip/preserve-20260802/*`, and recovery refs | generated `bench/results/sota/2026-08-02/snapshot.sha256` excluded; larger local main remains ahead of hosted `main=0ee95d9` |

These refs preserve source provenance only. They do not establish merge readiness,
quality, ownership, or archive/tombstone authorization.

## Follow-up source-capture wave (2026-08-04)

| Repository | Remote ref and exact commit lineage | Stable diff hash and captured source scope | Explicit exclusions / gate |
|---|---|---|---|
| ResearchLedger | `origin:wip/preserve-20260804/researchledger-source-followup-20260804T0913` -> `b649002ce4fd9c41ad2badafd653fe992df99ac3` (parent `c501b0e66c591cb14737d6a8c356101d14a21000`) | patch-id `adb6d443b1d0246ed1e8042c43bd11630dd1d4a3`; desktop Rust command/embedding/GitHub/RAG/storage and CSP work, capture scripts, UI and Rust contract fixtures/tests, docs and package manifest | Generated outputs, caches, ignored material, secrets, and linked-worktree payloads were excluded; preservation receipt only. |
| forgecode | `fork:wip/preserve-20260804/forgecode-source-followup-20260804T0915` -> `dccf42deda18ca6da8bf204ac8cc4c489473c01d` (parent `8ff6fcbe1d2e5490664ddc0a7d4fe126c1c1c56e`) | patch-id `e6151d4d616ea7b6fbfcbea05d38355f60715aef`; release workflow, Cargo lock, Forge CI publish implementation/tests, main/native update/UI/updater code, and `install.sh` | Generated outputs, caches, ignored material, secrets, and linked-worktree payloads were excluded; fork receipt is additive and does not alter upstream. |
| thegent | `origin:wip/preserve-20260804/thegent-test-delta-capture` -> `a660a882a1f74750b4d0b825ba0828d4075f093a` (parent `bc91aff123b80a9320c59a657846b09c45058531`) | patch-id `e1e1dfa38f4f3d61647a74cfa97fc2c6173b8cb0`; execution-extraction CLI test delta | Generated outputs, caches, ignored material, secrets, and linked-worktree payloads were excluded; no boundary decision follows. |
| phenotype-tooling | `origin:wip/preserve-20260804/phenotype-tooling-inbox-delta-capture` -> `97ac922818e1010404ee297938247d33365588c7` (parent `134d35599d76273c7d404e377834ab30db54c9f1`) | patch-id `c1d517c0b87124c3e8c2802d18726dfef9d586d5`; `crates/elicitate/src/inbox/mod.rs` inbox source delta | Generated outputs, caches, ignored material, secrets, and linked-worktree payloads were excluded; preservation receipt only. |
| pheno-harness | `origin:wip/preserve-20260804/pheno-harness-desktop-lane-followup-20260804T0938` -> `3ab267da9d6eaeacf99263b84cd1a32a6eddf94a` (parent `3b82a033b4e7390f085075306fc7fe1d62071b01`) | patch-id `fb413b30943d081d6d1bd2f88902db32688908bc`; desktop fixture/evaluation/dual-GPU launch scripts plus desktop fixture/eval/launcher tests | Generated outputs, caches, ignored material, secrets, and linked-worktree payloads were excluded; preservation receipt only. |

All five hosted refs were reconciled as capture receipts. This wave makes no claim of
promotion, quality, ownership, parity, merge readiness, archive/tombstone eligibility, or
pointer/PR state change.

## Boundary review wave (2026-08-03)

| Surface | Evidence-backed provisional disposition | Required proof before any move |
|---|---|---|
| ResearchLedger | KEEP standalone/HOLD; Tauri/Vite app has no sibling manifest consumer edge | hosted CI/build, lineage and ownership receipt |
| PlayCua | KEEP split runtime/HOLD; Eidolon exposes only a trait-level conceptual port, not a manifest dependency | concrete transport implementation and target workspace dependency closure |
| PhenoObservability | KEEP_STANDALONE/HOLD; OmniRoute has Rust path copies and an optional `@pheno-otel/tracing` specifier with prior npm E404 | exact-tree/API parity and hosted consumer CI proof |
| Agentora | KEEP canonical hub/HOLD; active workspace has no sibling `agentkit` manifest imports; old Python row is archived | live-main CI/license and consumer-boundary proof |
| hfscope | KEEP standalone/HOLD; Go server and browser extension have no sibling manifest edges | branch reconciliation, Go test/build, extension API and auth hygiene |
| HexaKit | KEEP canonical scaffold/HOLD; no external manifest consumers found, while registry archive/retire labels conflict | exact crate ownership and parity with Agentora/PhenoObservability |
| Melosviz | HOLD; registry owner/absorption records conflict and no path consumers were found | authoritative owner, source SHA/tree, test claim, and target parity receipt |

These are evidence-backed holds, not merge/archive/tombstone approvals.

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
   ResearchLedger, hfscope, thegent, and the four pheno-harness scopes have exact
   recovery/Airlock refs; quality, ownership, and promotion gates remain separate.

## 2026-08-03 capture and boundary checkpoint

The following evidence is read-only and does not authorize merge, archive, tombstone,
delete, or remote mutation.

| Surface | Exact local/remote evidence | Recommended boundary | Evidence gap |
|---|---|---|---|
| `pheno-rt-spec-probe` | local `main@5b043a1f`; 22 tracked files; origin `KooshaPari/phenotype-router-spec` returns 404 | preserve as a probe/evidence collection under `phenotype-registry`; keep canonical router protocol docs as the parent | 8 of 9 compared protocol/schema files differ from current absorbed copies; semantic reconciliation is required |
| `phenotype-apps` | local `main@5a067202`; 57 tracked files; no configured remote; GitHub `KooshaPari/phenotype-apps` is active with default `apps-extract`; recovery ref `recovery/phenotype-apps-local-20260726` equals `5a067202` | KEEP standalone as the app-plane parent | registry retirement/archive wording conflicts with live GitHub metadata; reconcile local slice ancestry with `apps-extract`/`main` |
| `phenotype-hub` | local `main@667d77c`; 194 tracked files; GitHub archived and `diskUsage=0`; live remote HEAD `c7dd053e` | archive-only provenance pointer to the absorbed hub docs; no new parent | local merge and live archived remote diverge; verify the redirect target and preserve local commits before any cleanup |
| `Planify2` | local `feat/dual-harness-fixture-path-fix@e6b8e235` (local `main` is same); original `KooshaPari/Planify2` returns 404; `Planify:wip/preserve-20260802/planify2-local-main` equals `e6b8e235` | Planify is the preservation parent; keep Planify2 as a source-boundary record pending sponsor decision | fork ancestry, unique `site/`/`infra/` delta, and Planify parent ownership still need proof |

### Next-20 boundary evidence

| Surface | Evidence-backed disposition | Remaining gate |
|---|---|---|
| Benchora (`main@5dff436`) | KEEP standalone; live source is canonical and the nested shelf is not parity | prove a migration manifest/API-owner map, real consumers, and focused source/target build-test evidence before any new boundary proposal |
| PhenoPlugins (`e57ee79`) | HOLD; 36 common paths, 15 identical, 21 divergent, 62 missing; historical target is unreachable | restore target provenance and complete crate/hash/build comparison |
| asset-engine (`41ade55`) | archive-only preservation; clean archive branch, archived remote main `e188dab`; no project manifest and README restoration claim remains unproven | prove artifact/asset consumers and any restoration provenance; no parent attach or retirement action |
| nanovms (`9a0e286`) | KEEP standalone | map runtime/VMM consumers before any parent proposal |
| PlayCua (`29c6c66`) | KEEP_STANDALONE/HOLD; hosted default is `master=cda798f` while a distinct non-default `main=43d2e8d` also exists; Eidolon bridge remains trait-only | complete concrete transport, consumer scan, and target-workspace dependency closure |
| RepoLedger (`7dabedc`) | KEEP/HOLD; clean `main` is ahead 2/behind 54 of current `origin/main=f6b90b8`; preserve ref is remote-verifiable; pnpm/Bun workspace has no registry/AgilePlus edge | the older `53 local-only commits` classification is stale; complete consumer ownership and divergence proof before any parent or boundary action |

### Next-20 completion checkpoint (2026-08-04)

This finishes evidence coverage for the four remaining named next-20 surfaces. It is a
preservation and boundary checkpoint only: no merge, archive, tombstone, pointer,
project-metadata, or pull-request action is authorized.

| Surface | Exact returned ref/state | Evidence-backed disposition | Remaining proof gate |
|---|---|---|---|
| Grapheon | recovery checkout clean at `523b67d` (earlier inventory source `8a15328`) | KEEP standalone private Tracera-derived graph runtime | route/store/API lineage against current Tracera and `pheno/crates/agileplus-graph`, plus consumer proof; no proven absorption mapping |
| hwLedger | local source `08a83db`; GitHub live, 543 MB | KEEP standalone / archive-only review | reconcile ten local commits and OMLX sidecar provenance; classify reusable fleet/capacity capability before any archive proposal |
| phenotype-apps | local recovery source `5a0672024b798f852b6a36eaa83820c424d0b5aa`; active GitHub default `apps-extract=f4c559fcf1abcbcc2bde210b08ae9dd4e2e18ddb`; `recovery/phenotype-apps-local-20260726` equals the local source | KEEP standalone canonical app-plane parent | reconcile local ancestry with `apps-extract` and `main=6a41bf015b9b4a333d2a2efd8d1f8670706a7a06`; map deployment/manifest ownership and duplicate/consumer surfaces |
| pheno-rt-spec-probe | local `main@5b043a1f`; 22 tracked files; `KooshaPari/phenotype-router-spec` origin returns 404 | HOLD as registry probe/evidence collection; canonical router protocol docs remain parent | semantic reconciliation for 8 of 9 divergent protocol/schema files; publish to a live owner or create an approved evidence collection |

The next-20 cohort is therefore evidence-complete at the current audit depth, but every
consolidation decision remains sponsor-gated after the listed ancestry, consumer, parity,
and ownership proofs are complete.

### Benchora and PhenoPlugins exact boundary refresh (2026-08-04)

| Repository | Exact source ref(s) | Structural/blob comparison | Current boundary decision | Required proof before any move |
|---|---|---|---|---|
| Benchora | local and `KooshaPari/Benchora:main` `5dff4367bc528c9590ecced0199d54de1728a39f`; target `phenotype-tooling:origin/main` `3b952d66267c06ec5a68e2c4b0a37ac6a59a4e47` | historical import `8e8f3a9` was replaced at `60cccce`; source has 112 paths/19 Rust modules versus 11 target-shelf paths, 3 common/0 blob-identical, and no consumers | KEEP standalone; HOLD absorption | reconcile historical migration/owner map, then prove consumer closure and focused source/target build-test parity; no attach, archive, or tombstone |
| PhenoPlugins | local `e57ee7985adabff9cd445557c2cc77ccf4be851f`; `origin/main` `feed4fcf0419d2adf23f2e5805aaa1e5243f3957` | 36 common paths (15 blob-identical, 21 divergent), plus 62 source-only paths; historical proposed target is unreachable | KEEP standalone; HOLD absorption | restore target provenance; prove five-crate hashes, APIs, builds, and consumer closure |

Benchora's legacy absorbed/deleted registry wording is contradicted by the live source
remote and the current target shelf. Neither row is a merge, archive, tombstone, or
pointer-retarget authorization.

### RepoLedger, asset-engine, and nanovms exact boundary refresh (2026-08-04)

| Repository | Exact evidence | Boundary conclusion |
|---|---|---|
| RepoLedger | clean `main@7dabedc39c584f67331722607ed5e7814f31c47d`, ahead 2/behind 54 of current `origin/main@f6b90b8e90b24e82c1ac415ca5b15815b696e76c`; `wip/preserve-20260804/repoledger-local-main-7dabedc` resolves to the local SHA; pnpm/Bun workspace has no registry or AgilePlus manifest/code edge | KEEP standalone/HOLD until source/remote divergence and actual consumer ownership are proven; the older 53-local-only metadata is stale, and the preservation ref is not a promotion or parent decision |
| asset-engine | clean `preserve/asset-engine-archive-20260729@41ade55dc10730d5718941cea1fb795f7c23365e`; archived `origin/main@e188dab9c9c5bba97383e3f9d3b71f6ab01b0150`; no Cargo/npm/Python/Go manifest; 48 source paths versus one shared, divergent README blob | KEEP standalone as an archived compatibility/provenance pointer; prove consumer repointing and reversible capture before any retirement packet; no attach, merge, archive mutation, or tombstone action is authorized |
| nanovms | local `main@9a0e286f3f2f1c24e500a8293775adc6bc9358e1`; `origin/main@84f24f122a11ba02c8950e35946dae46eebb7ebf`; 89 shared paths (70 blob-identical, 19 divergent) and 490 standalone-only paths | KEEP standalone integration boundary; no absorption. Map runtime/VMM consumers and reconcile the 19 divergent paths before any future boundary proposal |

Benchora remains KEEP standalone under the immediately preceding refresh; no cohort row
changes that conclusion.

## Exact source-capture refs (2026-08-03 refresh)

| Repository | Cloud ref and SHA | Parent/tree/diff SHA-256 | Boundary posture |
|---|---|---|---|
| ResearchLedger | `wip/preserve-20260803/researchledger-github-dirty-capture` -> `c501b0e66c591cb14737d6a8c356101d14a21000` | `7f4736f401fc225c0594ece59efe1f726df6ec03` / `76b907905358f70fc15695c249c2612cc1e5bcc8` / `83cf54eb26dd136ceb9a0ed813155d48904e325baa3ea2b95e856257c5289b7a` | preserve-only; current dirty source requires another capture |
| forgecode | `wip/preserve-20260803/forgecode-dirty-capture` -> `8ff6fcbe1d2e5490664ddc0a7d4fe126c1c1c56e`; installer alias `6d7ca1265d95fda230ddacf21c6206710d8a2b30` | `74464752a22e5d53138a821a186c2f78278f670f` / `a7bedd100d01c76ef99b7aa27aa2f041c45a774c` / `38510ad684888a82444061a8d4c062cd0049f09bf0e7cea93beb8f9695656c25` | preserve-only; follow-up source/docs deltas open |
| phenotype-tooling | `wip/preserve-20260803/phenotype-tooling-inbox-delta` -> `a24b0329f6249538094276e8f35b54388f54cf63` | `134d35599d76273c7d404e377834ab30db54c9f1` / `829c3d4258079a5033993a10005d31338fd05908` / `121411aacf00592bb198c56e49743577728da9e2741b7e8544361cb60415934b` | preserve-only; untracked worktree excluded |
| thegent | `wip/preserve-20260803/thegent-source-delta` -> `0e719cf15d4b8f618674acc4726bb7db8e86b0d8` | `d0f31a24d61e7abcd90cb077073f5444892396da` / `1bdf7688795bd372cf4ef04e98879dcacce3b018` / `6c4d3ba162911ba5e132d5f5c7a24f339abbee4e1fe8745262d0c246125854e3` | preserve-only; decomposition/source-test follow-up open |

The prior provenance discrepancy is resolved by named remote refs:
`ResearchLedger:wip/preserve-20260803/researchledger-github-source-delta` ->
`7c3a043f8245e206fc90c9bbf64c6220fdf32a72`, and
`KooshaPari/forgecode:wip/preserve-20260803/forgecode-source-delta` ->
`dd03d08584e839356743d5955ae27f398a62661d`.  Live registry `main` is
`3b3edc26864bc60878192828a186db04c37fed9d`; current protected PR gates are not
green across the fleet.  No move, merge, archive, or tombstone is authorized by
this inventory.

### ResearchLedger and PlayCua boundary refresh (2026-08-04)

| Surface | Exact evidence | Boundary posture and remaining gate |
|---|---|---|
| ResearchLedger | source-only chain `wip/preserve-20260804/researchledger-source-delta-20260804T0637` -> `8290fd5b285b966a765309a6a2bf075315f24b3a`; child `wip/preserve-20260804/researchledger-source-delta-20260804T0657` -> `80899613557d85c2ea57ef50ff015abe6dcb3531`; 18 code/test/docs/script paths total | preserve-only; data JSON, cross-encoder JSON fixture, and nested worktree excluded; dirty worktree intentionally retained; ownership/consumer proof remains required before any parent, archive, or tombstone decision |
| PlayCua | local `master@29c6c66e0f87b7567c9601f49c838dcbaa1337f0`; hosted canonical default `master@cda798f21552789cf51da7541619b1f708685c3d`; non-default `main@43d2e8d34bd8dd7e31c41adab1db71ad1c8d8574`; no manifest consumers; Eidolon bridge is trait-only | KEEP_STANDALONE/HOLD; hosted gates are failing. Treat `master`, not the competing `main`, as canonical until ownership evidence changes; prove a concrete transport implementation and target-workspace dependency closure before any boundary change |

### PhenoObservability exact boundary checkpoint (2026-08-04)

| Surface | Exact evidence | Boundary posture and remaining gate |
|---|---|---|
| PhenoObservability | canonical remote `git@github.com:KooshaPari/PhenoObservability.git`; clean local `wip/2026-07-22-phenoobservability-worklog@9192f73e7cc31831f83eba79a5d4f2dcda287c3a`; live `main@7f2e8d778615a0af6aafcdd4e247d541557a7c08`; R2 and bundle manifests are parity-verified | KEEP_STANDALONE/HOLD. Sponsor acknowledgement is missing; PR #209 is stale/diverged and strict branch protection remains in force. Reconcile the PR against live main, obtain sponsor acknowledgement, and prove consumers before any boundary change. This is preservation evidence only, not a promotion or retirement authorization. |

### AgilePlus plane capture inventory (2026-08-04)

| Repository | Canonical parent and source-only capture | Exact payload and integrity evidence | Boundary and promotion posture |
|---|---|---|---|
| AgilePlus | `main` parent `2fa631baa2a91e9df36b367d821bc47e6eb855a3`; first capture `47a9c174ed639fc27478686bae5a8115bda76063` at remote-verifiable `wip/preserve-20260804/agileplus-plane-delta-0843`; recapture `07ab99b9faedb62728faad803def66f1b3f29106` (parent `47a9c174ed639fc27478686bae5a8115bda76063`) at remote-verifiable `wip/preserve-20260804/agileplus-source-recapture-0925` | first capture: exactly `crates/agileplus-plane/src/daemon.rs` and `crates/agileplus-plane/src/lib.rs` (patch SHA-256 `35025280160380930915574876baa7f51fd08687c58b294861cc83b192af67fa`); recapture: exactly `crates/agileplus-plane/src/daemon.rs`, `crates/agileplus-dashboard/src/app_state.rs`, and `crates/agileplus-dashboard/src/routes/mod.rs`; original `main`, index, and worktree untouched | preserve-only. No merge, release, archive, or promotion authorization; retain the original local state for separate review. |

## Dogfood and release-gate audit (2026-08-05)

| Surface | Exact audited state | Remaining gate |
|---|---|---|
| AgilePlus | canonical `main@1d60137...` is clean/current. Branch protection requires strict `ci / lint` and `ci / test`, both queued in the audit. Current Sonar, tag, and benchmark checks fail. The installed `v0.2.1` release digest matches its release, but there is no artifact from current `main` and no recorded dogfood transcript. | Resolve strict and quality checks; build and verify a current-main artifact; capture installed end-to-end dogfood. Matching an older release digest is not current-main release proof. |
| Tracera | preserve `HEAD@d3a9d84...` diverges from `main@8e579f...`. Installed backend `0.1.3` passes loopback health and readiness. The frontend is absent, root returns `404`, and full E2E dogfood fails. App provenance is inferred only because the reported version hash is `dev`. | Retain the divergent preserve state; prove a frontend-bearing installed flow, complete full E2E dogfood, and establish explicit build provenance. Backend loopback health alone is not promotion evidence. |

These observations are additive, read-only gate facts only. They do not authorize a
merge, release, promotion, archive, tombstone, or boundary change.
