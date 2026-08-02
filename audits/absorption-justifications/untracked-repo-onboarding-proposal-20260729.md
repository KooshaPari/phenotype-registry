# untracked-repo-onboarding-proposal-20260729

Generated: 2026-07-29T21:39:16Z UTC

Context: 13 local repos not linked by `path/full_name` to existing phenotype-registry records after improved matching.

## Proposal set (local-only evidence, unscheduled)

|repo|remote_full_name|local_branch|local_worktree_state|remote_size|remote_url|recommended_action|
|---|---|---|---|---:|---|---|
|Planify2|KooshaPari/Planify2|feat/dual-harness-fixture-path-fix|clean|3|https://github.com/KooshaPari/Planify2.git|review_alias_or_canonical_merge|
|shared|KooshaPari/phenotype-shared|main|clean|310|git@github.com:KooshaPari/phenotype-shared.git|queue_as_ABSORB|
|PhenoPlugins|KooshaPari/PhenoPlugins|main|clean|627|https://github.com/KooshaPari/PhenoPlugins.git|queue_as_ABSORB|
|phenotype-journeys|KooshaPari/phenotype-journeys|main|clean|1080|https://github.com/KooshaPari/phenotype-journeys.git|queue_as_ABSORB|
|phenotype-python-sdk|KooshaPari/phenotype-python-sdk|main|clean|5884|https://github.com/KooshaPari/phenotype-python-sdk.git|queue_as_ABSORB|
|pheno-harness|KooshaPari/pheno-harness|main|dirty|6333|git@github.com:KooshaPari/pheno-harness.git|review_alias_or_canonical_merge|
|PhenoObservability|KooshaPari/PhenoObservability|wip/2026-07-22-phenoobservability-worklog|clean|8494|https://github.com/KooshaPari/PhenoObservability.git|queue_as_ABSORB|
|CivicSurvival-public|KooshaPari/CivicSurvival-public|main|clean|34177|git@github.com:KooshaPari/CivicSurvival-public.git|queue_as_ABSORB|
|airlock|KooshaPari/airlock|main|clean|68670|https://github.com/KooshaPari/airlock|preserve_boundary_root|
|phenotype-registry|KooshaPari/phenotype-registry|chore/preserve-omlx-ffi-validation|dirty|93559|git@github.com:KooshaPari/phenotype-registry.git|preserve_boundary_root|
|Civis|KooshaPari/Civis|wip/2026-07-22-civis-quality-manifest|clean|1675291|git@github.com:KooshaPari/Civis.git|review_alias_or_canonical_merge|
|pheno-rt-spec-probe|KooshaPari/phenotype-router-spec|main|clean|API_FAIL|https://github.com/KooshaPari/phenotype-router-spec.git|archive_as_BOUNDARY_DONE|
|phenoAI|-|fix/phenoai-codeql-workflow-schema|clean|-|/Users/kooshapari/.airlock/repos/64f03a81ecb2.git|queue_as_ABSORB|

## Cohort 22 dispositions (verified local evidence, unscheduled)

|repo|verified local state|canonical purpose|disposition|rationale and next gate|
|---|---|---|---|---|
|RepoLedger|clean; `main` behind `origin/main` by 4|React/Vite ecosystem console with a Go websocket server|retain_independent; evaluate integration branch|A product-facing topology console complements registry governance rather than duplicating it. Fast-forward the clean checkout, then verify its data contract before proposing an adapter branch.|
|ResearchLedger|clean; `main` synchronized with `origin/main`|Tauri local-first research ledger with Markdown/SQLite provenance, import, search, RAG, and export|retain_independent|Its local research-vault and citation domain is complementary to registry evidence. No absorption or retirement action is justified.|
|Benchora|clean feature branch `feat/cross-repo-audit-fixes` tracking origin|Published Rust benchmarking and xDD testing toolkit with Criterion, SQLite baselines, mutation coverage, and CLI|retain_independent; preserve active branch|A standalone reusable developer tool, not a registry boundary duplicate. Preserve the feature branch and evaluate downstream crate consumption through an explicit integration proposal.|
|Grapheon|clean airlock recovery branch tracking origin|Agent-native requirements traceability/project management (`tracertm`) with Python MCP integration and supporting Rust services|preserve_recovery_branch; review alias or canonical merge|Traceability overlaps registry governance at the integration boundary, but is a distinct runtime product. Reconcile recovered branch provenance and map contracts before any canonicalization decision.|
|PhenoPlugins|clean; `main` synchronized with `origin/main`|Rust trait-based plugin framework, registry, lifecycle, and Git/SQLite/Vessel adapters for Phenotype hosts|queue_as_ABSORB|Verified ecosystem-wide shared-library purpose and explicit AgilePlus migration history support the existing onboarding recommendation. Gate absorption on crate/API dependency mapping and provenance-preserving import plan.|

## Cohort 22B dispositions (verified local evidence, unscheduled)

|repo|verified local state|canonical parent|disposition|rationale and next gate|
|---|---|---|---|---|
|CivicSurvival-public|clean; `main` synchronized with `origin/main`|CivicSurvival program|protect public boundary; no merge|The public source/docs client boundary is deliberately source-available, non-buildable, and paired with a closed server; PolyForm Strict and separately licensed assets prohibit an assimilation decision.|
|Civis|clean `wip/2026-07-22-civis-quality-manifest` tracking origin|Civis|retain independent WIP|Its explicit FR-CIV godgame scope excludes organization governance. Preserve the remote-tracked WIP branch; registry records governance evidence only.|
|Eidolon|clean local `feat/cross-repo-audit-wave2` with no upstream shown|Eidolon|publish local branch, then retain independent|Device automation is a distinct library product; its archived satellites are extract-on-demand rather than merge candidates. Establish remote provenance for the local branch before further boundary review.|
|HexaKit|clean `main` ahead of `origin/main` by 1|phenotype-infrakit (HexaKit)|retain canonical; push ahead commit|The canonical Rust infrastructure-kit code boundary complements registry governance. Preserve the ahead commit remotely before any dependency-level consolidation work.|
|Melosviz|clean recovery branch `recovery/melosviz-local-20260726` tracking origin|Melosviz|retain independent recovery branch|Music visualization (Python backend, React web, Rust WGPU/MIR) has no material registry overlap. Retain and verify recovery-branch provenance.|

## Cohort 22C dispositions (verified active-lane and registry evidence, unscheduled)

|repo|verified local state|canonical parent|disposition|blocker and next gate|
|---|---|---|---|---|
|AgilePlus|`main` ahead of origin by 1; materially dirty with source, Airlock-document, and untracked MCP work|AgilePlus PLATFORM spine|preserve WIP; ARCHIVE_ONLY, no absorption|Registry boundary policy requires sponsor ratification of PLATFORM-spine promotion; the dirty 94-crate mega-workspace is unsafe for integration. Snapshot/publish current work before any isolated review.|
|OmniRoute|dirty `fix/stray-brace-mitm-manager` tracking origin|OmniRoute canonical LLM router|preserve active branch; never archive|The active router remains canonical. The separate archived `omniroute-rust` source needs a 13-crate ownership and provenance reconciliation; no name-level merge is valid.|
|PlayCua|clean `master` tracking origin|PlayCua archive evidence / phenoAI review target|archive-only evidence; no import|Wave-21 registry evidence records ARCHIVE_ONLY after structural Rust-workspace dependency failures prevented phenoAI ingestion; no merge is required in this wave.|
|SessionLedger|`main` tracking origin with material tracked source/test changes and untracked coverage/mutant outputs|SessionLedger session-compiler product|preserve WIP; no merge or archive|The active OKF session-compiler boundary is distinct. Publish and validate the dirty worktree in isolation before its no-auto-merge lane can advance.|
|Tracera|heavily dirty `preserve/tracera-dirty-wave-20260729` tracking origin, including source, docs, and generated paths|Tracera trace/observability/audit ledger|preserve dirty branch; no absorption or archive|Five recovery shells remain recorded as empty with local payload search blocked. Establish recovery parity and isolate generated artifacts before any boundary transaction.|

## Next Cohort dispositions (verified local evidence, unscheduled)

|repo|verified local state|canonical role or parent|disposition|overlap, risk, and next gate|
|---|---|---|---|---|
|asset-engine|clean preservation branch `preserve/asset-engine-archive-20260729`|phenoDesign and pheno|ARCHIVED-PRESERVED|README records completed asset-pipeline absorption into phenoDesign/pheno; preserve history only.|
|cliproxyapi-plusplus|clean WIP branch `wip/2026-07-22-cliproxyapi-go-mod-preservation`|gateway / OmniRoute-adjacent fork|preserve isolated fork|Multi-provider Go proxy has residual Go test failures; require API and fork-provenance mapping before any integration.|
|forgecode|dirty preservation branch tracking a fork|HeliosLite product|preserve fork WIP|Rust agentic terminal/TUI rebrand atop upstream forgecode; retain independently pending upstream/provenance review.|
|helios-cli|dirty WIP branch with harness changes|HeliosCLI|preserve independent WIP|Distinct Phenotype harness/CLI product; publish and validate the dirty worktree before any boundary change.|
|hfscope|dirty remote-tracked Go fix branch; no root README|unclassified|evidence-only HOLD|No root intent/contract evidence supports a parent choice; preserve branch and perform a bounded source/contract audit.|
|hwLedger|clean remote-tracked WIP branch|hwLedger|retain independent WIP|Pre-alpha hardware capacity/fleet ledger and desktop inference runtime is a distinct product boundary.|
|nanovms|clean `main` tracking origin|nanovms engine|retain independent canonical engine|May expose an Eidolon adapter crossing, but engine ownership remains independent.|
|portage|remote-tracked fix branch with staged deletion/type changes|portage / Harbor fork|preserve fork branch|Harbor/Terminal-Bench evaluation fork requires upstream provenance and staged-change validation before action.|
|sharecli|dirty Rust runtime/OpenAPI branch|sharecli|preserve WIP; dedupe required|OS-adjacent multi-agent runtime overlaps `thegent-sharecli`; compare semantics, contracts, and history before target selection.|
|pheno|dirty `main` tracking origin|component-level Phenotype infrastructure parent|preserve WIP; decompose only|Broad monorepo is unsafe for wholesale absorption; map component provenance before any redistribution.|
|phenotype-apps|clean local `main`; no root README or manifest evidence|unproven|evidence-only HOLD|Do not select a parent until a bounded source/intent audit establishes ownership.|
|phenotype-hub|clean `main` tracking origin|governance coordination scaffold|retain separate scaffold|README declares no runtime source; require content-parity proof before any registry consolidation.|
|phenotype-omlx|feature branch ahead of origin by 10|phenotype-omlx|publish branch; retain canonical|Explicit canonical MLX-native OMLX research stack; no absorption action is justified.|
|phenotype-tooling|WIP branch ahead of main by 76|phenotype-tooling|publish WIP; retain canonical|Developer tooling/CI/quality/release workspace; only component-level imports after provenance checks.|
|thegent|remote-tracked governance branch ahead 26 with dirty work and untracked `sharecli/`|thegent|preserve/publish branch|Unified agent-orchestration CLI has embedded/sharecli overlap; reconcile via API and provenance audit.|
|thegent-sharecli|clean `main` tracking origin|pending semantic duplicate decision|retain pending dedupe|Python command-sharing/task-queue tool overlaps Rust `sharecli`; do not archive before parity proof.|
|turboquant_plus|clean `main` tracking origin|TurboQuant research provenance|retain independent research repo|Research/reference/benchmark home with upstream vLLM and llama.cpp adoption; no physical absorption.|
|vibeproxy-monitoring-unified|clean `main` behind origin by 7|unproven monitoring governance owner|fast-forward then evidence-only HOLD|Spec-only scaffold contains no runtime assets; identify VibeProxy or PhenoObservability owner through content parity.|
|.tmp-phenotypes-boundary|clean `main` tracking origin; registry-identifying README/manifest|phenotype-registry duplicate boundary evidence|preserve evidence; no product action|Appears to be a full registry clone; prove ref/tree parity against phenotype-registry before treating it as disposable or archival evidence.|

## Wave 23 semantic dedupe - sharecli and thegent-sharecli

|dimension|sharecli|thegent-sharecli|dedupe finding|
|---|---|---|---|
|provenance|Rust repository `KooshaPari/sharecli`|Python repository `KooshaPari/thegent-sharecli`|Independent provenance: neither repository contains the other's inspected HEAD object, so no shared merge-base evidence exists.|
|runtime scope|OS-adjacent process runtime: sessions, FUSE, fleet/thermal control, dashboard, mesh queue, and SmartMerger|In-memory command locks, priority task queue, merge and edit-intent domain models|Only a qualitative 15-25% overlap at coordination vocabulary level; runtime and persistence surfaces differ materially.|
|canonical ownership|Durable multi-agent coordination runtime|Agent-oriented Python facade|Retain separate. `sharecli` is the canonical runtime owner; no repository merge, extraction, or archival action is justified yet.|

### Required parity gate: `coordination-lock-queue-v1`

Before any branch-level contract extraction is proposed, both adapters must run the same fixture and produce these outcomes:

1. Acquire command hash `H` for `PID1` yields `locked`.
2. Acquire `H` for `PID2` yields `already_locked`.
3. Release `H` for `PID1` yields `unlocked`.
4. Enqueue `low` then `high`; dequeue yields `high` first.
5. Edit intents `[10,20]` and `[30,40]` do not conflict; `[10,20]` and `[15,25]` conflict.

Missing surface or divergent behavior is decision evidence, not an implementation shortcut. Parity is not established until both durable adapters pass the fixture.

## DEDUPE-02 - cliproxyapi-plusplus and OmniRoute

|dimension|cliproxyapi-plusplus|OmniRoute|dedupe finding|
|---|---|---|---|
|provenance|Go module `github.com/kooshapari/CLIProxyAPI/v7`; `KooshaPari/cliproxyapi-plusplus` fork with upstream `router-for-me/CLIProxyAPI`|TypeScript/Rust gateway `KooshaPari/OmniRoute`; inspected checkout has only its Koosha origin|Independent Git provenance: neither checkout contains the other's inspected HEAD object. No shared-history or subtree evidence was found.|
|runtime relationship|Maintained multi-provider CLIProxyAPI runtime, exposing OpenAI-compatible proxy endpoints|Gateway product with a dedicated CLIProxyAPI executor, installer, and OAuth-import boundary; defaults to the external proxy at `127.0.0.1:8317`|cliproxyapi-plusplus is an external runtime dependency/component of OmniRoute, not a component extracted from OmniRoute. Shared OpenAI-compatible endpoint vocabulary is an integration contract, not provenance.|
|disposition|Retain isolated upstream fork|Retain canonical gateway product|retain_separate. No repository merge, branch extraction, or archive action is justified by the current evidence.|

### Required provenance gate: `cliproxy-omniroute-path-provenance-v1`

Before proposing any branch extraction, compare OmniRoute's `open-sse/executors/cliproxyapi.ts` and the CLIProxyAPI installer and OAuth auth-import boundaries with the corresponding cliproxyapi-plusplus and upstream source paths, using commit/tree/path attribution. Extraction is permitted only if the comparison demonstrates copied or ported implementation provenance beyond public endpoint/configuration compatibility. Otherwise preserve the external-adapter boundary and retain both repositories separately.

## DEDUPE-03 - PhenoObservability and Tracera

|dimension|PhenoObservability|Tracera|dedupe finding|
|---|---|---|---|
|runtime scope|Reusable Rust/Python observability substrate: OpenTelemetry/OTLP, Prometheus metrics, structured logging, and pluggable ports/adapters|Stateful Rust traceability and audit-ledger application: evidence, trace-links, governance computation, ingest, MCP, CLI, and web/desktop clients|Medium vocabulary and outcome overlap around tracing, metrics, and audit signals; the boundaries are complementary producer/substrate and consumer/ledger rather than duplicate products.|
|provenance|`KooshaPari/PhenoObservability` with a local `pheno-tracing` remote|`KooshaPari/Tracera` origin|Independent provenance: neither checkout contains the other's inspected HEAD object and no direct cross-Cargo dependency was found. The PhenoObservability README identifies Tracera as a primary consumer, which is integration intent rather than shared implementation provenance.|
|worktree state|Clean remote-tracked WIP branch|Materially dirty recovery branch: 81 tracked paths and 16 untracked paths, including server/store, frontend, docs, and generated/recovery content|Tracera's unsealed recovery payload blocks extraction or merge assessment until it is preserved and reproducible from a clean base.|
|disposition|Own reusable instrumentation and exporter primitives|Own durable evidence, trace-link, and audit product state|retain_separate. No branch extraction or workspace merge is justified. A future integration belongs in a thin adapter owned by the producer-consumer contract.|

### Required compatibility gate: `observability-ledger-consumer-v1`

After Tracera recovery has a remote preservation snapshot and clean-base proof, run an isolated SQLite-backed Tracera server with a sanitized PhenoObservability-produced event fixture containing `artifact_id`, `kind`, `url`, and metadata with a correlation/span identifier. The adapter must make Tracera `POST /evidence` accept the fixture; `GET /evidence` must return it; and `POST /api/v1/trace/forward/{artifact_id}` must address it through the mounted traceability contract. Capture request/response schemas and adapter provenance. Passing proves producer-consumer compatibility only; it does not authorize extraction without a separate path/tree provenance audit.

## DEDUPE-04 - Agentora and legacy PhenoAgent/agentkit copies

|dimension|Agentora|legacy PhenoAgent/agentkit copies|dedupe finding|
|---|---|---|---|
|canonical owner|`KooshaPari/Agentora`: root `agentkit` framework plus workspace members `crates/pheno-agent/{phenotype-daemon,phenotype-skills}`|Deleted `KooshaPari/PhenoAgent` source, excluded `Agentora/agents/phenoagent/*` tree, and `phenotype-tooling/docs/absorbed-from-PhenoAgent/` evidence archive|Retain Agentora as the live canonical owner. Cargo metadata includes the `crates/pheno-agent/*` members, while the legacy tree is deliberately excluded from workspace ownership.|
|provenance|`ORIGIN.md` declares Agentora/agentkit canonical; the PhenoAgent absorption record names `crates/pheno-agent/` canonical|Direct lineage: the record describes an Agentora-to-PhenoAgent forward port at `aee873f`, then reverse absorption; the original remote now returns 404|This is direct historical lineage, not a name-level overlap. The canonical crate absorption and the legacy-tree merge have separate Agentora history.|
|duplicate state|Canonical daemon and skills paths are registered workspace members and have canonical tests|`agents/phenoagent` is a divergent excluded copy; daemon has 23 files versus canonical 22, including legacy-only `shims/typescript/langchain.ts`; daemon, skills, Cargo, RPC, and protocol files differ. The tooling archive is a third historical snapshot with sampled hashes different from both Agentora trees.|Do not blindly extract, delete, or select a legacy tree: unresolved divergent behavior and provenance remain. The tooling path is archive evidence, not a live runtime owner.|
|disposition|retain canonical live Agentora|retain deleted-source tombstone and archive evidence; no new runtime product|No repository merge or branch extraction now. The stale Cargo comment pointing to the absent PhenoAgent remote cannot override the documented absorption record.|

### Required reconciliation gate: `agentora-phenoagent-canonical-runtime-v1`

Create a path-by-path, commit-and-hash provenance map for every executable file in `agents/phenoagent/{phenotype-daemon,phenotype-skills}` and the tooling archive, classifying it as canonical `crates/pheno-agent/*`, separately owned, or archive-only. Resolve every non-identical or legacy-only file, including `shims/typescript/langchain.ts`, by an explicit transplant-with-tests or archival decision. Then prove canonical workspace ownership with `cargo metadata --no-deps`, run `cargo test --workspace --all-features`, and pass a daemon request/response plus skill-registry compatibility fixture against canonical paths. Only then may the excluded legacy tree be retired; this gate does not authorize absorbing Agentora into another parent.

## DEDUPE-05 - `.tmp-phenotypes-boundary` and phenotype-registry

|proof|evidence|dedupe finding|
|---|---|---|
|remote and ancestry|The temporary checkout and canonical checkout both use `git@github.com:KooshaPari/phenotype-registry.git`. Temporary HEAD `424a9e44a37ba19c5d16f5ef9050dcba8ccae199` is an ancestor of canonical WIP commit `f835eb2b93843d98060ae208207fbbff8aa6fea3`; the reverse is false.|This is a stale local checkout of the canonical registry, not a separate repository boundary.|
|unique commits and tracked paths|`git rev-list` reports 0 temporary-only commits and 34 canonical-only commits. `git diff --name-status` reports 0 temporary-only tracked paths and 56 canonical-only added paths.|No unique committed source or evidence remains in the temporary checkout.|
|untracked payload|Untracked-file listing reports 0 files in the temporary checkout and 0 in the canonical checkout.|Git ancestry is not masking local-only payload in the temporary checkout.|
|disposition|Canonical registry retains all source/evidence; temporary checkout is non-authoritative.|No merge or archive transaction is required. The local checkout is eligible for later retirement only after the remote-ref proof gate passes; no deletion is authorized by this record.|

### Required proof gate: `registry-duplicate-checkout-retirement-v1`

Before any local checkout retirement, record a fresh target ref on `KooshaPari/phenotype-registry`, prove the temporary HEAD is reachable from that remote ref, rerun temporary-only commit/path/untracked checks with all values zero, and verify no linked worktree or active process references `.tmp-phenotypes-boundary`. The gate authorizes only local-checkout cleanup under a separately approved destructive operation; it does not create an archive or alter canonical repository history.

## coordination-lock-queue-v1 publication blocker - thegent-sharecli

The isolated `thegent-sharecli` contract commit `2e1d734067c5d07847235bfbdf0a91c08bebc20b` contains only `src/thegent_cli_share/coordination_contract.py` and `tests/test_thegent_cli_share.py`; its focused normalized JSONL contract test passed. A non-force push to `KooshaPari/thegent-sharecli` was rejected because the GitHub repository is archived and read-only. No alternate remote, archive bypass, or forced publication was attempted. Sponsor direction is required before choosing whether to unarchive/publish, transplant the preserved commit into the established canonical owner, or retain it as local-only preservation evidence.

## observability-ledger-consumer-v1 contract

PhenoObservability emits `TraceOperation { trace_id, span_id, parent_span_id, kind, name, attributes }` through `TracePort::submit`. The isolated consumer fixture must map that data into Tracera `POST /evidence` with required `artifact_id`, `kind`, and `url`, plus optional JSON `metadata`; a successful create returns `201` with `EvidenceItem { id, artifact_id, kind, url, metadata, created_at, updated_at }`. `GET /evidence` returns `{ count, items }` and must contain the submitted artifact. `POST /api/v1/trace/forward/:artifact_id` accepts `{ links: [{ source_id, target_id, relationship, confidence, updated_at? }] }` and returns `{ artifact_id, direction: "forward", neighbors }`. The forward route computes neighbors from the supplied request links; it does not read persisted evidence, so a passing fixture proves request-level trace navigation rather than evidence-to-trace persistence. Use a clean pinned Tracera worktree with a fresh SQLite database and a sanitized deterministic trace/span/correlation fixture; no dirty recovery checkout may serve as test evidence.
