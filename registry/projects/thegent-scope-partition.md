# thegent Absorption Scope Partition

> **Status:** scope survey only (no code yet)
> **Source tree:** `https://github.com/KooshaPari/thegent` (remote-only, 1.0 GB)
> **Date:** 2026-07-04

---

## 1. Why scope partition matters

`thegent` is **1 GB** — too large to absorb monolithically. The conservative posture is to partition by **functional slice** before any PR.

---

## 2. What we know from audit_candidates.json

| Field | Value |
|---|---|
| `id` | `gate-thegent` |
| `name` | `thegent` |
| `path` | `KooshaPari/thegent` |
| `fsm` | `open` |
| `disp` | `AFFIRM` |
| `size_kb` | `1025150` (≈1001 MB) |
| `archived_remote` | `false` |
| `pushed_at` | `2026-07-02T06:15:29Z` |
| `default_branch` | `main` |

---

## 3. Proposed scope partition (5 slices)

| # | Slice | Likely contents | Target repo | Est. |
|---|-------|-----------------|-------------|------|
| 1 | **agent-core** | core agent loop, prompt orchestration | `phenotype-tooling/crates/agent-core` (new) | 6–8 h |
| 2 | **agent-mcp-bridge** | MCP server client, JSON-RPC handlers | `phenotype-mcp-server` (existing) | 4–6 h |
| 3 | **agent-llm-providers** | provider adapters (OpenAI, Anthropic, etc.) | `phenotype-llm` (existing crate) | 3–4 h |
| 4 | **agent-evals** | eval harness, scenarios, scoring | `phenotype-python-sdk/packages/pheno-evals` (new) | 4–6 h |
| 5 | **agent-runtime** | scheduler, queue, replay | `pheno-runtime/crates/phenotype-agent-runtime` (new) | 6–8 h |

**Total:** 23–32 h, ~5 PRs.

---

## 4. Pre-PR reconnaissance steps (BEFORE any code move)

1. **Shallow clone** `KooshaPari/thegent` (depth=1) into `C:\Users\koosh\_tmp\thegent-survey\` (~300 MB).
2. **Top-level inventory:**
   ```bash
   git ls-tree -r HEAD --name-only | awk -F/ '{print $1"/"$2}' | sort -u | head -50
   ```
3. **Language breakdown:**
   ```bash
   git ls-tree -r HEAD --name-only | grep -E '\.(py|ts|rs|go|zig|mojo)$' | awk -F. '{print $NF}' | sort | uniq -c | sort -rn | head
   ```
4. **Locate entry-points:** `find . -name "main.*" -not -path "*/node_modules/*" -not -path "*/target/*" | head`
5. **Identify the 5 slices** by directory pattern (heuristic: look for `agent/`, `mcp/`, `providers/`, `evals/`, `runtime/`).

Until steps 1–5 are complete, the scope partition in §3 is a **hypothesis** — not a plan.

---

## 5. Risks (HIGH — flagging now)

1. **Size**: 1 GB repo may include datasets, model weights, or generated artefacts — must filter before absorbing.
2. **History entanglement**: 1 GB repos often have binary blobs in git history. `git subtree add` may fail; may need `git filter-repo`.
3. **License**: unverified. Thegent may have a different license than MIT/Apache-2.0 dual used elsewhere.
4. **Secrets**: large repos often have leaked keys. Run `gitleaks` before any clone→copy.

---

## 6. Recommended next action

**Land the reconnaissance PR first (`chore/thegent-scope-survey`)**, then issue 5 slice-specific PRs only after the survey confirms the §3 partition.

DO NOT attempt any code merge from `thegent` until this survey is complete.