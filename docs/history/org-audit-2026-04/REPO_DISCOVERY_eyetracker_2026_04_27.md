# Repo Discovery: eyetracker

Date: 2026-04-27
Path: `/Users/kooshapari/CodeProjects/Phenotype/repos/eyetracker`
Mode: local-only discovery audit

## Command Results

### Git Status

```text
## main...origin/main [behind 2]
```

### Cargo Check Filter

Command:

```bash
timeout 60 cargo check --workspace 2>&1 | grep -E "^error|^warning:" | sort -u | head -15
```

Filtered result: no matching `error` or `warning:` lines.

### Rust TODO Markers

Command:

```bash
grep -rn "TODO\|FIXME\|XXX\|HACK" --include="*.rs" . 2>/dev/null | grep -v "/target/\|/.archive/" | head -20
```

Result: no matching Rust markers outside `target/` and `.archive/`.

### Rust Line Count

```text
1001 total
```

### Cargo Package Count

Requested pipeline:

```bash
cargo metadata --no-deps 2>&1 | jq -r '.packages[].name' 2>/dev/null | wc -l
```

Result:

```text
0
```

Interpretation: the requested pipeline combines stderr with stdout. On this checkout, Cargo emits
`warning: please specify --format-version flag explicitly to avoid compatibility problems`, which
prevents `jq` from parsing the JSON stream. A raw metadata check shows four workspace packages:
`eyetracker-domain`, `eyetracker-math`, `eyetracker-core`, and `eyetracker-ffi`.

## Findings

`eyetracker` is a small Rust workspace with 1,001 non-archived Rust lines and four packages.
The requested cargo-check warning/error filter was clean, and no TODO/FIXME/XXX/HACK Rust markers
were found outside ignored paths. The canonical checkout is on `main` but behind `origin/main` by
two commits, so current local discovery may trail remote state.
