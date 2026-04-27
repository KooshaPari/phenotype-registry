# README Badge Coverage Audit - 2026-04-27

Scope: non-archived KooshaPari Phenotype repos listed in the audit request.

Method:

```bash
gh api repos/KooshaPari/$r/readme --jq .content 2>/dev/null | base64 -d 2>/dev/null
```

Badge regexes:

- Cargo deny: `cargo-deny.*svg`
- License: `license.*svg|License-`
- CI: `actions/workflow.*svg|Build|CI`

## Summary

| Badge type | Present | Total | Coverage |
| --- | ---: | ---: | ---: |
| cargo-deny | 0 | 36 | 0.0% |
| license | 15 | 36 | 41.7% |
| CI | 25 | 36 | 69.4% |

## Repo Coverage

Sorted by missing badge count descending, then repo name ascending.

| Repo | cargo-deny | license | CI | Missing badges | README status |
| --- | --- | --- | --- | ---: | --- |
| agentkit | no | no | no | 3 | missing_or_empty |
| eyetracker | no | no | no | 3 | present |
| FocalPoint-vitepress | no | no | no | 3 | missing_or_empty |
| helios-app | no | no | no | 3 | missing_or_empty |
| helios-router | no | no | no | 3 | present |
| HeliosLab | no | no | no | 3 | present |
| hwLedger | no | no | no | 3 | present |
| KDV | no | no | no | 3 | missing_or_empty |
| phenoShared | no | no | no | 3 | present |
| Pyron | no | no | no | 3 | missing_or_empty |
| agentapi-plusplus | no | no | yes | 2 | present |
| AgilePlus | no | no | yes | 2 | present |
| BytePort | no | no | yes | 2 | present |
| Civis | no | no | yes | 2 | present |
| FocalPoint | no | no | yes | 2 | present |
| GDK | no | no | yes | 2 | present |
| helios-cli | no | no | yes | 2 | present |
| HexaKit | no | no | yes | 2 | present |
| PhenoKits | no | no | yes | 2 | present |
| PolicyStack | no | no | yes | 2 | present |
| Sidekick | no | yes | no | 2 | present |
| Tokn | no | no | yes | 2 | present |
| Configra | no | yes | yes | 1 | present |
| Eidolon | no | yes | yes | 1 | present |
| KDesktopVirt | no | yes | yes | 1 | present |
| Metron | no | yes | yes | 1 | present |
| phenoAI | no | yes | yes | 1 | present |
| phenoData | no | yes | yes | 1 | present |
| PhenoMCP | no | yes | yes | 1 | present |
| PhenoObservability | no | yes | yes | 1 | present |
| PhenoPlugins | no | yes | yes | 1 | present |
| PhenoProc | no | yes | yes | 1 | present |
| PhenoRuntime | no | yes | yes | 1 | present |
| phenotype-bus | no | yes | yes | 1 | present |
| phenoUtils | no | yes | yes | 1 | present |
| Tasken | no | yes | yes | 1 | present |
