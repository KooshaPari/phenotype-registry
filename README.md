<!-- AI-DD-META:START -->
<!-- This repository is planned, maintained, and managed by AI Agents only. -->
<!-- Slop issues are expected and intentionally present as part of an HITL-less -->
<!-- /minimized AI-DD metaproject of learning, refining, and building brute-force -->
<!-- training for both agents and the human operator. -->
![Downloads](https://img.shields.io/github/downloads/KooshaPari/phenotype-org-governance/total?style=flat-square&label=downloads&color=blue)
![GitHub release](https://img.shields.io/github/v/release/KooshaPari/phenotype-org-governance?style=flat-square&label=release)
![License](https://img.shields.io/github/license/KooshaPari/phenotype-org-governance?style=flat-square)
![AI-Slop](https://img.shields.io/badge/AI--DD-Slop%20Expected-orange?style=flat-square)
![AI-Only-Maintained](https://img.shields.io/badge/Planned%20%26%20Maintained%20by-AI%20Agents%20Only-red?style=flat-square)
![HITL-less](https://img.shields.io/badge/HITL--less%20AI--DD-metaproject-yellow?style=flat-square)

> ⚠️ **AI-Agent-Only Repository**
>
> This repo is **planned, maintained, and managed exclusively by AI Agents**.
> Slop issues, rough edges, and AI artifacts are **expected and intentionally
> present** as part of an **HITL-less / minimized AI-DD** metaproject focused
> on learning, refining, and brute-force training both the agents and the
> human operator. Bug reports and contributions are still welcome, but please
> expect AI-generated code, comments, and documentation throughout.
<!-- AI-DD-META:END -->
> **Work state:** ACTIVE · **Progress:** `████████░░ 80%`
> ENFORCEMENT surface — deny.toml policy baseline (consumed by tooling's reusable); history archived to docs/history/ · updated 2026-06-02

# Phenotype-Org Governance

The **ENFORCEMENT** member of the spec/governance spine: home of the canonical **`deny.toml`/license + advisory baseline** that sibling repos consume. The reusable workflow *mechanism* lives in [phenotype-tooling](https://github.com/KooshaPari/phenotype-tooling) and consumes this policy (governance owns WHAT, tooling owns HOW). Start at **[POLICY.md](POLICY.md)**.

## The 4-role spine

This repo enforces; it does not index, decide, or document conventions — each of those has its own home.

| Repo | Role |
|------|------|
| [phenotype-registry](https://github.com/KooshaPari/phenotype-registry) | **INDEX** — canonical ecosystem map ([ECOSYSTEM_MAP.md](https://github.com/KooshaPari/phenotype-registry/blob/main/ECOSYSTEM_MAP.md)) |
| [PhenoSpecs](https://github.com/KooshaPari/PhenoSpecs) | **ADRs / API contracts / specs** |
| [PhenoHandbook](https://github.com/KooshaPari/PhenoHandbook) | **CONVENTIONS / patterns** |
| **phenotype-org-governance** (this repo) | **ENFORCEMENT** — `deny.toml`/license + advisory policy baseline (workflow mechanism lives in phenotype-tooling) |

## Current State

- **[`POLICY.md`](POLICY.md)** — forward-looking: the enforced policies and how siblings consume them.
- **[`deny.toml`](deny.toml)** — the canonical supply-chain policy baseline (license allowlist + advisories). Consumed by phenotype-tooling's `reusable/cargo-deny.yml` mechanism.
- **[`scripts/`](scripts/)** — billing-free org-wide local sweep (`cargo-deny-org-weekly.sh`).
- **[`docs/history/`](docs/history/)** — archived audit waves, session logs, and dashboards (the former `governance/`, `org-audit-2026-04/`, and `changes/` trees). Reference only; not active policy.

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
