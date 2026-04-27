# CodeQL Rust Coverage Gap Audit - 2026-04-27

Audit scope: non-archived Phenotype Rust repositories named in the 2026-04-27
CodeQL coverage request.

Premise: GitHub default CodeQL setup does not include Rust, so Rust repositories
need explicit CodeQL workflow coverage.

Source of truth:

```bash
gh api repos/KooshaPari/$r/contents/.github/workflows \
  --jq '.[] | select(.name | contains("codeql")) | .name'
```

Repos returning no matching workflow are marked `GAP`. Repos without a
`.github/workflows` directory are marked `WORKFLOWS_NOT_FOUND`.

Coverage: 14 / 34 repos have an explicit CodeQL workflow (41.2%).

| Status | Repository | CodeQL workflow evidence |
|---|---|---|
| HAS_CODEQL | AgilePlus | `codeql.yml` |
| HAS_CODEQL | BytePort | `codeql.yml` |
| HAS_CODEQL | Civis | `codeql.yml` |
| HAS_CODEQL | GDK | `codeql.yml` |
| HAS_CODEQL | HexaKit | `codeql.yml` |
| HAS_CODEQL | Metron | `codeql.yml` |
| HAS_CODEQL | PhenoKits | `codeql.yml` |
| HAS_CODEQL | PhenoProc | `codeql.yml` |
| HAS_CODEQL | PhenoRuntime | `codeql.yml` |
| HAS_CODEQL | agentapi-plusplus | `codeql.yml` |
| HAS_CODEQL | hwLedger | `codeql.yml` |
| HAS_CODEQL | phenoAI | `codeql.yml` |
| HAS_CODEQL | phenoData | `codeql.yml` |
| HAS_CODEQL | phenoShared | `codeql.yml` |
| GAP | Configra | `NO_CODEQL_WORKFLOW` |
| GAP | Eidolon | `NO_CODEQL_WORKFLOW` |
| GAP | FocalPoint | `NO_CODEQL_WORKFLOW` |
| GAP | HeliosLab | `NO_CODEQL_WORKFLOW` |
| GAP | KDV | `WORKFLOWS_NOT_FOUND` |
| GAP | KDesktopVirt | `NO_CODEQL_WORKFLOW` |
| GAP | PhenoMCP | `NO_CODEQL_WORKFLOW` |
| GAP | PhenoObservability | `NO_CODEQL_WORKFLOW` |
| GAP | PhenoPlugins | `NO_CODEQL_WORKFLOW` |
| GAP | PolicyStack | `NO_CODEQL_WORKFLOW` |
| GAP | Pyron | `WORKFLOWS_NOT_FOUND` |
| GAP | Sidekick | `NO_CODEQL_WORKFLOW` |
| GAP | Tasken | `NO_CODEQL_WORKFLOW` |
| GAP | agentkit | `WORKFLOWS_NOT_FOUND` |
| GAP | eyetracker | `NO_CODEQL_WORKFLOW` |
| GAP | helios-app | `WORKFLOWS_NOT_FOUND` |
| GAP | helios-cli | `NO_CODEQL_WORKFLOW` |
| GAP | helios-router | `NO_CODEQL_WORKFLOW` |
| GAP | phenoUtils | `NO_CODEQL_WORKFLOW` |
| GAP | phenotype-bus | `NO_CODEQL_WORKFLOW` |

Gap repos:

`Configra`, `Eidolon`, `FocalPoint`, `HeliosLab`, `KDV`, `KDesktopVirt`,
`PhenoMCP`, `PhenoObservability`, `PhenoPlugins`, `PolicyStack`, `Pyron`,
`Sidekick`, `Tasken`, `agentkit`, `eyetracker`, `helios-app`, `helios-cli`,
`helios-router`, `phenoUtils`, `phenotype-bus`.
