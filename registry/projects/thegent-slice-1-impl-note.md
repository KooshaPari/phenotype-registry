# thegent Slice-1 Recon — Thin-Shell Implementation

**Status:** Recon-only skeleton (no code copy)
**Repo:** `KooshaPari/thegent` (1.0 GB monorepo, GitHub only)
**Local mirror:** `C:\Users\koosh\thegent.git` (bare clone, 2026-07-02 snapshot)
**License:** unknown (LICENSE file absent from upstream)
**Slice weight:** < 50 KB on disk (just thin re-exports, no source copy)

## Why thin-shell

The full `thegent` repo is **1 GB** — too large to vendor in-tree under
`registry/projects/`. Instead, slice-1 is a **recon artefact** that:

1. Records upstream provenance (commit SHA, license status, snapshot date).
2. Mirrors only the **README + manifest + CHANGELOG** from upstream.
3. Provides a **stub interface** that the rest of the fleet can call
   against the upstream remote until a proper absorption PR lands.

## Files in this slice

| File | Size | Source |
|---|---|---|
| `thegent-slice-1-README.md` | ~10 KB | `KooshaPari/thegent@<sha>:README.md` (vendored) |
| `thegent-slice-1-manifest.yaml` | ~2 KB | `KooshaPari/thegent@<sha>:Cargo.toml` (manifest digest) |
| `thegent-slice-1-CHANGELOG.md` | ~5 KB | `KooshaPari/thegent@<sha>:CHANGELOG.md` (first 200 lines) |
| `thegent-slice-1-stub.rs` | ~1 KB | hand-written: stub interface module |

## Upstream provenance

- **Repo:** `https://github.com/KooshaPari/thegent`
- **Snapshot SHA:** see `thegent-slice-1-manifest.yaml` `upstream.sha`
- **Snapshot date:** 2026-07-02 (pushed_at per GitHub API)
- **Default branch:** `main`
- **License:** unknown (no LICENSE file detected at snapshot)

## Stub interface (thegent-slice-1-stub.rs)

```rust
//! Thin-shell recon stub for KooshaPari/thegent.
//!
//! This is NOT a working integration. It's a place-holder interface that
//! the fleet can depend on while slice-2..slice-5 (per
//! `thegent-scope-partition.md`) get absorbed in order.
//!
//! To upgrade to a real implementation:
//!   1. Replace this stub with the upstream `thegent` crate vendored
//!      under `Cargo.toml` `[patch.crates-io]` or via path-dep.
//!   2. Update `thegent-slice-1-manifest.yaml` `status` from
//!      `recon-stub` to `vendored`.

#![doc = "Stub interface — see registry/projects/thegent-slice-1-recon-skeleton.md"]

pub const UPSTREAM_REPO: &str = "https://github.com/KooshaPari/thegent";
pub const SNAPSHOT_DATE: &str = "2026-07-02";
pub const STAGE: SliceStage = SliceStage::ReconStub;

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum SliceStage {
    ReconStub,
    Vendored,
    Inlined,
    NativePort,
}

/// Returns upstream repo provenance. Replace with real call once
/// `thegent` is vendored.
pub fn upstream_provenance() -> UpstreamProvenance {
    UpstreamProvenance {
        repo: UPSTREAM_REPO,
        snapshot_date: SNAPSHOT_DATE,
        stage: STAGE,
    }
}

#[derive(Debug, Clone)]
pub struct UpstreamProvenance {
    pub repo: &'static str,
    pub snapshot_date: &'static str,
    pub stage: SliceStage,
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn stage_is_recon_stub() {
        assert_eq!(STAGE, SliceStage::ReconStub);
        assert!(matches!(STAGE, SliceStage::ReconStub));
    }

    #[test]
    fn upstream_provenance_is_stable() {
        let p = upstream_provenance();
        assert_eq!(p.repo, "https://github.com/KooshaPari/thegent");
        assert_eq!(p.snapshot_date, "2026-07-02");
    }
}
```

## Why this approach (alternatives considered)

| Approach | Pros | Cons | Decision |
|---|---|---|---|
| Full vendor (1 GB) | complete | bloats repo by 1 GB; licence-unknown | ✗ |
| Git submodule | tracks upstream | requires network for build; licence-unknown | ✗ |
| Cargo `[patch]` | tracks upstream | requires network at build; licence-unknown | ✗ |
| **Thin-shell recon (this)** | **< 50 KB; safe; provenance-clear** | **requires upgrade to use** | **✓** |

## Upgrade path (slice-2..slice-5)

Per `thegent-scope-partition.md`, the full absorption proceeds in 5 slices.
This stub exists so PR-2..PR-5 can be developed incrementally without
bloating any in-tree crate with the full 1 GB vendored copy.

When a downstream crate wants to call into `thegent`:
1. Add `thegent = { path = ".../thegent-slice-1" }` to Cargo.toml.
2. Use only the symbols exposed by `thegent-slice-1-stub.rs`.
3. When slice-2 lands (per partition), update the stub to re-export
   the real symbols and bump `STAGE` to `SliceStage::Vendored`.

## Audit integration

This slice does NOT add a new audit. The `thegent-2026-07-02` audit
already covers the full upstream at 14/14 L4 (per
`audits/absorption-justifications/thegent-2026-07-02.md`).

## References

- `registry/projects/thegent-scope-partition.md` — 5-slice scope partition
- `audits/absorption-justifications/thegent-2026-07-02.md` — L4 audit
- `projects/thegent.json` — registry project card
- `phenotype-registry/registry/audit-absorption-justification/grade.sh` — grader

---

**Status:** recon-stub · **next:** slice-2 (thegent-cli absorb)