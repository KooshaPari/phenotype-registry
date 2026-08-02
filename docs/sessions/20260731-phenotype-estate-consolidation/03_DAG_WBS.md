# DAG and WBS

```text
P0 inventory
  -> P1 preserve dirty/ahead/local-only states
      -> P2 verify remote refs and exact SHAs
          -> P3 refresh GitHub refs
              -> P4 reconcile branches to current main
                  -> P5 repair CI/reviews/security
                      -> P6 merge verified PR heads
                          -> P7 local/installed dogfood
                              -> P8 registry closeout
                                  -> P9 sponsor-approved archive/tombstone

D1 semantic dedup -> D2 contract/parity fixture -> D3 spec review -> D4 quality review
A0 thegent-sharecli archive-only lineage -> A1 parity fixture -> A2 sponsor gate

2026-08-01 tranche:
  C0 source-bearing dirty capture (5/5 cloud refs)
    -> C1 parent-boundary proof (Tracera + sharecli + pheno disposition complete)
      -> C2 update registry scorecard/DAG (this commit)
        -> C3 protected PR promotion (#443 -> #441/#442 synchronization)
          -> C4 residual generated/local classification
            -> C5 sponsor-gated merge/archive packets

Boundary lanes:
  Tracera KEEP standalone -- PhenoObservability producer contract -- Grapheon lineage diff
  sharecli KEEP Rust runtime -- thegent-sharecli archive-only -- coordination parity fixture
  pheno AgilePlus/HexaKit parent hypothesis -- crate/API/consumer proof -- sponsor gate
```

| ID | Tag | Work item | Exit evidence |
|---|---|---|---|
| P0 | [G] | Full estate inventory | all source-bearing paths classified |
| P1 | [G] | Preserve dirty/ahead/local-only state | recoverable refs prepared |
| P2 | [G] | Verify cloud refs | `git ls-remote` exact SHA records |
| P3 | [P] | Refresh authoritative GitHub state | current main/PR table |
| P4 | [P] | Reconcile active branches | no stale-base merge candidate |
| P5 | [P] | Repair required checks/reviews | green required checks |
| P6 | [G] | Merge | protected-branch merge SHA |
| P7 | [G] | Dogfood | reproducible local/installed run |
| D1-D4 | [P]/[G] | Dedup and reviews | contract evidence plus required governance review |
| P9 | [G] | Archive/tombstone | sponsor-approved reversible packet |
| C0 | [ok] | Capture SessionLedger, pheno-harness, Tracera, sharecli, and pheno dirty payloads | immutable recovery refs: `ec278e3c`, `9fdef790`, `47ef7f41`, `08ad5d10`, `6140133` |
| C1 | [ok] | Prove parent boundaries for captured lanes | Tracera KEEP standalone; sharecli KEEP Rust/archive-only Python; AgilePlus and HexaKit HOLD standalone |
| C2 | [ok] | Refresh scorecard, known issues, inventory, and this DAG | commits `d277759`, `712f43d`; Airlock snapshot required before turn end |
| C3 | [wip] | Attach isolated docs/workflow repairs, then synchronize #441/#442 | repair refs published (`4160517`, `e25fc2`, `4dc7b5`, `a7c39fe`); checks and sponsor review remain |
| C4 | [wip] | Classify residual generated/local payloads and stash provenance | pheno follow-up must force-add ignored manifests; SessionLedger mutation output remains excluded; sharecli post-capture file changed |
| C5 | [hold] | Merge/archive/tombstone packets | sponsor approval, green protected checks, and reversible evidence |

AgilePlus is a governance dependency, not a prerequisite for preserving source state. AgilePlus's checked-in DB could not open WAL on the full volume; planning used an isolated DB and the limitation is recorded in session overview.
