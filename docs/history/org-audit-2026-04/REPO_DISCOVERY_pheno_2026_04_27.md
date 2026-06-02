# pheno Discovery Audit - 2026-04-27

Local-only discovery audit for:
`/Users/kooshapari/CodeProjects/Phenotype/repos/pheno`

## Build State

- Git state: `## pheno/ci/repair-sast-full...origin/pheno/ci/repair-sast-full`
- Command: `timeout 60 cargo check --workspace 2>&1 | grep -E "^error|^warning:" | sort -u | head -15`
- Result: no matching `error` or `warning:` lines were emitted.
- Build summary: the requested warning/error filter produced no output within the 60s command path.

## TODO/FIXME Markers

- Command: `grep -rn "TODO\|FIXME\|XXX\|HACK" --include="*.rs" . 2>/dev/null | grep -v "/target/\|/.archive/" | head -20`
- Count: 3
- Top examples:

```text
./crates/phenotype-security-aggregator/src/lib.rs:203:        // TODO: Parse JSON response into SecurityAlert structs
./agileplus/crates/agileplus-domain/src/credentials/file.rs:34:    /// TODO (SECURITY): Implement full AES-256-GCM + Argon2id encryption:
./agileplus/crates/agileplus-dashboard/src/process_detector.rs:107:    // Look for task identifiers like WP13, FR-XXX, etc. in command line
```

## Size And Crate Count

- Rust LOC outside `target` and `.archive`: 160,256
- Requested crate-count pipeline output: 0
- Actual package count with explicit metadata format: 21

Note: the requested `cargo metadata --no-deps 2>&1 | jq -r '.packages[].name' 2>/dev/null | wc -l`
pipeline returned zero package names. Re-running locally with `--format-version 1` reports 21
packages.

## Spec Doc Presence

Present:

- `README.md`
- `PRD.md`
- `ADR.md`
- `FUNCTIONAL_REQUIREMENTS.md`
- `PLAN.md`

Missing: none from the checked root spec docs.

## Top 3 Actionable Items

1. Update the local crate-count discovery command to use `cargo metadata --no-deps --format-version 1` so the package count reflects the 21-package workspace.
2. Triage the security-sensitive TODO in `agileplus/crates/agileplus-domain/src/credentials/file.rs` before broader hygiene cleanup.
3. Confirm whether the embedded `agileplus/` Rust crates are intentional members of the pheno audit scope, since they account for two of the three Rust TODO markers found.
