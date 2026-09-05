# melgarafael/DeskcommCRM: five contribution proposals

**Goal:** Five bounded useful contributions, offered separately after scope and ownership checks.

**Architecture:** Preserve current upstream boundaries. These are plans, not implemented changes; reported bugs still require reproduction.

**Tech stack:** TypeScript / Next.js / PostgreSQL.

Inspected September 5 UTC 2026. Refresh HEAD and issue/PR state before execution.

**Overlap and policy:** Active triage/reconciliation: inspect #576/#578/#590 and issue ownership before code. Public open PR endpoint returned none at snapshot, not a guarantee of no parallel work. Tests requiring DB use pnpm test:db in isolated services.

**Repository checks:** `pnpm test:unit && pnpm typecheck && pnpm lint`. Commands are proposed validation, not checks run on upstream changes in this session.

## DC01: Follow-up graph collision validation

- **Evidence/status:** [Source](https://github.com/melgarafael/DeskcommCRM/issues/586). Reporter already offers patch: coordinate, do not take over.
- **Source paths:** `app/app/ai/followups/[id]/_components/FlowCanvas.tsx`.
- **Scope:** Offer focused regression/validation support around reporter's fix; exclude automatic repair of historical corrupt graphs.
- **Non-goals:** Unrelated cleanup, dependency upgrades, and already implemented functionality.
- **Validation/acceptance:** Load graph with sparse/nonstandard IDs, remount, add nodes/edges; no saved element replaced; reject duplicate IDs before save. All stated scenarios must pass with preserved supported behavior and recorded reproduction evidence.
- **Effort:** 4-8 engineering hours after setup; excludes maintainer delay.
- **Dependencies/engagement:** Check current issue ownership and coordinate feature scope; no dependency on other planned PRs unless upstream overlap requires it.
- **Value:** Produces demonstrable follow-up graph collision validation work useful to SMB customer operations and product engineering; record shipped behavior and measured benefit for resume evidence.

- [ ] Inspect full source and current instructions, record SHA, and refresh overlapping work.
- [ ] Reproduce the concrete scenario; retire/re-scope if already addressed.
- [ ] Agree scope, implement one bounded change, and verify using the scenarios and repository checks above.
- [ ] Prepare a PR with before/after evidence and attribution when submission is authorized.

## DC02: Decode legacy text knowledge uploads

- **Evidence/status:** [Source](https://github.com/melgarafael/DeskcommCRM/issues/531). Reported cp1252 decoding defect.
- **Source paths:** `lib/ai/rag/extractors/markdown.ts`, `lib/contacts/csv.ts`.
- **Scope:** Reuse agreed decoding utility instead of duplicating charset heuristics.
- **Non-goals:** Unrelated cleanup, dependency upgrades, and already implemented functionality.
- **Validation/acceptance:** UTF-8 and cp1252 accented text decode correctly; binary rejected; extracted RAG text matches input; valid UTF-8 unchanged. All stated scenarios must pass with preserved supported behavior and recorded reproduction evidence.
- **Effort:** 4-8 engineering hours after setup; excludes maintainer delay.
- **Dependencies/engagement:** Check current issue ownership and coordinate feature scope; no dependency on other planned PRs unless upstream overlap requires it.
- **Value:** Produces demonstrable decode legacy text knowledge uploads work useful to SMB customer operations and product engineering; record shipped behavior and measured benefit for resume evidence.

- [ ] Inspect full source and current instructions, record SHA, and refresh overlapping work.
- [ ] Reproduce the concrete scenario; retire/re-scope if already addressed.
- [ ] Agree scope, implement one bounded change, and verify using the scenarios and repository checks above.
- [ ] Prepare a PR with before/after evidence and attribution when submission is authorized.

## DC03: Correct scheduling input-error response

- **Evidence/status:** [Source](https://github.com/melgarafael/DeskcommCRM/issues/540). Reported wrong status; current reproduction required.
- **Source paths:** `app/api/v1/agenda/agendamentos/route.ts`.
- **Scope:** Map specific caller error and extend route-level regression; no broader agenda redesign.
- **Non-goals:** Unrelated cleanup, dependency upgrades, and already implemented functionality.
- **Validation/acceptance:** Invalid lead target yields 422; genuine server error stays 500; route test exercises behavior rather than only library. All stated scenarios must pass with preserved supported behavior and recorded reproduction evidence.
- **Effort:** 3-6 engineering hours after setup; excludes maintainer delay.
- **Dependencies/engagement:** Check current issue ownership and coordinate feature scope; no dependency on other planned PRs unless upstream overlap requires it.
- **Value:** Produces demonstrable correct scheduling input-error response work useful to SMB customer operations and product engineering; record shipped behavior and measured benefit for resume evidence.

- [ ] Inspect full source and current instructions, record SHA, and refresh overlapping work.
- [ ] Reproduce the concrete scenario; retire/re-scope if already addressed.
- [ ] Agree scope, implement one bounded change, and verify using the scenarios and repository checks above.
- [ ] Prepare a PR with before/after evidence and attribution when submission is authorized.

## DC04: Unknown catalog count stays unknown

- **Evidence/status:** [Source](https://github.com/melgarafael/DeskcommCRM/issues/539). Reported null-count pagination defect.
- **Source paths:** `lib/catalogo/busca.ts`.
- **Scope:** Preserve unknown count and partial-scan semantics, update tool description if needed; exclude unrelated KPI pagination.
- **Non-goals:** Unrelated cleanup, dependency upgrades, and already implemented functionality.
- **Validation/acceptance:** Three-thousand-row fixture with count null cannot falsely assert absence; complete search still returns known result; partial scan labeled. All stated scenarios must pass with preserved supported behavior and recorded reproduction evidence.
- **Effort:** 4-8 engineering hours after setup; excludes maintainer delay.
- **Dependencies/engagement:** Check current issue ownership and coordinate feature scope; no dependency on other planned PRs unless upstream overlap requires it.
- **Value:** Produces demonstrable unknown catalog count stays unknown work useful to SMB customer operations and product engineering; record shipped behavior and measured benefit for resume evidence.

- [ ] Inspect full source and current instructions, record SHA, and refresh overlapping work.
- [ ] Reproduce the concrete scenario; retire/re-scope if already addressed.
- [ ] Agree scope, implement one bounded change, and verify using the scenarios and repository checks above.
- [ ] Prepare a PR with before/after evidence and attribution when submission is authorized.

## DC05: Deterministic prompt-time invariant

- **Evidence/status:** [Source](https://github.com/melgarafael/DeskcommCRM/issues/506). Reported flaky assertion; culprit must be reproduced.
- **Source paths:** `tests/invariants/o-turno-diz-ao-modelo-que-dia-e-hoje.test.ts`.
- **Scope:** Target assertion to actual time block/full expected string; never weaken timezone guarantee or alter wall clock.
- **Non-goals:** Unrelated cleanup, dependency upgrades, and already implemented functionality.
- **Validation/acceptance:** Inject unrelated 14:30 timestamp outside time block; correct block passes and wrong timezone inside block fails. All stated scenarios must pass with preserved supported behavior and recorded reproduction evidence.
- **Effort:** 3-6 engineering hours after setup; excludes maintainer delay.
- **Dependencies/engagement:** Check current issue ownership and coordinate feature scope; no dependency on other planned PRs unless upstream overlap requires it.
- **Value:** Produces demonstrable deterministic prompt-time invariant work useful to SMB customer operations and product engineering; record shipped behavior and measured benefit for resume evidence.

- [ ] Inspect full source and current instructions, record SHA, and refresh overlapping work.
- [ ] Reproduce the concrete scenario; retire/re-scope if already addressed.
- [ ] Agree scope, implement one bounded change, and verify using the scenarios and repository checks above.
- [ ] Prepare a PR with before/after evidence and attribution when submission is authorized.
