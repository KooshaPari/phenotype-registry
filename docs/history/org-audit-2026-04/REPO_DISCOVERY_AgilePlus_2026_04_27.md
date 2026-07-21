# AgilePlus Repo Discovery Audit - 2026-04-27

Scope: local-only discovery audit for
`/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus`.

## Build State

Requested command:

```bash
timeout 90 cargo check --workspace 2>&1 | grep -E "^error|^warning:" | sort -u | head -20
```

Result: not completed in this Codex run because the local shell execution wrapper
failed before launching commands with:

```text
zsh fork feature enabled, but execve wrapper is not configured
```

No `cargo check` errors or warnings were captured.

## TODO / FIXME / XXX / HACK

Command-equivalent local filesystem scan, excluding `target` and `.archive`,
found 18 matching Rust lines. Top examples:

```text
.claude/worktrees/agent-a699a818/crates/agileplus-domain/src/credentials/file.rs:34:    /// TODO (SECURITY): Implement full AES-256-GCM + Argon2id encryption:
.worktrees/chore-governance-baseline/crates/agileplus-domain/src/credentials/file.rs:34:    /// TODO (SECURITY): Implement full AES-256-GCM + Argon2id encryption:
.worktrees/dashboard-extraction/crates/agileplus-domain/src/credentials/file.rs:34:    /// TODO (SECURITY): Implement full AES-256-GCM + Argon2id encryption:
.worktrees/refactor-cli-event-flow/crates/agileplus-domain/src/credentials/file.rs:34:    /// TODO (SECURITY): Implement full AES-256-GCM + Argon2id encryption:
crates/agileplus-domain/src/credentials/file.rs:34:    /// TODO (SECURITY): Implement full AES-256-GCM + Argon2id encryption:
crates/agileplus-dashboard/src/process_detector.rs:107:    // Look for task identifiers like WP13, FR-XXX, etc. in command line
```

Canonical tree examples are duplicated across local worktree directories because
the requested grep excludes only `target` and `.archive`.

## LOC and Crate Count

- Rust files scanned: 4,698
- Rust LOC from command-equivalent scan: 698,043
- Workspace members in root `Cargo.toml`: 41
- `cargo metadata --no-deps` package count: not executed because shell command
  launch is blocked; root workspace member count is 41.

## Spec Doc Presence

Present:

```text
README.md
PRD.md
ADR.md
FUNCTIONAL_REQUIREMENTS.md
PLAN.md
```

## Top 3 Actionable Items

1. Run the requested 90-second `cargo check --workspace` once local command
   execution is restored; this audit has no build error/warning capture.
2. Prioritize `crates/agileplus-domain/src/credentials/file.rs` because the
   canonical TODO is security-sensitive encryption work.
3. Separate canonical tree audit metrics from local worktree clones in follow-up
   reporting, or explicitly exclude `.worktrees`, `.claude/worktrees`, and
   `AgilePlus-wtrees` when the goal is source-of-truth metrics.
