# thegent Slice-1 Reconnaissance Manifest

> **Status:** recon-only (no code moved)
> **Source:** `KooshaPari/thegent` (1.0 GB, remote-only, default_branch=main, last push 2026-07-02T06:15:29Z)
> **Date:** 2026-07-04
> **Parent document:** `thegent-scope-partition.md` §3 (slice 1 of 5: agent-core)

---

## 1. Why this slice first

`agent-core` is the **highest-leverage** of the 5 proposed slices:

- Every other slice (`mcp-bridge`, `llm-providers`, `evals`, `runtime`) **imports** agent-core types
- Without agent-core the other 4 cannot be absorbed — they would have dangling references
- Estimated 6–8 h to absorb (vs. 23–32 h for all 5)

If slice-1 fails for license, secrets, or binary-blob reasons, none of the other slices proceed.

---

## 2. What this recon produces

A **documented manifest** of what slice-1 *should* contain, not a code copy. This means:

1. **No `git subtree add`** until recon confirms the §3 partition hypothesis.
2. **No PR creation** until recon is reviewed.
3. **No commit** — this document itself IS the recon deliverable.

---

## 3. Recon inputs (already collected)

From `phenotype-registry/audit_candidates_with_size.json`:

| Field | Value |
|---|---|
| `path` | `KooshaPari/thegent` |
| `size_kb` | `1025150` (≈1001 MB) |
| `fsm` | `open` |
| `disp` | `AFFIRM` |
| `default_branch` | `main` |
| `pushed_at` | `2026-07-02T06:15:29Z` |
| `archived_remote` | `false` |

From `KooshaPari/thegent` GitHub metadata (public):

- **Repo type:** monorepo (single default branch, no sub-repos)
- **Visibility:** public
- **Size flag:** GitHub reports ~1 GB → confirms `size_kb` derivation
- **Languages:** unknown without clone

---

## 4. Required clone + scan (BEFORE any absorb decision)

These commands MUST be run on a shallow clone before any other action. They are recorded here so the recon can be reproduced.

```bash
# 1. Shallow clone to a sandbox location
git clone --depth 1 https://github.com/KooshaPari/thegent.git \
    C:\Users\koosh\_tmp\thegent-survey\

# 2. Top-level inventory (depth=1)
cd C:\Users\koosh\_tmp\thegent-survey
git ls-tree -r HEAD --name-only | awk -F/ '{print $1"/"$2}' | sort -u | head -50

# 3. Language breakdown
git ls-tree -r HEAD --name-only | grep -E '\.(py|ts|rs|go|zig|mojo|swift|cpp|c|h)$' \
    | awk -F. '{print $NF}' | sort | uniq -c | sort -rn | head

# 4. Locate entry-points
find . -name "main.*" -not -path "*/node_modules/*" -not -path "*/target/*" | head

# 5. License verification
find . -maxdepth 2 -iname "LICENSE*" -not -path "*/node_modules/*"

# 6. Secret scan (run BEFORE any subsequent step)
gitleaks detect --source . --report-path _tmp/thegent-gitleaks.json
```

**Gate criteria** (must all be true to proceed past recon):

- [ ] Top-level dir count < 30 (i.e. the 5-slice partition is plausible)
- [ ] No `*.bin`, `*.safetensors`, `*.onnx`, `*.pt` files in tracked tree (else filter before absorb)
- [ ] LICENSE matches MIT/Apache-2.0 dual used by the rest of the org
- [ ] `gitleaks` finds 0 secrets at default confidence
- [ ] `agent/` directory exists with reasonable Python or TS surface area

If any gate fails, **STOP** and surface to the user for a re-plan.

---

## 5. Expected post-recon artefacts

Once §4 commands complete, the next batch will produce:

1. `_tmp/thegent-survey/TOP-DIRS.txt` — top-level inventory
2. `_tmp/thegent-survey/LANGS.txt` — language breakdown
3. `_tmp/thegent-survey/LICENSE-report.md` — license compatibility verdict
4. `_tmp/thegent-survey/gitleaks-report.json` — secret-scan verdict
5. `_tmp/thegent-survey/agent-core-inventory.txt` — files in `agent/` dir, by sub-pattern

These artefacts feed into the **slice-1 absorb PR** (slice-1-PR), which would:

- Copy `agent/` from `thegent` → `phenotype-tooling/crates/agent-core/`
- Re-export under a `thegent_compat` module for one release, then remove
- Add the absorbed files to `phenotype-registry/audits/absorption-justifications/thegent-agent-core-2026-MM-DD.md`
- Re-grade: target `14/14 L4` on the new audit

---

## 6. Risks (UNCHANGED from partition doc)

| Risk | Mitigation |
|---|---|
| Binary blobs in tracked tree | §4 step 2 will detect via file-extension heuristic |
| History entanglement | `git subtree add` with `--squash` + `--allow-empty-message` fallback |
| License mismatch | §4 step 5 + legal review before any copy |
| Secret leak | §4 step 6 — gitleaks gate must be 0 |
| 1 GB → sub-PR too large | Slice partition (this is exactly what §4 enables) |

---

## 7. Status (live)

- [x] Recon manifest written (this doc)
- [ ] Shallow clone executed
- [ ] Top-level inventory collected
- [ ] Language breakdown collected
- [ ] Entry-points located
- [ ] License verified
- [ ] gitleaks scan clean
- [ ] Slice-1 absorb PR ready

**Until all 8 checkboxes are ticked, no slice-1 code move.**

---

## 8. Reference

- Parent partition: `registry/projects/thegent-scope-partition.md`
- Audit at L4: `audits/absorption-justifications/thegent-2026-07-02.md`
- Project card: `projects/thegent.json` (`disposition: AFFIRM`)
- Live PR: `phenotype-registry` PR #380 (audit batch)