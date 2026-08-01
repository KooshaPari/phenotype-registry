# Cross-Project Sync

| Project | Primary action | Sibling/related action | Order |
|---|---|---|---|
| Tracera | publish/reconcile dirty packet and fixture | PhenoObservability contract remains separate | preserve -> review -> PR -> dogfood |
| OmniRoute | reconcile #481/#483 | cliproxy path provenance | preserve -> rebase -> CI -> merge |
| phenotype-tooling | classify post-#252 branch | absorbed docs remain evidence | preserve -> compare -> promote/defer |
| portage | repair #495 | no intermediate-merge assumption | preserve -> current-main -> CI -> merge |
| phenotype-registry | reconcile #432 and publish ledger | all sibling evidence links here | preserve -> registry PR -> closeout |
| SessionLedger | preserve and repair #391 | release artifact/provenance checks | preserve -> rebase -> repair |
| phenoAI | stabilize #69/#70 | #68 remains historical merge | preserve -> CI -> merge |
| phenotype-omlx | prove parity after divergence | perf-core evidence remains separate | reconcile -> parity -> promote |
| AgilePlus | remain parked; governance spec recorded | no active merge train | sponsor reactivation only |

Archived thegent-sharecli is blocked pending sponsor-approved unarchive request.

## Current ordering

1. Hold PR #432 and split or repair the unresolved OMLX preservation pointer.
2. Let additive PR #442 precede any broad absorption work once Actions/protection and one human approval are resolved.
3. Keep PR #441 content-only and reversible; do not archive or delete `pheno-errors` from this packet.
4. Rebase broad absorption work only after the provenance lane is authoritative.
