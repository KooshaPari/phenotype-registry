# Cargo Deny Workflow Dispatch Gap Audit - 2026-04-27

Audit scope: 36 enrolled repositories under `KooshaPari`.

Audit command requested:

```bash
gh api repos/KooshaPari/$r/contents/.github/workflows/cargo-deny.yml --jq .content 2>/dev/null | base64 -d | grep -c "workflow_dispatch:"
```

Local execution used GNU `gbase64 -d` for the same decode step because the shell environment emitted decode errors on empty/missing content. `has_dispatch` is the resulting grep count for `workflow_dispatch:`.

Coverage: 0/36 repos have the on-demand trigger (`0.0%`). Gap count: 36/36.

Recommendation: PR a single-line addition `workflow_dispatch:` under `on:` block to enable on-demand verification.

| Repo | has_dispatch | cargo-deny.yml status |
| --- | ---: | --- |
| BytePort | 0 | present |
| FocalPoint | 0 | present |
| FocalPoint-vitepress | 0 | missing or API unreadable |
| PhenoObservability | 0 | present |
| AgilePlus | 0 | missing or API unreadable |
| helios-app | 0 | missing or API unreadable |
| helios-cli | 0 | present |
| helios-router | 0 | missing or API unreadable |
| HeliosLab | 0 | missing or API unreadable |
| HexaKit | 0 | missing or API unreadable |
| phenoAI | 0 | missing or API unreadable |
| phenoData | 0 | missing or API unreadable |
| PhenoKits | 0 | missing or API unreadable |
| PhenoMCP | 0 | present |
| PhenoPlugins | 0 | present |
| PhenoProc | 0 | missing or API unreadable |
| PhenoRuntime | 0 | missing or API unreadable |
| phenoShared | 0 | missing or API unreadable |
| phenotype-bus | 0 | present |
| phenoUtils | 0 | present |
| KDV | 0 | missing or API unreadable |
| KDesktopVirt | 0 | missing or API unreadable |
| Tokn | 0 | missing or API unreadable |
| PolicyStack | 0 | missing or API unreadable |
| Tasken | 0 | present |
| Sidekick | 0 | present |
| Civis | 0 | present |
| Eidolon | 0 | present |
| eyetracker | 0 | present |
| Configra | 0 | present |
| Metron | 0 | present |
| hwLedger | 0 | present |
| GDK | 0 | missing or API unreadable |
| agentkit | 0 | missing or API unreadable |
| agentapi-plusplus | 0 | missing or API unreadable |
| Pyron | 0 | missing or API unreadable |
