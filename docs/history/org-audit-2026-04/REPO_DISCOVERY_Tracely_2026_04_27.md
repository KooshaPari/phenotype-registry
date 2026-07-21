# Tracely Repo Discovery Audit - 2026-04-27

Scope: local-only discovery audit for
`/Users/kooshapari/CodeProjects/Phenotype/repos/Tracely`.

## Git State

Requested command:

```bash
git status --short --branch
```

Result:

```text
## chore/dead-code-phase1-tracely...origin/chore/dead-code-phase1-tracely
 M ADR.md
 M Cargo.toml
 M PRD.md
 M SPEC.md
 m crates/pheno-logging-zig
 M crates/tracely-sentinel/.agileplus/worklog.md
 M crates/tracely-sentinel/Cargo.toml
 M crates/tracely-sentinel/worklog.md
 ? crates/zerokit
 M docs/worklogs/README.md
?? CHARTER.md
?? SOTA.md
?? crates/tracely-core/tests/
?? crates/tracely-sentinel/docs/adr/
?? docs/FUNCTIONAL_REQUIREMENTS.md
?? docs/adr/
?? docs/reference/
?? docs/research/
?? worklog.md
```

The checkout already has modified and untracked work. This audit did not edit
the Tracely repository.

## Build State

Requested command:

```bash
timeout 60 cargo check --workspace 2>&1 | grep -E "^error|^warning:" | sort -u | head -15
```

Result: no matching `error` or `warning:` lines were emitted before the
60-second cutoff.

## TODO / FIXME / XXX / HACK

Requested command:

```bash
grep -rn "TODO\|FIXME\|XXX\|HACK" --include="*.rs" . 2>/dev/null | grep -v "/target/\|/.archive/" | head -20
```

Result: no matching Rust source lines outside `target` and `.archive`.

## LOC and Package Count

Requested Rust LOC command:

```bash
find . -name "*.rs" -not -path "*/target/*" -not -path "*/.archive/*" | xargs wc -l 2>/dev/null | tail -1
```

Result:

```text
    1792 total
```

Requested package-count command:

```bash
cargo metadata --no-deps 2>&1 | jq -r '.packages[].name' 2>/dev/null | wc -l
```

Result:

```text
       0
```

Note: the exact pipeline reports `0` because Cargo emits a compatibility warning
before the JSON payload. Raw `cargo metadata --no-deps` shows two workspace
packages: `tracely` and `phenotype-sentinel`.

## Top Actionable Findings

1. The workspace is not clean; preserve the active branch work before any
   stabilization or cleanup pass.
2. The filtered build check has no immediate compiler errors or warning lines,
   but it did not finish within the requested 60-second window.
3. Rust source footprint is small at 1,792 lines across two metadata-visible
   packages, with no TODO/FIXME/XXX/HACK debt found by the requested scan.
