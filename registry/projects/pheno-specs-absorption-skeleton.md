# pheno-specs Absorption Skeleton → kitty-specs subsystem

> **Status:** skeleton / paper exercise
> **Source tree:** `C:\Users\koosh\phenoSpecs.git\` (bare, freshly cloned)
> **Destination:** `pheno-runtime/docs/.kitty-specs-source/` (mirror)
> **Date:** 2026-07-04

---

## 1. Source inventory (verified)

| Path | Type | Notes |
|---|---|---|
| `VERSION` | text | `0.1.0` |
| `registry.yaml` | YAML | 30 lines (frontmatter for spec cards) |
| `README.md` | docs | spec-traceability scope |
| `*.md` (spec files) | Markdown | spec cards, traceability edges |
| Python + YAML tooling | mixed | spec generators, validators |

Last commit 2026-07-02 (yesterday), FSM=active, disp=AFFIRM, 1.8 MB total.

---

## 2. Verdict

**Mirror into `pheno-runtime/docs/.kitty-specs-source/` — NOT a separate crate.** Rationale:

- `pheno-runtime` already has a `kitty-specs/` subsystem (per `lang/rust/packages/pheno-runtime/kitty-specs/`).
- `pheno-specs` is a **content source** (spec cards), not a runtime crate.
- Mirroring preserves provenance while keeping the runtime dependency-free.

---

## 3. Landing matrix

| Source | Destination |
|---|---|
| `VERSION`, `registry.yaml` | `pheno-runtime/docs/.kitty-specs-source/{VERSION,registry.yaml}` |
| All `*.md` spec files | `pheno-runtime/docs/.kitty-specs-source/specs/*.md` |
| `README.md` | `pheno-runtime/docs/.kitty-specs-source/README.md` |
| Python tooling | `pheno-runtime/docs/.kitty-specs-source/tooling/` (no executable) |

---

## 4. Skeleton

```text
pheno-runtime/docs/.kitty-specs-source/
├── README.md
├── VERSION                   # 0.1.0
├── registry.yaml
├── specs/                    # all .md spec cards mirrored
│   ├── SPEC-001.md
│   ├── SPEC-002.md
│   └── ...
└── tooling/                  # python + yaml (no .py execution paths)
```

---

## 5. Phase plan (1 PR)

1. `git clone` `pheno-specs` bare into `pheno-runtime/docs/.kitty-specs-source/` as a vendored mirror.
2. Annotate with `PROVENANCE.md` (upstream URL, license, last-synced date).
3. Wire `pheno-runtime/kitty-specs/` build script to consume these specs (optional, follow-up PR).
4. `KooshaPari/pheno-specs` retained as upstream.

**Open questions:**
- Should `pheno-specs` be kept as separate `KooshaPari/pheno-specs` or fully absorbed? Recommendation: keep as **source of truth**, mirror into pheno-runtime.
- Need to confirm license (current `pheno-runtime` uses MIT/Apache-2.0 dual).

---

## 6. Decision

**Land in 1 PR — `chore/mirror-pheno-specs`** under `pheno-runtime`.