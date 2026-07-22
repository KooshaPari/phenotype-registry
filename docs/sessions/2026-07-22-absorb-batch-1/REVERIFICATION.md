# Re-verification — current remote byte-state for 4 candidates

**Date:** 2026-07-22
**Method:** `gh api` against current remote (not stale local mirrors). Local mirrors were cloned earlier in this session; this re-verification supersedes them.

## Why this matters

Two of the four candidates have an existing 2026-07-17 audit whose claims are now false:
- `clap-ext-2026-07-17.md` says absorbed into `HexaKit/libs/clap-ext/`, but ADR-007 hard-excludes HexaKit and `BOUNDARY_OWNERS.md` marks HexaKit as scaffold-only.
- `phenoEvents-2026-07-17.md` says absorbed into `pheno/crates/phenotype-event-bus/`, but that path is **404**.

This file records the byte-state evidence that forces the supersede.

---

## 1. `KooshaPari/clap-ext` — current remote state

| Field | Value |
|-------|-------|
| HEAD SHA | `a623144` (main, 2026-07-01) |
| Size | 119 KB |
| Branches | 6 (1 main + 5 non-default: `integration/consolidate`, `chore/s7-threat-model-tick20`, `orch-v12-s1-003`, `archive/orphan-wt-clap-ext-p3-*`, `backup/fix-p3-remediate-2026-07-01-*`, `wip/2026-07-16-0027-auto`) |
| Archived | NO (unarchived 2026-07-21) |
| Tags | `v0.1.0` (cc4b1f6) |
| Default branch | `main` |
| Tree | `.github/, AGENTS.md, CLAUDE.md, CONTRIBUTING.md, SECURITY.md, crates/, docs/, examples/, Cargo.toml/.lock, LICENSE*` |

**2026-07-17 audit claim:** "absorbed into HexaKit/libs/clap-ext/"
**Current reality (2026-07-22):** `HexaKit` tree (`gh api repos/KooshaPari/HexaKit/contents/`) shows `crates/` is NOT a directory under HexaKit at the root — HexaKit is scaffold-only. **The 2026-07-17 claim is false.** clap-ext still exists as a standalone repo with full source.

**ADR-007 check:** HexaKit is on the hard-exclude list (rule #1: too-large for clean absorption + scaffold-only). A destination of `HexaKit/libs/clap-ext/` violates ADR-007 directly.

**`BOUNDARY_OWNERS.md` check:** HexaKit owns "by-language/, by-project/, registry.yaml, .template.*, governance workflow references, hexagonal folder patterns copied into new repos. **Does not own:** Runtime metrics, tracing, config engines, resilience implementations." clap-ext (a CLI extension library) does not match the HexaKit charter.

**Correct destination per Domain SDK layer:** `KooshaPari/phenotype-rust-sdk` (Rust SDK; absorb clap-ext as a sibling crate). Confirmed by user direction 2026-07-22.

---

## 2. `KooshaPari/phenoEvents` — current remote state (CRITICAL for 2phenoEvents decision)

| Field | Value |
|-------|-------|
| HEAD SHA | (latest on `main`, 2026-07-22) |
| Size | 235 KB |
| Archived | NO (unarchived 2026-07-21, alive) |
| Default branch | `main` |
| Tree (src/) | `bus/`, `core/`, `lib.rs`, `observability.rs`, `projection/`, `schema/` — **all 10 source files present** |
| Tree (top-level) | `.env.example, .github, .gitignore, .pre-commit-config.yaml, AGENTS.md, CHANGELOG.md, CLAUDE.md, CODEOWNERS, CODE_OF_CONDUCT.md, CONTRIBUTING.md, Cargo.lock, Cargo.toml, LICENSE, README.md, SECURITY.md, SSOT.md, audit_scorecard.json, benches, cliff.toml, crates, deny.toml, docs, justfile, llms.txt, phenoEvents/, src, tests` |
| Last push | 2026-07-22T00:39:01Z (today) |

**2026-07-17 audit claim:** "phenoEvents absorbed into `pheno/crates/phenotype-event-bus/` at confidence 0.85"
**Current reality (2026-07-22):** `gh api repos/KooshaPari/pheno/contents/crates/phenotype-event-bus` → **404 Not Found**. Searching `pheno` for any `event-bus` / `phenotype-event` crate path returns only:
- `crates/phenotype-event-sourcing/` (different crate — sourcing, not bus)
- `crates/agileplus-events/` (sibling, unrelated)
- `agileplus/crates/agileplus-grpc/src/event_bus.rs` (one file inside agileplus-grpc, not a standalone crate)

**The 2026-07-17 audit's "phenotype-event-bus absorbed into pheno" claim is FALSE.** Either the absorb was reverted, never landed, or was made in a branch that was not merged. **The source-of-truth for the event-bus code is still `KooshaPari/phenoEvents` itself.**

**Implication for 2phenoEvents:** The earlier local-mirror byte-diff (showing `2phenoEvents/src` ≡ `phenoEvents/src` at MD5 `4a81dec5249e35cd3c7032b512fdc20b`) is **correct** — `2phenoEvents` is a restore copy of `phenoEvents`, both still containing the live event-bus source. With `phenoEvents` alive and unarchived, `2phenoEvents` is a redundant satellite that adds no unique code.

---

## 3. `KooshaPari/agent-platform` — current remote state

| Field | Value |
|-------|-------|
| HEAD SHA | `48853e7` (main, 2026-06-20) |
| Size | 111 KB |
| Archived | NO (unarchived 2026-07-21) |
| Default branch | `main` |
| Tree | `AGENTS.md, CODEOWNERS, examples, ports, package.json/lock, tsconfig.json, vitest.config.ts` |
| Branches | 5 non-default: `chore/dependabot-2026-06-08`, `chore/async-trait-2026-06-08`, `feat/codex-cli-adapter-2026-06-18`, `feat/modal-adapters-2026-06-18`, `chore/v16-cycle6-L7-subsystems-2026-06-21` |
| Tags | none |

**No 2026-07-17 audit exists.** Clean slate. TS project with two genuine sibling feature branches (`feat/codex-cli-adapter-2026-06-18`, `feat/modal-adapters-2026-06-18`) that warrant separate absorption destinations per user direction (Eidolon + HexaKit).

---

## 4. `KooshaPari/Guardrail` — current remote state

| Field | Value |
|-------|-------|
| HEAD SHA | `b8e498d` (main, 2026-03-25 — **4 months old**) |
| Size | 2 KB |
| Archived | NO (unarchived 2026-07-21) |
| Default branch | `main` |
| Tags | `v0.1.0` (b8e498d) |
| Tree | `.github/, Cargo.toml, LICENSE, README.md` |
| **No `src/` directory** | Empty scaffold |

**No 2026-07-17 audit exists.** Clean slate. Per user direction (2026-07-22): leave standalone (A6), no mutation.

---

## Summary of re-verification outcomes

| Audit target | 2026-07-17 audit | Current reality | Action |
|--------------|------------------|-----------------|--------|
| clap-ext destination | `HexaKit/libs/clap-ext/` | HexaKit hard-excluded; `BOUNDARY_OWNERS` says scaffold-only | **SUPERSEDE** with `phenotype-rust-sdk` |
| phenoEvents destination | `pheno/crates/phenotype-event-bus/` | Path 404; absorb never landed | **SUPERSEDE** parent audit; new audit for 2phenoEvents reflects `phenoEvents` is the live parent |
| agent-platform | n/a | n/a | NEW audit |
| Guardrail | n/a | n/a | NEW audit |

This re-verification is the basis for the 4 audit files in `audits/absorption-justifications/`.
