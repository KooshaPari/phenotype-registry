# Cross-Project Sync

## Disposition Matrix

| Disposition | Repositories | Sync requirement |
|---|---|---|
| HOLD | `AgilePlus-recovery-20260714`, `AgilePlus-recovery-evidence-20260714` | Resolve identity |
| HOLD | `phenotype-registry-archive`, `phenotype-org-audits-archive2`, `PhenoRuntime-archive`, `ResilienceKit-archive`, `phenotype-shared-archive` | Preserve pending parity evidence |
| HOLD | `Stashly`, `phenotype-teamcomm` | Resolve contradictions |
| VERIFY-ONLY | `agileplus-spec-harmonizer-tool-archive-2026-07-14`, `4sgm-archive`, `Parpoura-archive`, `phenoResearchEngine-archive`, `home-recovery-2026-07-archive`, `phenotype-monorepo-state-archive`, `agent-user-status-archive` | Capture branch, SHA, and content proof |
| VERIFY-ONLY | `Quillr` | Confirm tombstone evidence |
| VERIFY-ONLY | `router-docs` | Confirm absorption into OmniRoute; fork remote untouched |
| VERIFY-ONLY | `template-commons` | Confirm absorption into phenokits; fork remote untouched |
| HOLD | `PriceyApp` | Leave fork remote untouched |

## Coordination Contract

- Registry is the disposition ledger; source repositories remain preservation evidence.
- Lane T owns consolidation evidence; the preservation sublane enforces non-destructive handling.
- No project receives a READY remote-mutation signal until both SHA and content parity are recorded.
- Cross-project updates must carry the actual default branch and corrected Batch A destination.
