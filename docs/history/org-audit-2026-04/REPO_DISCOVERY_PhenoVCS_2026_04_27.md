# Repo Discovery: PhenoVCS (2026-04-27)

## Scope

- Repository: `/Users/kooshapari/CodeProjects/Phenotype/repos/PhenoVCS`
- Mode: local-only discovery audit
- Requested validation window: `timeout 60 cargo check --workspace`

## Git State

```text
## chore/sync-state...origin/chore/sync-state
 M SPEC.md
 M crates/pheno-vcs-core/Cargo.toml
 M docs/worklogs/README.md
?? .clippy.toml
?? .editorconfig
?? .github/dependabot.yml
?? .github/workflows/traceability.yml
?? .phenotype/
?? .pre-commit-config.yaml
?? ADR.md
?? ARCHITECTURE.md
?? CHARTER.md
?? GOVERNANCE.md
?? PRD.md
?? SECURITY.md
?? codecov.yml
?? deny.toml
?? docs/FUNCTIONAL_REQUIREMENTS.md
?? docs/adr/
?? docs/reference/
?? docs/research/
?? rustfmt.toml
?? specs/
?? tests/
?? validate_governance.py
?? worklog.md
```

## Build State

Requested filtered command:

```bash
timeout 60 cargo check --workspace 2>&1 | grep -E "^error|^warning:" | sort -u | head -15
```

Filtered result: no `error` or `warning:` lines were emitted.

## TODO / FIXME / XXX / HACK

- Count: 0 in Rust files outside `target/` and `.archive/`.
- Top examples: none found.

## Size and Crates

- Rust LOC: 9 total.
- Rust files scanned: 2.
- Requested crate-count pipeline output: 0.
- Direct metadata diagnostic: 1 package, `pheno-vcs-core`.

Note: the exact requested crate-count pipeline combines stderr into stdout before
`jq`, so Cargo's compatibility warning makes the stream non-JSON and the pipeline
counts zero packages. Direct `cargo metadata --no-deps` output lists one workspace
package.

## Top 3 Actionable Items

1. Decide whether the large untracked governance/spec scaffold in the PhenoVCS
   checkout is intended to be committed, routed elsewhere, or cleaned up.
2. Re-run crate counting with `cargo metadata --no-deps --format-version 1 2>/dev/null`
   for machine-readable audit scripts.
3. Expand the Rust implementation beyond the current 9-line stub before treating
   `cargo check` success as meaningful implementation health.
