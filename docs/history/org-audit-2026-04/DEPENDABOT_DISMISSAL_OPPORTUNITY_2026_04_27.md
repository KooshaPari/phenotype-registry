# Dependabot Dismissal Opportunity - 2026-04-27

Read-only audit. No Dependabot alerts were dismissed.

## Scope and Method

- Source: `CARGO_DENY_100_PERCENT_2026_04_27.md` enrolled-repo list, then live `gh api` checks.
- For each non-archived candidate, fetched remote `deny.toml` via `gh api repos/KooshaPari/<repo>/contents/deny.toml` and extracted `RUSTSEC-*` suppressions.
- Fetched open Dependabot alerts with `gh api repos/KooshaPari/<repo>/dependabot/alerts?state=open&per_page=100`.
- Direct GitHub alert identifiers were compared to suppressed RUSTSEC IDs. Because GitHub returned GHSA/CVE identifiers for Rust alerts, the audit also cross-checked aliases from `/Users/kooshapari/.cargo/advisory-dbs/advisory-db-3157b0e258782691`.

## Summary

| Metric | Count |
|---|---:|
| Source candidates from enrolled report | 46 |
| Scanned with remote deny.toml | 35 |
| Repos with suppressed RUSTSEC IDs | 10 |
| Open Dependabot alerts in scanned repos | 71 |
| Direct identifier matches dismissable without code | 0 |
| RustSec alias-mapped matches dismissable without code | 0 |
| Alerts needing real fixes | 71 |

Result: **0 open alerts are dismissable solely because their RustSec ID is already suppressed in remote `deny.toml`**. All 71 open alerts in scanned repos need package/workspace fixes or a new suppression decision.

## Repo Results

Sorted by dismissable count descending, then open alert count descending.

| Repo | Suppressed RUSTSEC IDs | Open alerts | Dismissable | Needs fixes | Severities |
|---|---|---:|---:|---:|---|
| `heliosCLI` | `RUSTSEC-2025-0134`, `RUSTSEC-2025-0140`, `RUSTSEC-2026-0049` | 18 | 0 | 18 | high:4, low:7, medium:7 |
| `BytePort` | `RUSTSEC-2024-0370`, `RUSTSEC-2024-0411`, `RUSTSEC-2024-0412`, `RUSTSEC-2024-0413`, `RUSTSEC-2024-0414`, `RUSTSEC-2024-0415`, `RUSTSEC-2024-0416`, `RUSTSEC-2024-0417`, `RUSTSEC-2024-0418`, `RUSTSEC-2024-0419`, `RUSTSEC-2024-0420`, `RUSTSEC-2025-0057`, `RUSTSEC-2025-0075`, `RUSTSEC-2025-0080`, `RUSTSEC-2025-0081`, `RUSTSEC-2025-0098`, `RUSTSEC-2025-0100` | 16 | 0 | 16 | low:5, medium:11 |
| `pheno` | `RUSTSEC-2025-0134`, `RUSTSEC-2025-0140`, `RUSTSEC-2026-0002`, `RUSTSEC-2026-0049` | 9 | 0 | 9 | high:4, low:2, medium:3 |
| `HexaKit` | `RUSTSEC-2025-0134`, `RUSTSEC-2025-0140`, `RUSTSEC-2026-0002`, `RUSTSEC-2026-0049` | 8 | 0 | 8 | high:2, medium:6 |
| `PhenoRuntime` | none | 6 | 0 | 6 | high:1, low:4, medium:1 |
| `KDesktopVirt` | `RUSTSEC-2024-0320` | 5 | 0 | 5 | high:1, low:2, medium:2 |
| `AgilePlus` | none | 4 | 0 | 4 | high:1, medium:3 |
| `HeliosLab` | none | 3 | 0 | 3 | low:1, medium:2 |
| `helios-router` | none | 2 | 0 | 2 | medium:2 |
| `Tracely` | none | 0 | 0 | 0 | none |
| `Tokn` | none | 0 | 0 | 0 | none |
| `thegent-workspace` | none | 0 | 0 | 0 | none |
| `thegent-dispatch` | none | 0 | 0 | 0 | none |
| `Tasken` | `RUSTSEC-2025-0134`, `RUSTSEC-2025-0140`, `RUSTSEC-2026-0049` | 0 | 0 | 0 | none |
| `Sidekick` | none | 0 | 0 | 0 | none |
| `rich-cli-kit` | none | 0 | 0 | 0 | none |
| `PlayCua` | none | 0 | 0 | 0 | none |
| `PhenoVCS` | none | 0 | 0 | 0 | none |
| `phenoUtils` | `RUSTSEC-2025-0134`, `RUSTSEC-2025-0140`, `RUSTSEC-2026-0049` | 0 | 0 | 0 | none |
| `phenotype-tooling` | none | 0 | 0 | 0 | none |
| `phenotype-journeys` | none | 0 | 0 | 0 | none |
| `phenotype-bus` | none | 0 | 0 | 0 | none |
| `phenoShared` | none | 0 | 0 | 0 | none |
| `PhenoProc` | none | 0 | 0 | 0 | none |
| `PhenoObservability` | `RUSTSEC-2024-0437`, `RUSTSEC-2026-0105` | 0 | 0 | 0 | none |
| `PhenoMCP` | `RUSTSEC-2026-0098`, `RUSTSEC-2026-0099`, `RUSTSEC-2026-0104` | 0 | 0 | 0 | none |
| `PhenoKits` | none | 0 | 0 | 0 | none |
| `phenoData` | none | 0 | 0 | 0 | none |
| `phenoAI` | none | 0 | 0 | 0 | none |
| `Metron` | none | 0 | 0 | 0 | none |
| `helios-cli` | `RUSTSEC-2025-0134`, `RUSTSEC-2025-0140`, `RUSTSEC-2026-0049` | 0 | 0 | 0 | none |
| `Eidolon` | none | 0 | 0 | 0 | none |
| `Configra` | none | 0 | 0 | 0 | none |
| `Civis` | none | 0 | 0 | 0 | none |
| `bare-cua` | none | 0 | 0 | 0 | none |

## Top Repos by Remaining Real-Fix Alerts

| Repo | Needs fixes | Open alerts | Suppressed IDs present? |
|---|---:|---:|---|
| `heliosCLI` | 18 | 18 | yes |
| `BytePort` | 16 | 16 | yes |
| `pheno` | 9 | 9 | yes |
| `HexaKit` | 8 | 8 | yes |
| `PhenoRuntime` | 6 | 6 | no |

## Skipped Candidates

These source-list candidates could not be evaluated under the requested remote-`deny.toml` method.

| Repo | Reason | Detail |
|---|---|---|
| `agentapi-plusplus` | no remote deny.toml | gh: Not Found (HTTP 404) |
| `agentkit` | repo metadata error | gh: Not Found (HTTP 404) |
| `eyetracker` | no remote deny.toml | gh: Not Found (HTTP 404) |
| `FocalPoint` | no remote deny.toml | gh: Not Found (HTTP 404) |
| `FocalPoint-vitepress` | repo metadata error | gh: Not Found (HTTP 404) |
| `GDK` | no remote deny.toml | gh: Not Found (HTTP 404) |
| `helios-app` | repo metadata error | gh: Not Found (HTTP 404) |
| `hwLedger` | no remote deny.toml | gh: Not Found (HTTP 404) |
| `KDV` | repo metadata error | gh: Not Found (HTTP 404) |
| `PhenoPlugins` | no remote deny.toml | gh: Not Found (HTTP 404) |
| `Pyron` | repo metadata error | gh: Not Found (HTTP 404) |

## Evidence Notes

- Current live GitHub alert identifiers for Rust alerts did not include `RUSTSEC-*` values; examples were GHSA/CVE-only.
- The RustSec advisory DB alias pass also found zero overlaps with the remote `deny.toml` suppression sets.
- This is an audit-only report; no `dependabot/alerts/<id>` dismissal endpoint was called.
