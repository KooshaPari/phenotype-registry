# Current Estate Scorecard

Evidence timestamp: 2026-08-02 22:19 UTC. GitHub values take precedence over stale local tracking refs.

| Repo | Local HEAD/state | Authoritative remote evidence | Grade | Gate |
|---|---|---|---:|---|
| AgilePlus | `16da102a`; clean; local main ahead 3 after stash recovery | `main=06c5823fea5c`; dirty-state recovery ref `wip/preserve-20260801/agileplus-dirty-0605` at `16da102a`; isolated AgilePlus validation `0/6` | C+ | attach CI/review evidence before any promotion |
| OmniRoute | `fix/stray-brace-mitm-manager@03c6b8a`; source tree clean after auto-commit | source/config capture is cloud-visible at `03c6b8a`; provenance packet `omniroute-stash-packet-2247` -> `d8ab8ac`; six stash commits are preserved as `omniroute-stash-0..5` | C+ | classify stash payloads and conflict-marked history before any repair or merge |
| Tracera | `9be786f7d`; 76 dirty preserve files; preserve branch ahead 9 | `main=774c0061e886`; recovery `wip/preserve-20260801/tracera-dirty-capture-0955` -> `47ef7f41`; draft PR #771 | C+ | semantic audit recommends KEEP standalone; prove producer/consumer contracts; smoke/Vercel failures remain |
| phenotype-tooling | `5b854782`; 76 ahead stale local main; 2 dirty | `main=587805e38800`; #252 merged, branch 57 ahead/9 behind current main | C | classify post-merge branch |
| portage | `65e9ae47`; 2 dirty | `main=b35d00454fa8`; #495 dirty and required checks red | D | repair security/lint/type/test/verify |
| phenotype-registry | evidence checkpoint `5324a7b`; latest docs wrapper `c7475c1`; clean preservation branch | `main=3b3edc26864b`; current open repair/cohort PRs include #444-#452; legacy #441/#442/#443/#432 remain historical lanes; Airlock through `wip/20260802T2219-18c81d07e3762120` | C+ | rebase repair work onto live main; do not attach stale-base refs |
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
