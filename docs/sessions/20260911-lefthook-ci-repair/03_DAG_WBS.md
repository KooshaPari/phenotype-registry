# Work breakdown

1. [G] Read instructions, inspect dirty main/worktrees and actual failed job logs.
2. [G] Research official binary support, download artifacts, verify checksums.
3. [G] Fix both installers, CLI compatibility and PR-title shell boundary.
4. [G] Validate syntax, positive/negative installers and real commit-msg invocation.
5. [G] Commit only allowlisted files, publish separate branch and PR, inspect remote CI.

Only phenotype-registry is in scope. No sibling PRs or absorption work.
Existing unrelated baseline pre-commit guard failures are documented, not bypassed.
