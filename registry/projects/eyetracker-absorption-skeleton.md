# eyetracker Absorption Skeleton → pheno-runtime multimedia crate

> **Status:** skeleton / paper exercise
> **Source tree:** `C:\Users\koosh\eyetracker\` (local) + `KooshaPari/eyetracker` (remote)
> **Destination:** `pheno-runtime/crates/phenotype-multimedia/` (new sub-crate)
> **Date:** 2026-07-04

---

## 1. Source inventory (verified)

| Path | Type | Notes |
|---|---|---|
| `Cargo.toml` | workspace root | 7-crate workspace, version `0.1.0-alpha` |
| `crates/eyetracker-core/` | lib | core detection primitives |
| `crates/eyetracker-{over,under,prefix,phase,fusion,gaze}/` | libs (5) | signal-processing pipeline |
| `.github/workflows/` | CI | 9+ workflows present |
| `README.md` | docs | (to be merged) |

Total: **7 crates**, ~0.4 MB, last commit 2026-07-02T22:21Z, FSM=active, disp=AFFIRM.

---

## 2. Verdict

**Fold into `pheno-runtime` as `phenotype-multimedia` sub-crate.** The 7-crate workspace maps cleanly:

- `eyetracker-core` → `phenotype-multimedia/src/lib.rs` (re-export hub)
- 5 signal-processing crates → `phenotype-multimedia/src/{calibration,filter,tracking,fusion,gaze}.rs`
- one remaining crate (gazeto-world projection?) → `phenotype-multimedia/src/project.rs`

Rationale: eyetracker is a leaf multimedia input — same category as future webcam/audio crates. Grouping them under one multimedia crate keeps `pheno-runtime` monolith-free while avoiding the proliferation of single-purpose repos.

---

## 3. Landing matrix

| Source | Destination |
|---|---|
| `crates/eyetracker-core/` | `pheno-runtime/crates/phenotype-multimedia/src/lib.rs` + `core.rs` |
| `crates/eyetracker-over/` | `pheno-runtime/crates/phenotype-multimedia/src/oversample.rs` |
| `crates/eyetracker-under/` | `.../undersample.rs` |
| `crates/eyetracker-prefix/` | `.../prefix.rs` |
| `crates/eyetracker-phase/` | `.../phase.rs` |
| `crates/eyetracker-fusion/` | `.../fusion.rs` |
| `crates/eyetracker-gaze/` | `.../gaze.rs` |
| 9 `.github/workflows/*` | merge into `pheno-runtime/.github/workflows/` (dedup) |
| `README.md` | fold into `pheno-runtime/docs/phenoruntime/multimedia.md` |

---

## 4. Skeleton

```text
pheno-runtime/crates/phenotype-multimedia/
├── Cargo.toml          # inherits pheno-runtime workspace; depends on phenotype-iter
├── src/
│   ├── lib.rs          # pub use core::* + re-exports
│   ├── core.rs         # DetectionEvent, Sample traits
│   ├── oversample.rs
│   ├── undersample.rs
│   ├── prefix.rs
│   ├── phase.rs
│   ├── fusion.rs
│   ├── gaze.rs
│   └── project.rs      # screen → world
└── tests/
    └── integration.rs
```

---

## 5. Phase plan (1 PR)

1. Create `phenotype-multimedia` sub-crate under `pheno-runtime/crates/`.
2. `git subtree add` for each of the 7 source crates (history preserved).
3. Re-export hub pattern: `lib.rs` mirrors `phenotype-core`'s pattern.
4. `cargo check --workspace && cargo test -p phenotype-multimedia`.
5. Deprecate `KooshaPari/eyetracker` (set `archived = true` post-merge).

**Open questions:**
- Confirm `phenotype-iter` is the right dep (vs `phenotype-time` for timestamps).
- Eyetracker release version `0.1.0-alpha` → bump to `0.1.0` to match `pheno-runtime` convention.
- Decide whether to land on `main` directly (it is FSM=active, so yes).

---

## 6. Decision

**Land in 1 PR — `feat/eyetracker-into-phenotype-multimedia`** under `pheno-runtime`.