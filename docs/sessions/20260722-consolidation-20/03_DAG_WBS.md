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
       -> exactly one READY: AgilePlus-recovery-20260714
            -> immediate preflight
            -> rename to zz-archive-AgilePlus-recovery-20260714
            -> archive, never delete
```

## Lane T Work Breakdown

| Work package | Dependency | Exit condition |
|---|---|---|
| T1 inventory | none | Exact 20 reconciled |
| T2 metadata | T1 | Archive, fork, and actual default branch recorded |
| T3 evidence | T2 | Partial bare-clone SHA/content evidence captured |
| T4 correction | T2 | Batch A misplacements corrected |
| T5 disposition | T3, T4 | Exactly one READY; all other HOLD/VERIFY-ONLY rationale complete |
| T6 READY preflight | T5 | Sole head, exact commit/tree, and canonical exact head revalidated |
| T7 READY archive | T6 | Source renamed to `zz-archive-AgilePlus-recovery-20260714` and archived, never deleted |
| T-P preservation | all | No destructive or remote mutation occurred |
