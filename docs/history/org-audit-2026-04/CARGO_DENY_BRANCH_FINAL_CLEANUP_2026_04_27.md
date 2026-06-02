# Cargo Deny Branch Final Cleanup - 2026-04-27

Scanned 103 non-archived `KooshaPari` repositories with:

`git ls-remote --heads https://github.com/KooshaPari/$repo 2>&1 | grep -E "ci/cargo-deny|ci/add-starter-deny"`

Deleted: none.

No non-archived repo currently has multiple `ci/cargo-deny*` rollout branches, so there were no compact-date duplicates to remove. No `ci/cargo-deny-rollout-20260427` branch had a dashed-format sibling.

Retained:

- `helios-router`: `ci/add-starter-deny-toml-20260427`
- `GDK`: `ci/add-starter-deny-toml-20260427`

Both retained branches are the only matching rollout branch on their repo, are not ancestors of the default branch, and have no matching PR metadata. They were not deleted because the cleanup rule forbids deleting the only rollout branch unless it is clearly a duplicate or merged orphan.
