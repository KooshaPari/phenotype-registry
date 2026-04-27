# TRUE cargo-deny coverage from local clones (avoids gh contents API false-positive bug)

Generated: 2026-04-27 MST.

Scope: local Rust clones with root `Cargo.toml` under `/Users/kooshapari/CodeProjects/Phenotype/repos/*/Cargo.toml`, excluding `.archive`, `.worktrees`, `worktrees`, `*-wtrees`, and `*-wtr` paths. No GitHub API calls were used.

Enumeration command:

```bash
find /Users/kooshapari/CodeProjects/Phenotype/repos -mindepth 2 -maxdepth 2 -name Cargo.toml \
  -not -path '*/.archive/*' \
  -not -path '*/.worktrees/*' \
  -not -path '*/worktrees/*' \
  -not -path '*-wtrees/*' \
  -not -path '*-wtr/*'
```

## TRUE Counts

| Metric | Count |
| --- | ---: |
| Local Rust repos enumerated | 42 |
| Repos with `.github/workflows/cargo-deny.yml` | 18 |
| Repos with `workflow_dispatch:` in `cargo-deny.yml` | 5 |
| Repos with root `deny.toml` | 35 |
| Repos with no `cargo-deny.yml` | 24 |
| Repos with `cargo-deny.yml` but no dispatch trigger | 13 |

## Top Discrepancies vs `d2e1eec` Audit

- `d2e1eec` used GitHub contents/language metadata and reported 61 Rust-scope repos; local root `Cargo.toml` truth enumerates 42 repos.
- `d2e1eec` classified 17 repos as having `cargo-deny.yml`; local truth finds 18.
- `d2e1eec` classified 10 repos as having `workflow_dispatch:`; local truth finds 5.
- `d2e1eec` classified 44 repos as `NO_FILE`; local truth finds 24 among local root Rust clones.
- Earlier completion notes claimed 100% cargo-deny coverage across 36 active Rust repos; local truth shows 18/42 root Rust clones have `cargo-deny.yml`.

Top overlapping repo-level mismatches:

| Repo | `d2e1eec` state | Local state |
| --- | --- | --- |
| `FocalPoint` | `HAS_FILE_AND_DISPATCH` | `HAS_FILE_NO_DISPATCH` |
| `helios-cli` | `HAS_FILE_AND_DISPATCH` | `HAS_FILE_NO_DISPATCH` |
| `KDesktopVirt` | `NO_FILE` | `HAS_FILE_NO_DISPATCH` |
| `PhenoMCP` | `HAS_FILE_AND_DISPATCH` | `HAS_FILE_NO_DISPATCH` |
| `PhenoObservability` | `HAS_FILE_AND_DISPATCH` | `HAS_FILE_NO_DISPATCH` |
| `PhenoPlugins` | `HAS_FILE_AND_DISPATCH` | `HAS_FILE_NO_DISPATCH` |

## Local Truth Table

| Repo | cargo-deny.yml | workflow_dispatch | deny.toml |
| --- | --- | ---: | --- |
| `AgilePlus` | no | 0 | yes |
| `bare-cua` | no | 0 | yes |
| `GDK` | no | 0 | yes |
| `helios-router` | no | 0 | no |
| `HeliosLab` | no | 0 | yes |
| `HexaKit` | no | 0 | no |
| `KlipDot` | no | 0 | yes |
| `kmobile` | no | 0 | yes |
| `pheno` | no | 0 | yes |
| `phenoAI` | no | 0 | no |
| `phenoData` | no | 0 | no |
| `PhenoKits` | no | 0 | no |
| `PhenoProc` | no | 0 | yes |
| `PhenoRuntime` | no | 0 | no |
| `phenoShared` | no | 0 | yes |
| `phenotype-journeys` | no | 0 | yes |
| `phenotype-tooling` | no | 0 | yes |
| `PhenoVCS` | no | 0 | yes |
| `PlayCua` | no | 0 | yes |
| `rich-cli-kit` | no | 0 | yes |
| `thegent-dispatch` | no | 0 | yes |
| `thegent-workspace` | no | 0 | yes |
| `Tokn` | no | 0 | yes |
| `Tracely` | no | 0 | yes |
| `BytePort` | yes | 1 | yes |
| `Civis` | yes | 0 | yes |
| `Configra` | yes | 0 | yes |
| `Eidolon` | yes | 0 | yes |
| `eyetracker` | yes | 0 | no |
| `FocalPoint` | yes | 0 | yes |
| `helios-cli` | yes | 0 | yes |
| `heliosCLI` | yes | 0 | yes |
| `hwLedger` | yes | 0 | yes |
| `KDesktopVirt` | yes | 0 | yes |
| `Metron` | yes | 0 | yes |
| `PhenoMCP` | yes | 0 | yes |
| `PhenoObservability` | yes | 0 | yes |
| `PhenoPlugins` | yes | 0 | yes |
| `phenotype-bus` | yes | 1 | yes |
| `phenoUtils` | yes | 1 | yes |
| `Sidekick` | yes | 1 | yes |
| `Tasken` | yes | 1 | yes |
