# phenoShared Discovery Audit - 2026-04-27

Local-only discovery audit for:
`/Users/kooshapari/CodeProjects/Phenotype/repos/phenoShared`

## Build State

- Git state: `## main...origin/main`
- Command: `timeout 90 cargo check --workspace 2>&1 | grep -E "^error|^warning:" | sort -u | head -20`
- Result: no matching `error` or `warning:` lines were emitted.
- Build summary: workspace check passed the requested error/warning filter inside the 90s timeout.

## TODO/FIXME Markers

- Command: `grep -rn "TODO\|FIXME\|XXX\|HACK" --include="*.rs" . 2>/dev/null | grep -v "/target/\|/.archive/"`
- Count: 0
- Top examples: none found.

## Size And Crate Count

- Rust LOC: 14,465
- Requested crate-count pipeline output: 0
- Actual package count with explicit metadata format: 16

Note: `cargo metadata --no-deps` emits Cargo's compatibility warning before JSON in this checkout, which causes the requested `jq` pipeline to produce zero package names. Re-running with `--format-version 1` reports 16 packages.

## Spec Doc Presence

Present:

- `README.md`
- `PRD.md`
- `ADR.md`
- `FUNCTIONAL_REQUIREMENTS.md`
- `PLAN.md`

Missing: none from the requested list.

## Top 3 Actionable Items

1. Update the local audit command for crate counting to call `cargo metadata --no-deps --format-version 1` so the count reflects the 16 workspace packages.
2. Keep the current zero TODO/FIXME Rust marker baseline enforced in review so new tactical debt stays visible.
3. Add a recurring local `cargo check --workspace` discovery gate to catch warning/error regressions while CI billing remains an external blocker.
