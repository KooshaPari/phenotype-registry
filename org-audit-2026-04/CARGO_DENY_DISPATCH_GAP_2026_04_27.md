# Cargo Deny Workflow Dispatch Gap Audit - 2026-04-27

Scope: non-archived `KooshaPari` repositories whose GitHub language metadata includes Rust or whose primary language is Rust.

This replaces the earlier incorrect audit that treated base64 content and missing files incorrectly. The check used fresh GitHub API data and an exit-status guard so 404 responses are classified as `NO_FILE`, not as decoded workflow content.

Requested content check:

```bash
content=$(gh api repos/KooshaPari/$r/contents/.github/workflows/cargo-deny.yml --jq .content 2>/dev/null)
decoded=$(printf "%s" "$content" | base64 -d)
printf "%s" "$decoded" | rg -q "^\s*workflow_dispatch\s*:"
```

Tri-state definitions:

- `HAS_FILE_AND_DISPATCH`: `.github/workflows/cargo-deny.yml` exists and decoded content contains `workflow_dispatch:`.
- `HAS_FILE_NO_DISPATCH`: `.github/workflows/cargo-deny.yml` exists but decoded content lacks `workflow_dispatch:`.
- `NO_FILE`: `.github/workflows/cargo-deny.yml` is absent.

Coverage summary:

| State | Count | Share |
| --- | ---: | ---: |
| HAS_FILE_AND_DISPATCH | 10 | 16.4% |
| HAS_FILE_NO_DISPATCH | 7 | 11.5% |
| NO_FILE | 44 | 72.1% |
| TOTAL | 61 | 100.0% |

Top actual `cargo-deny.yml` dispatch gaps:

| Priority | Repo | Gap |
| ---: | --- | --- |
| 1 | `Civis` | cargo-deny.yml exists but lacks workflow_dispatch |
| 2 | `Configra` | cargo-deny.yml exists but lacks workflow_dispatch |
| 3 | `Eidolon` | cargo-deny.yml exists but lacks workflow_dispatch |
| 4 | `eyetracker` | cargo-deny.yml exists but lacks workflow_dispatch |
| 5 | `heliosCLI` | cargo-deny.yml exists but lacks workflow_dispatch |

Full corrected tri-state table:

| Repo | State | Decoded lines |
| --- | --- | ---: |
| `Agentora` | `NO_FILE` | 0 |
| `AgilePlus` | `NO_FILE` | 0 |
| `Apisync` | `NO_FILE` | 0 |
| `AuthKit` | `NO_FILE` | 0 |
| `Benchora` | `NO_FILE` | 0 |
| `BytePort` | `HAS_FILE_AND_DISPATCH` | 30 |
| `Civis` | `HAS_FILE_NO_DISPATCH` | 29 |
| `Configra` | `HAS_FILE_NO_DISPATCH` | 29 |
| `DataKit` | `NO_FILE` | 0 |
| `Dino` | `NO_FILE` | 0 |
| `Eidolon` | `HAS_FILE_NO_DISPATCH` | 29 |
| `eyetracker` | `HAS_FILE_NO_DISPATCH` | 29 |
| `FocalPoint` | `HAS_FILE_AND_DISPATCH` | 30 |
| `GDK` | `NO_FILE` | 0 |
| `helios-cli` | `HAS_FILE_AND_DISPATCH` | 26 |
| `helios-router` | `NO_FILE` | 0 |
| `heliosCLI` | `HAS_FILE_NO_DISPATCH` | 28 |
| `HeliosLab` | `NO_FILE` | 0 |
| `HexaKit` | `NO_FILE` | 0 |
| `hwLedger` | `HAS_FILE_NO_DISPATCH` | 29 |
| `KDesktopVirt` | `NO_FILE` | 0 |
| `MCPForge` | `NO_FILE` | 0 |
| `McpKit` | `NO_FILE` | 0 |
| `Metron` | `HAS_FILE_NO_DISPATCH` | 29 |
| `ObservabilityKit` | `NO_FILE` | 0 |
| `Paginary` | `NO_FILE` | 0 |
| `pheno` | `NO_FILE` | 0 |
| `PhenoAgent` | `NO_FILE` | 0 |
| `phenoAI` | `NO_FILE` | 0 |
| `PhenoCompose` | `NO_FILE` | 0 |
| `phenoData` | `NO_FILE` | 0 |
| `PhenoKits` | `NO_FILE` | 0 |
| `PhenoLang` | `NO_FILE` | 0 |
| `PhenoMCP` | `HAS_FILE_AND_DISPATCH` | 30 |
| `PhenoObservability` | `HAS_FILE_AND_DISPATCH` | 64 |
| `PhenoPlugins` | `HAS_FILE_AND_DISPATCH` | 30 |
| `PhenoProc` | `NO_FILE` | 0 |
| `PhenoRuntime` | `NO_FILE` | 0 |
| `phenoShared` | `NO_FILE` | 0 |
| `phenotype-bus` | `HAS_FILE_AND_DISPATCH` | 30 |
| `phenotype-infra` | `NO_FILE` | 0 |
| `phenotype-journeys` | `NO_FILE` | 0 |
| `phenotype-org-audits` | `NO_FILE` | 0 |
| `phenotype-tooling` | `NO_FILE` | 0 |
| `phenoUtils` | `HAS_FILE_AND_DISPATCH` | 30 |
| `PhenoVCS` | `NO_FILE` | 0 |
| `PlayCua` | `NO_FILE` | 0 |
| `PolicyStack` | `NO_FILE` | 0 |
| `ResilienceKit` | `NO_FILE` | 0 |
| `rich-cli-kit` | `NO_FILE` | 0 |
| `Sidekick` | `HAS_FILE_AND_DISPATCH` | 30 |
| `Stashly` | `NO_FILE` | 0 |
| `Tasken` | `HAS_FILE_AND_DISPATCH` | 30 |
| `TestingKit` | `NO_FILE` | 0 |
| `thegent` | `NO_FILE` | 0 |
| `thegent-dispatch` | `NO_FILE` | 0 |
| `thegent-workspace` | `NO_FILE` | 0 |
| `Tokn` | `NO_FILE` | 0 |
| `Tracely` | `NO_FILE` | 0 |
| `Tracera` | `NO_FILE` | 0 |
| `vibeproxy` | `NO_FILE` | 0 |

Notes:

- `BytePort` is correctly classified as `HAS_FILE_AND_DISPATCH`.
- `AgilePlus` is correctly classified as `NO_FILE` for `cargo-deny.yml`; it has other security workflows, but not `.github/workflows/cargo-deny.yml` in this audit target.
