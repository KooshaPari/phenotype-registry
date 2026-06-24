# Absorption-Justification Audit Grades

**Generated:** 2026-06-24
**Rubric:** `registry/audit-absorption-justification/schema.json` (max 14)
**Authority:** phenotype-registry
**Fleet Size:** 8 audits graded

---

## Grade Boundaries

| Grade | Score Range | Classification |
|---|---|---|
| **L4** | 11.50 – 14.00 | Excellent: Absorption fully justified |
| **L3** | 10.00 – 11.49 | On Track: Minor gaps in justification |
| **L2** | 7.00 – 9.99 | Needs Improvement: Substantive gaps |
| **L1** | 3.00 – 6.99 | Critical Foundation Needed |
| **L0** | 0.00 – 2.99 | Unacceptable: Absorption not justified |

---

## Fleet Summary

| Metric | Value |
|---|---|
| **Total audits graded** | 8 |
| **Rubric max score** | 14 |
| **Fleet average score** | **13.625 / 14** |
| **Fleet average percentage** | **97.32 %** |
| **Fleet average grade** | **L4** |
| **Fleet classification** | Excellent: Absorption fully justified |
| **Perfect scores (14/14)** | 2 audits (BytePort, phenotype-go-sdk) |
| **Near-perfect scores (13.5/14)** | 6 audits |

**Grade distribution**

| Grade | Count | % of fleet |
|---|---|---|
| L4 | 8 | 100 % |
| L3 | 0 | 0 % |
| L2 | 0 | 0 % |
| L1 | 0 | 0 % |
| L0 | 0 | 0 % |

**Strongest audits** (14/14, perfect)

- `BytePort-2026-06-23.md` — AFFIRM_WITH_RUST_MIGRATION
- `phenotype-go-sdk-2026-06-23.md` — ARCHIVE_DELETE_BLOCKED

**Weakest audit** (13.5/14, sorted first)

- `phenotype-infra-2026-06-23.md` — AFFIRM_CONSOLIDATION_TARGET (P5 restore-command-validity is a comment-only, not a verifiable invocation)

**Recurring weak pillar**

- **P7 (deletion-gate-tooling-coverage)** — 6 of 8 audits do not explicitly cite `bin/repo-delete-gate.sh/.ps1` and lose 0.5 on this pillar.

**Improvement target**

- Add an explicit one-line reference to `bin/repo-delete-gate.sh/.ps1` (or a justification for omission) to every audit that uses `gh repo delete` or `gh repo archive` directly.

---

## Per-Audit Grades (sorted ascending — weakest first)

| # | Source Repo | Audit Path | Verdict | Score | % | Grade |
|---|---|---|---|---:|---:|---|
| 1 | phenotype-infra | `audits/absorption-justifications/phenotype-infra-2026-06-23.md` | AFFIRM_CONSOLIDATION_TARGET | 13.5 / 14 | 96.43 % | **L4** |
| 2 | go-nippon | `audits/absorption-justifications/go-nippon-2026-06-23.md` | ARCHIVE_ONLY | 13.5 / 14 | 96.43 % | **L4** |
| 3 | smart-mcp-go | `audits/absorption-justifications/smart-mcp-go-2026-06-23.md` | NO_MERIT_WITH_INTENT | 13.5 / 14 | 96.43 % | **L4** |
| 4 | McpKit | `audits/absorption-justifications/McpKit-2026-06-23.md` | HARD_DELETE_READY | 13.5 / 14 | 96.43 % | **L4** |
| 5 | phenocompose | `audits/absorption-justifications/phenocompose-2026-06-23.md` | DELETABLE_DOWNGRADED_TO_ARCHIVE | 13.5 / 14 | 96.43 % | **L4** |
| 6 | nanovms | `audits/absorption-justifications/nanovms-2026-06-23.md` | DELETION_CANDIDATE_PROCEED | 13.5 / 14 | 96.43 % | **L4** |
| 7 | BytePort | `audits/absorption-justifications/BytePort-2026-06-23.md` | AFFIRM_WITH_RUST_MIGRATION | 14.0 / 14 | 100.00 % | **L4** |
| 8 | phenotype-go-sdk | `audits/absorption-justifications/phenotype-go-sdk-2026-06-23.md` | ARCHIVE_DELETE_BLOCKED | 14.0 / 14 | 100.00 % | **L4** |

---

## Per-Pillar Breakdown (7 pillars, weights sum to 14)

| Pillar | Weight | Description |
|---|---:|---|
| P1 | 3 | manifest-completeness |
| P2 | 3 | parity-evidence |
| P3 | 2 | branch-coverage |
| P4 | 2 | last-resort-justification |
| P5 | 1 | restore-command-validity |
| P6 | 2 | registry-integration |
| P7 | 1 | deletion-gate-tooling-coverage |

### Pillar × Audit matrix

| Source Repo | P1 (3) | P2 (3) | P3 (2) | P4 (2) | P5 (1) | P6 (2) | P7 (1) | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| phenotype-infra | 3 | 3 | 2 | 2 | **0.5** | 2 | 1 | 13.5 |
| go-nippon | 3 | 3 | 2 | 2 | 1 | 2 | **0.5** | 13.5 |
| smart-mcp-go | 3 | 3 | 2 | 2 | 1 | 2 | **0.5** | 13.5 |
| McpKit | 3 | 3 | 2 | 2 | 1 | 2 | **0.5** | 13.5 |
| phenocompose | 3 | 3 | 2 | 2 | 1 | 2 | **0.5** | 13.5 |
| nanovms | 3 | 3 | 2 | 2 | 1 | 2 | **0.5** | 13.5 |
| BytePort | 3 | 3 | 2 | 2 | 1 | 2 | 1 | 14.0 |
| phenotype-go-sdk | 3 | 3 | 2 | 2 | 1 | 2 | 1 | 14.0 |
| **Fleet avg** | 3.00 | 3.00 | 2.00 | 2.00 | 0.94 | 2.00 | 0.81 | **13.625** |

Bold = pillar at less than full credit (the per-audit weak spot).

### Recurring pillar weakness

- **P5 (restore-command-validity):** Only `phenotype-infra` loses points here (0.5/1) — its Restore-Command section is a "governed by target CI" comment, not a concrete `mv .archive/X .` or `git clone` invocation.
- **P7 (deletion-gate-tooling-coverage):** 6 of 8 audits lose 0.5 here because they invoke `gh repo archive` / `gh repo delete` directly without referencing `bin/repo-delete-gate.sh/.ps1` and without an explicit justification for the omission. Only the two non-deleting audits (BytePort, phenotype-go-sdk) carry a sufficient Action Class statement to satisfy the schema's "explicitly explains why the gate is not required" allowance.

---

## Notable Audit Highlights

### Strongest P4 evidence (most rigorous last-resort-justification)
- **phenotype-go-sdk** — Three explicit blockers documented with reason + residual gap + why archival isn't sufficient. This is the strongest P4 in the fleet and is the only audit that hard-blocks archival/deletion with substantive rationale.

### Most defensive posture (downgrade rather than delete)
- **phenocompose** — DELETABLE_DOWNGRADED_TO_ARCHIVE; surfaces a posture shift in the matrix itself, demonstrating awareness of the conservative path when full delete isn't justified.

### Most process-aware (consumer-impact tracking)
- **phenotype-go-sdk** — ABSORPTION_MATRIX includes a "Consumer impact" row; explicit identification of downstream consumers.

### Weakest overall (most informative for improvement)
- **phenotype-infra** — P5 restore-command-validity partial. The Restore-Command section is a comment rather than a verifiable command. As the consolidation *target*, this audit's restore semantics rely on the target's own revert workflow, which is acceptable but should be made explicit with a concrete command.

---

## Fleet Average

> **13.625 / 14 (97.32 %) — L4 (Excellent: Absorption fully justified)**

The fleet is uniformly high-performing: every audit reaches L4. The two most informative improvement signals are concentrated in **P5** (one audit, phenotype-infra) and **P7** (six audits). Addressing P7 across all deletion-leaning audits is the single highest-leverage action to push the entire fleet to a perfect 14.0.

---

*Machine-readable grades: `GRADES.json` (same fields, structured).*
