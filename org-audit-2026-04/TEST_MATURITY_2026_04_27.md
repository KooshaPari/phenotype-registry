# Test Maturity Audit - 2026-04-27

Source: live GitHub API checks against `KooshaPari/<repo>` on 2026-04-27.

Scope: non-archived repositories from the requested governance set. Archived or unavailable repositories are listed after the active table and excluded from percentage denominators.

Level 3 proxy checks audited here: repository test directory (`tests/` or `test/`), `codecov.yml`, and `.github/workflows/quality-gate.yml`.

## Coverage Summary

- Active repositories audited: 32
- Has tests directory: 22/32 (68.8%)
- Has Codecov config: 6/32 (18.8%)
- Has quality gate workflow: 22/32 (68.8%)
- Full proxy maturity, 3/3 checks: 5/32 (15.6%)
- Partial maturity, 1-2 checks: 24/32 (75.0%)
- No audited maturity signals: 3/32 (9.4%)

## Repository Matrix

| Rank | Repository | Score | Tests dir | Codecov config | Quality gate workflow | Notes |
|---:|---|---:|---|---|---|---|
| 1 | `KooshaPari/AgilePlus` | 3/3 | yes | yes | yes |  |
| 2 | `KooshaPari/HexaKit` | 3/3 | yes | yes | yes |  |
| 3 | `KooshaPari/PhenoProc` | 3/3 | yes | yes | yes |  |
| 4 | `KooshaPari/PolicyStack` | 3/3 | yes | yes | yes |  |
| 5 | `KooshaPari/Tokn` | 3/3 | yes | yes | yes |  |
| 6 | `KooshaPari/agentapi-plusplus` | 2/3 | yes | no | yes |  |
| 7 | `KooshaPari/Eidolon` | 2/3 | yes | no | yes |  |
| 8 | `KooshaPari/FocalPoint` | 2/3 | yes | no | yes |  |
| 9 | `KooshaPari/GDK` | 2/3 | yes | no | yes |  |
| 10 | `KooshaPari/KDesktopVirt` | 2/3 | yes | no | yes |  |
| 11 | `KooshaPari/phenoAI` | 2/3 | yes | no | yes |  |
| 12 | `KooshaPari/PhenoObservability` | 2/3 | yes | no | yes |  |
| 13 | `KooshaPari/PhenoPlugins` | 2/3 | yes | no | yes |  |
| 14 | `KooshaPari/phenotype-bus` | 2/3 | yes | no | yes |  |
| 15 | `KooshaPari/Sidekick` | 2/3 | yes | no | yes |  |
| 16 | `KooshaPari/Tasken` | 2/3 | no | yes | yes |  |
| 17 | `KooshaPari/BytePort` | 1/3 | yes | no | no |  |
| 18 | `KooshaPari/Civis` | 1/3 | no | no | yes |  |
| 19 | `KooshaPari/Configra` | 1/3 | no | no | yes |  |
| 20 | `KooshaPari/helios-router` | 1/3 | yes | no | no |  |
| 21 | `KooshaPari/heliosApp` | 1/3 | no | no | yes | requested as `helios-app`; resolved by `gh repo list` to `heliosApp` |
| 22 | `KooshaPari/HeliosLab` | 1/3 | no | no | yes |  |
| 23 | `KooshaPari/hwLedger` | 1/3 | yes | no | no |  |
| 24 | `KooshaPari/Metron` | 1/3 | yes | no | no |  |
| 25 | `KooshaPari/phenoData` | 1/3 | no | no | yes |  |
| 26 | `KooshaPari/PhenoKits` | 1/3 | no | no | yes |  |
| 27 | `KooshaPari/PhenoRuntime` | 1/3 | yes | no | no |  |
| 28 | `KooshaPari/phenoShared` | 1/3 | yes | no | no |  |
| 29 | `KooshaPari/phenoUtils` | 1/3 | yes | no | no |  |
| 30 | `KooshaPari/eyetracker` | 0/3 | no | no | no |  |
| 31 | `KooshaPari/helios-cli` | 0/3 | no | no | no |  |
| 32 | `KooshaPari/PhenoMCP` | 0/3 | no | no | no |  |

## Excluded Or Unavailable

| Requested repository | Resolved repository | Archived | Notes |
|---|---|---|---|
| `KooshaPari/KDV` | not found | unknown | repo metadata unavailable via gh api and targeted repo search |
| `KooshaPari/agentkit` | not found | unknown | repo metadata unavailable via gh api and targeted repo search |
| `KooshaPari/Pyron` | not found | unknown | repo metadata unavailable via gh api and targeted repo search |
| `KooshaPari/FocalPoint-vitepress` | not found | unknown | repo metadata unavailable via gh api and targeted repo search |

## Notes

- This audit checks repository-level presence signals only; it does not execute tests or inspect actual coverage percentages.
- FR traceability and security scanning are Level 3 governance requirements but were outside the three explicit GitHub content checks requested for this pass.
