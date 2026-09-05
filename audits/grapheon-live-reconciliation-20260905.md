# Grapheon -> Tracera live reconciliation

**Captured:** 2026-09-05T01:15Z
**Scope:** archived Grapheon source, Tracera current main, and registry boundary records.
**Disposition:** NO-GO for absorption/retirement completion.

## Verified source custody

- `KooshaPari/zz-archive-grapheon` is private and archived; `main` is
  `8b57aa380dd6d288f451be5ef0e4e766f606c7fb`.
- Local Grapheon `git fsck --full --no-reflogs` passes. The preservation bundle
  `/tmp/grapheon-preservation-all-20260904-0757.bundle` is 431,515,603 bytes with
  SHA-256 `828023ca7f034b796a9e4867ae008fa0c1f5443162c78e256746402a082185f0`.
- `git bundle verify` lists 47 refs. An isolated local restore has exact sorted
  ref/object parity and `git fsck --full --no-dangling` exits 0.
- This is first-cloud/local evidence only. The registry manifest records
  `r2_upload=NOT_EXECUTED_CREDENTIALS_AND_MULTIPART_CLIENT_ABSENT` and
  `second_cloud_restore=NOT_EXECUTED`.

## Destination state

- Tracera has no open pull requests. Current remote `main` is
  `b23469678da42d0d0ec8c303a7a97e5b1b19d293` and hosted Rust/build/coverage
  checks fail; dependency policy reports yanked `chacha20 0.10.1` and `spin 0.9.8`.
- Vercel and Cloudflare Worker deployments succeeded for that commit, but the
  full-stack/Render build failed. These successes do not prove backend
  readiness or end-to-end consumption.
- `pheno-harness` still documents Grapheon as source-of-truth, defaults to
  `127.0.0.1:8080`, and has an unfinished Tracera adapter. No authenticated
  append/query/health dogfood, telemetry delivery, or AgilePlus compliance run
  is evidenced.
- A focused local compatibility patch is present in the existing dirty
  `pheno-harness` owner checkout (`pheno/runtime_config.py`,
  `pheno/trace_store/config.py`, and `pheno/trace_store/tracera.py`): canonical
  `GRAPHEON_*` variables now take precedence while `TRACERA_*` aliases remain
  supported. The black-box tests `tests/test_runtime_config.py`,
  `tests/trace_store/test_config.py`, and `tests/trace_store/test_tracera.py`
  pass 45/45 via `python3 -m pytest -q -c /dev/null ...`. It is uncommitted
  and not production/dogfood proof.
- A protected Tracera successor branch based on current remote `main` has local
  commit `ec47038ad181d2772e83e14419a96955f642612c`: Rust doc syntax fixed and
  yanked `chacha20`/`spin` lock entries updated. `rustfmt`, `cargo deny`, and
  locked metadata pass; the crate test remains blocked by four unrelated
  current-main code/dependency errors. It is unpushed.

## Gate decision

The GitHub archive rename preceded the required dual-cloud restore gate. Do not
rename, delete, reset, clean, prune, or force-push any source-bearing state.
Completion requires: current-main Tracera fixes and accepted successor slices;
consumer repoint plus authenticated dogfood/observability/compliance proof;
zero-billable-runner evidence; and immutable second-cloud upload with an
independent restore, ref parity, and git-fsck report. Sponsor re-acknowledgement
must follow those proofs.
