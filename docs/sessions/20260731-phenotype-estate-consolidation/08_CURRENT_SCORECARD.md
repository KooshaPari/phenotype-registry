# Current Estate Scorecard

Evidence timestamp: 2026-07-31 UTC. GitHub values take precedence over stale local tracking refs.

| Repo | Local HEAD/state | Authoritative remote evidence | Grade | Gate |
|---|---|---|---:|---|
| OmniRoute | `811d5964`; 2 dirty | `main=43f133f9972e`; #481 behind/CI red; #483 blocked | C- | current-main reconciliation and hosted CI |
| Tracera | `b8d657e7`; dirty preserve packet | `main=774c0061e886`; corrected preservation ref `wip/20260731T0748-18c750581389c880` | B- | PR publication, hosted CI, dogfood |
| phenotype-tooling | `5b854782`; 76 ahead stale local main; 2 dirty | `main=587805e38800`; #252 merged, branch 57 ahead/9 behind current main | C | classify post-merge branch |
| portage | `65e9ae47`; 2 dirty | `main=b35d00454fa8`; #495 dirty and required checks red | D | repair security/lint/type/test/verify |
| phenotype-registry | `21af7f6`; 5 dirty; 28 ahead local comparison | `main=052c5eff4856`; #432 blocked | C | reconcile authoritative ledger |
| SessionLedger | `a22420c2`; 23 dirty; 7 behind | `main=71a781ff3a97`; #391 behind with visual/e2e/provenance failures | D | preserve, rebase, repair |
| phenoAI | `a73ac4d`; 9 behind/5 ahead; 1 dirty | `main=751a8e77f854`; #69/#70 unstable | C- | stabilize CI/coverage |
| phenotype-omlx | `ec2ab02a`; clean; 17 ahead local | remote comparison 44 ahead/15 behind | C+ | rebase and parity proof |

## Roll-up

- Preservation: active and recoverable for the lanes explicitly snapshotted in this session.
- Deduplication: DEDUPE-01..05 and existing contract records are present.
- Promotion: no estate-wide release claim; multiple hosted gates remain red or stale.
- Archive/tombstone: none performed; all actions remain sponsor-gated.
- AgilePlus governance: feature is specified/researched/planned in isolated DB, but validation is `0/6` evidence items until CI/review artifacts are attached.
- AgilePlus governance mirror is cloud-published at `ad2a1b0705dbadaa5a46af6d0307a2caebc6f84`; the ignored local DB remains supplemental evidence only.
