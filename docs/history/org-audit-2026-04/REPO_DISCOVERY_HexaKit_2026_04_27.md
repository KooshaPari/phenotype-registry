# HexaKit Repo Discovery Audit - 2026-04-27

Scope: local-only discovery audit for
`/Users/kooshapari/CodeProjects/Phenotype/repos/HexaKit`.

## Repository State

Requested command:

```bash
git status --short --branch
```

Result: `HexaKit` resolves inside the parent `repos` git checkout, not as an
isolated repository root.

```text
## chore/gitignore-worktrees-2026-04-26...origin/chore/gitignore-worktrees-2026-04-26 [ahead 54]
```

The status output includes many unrelated parent-shelf modified and nested
worktree entries outside `HexaKit`; those were not changed for this audit.

## Build State

Requested command:

```bash
timeout 60 cargo check --workspace 2>&1 | grep -E "^error|^warning:" | sort -u | head -15
```

Filtered output:

```text
error: failed to load manifest for workspace member `/Users/kooshapari/CodeProjects/Phenotype/repos/HexaKit/crates/phenotype-bdd`
```

Status-preserving rerun showed the underlying manifest parse failure:

```text
error: failed to load manifest for workspace member `/Users/kooshapari/CodeProjects/Phenotype/repos/HexaKit/crates/phenotype-bdd`
referenced by workspace at `/Users/kooshapari/CodeProjects/Phenotype/repos/HexaKit/Cargo.toml`

Caused by:
  failed to parse manifest at `/Users/kooshapari/CodeProjects/Phenotype/repos/HexaKit/crates/phenotype-bdd/Cargo.toml`

Caused by:
  no targets specified in the manifest
  either src/lib.rs, src/main.rs, a [lib] section, or [[bin]] section must be present
```

Build state: blocked before Rust compilation by an invalid workspace member
manifest.

## TODO / FIXME / XXX / HACK

Requested command:

```bash
grep -rn "TODO\|FIXME\|XXX\|HACK" --include="*.rs" . 2>/dev/null | grep -v "/target/\|/.archive/" | head -20
```

Result: no matching Rust TODO/FIXME/XXX/HACK lines surfaced in the first 20
results.

## LOC and Crate Count

Requested Rust LOC command:

```bash
find . -name "*.rs" -not -path "*/target/*" -not -path "*/.archive/*" | xargs wc -l 2>/dev/null | tail -1
```

Result:

```text
682 total
```

Requested package-count command:

```bash
cargo metadata --no-deps 2>&1 | jq -r '.packages[].name' 2>/dev/null | wc -l
```

Result:

```text
0
```

The zero count is not evidence of an empty workspace; `cargo metadata` fails on
the same `crates/phenotype-bdd` no-target manifest before emitting package JSON.

## Top Actionable Items

1. Repair or remove the `crates/phenotype-bdd` workspace member so `cargo check`
   and `cargo metadata` can load the workspace.
2. Re-run `cargo metadata --no-deps` after the manifest fix to get a real
   package count; the requested jq pipeline currently reports `0` because Cargo
   emits an error instead of JSON.
3. Treat HexaKit as a template/kits surface during follow-up triage; do not use
   it as a destination for product/workspace crates without separate evidence.
