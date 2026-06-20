# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

## [0.1.1] - 2026-06-20

### Added
- **catalog/registry.yaml** — first canonical machine-readable substrate
  catalog (ADR-ECO-017). Three entries: Configra, pheno-tracing,
  pheno-mcp-router.
- **catalog/registry.schema.json** — JSON Schema for catalog entries;
  encodes the tier-required and architecture-required rules.
- **scripts/validate-catalog.py** — offline validator. Checks tier
  required, architecture required when tier=phenotype-framework,
  ports/adapters required when architecture=hexagonal-l4, naming
  conventions (`*Port` / `*Adapter` CamelCase), and boundary/intent
  path resolution.
- **.github/workflows/registry-validate.yml** — CI workflow that runs
  `scripts/validate-catalog.py` + `scripts/conventions-lint.sh` on PRs
  touching `catalog/`, `scripts/`, `docs/boundary/`, `docs/intent/`,
  or `docs/adrs/`.
- **docs/adrs/ADR-ECO-017-substrate-schema-conventions.md** — new ADR
  porting monorepo ADR-013 (substrate model) and ADR-014 (hexagonal
  port/adapter naming) into the registry catalog schema as enforced
  requirements.
- **docs/boundary/Configra.md** — first-class boundary entry for
  Configra (was missing; `role: unknown` previously).
- **docs/intent/Configra.md** — first-class intent entry for Configra.
- **okf/manifest.okf.yaml** — added `substrate-catalog` and
  `substrate-schema` artifacts so the OKF manifest indexes the catalog.

### Changed
- **docs/adrs/README.md** — registered ADR-017 in the ecosystem ADR table.

### Notes
- T23 registry refresh dispatch (2026-06-20).
- Closes the L5-110 / L5-114 / L5-500 substrate catalog gap.
- Cross-references: monorepo ADR-013, ADR-014, ADR-023, ADR-040,
  ADR-048.

## [0.1.0] - 2026-06-08
- Initial release
