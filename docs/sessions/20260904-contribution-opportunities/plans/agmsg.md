# agmsg: five proposed contributions

Repository: https://github.com/fujibee/agmsg. Evidence inspected 2026-09-04 Pacific / September 5 UTC. These are plans, not reproduced fixes or claimed issues. Source paths were confirmed through the live HEAD tree; hooks-json.sh and inbox.sh were also read. Baseline: [CONTRIBUTING.md](https://github.com/fujibee/agmsg/blob/main/CONTRIBUTING.md) requires focused squash PRs, `bats tests/`, and issue discussion for substantial changes; incompatible disk layouts require an ADR. Engineering estimates exclude review latency.

Overlap evidence: [open issues/PRs](https://github.com/fujibee/agmsg/issues?q=is%3Aopen) and [recent closed PRs](https://github.com/fujibee/agmsg/pulls?q=is%3Apr+is%3Aclosed+sort%3Aupdated-desc), sampled September 5 UTC. Not an exhaustive guarantee: recheck issue timelines and open PRs before implementation. Specifically excluded mark-read reporting: issue #1011 remains open but PR #1013 already merged; terminal-driver #1014 and Codex lifecycle #1016 are occupied. All proposals require current reproduction and an owner/assignee check before upstream submission.

## AGMSG-01: Preserve unrelated hooks during delivery-mode changes

- Evidence: VERIFIED reported defect [#1038](https://github.com/fujibee/agmsg/issues/1038), not locally reproduced. Inspected `scripts/lib/hooks-json.sh` uses `instr(command, SKILL_NAME)` for ownership; matching a substring can remove a user wrapper.
- Scope: narrow ownership matching in `scripts/lib/hooks-json.sh` and its callers in `scripts/delivery.sh`; regressions in existing `tests/test_delivery.bats`. Preserve mixed hook arrays and exact user command bytes. Non-goal: replacing the hook schema or changing Windows launching.
- Acceptance: switching each delivery mode preserves a user hook named `agmsg-my-wrapper.sh`, removes only installed hooks, and remains idempotent for paths with spaces/quotes. Run `bats tests/test_delivery.bats`, then `bats tests/`.
- Overlap: open sample had no matching PR; exclude #1029 Windows payload work. Sequence first, independent; 1-2 engineering days. Confirm owner agrees on exact-path versus tagged-entry ownership before coding. Value: dependable cross-agent integration and a concrete configuration-preservation case study.

## AGMSG-02: Add file/stdin message-body input

- Evidence: VERIFIED request [#1032](https://github.com/fujibee/agmsg/issues/1032). Shell interpolation occurs before the CLI; do not mislabel this as a CLI executing supplied text. User requests a safer argument interface.
- Scope: `scripts/send.sh`, `tests/test_messaging.bats`, `tests/test_local_quoting.bats`, and sending examples in `scripts/drivers/types/*/template.md`. Retain positional compatibility; agree on `--body-file` and stdin flags. No changes to terminal poke implementation or message storage schema.
- Acceptance: backticks, dollar expressions, newlines, quotes, Unicode, and trailing newlines survive supported storage round trips; missing/unreadable files fail explicitly; ambiguous positional/flag combinations are rejected. Define NUL policy because Bash variables cannot preserve NUL. Run `bats tests/test_messaging.bats tests/test_local_quoting.bats`, then `bats tests/`.
- Overlap: coordinate with terminal-driver #1014 but keep shipped send interface independent. Sequence second; 2-3 days. Maintainer flag/byte-contract alignment required. Value: safer agent automation and reliable review-message transport.

## AGMSG-03: Distinguish an unknown member from an empty inbox

- Evidence: VERIFIED report [#1027](https://github.com/fujibee/agmsg/issues/1027); inspected `scripts/inbox.sh` returns quiet success on absent storage before checking current membership.
- Scope: check roster membership through existing `scripts/lib/storage.sh` facade in `scripts/inbox.sh`; extend `tests/test_inbox.bats`. No identity-key migration, auto-join, or creation of a store during a read.
- Acceptance: registered empty inbox remains successful, unregistered/renamed-away names produce an agreed explicit diagnostic and status, `--quiet` suppresses ordinary emptiness but not invalid identity, sqlite/jsonl behavior agrees. Run `bats tests/test_inbox.bats tests/test_storage_contract.bats`, then `bats tests/`.
- Overlap: #1023/#1017 concern lock identity; this issue explicitly separates inbox behavior. Sequence third; 1-2 days. Align exit status with hook callers before implementation. Value: eliminates false healthy agent states and demonstrates useful CLI contract design.

## AGMSG-04: Clean role-session records during both despawn paths

- Evidence: VERIFIED report [#1041](https://github.com/fujibee/agmsg/issues/1041), describing graceful and forced teardown leaving records. Reused-name/resurrection consequences are unmeasured; do not claim they occurred.
- Scope: `scripts/despawn.sh`, `scripts/lib/role-session.sh`, existing `tests/test_despawn.bats` and `tests/test_role_session.bats`. Remove only the target member's record after the agreed teardown point; retain diagnostic state when teardown fails. No bulk cleanup or rewriting historical sessions.
- Acceptance: graceful/forced success removes the target role record; other team/member files remain; repeated teardown is safe; failed teardown follows documented retention semantics. Run `bats tests/test_despawn.bats tests/test_role_session.bats`, then `bats tests/`.
- Overlap: issue sample has no corresponding PR; coordinate with #1023 path-key changes. Sequence fourth before AGMSG-05; 1-2 days. Agree failure cleanup semantics. Value: reliable session lifecycle ownership and cleanup without collateral data loss.

## AGMSG-05: Make compound identity keys collision-free with migration

- Evidence: VERIFIED measured issue [#1023](https://github.com/fujibee/agmsg/issues/1023): `(a__b,c)` and `(a,b__c)` map to one run-file path. Not observed in live teams by reporter.
- Scope: `scripts/lib/actas-lock.sh`, `scripts/lib/role-session.sh`, `scripts/rename.sh`, and existing `tests/test_actas_lock.bats`/`tests/test_identity_path_forms.bats`. Choose unambiguous encoding or stable identity keys through an ADR; migrate/read legacy names without stealing active claims. No blanket deletion or unrelated terminal redesign.
- Acceptance: separator/Unicode/percent-containing names remain distinct, rename preserves exclusivity, active legacy locks remain honored, migration is idempotent and interrupted migration recoverable. Run `bats tests/test_actas_lock.bats tests/test_identity_path_forms.bats tests/test_role_session.bats`, then `bats tests/`.
- Overlap: coordinate #1017, #1023, and terminal-driver work. Depends on accepted identity ADR and AGMSG-04 path helper agreement; 3-5 days. Value: durable identity design and migration experience. Highest review burden in this five; hold until earlier collaboration establishes trust.
