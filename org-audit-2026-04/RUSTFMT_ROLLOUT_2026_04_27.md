# rustfmt.toml Rollout — 2026-04-27

## Status
**24 PRs merged** adding Phenotype-org standard rustfmt.toml across 24 Rust repos.

## Batch 1 (12)
pheno #115, phenoAI #19, phenoData #21, PhenoKits #66, PhenoVCS #34, Tracely #14, PlayCua #47, Civis #266, Eidolon #17, eyetracker #22, GDK #35, HexaKit #119

## Batch 2 (12)
Metron #24, rich-cli-kit #13, thegent-dispatch #13, thegent-workspace #15, phenotype-bus #11, phenotype-journeys #19, phenotype-tooling #29, phenoUtils #15, PhenoRuntime #31, helios-router #193, KDesktopVirt #20, Sidekick #16

## Standard
```toml
edition = "2021"
max_width = 100
hard_tabs = false
tab_spaces = 4
newline_style = "Unix"
imports_granularity = "Module"
group_imports = "StdExternalCrate"
reorder_imports = true
reorder_modules = true
```

Plus 1 CONTRIBUTING.md (hwLedger #54).
