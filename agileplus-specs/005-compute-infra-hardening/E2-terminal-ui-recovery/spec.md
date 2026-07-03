# E2 — Lift recovered terminal UI to branch + open PR

## Unit
- **ID:** E2
- **Repo:** BytePort (KooshaPari/BytePort)
- **Epic:** epic_E — BytePort: terminal UI, tools CLI, otel, governance
- **Type:** recover
- **Owner:** koosh
- **Status:** IN FLIGHT

## Summary
E1 recovered the terminal UI worktree from stash side-219, materializing the `byteport-transport` crate with the `UiPort` trait abstraction (`ui.rs`), a terminal/stdin adapter (`terminal_ui.rs`), and a `MockUiAdapter` for testing. The code landed on `main` via PR #248, and the DAG foundation was independently absorbed via Phase-6.

E2 documents the completion, updates the grade report, appends the worklog, and opens (or finalizes) a PR that captures the full DAG-compatible audit trail.

## Background
- **PR #252** was opened 2026-06-26 as the E2 tracking PR but is now stale (merge conflicts, failing CI, no reviews)
- The `byteport-transport` crate's terminal UI code (`terminal_ui.rs`, `ui.rs`, `mod.rs`) is already on `main`
- The `byteport-dag` crate (5 modules) is also on `main`
- 22 CI checks are failing on PR #252 — many are pre-existing infrastructure issues

## Acceptance Criteria
1. Terminal UI source files verified present on `main` (`crates/byteport-transport/src/ports/terminal_ui.rs`, `ui.rs`, `mod.rs`)
2. `cargo check --workspace` passes on the current working tree
3. `grade.sh --json` runs successfully and produces a grade report
4. Worklog entry appended with E2 completion details
5. PR #252 updated with current diff, or superseding PR opened
6. Branch pushed: `recover/E2-terminal-ui-pr` (fresh from main)

## Dependencies
- E1 (terminal UI recovery) — DONE (PR #248 merged)
- A11 (verify stash cleanup) — DONE (PR #221 merged)

## Gates
- [ ] Tier-0: cargo build, test-unit, fmt, clippy all pass
- [ ] Tier-1: cargo audit clean
- [ ] Tier-2: coverage >= 71% (where applicable)
- [ ] Cross-repo: phenotype-registry entry updated
