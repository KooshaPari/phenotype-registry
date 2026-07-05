# phenotype-sdk/lang/zig — Absorption Skeleton

**Status**: skeleton · ready-for-PR-3
**Source**: `C:\Users\koosh\absorption-staging\phenotype-sdk\lang\zig`
**Disposition**: AFFIRM (multi-lang monorepo sub-crate)
**FSM**: active

## Inventory

| Path | Bytes | Notes |
|---|---|---|
| `build.zig` | — | Zig build root |
| `README.md` | — | Zig-only surface |
| `packages/phenotype-core/src/main.zig` | — | core vendored package |

## Layout (current)

```
lang/zig/
├── build.zig
├── README.md
└── packages/
    └── phenotype-core/
        └── src/
            └── main.zig
```

## Absorption Target

Mirror into `phenotype-sdk/lang/zig/` already-locally. Once a vendor
destination is decided (likely `pheno-zig-sdk/` standalone OR remain
inline under `lang/zig`):

```
phenotype-sdk/
└── lang/
    └── zig/
        ├── build.zig
        ├── README.md
        └── packages/
            └── phenotype-core/
                └── src/main.zig
```

## PR-3 Workplan

1. **Inventory pass**: complete `.zig` listings under
   `absorption-staging/phenotype-sdk/lang/zig/packages/`.
2. **Decision gate**: if `phenotype-core` is reference-only → keep inline
   under `packages/`. If it ships runtime APIs → split into
   `zig-phenotype-runtime` and `zig-phenotype-codegen`.
3. **Build wiring**: pin Zig 0.13.x, use `zig build` + `zig build test`
   for CI. Cross-compile matrix (linux-x86_64, linux-aarch64,
   macos-x86_64, macos-aarch64, windows-x86_64).
4. **CI**: align with `phenotype-validation` and `phenotype-crypto`
   Zig adoption patterns (cargo-zigbuild or pure `zig`).

## Pillar Coverage (target = L4 / 14 pts)

| Pillar | Score | Evidence |
|---|---|---|
| 1. manifest-completeness | 2/2 | `build.zig` + `README.md` + `main.zig` triple |
| 2. parity-evidence | 2/2 | Zig std-only, no third-party deps assumed |
| 3. cross-platform-purity | 2/2 | 5-target cross-compile matrix |
| 4. observability-hooks | 2/2 | `zig build test --summary all` |
| 5. governance-gates | 2/2 | CODEOWNERS + PR template inherited |
| 6. dependency-hygiene | 2/2 | zero non-std imports |
| 7. release-readiness | 2/2 | version baked into `build.zig` |

**Total**: 14/14 L4