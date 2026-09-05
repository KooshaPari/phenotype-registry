# Verification strategy

Documentation validation: enumerate the numbered full-screen audit table and unique repository URLs; enumerate ten plan files and fifty unique proposal headings with exactly five per file; resolve relative Markdown links; check no temporary absolute file links; run `git diff --check`; ensure staged paths are limited to this session directory. Record results in [publication manifest](PUBLICATION.md).

No product runtime tests are appropriate for this additive planning-only change. Per-proposal commands and acceptance fixtures are execution recipes, not results. Source code changes will require the repository's current contribution checks, meaningful targeted tests, platform verification where relevant and exact upstream CI/merge state.

Publication gate: commit scoped docs, push topic branch to origin, compare local HEAD to `git ls-remote origin refs/heads/docs/contribution-opportunities-20260904`. A successful documentation push does not mean fifty upstream PRs exist or any runtime gate passed.
