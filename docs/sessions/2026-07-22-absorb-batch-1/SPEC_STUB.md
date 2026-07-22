# Spec Stub — `absorb-batch-1-2026-07-22`

> **Stub.** This file exists because `phenotype-registry/AGENTS.md` mandates that all non-trivial cross-repo absorption work is tracked in AgilePlus via `agileplus specify`. The stub records the intent and links the actual spec work item to this session.

## Spec metadata

| Field | Value |
|-------|-------|
| Spec ID | `absorb-batch-1-2026-07-22` |
| Created | 2026-07-22 |
| Status | DRAFT (awaiting user approval of the 4 audit files) |
| Owner | koosha (HITL for all conflict resolution) |
| Linked session | `docs/sessions/2026-07-22-absorb-batch-1/` |
| Parent ADR | `docs/adr/ADR-007-absorption-eligibility-boundary.md` |

## Goal

Validate, then execute, the absorb actions for the 4 candidates audited in this session. Each action is gated on (a) the audit file being reviewed and (b) the user issuing an explicit "go" for that specific absorb.

## Work items (gated individually)

| WI | Title | Parent | Action | Gating |
|----|-------|--------|--------|--------|
| WI-1 | Absorb `clap-ext` into `phenotype-rust-sdk` | `phenotype-rust-sdk` | A1 (ff-merge wip branch) → A3 fallback; rename source to `zz-archive-clap-ext`; archive | audit review + user go |
| WI-2 | Split-absorb `agent-platform` into Eidolon + HexaKit | `Eidolon` (`feat/codex-cli-adapter`) + `HexaKit` (`feat/modal-adapters`) | A7 custom split with A1→A3 discipline per side; rename source to `zz-archive-agent-platform`; archive | audit review + user go per side |
| WI-3 | Leave `Guardrail` standalone (no mutation) | n/a | A6 — only registry pointer; no rename, no archive | audit review only |
| WI-4 | Pointer `2phenoEvents` → `phenoEvents` (archive-only) | `phenoEvents` | A7 = A5 + archive; rename source to `zz-archive-2phenoEvents`; archive | audit review + user go |

## Acceptance criteria

- All 4 audit files reviewed and explicitly approved by user.
- Source HEAD SHAs re-verified at the moment of mutation (no drift).
- Branch-name collisions in parent repos detected before any merge attempt.
- Version-pin conflicts (Cargo.toml/package.json) surfaced as individual HITL pings, not auto-resolved.
- After absorb merge lands: source rename + archive happens as a single batched gh command sequence per repo.
- Per-repo PR opened in the parent for review.
- Registry pointer updated with final absorb SHA.

## Non-goals

- No mutations to `phenoEvents`, `pheno`, or any other large workspace repo in this batch.
- No deletion of any source repo (per user "zero deletes" rule).
- No mutation of any audit file (supersede-only; the 2026-07-17 audits stay intact per "additive registry entries only" rule).

## Risks

- **WI-1 Cargo.toml conflict:** `phenotype-tooling` already has `clap` pinned; `clap-ext` may bring its own pin. Conflict resolution requires user.
- **WI-2 TS module overlap:** if `Eidolon` and `HexaKit` both have adapter-pattern scaffolding, the two cherry-picks may conflict on type imports. Per-side A1→A3 fallback handles this, but conflict surfacing requires user.
- **WI-4 archive-only risk:** zero — `2phenoEvents` is verified byte-identical to `phenoEvents/src` (MD5 `4a81dec5249e35cd3c7032b512fdc20b`). Archive-only is the correct action.

## Dependencies

- User approval of `audits/absorption-justifications/clap-ext-2026-07-22.md` (supersedes 2026-07-17)
- User approval of `audits/absorption-justifications/agent-platform-2026-07-22.md` (new)
- User approval of `audits/absorption-justifications/Guardrail-2026-07-22.md` (new)
- User approval of `audits/absorption-justifications/2phenoEvents-2026-07-22.md` (new)

## Traceability

| Artifact | Path |
|----------|------|
| Re-verification evidence | `docs/sessions/2026-07-22-absorb-batch-1/REVERIFICATION.md` |
| This spec stub | `docs/sessions/2026-07-22-absorb-batch-1/SPEC_STUB.md` |
| Parent ADR | `docs/adr/ADR-007-absorption-eligibility-boundary.md` |
| Boundary SSOT | `BOUNDARY_OWNERS.md` |
| HexaKit rule | `docs/rationalization/boundary-shaping.md` |
