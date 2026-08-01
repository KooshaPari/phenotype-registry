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
| High | AgilePlus checked-in SQLite DB fails WAL pragma with disk I/O error | use isolated DB; retain existing dirty snapshot; do not delete DB files |
| High | Workspace has critically low free space | route heavy builds to isolated target/cache or heavy runner |
| Non-blocker | Tracera workspace-wide format check has pre-existing `tracera-cli` drift | keep focused fixture gate separate and record baseline debt |
| Blocker | AgilePlus governance validation currently finds 0/6 required CI/review evidence items | attach remote CI and review artifacts before implementing/validating the feature |
| Blocker | phenotype-registry Actions are enabled and PR #443 proves `ci / lint` and `ci / test`, but #441/#442 still need a post-#443 synchronization; #443 also exposes unrelated secret-guard drift in `compute-infra-auditors.yml` | Kilo review now passes on #443; obtain ordinary approval, merge through protected governance, then synchronize promotion PRs; keep unrelated action pinning separate |
| Baseline | PR #443 `docs:build` fails on pre-existing malformed Markdown at `docs/specs/pheno-specs/specs/platform/build-system/PRD.md:65:60` (`Element is missing end tag`) | repair the source Markdown in a separate docs-maintenance lane; do not widen the protected-check recovery PR |
| Blocker | PR #432 contains an unresolved `phenotype-omlx` gitlink at `a7118ed9...` with no live remote ref | split the preservation pointer or publish a verifiable immutable ref before any promotion |
| Blocker | PR #442's schema-review threads required consistent `source_artifact` ordering and replacement of the two remaining `source_archived` keys | head `33e0cdf` orders all six keys and removes the legacy names; Kilo review passes and all threads are resolved, but required contexts are absent, docs/secret-guard/trufflehog fail, and ordinary approval is still required |
| High | Current dirty/untracked payloads remain in Tracera (76), SessionLedger (23), pheno-harness (51), pheno (16), and sharecli (22 plus eight stashes) | preserve via isolated stash/bundle or recovery commits after excluding generated caches and secrets; current HEAD refs alone are not sufficient |
| Deferred | AgilePlus reactivation and any archive/delete action | sponsor gate only |
