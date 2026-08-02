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

2026-08-02 live checkpoint:
  L0 protected main provenance (#448/#453/#454/#455/#456/#457)
    -> L1 current-main baseline `3b3edc2`
        -> L2 rebase-only repair lanes (#444-#452 and legacy history)
            -> L3 hosted required checks and review receipts
                -> L4 sponsor-selected registry/pointer action

  OMLX boundary hold:
    parent gitlink `60243d...` (local-only)
      -> cloud reachability proof OR sponsor-selected pointer candidate `52682309...`
          -> ancestry/tree/CI proof
              -> attach only through a protected registry PR

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
| C2 | [ok] | Refresh scorecard, known issues, inventory, and this DAG | local baseline `bf9123d`; live `main=3b3edc2`; Airlock `wip/20260802T2150-18c81b6d5de30938` |
| C3 | [wip] | Synchronize current promotion PRs after live-main repair integration | `wip/preserve-20260802/registry-repair-integration` -> `3b3edc2` is clean against live main; hosted PR synchronization and sponsor review remain |
| C4 | [wip] | Classify residual generated/local payloads and stash provenance | pheno source follow-up `ee890798` and OmniRoute source/stash refs `03c6b8a`/`omniroute-stash-0..5` are preserved; forgecode, pheno-harness, and thegent residual deltas remain |
| C5 | [hold] | Merge/archive/tombstone packets | sponsor approval, green protected checks, reversible evidence, and OMLX pointer decision; current `60243d...` gitlink is not cloud-resolvable |

AgilePlus is a governance dependency, not a prerequisite for preserving source state. AgilePlus's checked-in DB could not open WAL on the full volume; planning used an isolated DB and the limitation is recorded in session overview.
