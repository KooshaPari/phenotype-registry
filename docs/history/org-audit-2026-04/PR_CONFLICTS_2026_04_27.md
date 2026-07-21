# PR Conflicts Audit - 2026-04-27

Scope: open, non-draft pull requests under `KooshaPari`, excluding archived repositories.

The installed `gh search prs` command does not expose the `mergeable`, `headRefName`,
or `baseRefName` JSON fields, so the audit verified the open PR inventory with both
`gh search prs` and the GitHub Search API before conflict enrichment. Both returned
zero open non-draft PRs for the requested owner scope.

| Repo | # | Title | EligibleAutoRebase |
|---|---:|---|---|
