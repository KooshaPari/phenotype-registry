# DAG and Work Breakdown

## Dependency Graph

```text
inventory confirmation
  -> default-branch and fork resolution
  -> Batch A placement correction
  -> partial bare-clone evidence capture
  -> SHA parity + content parity
  -> disposition review
       -> HOLD remains preserved
       -> VERIFY-ONLY remains blocked or gains proof
       -> READY may be proposed, never assumed
```

## Lane T Work Breakdown

| Work package | Dependency | Exit condition |
|---|---|---|
| T1 inventory | none | Exact 20 reconciled |
| T2 metadata | T1 | Archive, fork, and actual default branch recorded |
| T3 evidence | T2 | Partial bare-clone SHA/content evidence captured |
| T4 correction | T2 | Batch A misplacements corrected |
| T5 disposition | T3, T4 | HOLD/VERIFY-ONLY rationale complete |
| T-P preservation | all | No destructive or remote mutation occurred |
