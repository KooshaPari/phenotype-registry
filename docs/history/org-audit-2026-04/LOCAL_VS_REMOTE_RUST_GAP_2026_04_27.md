# Local vs Remote Rust Repo Gap - 2026-04-27

## Summary

The local checkout scan found 43 unique `Cargo.toml` repository directories under
`/Users/kooshapari/CodeProjects/Phenotype/repos` using the provided max-depth
command. The cached remote inventory at `/tmp/phenotype-rust-repos-20260427.json`
contains 61 active remote repositories with Rust present in their language list.

The direct name diff shows 22 active remote Rust repositories that are not checked
out locally. The count is higher than the headline 18-repo gap because four local
Rust names are not in the active remote Rust set: `bare-cua`, `KlipDot`, `kmobile`,
and `repos`.

## Method

Local list:

```bash
find /Users/kooshapari/CodeProjects/Phenotype/repos -maxdepth 2 -name Cargo.toml \
  -path "*/Cargo.toml" 2>/dev/null \
  | grep -v -E 'wtrees|\.archive|\.worktrees|target' \
  | xargs -I{} dirname {} \
  | xargs -I{} basename {} \
  | sort -u > /tmp/local_rust.txt
```

Remote list:

```bash
jq -r '.[] | select(.isArchived == false and any(.languages[]?; .node.name == "Rust")) | .name' \
  /tmp/phenotype-rust-repos-20260427.json \
  | sort -u > /tmp/remote_rust_any_active.txt
```

Diff:

```bash
comm -23 /tmp/remote_rust_any_active.txt /tmp/local_rust.txt > /tmp/missing_local_rust.txt
```

## Missing Local Checkouts

| Remote repo | Recommendation |
| --- | --- |
| `Agentora` | Clone locally or document why this active Rust repo is intentionally excluded. |
| `Apisync` | Clone locally or document why this active Rust repo is intentionally excluded. |
| `AuthKit` | Clone locally or document why this active Rust repo is intentionally excluded. |
| `Benchora` | Clone locally or document why this active Rust repo is intentionally excluded. |
| `DataKit` | Clone locally or document why this active Rust repo is intentionally excluded. |
| `Dino` | Clone locally or document why this active Rust repo is intentionally excluded. |
| `MCPForge` | Clone locally or document why this active Rust repo is intentionally excluded. |
| `McpKit` | Clone locally or document why this active Rust repo is intentionally excluded. |
| `ObservabilityKit` | Clone locally or document why this active Rust repo is intentionally excluded. |
| `Paginary` | Clone locally or document why this active Rust repo is intentionally excluded. |
| `PhenoAgent` | Clone locally or document why this active Rust repo is intentionally excluded. |
| `PhenoCompose` | Clone locally or document why this active Rust repo is intentionally excluded. |
| `PhenoLang` | Clone locally or document why this active Rust repo is intentionally excluded. |
| `phenotype-infra` | Clone locally or document why this active Rust repo is intentionally excluded. |
| `phenotype-org-audits` | Clone locally or document why this active Rust repo is intentionally excluded. |
| `PolicyStack` | Clone locally or document why this active Rust repo is intentionally excluded. |
| `ResilienceKit` | Clone locally or document why this active Rust repo is intentionally excluded. |
| `Stashly` | Clone locally or document why this active Rust repo is intentionally excluded. |
| `TestingKit` | Clone locally or document why this active Rust repo is intentionally excluded. |
| `thegent` | Clone locally or document why this active Rust repo is intentionally excluded. |
| `Tracera` | Clone locally or document why this active Rust repo is intentionally excluded. |
| `vibeproxy` | Clone locally or document why this active Rust repo is intentionally excluded. |

## Next Action

Create a tracked exclusion manifest for intentionally omitted active Rust repos.
Everything else in this list should be cloned into the local repo shelf before the
next governance inventory pass.
