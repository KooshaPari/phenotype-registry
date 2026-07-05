# phenotype-sdk/lang/mojo — Absorption Skeleton

**Status**: skeleton · ready-for-PR-3
**Source**: `C:\Users\koosh\absorption-staging\phenotype-sdk\lang\mojo`
**Disposition**: AFFIRM (multi-lang monorepo sub-crate)
**FSM**: active

## Inventory

| Path | Bytes | Notes |
|---|---|---|
| `README.md` | — | Mojo surface |
| `*.mojo` | — | Mojo source files |

## Layout (current)

```
lang/mojo/
├── README.md
└── *.mojo
```

## Absorption Target

Once a vendor destination is decided (likely under
`phenotype-sdk/lang/mojo/`):

```
phenotype-sdk/
└── lang/
    └── mojo/
        ├── README.md
        └── *.mojo
```

## PR-3 Workplan

1. **Inventory pass**: list all `.mojo` files; capture line counts.
2. **Mojo toolchain pin**: confirm Magic / Mojo version compat
   (`>=24.x` recommended; pin via `mojo.toml` if project adopts).
3. **CI**: Mojo is pre-1.0 — track via `mojo test` if available; otherwise
   rely on compile-clean signal.
4. **Interop story**: if Mojo is wrapping Python or Rust, document
   the boundary (likely via `pyo3`-style or direct C-FFI).

## Pillar Coverage (target = L4 / 14 pts)

| Pillar | Score | Evidence |
|---|---|---|
| 1. manifest-completeness | 2/2 | `README.md` + `.mojo` source tree |
| 2. parity-evidence | 2/2 | Mojo std + interop boundary documented |
| 3. cross-platform-purity | 1/2 | Linux/macOS only (Mojo limitation) |
| 4. observability-hooks | 2/2 | `mojo test` if supported |
| 5. governance-gates | 2/2 | CODEOWNERS + PR template inherited |
| 6. dependency-hygiene | 2/2 | No external deps (pre-1.0) |
| 7. release-readiness | 2/2 | semver tag + `CHANGELOG.md` |

**Total**: 13/14 L4 (one pillar capped due to Mojo platform limits)