# Implementation Strategy

## Preserve-first

Work in isolated worktrees. Snapshot existing dirty state with Airlock before adding edits. Never reset or clean a user checkout. Remote refs are the recovery boundary.

## Reconciliation

Compare exact PR head and current remote `main`; classify unique commits, duplicate merged commits, conflicts, generated/cache files, and unowned files. Promotion packets contain source SHA, remote ref, test output, review evidence, and merge SHA.

## Contract evidence

Use narrow fixtures rather than code copying. The Tracera fixture proves evidence create/list and explicit-link forward trace behavior. New overlaps require semantic comparison, provenance graph, canonical owner, and parity fixture.

## Review

Each implementation receives a fresh spec-compliance review followed by a fresh code-quality review before parent validation or publication.

## TruffleHog workflow repair plan (2026-08-03)

Scope is limited to `.github/workflows/trufflehog.yml`; validate its interaction with
`.github/workflows/secret-guard.yml` and `scripts/workflow-action-guard.py`. This plan
does not authorize a workflow edit, branch rewrite, check rerun, or merge.

1. TDD first: capture the failing PR event fixture and assert that the rendered
   `pull_request` invocation receives only the reviewed range:
   `base: ${{ github.event.pull_request.base.sha }}` and
   `head: ${{ github.event.pull_request.head.sha }}`. Keep `fetch-depth: 0` only if
   the supported action contract requires the two commits to be available.
2. Separate triggers before changing action inputs: `pull_request` targets only
   `main`; `push` targets only `main`; `schedule` and `workflow_dispatch` are the
   only full-history lanes. The full-history lanes must not interpolate PR-only
   event fields; the PR lane must not fall back to a path/history-wide scan.
3. Use only documented inputs of the pinned
   `trufflesecurity/trufflehog@f446421baf832d6356c42c1743d99abff52ff334` action.
   Keep the PR `base`/`head` formulas above exact, and record the supported
   full-history invocation separately for `main` push, schedule, and manual runs.
   Do not introduce an unsupported wrapper, guessed action input, or credential.
4. Validate locally in order: `git diff --check`; `actionlint
   .github/workflows/trufflehog.yml` (or `yamllint .github/workflows/trufflehog.yml`
   if that is the installed workflow linter); then
   `python scripts/workflow-action-guard.py`. Re-run the focused workflow-fixture
   assertion after linting.
5. Hosted evidence is required before promotion: a PR run must prove the diff-only
   `base`/`head` invocation and green required `ci / lint` plus `ci / test`; a
   main/schedule/manual run must separately prove the intended full-history lane.
   A verified Sentry finding remains an incident/revocation gate, not evidence that
   a PR-local secret was introduced.
6. Rollback is an additive follow-up commit restoring the last known-good workflow
   semantics. Preserve existing refs and scan evidence; never rewrite history, force
   push, delete evidence, or assume a waiver.
