# cargo-audit rollout — 2026-04-27

## Tooling
- `gh` `2.91.0 (2026-04-22)`
- `git` `2.50.1 (Apple Git-155)`
- UTC date: `2026-04-27T14:13:48Z`

## Targets (12 repos)
- `BytePort`
- `helios-cli`
- `phenoShared`
- `HeliosLab`
- `PhenoMCP`
- `PhenoObservability`
- `PhenoPlugins`
- `AgilePlus`
- `pheno`
- `phenoAI`
- `phenoData`
- `hwLedger`

## Raw execution
- `BytePort` -> clone -> commit `cfd28788a436683f4fcc3c66c709ffaef6e29d26` -> push -> PR `#76`
- `helios-cli` -> clone -> commit `6d7b6cc880f1f4c30d66d4eae51fe1a36d2c06b2` -> push -> PR `#542`
- `phenoShared` -> clone -> commit `a47383142804e2244167a7a3bfb0f5341c4af129` -> push -> PR `#138`
- `HeliosLab` -> clone -> commit `95d88e48e1caf72d484a72bb74ec6d090c19d42f` -> push -> PR `#70`
- `PhenoMCP` -> clone -> commit `b7ff1ae23308d2cd72d647af5cc3bf82fa70cace` -> push -> PR `#31`
- `PhenoObservability` -> clone -> commit `91cf73b6c6cebde566c922174a914227230e7e57` -> push -> PR `#51`
- `PhenoPlugins` -> clone -> commit `dcf1f85af4099200f07a5a0adfb4e92a78e2a556` -> push -> PR `#39`
- `AgilePlus` -> clone -> commit `4f518ea0451d79bbfb85c828bb0dc386a11751c2` -> push -> PR `#447`
- `pheno` -> clone -> commit `fef74188dc30c6ca41e6a976aaedd1498e83ad88` -> push -> PR `#116`
- `phenoAI` -> clone -> commit `5db6e5e113b6fa17affcec8b14523c5bb6e23c3c` -> push -> PR `#24`
- `phenoData` -> clone -> commit `4e08a4942b2f91ae338288fc904d9ffcb8ef4abf` -> push -> PR `#26`
- `hwLedger` -> clone -> no `cargo-audit.yml` on `main` at verification time; contents API returned `404`

## Outcomes
- `BytePort` PR `#76` merged
- `helios-cli` PR `#542` merged
- `phenoShared` PR `#138` merged
- `HeliosLab` PR `#70` merged
- `PhenoMCP` PR `#31` merged
- `PhenoObservability` PR `#51` merged
- `PhenoPlugins` PR `#39` merged
- `AgilePlus` PR `#447` merged
- `pheno` PR `#116` merged
- `phenoAI` PR `#24` merged
- `phenoData` PR `#26` merged
- `hwLedger` remained pending; no merged cargo-audit PR was verifiable from the repository contents API

## Annotations
- The existing rollout note in `org-audit-2026-04/CARGO_AUDIT_ROLLOUT_2026_04_27.md` said "12 PRs merged", but direct GitHub API verification only surfaced 11 merged cargo-audit workflow PRs.
- `hwLedger` is the only target in this batch whose `contents` lookup still returns `404` for `.github/workflows/cargo-audit.yml`.
- The hyphenated repo is `helios-cli`; `heliosCLI` is a different repo and was not part of this cargo-audit wave.
- The workflow added in the merged repos is `cargo-audit.yml`, not a cargo-deny file.

## Verification
- `gh api repos/KooshaPari/BytePort/contents/.github/workflows/cargo-audit.yml --jq .name` -> `cargo-audit.yml`
- `gh api repos/KooshaPari/helios-cli/contents/.github/workflows/cargo-audit.yml --jq .name` -> `cargo-audit.yml`
- `gh api repos/KooshaPari/phenoShared/contents/.github/workflows/cargo-audit.yml --jq .name` -> `cargo-audit.yml`
- `gh api repos/KooshaPari/HeliosLab/contents/.github/workflows/cargo-audit.yml --jq .name` -> `cargo-audit.yml`
- `gh api repos/KooshaPari/PhenoMCP/contents/.github/workflows/cargo-audit.yml --jq .name` -> `cargo-audit.yml`
- `gh api repos/KooshaPari/PhenoObservability/contents/.github/workflows/cargo-audit.yml --jq .name` -> `cargo-audit.yml`
- `gh api repos/KooshaPari/PhenoPlugins/contents/.github/workflows/cargo-audit.yml --jq .name` -> `cargo-audit.yml`
- `gh api repos/KooshaPari/AgilePlus/contents/.github/workflows/cargo-audit.yml --jq .name` -> `cargo-audit.yml`
- `gh api repos/KooshaPari/pheno/contents/.github/workflows/cargo-audit.yml --jq .name` -> `cargo-audit.yml`
- `gh api repos/KooshaPari/phenoAI/contents/.github/workflows/cargo-audit.yml --jq .name` -> `cargo-audit.yml`
- `gh api repos/KooshaPari/phenoData/contents/.github/workflows/cargo-audit.yml --jq .name` -> `cargo-audit.yml`
- `gh api repos/KooshaPari/hwLedger/contents/.github/workflows/cargo-audit.yml --jq .name` -> `404 Not Found`
