# Cargo Deny Live Verification - 2026-04-27

Source audit: `CARGO_DENY_DISPATCH_GAP_2026_04_27.md`.

The dispatch gap audit reported `Coverage: 0/36 repos have the on-demand trigger (0.0%)`.
Because the HAS_DISPATCH set was empty, no `cargo-deny.yml` workflow_dispatch runs were
triggered. This preserves the requested billing cap and avoids triggering repositories without
the required manual dispatch entrypoint.

| Repo | RunID | Conclusion | Duration |
| --- | --- | --- | --- |
| None | N/A | No HAS_DISPATCH repos in source audit; zero workflows triggered | 0s |

## Requested Verification Run - 2026-04-27 01:21 MST

Input file: `CARGO_DENY_DISPATCH_GAP_2026_04_27.md`.

Eligibility rule requested: trigger the first five repositories with `HAS=1` / `workflow_dispatch:`.

Live source audit result: no eligible repositories. The audit table reports `has_dispatch = 0`
for all 36 enrolled repositories, so zero `gh workflow run cargo-deny.yml` commands were issued.
This keeps the requested cap of 5 and avoids attempting manual dispatch on workflows that do not
expose `workflow_dispatch`.

| Repo | Triggered | RunID | Status | Conclusion |
| --- | --- | --- | --- | --- |
| None | no | N/A | not_started | No HAS=1 entries in source audit |
