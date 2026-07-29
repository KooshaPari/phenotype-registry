# phenoVessel → PhenoPlugins/pheno-plugin-vessel — Absorption Docket (BLOCKED)

**Generated:** 2026-07-28
**Authority:** phenotype-registry (registry/disposition-index.json + projects/phenoVessel.json)
**Disposition:** ABSORB_BUT_TARGET_MISSING (fsm=blocked, final_classification=E:ABSORB_BUT_TARGET_MISSING)
**Registry row:** staged in `phenotype-registry/registry/disposition-pending-additions-2026-07-28.json` (registry file is FROZEN — apply patch only after explicit unfreeze AND blocker resolution)
**GitHub source:** `KooshaPari/phenoVessel` (Private, HTML, Other, last pushed 2025-04-03, deleted 2026-06-16)
**Local clone:** NONE (source GH-deleted 2026-06-16; no local backup)

---

## State

| Field | Value |
|-------|-------|
| Source repo | `KooshaPari/phenoVessel` |
| Source language | HTML (per GH API) |
| Source size | unknown (size_kb = 0 in registry; placeholder) |
| Source state | Deleted from GitHub 2026-06-16 |
| Absorption target (claimed) | `PhenoPlugins/pheno-plugin-vessel` |
| Absorption target (actual) | **MISSING LOCALLY** — `PhenoPlugins/` does not exist on disk (verified 2026-07-28) |
| Boundary doc | not present locally |
| Git evidence | NONE — no commit/PR found in registry or local git history for `pheno-plugin-vessel` |

---

## Migration works

### What was absorbed (claimed)

Per projects/phenoVessel.json:11: "Merged into PhenoPlugins as pheno-plugin-vessel crate." This was a deprecated/merged target per registry projects file.

### How the absorption was done (unverifiable)

The projects file asserts absorption but provides no PR number, commit hash, or migration date. The local filesystem has no `PhenoPlugins/` directory and no `pheno-plugin-vessel*` files anywhere within the working tree (verified via `find ... -name "pheno-plugin-vessel*"`).

### No-novel-items check

**Cannot be performed — target repo does not exist locally.**

### Regressive branches / commits

None found (no records exist for the claimed absorption).

---

## Supersedes chain

| Direction | Relationship |
|-----------|--------------|
| `phenoVessel` **is claimed superseded by** | `PhenoPlugins/pheno-plugin-vessel` (UNVERIFIED — target missing) |
| `phenoVessel` does **NOT** supersede | any other repo (no prior version of this concept absorbed) |

---

## BLOCKER — requires user direction

| Option | Description | Outcome |
|--------|-------------|---------|
| **(a) Regenerate** | Scaffold `PhenoPlugins/` + `pheno-plugin-vessel/` from absorbed content. Requires retrieval of `phenoVessel` content from somewhere (not possible — source GH-deleted, no local clone, no fork lineage). | Effectively impossible without external data |
| **(b) Tombstone-only** | Mark `phenoVessel` as registry tombstone with `boundary_classification=absorbed-but-target-missing`. Do not assert functional absorption. No code merge. | Reversible: if content resurfaces later, can re-evaluate |
| **(c) Skip** | Remove from registry entirely as unverified claim. | Loses audit trail; not recommended |

**Recommended: (b) Tombstone-only.** Y/N?

---

## Open items (squash blocked pending approval AND blocker resolution)

- [ ] User decision on (a)/(b)/(c) above.
- [ ] If (b): finalize docket with `final_classification=E:ABSORB_BUT_TARGET_MISSING` and write `phenotype-registry/docs/boundary/phenovessel.md` explaining the unverified status.
- [ ] Squash confirmation per AGENTS.md: pending explicit per-repo approval from user.
- [ ] Create `archive/` branch (one tombstone commit: `absorbed → PhenoPlugins (target missing, see docket) on 2026-07-28; see docket URL`).
- [ ] Create `zz-archive/` branch (GH pre-delete mirror — source is GH-deleted, so mirror = empty tombstone).
- [ ] Apply staged patch from `phenotype-registry/registry/disposition-pending-additions-2026-07-28.json` after registry unfreeze AND blocker resolution.
