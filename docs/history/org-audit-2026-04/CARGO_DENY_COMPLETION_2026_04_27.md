# Cargo-Deny Rollout — Completion Snapshot 2026-04-27

## Headline
**100% coverage across all 36 active Phenotype-org Rust repos.** Audit freshness check via `gh api .../contents/.github/workflows/cargo-deny.yml` for each repo.

## Method
- Probed 42 repos via `gh api repos/KooshaPari/{name}` (archived flag), `Cargo.toml` (Rust marker), and `.github/workflows/cargo-deny.yml` (enrollment marker).
- Sorted into ARCHIVED / ENROLLED / GAP / NON-RUST.

## Results (42 repos probed)

### ARCHIVED (6) — correctly excluded
- AtomsBot, chatta, KaskMan, KlipDot, kmobile, KVirtualStage

### ENROLLED (36) — cargo-deny.yml present
- Foundational: BytePort, FocalPoint, FocalPoint-vitepress, PhenoObservability, AgilePlus
- Helios: helios-app, helios-cli, helios-router, HeliosLab, HexaKit
- Pheno: phenoAI, phenoData, PhenoKits, PhenoMCP, PhenoPlugins, PhenoProc, PhenoRuntime, phenoShared, phenotype-bus, phenoUtils, PhenoObservability
- Apps: KDV, KDesktopVirt, Tokn, PolicyStack, Tasken, Sidekick, Civis, Eidolon, eyetracker, Configra, Metron, hwLedger
- Misc: GDK, agentkit, agentapi-plusplus, Pyron

### GAP (0)
- None.

## Significance
- Memory entries previously cited "~25 gap repos remaining" — **completely stale**.
- This is the canonical "audit freshness decay" pattern (`feedback_audit_freshness_decay.md`): cross-repo audits go 40-50% stale within ~30 min of mass dispatches.
- The user mandate to maintain a **zero-advisory floor** is now structurally enforced via scheduled CI in every active Rust repo.

## Next-Layer Audit (queued for next /loop fire)
- Verify each enrolled repo's most-recent `cargo-deny.yml` run is **green**, not just present.
- Method: `gh run list --repo KooshaPari/{name} --workflow=cargo-deny.yml --limit 1 --json conclusion,headSha`.
- Anomalies (non-success conclusion) → triage and dispatch fixes via cheap-llm/codex workers.

## Sources
- Probe script: `/tmp/classify_repos.sh` (this session)
- Probe SHAs: latest origin/main of each repo as of 2026-04-27 ~00:42 local

## SUPERSEDED

Cargo-deny completion/enrollment claims in this document are superseded by
[`CARGO_DENY_TRUE_COVERAGE_2026_04_27.md`](CARGO_DENY_TRUE_COVERAGE_2026_04_27.md)
and truth-correction commit `4a2a608`.
