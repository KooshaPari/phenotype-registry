# Current Estate Scorecard

Evidence timestamp: 2026-08-03 01:05 UTC. GitHub values take precedence over stale local tracking refs.

| Repo | Local HEAD/state | Authoritative remote evidence | Grade | Gate |
|---|---|---|---:|---|
| AgilePlus | `16da102a`; clean; local main ahead 3 after stash recovery | `main=06c5823fea5c`; dirty-state recovery ref `wip/preserve-20260801/agileplus-dirty-0605` at `16da102a`; isolated AgilePlus validation `0/6` | C+ | attach CI/review evidence before any promotion |
| OmniRoute | `fix/stray-brace-mitm-manager@03c6b8a`; source tree clean after auto-commit | source/config capture is cloud-visible at `03c6b8a`; provenance packet `omniroute-stash-packet-2247` -> `d8ab8ac`; six stash commits are preserved as `omniroute-stash-0..5` | C+ | classify stash payloads and conflict-marked history before any repair or merge |
| Tracera | `9be786f7d`; 76 dirty preserve files; preserve branch ahead 9 | `main=774c0061e886`; recovery `wip/preserve-20260801/tracera-dirty-capture-0955` -> `47ef7f41`; draft PR #771 | C+ | semantic audit recommends KEEP standalone; prove producer/consumer contracts; smoke/Vercel failures remain |
| phenotype-tooling | `5b854782`; 76 ahead stale local main; 2 dirty | `main=587805e38800`; #252 merged, branch 57 ahead/9 behind current main | C | classify post-merge branch |
| portage | `65e9ae47`; 2 dirty | `main=b35d00454fa8`; #495 dirty and required checks red | D | repair security/lint/type/test/verify |
| phenotype-registry | evidence checkpoint `5324a7b`; latest boundary ledger `1d2c15e`; clean preservation branch | `main=3b3edc26864b`; current open repair/cohort PRs include #444-#452; legacy #441/#442/#443/#432 remain historical lanes; Airlock `wip/20260803T0105-18c8261ae4b92228` | C+ | rebase repair work onto live main; do not attach stale-base refs |
| SessionLedger | `7b1c243e`; 19 tracked + 4 untracked entries (17 files); 99 local heads | `main=71a781ff3a97`; recovery `wip/preserve-20260801/sessionledger-dirty-capture-0902` -> `ec278e3c`; #391 behind with visual/e2e/provenance failures | D+ | preserve remaining generated/local payloads, then rebase/repair |
| pheno-harness | `fix/pheno-harness-runner-provenance@4131b7c`; 2 tracked + 52 untracked entries | source branch head `4131b7c`; recovery `wip/preserve-20260801/pheno-harness-dirty-capture-0902` -> `9fdef790`; exclusion manifest committed | C+ | preserve linked worktree separately, then evaluate harness/tooling boundary |
| forgecode | `preserve/workflow-schema-wave-20260729@4fe8aaf0`; 3 dirty source/docs files | recovery `wip/preserve-20260802/forgecode-dirty-capture` -> `ab49d70` on fork remote | C+ | compare captured update/packaging diff with current upstream before rebase or parent decision |
| thegent | `chore/thegent-governance-integration-wave@d0f31a`; one post-capture tracked delta; 5 stashes | post-capture `wip/preserve-20260802/thegent-postcapture` -> `b9ce6c1`; `thegent-stash-0..4` all exact remote refs | C+ | classify stash source/docs/generated payloads before any rebase or boundary action |
| sharecli | `fix/runtime-openapi-drift@7bafd605`; post-capture `AppState.swift` delta preserved | base recovery `wip/preserve-20260801/sharecli-dirty-capture-0955` -> `08ad5d10`; follow-up `wip/preserve-20260802/sharecli-postcapture-20260802T014647Z` -> `fd2a4eea` | C+ | KEEP Rust runtime canonical; thegent-sharecli archive-only; parity fixture still unrun |
| pheno | `main@a3c9dde`; 14 tracked + ~5,278 untracked entries | recovery `wip/preserve-20260801/pheno-dirty-capture-0955` -> `6140133`; follow-up `wip/preserve-20260802/pheno-source-manifest-capture` -> `ee890798`; all 151 nested Cargo manifests/locks plus the six-file metadata whitelist are now cloud-preserved; AgilePlus comparison finds 1,812/1,846 common paths byte-identical vs standalone `3b61d0d`; HexaKit comparison finds 3,209 common paths and no differing manifests/locks vs standalone `b47132a` | C+ | HOLD blanket absorption; review 34 AgilePlus divergences and four HexaKit metadata/docs differences before any parent or duplicate-shelf tombstone action |
| phenoAI | `a73ac4d`; 9 behind/5 ahead; 1 dirty | `main=751a8e77f854`; #69/#70 unstable | C- | stabilize CI/coverage |
| ResearchLedger | `main@0c207459`; 25 dirty source/docs entries | preservation `wip/preserve-20260802/researchledger-dirty-capture` -> `3b3facc`; original checkout remains dirty | C+ | compare against SessionLedger/phenoAI artifact ownership before any parent or archive decision |
| hfscope | `fix/preserve-search-kind@f119063`; one tracked source delta | preservation `wip/preserve-20260802/hfscope-dirty-capture` -> `865670b`; original checkout remains dirty | C+ | inspect observability/tooling consumers and API overlap before any parent decision |
| phenotype-omlx | `31cada2d`; 1 dirty; feature branch behind 29 | `main=c88431ad6004`; recovery ref `wip/preserve-20260801/phenotype-omlx/recovery--phenotype-omlx-local-20260726` at `8a1150f` | C+ | keep archive-only boundary; finish parity/provenance proof |

## Roll-up

- Preservation: active and recoverable for the lanes explicitly snapshotted in this session.
- Deduplication: DEDUPE-01..05 and existing contract records are present.
- Promotion: no estate-wide release claim; multiple hosted gates remain red or stale.
- Archive/tombstone: none performed; all actions remain sponsor-gated.
- AgilePlus governance: feature is specified/researched/planned in isolated DB, but validation is `0/6` evidence items until CI/review artifacts are attached.
- AgilePlus governance mirror is cloud-published at `ad2a1b0705dbadaa5a46af6d0307a2caebc6f84`; the ignored local DB remains supplemental evidence only.
- Registry governance packet is cloud-published through Airlock branch `wip/20260801T1045-18c7a89048cda260` at the latest scorecard snapshot.
- Pheno source completeness follow-up is cloud-published at `KooshaPari/pheno:wip/preserve-20260802/pheno-source-manifest-capture` -> `ee890798`; this closes the missing-manifest preservation gate only, not the boundary/parity gate.
- #432 pointer-only repair candidate is cloud-published at `wip/preserve-20260802/registry-omlx-pointer-repair` -> `a407839`; it replaces only the unresolved OMLX gitlink `a7118ed9...` with cloud-resolvable `52682309...` and remains unattached to the PR.
- Live-main repair integration is cloud-published at `wip/preserve-20260802/registry-repair-integration` -> `3b3edc2`; its diff against live `origin/main` is empty because all four repair contents are already present there; YAML and diff-scope checks pass.

## Promotion lanes

| PR | Head | Scope | Current disposition |
|---|---|---|---|
| #441 | `040eb7d` | pheno-errors reversible tombstone evidence | content-ready; required contexts absent; current docs-build and secret-guard fail; all four review threads are outdated/unresolved |
| #442 | `33e0cdf` | four-source provenance metadata and key normalization | ordering fix present; all review threads resolved; required contexts absent; docs-build fails at PRD.md:65:60; secret-guard flags a potential npm token in `registry/disposition-index.json` |
| #432 | `495d69b9` | broad absorption/OMLX preservation packet | hold/rework; pointer-only candidate `a407839` changes `a7118ed9...` to cloud-resolvable `52682309...`; current Kilo review fails and candidate is not attached |
| #443 | `fd898dc` | coverage workflow recovery trigger and protected check names | protected `ci / lint`, `ci / test`, and coverage are green; docs-build fails at README.md:81:47; secret-guard flags six unpinned workflow refs; merge state behind |

Repository Actions are enabled. PR #443 proves `coverage.yml` can emit `ci / lint`, `ci / test`, and coverage; #441 and #442 still require a post-#443 synchronization after the workflow repair is promoted.

Isolated repair refs (not merged): #441 docs `wip/preserve-20260802/registry-docs-pr441-angle-fix` -> `4160517`; #442 docs
`wip/preserve-20260802/registry-docs-pr442-angle-fix` -> `e25fc2`; #443 docs
`wip/preserve-20260802/registry-docs-pr443-angle-fix` -> `4dc7b5`; shared workflow
`wip/preserve-20260802/registry-workflow-action-pins` -> `a7c39fe`. All four are
diff-scope verified; the workflow YAML parses, but hosted checks and sponsor review
are still required before attachment or merge.

## 2026-08-03 hosted and boundary checkpoint

| Lane | Current evidence | Grade/gate |
|---|---|---|
| Registry provenance | local docs `HEAD=0a5eead1`; Airlock `wip/20260803T0019-18c8239a3080e110`; live `main=3b3edc2`; worktree clean | C+ / documentation preserved; no promotion claim |
| Hosted PR fleet | 13 open heads are `BEHIND` (#391, #392, #399, #432, #440, #441, #442, #443, #445, #446, #447, #449, #450, #451) and 5 are `DIRTY` (#393, #426, #427, #444, #452) | D / rebase, repair, and required checks remain open |
| Protected checks | branch protection requires strict `ci / lint` + `ci / test`; zero approvals; force-push and deletion disabled | HOLD / sponsor review plus green protected checks |
| pheno-rt-spec-probe | local `5b043a1f`; 404 origin; 8/9 protocol/schema files differ from registry absorbed copies | C- / preserve probe and reconcile semantics |
| phenotype-apps | local `5a067202`; active GitHub parent default `apps-extract`; recovery ref exact | C / KEEP standalone; stale registry retirement metadata needs reconciliation |
| phenotype-hub | local `667d77c`; archived remote disk usage 0, live remote HEAD `c7dd053e` | C- / archive-only provenance pointer; preserve local merge |
| Planify2 | local `e6b8e235`; original origin 404; exact preservation branch on Planify | C / Planify parent candidate; fork/site/infra proof pending |
| Next-20 boundaries | Benchora/PhenoPlugins/PlayCua HOLD; asset-engine/nanovms/RepoLedger KEEP standalone | C / consumer and ancestry evidence pending |

Cloud refs independently verified in this checkpoint: pheno source manifests
`ee890798`, forgecode recovery `ab49d70`, thegent post-capture `b9ce6c1`,
ResearchLedger `3b3facc`, phenotype-tooling plugin recovery `fd51689`, and current
phenotype-tooling inbox delta `a24b0329` (`wip/preserve-20260803/phenotype-tooling-inbox-delta`).
These are preservation proofs only; none authorizes merge, archive, or tombstone.

## Exact-ref refresh (2026-08-03 05:49-06:01 UTC)

| Lane | Current authoritative ref | Parent/tree/diff evidence | Status |
|---|---|---|---|
| ResearchLedger | `wip/preserve-20260803/researchledger-github-dirty-capture` -> `c501b0e66c591cb14737d6a8c356101d14a21000` | parent `7f4736f401fc225c0594ece59efe1f726df6ec03`; tree `76b907905358f70fc15695c249c2612cc1e5bcc8`; diff SHA-256 `83cf54eb26dd136ceb9a0ed813155d48904e325baa3ea2b95e856257c5289b7a` | C+ / preserve; current dirty source follow-up open |
| forgecode | `wip/preserve-20260803/forgecode-dirty-capture` -> `8ff6fcbe1d2e5490664ddc0a7d4fe126c1c1c56e`; installer alias `6d7ca1265d95fda230ddacf21c6206710d8a2b30` | parent `74464752a22e5d53138a821a186c2f78278f670f`; tree `a7bedd100d01c76ef99b7aa27aa2f041c45a774c`; diff SHA-256 `38510ad684888a82444061a8d4c062cd0049f09bf0e7cea93beb8f9695656c25` | C+ / preserve; seven-file dirty follow-up open |
| phenotype-tooling | `wip/preserve-20260803/phenotype-tooling-inbox-delta` -> `a24b0329f6249538094276e8f35b54388f54cf63` | parent `134d35599d76273c7d404e377834ab30db54c9f1`; tree `829c3d4258079a5033993a10005d31338fd05908`; diff SHA-256 `121411aacf00592bb198c56e49743577728da9e2741b7e8544361cb60415934b` | C+ / preserve; untracked worktree excluded |
| thegent | `wip/preserve-20260803/thegent-source-delta` -> `0e719cf15d4b8f618674acc4726bb7db8e86b0d8` | parent `d0f31a24d61e7abcd90cb077073f5444892396da`; tree `1bdf7688795bd372cf4ef04e98879dcacce3b018`; diff SHA-256 `6c4d3ba162911ba5e132d5f5c7a24f339abbee4e1fe8745262d0c246125854e3` | C+ / preserve; source/test decomposition follow-up open |

The formerly disputed source-delta commits are now cloud-verifiable and supersede
the earlier local-only discrepancy: ResearchLedger
`wip/preserve-20260803/researchledger-github-source-delta` ->
`7c3a043f8245e206fc90c9bbf64c6220fdf32a72`, and forgecode (fork remote)
`wip/preserve-20260803/forgecode-source-delta` ->
`dd03d08584e839356743d5955ae27f398a62661d`.  They are preservation evidence
only and do not authorize a merge, archive, or tombstone.  Live registry `main`
remains `3b3edc26864bc60878192828a186db04c37fed9d`.

### Fresh preservation refs (2026-08-03)

| Lane | Cloud-visible preservation evidence | Disposition |
|---|---|---|
| OmniRoute merge sweep | `wip/preserve-20260803/omniroute-main-dirty-20260803T105436` -> `e4c53857c07ac1994186ec24db459d39eb1fe8c5` | preserve-only; classify the 69 tracked modifications and two compression docs before repair or merge |
| OmniRoute native SQLite | `wip/preserve-20260803/pr481-native-sqlite-dirty-20260803T092433` -> `9a77beadf00961524f303b4a703558db03ea82d0` | preserve-only; retain separately from the merge-sweep payload |
| OmniRoute review fixes | `wip/preserve-20260803/pr481-review-fixes-dirty-202603T092433` -> `df070a3fbda9ac286d19a599d50244a348193058` | preserve-only; rate-limiter/test payload remains subject to current-main and hosted-gate review |
| thegent current helper delta | `wip/preserve-20260803/thegent-current-helper-delta` -> `7cda67f9597b0f9994f4f9a014c2586e23ea1da5` | preserve-only; parent `bc91aff123b80a9320c59a657846b09c45058531`; classify before rebase or boundary action |
| hfscope current baseline | `fix/preserve-search-kind` -> `f119063f2d8d` | clean current checkout; retain prior dirty capture `865670b` as independent provenance |

### ResearchLedger, RepoLedger, and PlayCua current checkpoint (2026-08-04)

| Surface | Exact evidence | Score and disposition |
|---|---|---|
| ResearchLedger | source-only `wip/preserve-20260804/researchledger-source-delta-20260804T0637` -> `8290fd5b285b966a765309a6a2bf075315f24b3a`; child `wip/preserve-20260804/researchledger-source-delta-20260804T0657` -> `80899613557d85c2ea57ef50ff015abe6dcb3531`; 18 code/test/docs/script paths | C+ / preserve-only. Data JSON, cross-encoder JSON fixture, and nested worktree were excluded; dirty worktree is intentionally retained. No parent/archive/tombstone action. |
| RepoLedger | local `main@7dabedc39c584f67331722607ed5e7814f31c47d`; current `origin/main@f6b90b8e90b24e82c1ac415ca5b15815b696e76c`; 2 ahead / 54 behind; preservation `wip/preserve-20260804/repoledger-local-main-7dabedc` -> local SHA | C / KEEP_STANDALONE/HOLD. The older `53 local-only commits` label is stale; no registry or AgilePlus manifest/code edge proves a parent. Reconcile divergence and actual consumer ownership before any boundary action. |
| PlayCua | local `master@29c6c66e0f87b7567c9601f49c838dcbaa1337f0`; hosted default `master@cda798f21552789cf51da7541619b1f708685c3d`; non-default `main@43d2e8d34bd8dd7e31c41adab1db71ad1c8d8574`; no manifest consumers; trait-only Eidolon bridge; hosted gates failing | C / KEEP_STANDALONE/HOLD. The competing `main` ref is not the canonical default. Require concrete transport implementation and target-workspace dependency closure before any boundary change. |

### Benchora and PhenoPlugins boundary evidence (2026-08-04)

| Source | Exact ref evidence | Overlap/blob evidence | Disposition and proof gap |
|---|---|---|---|
| Benchora | local and `KooshaPari/Benchora:main` both `5dff4367bc528c9590ecced0199d54de1728a39f`; target `phenotype-tooling:origin/main` `3b952d66267c06ec5a68e2c4b0a37ac6a59a4e47` | historical import `8e8f3a9` was replaced at `60cccce`; source has 112 paths/19 Rust modules versus 11 target-shelf paths, 3 common/0 identical blobs, and no consumers | KEEP standalone; legacy absorbed/deleted wording is contradicted. No archive, attach, or tombstone; require migration/owner map, consumer closure, and focused source/target build-test proof before any new parent decision. |
| PhenoPlugins | local `e57ee7985adabff9cd445557c2cc77ccf4be851f`; `KooshaPari/PhenoPlugins:main` `feed4fcf0419d2adf23f2e5805aaa1e5243f3957` | 36 common paths: 15 blob-identical and 21 divergent; 62 source-only paths; historical proposed target is unreachable | KEEP standalone; HOLD any absorption. Restore target provenance, then complete five-crate hash/API/build parity and consumer evidence. |

These are preserve-first boundary findings only. They do not authorize a parent
pointer change, merge, archive, or tombstone.

### asset-engine and nanovms boundary evidence (2026-08-04)

| Source | Exact ref evidence | Overlap/blob evidence | Disposition and proof gap |
|---|---|---|---|
| asset-engine | local `41ade55dc10730d5718941cea1fb795f7c23365e`; archived `KooshaPari/asset-engine:main` `e188dab9c9c5bba97383e3f9d3b71f6ab01b0150` | 48 source paths versus one shared README path; that README blob diverges | KEEP standalone as an archived compatibility/provenance pointer. Prove consumer repointing and reversible capture before any retirement packet. |
| nanovms | local `9a0e286f3f2f1c24e500a8293775adc6bc9358e1`; `KooshaPari/nanovms:main` `84f24f122a11ba02c8950e35946dae46eebb7ebf` | 89 shared paths: 70 blob-identical and 19 divergent; 490 standalone-only paths | KEEP standalone integration boundary; no absorption. Map runtime/VMM consumers and reconcile the 19 divergent paths before any future boundary proposal. |

These are preserve-first boundary findings only. They do not authorize a parent
pointer change, merge, archive, or tombstone.

### Current parent/gate blockers

- `ResilienceKit` gitlink `a50f52561ba95b656dcd8a612efa3fe3ff78ca11` in live main
  is contained by the canonical `KooshaPari/ResilienceKit` main/recovery lineage.
  Retain the existing gitlink; no pointer retarget is warranted.
- `phenotype-hub` gitlink `c93bc65f5beb55b1e62406996ebdc24a479071a1` has durable
  migrated-source provenance at
  `phenotype-apps:refs/sources/phenotype-hub/audit/ownership-20260722-phenotype-hub`
  -> `c93bc65f5beb55b1e62406996ebdc24a479071a1`.  Retain the existing gitlink; no
  pointer retarget is warranted.
- `phenotype-omlx` gitlink `8eb9891653e00a5dde986e60be3e84bfbf81d943` is not on
  hosted refs; hosted `main=302321a33812ef0c40bf3f3cb934e23b6ef7008e`, and
  `52682309e2576574739fc97b1b937af1d570ef43` is a separate candidate on
  `fix/ffi-turbo-quant-validation`/PR #82.
- Protected registry contexts remain strict `ci / lint` and `ci / test`; the open
  PR fleet is not promotion-ready (`BEHIND` and `DIRTY` states with failed checks).
  No merge, archive, or tombstone is authorized by this scorecard.
- Luna validation: `~/.codex/agents/luna-worker.toml` exists unchanged; installed
  `codex-cli 0.146.0` accepted the `gpt-5.6-luna` availability probe, which returned
  exactly `LUNA_MODEL_PROBE_OK`. `codex exec --help` still documents no agent-file
  selector (while `--strict-config` applies to `config.toml`). Attempts to run a
  full bounded audit inherited stdin, hung at `Reading additional input from stdin...`,
  and were terminated. Therefore this records model availability only, not a Luna
  worker/audit execution claim.

### PR #458 security-gate checkpoint

PR #458 is `DRAFT` and open against `main=3b3edc26864bc60878192828a186db04c37fed9d`
at head `5ac89db16311c80006067d975882a05fe01167a2`. Its required `ci / lint` and
`ci / test` checks passed, but the TruffleHog security check remains failed: run
`30794174416` (job `91623908467`) verified one `SentryToken` finding, left nine
additional findings unverified, and exited `183`. No merge or bypass was performed.
The minimum safe action is non-destructive remediation of the reported
security-gate scope, followed by a fresh full-history run on the same or a
current-main-reconciled head; do not infer readiness from partial verification.

### PhenoObservability current boundary checkpoint (2026-08-04)

| Surface | Exact evidence | Score and disposition |
|---|---|---|
| PhenoObservability | canonical remote `git@github.com:KooshaPari/PhenoObservability.git`; clean local `wip/2026-07-22-phenoobservability-worklog@9192f73e7cc31831f83eba79a5d4f2dcda287c3a`; live `main@7f2e8d778615a0af6aafcdd4e247d541557a7c08`; R2 and bundle manifests are parity-verified; PR #209 is stale/diverged under strict protection | C / KEEP_STANDALONE/HOLD. Sponsor acknowledgement and hosted consumer proof are missing. Reconcile PR #209 to live main and obtain the sponsor gate before any boundary action; this preserve-only evidence authorizes neither promotion nor retirement. |

### AgilePlus plane source capture (2026-08-04)

| Surface | Exact capture evidence | Disposition |
|---|---|---|
| AgilePlus plane delta | canonical `main` parent `2fa631baa2a91e9df36b367d821bc47e6eb855a3`; first source-only capture `47a9c174ed639fc27478686bae5a8115bda76063` on `wip/preserve-20260804/agileplus-plane-delta-0843` captured exactly `crates/agileplus-plane/src/daemon.rs` and `crates/agileplus-plane/src/lib.rs` (patch SHA-256 `35025280160380930915574876baa7f51fd08687c58b294861cc83b192af67fa`); recapture `07ab99b9faedb62728faad803def66f1b3f29106` has parent `47a9c174ed639fc27478686bae5a8115bda76063` on `wip/preserve-20260804/agileplus-source-recapture-0925` and captures exactly `crates/agileplus-plane/src/daemon.rs`, `crates/agileplus-dashboard/src/app_state.rs`, and `crates/agileplus-dashboard/src/routes/mod.rs` | C+ / preserve-only. The original AgilePlus `main`, index, and worktree remain untouched; neither capture authorizes merge, release, archive, or other promotion. |

### Dogfood gate refresh (2026-08-05)

| Surface | Exact current evidence | Grade/gate |
|---|---|---|
| AgilePlus | canonical `main@1d60137...` is clean/current. Strict required `ci / lint` and `ci / test` are queued; the current Sonar, tag, and benchmark checks fail. Installed `v0.2.1` release digest matches, but no artifact built from current `main` or dogfood transcript is recorded. | HOLD / no promotion or release claim until the strict checks and quality failures are resolved, a current-main artifact is verified, and dogfood evidence is captured. |
| Tracera | preserve `HEAD@d3a9d84...` diverges from `main@8e579f...`. Installed backend `0.1.3` passes loopback `/health` and `/ready`; frontend is absent, root returns `404`, and full E2E dogfood fails. Application provenance is inferred only because the version hash is `dev`. | HOLD / preserve divergence; backend-only loopback success is insufficient. Restore/verify frontend and full E2E, then establish non-inferred app provenance before any promotion claim. |

This is read-only gate evidence. It authorizes no merge, release, promotion, archive,
tombstone, or boundary change.
