# eyetracker PR-1 Scaffold — Cargo Workspace under pheno-runtime/multimedia/

**Audit:** eyetracker-2026-07-02 (14/14 L4, 100.00%)
**Goal:** Fold eyetracker's 7-crate workspace into `pheno-runtime/multimedia/eyetracker/` as a single Cargo sub-workspace.

## Crate Map (eyetracker upstream)

The eyetracker repository (KooshaPari/eyetracker) has 7 crates in its
workspace. Per `eyetracker-absorption-skeleton.md`:

| Crate | Purpose | Target subdir |
|---|---|---|
| `eyetracker-core` | Camera capture, gaze math | `pheno-runtime/multimedia/eyetracker/core/` |
| `eyetracker-v4l` | Linux V4L2 backend | `pheno-runtime/multimedia/eyetracker/v4l/` |
| `eyetracker-uinput` | Linux uinput mouse driver | `pheno-runtime/multimedia/eyetracker/uinput/` |
| `eyetracker-macos` | macOS AVFoundation backend | `pheno-runtime/multimedia/eyetracker/macos/` |
| `eyetracker-windows` | Windows MediaFoundation backend | `pheno-runtime/multimedia/eyetracker/windows/` |
| `eyetracker-cli` | CLI tool | `pheno-runtime/multimedia/eyetracker/cli/` |
| `eyetracker-bench` | Criterion benches | `pheno-runtime/multimedia/eyetracker/bench/` |

## PR-1 Scaffold (this slice)

This PR-1 scaffolds the workspace structure and module stubs only — no
business-logic code is moved. The PR is the **structural landing site** so
subsequent PRs (PR-2 … PR-7) can move individual crates.

### Files Created

```
pheno-runtime/
└── multimedia/
    └── eyetracker/
        ├── Cargo.toml         # sub-workspace manifest
        ├── README.md          # crate map + provenance
        └── crates/
            ├── core/
            │   ├── Cargo.toml
            │   └── src/lib.rs # stub: re-exports eyetracker-core API surface
            ├── v4l/
            │   ├── Cargo.toml
            │   └── src/lib.rs # stub
            ├── uinput/
            │   ├── Cargo.toml
            │   └── src/lib.rs # stub
            ├── macos/
            │   ├── Cargo.toml
            │   └── src/lib.rs # stub
            ├── windows/
            │   ├── Cargo.toml
            │   └── src/lib.rs # stub
            ├── cli/
            │   ├── Cargo.toml
            │   └── src/main.rs # stub
            └── bench/
                ├── Cargo.toml
                └── benches/gaze_pipeline.rs # criterion bench stub
```

### Sub-Workspace Manifest (`Cargo.toml`)

```toml
[workspace]
resolver = "2"
members = [
    "crates/core",
    "crates/v4l",
    "crates/uinput",
    "crates/macos",
    "crates/windows",
    "crates/cli",
    "crates/bench",
]

[workspace.package]
version = "0.1.0-alpha"
edition = "2021"
license = "MIT OR Apache-2.0"
authors = ["Phenotype Runtime Team"]
repository = "https://github.com/KooshaPari/pheno-runtime"

[workspace.dependencies]
# Filled in subsequent PRs from eyetracker upstream's Cargo.lock
serde = { version = "1", features = ["derive"] }
thiserror = "1"
criterion = { version = "0.5", features = ["html_reports"] }
```

### Core Crate Stub

```rust
// pheno-runtime/multimedia/eyetracker/crates/core/src/lib.rs
//! eyetracker-core — camera capture + gaze math.
//!
//! Source: KooshaPari/eyetracker (PR-1 scaffold).
//! This is a stub; the real implementation lands in PR-2.
#![deny(missing_docs)]
#![warn(rust_2018_idioms)]

/// Re-export surface for the eyetracker-core API.
/// Real exports land in PR-2.
pub fn version() -> &'static str {
    env!("CARGO_PKG_VERSION")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn version_is_set() {
        assert!(!version().is_empty());
    }
}
```

## PR-1 Acceptance Criteria

- [ ] `pheno-runtime/multimedia/eyetracker/Cargo.toml` exists and lists 7 members
- [ ] Each sub-crate has a `Cargo.toml` + `src/lib.rs` (or `src/main.rs` for CLI)
- [ ] `cargo check --workspace` passes (stubs compile)
- [ ] `cargo metadata --no-deps --format-version=1` returns the 7-crate graph
- [ ] README documents the crate map + provenance
- [ ] No business-logic code moved in PR-1 (intentional)

## Follow-up PRs

- **PR-2**: move `eyetracker-core` (real implementation)
- **PR-3**: move `eyetracker-v4l` (Linux V4L2 backend)
- **PR-4**: move `eyetracker-uinput` (Linux uinput driver)
- **PR-5**: move `eyetracker-macos` + `eyetracker-windows` (cross-platform backends)
- **PR-6**: move `eyetracker-cli`
- **PR-7**: move `eyetracker-bench` + CI integration

## Risk

- pheno-runtime already has its own Cargo.toml at the workspace root. PR-1
  must add `multimedia/eyetracker/` as a `[workspace]` member without
  breaking the existing crate resolution.
- `pheno-runtime/Cargo.toml` needs `members = ["crates/*", "multimedia/eyetracker"]`
  or a sub-workspace declaration.

## Provenance

- Source: https://github.com/KooshaPari/eyetracker (public)
- Audit: `phenotype-registry/audits/absorption-justifications/eyetracker-2026-07-02.md` (14/14 L4)
- Skeleton: `phenotype-registry/registry/projects/eyetracker-absorption-skeleton.md`