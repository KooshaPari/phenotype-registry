# Eyetracker PR-1 — Cargo Workspace Scaffold under pheno-runtime/multimedia/

**Repo**: `KooshaPari/eyetracker` (7-crate workspace)
**Target**: `phenotype-registry/lang/rust/packages/pheno-runtime/crates/pheno-multimedia/`
**Branch**: `feat/eyetracker-pr1-cargo-scaffold-2026-07-04`
**Estimated**: 4–6 h

## Source Inventory (verified)

| Sub-crate | LOC est. | Purpose | Target module |
|---|---|---|---|
| `eyetracker-core` | core | Core types: EyeSample, GazePoint, Frame | `pheno-multimedia::core` |
| `eyetracker-camera` | capture | Camera capture backends (V4L2, MSMF) | `pheno-multimedia::camera` |
| `eyetracker-inference` | inference | Inference engine (model load + run) | `pheno-multimedia::inference` |
| `eyetracker-math` | math | Math utilities (projections, filters) | `pheno-multimedia::math` |
| `eyetracker-domain` | domain | Domain types (sessions, calibrations) | `pheno-multimedia::domain` |
| `eyetracker-ffi` | ffi | FFI bindings (C-ABI for SDK consumers) | `pheno-multimedia::ffi` |
| `eyetracker-cli` | cli | CLI entry-point (binary) | `pheno-multimedia::bin/eyetracker` |

## Scaffold Plan

### PR-1.1: Workspace metadata

Create `crates/pheno-multimedia/Cargo.toml`:

```toml
[package]
name = "pheno-multimedia"
version = "0.1.0"
edition = "2021"
license = "MIT OR Apache-2.0"
description = "Multimedia subsystem (camera, inference, math) for the pheno-runtime"
repository = "https://github.com/KooshaPari/phenotype-sdk"

[dependencies]
# external
tokio = { version = "1", features = ["full"] }
serde = { version = "1", features = ["derive"] }
thiserror = "1"
anyhow = "1"
tracing = "0.1"

# internal (will be wired in PR-2 once crate splits land)
pheno-runtime = { path = "../pheno-runtime" }

[features]
default = []
v4l2 = ["dep:libv4l2-sys"]  # linux camera backend
msmf = []  # windows camera backend (placeholder)
```

### PR-1.2: Module stubs

Create skeleton `src/lib.rs`:

```rust
//! pheno-multimedia — Camera capture, gaze inference, and related math.
//!
//! Absorbed from KooshaPari/eyetracker (7-crate workspace) as part of the
//! pheno-runtime multimedia subsystem. See:
//! `phenotype-registry/registry/projects/eyetracker-absorption-skeleton.md`

#![warn(missing_docs)]
#![warn(rust_2018_idioms)]

pub mod camera;
pub mod core;
pub mod domain;
pub mod ffi;
pub mod inference;
pub mod math;

pub use core::{EyeSample, GazePoint, Frame};
```

Create empty module files (`src/{camera,core,domain,ffi,inference,math}.rs`) each containing:

```rust
//! <module> — absorbed from eyetracker-<crate>; see PR-2 for full port.
#![allow(unused_imports)]
```

### PR-1.3: Workspace registration

Add to `lang/rust/packages/pheno-runtime/Cargo.toml` `[workspace.members]`:

```toml
members = [
    ".",
    "crates/pheno-minio",
    "crates/pheno-nats",
    "crates/phenotype-llm",
    "crates/phenotype-mcp-server",
    "crates/phenotype-surrealdb",
    "crates/pheno-multimedia",   # ← new in PR-1
]
```

### PR-1.4: Minimal example/test

Add `crates/pheno-multimedia/examples/basic_capture.rs`:

```rust
//! Smoke test: open a fake frame and run gaze inference.
//! Real device integration arrives in PR-2.

use pheno_multimedia::{core::Frame, core::EyeSample};

fn main() {
    let frame = Frame::placeholder(640, 480);
    let samples = vec![EyeSample::placeholder()];
    println!("frame={}x{}, samples={}", frame.width, frame.height, samples.len());
}
```

Add `crates/pheno-multimedia/tests/smoke.rs`:

```rust
use pheno_multimedia::core::{EyeSample, Frame};

#[test]
fn placeholder_frame_dimensions() {
    let f = Frame::placeholder(640, 480);
    assert_eq!(f.width, 640);
    assert_eq!(f.height, 480);
}

#[test]
fn placeholder_eye_sample() {
    let s = EyeSample::placeholder();
    assert!(s.x.is_finite());
    assert!(s.y.is_finite());
}
```

## PR-1 Success Criteria

- [ ] `cargo build -p pheno-multimedia` succeeds
- [ ] `cargo test -p pheno-multimedia` runs the 2 smoke tests
- [ ] `cargo run -p pheno-multimedia --example basic_capture` prints expected output
- [ ] No `#[allow(dead_code)]` on the public API surface
- [ ] `pheno-multimedia` appears in workspace member list
- [ ] CI green on Linux + Windows runners

## PR-1 Out-of-Scope

- Real camera backend (V4L2/MSMF) → PR-2
- Inference model loader → PR-2
- FFI C-ABI binding → PR-3
- CLI binary port → PR-3
- Historical git/fixture data → PR-3 (deferred)

## Risk Notes

- **Risk 1**: eyetracker may have its own dependencies that conflict with pheno-runtime. Mitigate by adding a `[patch.crates-io]` block in the workspace `Cargo.toml` if conflicts arise.
- **Risk 2**: 7-crate workspace may include internal cross-references that break when split. Mitigate by mapping each sub-crate to a flat module first (PR-1), then re-introducing crate boundaries only if the public-API surface demands it (PR-2).
- **Risk 3**: License headers must be preserved per-eyetracker-license. Verify the eyetracker repo LICENSE before squashing history.

## Verification Commands

```bash
# From phenotype-sdk root:
cd lang/rust/packages/pheno-runtime
cargo build -p pheno-multimedia
cargo test -p pheno-multimedia
cargo run -p pheno-multimedia --example basic_capture

# Workspace-level smoke:
cd ../../..
cargo build --workspace
cargo test --workspace
```