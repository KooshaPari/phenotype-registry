# FocalPoint Discovery Audit - 2026-04-27

Local-only discovery audit for:
`/Users/kooshapari/CodeProjects/Phenotype/repos/FocalPoint`

## Build State

- Git state: `## main...origin/main [behind 7]`
- Existing local changes in audited checkout: generated iOS FFI artifacts modified,
  `crates/focus-ffi/include/focus_ffiFFI.h` modified, and many untracked
  `*.cdx.json` SBOM artifacts across crates, services, scripts, tests, and tooling.
- Command: `timeout 90 cargo check --workspace 2>&1 | grep -E "^error|^warning:" | sort -u | head -20`
- Result: failed inside the 90s timeout; the first 20 filtered lines are compile errors.
- Error summary:
  - `async_instrumented` rejects connector async functions returning `ConnResult<T>`
    instead of `Result<T, E>` or `anyhow::Result<T>`.
  - Missing client methods on `tokio::sync::MutexGuard` block connector crates:
    `get_articles`, `get_highlights`, and `get_reader_data` for Readwise;
    `get_athlete` and `get_recent_activities` for Strava;
    `get_issues` for Linear; `get_me` and `get_pages` for Notion.
  - Cargo reported failed compilation for `connector-linear`, `connector-notion`,
    `connector-readwise`, and `connector-strava`.
- Warning summary: no `^warning:` lines appeared in the requested top-20 filtered
  output; Cargo's error summaries reported `3 warnings emitted` for each failing
  connector crate.

## TODO/FIXME Markers

- Command: `grep -rn "TODO\|FIXME\|XXX\|HACK" --include="*.rs" . 2>/dev/null | grep -v "/target/\|/.archive/"`
- Count: 33
- Top examples:

```text
./tooling/fr-coverage/src/main.rs:87:    // Regex to match `- **FR-XXXX-NNN** — Description.`
./crates/focus-lang/src/lib.rs:622:                // TODO: structured constraint parsing once focus-ir is finalized
./crates/focus-lang/src/lib.rs:852:        asset_hash: "TODO:compute_hash".to_string(),
./crates/focus-connectors/src/signature_verifiers.rs:289:            // TODO: validate X-Goog-Channel-Id references a known watch channel
./crates/connector-fitbit/src/auth.rs:91:        // TODO: Call into iOS keychain via FFI (crates/focus-ffi).
./crates/connector-fitbit/src/auth.rs:97:        // TODO: Call into iOS keychain via FFI.
./crates/connector-fitbit/src/auth.rs:101:        // TODO: Call into iOS keychain via FFI.
./crates/focus-webhook-server/src/handler.rs:207:        // TODO: map Canvas event payload to NormalizedEvents
./crates/focus-webhook-server/src/handler.rs:228:        // TODO: map GCal event payload to NormalizedEvents
./crates/focus-webhook-server/src/main.rs:301:            account_id: uuid::Uuid::nil(), // TODO: extract from config
```

## Size And Crate Count

- Rust LOC, excluding `target` and `.archive`: 65,965
- Requested crate-count pipeline output: 0
- Actual package count with explicit metadata format: 61

Note: `cargo metadata --no-deps` emits Cargo warnings before JSON in this checkout,
so the requested `2>&1 | jq ...` pipeline reports zero packages. Re-running as
`cargo metadata --no-deps --format-version 1 2>/dev/null | jq -r '.packages[].name'`
reports 61 packages.

## Spec Doc Presence

Present:

- `README.md`
- `PRD.md`
- `ADR.md`
- `FUNCTIONAL_REQUIREMENTS.md`
- `PLAN.md`

Missing: none from the requested list.

## Top 3 Actionable Items

1. Fix the connector compile break by aligning `#[async_instrumented]` return-type
   expectations with `ConnResult<T>` or removing the macro where the return contract
   cannot match.
2. Reconcile connector trait/client surfaces for Readwise, Strava, Linear, and Notion
   so the workspace has concrete implementations for the missing methods.
3. Clean up repository hygiene separately: canonical `main` is seven commits behind
   `origin/main`, with pre-existing generated FFI drift and untracked SBOM artifacts.
