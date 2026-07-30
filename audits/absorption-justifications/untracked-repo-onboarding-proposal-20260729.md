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
|pheno-rt-spec-probe|KooshaPari/phenotype-router-spec|main|clean|API_FAIL|https://github.com/KooshaPari/phenotype-router-spec.git|queue_as_ABSORB|
|phenoAI|-|fix/phenoai-codeql-workflow-schema|clean|-|/Users/kooshapari/.airlock/repos/64f03a81ecb2.git|queue_as_ABSORB|

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
