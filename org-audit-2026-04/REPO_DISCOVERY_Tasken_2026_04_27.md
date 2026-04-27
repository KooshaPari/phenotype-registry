# Tasken Repo Discovery - 2026-04-27

## Scope

- Repository: `/Users/kooshapari/CodeProjects/Phenotype/repos/Tasken`
- Mode: audit only, local discovery
- Git state: `## codex/worklog-doc-links...origin/codex/worklog-doc-links [gone]`

## Build State

`timeout 90 cargo check --workspace` completed before the timeout and failed.

Unique error/warning summary:

```text
error: could not compile `taskkit` (lib) due to 16 previous errors; 8 warnings emitted
error: lifetime may not live long enough
error[E0195]: lifetime parameters or bounds on method `execute_async` do not match the trait declaration
error[E0277]: the trait bound `cli::Command: Parser` is not satisfied
error[E0277]: the trait bound `CreateTask: serde::Serialize` is not satisfied
error[E0277]: the trait bound `ListTasks: serde::Serialize` is not satisfied
error[E0432]: unresolved import `crate::domain::Priority`
error[E0432]: unresolved import `super::super::domain::TaskId`
error[E0432]: unresolved import `super::TaskId`
error[E0432]: unresolved imports `crate::domain::Priority`, `crate::domain::RetryPolicy`, `crate::domain::TaskId`
error[E0432]: unresolved imports `domain::RetryPolicy`, `domain::Timeout`
error[E0432]: unresolved imports `super::super::domain::Priority`, `super::super::domain::RetryPolicy`, `super::super::domain::TaskId`
error[E0433]: cannot find module or crate `cron_parser` in this scope
error[E0433]: cannot find module or crate `petgraph` in this scope
error[E0521]: borrowed data escapes outside of method
warning: `taskkit` (lib) generated 8 warnings
warning: unused import: `async_trait::async_trait`
warning: unused import: `crate::domain::errors::TaskError`
warning: unused import: `TaskState`
warning: unused import: `uuid::Uuid`
```

## TODO / FIXME Inventory

- Count: 0 Rust TODO/FIXME/XXX/HACK markers outside `target/` and `.archive/`
- Top examples: none found

## Size And Crates

- Rust LOC: 2,250
- Cargo package count: 1 (`taskkit`)
- Note: the exact requested `cargo metadata --no-deps 2>&1 | jq ... | wc -l`
  pipeline returned `0` because Cargo's compatibility warning is merged into
  the JSON stream before `jq`; the metadata payload itself lists one package.

## Spec Documents

Present:

- `README.md`
- `PRD.md`
- `FUNCTIONAL_REQUIREMENTS.md`
- `PLAN.md`

Absent:

- `ADR.md`

## Top 3 Actionable Items

1. Restore domain exports/import paths for `Priority`, `RetryPolicy`, `TaskId`,
   and `Timeout`, then rerun `cargo check --workspace`.
2. Add or replace missing scheduler dependencies for `cron_parser` and `petgraph`
   so the scheduler modules compile against declared Cargo dependencies.
3. Align the CLI and async executor APIs: derive or wrap `cli::Command` so it
   satisfies `clap::Parser`, add `Serialize` for `CreateTask`/`ListTasks`, and
   fix the `execute_async` lifetime contract.
