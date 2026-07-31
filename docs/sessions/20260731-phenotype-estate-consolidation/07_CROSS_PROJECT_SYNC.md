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
