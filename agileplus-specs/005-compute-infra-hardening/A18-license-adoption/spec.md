# Spec: A18 — Adopt Apache-2.0 LICENSE + dual-license NOTICE

## Metadata
- **Unit ID:** A18
- **Epic:** A — Hygiene garden & branch slim
- **Type:** config
- **Repo:** all (phenotype-infra, PhenoCompose, BytePort, phenotype-registry, agileplus)
- **Priority:** S (must-pass gate for Tier-1)
- **Dependencies:** none

## Objective
Adopt the Apache-2.0 LICENSE + dual-license pattern with a NOTICE file across all 5 phenotype-org repos. Apache-2.0 is the preferred license for the Phenotype ecosystem; all repos must have:
1. A `LICENSE` file containing the Apache-2.0 full text
2. A `LICENSE-MIT` file for MIT option (dual-license)
3. A `NOTICE` file with copyright attribution per Apache-2.0 Section 4(d)
4. Cargo.toml / package.json license field set to `"MIT OR Apache-2.0"`
5. README license badge and section updated

## Acceptance Criteria
- [ ] `LICENSE` contains Apache-2.0 full text in every repo
- [ ] `LICENSE-MIT` contains MIT license text in every repo
- [ ] `NOTICE` file exists in every repo with copyright statement
- [ ] Cargo.toml / package.json declares `MIT OR Apache-2.0`
- [ ] README has license badge and section acknowledging dual-license
- [ ] All Tier-0 gates pass on each repo

## Current State (per audit)
| Repo | Apache-2.0 LICENSE | NOTICE | Cargo.toml license | Status |
|---|---|---|---|---|
| phenotype-infra | Full text | **MISSING** | `MIT OR Apache-2.0` | Needs NOTICE + README fix |
| PhenoCompose | Full text | **MISSING** | `MIT OR Apache-2.0` | Needs NOTICE |
| BytePort | **MISSING** | **MISSING** | Not set (root) | Needs Apache LICENSE + NOTICE |
| phenotype-registry | **Placeholder** | **MISSING** | Not set | Needs full text + NOTICE |
| agileplus | **MISSING** | **MISSING** | `MIT` | Needs Apache LICENSE + NOTICE |

## Work Packages
- WP01: phenotype-infra — add NOTICE file, update README
- WP02: PhenoCompose — add NOTICE file
- WP03: BytePort — add Apache-2.0 LICENSE, NOTICE, update Cargo.toml
- WP04: phenotype-registry — replace placeholder Apache-2.0, add NOTICE
- WP05: agileplus — add Apache-2.0 LICENSE, NOTICE, update Cargo.toml
