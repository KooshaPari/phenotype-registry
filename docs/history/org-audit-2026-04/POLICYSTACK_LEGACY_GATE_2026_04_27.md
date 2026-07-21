# PolicyStack Legacy Tooling Gate Triage - 2026-04-27

Scope: local audit only in `/Users/kooshapari/CodeProjects/Phenotype/repos/PolicyStack`.

Workflow checked: `.github/workflows/legacy-tooling-gate.yml`. The gate checks out shared
scanner assets from `kooshapari/phenotype` at `tooling/legacy-enforcement`, installs
`pyyaml`, and runs `scanner/legacy_tooling_scanner.py` against the repo in WARN/report-only
mode using `policy/rules.yaml`.

Local config state:
- No repo-local `tooling/legacy-tooling-governance/` directory found in PolicyStack.
- No repo-local `rules.yaml`, `maturity.json`, or `exceptions.yaml` found in PolicyStack.
- Shared local policy copy read from `phenoShared-wtrees/reqwest-feature-fix/tooling/legacy-enforcement/policy/rules.yaml`.
- Shared `exceptions.yaml` has no active exceptions.

Command run:
`python3 .../legacy_tooling_scanner.py --repo-root . --policy .../rules.yaml --exceptions .../exceptions.yaml --report-only`

Findings: 24 total, all medium severity. Critical: 0, high: 0, medium: 24, low: 0.

Top category: `LT-GEN-005` large file/module size, 24 findings. Largest examples:
`tests/test_policy_contract.py` 2947 lines, `scripts/sync_host_rules.py` 933 lines,
`cli/src/policy_federation/cli.py` 901 lines, `tests/test_sync_host_rules_governance.py`
874 lines, `cli/src/policy_federation/delegate.py` 662 lines.
