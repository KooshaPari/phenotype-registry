# phenoAI Discovery Audit - 2026-04-27

Local-only discovery audit for:
`/Users/kooshapari/CodeProjects/Phenotype/repos/phenoAI`

## Build State

- Git state: `## main...origin/main [behind 3]`
- Command: `timeout 60 cargo check --workspace 2>&1 | grep -E "^error|^warning:" | sort -u | head -15`
- Result:

```text
error: failed to load manifest for workspace member `/Users/kooshapari/CodeProjects/Phenotype/repos/phenoAI/crates/llm-router`
error: invalid unquoted key, expected letters, numbers, `-`, `_`
```

- Build summary: workspace check is blocked before compilation by an invalid Cargo manifest.
- Root cause pointer: `crates/llm-router/Cargo.toml:17` contains `tokio::sync = { version = "1.44", features = ["RwLock"] }`, which is not a valid dependency key.

## TODO/FIXME Markers

- Command: `grep -rn "TODO\|FIXME\|XXX\|HACK" --include="*.rs" . 2>/dev/null | grep -v "/target/\|/.archive/" | head -20`
- Count: 0
- Top examples: none found.

## Size And Crate Count

- Rust LOC, excluding `target` and `.archive`: 373
- Rust files scanned:
  - `crates/mcp-server/src/lib.rs`
  - `crates/pheno-embedding/src/lib.rs`
  - `crates/llm-router/src/lib.rs`
  - `tests/smoke_test.rs`
- Requested crate-count pipeline output: 0
- Actual package count with explicit metadata format: 0

Note: package counting is also blocked by the invalid `crates/llm-router/Cargo.toml` manifest, so Cargo cannot emit workspace metadata.

## Top 3 Actionable Items

1. Fix `crates/llm-router/Cargo.toml:17` by removing the invalid `tokio::sync` dependency entry and relying on the existing workspace `tokio` dependency/features.
2. Re-run `cargo metadata --no-deps --format-version 1` after the manifest parses to establish the real workspace package count.
3. Re-run `timeout 60 cargo check --workspace` after metadata recovers; current audit cannot reach Rust compilation or warning discovery.
