# Cargo Deny Live Verification - 2026-04-27

Source audit: `CARGO_DENY_DISPATCH_GAP_2026_04_27.md`.

The dispatch gap audit reported `Coverage: 0/36 repos have the on-demand trigger (0.0%)`.
Because the HAS_DISPATCH set was empty, no `cargo-deny.yml` workflow_dispatch runs were
triggered. This preserves the requested billing cap and avoids triggering repositories without
the required manual dispatch entrypoint.

| Repo | RunID | Conclusion | Duration |
| --- | --- | --- | --- |
| None | N/A | No HAS_DISPATCH repos in source audit; zero workflows triggered | 0s |
