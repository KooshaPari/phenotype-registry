# Phenotype-Org Governance

Source of truth for organizational policies, audit trails, and operational runbooks.  
Navigate by status first, then by domain.

## Current State

- **`/governance/`** — Live policies, active rollouts, and domain standards.
  - `domains/` — Functional-area policies (e.g., data, security, network).
  - `rollouts/` — Phase plans, change-management trackers, sprint records.
  - `templates/` — Document schemas; copy these when adding docs.
- **`/org-audit-2026-04/`** — Audit snapshot for the April 2026 hardening sprint. Reference only; do not edit. See `SUPERSEDED.md` for replaced versions.

## Authority & Supersession

| Indicator | Meaning |
|-----------|---------|
| `STATUS: AUTHORITATIVE` in frontmatter | Current source of truth |
| `STATUS: SUPERSEDED` + `replaces:` pointer | Archive; consult only for historical context |
| Dated filenames (e.g., `policy-2026-04.md`) | Superseded unless explicitly linked from current canonical |

When conflicting guidance appears, the document with the latest `effective_date:` in `/governance/` wins.

## Authoritative current state (2026-04-27)

- **Cargo-deny rollout:** `org-audit-2026-04/CARGO_DENY_VICTORY_2026_04_27.md` (40/42 = 95% enrolled, +bare-cua = 41/42 effective 100% of active)
- **CodeQL Rust:** `org-audit-2026-04/CODEQL_RUST_FINAL_2026_04_27.md` (34/42 = 80%)
- **Pages:** 7 sites LIVE (Tokn, thegent, PolicyStack, HexaKit, HeliosLab, FocalPoint, AgilePlus)
- **Roadmap:** `governance/rollouts/30_DAY_ROADMAP_2026_04_27.md`
- **Domain wiring:** `governance/domains/PHENOTYPE_DOMAINS_TF_PLAN_2026_04_27.md`
- **CHANGELOG:** `governance/CHANGELOG_2026_04_27.md`

## Memory Cross-References

Agent memory at `~/.claude/projects/-Users-kooshapari-CodeProjects-Phenotype-repos/memory/MEMORY.md`. Key entries:
- `feedback_only_parent_claude.md` — parent-only-Claude regime
- `feedback_codex_dispatch_pattern.md` — codex dispatch syntax
- `feedback_kimi_first_preference.md` — Kimi → Minimax → Codex
- `feedback_omniroute_kimi_tiers_2026_04_27.md` — working `nvidia/moonshotai/kimi-k2.5` route
- `feedback_one_shell_per_agent_or_hierarchical.md` — one Bash per worker
- `feedback_billing_blocked_rules.md` — Actions billing constraint
- `reference_phenotype_domains.md` — domain inventory + canonical strategy

## Adding New Docs

1. Copy the appropriate template from `/governance/templates/`.
2. Name descriptively: `<domain>-<action>-YYYY-MM-DD.md` (or _2026_04_27 short form).
3. Fill frontmatter (where applicable): `title`, `status`, `domain`, `effective_date`, `see_also`, `supersedes`, `replaced_by`.
4. Place in `/governance/domains/<domain>/` or `/governance/rollouts/`.
5. Update `SUPERSEDED.md` if your doc replaces an existing one.
6. Commit message: `docs(<area>): <verb> <noun>` (e.g., `docs(governance): add Codeberg mirror plan`)

## Quick Links

- [SUPERSEDED catalog](./SUPERSEDED.md)
- [Taxonomy proposal](./TAXONOMY_PROPOSAL_2026_04_27.md)
- [Latest CHANGELOG](./governance/CHANGELOG_2026_04_27.md)
- [30-day roadmap](./governance/rollouts/30_DAY_ROADMAP_2026_04_27.md)
- [Cargo-deny victory](./org-audit-2026-04/CARGO_DENY_VICTORY_2026_04_27.md)
