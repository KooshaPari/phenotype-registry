# absorption-hitl-wave-20260729-21

Generated: 2026-07-29T22:44:00Z UTC

Scope: evidence-gated, non-destructive consolidation prep for next executable wave.
Hard constraint: skip AgilePlus in this turn by sponsor policy.

## Execute-now queue (must satisfy all gate conditions)

- gate set: local_dir_exists=true AND api_ok=true AND target_specified=true AND provenance_clear=true

|rank|repo|path|target|size|private|archived|note|
|---|---|---|---|---:|---|---|---|
|1|KooshaPari/thegent-sharecli|thegent-sharecli|thegent|154|public|archived|Deprecated duplicate helper.|
|2|KooshaPari/phenotype-shared|shared|phenotype-shared|310|private|active|onboarding_action:queue; local_repo_dir:shared|
|3|KooshaPari/HexaKit|HexaKit|pheno (crates/hexa-kit)|23130|public|active|Phenotype-org hexagonal architecture toolkit.|

## Hold queue (do not execute until HITL/owner resolves)

|rank|repo|path|target|flags|note|
|---|---|---|---|---|---|
|5|KooshaPari/omniroute-rs|omniroute-rs|-|queued_or_active,api_fail|Audited 2026-07-17; Rust service port of OmniRoute. No README yet — verify scope.|
|6|KooshaPari/phenotype-router-spec|pheno-rt-spec-probe|phenotype-router-spec|queued_or_active,api_fail,local_present,targeted|onboarding_action:queue; local_repo_dir:pheno-rt-spec-probe; hold: remote origin exists but repository not readable (git ls-remote: repository not found), so API/remote provenance remains unresolved|
|7|KooshaPari/pheno-otel|pheno-otel|PhenoObservability|queued_or_active,api_ok,targeted|Audited 2026-07-17; Rust crate for OTEL bindings; fits observability spine; target backfilled from absorption note.|
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
|29|KooshaPari/PlayCua|PlayCua|-|queued_or_active,api_ok,local_present|Audited 2026-07-17; Rust+Python polyglot; absorbs cleanly into phenoAI agent workspace.|
|30|KooshaPari/phenotype-journeys|phenotype-journeys|-|queued_or_active,api_ok,local_present|onboarding_action:queue; local_repo_dir:phenotype-journeys|
|31|KooshaPari/PhenoMCPServers|PhenoMCPServers|PhenoMCPServers (self, fleet aggregator)|queued_or_active,api_ok,targeted|Phenotype MCP implementations registry - candidate for AFFIRM promotion.|
|32|KooshaPari/phenotype-python-sdk|phenotype-python-sdk|-|queued_or_active,api_ok,local_present|onboarding_action:queue; local_repo_dir:phenotype-python-sdk|
|33|KooshaPari/PhenoObservability|PhenoObservability|-|queued_or_active,api_ok,local_present|onboarding_action:queue; local_repo_dir:PhenoObservability|
|34|KooshaPari/PolicyStack|PolicyStack|-|queued_or_active,api_ok|Audited 2026-07-17; per RATIONALIZATION_EXECUTION.md the policy-federation identifier is already resolved; safe to absorb without chokepoint concerns.|
|35|KooshaPari/HeliosLab|HeliosLab|-|queued_or_active,api_ok|Audited 2026-07-17; research content fits docs layer.|
|36|KooshaPari/KodeVibe|KodeVibe|-|queued_or_active,api_ok| |
|37|KooshaPari/context-mode-plusplus|context-mode-plusplus|-|queued_or_active,api_ok|Audited 2026-07-17; fork; integration code (middleware + adapters) belongs with route layer.|
|38|KooshaPari/CivicSurvival-public|CivicSurvival-public|-|queued_or_active,api_ok,local_present|onboarding_action:queue; local_repo_dir:CivicSurvival-public|
|39|KooshaPari/KWatch|KWatch|-|queued_or_active,api_ok|Audited 2026-07-17; active monitoring/watchdog daemon for K-series services. Now queued for absorption into phenotype-tooling.|
|40|KooshaPari/WorldSphereMod|WorldSphereMod|phenotype-legacy-collection|queued_or_active,api_ok,targeted|Backup of deleted WorldSphereMod repo (100% recovered). Legacy 3D mod backup.|
|41|KooshaPari/Dino|Dino|phenotype-apps (DINOForge)|queued_or_active,api_ok,targeted|DINOForge general-purpose mod platform for AI agents. BLOCK-A app, fits phenotype-apps pattern.|

### HITL requests for sponsor

- Confirm execute order for execute-now queue (smallest-footprint first).
- Resolve `phenotype-router-spec` provenance: remote not readable despite configured origin/URL.
- Confirm whether AgilePlus remains policy-skipped or can be queued in a separate archival wave.
