# Civis PBR Phase 3 — Triplanar WGSL + Greedy Atlas Skeleton

> **Status:** delivered (commit `ffef66c` on `feat/civis-pbr-phase3-2026-07-04`, pushed)
> **Substrate repo:** `Civis` (`main` ← `feat/civis-pbr-phase3-2026-07-04`)
> **Source tree:** `C:\Users\koosh\Civis\`
> **Date:** 2026-07-04

---

## 1. Functional requirements tracked

| FR ID | Title | Status |
|---|---|---|
| FR-CIV-PBR-001..009 | Phase 1 + 2 substrate (tonemap, color grading, volumetric fog, SSR, etc.) | ✅ landed on `main` |
| **FR-CIV-PBR-010** | Triplanar PBR WGSL shader (world-space 3-axis projection) | ✅ landed on `feat/civis-pbr-phase3-2026-07-04` |
| **FR-CIV-PBR-011** | Greedy atlas packer (pure-Rust, std-only, shelf-bin) | ✅ landed on `feat/civis-pbr-phase3-2026-07-04` |

---

## 2. Verified substrate (post-commit)

| File | Lines | Role |
|---|---|---|
| `Civis/crates/voxel/shaders/pbr_triplanar.wgsl` | 167 | WGSL fragment + vertex shaders; triplanar blend via `pow(|n|, sharpness)`; three axis-aligned UV projections (`wpos.zy`, `wpos.xz`, `wpos.xy`); channels for albedo, normal (re-oriented per axis), ORM |
| `Civis/crates/voxel/src/atlas/gpu_atlas.rs` | 680 | `GreedyAtlasPacker` (shelf-bin, `pack_to_png` debug helper, 4+ unit tests) |
| `Civis/crates/voxel/src/pbr/mod.rs` | — | `TRIPLANAR_WGSL_PATH = "shaders/pbr_triplanar.wgsl"` constant + `pub use` hub |
| `Civis/crates/voxel/src/pbr/triplanar_pipeline.rs` | 342 | `TriplanarPbrMaterial` (wgsl mirror) + pipeline descriptors |
| `Civis/crates/voxel/src/pbr/greedy_atlas.rs` | — | CPU-side `GreedyAtlas` matching the GPU packer |
| `Civis/crates/voxel/src/lib.rs` | +2 | additive `pub mod atlas;` + `pub mod pbr;` with Phase-3 doc comment |
| `Civis/crates/voxel/Cargo.toml` | +4 | `[[bench]] pbr_greedy_atlas` entry |
| `Civis/crates/voxel/src/material_pbr.rs` | +1 | `MaterialCatalog::material_count()` (additive) |
| `Civis/CHANGELOG.md` | +14 | `[Unreleased]` Phase-3 section (FR-CIV-PBR-010/011) |

---

## 3. Wiring invariants verified

- `lib.rs` adds `pub mod atlas;` and `pub mod pbr;` — additive only; existing `material_pbr` re-exports unchanged.
- `Cargo.toml` `[[bench]] pbr_greedy_atlas` references the existing `atlas/greedy_atlas` benchmark fixture; no new deps.
- `CHANGELOG.md` entries use the `[Unreleased]` anchor — no released-version edits.
- WGSL struct `PbrMaterialUniforms` mirrors `TriplanarPbrMaterial` (Rust) field-for-field; bind-group 0 = uniform, bind-group 1 = texture samplers.
- Atlas UV channel (`atlas_uv_channel`) referenced in substrate vertex pipeline; WGSL `world_pos` input is world-space (not UV-space), so the channel value is composed in the Bevy adapter (`pbr_pipeline.rs`, FR-CIV-PBR-005 hook).

---

## 4. Build + test gates (next step)

```bash
cd "C:\Users\koosh\Civis"
cargo check -p voxel
cargo test  -p voxel --lib atlas::        # greedy_atlas tests
cargo test  -p voxel --lib pbr::          # triplanar_pipeline tests
cargo bench -p voxel pbr_greedy_atlas     # perf baseline
```

All four must pass before merging `feat/civis-pbr-phase3-2026-07-04` → `main`. No expected blockers — all changes are additive over FR-CIV-PBR-001..009 substrate.

---

## 5. Decision

**Land on `main` after CI green.** The Phase-3 substrate is a single-branch delivery with 9 additive files; no migration risk; no public-API breakage (existing `material_pbr` exports preserved).
