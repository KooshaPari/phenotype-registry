# Known Issues

| Issue | Impact | Required resolution |
|---|---|---|
| Eight sources use non-`main` defaults | Old scripts may compare the wrong branch | Resolve and record each actual default branch |
| Batch A placement errors | Prior disposition evidence may be attached incorrectly | Reconcile repository-to-destination placement |
| Disk is 98% full, about 22 GiB free | Full clones risk exhaustion | Use partial bare clones only |
| READY source could drift before action | Prior parity proof would no longer authorize archival | Immediately preflight the sole head `recovery/isolated-20260714`, exact commit `0aafdf9692c11abb6e426f36857aeec7bb6cd942`, exact tree `eb82ced16353219d85aa83c925819ae48cb36c16`, and canonical exact head before rename/archive |
| Recovery evidence is unique | Deletion would destroy preservation evidence | Keep `AgilePlus-recovery-evidence-20260714` on HOLD and never delete it |
| `Stashly` contradiction | Disposition is unsafe | Keep on HOLD until contradiction closes |
| `phenotype-teamcomm` contradiction | Disposition is unsafe | Keep on HOLD until contradiction closes |
| Ecosystem validator baseline fails | Global validation is not currently green | Track baseline: 18 reachable, 2 unreachable, 17 drift, 47 items |
| Docs build baseline fails | Full docs gate cannot pass in this session | Fix Vue missing end tag at `docs/specs/pheno-specs/specs/platform/build-system/PRD.md:65:60` |

No issue above authorizes bypassing SHA/content parity or preservation controls. Only
`AgilePlus-recovery-20260714` is READY, and its safe action is rename to
`zz-archive-AgilePlus-recovery-20260714` and archive after immediate preflight, never deletion.
