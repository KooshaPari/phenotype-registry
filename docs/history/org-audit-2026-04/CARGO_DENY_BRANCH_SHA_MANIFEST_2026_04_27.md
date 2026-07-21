# Cargo Deny Branch SHA Manifest - 2026-04-27

Source branch list: `scripts/create_cargo_deny_prs_2026_04_27.sh` at commit `1b9856b`.

Verification command pattern:

```bash
git ls-remote --heads https://github.com/KooshaPari/$repo $branch
git fetch https://github.com/KooshaPari/$repo $sha
git log -1 --format=%s $sha
```

| Repo | Branch | SHA | Commit subject |
|---|---|---|---|
| AgilePlus | `ci/cargo-deny-full-rollout-2026-04-27` | `c637549ba77fb987db40b00150be56fc95009a3f` | ci(cargo-deny): add starter deny.toml + scheduled scan workflow (zero-advisory floor) |
| GDK | `ci/cargo-deny-rollout-2026-04-27` | `586c3c42af04cd697f85b397012625f232493279` | ci(cargo-deny): add scheduled scan + workflow_dispatch trigger (zero-advisory floor) |
| HeliosLab | `ci/cargo-deny-rollout-2026-04-27` | `aa2290464131bc801bab9003bc72375431c40f73` | ci(cargo-deny): add scheduled scan + workflow_dispatch trigger (zero-advisory floor) |
| HexaKit | `ci/cargo-deny-rollout-20260427` | `447d8eede630f995e26d48bb6ee54ce6fef8d81d` | ci(cargo-deny): add scheduled scan + workflow_dispatch (zero-advisory floor) |
| KDesktopVirt | `ci/cargo-deny-full-rollout-2026-04-27` | `40d6a1f62b420de0c61ed1be6ebe9fd44ec0564b` | ci(cargo-deny): add starter deny.toml + scheduled scan workflow (zero-advisory floor) |
| pheno | `ci/cargo-deny-rollout-2026-04-27` | `83d48a2c6e7f9bddd34e6a7ba1f1a899887c3cdf` | ci(cargo-deny): add scheduled scan + workflow_dispatch trigger (zero-advisory floor) |
| phenoAI | `ci/cargo-deny-full-rollout-2026-04-27` | `3ac84855e8be3720f73506d26bd126d41669d33a` | ci(cargo-deny): add starter deny.toml + scheduled scan workflow (zero-advisory floor) |
| phenoData | `ci/cargo-deny-full-rollout-2026-04-27` | `25024f0d632e445488bad785e3a4579d49fb1721` | ci(cargo-deny): add starter deny.toml + scheduled scan workflow (zero-advisory floor) |
| PhenoKits | `ci/cargo-deny-full-rollout-2026-04-27` | `9c0db31102f311b4431a298c92e6b30a5476aca5` | ci(cargo-deny): add starter deny.toml + scheduled scan workflow (zero-advisory floor) |
| PhenoProc | `ci/cargo-deny-full-rollout-2026-04-27` | `8ae1fa84041fab5f4789387b68e8a73c7c6c9494` | ci(cargo-deny): add starter deny.toml + scheduled scan workflow (zero-advisory floor) |
| PhenoRuntime | `ci/cargo-deny-full-rollout-2026-04-27` | `80daae924a0d144e8b650800a1b6a0a1ea76341c` | ci(cargo-deny): add starter deny.toml + scheduled scan workflow (zero-advisory floor) |
| phenoShared | `ci/cargo-deny-rollout-2026-04-27` | `74e634a4b626c2611ffa0bbdd5b968b574ba8706` | ci(cargo-deny): add scheduled scan + workflow_dispatch trigger (zero-advisory floor) |
| phenotype-journeys | `ci/cargo-deny-full-rollout-2026-04-27` | `e26300703f2d468cbb630597bdde7683b9832d51` | ci(cargo-deny): add starter deny.toml + scheduled scan workflow (zero-advisory floor) |
| phenotype-tooling | `ci/cargo-deny-full-rollout-2026-04-27` | `47c9eecc2961b5fe8be290a23db759e10394cb2e` | ci(cargo-deny): add starter deny.toml + scheduled scan workflow (zero-advisory floor) |
| PhenoVCS | `ci/cargo-deny-full-rollout-2026-04-27` | `b8fc68f6d454c2d3ad4c36ce37b443b48afb404e` | ci(cargo-deny): add starter deny.toml + scheduled scan workflow (zero-advisory floor) |
| PlayCua | `ci/cargo-deny-full-rollout-2026-04-27` | `d2370482d60226fb59899edc437bb6df55610c86` | ci(cargo-deny): add starter deny.toml + scheduled scan workflow (zero-advisory floor) |
| rich-cli-kit | `ci/cargo-deny-full-rollout-2026-04-27` | `71c7a92df7140e9dd22419d941e497f39e5dc592` | ci(cargo-deny): add starter deny.toml + scheduled scan workflow (zero-advisory floor) |
| thegent-dispatch | `ci/cargo-deny-full-rollout-2026-04-27` | `6eea26a3e856ed9a610c1c8d1fa510caefc341aa` | ci(cargo-deny): add starter deny.toml + scheduled scan workflow (zero-advisory floor) |
| thegent-workspace | `ci/cargo-deny-full-rollout-2026-04-27` | `0fcfaf7b97ce69bbe98843d54e09d8f1bf1faaa6` | ci(cargo-deny): add starter deny.toml + scheduled scan workflow (zero-advisory floor) |
| Tokn | `ci/cargo-deny-full-rollout-2026-04-27` | `2623bd7ba8d550912f492256c604869bb523a1ca` | ci(cargo-deny): add dedicated workflow with workflow_dispatch (alongside existing quality-gate cargo-deny step) |
| Tracely | `ci/cargo-deny-full-rollout-2026-04-27` | `8274d74f1dfd05f1cb7f50b7166b6f033e780829` | ci(cargo-deny): add starter deny.toml + scheduled scan workflow (zero-advisory floor) |
| Civis | `ci/cargo-deny-add-workflow-dispatch-2026-04-27` | `f837fe5a1936aff658d3bcd0b190c887d8374ffd` | ci(cargo-deny): add workflow_dispatch trigger for on-demand verification |
| Configra | `ci/cargo-deny-add-workflow-dispatch-2026-04-27` | `56bca4d222d6a6fcdb5a1489a56f0570a0288524` | ci(cargo-deny): add workflow_dispatch trigger for on-demand verification |
| Eidolon | `ci/cargo-deny-add-workflow-dispatch-2026-04-27` | `103d6591554ecbab2910741ee6e06d0143e8abd8` | ci(cargo-deny): add workflow_dispatch trigger for on-demand verification |
| eyetracker | `ci/cargo-deny-add-workflow-dispatch-2026-04-27` | `6a868295e2e8f856a7b03931f664b18c7839a7af` | ci(cargo-deny): add workflow_dispatch trigger for on-demand verification |
| heliosCLI | `ci/cargo-deny-add-workflow-dispatch-2026-04-27` | `7385f3ff79a9e827d94f3786b7e01881146d75be` | ci(cargo-deny): add workflow_dispatch trigger for on-demand verification |
| Metron | `ci/cargo-deny-add-workflow-dispatch-2026-04-27` | `d93f84536ad1202601ea58d62b4e86bda0aae8fb` | ci(cargo-deny): add workflow_dispatch trigger for on-demand verification |

Result: all 27 expected rollout branch heads resolved to concrete SHAs, fetched successfully, and produced commit subjects.
