# Repo Discovery: PhenoPlugins

Date: 2026-04-27
Scope: Local-only audit of `/Users/kooshapari/CodeProjects/Phenotype/repos/PhenoPlugins`

## Git State

```text
## main...origin/main [behind 3]
 M Cargo.toml
 M crates/pheno-plugin-vessel/.agileplus/worklog.md
 M crates/pheno-plugin-vessel/worklog.md
 M docs/worklogs/README.md
?? crates/pheno-plugin-core/tests/
?? deny.toml
?? docs/FUNCTIONAL_REQUIREMENTS.md
?? worklog.md
```

## Build State

Command:

```bash
timeout 90 cargo check --workspace 2>&1 | grep -E "^error|^warning:" | sort -u | head -20
```

Result:

```text
error: failed to load manifest for workspace member `/Users/kooshapari/CodeProjects/Phenotype/repos/PhenoPlugins/crates/pheno-plugin-core`
```

Expanded local check shows the missing manifest:

```text
failed to read `/Users/kooshapari/CodeProjects/Phenotype/repos/PhenoPlugins/crates/pheno-plugin-core/Cargo.toml`
No such file or directory (os error 2)
```

Warnings: none reached before manifest load failure.

## TODO/FIXME Audit

Count: 0 Rust TODO/FIXME/XXX/HACK markers outside `target/` and `.archive/`.

Top examples: none found.

## Size And Package Inventory

Rust LOC:

```text
3479 total
```

Crate count from requested metadata command:

```text
0
```

Note: `cargo metadata --no-deps` fails because the workspace references missing crate
manifests. The root workspace declares four members, but only
`crates/pheno-plugin-vessel/Cargo.toml` exists locally.

## Spec Doc Presence

Present at repo root:

```text
PLAN.md
README.md
```

Absent at repo root: `PRD.md`, `ADR.md`, `FUNCTIONAL_REQUIREMENTS.md`.

## Top 3 Actionable Items

1. Restore or remove the missing workspace members referenced by root `Cargo.toml`:
   `pheno-plugin-core`, `pheno-plugin-git`, and `pheno-plugin-sqlite`.
2. Re-run `cargo metadata --no-deps` and `cargo check --workspace` after the workspace
   manifest matches the local crate tree.
3. Reconcile the dirty local audit/worklog state before feature work, especially the
   modified `Cargo.toml`, untracked `deny.toml`, and untracked `crates/pheno-plugin-core/tests/`.
