# Cross-Project Sync

## Disposition Matrix

| Disposition | Repositories | Sync requirement |
|---|---|---|
| ARCHIVED-PRESERVED / complete | `zz-archive-AgilePlus-recovery-20260714` (docketed as `AgilePlus-recovery-20260714`) | Preflight, rename, archive, and postverification complete; preserved, never deleted |
| HOLD | `AgilePlus-recovery-evidence-20260714` | Preserve as unique evidence; never delete |
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
- Exactly one READY action completed: `AgilePlus-recovery-20260714` is now
  `zz-archive-AgilePlus-recovery-20260714`, `ARCHIVED-PRESERVED`. Its sole head
  `recovery/isolated-20260714` is exact commit `0aafdf9692c11abb6e426f36857aeec7bb6cd942`, and
  canonical AgilePlus contains that exact commit and tree
  `eb82ced16353219d85aa83c925819ae48cb36c16` with the exact head.
- Postverification records `archived=true`, `private=true`, `fork=false`, default branch
  `recovery/isolated-20260714`, one branch, zero tags, unchanged
  `pushed_at=2026-07-16T00:20:23Z`, and an old-name redirect. No deletion occurred.
- The other 19 repositories retain their HOLD or VERIFY-ONLY dispositions.
- No other project receives a READY remote-mutation signal until both SHA and content parity are
  recorded.
- Cross-project updates must carry the actual default branch and corrected Batch A destination.
