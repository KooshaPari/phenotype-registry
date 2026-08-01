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

## Cloud preservation refs (2026-08-01)

| Repo | Local source branch | Preserved remote WIP ref | Verified SHA |
|---|---|---|---|
| AgilePlus | `docs-preservation-fixes` | `wip/preserve-20260801/agileplus/docs-preservation-fixes` | `2fb6b68780d325dc087df563fe6d36cb1cd33c62` |
| AgilePlus | `docs/preservation-manifests-20260729-fix` | `wip/preserve-20260801/agileplus/docs--preservation-manifests-20260729-fix` | `0ed541dbeeab8922ba72681196ed51eb5a1061dd` |
| Tracera | `feat/agentora-http-ingest` | `wip/preserve-20260801/tracera/feat--agentora-http-ingest` | `929a0a6b0daecd231270f75e92ec0f1819baae66` |
| Tracera | `feat/agentora-replay-contract` | `wip/preserve-20260801/tracera/feat--agentora-replay-contract` | `02d80013a8caae06e7a8adb7b154300a737f4bca` |
| phenotype-tooling | `recovery/phenotype-tooling-plugins-20260726` | `wip/preserve-20260801/phenotype-tooling/recovery--phenotype-tooling-plugins-20260726` | `fd51689ac8c0cf1f2b6ae58e6cc97efd7709be3e` |
| phenotype-tooling | `wip/2026-07-22-phenotype-tooling-absorbed-go-mod` | `wip/preserve-20260801/phenotype-tooling/wip--2026-07-22-phenotype-tooling-absorbed-go-mod` | `5b854782b2e27021336c67379fa59ab5c77c491b` |
| portage | `feat/cross-repo-audit-fixes` | `wip/preserve-20260801/portage/feat--cross-repo-audit-fixes` | `8c0c2700aab908adc432f8f0da3cd277dba72846` |
| SessionLedger | `fix/sessionledger-forward-candidate` | `wip/20260801T0339-18c79151e6bc0418` (Airlock immutable snapshot) | `a5d315ba1d6df5f47d81a978b81deac5238dcf38` |
| phenoAI | `fix/phenoai-trunk-action-pin` | `wip/preserve-20260801/phenoai/fix--phenoai-trunk-action-pin` | `45b09e7f9a96f321113401cc98f3e5c461df2c90` |
| phenotype-omlx | `recovery/phenotype-omlx-local-20260726` | `wip/preserve-20260801/phenotype-omlx/recovery--phenotype-omlx-local-20260726` | `8a1150f831b24b5fb673ec3fde8ed71a335f484d` |

The namespaced SessionLedger preservation branch remains cloud-published but advanced to current source `fc541038446b3ff8953fe97138ebf7bb1d2e1fc9`; the original `a5d315ba` payload is preserved immutably by the Airlock ref above. This is provenance repair, not a force-push or deletion.
