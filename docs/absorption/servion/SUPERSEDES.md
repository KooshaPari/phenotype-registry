# Servion → phenotype-service-registry — Absorption Docket

**Generated:** 2026-07-28
**Authority:** phenotype-registry (registry/disposition-index.json + projects/Servion.json)
**Disposition:** ABSORB (fsm=done, final_classification=B:WORKING)
**Registry row:** staged in `phenotype-registry/registry/disposition-pending-additions-2026-07-28.json` (registry file is FROZEN — apply patch only after explicit unfreeze)
**GitHub source:** `KooshaPari/Servion` (Private, Other, last pushed 2025-03-25, deleted 2026-06-16)
**Local clone:** NONE (source GH-deleted 2026-06-16; no local backup)

---

## State

| Field | Value |
|-------|-------|
| Source repo | `KooshaPari/Servion` |
| Source language | "Other" (per GH API) |
| Source size | 28 KB (per registry) |
| Source state | Deleted from GitHub 2026-06-16 |
| Absorption target | `phenotype-tooling/crates/phenotype-service-registry/` |
| Target size | 28 KB (matches source size — strong absorption signal) |
| Boundary doc | `phenotype-registry/docs/boundary/phenotype-service-registry.md` |
| Intent doc | not present locally |
| Git evidence | `phenotype-tooling` commit `7c5ed3a66` — `feat(service-registry): add phenotype-service-registry crate (migrated from Servion) (#76)` |

---

## Migration works

### What was absorbed

Service registry and discovery for microservices (per projects/Servion.json:11).

### How the absorption was done

A single-purpose PR (#76) added the `phenotype-service-registry` crate to the `phenotype-tooling` workspace, with the explicit commit message "migrated from Servion." This matches the registry entry's claim and the projects-file absorption target. The 28 KB target size closely matches the 28 KB source size, supporting a no-content-loss absorption.

### No-novel-items check

Target `phenotype-service-registry/` contents:
- `Cargo.toml` (Rust crate manifest)
- `src/` (Rust source)

vs. source Servion contents (per projects/Servion.json): service registry & discovery code. Semantic match.

### Regressive branches / commits

None found. Only the migration PR (#76) is recorded in registry for this absorption.

---

## Supersedes chain

| Direction | Relationship |
|-----------|--------------|
| `Servion` **is superseded by** | `phenotype-tooling/crates/phenotype-service-registry/` |
| `phenotype-service-registry/` **supersedes** | `Servion` |
| `Servion` does **NOT** supersede | any other repo (no prior version of this concept absorbed) |
| `phenotype-service-registry/` is **NOT** superseded by | any other repo (still canonical as of 2026-07-28) |

---

## Open items (squash blocked pending approval)

- [ ] Squash confirmation per AGENTS.md (destructive = branch-delete): pending explicit per-repo approval from user.
- [ ] Create `archive/` branch (one tombstone commit: `absorbed → phenotype-tooling/crates/phenotype-service-registry/ on 2026-06-16; see docket URL`).
- [ ] Create `zz-archive/` branch (GH pre-delete mirror — source is GH-deleted, so mirror = empty tombstone).
- [ ] Apply staged patch from `phenotype-registry/registry/disposition-pending-additions-2026-07-28.json` after registry unfreeze.
