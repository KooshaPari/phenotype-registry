# queued-batch-1-exec-manifest-20260729-20

Generated: 2026-07-29T22:08:25Z UTC

Total queued + ABSORB records with full_name: 24

Execution-first rule: local-first merge only, preserve/skip anything flagged API_FAIL until provenance is verified, and no destructive actions implied by this file.

## Top 20 queued ABSORB candidates by size

|rank|repo|size|path|local|target|flags|default_branch|canonical_name|notes|
|---|---|---:|---|---|---|---|---|---|---|
|1|KooshaPari/phenotype-router-spec|0|repos/pheno-rt-spec-probe|ci|-|API_FAIL|-|-|onboarding_action:queue; local_repo_dir:pheno-rt-spec-probe|
|2|KooshaPari/PlusForges|17|PlusForges|none|-|NO_LOCAL_DIR|main|-|-|
|3|KooshaPari/pheno-mcp-router|19|pheno-mcp-router|none|-|NO_LOCAL_DIR|main|-|-|
|4|KooshaPari/tehgent|34|tehgent|none|-|NO_LOCAL_DIR|main|-|-|
|5|KooshaPari/Compound-Spheres-3D-Backup|147|Compound-Spheres-3D-Backup|none|-|NO_LOCAL_DIR,PRIVATE|wsm3d/main|-|-|
|6|KooshaPari/thegent-sharecli|154|thegent-sharecli|exact|-|ARCHIVED_REMOTE|main|-|-|
|7|KooshaPari/phenotypeActions|171|phenotypeActions|none|-|NO_LOCAL_DIR,PRIVATE|main|-|-|
|8|KooshaPari/phenotype-go-kit|296|phenotype-go-kit|none|-|NO_LOCAL_DIR,PRIVATE|main|-|-|
|9|KooshaPari/phenotype-shared|310|repos/shared|ci|-|PRIVATE|main|-|onboarding_action:queue; local_repo_dir:shared|
|10|KooshaPari/phenotype-infrakit|338|phenotype-infrakit|none|-|NO_LOCAL_DIR,PRIVATE|chore/gitattributes|-|-|
|11|KooshaPari/phenoAI|348|repos/phenoAI|ci|-|ok|main|-|full_name backfilled from airlock bare remote|
|12|KooshaPari/PhenoRuntime|361|PhenoRuntime|none|-|NO_LOCAL_DIR,PRIVATE|main|-|-|
|13|KooshaPari/UnityDoorstop-NexusPatched|571|UnityDoorstop-NexusPatched|none|-|NO_LOCAL_DIR|master|-|-|
|14|KooshaPari/Tasken|609|Tasken|none|-|NO_LOCAL_DIR|main|-|-|
|15|KooshaPari/PhenoPlugins|627|repos/PhenoPlugins|ci|-|ok|main|-|onboarding_action:queue; local_repo_dir:PhenoPlugins|
|16|KooshaPari/phenotype-journeys|1080|repos/phenotype-journeys|ci|-|ok|main|-|onboarding_action:queue; local_repo_dir:phenotype-journeys|
|17|KooshaPari/PhenoMCPServers|3216|PhenoMCPServers|none|-|NO_LOCAL_DIR|main|-|-|
|18|KooshaPari/phenotype-python-sdk|5884|repos/phenotype-python-sdk|ci|-|ok|main|-|onboarding_action:queue; local_repo_dir:phenotype-python-sdk|
|19|KooshaPari/PhenoObservability|8494|repos/PhenoObservability|ci|-|ok|main|-|onboarding_action:queue; local_repo_dir:PhenoObservability|
|20|KooshaPari/HexaKit|23130|HexaKit|exact|-|ok|main|-|-|

## Hold list (review before execution)
- Records with `API_FAIL` or `NO_LOCAL_DIR` are review-gated for next turn.
- pheno-router-spec currently API_FAIL; verify rename/deletion before merge execution.
