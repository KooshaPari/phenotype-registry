# Known Issues

| Severity | Issue | Mitigation |
|---|---|---|
| Blocker | Several lanes have dirty/local-only payloads not yet reconciled to live remote refs | preserve and publish exact refs before promotion |
| Blocker | phenotype-registry `main` advanced from `834c721f` to `3b3edc2`; previously published repair refs were stale-base, while open PRs #444-#452 are current hosted state | live-main integration `wip/preserve-20260802/registry-repair-integration` -> `3b3edc2` is verified clean; preserve old refs but do not attach them directly |
| High | OmniRoute source/config payload is now cloud-preserved at `03c6b8a`; provenance packet `omniroute-stash-packet-2247` -> `d8ab8ac` and six raw stash refs preserve (`52d146b99b`, `2923b3bf79`, `d069e70835`, `e94b073bb1`, `3d2e1281de`, `5039bddc25`) | classify each stash's source/docs/generated content and conflict markers before any repair or merge; never drop or rewrite the original stash stack |
| High | forgecode's three dirty source/docs files are preserved at `wip/preserve-20260802/forgecode-dirty-capture` -> `ab49d70`; pheno-harness retains only a generated benchmark checksum delta; thegent post-capture source delta is preserved at `b9ce6c1` and five stashes at `thegent-stash-0..4` | classify forgecode/thegent source-vs-generated payloads and verify pheno-harness checksum provenance before any rebase or boundary decision |
| High | thegent stash #1 (`116a774b...`) contains a 2,411-line `phench/service.py` collapse plus new modules up to 675 lines and a UX test change | preserve the source/test/untracked module set atomically, then decompose or explicitly document file-size exceptions before any merge |
| Blocker | Tracera draft PR #771 has failing runtime smoke and Vercel checks | inspect exact failing logs; do not merge on local fixture evidence alone |
| Baseline | PR #771 hosted failures currently resolve to frontend `@tracertm/web` build exit, missing `trunk-action` revision, and pre-existing `tracera-cli` formatting drift; no failure points at the two candidate files | keep PR draft; repair or quarantine baseline gates before promotion |
| Blocker | OmniRoute, portage, SessionLedger, phenoAI, and registry PR gates are failing or behind | repair only after current-main reconciliation |
| Blocker | thegent-sharecli is archived/read-only | request unarchive; do not create an alternate repo |
| High | sharecli and thegent-sharecli overlap vocabulary but not implementation/provenance; registry boundary docs disagree on absorption | keep Rust sharecli canonical, preserve archived Python lineage, run the parity fixture and reconcile docs before any extraction/archive |
| High | Tracera and Grapheon share lineage and route vocabulary while diverging in APIs/history; Tracera consumes PhenoObservability metadata rather than implementing its substrate | keep both preserved and standalone; complete API/DB/consumer/lineage diff before any archive or merge |
| High | pheno recovery `6140133` omitted 119 of 151 nested Cargo manifests/locks plus a small ignored source-metadata whitelist; follow-up `wip/preserve-20260802/pheno-source-manifest-capture` -> `ee890798` now preserves all 151 and the six whitelist files | compare API/dependency/test parity per overlapping AgilePlus and HexaKit crate before any build, parent, merge, archive, or tombstone claim |
| High | Pheno nested AgilePlus ref `ee890798` versus standalone AgilePlus `main@3b61d0d` has 1,846 common paths: 1,812 byte-identical and 34 divergent, with 26 nested-only and 1,129 standalone-only paths; current HexaKit comparison is nearly path-identical to standalone `main@b47132a` (3,209 common paths, four metadata/docs divergences, no differing Cargo manifests/locks) | keep standalone AgilePlus and HexaKit as canonical parents; review the 34 AgilePlus divergences and the four HexaKit metadata/docs differences before any duplicate-shelf tombstone or absorption action |
| High | Agentora local checkout is 10 commits behind origin and has a `.trunk/trunk.yaml` conflict plus generated `.trunk` tool state | preserve only source-bearing Agentora changes if found; exclude `.trunk` runtime/tool output and defer parent decision until current-main reconciliation |
| Info | Grapheon recovery checkout is clean at `523b67d` but its registry boundary evidence is stale relative to current Tracera | retain standalone; refresh route/store/consumer lineage before any parent or archive decision |
| Info | Planify2's original GitHub `origin` returns repository-not-found, but clean `main@e6b8e235` is now preserved on `KooshaPari/Planify:wip/preserve-20260802/planify2-local-main` | keep the branch preservation-only; obtain sponsor direction before any parent merge, archive, or new-repo creation |
| High | ResearchLedger has 25 dirty source/docs entries and hfscope has one tracked source delta; neither had a cloud recovery ref at the prior inventory cut | preserve source-bearing changes in isolated refs, then compare consumers and API ownership against SessionLedger, phenoAI, and observability parents |
| High | AgilePlus checked-in SQLite DB fails WAL pragma with disk I/O error | use isolated DB; retain existing dirty snapshot; do not delete DB files |
| High | Workspace has critically low free space | route heavy builds to isolated target/cache or heavy runner |
| Non-blocker | Tracera workspace-wide format check has pre-existing `tracera-cli` drift | keep focused fixture gate separate and record baseline debt |
| Blocker | AgilePlus governance validation currently finds 0/6 required CI/review evidence items | attach remote CI and review artifacts before implementing/validating the feature |
| Blocker | phenotype-registry PRs #441/#442/#443 are behind; current docs-build and secret-guard fail on all three, and #432 Kilo review fails | repair and rerun isolated docs/security lanes, then synchronize promotion PRs; branch protection requires strict `ci / lint` and `ci / test` contexts but no approving review |
| Blocker | Current repair queue still targets stale base `052c5ef`: #442 and #451 are exact duplicates, #445 is a strict subset, #443/#447 are already integrated, #444 is functionally present with additional main hardening, #452 is superseded, and #446 overlaps pointer-sensitive #432 | preserve exact PR refs/metadata; do not cherry-pick or update PRs until sponsor disposition, additive rebase, and hosted checks are available; unique candidates remain #441, #449, and #450 |
| Baseline | PR #443 `docs:build` fails VitePress parsing at `docs/absorption/pheno-runtime-config/README.md:81:47` (`Element is missing end tag`) | repair the source Markdown in a separate docs-maintenance lane; do not widen the workflow trigger change |
| Blocker | PR #443 secret guard rejects unpinned actions in `.github/workflows/compute-infra-auditors.yml` at lines 77, 90, 99, 106, 113, and 127 | pin those action refs in a separate security lane or explicitly scope the repair |
| Baseline | PR #441 `docs:build` fails at `docs/specs/pheno-specs/specs/platform/003-agileplus-platform-completion/data-model.md:61:11`; PR #442 fails at `docs/specs/pheno-specs/specs/platform/build-system/PRD.md:65:60` | repair each malformed Markdown source in a docs-only lane; do not widen provenance/tombstone changes |
| Blocker | PR #432 originally contained an unresolved `phenotype-omlx` gitlink at `a7118ed9...` with no live remote ref | pointer-only candidate `wip/preserve-20260802/registry-omlx-pointer-repair` -> `a407839` now targets cloud-resolvable `52682309...`; sponsor must choose whether to attach it after Kilo review and protected checks are repaired |
| Blocker | Current registry index still points `phenotype-omlx` at `60243d0019930cae2508ee01030a6d55d5e4d6cb`, which is not reachable from the hosted phenotype-omlx remote; the nested checkout is clean locally but its preservation branch is not at the same remote tip | retain the exact local/Airlock refs; keep pointer candidate `a407839` unattached until sponsor selection, ancestry/tree proof, and protected hosted checks are complete; its comparison to live `main=3b3edc2` is a broad stale-base diff, not an attachable one-file promotion |
| Blocker | PR #442's schema-review threads required consistent `source_artifact` ordering and replacement of the two remaining `source_archived` keys | head `33e0cdf` orders all six keys and removes the legacy names; all threads are resolved, but required contexts are absent and current docs/secret-guard/trufflehog evidence is not green |
| High | Current dirty/untracked payloads remain in Tracera (76), SessionLedger (23), pheno-harness (51), pheno (16), and sharecli (22 plus eight stashes) | preserve via isolated stash/bundle or recovery commits after excluding generated caches and secrets; current HEAD refs alone are not sufficient |
| High | sharecli changed again after capture (`desktop/ShareCLITray/Sources/ShareCLICore/AppState.swift`); SessionLedger retains generated `mutants.out*` reports | take a second source-only sharecli capture before cleanup; keep mutation output excluded unless a dedicated evidence packet is requested |
| Info | ShareCLI post-capture source-only ref is published at `wip/preserve-20260802/sharecli-postcapture-20260802T014647Z` (`fd2a4eea`) | retain all eight stash refs; parity fixture and sponsor boundary decision remain open |
| Info | Four isolated registry repair refs are diff-scope verified; none is attached to an open PR yet | run hosted checks, then require sponsor/HITL selection before any PR update or merge |
| Deferred | AgilePlus reactivation and any archive/delete action | sponsor gate only |
| High | GitHub Dependabot reports one open high-severity `postcss` advisory on the default branch (alert 1) | create a separate dependency-security remediation lane; do not conflate it with registry boundary promotion |

## 2026-08-03 capture and hosted-gate checkpoint

This is an additive evidence refresh. No merge, archive, tombstone, delete, reset,
or force-push was performed.

| Severity | Current evidence | Required follow-up |
|---|---|---|
| Blocker | phenotype-registry live `main=3b3edc26864b`; required contexts remain strict `ci / lint` and `ci / test`, with zero required approvals and force-push/deletion disabled | keep all stale/dirty PR heads unattached until additive rebase and protected hosted checks are green |
| High | #391/#392/#399/#432/#440/#441/#442/#443/#445/#446/#447/#449/#450/#451 are `BEHIND`; #393/#426/#427/#444/#452 are `DIRTY` | refresh each candidate from live main only in isolated branches; sponsor selects promotion order |
| High | #441 has `docs:build` and `secret-guard` failures; #442 has `docs:build`, `secret-guard`, and `trufflehog` failures; #443 has `docs:build`, `secret-guard`, and `trufflehog` failures; #432 Kilo review fails; #391 has `secret-guard` and `regen-ecosystem-map` failures | repair one gate family at a time; do not infer merge readiness from non-required green checks |
| High | `pheno-rt-spec-probe` local `main@5b043a1f` points to 404 `phenotype-router-spec`; registry absorbed copies are not byte-identical on 8/9 protocol/schema files | preserve the local probe under registry evidence and perform semantic diff before replacing canonical docs |
| High | `phenotype-apps` local `main@5a067202` has no configured remote, while active GitHub `phenotype-apps` uses default `apps-extract`; exact recovery ref `recovery/phenotype-apps-local-20260726` already exists | reconcile stale registry retirement wording with active-repo metadata; keep app-plane standalone |
| High | `phenotype-hub` local `main@667d77c` diverges from archived remote HEAD `c7dd053e`; local branch carries unpushed merge work | preserve local commits and redirect provenance; do not delete or re-archive the already archived source |
| High | `Planify2` original origin is 404; local `e6b8e235` is preserved at `KooshaPari/Planify:wip/preserve-20260802/planify2-local-main` | prove fork ancestry and unique `site/`/`infra/` ownership before any Planify extraction or archive action |
| High | forgecode current checkout still has the three captured source/docs deltas and a newer `install.sh` delta beyond recovery `ab49d70` | take a follow-up source-only capture for the new installer delta before rebase or parent decision |
| High | thegent current checkout advanced to `0e719cf`; five historical stashes remain, including stash #1's 2,411-line `phench/service.py` decomposition plus UX test and six new modules; post-capture ref remains `b9ce6c1` | preserve the current head and classify stash #1 atomically before any merge or boundary action |
| High | ResearchLedger retains 25 dirty source/docs entries and two new Rust modules; recovery ref `3b3facc` is cloud-published | compare artifact ownership with SessionLedger/phenoAI before parent selection |
| High | phenotype-tooling remains 82 commits ahead of hosted main with tracked `elicitate` source delta and an untracked worktree; recovery ref `fd51689` covers the prior plugin lane | preserve the current source/worktree separately; exclude generated worktree state from promotion |
| High | pheno-harness current dirty entry is generated `bench/results/sota/2026-08-02/snapshot.sha256`; source recovery `9fdef790` exists | retain checksum as generated evidence only and verify source recovery before any boundary claim |
| Info | Next-20 audit classified Benchora/PhenoPlugins/PlayCua as HOLD, asset-engine/nanovms/RepoLedger as KEEP standalone | complete consumer/ancestry/hash proof before proposing a parent or archive packet |

The phenotype-tooling inbox source delta is now additionally preserved at
`wip/preserve-20260803/phenotype-tooling-inbox-delta` -> `a24b0329`; the earlier
`fd51689` recovery remains immutable historical provenance.

## 2026-08-03 exact-ref and boundary-gate refresh (05:49-06:01 UTC)

Fresh remote checks now verify the formerly missing source-delta objects:
ResearchLedger `7c3a043f8245e206fc90c9bbf64c6220fdf32a72` on
`wip/preserve-20260803/researchledger-github-source-delta`, and forgecode
`dd03d08584e839356743d5955ae27f398a62661d` on the fork ref
`wip/preserve-20260803/forgecode-source-delta`.  The discrepancy is closed;
both refs remain preserve-only.  Current source captures are
`c501b0e66c591cb14737d6a8c356101d14a21000` (ResearchLedger),
`8ff6fcbe1d2e5490664ddc0a7d4fe126c1c1c56e` plus installer alias
`6d7ca1265d95fda230ddacf21c6206710d8a2b30` (forgecode),
`a24b0329f6249538094276e8f35b54388f54cf63` (phenotype-tooling), and
`0e719cf15d4b8f618674acc4726bb7db8e86b0d8` (thegent).

| Severity | New evidence | Required follow-up |
|---|---|---|
| Blocker | live registry `main=3b3edc26864bc60878192828a186db04c37fed9d`; PR fleet contains `BEHIND` and `DIRTY` heads, while protected `ci / lint` and `ci / test` are not green across candidates | sponsor selects one additive rebase lane; do not attach or merge stale heads |
| Resolved provenance | live registry tree points `registry/absorbed-crates/ResilienceKit` to gitlink `a50f52561ba95b656dcd8a612efa3fe3ff78ca11`, contained by the canonical `KooshaPari/ResilienceKit` main/recovery lineage | retain the existing gitlink; no pointer retarget is warranted |
| Resolved provenance | live registry tree points `registry/absorbed-crates/phenotype-hub` to `c93bc65f5beb55b1e62406996ebdc24a479071a1`, durably represented by `phenotype-apps:refs/sources/phenotype-hub/audit/ownership-20260722-phenotype-hub` -> the same SHA | retain the existing gitlink; no pointer retarget is warranted |
| Blocker | live registry tree points `registry/absorbed-crates/phenotype-omlx` to `8eb9891653e00a5dde986e60be3e84bfbf81d943`, absent from hosted refs; hosted OMLX `main=302321a33812ef0c40bf3f3cb934e23b6ef7008e`, while cloud candidate `52682309e2576574739fc97b1b937af1d570ef43` is on `fix/ffi-turbo-quant-validation` and PR #82 | keep the pointer-repair candidate unattached until sponsor selection, ancestry/tree proof, Kilo review, and protected checks |
| High | ResearchLedger current checkout still has four tracked source/script deltas plus an untracked `worktrees/` directory; forgecode has seven tracked deltas after the installer capture; thegent has source/test decomposition payloads beyond `0e719cf` | take source-only follow-up captures, excluding generated/worktree state, before any rebase or boundary choice |
| High | PR #441/#442/#443/#445/#446/#447/#449/#450/#451 are behind; #380/#386/#387/#388/#389/#393/#426/#427/#444/#452 are dirty; multiple candidate checks report failures | repair one gate family at a time and require current-main SHA, strict required checks, and review receipt |
