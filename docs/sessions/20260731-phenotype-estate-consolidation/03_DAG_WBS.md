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
A0 thegent-sharecli unarchive request -> A1 publish preserved contract after access returns
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
| D1-D4 | [P]/[G] | Dedup and reviews | contract plus two reviewer approvals |
| P9 | [G] | Archive/tombstone | sponsor-approved reversible packet |

AgilePlus is a governance dependency, not a prerequisite for preserving source state. AgilePlus's checked-in DB could not open WAL on the full volume; planning used an isolated DB and the limitation is recorded in session overview.
