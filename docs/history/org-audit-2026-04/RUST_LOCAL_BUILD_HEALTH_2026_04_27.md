# Rust Local Build Health - 2026-04-27

Local-only audit of five foundational Rust workspaces under
`/Users/kooshapari/CodeProjects/Phenotype/repos`.

Command run in each repository:

```bash
cargo check --workspace 2>&1 | grep "^error\|^warning" | sort -u | head -10
```

Each `cargo check --workspace` invocation was capped at 120 seconds. Error and
warning counts below are based on unique lines matching `^error` or `^warning`
after sorting.

| Rank | Repository | Cargo status | Errors | Warnings | Top local signal |
| --- | --- | ---: | ---: | ---: | --- |
| 1 | FocalPoint | 101 | 6 | 14 | `connector-strava` compile failures around `async_instrumented` return types and missing `StravaClient` methods. |
| 2 | hwLedger | 101 | 2 | 0 | Manifest/dependency resolution fails on duplicate key and missing `phenotype-error-core`. |
| 3 | AgilePlus | 101 | 1 | 0 | Build script fingerprint resolution fails for `agileplus-grpc`. |
| 4 | BytePort | 0 | 0 | 0 | Clean under the audited command. |
| 5 | helios-cli | 0 | 0 | 0 | Clean under the audited command. |

## Command Samples

### FocalPoint

```text
error: async_instrumented can only be applied to async fn returning Result<T, E> or anyhow::Result<T>; got: ConnResult < Activity >
error: async_instrumented can only be applied to async fn returning Result<T, E> or anyhow::Result<T>; got: ConnResult < Value >
error: async_instrumented can only be applied to async fn returning Result<T, E> or anyhow::Result<T>; got: ConnResult < Vec < Activity > >
error: could not compile `connector-strava` (lib) due to 5 previous errors; 3 warnings emitted
error[E0599]: no method named `get_athlete` found for struct `tokio::sync::MutexGuard<'_, StravaClient>` in the current scope
error[E0599]: no method named `get_recent_activities` found for struct `tokio::sync::MutexGuard<'_, StravaClient>` in the current scope
warning: `connector-strava` (lib) generated 3 warnings
warning: `focus-always-on` (lib) generated 2 warnings
warning: `focus-connectors-mock-familycontrols` (lib) generated 1 warning (run `cargo fix --lib -p focus-connectors-mock-familycontrols` to apply 1 suggestion)
warning: `focus-connectors` (lib) generated 1 warning
```

### hwLedger

```text
error: duplicate key
error: no matching package named `phenotype-error-core` found
```

### AgilePlus

```text
error: failed to determine package fingerprint for build script for agileplus-grpc v0.1.1 (/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus/crates/agileplus-grpc)
```

### BytePort

```text
No `^error` or `^warning` lines emitted.
```

### helios-cli

```text
No `^error` or `^warning` lines emitted.
```
