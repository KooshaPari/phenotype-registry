# Known Issues

| Severity | Issue | Mitigation |
|---|---|---|
| Blocker | Several lanes have dirty/local-only payloads not yet reconciled to live remote refs | preserve and publish exact refs before promotion |
| Blocker | Tracera draft PR #771 has failing runtime smoke and Vercel checks | inspect exact failing logs; do not merge on local fixture evidence alone |
| Baseline | PR #771 hosted failures currently resolve to frontend `@tracertm/web` build exit, missing `trunk-action` revision, and pre-existing `tracera-cli` formatting drift; no failure points at the two candidate files | keep PR draft; repair or quarantine baseline gates before promotion |
| Blocker | OmniRoute, portage, SessionLedger, phenoAI, and registry PR gates are failing or behind | repair only after current-main reconciliation |
| Blocker | thegent-sharecli is archived/read-only | request unarchive; do not create an alternate repo |
| High | sharecli and thegent-sharecli overlap vocabulary but not implementation/provenance; registry boundary docs disagree on absorption | keep Rust sharecli canonical, preserve archived Python lineage, run the parity fixture and reconcile docs before any extraction/archive |
| High | Tracera and Grapheon share lineage and route vocabulary while diverging in APIs/history; Tracera consumes PhenoObservability metadata rather than implementing its substrate | keep both preserved and standalone; complete API/DB/consumer/lineage diff before any archive or merge |
| Blocker | pheno recovery `6140133` omitted all nested AgilePlus Cargo manifests/locks and about 63 other source-bearing manifests due ignore rules | force-add manifests/specs/configs in a new recovery ref; retain generated/runtime exclusions; do not treat the current ref as build-complete |
| High | pheno nested AgilePlus is mostly path-identical to standalone AgilePlus, while HexaKit has 14 overlapping crate names with divergent APIs and unique bootstrap/template APIs | keep AgilePlus and HexaKit standalone; review crate-level parity and source SHA before any absorption or tombstone |
| High | AgilePlus checked-in SQLite DB fails WAL pragma with disk I/O error | use isolated DB; retain existing dirty snapshot; do not delete DB files |
| High | Workspace has critically low free space | route heavy builds to isolated target/cache or heavy runner |
| Non-blocker | Tracera workspace-wide format check has pre-existing `tracera-cli` drift | keep focused fixture gate separate and record baseline debt |
| Blocker | AgilePlus governance validation currently finds 0/6 required CI/review evidence items | attach remote CI and review artifacts before implementing/validating the feature |
| Blocker | phenotype-registry Actions are enabled and PR #443 proves `ci / lint`, `ci / test`, and coverage, but #441/#442 still lack required contexts | repair #443 blockers, then synchronize promotion PRs; branch protection currently requires no approving review but does require strict CI contexts |
| Baseline | PR #443 `docs:build` fails VitePress parsing at `docs/absorption/pheno-runtime-config/README.md:81:47` (`Element is missing end tag`) | repair the source Markdown in a separate docs-maintenance lane; do not widen the workflow trigger change |
| Blocker | PR #443 secret guard rejects unpinned actions in `.github/workflows/compute-infra-auditors.yml` at lines 77, 90, 99, 106, 113, and 127 | pin those action refs in a separate security lane or explicitly scope the repair; current trufflehog passes |
| Baseline | PR #441 `docs:build` fails at `docs/specs/pheno-specs/specs/platform/003-agileplus-platform-completion/data-model.md:61:11`; PR #442 fails at `docs/specs/pheno-specs/specs/platform/build-system/PRD.md:65:60` | repair each malformed Markdown source in a docs-only lane; do not widen provenance/tombstone changes |
| Blocker | PR #432 contains an unresolved `phenotype-omlx` gitlink at `a7118ed9...` with no live remote ref | split the preservation pointer or publish a verifiable immutable ref before any promotion |
| Blocker | PR #442's schema-review threads required consistent `source_artifact` ordering and replacement of the two remaining `source_archived` keys | head `33e0cdf` orders all six keys and removes the legacy names; Kilo review passes and all threads are resolved, but required contexts are absent and docs/secret-guard fail |
| High | Current dirty/untracked payloads remain in Tracera (76), SessionLedger (23), pheno-harness (51), pheno (16), and sharecli (22 plus eight stashes) | preserve via isolated stash/bundle or recovery commits after excluding generated caches and secrets; current HEAD refs alone are not sufficient |
| High | sharecli changed again after capture (`desktop/ShareCLITray/Sources/ShareCLICore/AppState.swift`); SessionLedger retains generated `mutants.out*` reports | take a second source-only sharecli capture before cleanup; keep mutation output excluded unless a dedicated evidence packet is requested |
| Info | ShareCLI post-capture source-only ref is published at `wip/preserve-20260802/sharecli-postcapture-20260802T014647Z` (`fd2a4eea`) | retain all eight stash refs; parity fixture and sponsor boundary decision remain open |
| Info | Four isolated registry repair refs are diff-scope verified; none is attached to an open PR yet | run hosted checks, then require sponsor/HITL selection before any PR update or merge |
| Deferred | AgilePlus reactivation and any archive/delete action | sponsor gate only |
| High | GitHub Dependabot reports one open high-severity `postcss` advisory on the default branch (alert 1) | create a separate dependency-security remediation lane; do not conflate it with registry boundary promotion |
