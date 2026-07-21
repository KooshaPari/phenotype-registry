# PhenoObservability Repo Discovery - 2026-04-27

## Scope

- Repository: `/Users/kooshapari/CodeProjects/Phenotype/repos/PhenoObservability`
- Mode: audit only, local discovery
- Git state: `## main...origin/main [behind 5]`
- Dirty entries observed: `KWatch`, `ObservabilityKit`

## Build State

`timeout 90 cargo check --workspace` completed before the timeout and failed.

Unique error/warning summary:

```text
error: async_instrumented can only be applied to async fn returning Result<T, E> or anyhow::Result<T>; got: TraceResult < () >
error: could not compile `tracingkit` (lib) due to 1 previous error
warning: `phenotype-observably-logging` (lib) generated 1 warning
warning: `phenotype-observably-sentinel` (lib) generated 1 warning
warning: build failed, waiting for other jobs to finish...
warning: field `config` is never read
warning: field `context` is never read
```

## TODO / FIXME Inventory

- Count: 0 Rust TODO/FIXME/XXX/HACK markers outside `target/` and `.archive/`
- Top examples: none found

## Size And Crates

- Rust LOC: 15,409
- Cargo package count: 12
- Note: the exact requested `cargo metadata --no-deps 2>&1 | jq ... | wc -l`
  pipeline returned `0` because Cargo's compatibility warning is merged into
  the JSON stream before `jq`; with `--format-version 1`, the metadata lists 12
  packages.
- Packages:
  - `pheno-dragonfly`
  - `phenotype-observably-macros`
  - `pheno-questdb`
  - `phenotype-llm`
  - `phenotype-mcp-server`
  - `tracely`
  - `phenotype-sentinel`
  - `helix-logging`
  - `tracingkit`
  - `phenotype-observably-tracing`
  - `phenotype-observably-logging`
  - `phenotype-observably-sentinel`

## Spec Documents

Present:

- `README.md`
- `PRD.md`
- `ADR.md`
- `PLAN.md`

Absent:

- `FUNCTIONAL_REQUIREMENTS.md`

## Top 3 Actionable Items

1. Fix the `tracingkit` macro application that applies `async_instrumented` to
   an async function returning `TraceResult<()>` instead of `Result<T, E>` or
   `anyhow::Result<T>`, then rerun `cargo check --workspace`.
2. Clean up dead fields reported by the check output: `config` in
   `phenotype-observably-logging` and `context` in
   `phenotype-observably-sentinel`, or wire them into behavior if intentional.
3. Add or route a canonical `FUNCTIONAL_REQUIREMENTS.md` surface so the root
   spec set is complete alongside `README.md`, `PRD.md`, `ADR.md`, and
   `PLAN.md`.
