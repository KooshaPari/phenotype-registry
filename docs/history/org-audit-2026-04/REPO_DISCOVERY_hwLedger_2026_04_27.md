# hwLedger Repo Discovery - 2026-04-27

## Scope

- Repository: `/Users/kooshapari/CodeProjects/Phenotype/repos/hwLedger`
- Mode: local-only discovery audit
- Constraint: `cargo check --workspace` capped at 90 seconds

## Git State

```text
## main...origin/main [behind 5]
?? docs-site/design_audit_2026_04_24.md
?? docs/reference/
```

## Build State

Command:

```bash
timeout 90 cargo check --workspace 2>&1 | grep -E "^error|^warning:" | sort -u | head -20
```

Result: the status-preserving rerun timed out at 90 seconds while still compiling/checking dependencies. No unique `error` or `warning:` lines were emitted before timeout.

Tail before timeout:

```text
   Compiling dirs v6.0.0
    Checking dirs v5.0.1
    Checking tower v0.5.3
    Checking num-iter v0.1.45
    Checking http-body-util v0.1.3
   Compiling cargo_toml v0.22.3
   Compiling curve25519-dalek v4.1.3
   Compiling time v0.3.47
   Compiling block-buffer v0.10.4
   Compiling crypto-common v0.1.7
   Compiling embed-resource v3.0.9
    Checking objc2-core-foundation v0.3.2
   Compiling digest v0.10.7
    Checking block2 v0.6.2
    Checking fastrand v2.4.1
   Compiling sha2 v0.10.9
    Checking base16ct v0.2.0
   Compiling tauri-winres v0.3.5
    Checking sec1 v0.7.3
    Checking tempfile v3.27.0
```

## TODO/FIXME Inventory

- Count: 19 Rust matches outside `target/` and `.archive/`

Top examples:

```text
./tools/cli-journey-record/src/main.rs:59:/// TODO(ADR-0036): replace with live probes of `adb devices` and
./tools/docs-health/src/lib.rs:14://! * `check_placeholders` — lingering `TODO` / `TBD` / `PLACEHOLDER` / `REDACTED` markers
./tools/docs-health/src/lib.rs:515:const PLACEHOLDER_MARKERS: &[&str] = &["TODO", "PLACEHOLDER", "REDACTED", "TBD", "FIXME"];
./tools/docs-health/src/lib.rs:708:        write(dir.path(), "node_modules/pkg/README.md", "TODO leak\n");
./tools/docs-health/src/lib.rs:759:        write(dir.path(), "p.md", "line ok\nline TODO finish\n");
./tools/docs-health/src/lib.rs:768:        write(dir.path(), "p.md", "TODO\n");
./tools/user-story-extract/src/lib.rs:401:/// contains an `FR-XXX` token (matching `FR-[A-Z0-9_-]+`) contributes its IDs.
./tools/user-story-extract/src/main.rs:61:    /// FR source (Markdown file with `FR-XXX` tokens). Defaults to PRD.md.
./tools/cli-ansi-parse/src/lib.rs:239:        // would, but asciinema rarely emits it; skip for now (TODO).
./crates/hwledger-ffi/src/lib.rs:180:/// **TODO WP-MoE**: refine resident-vs-active parameter counting.
```

## Size And Package Shape

- Rust LOC: 47,478 total
- Workspace package count: 37

## Spec Doc Presence

Present:

- `README.md`
- `PRD.md`
- `ADR.md`
- `PLAN.md`

Missing from requested set:

- `FUNCTIONAL_REQUIREMENTS.md`

## Top 3 Actionable Items

1. Split the build validation path: the workspace does not finish `cargo check --workspace` inside 90 seconds, so add or document a fast audit profile that checks core crates first and leaves GUI/Tauri-heavy crates to a longer gate.
2. Triage production-facing TODOs in fleet auth, agent/server uptime, SSH connection pooling, and FFI model accounting before counting docs-health fixture TODO strings as engineering debt.
3. Add or intentionally map `FUNCTIONAL_REQUIREMENTS.md` to the existing PRD/ADR/PLAN stack so external audits can find requirements without repo-specific interpretation.
