# Repo Discovery: Eidolon (2026-04-27)

## Scope

- Repository: `/Users/kooshapari/CodeProjects/Phenotype/repos/Eidolon`
- Mode: local-only discovery audit
- Requested validation window: `timeout 60 cargo check --workspace`

## Git State

```text
## main...origin/main [behind 2]
```

## Build State

Requested filtered command:

```bash
timeout 60 cargo check --workspace 2>&1 | grep -E "^error|^warning:" | sort -u | head -15
```

Filtered result:

```text
warning: `eidolon-core` (lib) generated 1 warning (run `cargo fix --lib -p eidolon-core` to apply 1 suggestion)
warning: `eidolon-desktop` (lib) generated 1 warning (run `cargo fix --lib -p eidolon-desktop` to apply 1 suggestion)
warning: unused import: `async_trait::async_trait`
```

No matching `error` lines were emitted.

## TODO / FIXME / XXX / HACK

- Count: 9 in Rust files outside `target/` and `.archive/`.
- Top examples:
  - `crates/eidolon-sandbox/src/docker/mod.rs:44` - Docker orchestrator integration TODO.
  - `crates/eidolon-sandbox/src/lib.rs:29` - nanoVMs / Docker / KVM introspection TODO.
  - `crates/eidolon-mobile/src/native/mod.rs:25` - iOS XCTest adapter TODO.
  - `crates/eidolon-mobile/src/native/mod.rs:26` - Android UiAutomator adapter TODO.
  - `crates/eidolon-desktop/src/lib.rs:24` - native display API integration TODO.

## Size and Crates

- Rust LOC: 515 total.
- Rust files scanned: 12.
- Requested crate-count pipeline output: 0.
- Direct metadata diagnostic: 4 packages: `eidolon-core`, `eidolon-desktop`,
  `eidolon-mobile`, `eidolon-sandbox`.

Note: the exact requested crate-count pipeline combines stderr into stdout before
`jq`, so Cargo's compatibility warning makes the stream non-JSON and the pipeline
counts zero packages. Direct `cargo metadata --no-deps --format-version 1` output
lists four workspace packages.

## Top 3 Actionable Items

1. Remove the unused `async_trait::async_trait` import reported by `cargo check`
   in `eidolon-core` and the related warning emitted for `eidolon-desktop`.
2. Replace or route the nine Rust TODO placeholders for sandbox, mobile, and
   desktop integrations before treating the crates as implementation-complete.
3. Update audit scripts to use `cargo metadata --no-deps --format-version 1 2>/dev/null`
   before piping to `jq`, otherwise valid Rust workspaces can report zero packages.
