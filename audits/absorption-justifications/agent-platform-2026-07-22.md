# agent-platform — Absorption Justification

**Status:** NEW (no prior audit exists)
**Date:** 2026-07-22
**Source:** `KooshaPari/agent-platform` (111 KB, 5 branches, last push 2026-06-21)
**Targets (split per A7):**
- `KooshaPari/Eidolon` ← `feat/codex-cli-adapter-2026-06-18`
- `KooshaPari/HexaKit` at `crates/desktop-adapters/` ← `feat/modal-adapters-2026-06-18`
**Disposition:** SPLIT-ABSORB (pending user green-light)

## Confidence

**0.78** — MEDIUM-HIGH. TS project with two genuinely different sibling feature branches. The split destinations match the boundary intent: Eidolon for agent runtime CLI adapters (CodexCliAdapter fits there); HexaKit for hexagonal scaffolding (modal-adapters belongs in the desktop-adapters crate family).

Downgraded to 0.78 from a hypothetical 0.85 because:
- TS module overlap may conflict with Eidolon's existing TS imports.
- `chore/async-trait-2026-06-08` has 10 ahead/15 behind — substantial governance noise that must be filtered, not auto-merged.

## Source state (current remote, 2026-07-22)

| Field | Value |
|-------|-------|
| HEAD SHA | `48853e7` (main, 2026-06-20) |
| Size | 111 KB |
| Archived | NO (unarchived 2026-07-21) |
| Default branch | `main` |
| Tags | none |
| Tree | `AGENTS.md, CODEOWNERS, examples/, ports/, package.json/.lock, tsconfig.json, vitest.config.ts` |
| Working tree | clean |

## Branch inventory

| Branch | Last commit | ahead / behind main | Disposition |
|--------|-------------|---------------------|-------------|
| `main` | `48853e7` (2026-06-20) | — | BASELINE |
| `chore/dependabot-2026-06-08` | `e6bd7d1` (2026-06-08) | 1 / 15 | governance sweep — discard |
| `chore/async-trait-2026-06-08` | `d211bcf` (2026-06-15) | 10 / 15 | **Largest non-default branch** — TBD: depends on whether the 10 ahead are governance noise or substantive async-trait additions |
| `feat/codex-cli-adapter-2026-06-18` | `572e71a` `feat(adapters): CodexCliAdapter` (2026-06-18) | 1 / 10 | **SPLIT-ABSORB → Eidolon** |
| `feat/modal-adapters-2026-06-18` | `ad17d6f` `Merge origin/main into …` (2026-06-18) | 3 / 9 | **SPLIT-ABSORB → HexaKit/crates/desktop-adapters/** (already has a merge commit from main) |
| `chore/v16-cycle6-L7-subsystems-2026-06-21` | `811857d` (2026-06-21) | 1 / 0 | already merged into main |

**Absorb strategy (A7 custom):** Cherry-pick each `feat/*` branch into its respective destination as a single commit. Apply A1→A3 merge discipline per side (try ff-merge; fall back to A3 if conflicts). Discard all `chore/*` branches as governance noise (they are not unique enough to justify a separate absorb).

## What will be absorbed

### Half A → `KooshaPari/Eidolon`

| Item | Source path | Target path | Notes |
|------|-------------|-------------|-------|
| CodexCliAdapter | `ports/codex-cli-adapter/` | `eidolon/src/adapters/codex_cli/` | renamed to follow Eidolon's adapter convention |
| TypeScript types | `ports/codex-cli-adapter/types.ts` | `eidolon/src/adapters/codex_cli/types.ts` | verified-compatible |
| Tests | `ports/codex-cli-adapter/__tests__/` | `eidolon/src/adapters/codex_cli/__tests__/` | vitest-compatible |

### Half B → `KooshaPari/HexaKit` at `crates/desktop-adapters/`

| Item | Source path | Target path | Notes |
|------|-------------|-------------|-------|
| Modal adapters | `ports/modal-adapters/` | `hexakit/crates/desktop-adapters/src/modal/` | hexagonal adapter pattern |
| Examples | `examples/modal-*` | `hexakit/crates/desktop-adapters/examples/modal-*` | usage examples |
| Docs | `docs/modal-adapters.md` | `hexakit/crates/desktop-adapters/docs/modal.md` | |

**Total: ~10 files transferred** (5 + 5 across both halves; matches roughly half the source tree).

## Boundary

New boundary docs to be created:
- `docs/boundary/codex-cli-adapter.md`
- `docs/boundary/desktop-adapters-modal.md`

## Restore procedure

```sh
# Per side:
gh repo unarchive KooshaPari/agent-platform  # only once for both sides

# Eidolon revert
cd /Users/kooshapari/CodeProjects/Phenotype/repos/Eidolon
git revert <codex-cli-adapter-absorb-sha>

# HexaKit revert
cd /Users/kooshapari/CodeProjects/Phenotype/repos/HexaKit
git revert <modal-adapters-absorb-sha>

# Update registry disposition
```

## Verification (pre-mutation)

- [ ] Re-verify `agent-platform` HEAD SHA at moment of mutation (no drift)
- [ ] Confirm `Eidolon` does not already have a `codex_cli` adapter
- [ ] Confirm `HexaKit/crates/desktop-adapters/` does not already have a `modal` module
- [ ] Check `chore/async-trait-2026-06-08`'s 10 unique commits — decide if they should be discarded (likely yes, governance noise) or absorbed separately

## Verification (post-mutation)

- [ ] `npm test` (or `pnpm test`) passes in Eidolon after the CodexCliAdapter absorb
- [ ] `cargo check -p desktop-adapters` passes in HexaKit after the modal-adapters absorb
- [ ] Source repo renamed to `zz-archive-agent-platform` and `archived=true`

## Cross-references

- Source: https://github.com/KooshaPari/agent-platform
- Targets: https://github.com/KooshaPari/Eidolon, https://github.com/KooshaPari/HexaKit
- Session: `docs/sessions/2026-07-22-absorb-batch-1/00_SESSION_OVERVIEW.md`
- Spec stub: `docs/sessions/2026-07-22-absorb-batch-1/SPEC_STUB.md` (WI-2)
- Boundary SSOT: `BOUNDARY_OWNERS.md`
- ADR: `docs/adr/ADR-007-absorption-eligibility-boundary.md`

## Notes

This is the **only repo in the batch that uses an A7 custom split**. The decision rests on the two `feat/*` branches being genuinely different features with different boundary homes (CLI adapter for an agent runtime vs. modal adapter for a desktop framework). If the user prefers a single-destination absorb (e.g., everything into Eidolon), this audit needs revision.

Per user direction 2026-07-22 ("q2 same as q1+A7"): confirmed split with A1→A3 merge discipline per side.
