# Known Issues

| Issue | Impact | Required resolution |
|---|---|---|
| Eight sources use non-`main` defaults | Old scripts may compare the wrong branch | Resolve and record each actual default branch |
| Batch A placement errors | Prior disposition evidence may be attached incorrectly | Reconcile repository-to-destination placement |
| Disk is 98% full, about 22 GiB free | Full clones risk exhaustion | Use partial bare clones only |
| Recovery pair identity unresolved | Duplicate or divergent provenance is possible | Keep both on HOLD until identity proof |
| `Stashly` contradiction | Disposition is unsafe | Keep on HOLD until contradiction closes |
| `phenotype-teamcomm` contradiction | Disposition is unsafe | Keep on HOLD until contradiction closes |
| Ecosystem validator baseline fails | Global validation is not currently green | Track baseline: 18 reachable, 2 unreachable, 17 drift, 47 items |
| Docs build baseline fails | Full docs gate cannot pass in this session | Fix Vue missing end tag at `docs/specs/pheno-specs/specs/platform/build-system/PRD.md:65:60` |

No issue above authorizes bypassing SHA/content parity or preservation controls.
