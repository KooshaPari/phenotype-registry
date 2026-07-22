# 2phenoEvents — Absorption Justification

**Status:** NEW (no prior audit exists for `2phenoEvents` specifically)
**Date:** 2026-07-22
**Source:** `KooshaPari/2phenoEvents` (21 KB, 1 branch, last push 2026-07-18)
**Target:** n/a — pointer-only
**Disposition:** POINTER-ONLY + ARCHIVE (A5 + archive; pending user green-light)

## Context: the layered history

This audit must reconcile a layered archive history that was not correctly captured in any prior audit.

1. **`KooshaPari/phenoEvents` was audited on 2026-07-17** with the claim: "absorbed into `KooshaPari/pheno` at `crates/phenotype-event-bus/`" (confidence 0.85).
2. **That claim is false** as of 2026-07-22: `gh api repos/KooshaPari/pheno/contents/crates/phenotype-event-bus` returns **404 Not Found**. `phenoEvents` is **not** absorbed into `pheno`. The absorb never landed, was reverted, or was made in a branch that wasn't merged.
3. **`KooshaPari/phenoEvents` is the live source-of-truth** for the EventBus port with hexagonal architecture. `src/` contains `bus/`, `core/`, `lib.rs`, `observability.rs`, `projection/`, `schema/` — all 10 source files present.
4. **`KooshaPari/2phenoEvents` is a redundant satellite** of `phenoEvents`: byte-identical (MD5 `4a81dec5249e35cd3c7032b512fdc20b` for `src/`+`tests/`+`benches/`), differing only in `Cargo.toml` package naming (`phenotype-event-bus` ↔ `pheno-events`) and `README.md`.

The audit for `phenoEvents` (`phenoEvents-2026-07-17.md`) is therefore **also stale**. It should be superseded in a future session; this audit does not modify it (additive-only rule).

## Confidence

**0.95** — VERY HIGH. Byte-identical evidence; no unique code; pure-redundant satellite.

## Source state (current remote, 2026-07-22)

| Field | Value |
|-------|-------|
| HEAD SHA | `5bb0c89` (main, 2026-07-18) |
| Size | 21 KB |
| Archived | NO (unarchived 2026-07-21) |
| Default branch | `main` |
| Tags | none |
| Tree | `CHANGELOG.md, Cargo.toml, README.md, SSOT.md, benches/, src/, tests/` |
| Working tree | clean |

## Branch inventory

| Branch | Last commit | ahead / behind main | Disposition |
|--------|-------------|---------------------|-------------|
| `main` | `5bb0c89` `feat: restore phenoEvents — EventBus port with hexagonal architecture` (2026-07-18) | — | BASELINE — only branch |

**Absorb strategy (A5 + archive):** No code merge needed (zero unique code). Register pointer in registry, rename source to `zz-archive-2phenoEvents`, set `archived=true`.

## Byte-identical evidence

Captured in `docs/sessions/2026-07-22-absorb-batch-1/REVERIFICATION.md` and verified via:

```sh
# Both repos' src/ + tests/ + benches/ hash to the same MD5:
( cd /tmp/zz-merge/2phenoEvents && find src tests benches -type f -exec md5 -q {} \; | sort | md5 -q )
# => 4a81dec5249e35cd3c7032b512fdc20b

( cd /tmp/zz-merge/phenoEvents && find src tests benches -type f -exec md5 -q {} \; | sort | md5 -q )
# => 4a81dec5249e35cd3c7032b512fdc20b

# CHANGELOG.md and SSOT.md also byte-identical.
# Only Cargo.toml (package name) and README.md differ.
```

## What is registered

```yaml
- source: KooshaPari/2phenoEvents
  parent: KooshaPari/phenoEvents
  shape: A5
  sha: 5bb0c89  # HEAD at audit time
  size_kb: 21
  absorbed: false
  notes: |
    Verified byte-identical src+tests+benches to phenoEvents
    (MD5 4a81dec5249e35cd3c7032b512fdc20b).
    Eventra retired (a6a3933 chore: archive Eventra in favor of phenoEvents).
    2026-07-17 audit's claim that phenoEvents was absorbed into pheno
    is FALSE (pheno/crates/phenotype-event-bus returns 404).
    No merge needed — pure-redundant satellite.
  audit: audits/absorption-justifications/2phenoEvents-2026-07-22.md
  parent_audit: audits/absorption-justifications/phenoEvents-2026-07-17.md  # stale; to be superseded next session
```

## Boundary

None. `2phenoEvents` is a redundant satellite of `phenoEvents`. The boundary lives at `phenoEvents`.

## Restore procedure

```sh
# Un-archive and rename back (if user later wants to revert the archive)
gh repo unarchive KooshaPari/zz-archive-2phenoEvents
gh repo edit KooshaPari/zz-archive-2phenoEvents --name 2phenoEvents
```

## Verification (pre-mutation)

- [x] Byte-identical evidence captured in REVERIFICATION.md
- [x] `phenoEvents` confirmed as live source-of-truth (not absorbed into pheno)
- [ ] Re-verify `2phenoEvents` HEAD SHA at moment of mutation

## Verification (post-mutation)

- [ ] Source repo renamed to `zz-archive-2phenoEvents`
- [ ] `archived=true` applied
- [ ] Description updated: "ARCHIVED 2026-07-22 — verified byte-identical to phenoEvents/src. See ADR-007 + this audit."

## Cross-references

- Source: https://github.com/KooshaPari/2phenoEvents
- Parent (live): https://github.com/KooshaPari/phenoEvents
- Parent audit (stale, to be superseded): `audits/absorption-justifications/phenoEvents-2026-07-17.md`
- Session: `docs/sessions/2026-07-22-absorb-batch-1/00_SESSION_OVERVIEW.md`
- Spec stub: `docs/sessions/2026-07-22-absorb-batch-1/SPEC_STUB.md` (WI-4)
- ADR: `docs/adr/ADR-007-absorption-eligibility-boundary.md`

## Followup recommendations (out of scope for this audit)

1. **Supersede `phenoEvents-2026-07-17.md`** in a future session to reflect that the claimed `pheno` absorb never landed. Recommended action: re-affirm `phenoEvents` as canonical home for the EventBus port; mark the `pheno` absorb as "reverted or never merged."
2. **Track `pheno`'s workspace members** that are related to eventing: `crates/agileplus-events/`, `crates/phenotype-event-sourcing/`, and `agileplus/crates/agileplus-grpc/src/event_bus.rs`. These are siblings, not the same crate, but a future boundary audit should determine if any consolidation is warranted.
