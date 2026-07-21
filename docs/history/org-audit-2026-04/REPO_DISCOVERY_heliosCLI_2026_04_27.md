# heliosCLI Discovery Audit - 2026-04-27

## Scope

- Repository: `/Users/kooshapari/CodeProjects/Phenotype/repos/heliosCLI`
- Audit mode: local only
- Validation command: `timeout 90 cargo check --workspace`

## Build State

`cargo check --workspace` completed within the 90 second timeout.

Unique diagnostics from the requested filter:

```text
warning: profiles for the non root package will be ignored, specify profiles at the workspace root:
```

- Errors: 0
- Warnings: 1 unique warning
- Build state: warning-only cargo check

## TODO / FIXME / XXX / HACK

- Total Rust markers: 158

Top examples:

```text
./codex-rs/core/tests/common/responses.rs:1101:                // TODO(ccunningham): Update this mock to match future compaction model behavior:
./codex-rs/core/tests/suite/compact.rs:2310:// TODO(ccunningham): Re-enable after the follow-up compaction behavior PR lands.
./codex-rs/core/tests/suite/compact.rs:3097:// TODO(ccunningham): Update once pre-turn compaction includes incoming user input.
./codex-rs/core/tests/suite/compact.rs:3214:// TODO(ccunningham): Update once pre-turn compaction context-overflow handling includes incoming
./codex-rs/core/tests/suite/codex_delegate.rs:27:#[ignore = "TODO once we have a delegate that can ask for approvals"]
```

## Size / Crate Count

- Rust LOC outside `target` and `.archive`: 430,570
- Cargo metadata package count: 10

## Spec Doc Presence

Present:

- `README.md`
- `PRD.md`
- `ADR.md`
- `FUNCTIONAL_REQUIREMENTS.md`
- `PLAN.md`

## Top 3 Actionable Items

1. Move package profile configuration to the workspace root so `cargo check --workspace` is warning-clean.
2. Triage the 158 Rust TODO/FIXME/XXX/HACK markers, starting with ignored or disabled compaction/delegation tests.
3. Split the marker cleanup into test-debt and runtime-debt lanes so high-risk runtime TODOs are not hidden by large test-suite maintenance volume.
