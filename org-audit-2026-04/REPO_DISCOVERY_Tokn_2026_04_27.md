# Tokn Discovery Audit - 2026-04-27

Local-only discovery audit for:
`/Users/kooshapari/CodeProjects/Phenotype/repos/Tokn`

## Build State

- Git state: `## main...origin/main [behind 6]`
- Existing local changes in audited checkout:

```text
 M docs/.generated/doc-index.json
?? docs/package-lock.json
```

- Command: `timeout 90 cargo check --workspace 2>&1 | grep -E "^error|^warning:" | sort -u | head -20`
- Result: no matching `error` or `warning:` lines were emitted.
- Build summary: workspace check passed the requested error/warning filter inside the 90s timeout.

## TODO/FIXME Markers

- Command: `grep -rn "TODO\|FIXME\|XXX\|HACK" --include="*.rs" . 2>/dev/null | grep -v "/target/\|/.archive/"`
- Count: 2
- Top examples:

```text
./crates/tokenledger/src/utils.rs:720:        assert!(has_placeholder_marker("TODO: add price"));
./src/utils.rs:724:        assert!(has_placeholder_marker("TODO: add price"));
```

## Size And Crate Count

- Rust LOC, excluding `target` and `.archive`: 21,830
- Requested crate-count pipeline output: 0
- Actual package count with explicit metadata format: 2
- Packages:
  - `pareto-rs`
  - `tokenledger-rs`

Note: `cargo metadata --no-deps` emits Cargo's compatibility warning before JSON in
this checkout, which causes the requested `jq` pipeline to produce zero package names.
Re-running with `--format-version 1` reports 2 packages.

## Spec Doc Presence

Present:

- `README.md`
- `PRD.md`
- `ADR.md`
- `FUNCTIONAL_REQUIREMENTS.md`
- `PLAN.md`

Missing: none from the requested list.

## Top 3 Actionable Items

1. Reconcile the audited checkout hygiene: `main` is six commits behind `origin/main`
   and has pre-existing docs-generated/package-lock drift.
2. Investigate why `crates/tokenledger/src/utils.rs` and root `src/utils.rs` both
   carry equivalent placeholder-marker test coverage; consolidate if they are stale
   duplicate code paths.
3. Update future crate-count audit commands to use
   `cargo metadata --format-version 1 --no-deps` so Cargo's compatibility warning does
   not break JSON parsing.
