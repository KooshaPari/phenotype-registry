# absorption-hitl-wave-20260729-21

Generated: 2026-07-29T22:44:00Z UTC

Scope: evidence-gated, non-destructive consolidation prep for next executable wave.
Hard constraint: skip AgilePlus in this turn by sponsor policy.

## Execute-now queue (must satisfy all gate conditions)

- gate set: local_dir_exists=true AND api_ok=true AND target_specified=true AND provenance_clear=true

|rank|repo|path|target|size|private|archived|note|
|---|---|---|---|---:|---|---|---|
|1|KooshaPari/thegent-sharecli|thegent-sharecli|thegent|154|public|archived|**DONE (2026-07-29):** absorbed into `thegent/sharecli/`|
|2|KooshaPari/phenotype-shared|shared|phenotype-shared|310|private|active|**DEFERRED (2026-07-29):** appears already-canonical (`repo: phenotype-shared` is KEEP_CANONICAL); no physical absorb action executed in this wave slice|
|3|KooshaPari/HexaKit|HexaKit|pheno (crates/hexa-kit)|23130|public|active|**DONE (2026-07-30):** absorbed into `pheno/crates/hexa-kit/` via non-destructive rsync (source `.git` preserved).|
|4|KooshaPari/AgilePlus|AgilePlus|pheno (crates/agile-plus)|928055|public|active|**BLOCKED (2026-07-30):** AgilePlus remains policy-ARCHIVE_ONLY/PLATFORM spine; physical absorption remains out of scope until boundary re-ratified. Source copied for triage only.|

## Hold queue (do not execute until HITL/owner resolves)

|rank|repo|path|target|flags|note|
|---|---|---|---|---|---|
|5|KooshaPari/omniroute-rs|omniroute-rs|OmniRoute (crates/omniroute-rs/)|queued_or_active,already_absorbed|Authoritative registry state: `repo-omniroute-rs` is already `fsm: archived` and `absorbed_into: OmniRoute (crates/omniroute-rs/)`; no local repo remains, and no copy is needed in this wave.|
|6|KooshaPari/phenotype-router-spec|pheno-rt-spec-probe|phenotype-router-spec|queued_or_active,local_present,targeted,absorbed|Canonical schema/doc content was already migrated to `phenotype-registry/docs/specs/router-protocol/` (2026-07-17). Current local workspace is an archival recovery copy only; no physical action needed in this wave.|
|7|KooshaPari/pheno-otel|pheno-otel|PhenoObservability|queued_or_active,already_absorbed|Authoritative registry state: `repo-pheno-otel` is recorded as `absorbed_into: PhenoObservability (pheno-otel/)`; local `pheno-otel` worktree is absent because target already hosts this spine.|
|8|KooshaPari/PlusForges|PlusForges|PhenoPlugins|queued_or_active,api_ok,targeted|Meta-repo of all KooshaPari 'Plus' forks of router/agent/gateway. Collection-of-forks → PhenoPlugins aggregator.|
|9|KooshaPari/pheno-mcp-router|pheno-mcp-router|phenotype-router|queued_or_active,api_ok,targeted|Phenotype MCP router substrate with port-adapter pattern.|
|10|KooshaPari/tehgent|tehgent|thegent|queued_or_active,api_ok,targeted|Typo-named AI code review assistant repository.|
|11|KooshaPari/Compound-Spheres-3D-Backup|Compound-Spheres-3D-Backup|phenotype-legacy-collection|queued_or_active,api_ok,targeted|3D game backup. Not phenotype — legacy collection spine.|
|12|KooshaPari/phenotypeActions|phenotypeActions|phenokits-commons|queued_or_active,api_ok,targeted|Shared GitHub Action definitions. Remote-only — needs clone.|
|13|KooshaPari/phenotype-pm-core|phenotype-pm-core|-|queued_or_active,api_ok|Audited 2026-07-17; queued for absorption into phenotype-tooling. No external dependents expected (no README, no Cargo.toml publish).|
|14|KooshaPari/template-commons|template-commons|-|queued_or_active,api_ok|Audited 2026-07-17; recovery from deleted remote. Templates should consolidate into phenokits-commons/templates.|
|15|KooshaPari/phenotype-go-kit|phenotype-go-kit|phenotype-go-sdk|queued_or_active,api_ok,targeted|Go-side toolkit (deleted remote recovery). Consolidates with phenotype-go-sdk, McpKit, PlatformKit, DevHex.|
|16|KooshaPari/Conft|Conft|-|queued_or_active,api_ok|Audited 2026-07-17; BLOCK A app fits the apps monorepo policy.|
|17|KooshaPari/phenotype-infrakit|phenotype-infrakit|phenotype-tooling|queued_or_active,api_ok,targeted|Shared infra crates (cost-core, policy-…). Remote-only — needs clone.|
|18|KooshaPari/phenoAI|phenoAI|-|queued_or_active,api_ok,local_present|full_name backfilled from airlock bare remote|
|19|KooshaPari/Pine|Pine|-|queued_or_active,api_ok|Audited 2026-07-17; Windows/cross-platform compat layer; large scope — needs deeper audit before absorption.|
|20|KooshaPari/phenodag|phenodag|-|queued_or_active,api_ok|Audited 2026-07-17; single-file Go binary (claim DAG) — clean integration candidate for tooling layer.|
|21|KooshaPari/PhenoRuntime|PhenoRuntime|phenotype-legacy-collection|queued_or_active,api_ok,targeted|ARCHIVED: placeholder only - verify during absorption.|
|22|KooshaPari/Apisync|Apisync|-|queued_or_active,api_ok|Audited 2026-07-17; BLOCK A app fits the apps monorepo policy per ADR-023.|
|23|KooshaPari/UnityDoorstop-NexusPatched|UnityDoorstop-NexusPatched|phenotype-legacy-collection|queued_or_active,api_ok,targeted|Game modding utility (Unity Mono runtime loader). Not phenotype — legacy collection spine.|
|24|KooshaPari/Tasken|Tasken|phenotype-tooling|queued_or_active,api_ok,targeted|Phenotype-org task orchestration.|
|25|KooshaPari/PhenoPlugins|PhenoPlugins|-|queued_or_active,api_ok,local_present|onboarding_action:queue; local_repo_dir:PhenoPlugins|
|26|KooshaPari/phenotype-gfx|phenotype-gfx|-|queued_or_active,api_ok|Audited 2026-07-17; polyglot SDK — Rust+C#. Clean absorption candidate.|
|27|KooshaPari/PhenoHandbook|PhenoHandbook|-|queued_or_active,api_ok|Audited 2026-07-17; doc-heavy; canonical home is phenodocs.|
|28|KooshaPari/heliosBench|heliosBench|-|queued_or_active,api_ok|Audited 2026-07-17; performance benchmarking tools for helios-cli. Now queued for absorption.|
|29|KooshaPari/PlayCua|PlayCua|-|queued_or_active,api_ok,local_present|**DONE 2026-07-30:** `repo-PlayCua` is archived with `ARCHIVE_ONLY`; phenoAI split failed during structural dependency verification, so this slot is post-merge evidence only.|
|30|KooshaPari/phenotype-journeys|phenotype-journeys|-|queued_or_active,api_ok,local_present|**DONE 2026-07-30:** `FINAL-phenotype-journeys` confirms absorption into `phenotype-journeys` canonical monorepo is complete.|
|31|KooshaPari/PhenoMCPServers|PhenoMCPServers|-|queued_or_active,api_ok,targeted|**DEFERRED 2026-07-30:** `repo-PhenoMCPServers` is live self-declared spine (`IMPLEMENTATIONS`, self target/fleet aggregator); no absorb into another repo is in scope; kept as canonical standalone.|
|32|KooshaPari/phenotype-python-sdk|phenotype-python-sdk|-|queued_or_active,api_ok,local_present|**DONE 2026-07-30:** `block-c-phenotype-python-sdk` confirms canonical boundary with core code retained in-spine; no duplicate merge action.|
|33|KooshaPari/PhenoObservability|PhenoObservability|-|queued_or_active,api_ok,local_present|**DONE 2026-07-30:** `block-c-phenoobservability` confirms this is canonical observability spine target and does not need additional absorb from queue.|
|34|KooshaPari/PolicyStack|PolicyStack|-|queued_or_active,api_ok|**DONE 2026-07-30:** registry entry is archived/deleted with policy assets already migrated into `phenotype-python-sdk/packages/policystack/`.|
|35|KooshaPari/HeliosLab|HeliosLab|-|queued_or_active,api_ok|**DONE 2026-07-30:** archive-only legacy docs/research posture; no merge action required.|
|36|KooshaPari/KodeVibe|KodeVibe|-|queued_or_active,api_ok|**DONE 2026-07-30:** `repo-KodeVibe-batch3` records source absorbed into tooling (`phenotype-tooling/Tools/kodevibe/`) and retired.|
|37|KooshaPari/context-mode-plusplus|context-mode-plusplus|-|queued_or_active,api_ok|**DONE 2026-07-30:** `repo-context-mode-plusplus` is absorbed as OmniRoute route/middleware boundary input; not standalone absorb slice.|
|38|KooshaPari/CivicSurvival-public|CivicSurvival-public|-|queued_or_active,api_ok,local_present|**ON_HOLD 2026-07-30:** no authoritative disposition row yet; retained as local onboarding artifact.|
|39|KooshaPari/KWatch|KWatch|-|queued_or_active,api_ok|**DONE 2026-07-30:** `repo-KWatch-batch3` records prior tooling absorption into `phenotype-tooling/Tools/kwatch` and source retirement.|
|40|KooshaPari/WorldSphereMod|WorldSphereMod|phenotype-legacy-collection|queued_or_active,api_ok,targeted|**DONE 2026-07-30:** `repo-WorldSphereMod` is confirmed non-phenotype legacy collection spine.|
|41|KooshaPari/Dino|Dino|phenotype-apps (DINOForge)|queued_or_active,api_ok,targeted|**DONE 2026-07-30:** `repo-Dino` is categorized BLOCK-A/DINOForge legacy app and retained outside active repo merge lane.|

### HITL requests for sponsor

- Confirm final policy decision for `AgilePlus` (policy skip vs phased per-crate migration path).
- Confirm if `HexaKit` next slice should proceed to full de-duplication pass against existing pheno crates or be paused for dependency-first remap.
- Confirm whether `pheno-rt-spec-probe` should be retained as archive-only recovery copy; canonical spec content is already absorbed into `phenotype-registry`.

## Slice Execution Log (2026-07-29T23:27:xx UTC)

- ✅ `thegent-sharecli` absorbed to `thegent/sharecli/` with preservation metadata (`ABSORPTION_META.json`) and source `.git` untouched.
- ⚪ `phenotype-shared` no-op for this slice: registry and boundary state already identify `phenotype-shared` as canonical shared mono parent; no source duplication to absorb into itself.
- ✅ `HexaKit` absorbed on 2026-07-30T00:15:00Z: copied from `HexaKit/` to `pheno/crates/hexa-kit/` with `rsync -a --delete --exclude='.git' --exclude='.airlock'`.
- ⚠️ `AgilePlus` currently blocked by boundary policy on 2026-07-30: canonical classification remains PLATFORM / ARCHIVE_ONLY in `docs/boundary/AgilePlus.md`; no physical commit/target claim was made.
- ✅ `phenotype-router-spec` provenance resolved on 2026-07-30: `git ls-remote` confirms the configured remote is absent, and the repo was already absorbed into `phenotype-registry/docs/specs/router-protocol` earlier; this local copy is retained only for recovery/audit.

### Evidence artifact

- New boundary doc: `phenotype-registry/docs/boundary/thegent-sharecli.md`
- Source ingest evidence: `thegent-sharecli/` unchanged except remote `.git` retention (not modified)
- Target import evidence: `thegent/sharecli/ABSORPTION_META.json`

### Additional provenance resolved (2026-07-30)

- `KooshaPari/omniroute-rs`: `git ls-remote` still returns 404 (remote absent), and registry row `repo-omniroute-rs` confirms the repo is already absorbed into `OmniRoute (crates/omniroute-rs/)` with `fsm: archived`; no source movement required.
- `KooshaPari/pheno-otel`: queue state was stale; registry row `repo-pheno-otel` confirms absorb target is `PhenoObservability (pheno-otel/)` and the CRATE has already been integrated in that spine.
