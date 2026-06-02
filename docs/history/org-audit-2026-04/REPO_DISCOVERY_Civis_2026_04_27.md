# Civis Repo Discovery - 2026-04-27

## Scope

- Repository: `/Users/kooshapari/CodeProjects/Phenotype/repos/Civis`
- Mode: local-only discovery audit
- Date: 2026-04-27

## Command Results

### Git Status

```text
## main...origin/main [behind 6]
 M Cargo.lock
 M SPEC.md
 M docs/WORKLOG.md
 M docs/worklogs/README.md
 M package.json
?? .github/workflows/cargo-deny.yml
?? CHARTER.md
?? SOTA-CIVILIZATION-SIMULATION.md
?? docs/FUNCTIONAL_REQUIREMENTS.md
?? docs/adr/ADR-001-deterministic-simulation.md
?? docs/adr/ADR-002-ecs-architecture.md
?? docs/adr/ADR-003-policy-institution-modeling.md
?? docs/reference/fr_coverage_matrix.md
?? docs/research/GAME_ENGINES_SOTA.md
?? tests/
?? worklog.md
```

### Cargo Check Diagnostics

Command:

```bash
timeout 60 cargo check --workspace 2>&1 | grep -E "^error|^warning:" | sort -u | head -15
```

Result: no matching `error` or `warning:` lines.

Follow-up capture showed `cargo check --workspace` completed successfully:

```text
Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.21s
```

### Rust TODO/FIXME/XXX/HACK Markers

Command:

```bash
grep -rn "TODO\|FIXME\|XXX\|HACK" --include="*.rs" . 2>/dev/null | grep -v "/target/\|/.archive/" | head -20
```

Result: no matching Rust markers outside `target` and `.archive`.

### Rust Line Count

Command:

```bash
find . -name "*.rs" -not -path "*/target/*" -not -path "*/.archive/*" | xargs wc -l 2>/dev/null | tail -1
```

Result:

```text
721 total
```

Rust files counted:

```text
./crates/engine/src/engine.rs
./crates/engine/src/io.rs
./crates/engine/src/lib.rs
./crates/engine/src/metrics.rs
./crates/engine/src/policy.rs
./crates/server/src/main.rs
./tests/smoke_test.rs
```

### Cargo Package Count

Command:

```bash
cargo metadata --no-deps 2>&1 | jq -r '.packages[].name' 2>/dev/null | wc -l
```

Result:

```text
0
```

Cause: `cargo metadata --no-deps` emitted this warning before the JSON payload, causing jq to reject the mixed stream:

```text
warning: please specify `--format-version` flag explicitly to avoid compatibility problems
```

The valid metadata payload contains two workspace packages after ignoring that warning:

```text
civ-engine
civ-server
```

## Findings

- Build health is clean for the current local checkout: `cargo check --workspace` completes with no captured errors or warnings.
- Rust source surface is small at 721 lines across seven `.rs` files.
- No TODO/FIXME/XXX/HACK markers were found in Rust sources outside excluded paths.
- Workspace metadata has two packages, but the requested jq pipeline returns `0` because Cargo's format-version warning contaminates stdout/stderr JSON parsing.
- The Civis worktree is dirty and behind `origin/main` by six commits; discovery did not modify it.
