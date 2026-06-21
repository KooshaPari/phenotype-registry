# phenotype-cache-adapter - archive-if-unused verdict (P4 Lane D)

**Date:** 2026-06-19  
**Disposition:** ARCHIVE-IF-UNUSED (stub retained)  
**ADR:** ADR-ECO-014 (phenoShared interim staging)  
**Registry task:** Phase 4 backlog #48

## Verdict

**Do not implement** the hexagonal `phenotype-cache-adapter` scaffold. Retain the minimal compiling stub (`CacheAdapter` newtype in `crates/phenotype-cache-adapter/src/lib.rs`) for HexaKit API parity only.

| Signal | Finding |
|--------|---------|
| Fleet consumers | Single git-pin consumer: HexaKit `phenotype-cache-adapter` workspace dep (Wave 12) |
| Hexagonal submodules | `application/`, `adapters/`, `domain/` - empty module trees; 38 compile errors per `PLAN.md` |
| Canonical cache impl | `stashly` (ADR-ECO-001) + `phenotype-resilience` terminal owner |
| BLOCK-C audit | Items #3, #19, #44 recommend DELETE/SHRINK - superseded by this verdict |

## Rationale

1. No DOMAIN_ROLES terminal owner requires a standalone cache-adapter crate.
2. `CacheAdapter` type is re-exported via HexaKit `phenotype-core` for backward compatibility only.
3. Full two-tier LRU + DashMap implementation belongs in `stashly` / resilience lane, not phenoShared interim.
4. Implementing 38-error hexagonal scaffold would duplicate `stashly` without fleet demand.

## Retained surface

```rust
// crates/phenotype-cache-adapter/src/lib.rs - stub only
pub struct CacheAdapter;
impl CacheAdapter { pub fn new() -> Self { Self } }
```

Hexagonal submodule directories remain **unwired** (no `mod` declarations). Do not expand.

## Terminal target

| Phase | Owner | Action |
|-------|-------|--------|
| P4 (now) | phenoShared | Stub retained; this verdict merged |
| P5+ | HexaKit / phenotype-rust-sdk | Repoint `CacheAdapter` re-export to `stashly` or inline type; drop git pin |

## References

- [BLOCK-C-AUDIT.md](../audit/BLOCK-C-AUDIT.md) items #3, #19, #44
- [HEXAKIT_API_PARITY.md](../HEXAKIT_API_PARITY.md) - `CacheAdapter` mapping
- [phenoshared-p4-checkpoint.md](https://github.com/KooshaPari/phenotype-registry/blob/main/docs/disposition/phenoshared-p4-checkpoint.md) - fleet zero-dep audit
