---
stage: evergreen
---

# Superseded Catalog

Authoritative list of governance docs marked SUPERSEDED. Each entry links to the current replacement.

| Doc | Superseded date | Superseded by | Reason |
|---|---|---|---|
| ORG_DASHBOARD_v62 (e8fd4b2) | 2026-04-27 | v63 (d51e064) | rolling update |
| ORG_DASHBOARD_v63 (d51e064) | 2026-04-27 | v64 (537de97) | rolling update |
| ORG_DASHBOARD_v64 (537de97) | 2026-04-27 | v65 (45379a9) | rolling update |
| ORG_DASHBOARD_v65 (45379a9) | 2026-04-27 | v66 (e86b2bf) | Rust repo count corrected |
| ORG_DASHBOARD_v66 (e86b2bf) | 2026-04-27 | v67 (58de24b) | TRUE coverage 18/42 not 100% |
| CARGO_DENY_DISPATCH_GAP (b858bc1) | 2026-04-27 | redo-audit (d2e1eec) | base64 decode bugs in original |
| CARGO_DENY_TRUE_COVERAGE (4a2a608) | n/a — still authoritative | | **CURRENT canonical baseline** |

## Current authoritative state
- **Cargo-deny**: `org-audit-2026-04/CARGO_DENY_VICTORY_2026_04_27.md` (a30c88d) — 41/42 enrolled
- **Pages**: `org-audit-2026-04/CARGO_DENY_FINAL_STATE_2026_04_27.md` + parent CNAME PRs (Tokn #27 etc)
- **Roadmap**: `governance/rollouts/30_DAY_ROADMAP_2026_04_27.md` (e58f268)
- **Domain wiring**: `governance/domains/PHENOTYPE_DOMAINS_TF_PLAN_2026_04_27.md` (35fb498)

## How to update
When superseding a doc:
1. Add a `**SUPERSEDED 2026-XX-XX → see <new-doc>**` banner to the top of the old doc
2. Append a new row to this catalog
3. Commit with message: `docs(supersede): mark <old> as superseded by <new>`
