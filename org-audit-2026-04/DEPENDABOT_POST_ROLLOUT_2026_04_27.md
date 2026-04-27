# Dependabot Alerts Inventory - Post Cargo-Deny Rollout - 2026-04-27

Post-rollout open Dependabot alerts for non-archived `KooshaPari` repositories that
currently have `.github/workflows/cargo-deny.yml`.

Headline compared to `b6ade78`:

- Comparable cargo-deny overlap from the `b6ade78` inventory moved from 49 open alerts to
  34 open alerts, a reduction of 15.
- Current post-rollout scoped total is 51 open alerts across 38 cargo-deny-enrolled repos.
- The full `b6ade78` inventory total was 58 open alerts across its then-listed repos; the
  post-rollout total includes newly enrolled repos that were not listed in that snapshot.

Collection notes:

- Repo discovery used `gh repo list KooshaPari --limit 1000 --json name,isArchived`.
- Workflow enrollment used
  `gh api repos/KooshaPari/<repo>/contents/.github/workflows --jq 'any(.name=="cargo-deny.yml")'`.
- Open alert counts used
  `gh api repos/KooshaPari/<repo>/dependabot/alerts --jq '[.[] | select(.state=="open")] | length'`.
- Severity summaries are from open alerts only.

| Repo | Open alerts | Prior open in `b6ade78` | Delta | Open severities |
|---|---:|---:|---:|---|
| heliosCLI | 9 | n/a | n/a | high: 1, low: 5, medium: 3 |
| pheno | 8 | n/a | n/a | high: 4, low: 2, medium: 2 |
| BytePort | 7 | 7 | 0 | low: 2, medium: 5 |
| hwLedger | 7 | 7 | 0 | high: 3, low: 2, medium: 2 |
| PhenoRuntime | 6 | 6 | 0 | high: 1, low: 4, medium: 1 |
| AgilePlus | 3 | 2 | +1 | high: 1, medium: 2 |
| HeliosLab | 3 | 3 | 0 | low: 1, medium: 2 |
| HexaKit | 3 | 19 | -16 | high: 1, medium: 2 |
| KDesktopVirt | 3 | 3 | 0 | high: 1, low: 2 |
| helios-router | 2 | 2 | 0 | medium: 2 |
| Civis | 0 | 0 | 0 | none |
| Configra | 0 | 0 | 0 | none |
| Eidolon | 0 | 0 | 0 | none |
| eyetracker | 0 | 0 | 0 | none |
| FocalPoint | 0 | 0 | 0 | none |
| GDK | 0 | 0 | 0 | none |
| helios-cli | 0 | 0 | 0 | none |
| Metron | 0 | 0 | 0 | none |
| phenoAI | 0 | 0 | 0 | none |
| phenoData | 0 | 0 | 0 | none |
| PhenoKits | 0 | 0 | 0 | none |
| PhenoMCP | 0 | 0 | 0 | none |
| PhenoObservability | 0 | 0 | 0 | none |
| PhenoPlugins | 0 | 0 | 0 | none |
| PhenoProc | 0 | 0 | 0 | none |
| phenoShared | 0 | 0 | 0 | none |
| phenotype-bus | 0 | 0 | 0 | none |
| phenotype-journeys | 0 | n/a | n/a | none |
| phenotype-tooling | 0 | n/a | n/a | none |
| phenoUtils | 0 | 0 | 0 | none |
| PhenoVCS | 0 | n/a | n/a | none |
| PlayCua | 0 | n/a | n/a | none |
| rich-cli-kit | 0 | n/a | n/a | none |
| Sidekick | 0 | 0 | 0 | none |
| Tasken | 0 | 0 | 0 | none |
| thegent-dispatch | 0 | n/a | n/a | none |
| thegent-workspace | 0 | n/a | n/a | none |
| Tokn | 0 | 0 | 0 | none |
| Tracely | 0 | n/a | n/a | none |
