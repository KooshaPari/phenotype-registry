# Research

Live repo checks on 2026-04-27:

- `gh api repos/KooshaPari/BytePort` -> active, default branch `main`, no remote `clippy.toml`.
- `gh api repos/KooshaPari/FocalPoint` -> active, default branch `main`, no remote `clippy.toml`.
- `gh api repos/KooshaPari/helios-cli` -> active fork, default branch `main`, no remote `clippy.toml`.
- `gh api repos/KooshaPari/AgilePlus` -> active, default branch `main`, remote `clippy.toml` already present.
- `gh api repos/KooshaPari/PhenoMCP` -> active, default branch `main`, no remote `clippy.toml`.
- `gh api repos/KooshaPari/PhenoObservability` -> active, default branch `main`, no remote `clippy.toml`.
- `gh api repos/KooshaPari/hwLedger` -> active, default branch `main`, no remote `clippy.toml`.
- `gh api repos/KooshaPari/Sidekick` -> active, default branch `main`, no remote `clippy.toml`.

Implementation notes:

- Fresh clones were created under `/tmp/phenotype-clippy-rollout-2026-04-27/`.
- Standard file content used:

```toml
# Phenotype-org standard clippy config
msrv = "1.75"
avoid-breaking-exported-api = true
disallowed-methods = []
allow-dbg-in-tests = true
```

- `helios-cli` is a fork with an `upstream` remote; PR creation/merge needed an explicit `--repo KooshaPari/helios-cli` path to avoid targeting the wrong namespace.
- `hwLedger` initially cloned without a checked-out `HEAD`; fetching `origin/main` and switching to `main` repaired the checkout before commit.
