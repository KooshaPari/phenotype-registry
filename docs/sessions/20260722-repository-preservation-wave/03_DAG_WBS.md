# DAG and WBS

```text
W0 manifest
  -> W1 namespaced preservation imports
       -> W2 GitHub reachability proof
            -> W3 archive proposal (separate HITL gate)
```

| Lane | State | Exit condition |
|---|---|---|
| W0 manifest | complete | Valid 20-row ledger committed and pushed |
| W1 import | pending | Missing refs exist in canonical parents |
| W2 proof | pending | GitHub resolves every imported SHA/ref |
| Local-gap audit | pending | Empty remote names reconciled with local storage |
| W3 archive | blocked | Requires W2 evidence and sponsor approval |
