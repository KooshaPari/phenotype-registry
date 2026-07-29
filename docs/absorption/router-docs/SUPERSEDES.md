# router-docs → OmniRoute/docs/research/archive/router-docs — Absorption Docket

**Generated:** 2026-07-28
**Authority:** phenotype-registry (registry/disposition-index.json + projects/router-docs.json)
**Disposition:** ABSORB (fsm=done, final_classification=B:WORKING)
**Registry row:** staged in `phenotype-registry/registry/disposition-pending-additions-2026-07-28.json` (registry file is FROZEN — apply patch only after explicit unfreeze)
**GitHub source:** `KooshaPari/router-docs` (Private, Other, last pushed 2025-11-30, deleted 2026-06-16)
**Local clone:** NONE (source GH-deleted 2026-06-16; no local backup)

---

## State

| Field | Value |
|-------|-------|
| Source repo | `KooshaPari/router-docs` |
| Source language | markdown (per absorption content) |
| Source size | unknown (size_kb = 0 in registry; placeholder) |
| Source state | Deleted from GitHub 2026-06-16 |
| Absorption target | `OmniRoute/docs/research/archive/router-docs/` |
| Target structure | `README.md` (172 B) + `reference/` (33 entries) + `research/` (10 entries) |
| Boundary doc | not present locally (target is in OmniRoute's research archive) |
| Git evidence | `OmniRoute` commit `f2b8b3638` — `docs(archive): absorb router-docs research corpus from archive` |

---

## Migration works

### What was absorbed

Routing research docs (per projects/router-docs.json:11). The absorbed corpus contains:
- A README (172 B — minimal, likely a pointer to research/)
- A `reference/` directory with 33 entries (likely references to router specs, papers, or external links)
- A `research/` directory with 10 entries (likely research notes, benchmarks, design docs)

### How the absorption was done

A documentation-commit in `OmniRoute` (`f2b8b3638`) explicitly states "absorb router-docs research corpus from archive." This indicates the router-docs source was treated as an archive corpus and migrated to OmniRoute's research archive namespace.

A follow-up commit `1893b92f4` — `docs: remove stale generated and fabricated references` — indicates post-absorption cleanup. **Important:** this cleanup suggests the absorption absorbed both real content AND some generated/fabricated references; the latter were pruned.

### No-novel-items check

Cannot perform per-file diff (source GH-deleted, no local clone). However:
- The absorption commit explicitly claims the corpus came from router-docs.
- A second commit explicitly removed "stale generated and fabricated references" — meaning the absorbing engineer reviewed the content and removed what was not real.

This is the strongest "no-novel-items" check available without the source: the target content was actively curated post-absorption.

### Regressive branches / commits

- The post-absorption cleanup commit (`1893b92f4`) removed "stale generated and fabricated references." This is content loss vs. the original `router-docs`, but the removed content was self-described as fabricated. If `router-docs` source resurfaces with different content, reconciliation may be needed.

---

## Supersedes chain

| Direction | Relationship |
|-----------|--------------|
| `router-docs` **is superseded by** | `OmniRoute/docs/research/archive/router-docs/` |
| `OmniRoute/docs/research/archive/router-docs/` **supersedes** | `router-docs` |
| `router-docs` does **NOT** supersede | any other repo (no prior version of this concept absorbed) |
| `OmniRoute/docs/research/archive/router-docs/` is **NOT** superseded by | any other repo (still canonical as of 2026-07-28) |

---

## Open items (squash blocked pending approval)

- [ ] Squash confirmation per AGENTS.md (destructive = branch-delete): pending explicit per-repo approval from user.
- [ ] Create `archive/` branch (one tombstone commit: `absorbed → OmniRoute/docs/research/archive/router-docs/ on 2026-06-16; see docket URL`).
- [ ] Create `zz-archive/` branch (GH pre-delete mirror — source is GH-deleted, so mirror = empty tombstone).
- [ ] Apply staged patch from `phenotype-registry/registry/disposition-pending-additions-2026-07-28.json` after registry unfreeze.
