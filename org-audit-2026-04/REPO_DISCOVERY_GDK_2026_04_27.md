# GDK Discovery Audit - 2026-04-27

## Scope

- Repository: `/Users/kooshapari/CodeProjects/Phenotype/repos/GDK`
- Mode: local-only discovery audit
- Governance repo: `/Users/kooshapari/CodeProjects/Phenotype/phenotype-org-governance`

## Command Results

### Git Status

```text
## main...origin/main [ahead 6, behind 12]
```

### Cargo Check

Command:

```bash
timeout 60 cargo check --workspace 2>&1 | grep -E "^error|^warning:" | sort -u | head -15
```

Filtered findings:

```text
warning: `gdk` (lib) generated 1 warning
warning: value assigned to `commit_counter` is never read
```

Follow-up status check showed `cargo check --workspace` completed within the 60 second limit
with exit status `0`.

### TODO / FIXME / XXX / HACK Markers

Command returned no Rust markers outside `target/` and `.archive/`.

### Rust Line Count

```text
7616 total
```

### Package Count

Requested command result:

```text
0
```

Clarification: `cargo metadata --no-deps` emits a leading compatibility warning before JSON in
this checkout, so piping combined stdout/stderr into `jq` fails before package extraction. Running
metadata with `--format-version 1` reports one package: `gdk`.

## Findings

GDK is a single-package Rust workspace with 7,616 non-archived Rust lines. The checkout is
diverged from origin (`ahead 6, behind 12`). `cargo check --workspace` passes, with one warning for
an unused assignment to `commit_counter`. No TODO/FIXME/XXX/HACK Rust markers were found outside
excluded paths. Metadata parsing should add `--format-version 1` or avoid mixing warning text into
`jq`.
