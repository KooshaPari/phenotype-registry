# Stale Remote Branch Audit

Audited: 2026-05-25  
Base: `origin/main` @ `e7c0842`

---

## Summary

| Branch | Unmerged commits | Status | Recommendation |
|--------|-----------------|--------|----------------|
| `origin/chore/add-dependabot` | 3 | Superseded | **DELETE** |
| `origin/chore/deny-toml-wildcards-deny` | 1 | Unmerged — real delta | **REVIEW / MERGE** |
| `origin/chore/pin-actions-sha` | 1 | Superseded | **DELETE** |
| `origin/chore/pin-github-actions-20260430` | 2 | Superseded | **DELETE** |
| `origin/ci/add-push-pr-workflow` | 3 | Partially superseded; new ci.yml not on main | **REVIEW / MERGE** |
| `origin/docs/sladge-badge` | 1 | Superseded | **DELETE** |
| `origin/feat/journey-impl` | 1 | Superseded (merged via squash as #34) | **DELETE** |
| `origin/fix/add-rust-version` | 1 | Unmerged — real delta | **REVIEW / MERGE** |
| `origin/pr-33` | 2 | Superseded by direct commits on main | **DELETE** |

---

## Branch-by-branch Detail

### `origin/chore/add-dependabot` — DELETE

3 unmerged commits:
- `bbf74a4` docs: add sladge badge
- `4e49741` ci: add Dependabot for automated dependency updates
- `32c037e` chore: add rust-toolchain.toml for MSRV clarity

All three changes are already on `main` as equivalent commits (`ca2eabc`,
`4472d9e`, and `1bf3e0f`/`c80504f`). The diff vs main is only SHA-pinning
style on a few older `actions/checkout@v4` references, which were superseded
by the dedicated `chore/pin-github-actions-*` work. Branch is safe to delete.

---

### `origin/chore/deny-toml-wildcards-deny` — REVIEW / MERGE

1 unmerged commit:
- `908c71f` chore: change deny.toml wildcards warn->deny

This is a real, un-landed change: flips `wildcards = "warn"` to
`wildcards = "deny"` in `deny.toml`. Nothing equivalent is on `main`.
Stricter deny policy is consistent with org standards. Recommend opening/
merging a PR unless there is an active cargo wildcard dep that would block CI.

---

### `origin/chore/pin-actions-sha` — DELETE

1 unmerged commit:
- `bbf74a4` docs: add sladge badge

The only "unmerged" commit on this branch is the sladge-badge docs commit,
which is already on `main` (merged as part of #30). The actual SHA-pinning
work this branch was named for is fully present on `main` (`cabd7e6`,
`f439899`, `c80504f`). Safe to delete.

---

### `origin/chore/pin-github-actions-20260430` — DELETE

2 unmerged commits:
- `bbf74a4` docs: add sladge badge (already on main)
- `6b5ff00` chore: pin all GitHub Actions to commit SHAs

The SHA-pinning work in `6b5ff00` targets `cargo-deny.yml`, `fr-coverage.yml`,
and `quality-gate.yml`. Main already has equivalent or more up-to-date pinning
via `cabd7e6` and `f439899`. The specific SHAs used differ (this branch used
older SHAs) — the delta would be a net regression vs current main. Safe to
delete.

---

### `origin/ci/add-push-pr-workflow` — REVIEW / MERGE

3 unmerged commits:
- `576be36` chore: add trufflehog.yml secrets scanning (already on main as `e7c0842`)
- `a1c7034` chore: commit untracked infrastructure files
- `b78d6c7` ci(phenotype-bus): add push/PR CI workflow

The notable real delta:
1. `.github/workflows/ci.yml` — a minimal push/PR CI workflow running
   `cargo test --all-features` + `cargo clippy`. **This file does not exist
   on main.** The `quality-gate.yml` on main runs `cargo test --verbose` but
   only on push to main; this would add PR-gate coverage.
2. `trufflehog.yml` root-level file — `a1c7034` lands this, and main already
   has the same content at root via `e7c0842`. Net-new content is only ci.yml
   and the cargo-deny-action SHA upgrade (`@v2` → `@91bf2b6`).

Recommend reviewing whether the new `ci.yml` PR workflow should land. The
`EmbarkStudios/cargo-deny-action` SHA upgrade is also a useful security
hardening on top of main.

---

### `origin/docs/sladge-badge` — DELETE

1 unmerged commit:
- `bbf74a4` docs: add sladge badge

This exact change (README badge + session overview docs) is already on `main`
as part of commit `1bf3e0f` lineage and further commits. Safe to delete.

---

### `origin/feat/journey-impl` — DELETE

1 unmerged commit:
- `3917409` docs: add journey-traceability + iconography implementation

The subject matches main commit `8fd0895` ("docs: add journey-traceability +
iconography implementation (#34)"). This was merged to main via squash-merge
as PR #34. The branch tip commit is the pre-squash version. Safe to delete.

---

### `origin/fix/add-rust-version` — REVIEW / MERGE

1 unmerged commit:
- `e7a4230` ci: add rust-version MSRV policy

Adds `[workspace.package] rust-version = "1.75"` to `Cargo.toml`. This is
not present on `main`. Setting an explicit MSRV in `Cargo.toml` is org policy
(rust-toolchain.toml already pins 1.83 on main; this would publish the
published crate MSRV as 1.75 for downstream consumers). Recommend merging
after verifying the MSRV value is still correct relative to current
`rust-toolchain.toml`.

---

### `origin/pr-33` — DELETE

2 unmerged commits:
- `576be36` chore: add trufflehog.yml secrets scanning
- `a1c7034` chore: commit untracked infrastructure files

Both changes are already on `main` (`e7c0842` for trufflehog.yml, and
`bb554fa`/`e7c0842` for the infrastructure files). This branch appears to be
the pre-merge head of PR #33. Safe to delete.

---

## Deletion Candidates (7 branches)

```
git push origin --delete chore/add-dependabot
git push origin --delete chore/pin-actions-sha
git push origin --delete chore/pin-github-actions-20260430
git push origin --delete docs/sladge-badge
git push origin --delete feat/journey-impl
git push origin --delete pr-33
```

Note: These commands are provided for reference only. Verify via GitHub UI
before running, as remote deletions are irreversible.

## Branches Requiring Action (2 branches)

- `origin/chore/deny-toml-wildcards-deny`: open a PR to harden deny.toml wildcards policy
- `origin/fix/add-rust-version`: open a PR to publish MSRV in Cargo.toml (verify 1.75 is still correct)
- `origin/ci/add-push-pr-workflow`: open a PR to add the PR-gate CI workflow (ci.yml) + cargo-deny-action SHA pin
