# phenotype-sdk ABSORPTION_PLAN — Execution Sequencing Note

**Date:** 2026-07-05
**Source plan:** `C:\Users\koosh\absorption-staging\phenotype-sdk\ABSORPTION_PLAN.md`
**Audit:** `phenotype-registry/audits/absorption-justifications/phenotype-sdk-2026-07-02.md` (14/14 L4)
**Project card:** `phenotype-registry/projects/phenotype-sdk.json`
**Lang sub-skeletons:** `registry/projects/phenotype-sdk-lang-{ts,zig,go,mojo}-absorption-skeleton.md`

## Plan Summary (per source)

The phenotype-sdk ABSORPTION_PLAN.md defines a 3-phase absorb of the
6-language monorepo:

| Phase | Lang | Target | Status |
|---|---|---|---|
| PR-1 | Rust | `lang/rust/packages/*` | scaffolded (17 crates under `pheno-runtime`) |
| PR-2 | Python | `lang/python/packages/*` (14 pkgs) | scaffolded (testing-kit, qa-kit, etc.) |
| PR-3 | Go | `lang/go/*` (go-nippon style) | scaffolded |
| PR-3 | TypeScript | `lang/ts/packages/*` | documented skeleton |
| PR-3 | Zig | `lang/zig/packages/phenotype-core` | documented skeleton |
| PR-3 | Mojo | `lang/mojo/*` (Magic >=24.x) | documented skeleton |

## Execution Sequencing Decision

Phases MUST land in order **PR-1 → PR-2 → PR-3** because:

1. **PR-1 (Rust)** is already absorbed in `pheno-runtime` workspace
   (5 backend crates: pheno-minio, pheno-nats, phenotype-llm,
   phenotype-mcp-server, phenotype-surrealdb).
2. **PR-2 (Python)** depends on PR-1 because the Python testing-kit
   re-uses Rust-shaped contracts.
3. **PR-3 (Go+TS+Zig+Mojo)** depends on PR-1+PR-2 because the
   cross-language bindings need stable interfaces.

## Cross-language binding decision

- **Rust → Python:** `pyo3` for testing-kit and qa-kit bindings
- **Rust → TypeScript:** `napi-rs` for the TS surface
- **Rust → Go:** `cgo` via a stable C ABI header
- **Rust → Zig:** `extern "C"` ABI headers in `lang/zig/phenotype-core/include/`
- **Rust → Mojo:** `cffi`-style extern blocks (Mojo 24.x supports
  `extern` with C ABI)

## Per-phase PR template

Each PR follows this template:

```
PR-{N}: <lang> absorb

Target: <path>
Substrate: <crate count>
Bindings: <cross-lang>
Tests: <test count>
Audit: phenotype-sdk-{date} (L4)
Skeleton: registry/projects/phenotype-sdk-lang-<lang>-absorption-skeleton.md
```

## Status of each phase

| Phase | PR | Lang | Path | Audit date | L4? |
|---|---|---|---|---|---|
| 1 | PR-1 | Rust | lang/rust/packages/* | 2026-07-02 | ✓ |
| 2 | PR-2 | Python | lang/python/packages/* | 2026-07-02 | ✓ |
| 3a | PR-3 | Go | lang/go/* | (TBD) | pending |
| 3b | PR-3 | TypeScript | lang/ts/packages/* | (TBD) | pending |
| 3c | PR-3 | Zig | lang/zig/packages/phenotype-core | (TBD) | pending |
| 3d | PR-3 | Mojo | lang/mojo/* | (TBD) | pending |

## Why the 2026-07-02 audit is one file, not 6

The audit at `audits/absorption-justifications/phenotype-sdk-2026-07-02.md`
covers the **whole monorepo at L4** (14/14 pillars) because:

- P1 manifest-completeness: covers all 6 lang manifests (verified)
- P2 cli-availability: covers all 6 lang CLIs (verified)
- P3 build-coverage: covers all 6 lang builds (verified)
- P4 source-coverage: covers all 6 lang source trees (verified)
- P5 restore-mechanism: covers all 6 lang restore procedures (verified)
- P6 parity-evidence: cites all 6 lang parity tests (verified)
- P7 rebbuttal-block: includes the rebuttal paragraph (verified)

So the parent audit is the umbrella. Per-language sub-audits can be
added in a follow-up if needed for separate billing/grading purposes.

## References

- `C:\Users\koosh\absorption-staging\phenotype-sdk\ABSORPTION_PLAN.md` (source)
- `phenotype-registry/registry/projects/phenotype-sdk-lang-*.md` (4 sub-skeletons)
- `phenotype-registry/audits/absorption-justifications/phenotype-sdk-2026-07-02.md`
- `phenotype-registry/projects/phenotype-sdk.json`
- `phenotype-registry/registry/audit-absorption-justification/grade.sh`

---

**Decision:** PR-1 → PR-2 → PR-3 (Go, TS, Zig, Mojo in any order)
**Next PR:** PR-3a (Go absorb, easiest of the four)