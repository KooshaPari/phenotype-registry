# Implementation strategy

For each chosen proposal, read current upstream instructions and source at an identified SHA, search open/closed PRs and issues, and reproduce the stated behavior in an isolated checkout. If a feature is already implemented, replace the proposal with a demonstrated residual gap instead of reopening the same work.

Use one coherent problem per PR. Start with a failing regression scenario for behavior changes, apply the smallest coherent fix, run focused checks and required upstream checks, and document before/after behavior. For performance work, record environment, input, repeated measurements, and correctness parity. For docs, validate the documented procedure.

Preserve project-specific contribution rules. Octopus's prohibition on submitting test files does not waive local verification: retain verification evidence outside its submitted patch. Discuss meaningful feature/API changes when upstream requires it. Contributor attribution and published credit should remain explicit when maintainers fold work into follow-up PRs.

Resume evidence should describe shipped functionality and measured impact, not projected value or lines changed. Useful outcomes include reliable routing, accurate usage accounting, usable desktop behavior, and SMB workflow correctness.

