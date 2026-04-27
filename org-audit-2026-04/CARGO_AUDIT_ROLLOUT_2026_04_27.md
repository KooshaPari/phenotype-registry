# cargo-audit Rollout — 2026-04-27

12 PRs merged adding RustSec advisory check workflow:
BytePort #76, helios-cli #542, phenoShared #138, HeliosLab #70, PhenoMCP #31, PhenoObservability #51, PhenoPlugins #39, AgilePlus #447, pheno #116, phenoAI #24, phenoData #26, hwLedger pending

## Workflow
`rustsec/audit-check@v2` triggers on push/PR with Cargo.lock changes + Wednesday cron + on-demand. Complements cargo-deny.
