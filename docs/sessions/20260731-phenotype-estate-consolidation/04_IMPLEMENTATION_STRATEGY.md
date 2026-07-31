# Implementation Strategy

## Preserve-first

Work in isolated worktrees. Snapshot existing dirty state with Airlock before adding edits. Never reset or clean a user checkout. Remote refs are the recovery boundary.

## Reconciliation

Compare exact PR head and current remote `main`; classify unique commits, duplicate merged commits, conflicts, generated/cache files, and unowned files. Promotion packets contain source SHA, remote ref, test output, review evidence, and merge SHA.

## Contract evidence

Use narrow fixtures rather than code copying. The Tracera fixture proves evidence create/list and explicit-link forward trace behavior. New overlaps require semantic comparison, provenance graph, canonical owner, and parity fixture.

## Review

Each implementation receives a fresh spec-compliance review followed by a fresh code-quality review before parent validation or publication.
