# Spec Document Coverage Audit - 2026-04-27

Scope: local-only audit of visible canonical Git working trees under `/Users/kooshapari/CodeProjects/Phenotype/repos/<name>/`. Local presence is used as the non-archived repository proxy; no GitHub/API archive state was queried.

Required document checks, per `~/.claude/CLAUDE.md` Required Project Documentation request:
- `has_PRD`: `[ -f PRD.md ]`
- `has_ADR`: `[ -f ADR.md ] || [ -d docs/adr/ ]`
- `has_FR`: `[ -f FUNCTIONAL_REQUIREMENTS.md ]`
- `has_PLAN`: `[ -f PLAN.md ]`
- `has_USER_JOURNEYS`: `[ -f USER_JOURNEYS.md ]`

Exclusions: hidden shelf metadata, `.archive`, `.worktrees`, `worktrees`, `repos-wtrees`, `*-wtrees`, and `*-wtr` paths.

## Summary

- Repositories audited: 113
- Complete coverage: 11/113 (9.7%)
- Repositories missing all five required surfaces: 23
- Gap repositories: 102

| Document surface | Present | Missing | Coverage |
| --- | ---: | ---: | ---: |
| `PRD.md` | 67 | 46 | 59.3% |
| `ADR.md or docs/adr/` | 67 | 46 | 59.3% |
| `FUNCTIONAL_REQUIREMENTS.md` | 76 | 37 | 67.3% |
| `PLAN.md` | 70 | 43 | 61.9% |
| `USER_JOURNEYS.md` | 12 | 101 | 10.6% |

## Missing-Most-First Matrix

| Repo | Missing Count | has_PRD | has_ADR | has_FR | has_PLAN | has_USER_JOURNEYS | Missing |
| --- | ---: | --- | --- | --- | --- | --- | --- |
| `AgentMCP` | 5 | no | no | no | no | no | PRD.md, ADR.md or docs/adr/, FUNCTIONAL_REQUIREMENTS.md, PLAN.md, USER_JOURNEYS.md |
| `agileplus-landing` | 5 | no | no | no | no | no | PRD.md, ADR.md or docs/adr/, FUNCTIONAL_REQUIREMENTS.md, PLAN.md, USER_JOURNEYS.md |
| `artifacts` | 5 | no | no | no | no | no | PRD.md, ADR.md or docs/adr/, FUNCTIONAL_REQUIREMENTS.md, PLAN.md, USER_JOURNEYS.md |
| `byteport-landing` | 5 | no | no | no | no | no | PRD.md, ADR.md or docs/adr/, FUNCTIONAL_REQUIREMENTS.md, PLAN.md, USER_JOURNEYS.md |
| `DINOForge-UnityDoorstop` | 5 | no | no | no | no | no | PRD.md, ADR.md or docs/adr/, FUNCTIONAL_REQUIREMENTS.md, PLAN.md, USER_JOURNEYS.md |
| `foqos-private` | 5 | no | no | no | no | no | PRD.md, ADR.md or docs/adr/, FUNCTIONAL_REQUIREMENTS.md, PLAN.md, USER_JOURNEYS.md |
| `heliosBench` | 5 | no | no | no | no | no | PRD.md, ADR.md or docs/adr/, FUNCTIONAL_REQUIREMENTS.md, PLAN.md, USER_JOURNEYS.md |
| `hwledger-landing` | 5 | no | no | no | no | no | PRD.md, ADR.md or docs/adr/, FUNCTIONAL_REQUIREMENTS.md, PLAN.md, USER_JOURNEYS.md |
| `phenoData` | 5 | no | no | no | no | no | PRD.md, ADR.md or docs/adr/, FUNCTIONAL_REQUIREMENTS.md, PLAN.md, USER_JOURNEYS.md |
| `PhenoKits` | 5 | no | no | no | no | no | PRD.md, ADR.md or docs/adr/, FUNCTIONAL_REQUIREMENTS.md, PLAN.md, USER_JOURNEYS.md |
| `phenokits-landing` | 5 | no | no | no | no | no | PRD.md, ADR.md or docs/adr/, FUNCTIONAL_REQUIREMENTS.md, PLAN.md, USER_JOURNEYS.md |
| `phenotype-journeys` | 5 | no | no | no | no | no | PRD.md, ADR.md or docs/adr/, FUNCTIONAL_REQUIREMENTS.md, PLAN.md, USER_JOURNEYS.md |
| `phenotype-omlx` | 5 | no | no | no | no | no | PRD.md, ADR.md or docs/adr/, FUNCTIONAL_REQUIREMENTS.md, PLAN.md, USER_JOURNEYS.md |
| `phenotype-ops-mcp` | 5 | no | no | no | no | no | PRD.md, ADR.md or docs/adr/, FUNCTIONAL_REQUIREMENTS.md, PLAN.md, USER_JOURNEYS.md |
| `phenotype-ops-mcp-fix` | 5 | no | no | no | no | no | PRD.md, ADR.md or docs/adr/, FUNCTIONAL_REQUIREMENTS.md, PLAN.md, USER_JOURNEYS.md |
| `phenotype-org-audits` | 5 | no | no | no | no | no | PRD.md, ADR.md or docs/adr/, FUNCTIONAL_REQUIREMENTS.md, PLAN.md, USER_JOURNEYS.md |
| `phenotype-tooling` | 5 | no | no | no | no | no | PRD.md, ADR.md or docs/adr/, FUNCTIONAL_REQUIREMENTS.md, PLAN.md, USER_JOURNEYS.md |
| `Planify` | 5 | no | no | no | no | no | PRD.md, ADR.md or docs/adr/, FUNCTIONAL_REQUIREMENTS.md, PLAN.md, USER_JOURNEYS.md |
| `projects-landing` | 5 | no | no | no | no | no | PRD.md, ADR.md or docs/adr/, FUNCTIONAL_REQUIREMENTS.md, PLAN.md, USER_JOURNEYS.md |
| `rich-cli-kit` | 5 | no | no | no | no | no | PRD.md, ADR.md or docs/adr/, FUNCTIONAL_REQUIREMENTS.md, PLAN.md, USER_JOURNEYS.md |
| `Sidekick` | 5 | no | no | no | no | no | PRD.md, ADR.md or docs/adr/, FUNCTIONAL_REQUIREMENTS.md, PLAN.md, USER_JOURNEYS.md |
| `thegent-dispatch` | 5 | no | no | no | no | no | PRD.md, ADR.md or docs/adr/, FUNCTIONAL_REQUIREMENTS.md, PLAN.md, USER_JOURNEYS.md |
| `thegent-landing` | 5 | no | no | no | no | no | PRD.md, ADR.md or docs/adr/, FUNCTIONAL_REQUIREMENTS.md, PLAN.md, USER_JOURNEYS.md |
| `agent-user-status` | 4 | no | no | yes | no | no | PRD.md, ADR.md or docs/adr/, PLAN.md, USER_JOURNEYS.md |
| `AuthKit` | 4 | no | no | yes | no | no | PRD.md, ADR.md or docs/adr/, PLAN.md, USER_JOURNEYS.md |
| `cheap-llm-mcp` | 4 | no | no | yes | no | no | PRD.md, ADR.md or docs/adr/, PLAN.md, USER_JOURNEYS.md |
| `DevHex` | 4 | no | no | yes | no | no | PRD.md, ADR.md or docs/adr/, PLAN.md, USER_JOURNEYS.md |
| `dinoforge-packs` | 4 | no | no | yes | no | no | PRD.md, ADR.md or docs/adr/, PLAN.md, USER_JOURNEYS.md |
| `Eidolon` | 4 | no | no | yes | no | no | PRD.md, ADR.md or docs/adr/, PLAN.md, USER_JOURNEYS.md |
| `eyetracker` | 4 | no | no | yes | no | no | PRD.md, ADR.md or docs/adr/, PLAN.md, USER_JOURNEYS.md |
| `MCPForge` | 4 | no | no | yes | no | no | PRD.md, ADR.md or docs/adr/, PLAN.md, USER_JOURNEYS.md |
| `Metron` | 4 | no | no | yes | no | no | PRD.md, ADR.md or docs/adr/, PLAN.md, USER_JOURNEYS.md |
| `ObservabilityKit` | 4 | no | no | yes | no | no | PRD.md, ADR.md or docs/adr/, PLAN.md, USER_JOURNEYS.md |
| `Paginary` | 4 | no | no | yes | no | no | PRD.md, ADR.md or docs/adr/, PLAN.md, USER_JOURNEYS.md |
| `phenoAI` | 4 | no | no | yes | no | no | PRD.md, ADR.md or docs/adr/, PLAN.md, USER_JOURNEYS.md |
| `PhenoPlugins` | 4 | no | no | no | yes | no | PRD.md, ADR.md or docs/adr/, FUNCTIONAL_REQUIREMENTS.md, USER_JOURNEYS.md |
| `PhenoProject` | 4 | no | no | yes | no | no | PRD.md, ADR.md or docs/adr/, PLAN.md, USER_JOURNEYS.md |
| `phenotype-bus` | 4 | no | no | yes | no | no | PRD.md, ADR.md or docs/adr/, PLAN.md, USER_JOURNEYS.md |
| `phenotype-hub` | 4 | no | no | yes | no | no | PRD.md, ADR.md or docs/adr/, PLAN.md, USER_JOURNEYS.md |
| `phenotype-infra` | 4 | no | yes | no | no | no | PRD.md, FUNCTIONAL_REQUIREMENTS.md, PLAN.md, USER_JOURNEYS.md |
| `phenotype-registry` | 4 | no | no | no | yes | no | PRD.md, ADR.md or docs/adr/, FUNCTIONAL_REQUIREMENTS.md, USER_JOURNEYS.md |
| `phenoUtils` | 4 | no | no | yes | no | no | PRD.md, ADR.md or docs/adr/, PLAN.md, USER_JOURNEYS.md |
| `vibeproxy-monitoring-unified` | 4 | no | no | yes | no | no | PRD.md, ADR.md or docs/adr/, PLAN.md, USER_JOURNEYS.md |
| `Dino` | 3 | yes | yes | no | no | no | FUNCTIONAL_REQUIREMENTS.md, PLAN.md, USER_JOURNEYS.md |
| `GDK` | 3 | no | no | yes | yes | no | PRD.md, ADR.md or docs/adr/, USER_JOURNEYS.md |
| `nanovms` | 3 | no | yes | no | yes | no | PRD.md, FUNCTIONAL_REQUIREMENTS.md, USER_JOURNEYS.md |
| `PhenoCompose` | 3 | no | yes | no | yes | no | PRD.md, FUNCTIONAL_REQUIREMENTS.md, USER_JOURNEYS.md |
| `hwLedger` | 2 | yes | yes | no | yes | no | FUNCTIONAL_REQUIREMENTS.md, USER_JOURNEYS.md |
| `McpKit` | 2 | yes | yes | no | yes | no | FUNCTIONAL_REQUIREMENTS.md, USER_JOURNEYS.md |
| `PhenoObservability` | 2 | yes | yes | no | yes | no | FUNCTIONAL_REQUIREMENTS.md, USER_JOURNEYS.md |
| `PhenoSpecs` | 2 | yes | yes | no | yes | no | FUNCTIONAL_REQUIREMENTS.md, USER_JOURNEYS.md |
| `phenotype-auth-ts` | 2 | yes | yes | yes | no | no | PLAN.md, USER_JOURNEYS.md |
| `PlatformKit` | 2 | yes | yes | no | yes | no | FUNCTIONAL_REQUIREMENTS.md, USER_JOURNEYS.md |
| `PlayCua` | 2 | yes | yes | no | yes | no | FUNCTIONAL_REQUIREMENTS.md, USER_JOURNEYS.md |
| `ResilienceKit` | 2 | yes | yes | no | yes | no | FUNCTIONAL_REQUIREMENTS.md, USER_JOURNEYS.md |
| `Tasken` | 2 | yes | no | yes | yes | no | ADR.md or docs/adr/, USER_JOURNEYS.md |
| `thegent-workspace` | 2 | yes | yes | no | yes | no | FUNCTIONAL_REQUIREMENTS.md, USER_JOURNEYS.md |
| `vibeproxy` | 2 | yes | no | yes | yes | no | ADR.md or docs/adr/, USER_JOURNEYS.md |
| `agent-devops-setups` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `agentapi-plusplus` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `agslag-docs` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `AppGen` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `argis-extensions` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `atoms.tech` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `AtomsBot` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `bare-cua` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `BytePort` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `chatta` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `cloud` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `Configra` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `Conft` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `DataKit` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `helios-cli` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `heliosCLI` | 1 | yes | no | yes | yes | yes | ADR.md or docs/adr/ |
| `HeliosLab` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `Httpora` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `KDesktopVirt` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `KlipDot` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `kmobile` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `kwality` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `localbase3` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `netweave-final2` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `org-github` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `phench` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `PhenoAgent` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `phenoDesign` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `PhenoDevOps` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `phenodocs` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `phenodocs-scorecard-remediation` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `PhenoHandbook` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `PhenoMCP` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `PhenoProc` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `phenoResearchEngine` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `PhenoRuntime` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `PhenoVCS` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `phenoXdd` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `portage` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `TestingKit` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `thegent` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `Tokn` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `Tracely` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `Tracera-recovered` | 1 | yes | yes | yes | yes | no | USER_JOURNEYS.md |
| `AgilePlus` | 0 | yes | yes | yes | yes | yes | - |
| `Civis` | 0 | yes | yes | yes | yes | yes | - |
| `cliproxyapi-plusplus` | 0 | yes | yes | yes | yes | yes | - |
| `FocalPoint` | 0 | yes | yes | yes | yes | yes | - |
| `helios-router` | 0 | yes | yes | yes | yes | yes | - |
| `heliosApp` | 0 | yes | yes | yes | yes | yes | - |
| `Parpoura` | 0 | yes | yes | yes | yes | yes | - |
| `pheno` | 0 | yes | yes | yes | yes | yes | - |
| `phenoShared` | 0 | yes | yes | yes | yes | yes | - |
| `PolicyStack` | 0 | yes | yes | yes | yes | yes | - |
| `QuadSGM` | 0 | yes | yes | yes | yes | yes | - |

## Generation Command

```bash
python3 <local audit script>  # enumerated repos/*/.git and checked only root PRD/ADR/FR/PLAN/USER_JOURNEYS paths
```
