# Research and Ownership

## Boundaries

ResearchLedger owns corpus-repair implementation and its candidate evidence. Benchora owns performance-harness and PR #107 remediation under `BOUNDARY_OWNERS.md` Performance / Benchmark Harness (status: active per `projects/Benchora.json` and `BOUNDARY_OWNERS.md`). phenotype-registry owns only routing links.

**Benchora lane status:** Blocked until ownership records are reconciled. The Benchora lane for PR #107 remediation is not gated by this session's routing packet; exact-head revalidation and scorecard/Sonar/Infisical evidence belong to Benchora.

## Split targets

| Target | Role | Evidence limit |
| --- | --- | --- |
| ResearchLedger | Sole implementation lane | PR #81 `5ada3d8` is published; `fbf2d0d` and active list-support tests are unpublished/local, not completion evidence. |
| Benchora | Owner of #107 findings | The plan is local, committed on an unpublished temporary branch at the path in `00_SESSION_OVERVIEW.md`; do not represent it as hosted. |
| phenotype-registry | Link/governance record | This packet does not replace either owner artifact. |

## Prior state and deferrals

Historical Benchora #107 `668ceed` reportedly repaired gates green, while the stated snapshot retains scorecard `32/88 < 35`, Sonar fail, and Infisical queued. Exact-head revalidation belongs to Benchora. Historical contradictory catalog records are preserved, not reconciled here.
