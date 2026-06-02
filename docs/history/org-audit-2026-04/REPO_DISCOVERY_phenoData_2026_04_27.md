# phenoData Discovery Audit - 2026-04-27

Local-only discovery audit for:
`/Users/kooshapari/CodeProjects/Phenotype/repos/phenoData`

## Build State

- Git state: `## main...origin/main [ahead 1]`
- Existing local changes in audited checkout:

```text
?? worklogs/
```

- Command: `timeout 60 cargo check --workspace 2>&1 | grep -E "^error|^warning:" | sort -u | head -15`
- Result:

```text
warning: `pheno-query` (lib) generated 1 warning (run `cargo fix --lib -p pheno-query` to apply 1 suggestion)
warning: unused variable: `vec`
```

- Timeout check: a raw `timeout 60 cargo check --workspace` capture exited `124` while
  compiling native dependencies (`aws-lc-sys`, `surrealdb-librocksdb-sys`) after emitting
  the `pheno-query` warning above.

## TODO/FIXME Markers

- Command: `grep -rn "TODO\|FIXME\|XXX\|HACK" --include="*.rs" . 2>/dev/null | grep -v "/target/\|/.archive/" | head -20`
- Count: 0
- Top examples: none found.

## Size And Crate Count

- Rust LOC, excluding `target` and `.archive`: 387
- Requested crate-count pipeline output: 0
- Actual package count with explicit metadata format: 3
- Packages:
  - `surreal-bridge`
  - `pg-bridge`
  - `pheno-query`

Note: `cargo metadata --no-deps` emits Cargo's compatibility warning before JSON in
this checkout, which causes the requested `jq` pipeline to produce zero package names.
Re-running with `--format-version 1` reports 3 packages.

## Top 3 Actionable Items

1. Fix the `pheno-query` unused `vec` binding in `crates/pheno-query/src/lib.rs`.
2. Expect the first local workspace check to exceed 60 seconds while compiling
   SurrealDB/RocksDB and AWS-LC native dependencies; use a longer timeout for full validation.
3. Update future crate-count audit commands to use
   `cargo metadata --format-version 1 --no-deps` so Cargo's compatibility warning does
   not break JSON parsing.
