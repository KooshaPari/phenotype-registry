# Cargo Deny Local Verify - Newly Enrolled Repos - 2026-04-27

Local-only verification with `cargo-deny 0.19.0`. No target returned exit 0.

| Repo | SHA | Result | Advisory IDs / cause |
| --- | --- | --- | --- |
| `pheno` | `b91b9a2d86f6` | FAIL, exit 1 | No advisory IDs. Dependency load failed: `phenotype-observability`; submodule `crates/cryptora` has no URL. |
| `phenoShared` | `e48a4629a8df` | FAIL, exit 1 | No advisory IDs. Manifest load failed for `crates/phenotype-error-core`. |
| `PhenoVCS` | `22b95237daf6` | FAIL, exit 4 | No advisory IDs. Pull failed first: local changes. License rejected unmatched allowances: `0BSD`, `BSD-2-Clause`, `BSD-3-Clause`, `CC0-1.0`, `ISC`, `MPL-2.0`, `Zlib`. |
| `phenotype-tooling` | `a5227336d326` | FAIL, exit 4 | No advisory IDs. Internal crates are unlicensed: `agent-orchestrator`, `audit-privacy`, `bench-guard`, `commit-msg-check`, `doc-link-check`, `fr-coverage`, `fuzz-setup`, `sbom-gen`. |
| `Tracely` | `590a78ecdd09` | FAIL, exit 4 | `RUSTSEC-2024-0437`. Pull failed first: local changes. License rejected unmatched allowances: same list as `PhenoVCS`. |

Pull tails: `pheno`, `phenoShared`, and `phenotype-tooling` were up to date. `PhenoVCS` and `Tracely` returned `error: Please commit or stash them.` `phenotype-tooling` initially conflicted during pull; that rebase was cleared before the final check.
