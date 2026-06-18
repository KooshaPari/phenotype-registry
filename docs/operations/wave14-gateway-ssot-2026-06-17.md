# Wave 14 — Gateway SSOT foundation — 2026-06-17

**Predecessor:** [wave13-execution-2026-06-17.md](./wave13-execution-2026-06-17.md)  
**DAG:** [GATEWAY_MERGE_DAG.md](../rationalization/GATEWAY_MERGE_DAG.md)  
**ADR:** [ADR-ECO-007-gateway-merge-superset](../adrs/ADR-ECO-007-gateway-merge-superset.md)

## Remote audit baseline (gh, 2026-06-17)

| Repo | Branches | Registry verdict (corrected) |
|------|----------|------------------------------|
| agentapi-plusplus | 34 | **AFFIRM** `cli_proxy` — merge superset |
| cliproxyapi-plusplus | 11 | **AFFIRM** peer/submodule |
| bifrost | 339 | **VENDOR-KEEP** — sync lane only |
| OmniRoute | 26 | **CANONICAL** `route` — protect |
| phenotype-omlx | 27 (archived) | **DECISION** FINISH vs DROP |
| PhenoCompose | 15 | **AFFIRM** `platform` — blocks pheno archive |
| PhenoRuntime | 14 (archived) | **HARVEST → DELETE** |
| vibeproxy | 6 | **SKIP** reconciliation |
| agileplus-spec-harmonizer | 1 | Register tooling; spec SSOT for merges |
| phenotype-e2e-base | 2 | Absorb → phenotype-journeys |

## Registry contradictions fixed

| Topic | Stale | Fixed in |
|-------|-------|----------|
| OmniRoute archive | RATIONALIZATION_PLAN Step 1 | Banner + removal from archive list |
| agentapi++ archive | ECOSYSTEM_MAP §6, PLAN | AFFIRM + disposition row |
| Settly canonical | ECOSYSTEM_MAP Cluster H | phenotype-config (`settly` crate) |
| BytePort active | ECOSYSTEM_MAP §1 monorepo | ARCHIVED → phenotype-tooling |
| phenoXddLib owner | BOUNDARY_OWNERS | ARCHIVED; xDD → phenoXdd + journeys |
| Missing gateway roles | DOMAIN_ROLES | `route`, `cli_proxy`, `inference` |

## PR tracker

| PR | Repo | Status |
|----|------|--------|
| docs/wave14-gateway-ssot | phenotype-registry | open |

## Next waves (unblocked after merge)

| Wave | Lane |
|------|------|
| 15 | agentapi++ branch merge + SPEC.md |
| 16 | cliproxy boundary + prune |
| 16b | bifrost vendor policy |
| 17 | omlx decision |
| 17b | PhenoCompose + pheno repoint |
| 18 | archived `projects/*.json` |
| 18b | pheno fleet scan + archive gate |
| 19 | e2e-base → journeys |
