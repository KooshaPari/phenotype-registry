# helios-cli Local Discovery Audit - 2026-04-27

## Scope

- Repository: `/Users/kooshapari/CodeProjects/Phenotype/repos/helios-cli`
- Mode: local-only discovery audit
- Requested cargo timeout: 90 seconds

## Repository State

```text
## main...origin/main [behind 3]
 M CHANGELOG.md
 M Cargo.toml
```

The checkout exists and was audited in place. Existing local modifications were left untouched.

## Build State

Command:

```bash
timeout 90 cargo check --workspace 2>&1 | grep -E "^error|^warning:" | sort -u | head -20
```

Result: no matching `error` or `warning:` lines were emitted. `cargo check --workspace`
completed within the requested timeout.

## TODO / FIXME Inventory

- Total Rust TODO/FIXME/XXX/HACK matches: 211
- Top examples:

```text
./codex-rs/core/tests/common/responses.rs:1068:                // TODO(ccunningham): Update this mock to match future compaction model behavior:
./codex-rs/core/tests/suite/compact.rs:2231:// TODO(ccunningham): Re-enable after the follow-up compaction behavior PR lands.
./codex-rs/core/tests/suite/compact.rs:2988:// TODO(ccunningham): Update once pre-turn compaction includes incoming user input.
./codex-rs/core/tests/suite/compact.rs:3107:// TODO(ccunningham): Update once pre-turn compaction context-overflow handling includes incoming
./codex-rs/core/tests/suite/codex_delegate.rs:27:#[ignore = "TODO once we have a delegate that can ask for approvals"]
./codex-rs/core/tests/suite/codex_delegate.rs:119:#[ignore = "TODO once we have a delegate that can ask for approvals"]
./codex-rs/core/tests/suite/cli_stream.rs:70:    // TODO(jif) fix
./codex-rs/core/tests/suite/exec_policy.rs:82:    // TODO execpolicy doesn't parse powershell commands yet
./codex-rs/core/tests/suite/compact_remote.rs:1090:// TODO(ccunningham): Re-enable after the follow-up compaction behavior PR lands.
./codex-rs/core/tests/suite/compact_remote.rs:1967:// TODO(ccunningham): Update once remote pre-turn compaction includes incoming user input.
```

## Size and Package Count

- Rust LOC, excluding `target` and `.archive`: 720,055
- Cargo package count: 1
- Package: `helios`

Note: the exact requested pipeline without `--format-version` can report `0` because
`cargo metadata --no-deps` emits a compatibility warning before JSON. Re-running with
`--format-version 1` returned the package above.

## Spec Document Presence

All requested root spec documents are present:

```text
ADR.md
FUNCTIONAL_REQUIREMENTS.md
PLAN.md
PRD.md
README.md
```

## Top 3 Actionable Items

1. Resolve the repository hygiene drift first: local `CHANGELOG.md` and `Cargo.toml`
   edits are present while the branch is three commits behind `origin/main`.
2. Triage the 211 Rust TODO/FIXME/XXX/HACK matches by cluster, starting with ignored
   compaction/delegation tests and dynamic tool registry TODOs in `codex-rs/core`.
3. Repair the root `AGENTS.md` merge-conflict markers before using it as a reliable
   agent contract for future implementation work.
