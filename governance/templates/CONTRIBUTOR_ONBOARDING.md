# Contributor Onboarding One-Pager (Kimi-generated 2026-04-27)

Target: phenotype.space/contributing

>>> dispatch-worker tier=nvidia/moonshotai/kimi-k2.5 model=nvidia/moonshotai/kimi-k2.5 endpoint=http://localhost:20128/v1
>>> routed to backend: moonshotai/kimi-k2.5
 **Phenotype Developer Onboarding**

**Where to start:** Clone `phenotype-org/phenotype-core` first; it contains protocol primitives and shared schemas. Filter issues by `good-first-issue` here before touching `phenotype-cli` or `phenotype-node`.

**Architecture (5 lines):**
- `phenotype-core`: Shared data structures, validation logic, and serialization primitives.
- `phenotype-cli`: Reference implementation and developer tooling.
- `phenotype-node`: Distributed execution engine (async; runs on Tokio).
- `phenotype-wasm`: Browser-compatible WASM bindings for web clients.
- `phenotype-protocol`: Cross-language schema specs (Avro/Protobuf).

**Prerequisites:**
```bash
rustup update
cargo install just cargo-deny cargo-nextest
just setup  # installs git hooks & toolchain
```

**Running cargo-deny:**
```bash
just deny
# Or manually: cargo deny check advisories bans licenses
```
Run before pushing; CI blocks on yanked crates, license conflicts, or duplicate versions.

**PR Workflow:**
1. Fork and branch from `main` (prefix: `feat/`, `fix/`, `docs/`).
2. Ensure `just check` passes (fmt, clippy, test, deny).
3. Open PR; template auto-populates. Keep commits atomic; we squash-merge.
4. Require 1 approving review; ensure CI passes (Linux, macOS, Windows).

Questions? Open a Discussion in `phenotype-meta`.
