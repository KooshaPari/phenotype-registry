# PhenoKits Discovery Audit - 2026-04-27

Local-only discovery audit for:
`/Users/kooshapari/CodeProjects/Phenotype/repos/PhenoKits`

## Build State

- Git state: `## chore/gitignore-worktrees-2026-04-26...origin/chore/gitignore-worktrees-2026-04-26`
- Existing local changes in audited checkout:

```text
 m HexaKit
?? libs/python/pheno_adapters/
```

- Command: `timeout 60 cargo check --workspace 2>&1 | grep -E "^error|^warning:" | sort -u | head -15`
- Result:

```text
error: manifest path `/Users/kooshapari/CodeProjects/Phenotype/repos/PhenoKits` contains no package: The manifest is virtual, and the workspace has no members.
```

- Build summary: workspace check did not reach crate compilation because the root
  `Cargo.toml` is a virtual workspace with `members = []`.

## TODO/FIXME Markers

- Command: `grep -rn "TODO\|FIXME\|XXX\|HACK" --include="*.rs" . 2>/dev/null | grep -v "/target/\|/.archive/" | head -20`
- Top examples:

```text
./HexaKit/crates/phenotype-security-aggregator/src/lib.rs:210:        // TODO: Parse JSON response into SecurityAlert structs
./HexaKit/crates/phenotype-xdd-lib/src/mutation/mod.rs:142:            .map(|f| f.lines_executed as f64 / 100.0) // TODO: actual LOC
./HexaKit/crates/phenotype-xdd-lib/src/mutation/mod.rs:168:            .fold((0, 0), |(t, e), (_, exec)| (t + 100, e + exec)); // TODO: actual LOC
./HexaKit/crates/phenotype-xdd-lib/src/mutation/mod.rs:199:        // Coverage calculation uses TODO LOC, so just verify no panic
./HexaKit/agileplus/crates/agileplus-domain/src/credentials/file.rs:34:    /// TODO (SECURITY): Implement full AES-256-GCM + Argon2id encryption:
./HexaKit/agileplus/crates/agileplus-dashboard/src/process_detector.rs:107:    // Look for task identifiers like WP13, FR-XXX, etc. in command line
./hexagon/templates/rust/src/infrastructure/adapters/repository.rs:19:        // TODO: Implement SQLx query
```

## Size And Crate Count

- Rust LOC, excluding `target` and `.archive`: 99,445
- Requested crate-count pipeline output: 0
- Root manifest package state: virtual workspace with no members
- Nearby nested manifests:
  - `./HexaKit/Cargo.toml`
  - `./HexaKit/agileplus-agents/Cargo.toml`
  - `./HexaKit/forgecode-fork/Cargo.toml`
  - `./HexaKit/rust/Cargo.toml`
  - `./templates/clean-rust/Cargo.toml`

## Spec Doc Presence

Present:

- `README.md`
- `HexaKit/README.md`
- `HexaKit/ADR.md`
- `HexaKit/FUNCTIONAL_REQUIREMENTS.md`
- `HexaKit/PLAN.md`
- `HexaKit/PRD.md`
- `hexagon/ADR.md`
- `hexagon/PLAN.md`
- `hexagon/PRD.md`

## Top 3 Actionable Items

1. Decide whether `PhenoKits` should remain an empty Rust workspace wrapper or
   stop advertising root-level `cargo check --workspace` as a health signal.
2. Audit the embedded `HexaKit` subtree separately: it contains most of the Rust
   LOC and the visible TODO/security TODO markers.
3. Resolve checkout hygiene before deeper audit work: the audited branch has a
   modified `HexaKit` entry and an untracked `libs/python/pheno_adapters/` tree.
