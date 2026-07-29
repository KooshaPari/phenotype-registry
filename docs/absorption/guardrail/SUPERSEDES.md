# Guardrail → phenotype-resilience — Absorption Docket

**Generated:** 2026-07-28
**Authority:** phenotype-registry (registry/disposition-index.json + projects/Guardrail.json)
**Disposition:** ABSORB (fsm=done, final_classification=B:WORKING)
**Registry row:** staged in `phenotype-registry/registry/disposition-pending-additions-2026-07-28.json` (registry file is FROZEN — apply patch only after explicit unfreeze)
**GitHub source:** `KooshaPari/Guardrail` (Private, Other, last pushed 2025-03-25, deleted 2026-06-16)
**Local clone:** NONE (source GH-deleted 2026-06-16; no local backup)

---

## State

| Field | Value |
|-------|-------|
| Source repo | `KooshaPari/Guardrail` |
| Source language | "Other" (per GH API) |
| Source size | 48 KB (per registry) |
| Source state | Deleted from GitHub 2026-06-16 |
| Absorption target | `phenotype-tooling/crates/phenotype-resilience/` |
| Target size | 48 KB (matches source size — strong absorption signal) |
| Boundary doc | `phenotype-registry/docs/boundary/phenotype-resilience.md` |
| Intent doc | `phenotype-registry/docs/intent/phenotype-resilience.md` |
| Git evidence | `phenotype-tooling` commit `a298f2355` — `feat(resilience): add phenotype-resilience workspace crate (#72)` |

---

## Migration works

### What was absorbed

Rate limiting, circuit breaking, and bulkhead isolation (per projects/Guardrail.json:11).

### How the absorption was done

A single-purpose PR (#72) added the `phenotype-resilience` crate to the `phenotype-tooling` workspace. The 48 KB target size matches the 48 KB source size, supporting a no-content-loss absorption. Both `boundary/` and `intent/` docs exist for `phenotype-resilience` — indicating this absorption was planned and documented, not opportunistic.

### No-novel-items check

Target `phenotype-resilience/` contents:
- `Cargo.toml` (Rust crate manifest)
- `src/` (Rust source)

vs. source Guardrail contents (per projects/Guardrail.json): rate limiting + circuit breaking + bulkhead isolation. Semantic match.

### Regressive branches / commits

None found. Only the migration PR (#72) is recorded in registry for this absorption.

---

## Supersedes chain

| Direction | Relationship |
|-----------|--------------|
| `Guardrail` **is superseded by** | `phenotype-tooling/crates/phenotype-resilience/` |
| `phenotype-resilience/` **supersedes** | `Guardrail` |
| `Guardrail` does **NOT** supersede | any other repo (no prior version of this concept absorbed) |
| `phenotype-resilience/` is **NOT** superseded by | any other repo (still canonical as of 2026-07-28) |

---

## Open items (squash blocked pending approval)

- [ ] Squash confirmation per AGENTS.md (destructive = branch-delete): pending explicit per-repo approval from user.
- [ ] Create `archive/` branch (one tombstone commit: `absorbed → phenotype-tooling/crates/phenotype-resilience/ on 2026-06-16; see docket URL`).
- [ ] Create `zz-archive/` branch (GH pre-delete mirror — source is GH-deleted, so mirror = empty tombstone).
- [ ] Apply staged patch from `phenotype-registry/registry/disposition-pending-additions-2026-07-28.json` after registry unfreeze.
