# Current Estate Scorecard

Evidence timestamp: 2026-08-01 04:56 UTC. GitHub values take precedence over stale local tracking refs.

| Repo | Local HEAD/state | Authoritative remote evidence | Grade | Gate |
|---|---|---|---:|---|
| AgilePlus | `ad2a1b07`; 22 dirty existing files; 20 local heads | `main=06c5823fea5c`; governance mirror `ad2a1b0705db...` on WIP branch; isolated AgilePlus validation `0/6` | C | attach CI/review evidence before any promotion |
| OmniRoute | `811d5964`; 2 dirty | `main=43f133f9972e`; #481 behind/CI red; #483 blocked | C- | current-main reconciliation and hosted CI |
| Tracera | `d58df9a13`; 105 dirty preserve files; 141 local heads | `main=774c0061e886`; clean candidate `3abfa031b92d653bb1050a0a7d18875c94684861`; draft PR #771 | C+ | smoke/Vercel failures; remaining hosted checks queued |
| phenotype-tooling | `5b854782`; 76 ahead stale local main; 2 dirty | `main=587805e38800`; #252 merged, branch 57 ahead/9 behind current main | C | classify post-merge branch |
| portage | `65e9ae47`; 2 dirty | `main=b35d00454fa8`; #495 dirty and required checks red | D | repair security/lint/type/test/verify |
| phenotype-registry | `49493f9`; 5 unrelated dirty files; governance packet committed | `main=052c5eff4856`; #441 `040eb7d`, #442 `ab2a6a9`, #443 `756ee14`; #432 blocked by unresolved OMLX gitlink | C+ | promote CI repair through normal governance, then synchronize and review promotion PRs |
| SessionLedger | `7b1c243e`; 23 dirty; 99 local heads | `main=71a781ff3a97`; #391 behind with visual/e2e/provenance failures | D | preserve, rebase, repair |
| phenoAI | `a73ac4d`; 9 behind/5 ahead; 1 dirty | `main=751a8e77f854`; #69/#70 unstable | C- | stabilize CI/coverage |
| phenotype-omlx | `58cd8768`; 2 dirty; 242 local heads | remote main unavailable from current origin transport; prior comparison 44 ahead/15 behind | C+ | rebase and parity proof |

## Roll-up

- Preservation: active and recoverable for the lanes explicitly snapshotted in this session.
- Deduplication: DEDUPE-01..05 and existing contract records are present.
- Promotion: no estate-wide release claim; multiple hosted gates remain red or stale.
- Archive/tombstone: none performed; all actions remain sponsor-gated.
- AgilePlus governance: feature is specified/researched/planned in isolated DB, but validation is `0/6` evidence items until CI/review artifacts are attached.
- AgilePlus governance mirror is cloud-published at `ad2a1b0705dbadaa5a46af6d0307a2caebc6f84`; the ignored local DB remains supplemental evidence only.
- Registry governance packet is cloud-published through Airlock branch `wip/20260801T0456-18c7958c07e938c0` at the latest scorecard snapshot.

## Promotion lanes

| PR | Head | Scope | Current disposition |
|---|---|---|---|
| #441 | `040eb7d` | pheno-errors reversible tombstone evidence | content-ready; required contexts await CI repair promotion and human approval |
| #442 | `ab2a6a9` | four-source provenance metadata | additive and live-verified; required contexts await CI repair promotion and human approval |
| #432 | `495d69b9` | broad absorption/OMLX preservation packet | hold/rework; `phenotype-omlx` gitlink `a7118ed9...` is not cloud-resolvable |
| #443 | `756ee14` | coverage workflow recovery trigger and protected check names | draft maintenance PR; `ci / lint` and `ci / test` pass on its head; unrelated secret-guard baseline remains red |

Repository Actions are enabled. PR #443 proves `coverage.yml` can emit `ci / lint` and `ci / test`; #441 and #442 still require a post-#443 synchronization after the workflow repair is promoted.
