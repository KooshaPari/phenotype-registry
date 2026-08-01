# Current Estate Scorecard

Evidence timestamp: 2026-08-01 09:42 UTC. GitHub values take precedence over stale local tracking refs.

| Repo | Local HEAD/state | Authoritative remote evidence | Grade | Gate |
|---|---|---|---:|---|
| AgilePlus | `16da102a`; clean; local main ahead 3 after stash recovery | `main=06c5823fea5c`; dirty-state recovery ref `wip/preserve-20260801/agileplus-dirty-0605` at `16da102a`; isolated AgilePlus validation `0/6` | C+ | attach CI/review evidence before any promotion |
| OmniRoute | `811d5964`; 2 dirty | `main=43f133f9972e`; #481 behind/CI red; #483 blocked | C- | current-main reconciliation and hosted CI |
| Tracera | `d334cd587`; 76 dirty preserve files; preserve branch ahead 8 | `main=774c0061e886`; latest HEAD snapshot `wip/20260801T0834-18c7a16c00a168a8`; clean candidate `3abfa031b92d653bb1050a0a7d18875c94684861`; draft PR #771 | C+ | capture remaining dirty payload before promotion; smoke/Vercel failures remain |
| phenotype-tooling | `5b854782`; 76 ahead stale local main; 2 dirty | `main=587805e38800`; #252 merged, branch 57 ahead/9 behind current main | C | classify post-merge branch |
| portage | `65e9ae47`; 2 dirty | `main=b35d00454fa8`; #495 dirty and required checks red | D | repair security/lint/type/test/verify |
| phenotype-registry | `097051e`; 6 dirty entries (5 docs + OMLX gitlink); governance packet committed | `main=052c5eff4856`; #441 `040eb7d`, #442 `817a497`, #443 `756ee14`; #432 blocked by unresolved OMLX gitlink | C+ | promote CI repair through normal governance, then synchronize/review promotion PRs |
| SessionLedger | `7b1c243e`; 19 tracked + 4 untracked entries (17 files); 99 local heads | `main=71a781ff3a97`; recovery `wip/preserve-20260801/sessionledger-dirty-capture-0902` -> `ec278e3c`; #391 behind with visual/e2e/provenance failures | D+ | preserve remaining generated/local payloads, then rebase/repair |
| pheno-harness | `fix/pheno-harness-runner-provenance@4131b7c`; 2 tracked + 52 untracked entries | source branch head `4131b7c`; recovery `wip/preserve-20260801/pheno-harness-dirty-capture-0902` -> `9fdef790`; exclusion manifest committed | C+ | preserve linked worktree separately, then evaluate harness/tooling boundary |
| phenoAI | `a73ac4d`; 9 behind/5 ahead; 1 dirty | `main=751a8e77f854`; #69/#70 unstable | C- | stabilize CI/coverage |
| phenotype-omlx | `31cada2d`; 1 dirty; feature branch behind 29 | `main=c88431ad6004`; recovery ref `wip/preserve-20260801/phenotype-omlx/recovery--phenotype-omlx-local-20260726` at `8a1150f` | C+ | keep archive-only boundary; finish parity/provenance proof |

## Roll-up

- Preservation: active and recoverable for the lanes explicitly snapshotted in this session.
- Deduplication: DEDUPE-01..05 and existing contract records are present.
- Promotion: no estate-wide release claim; multiple hosted gates remain red or stale.
- Archive/tombstone: none performed; all actions remain sponsor-gated.
- AgilePlus governance: feature is specified/researched/planned in isolated DB, but validation is `0/6` evidence items until CI/review artifacts are attached.
- AgilePlus governance mirror is cloud-published at `ad2a1b0705dbadaa5a46af6d0307a2caebc6f84`; the ignored local DB remains supplemental evidence only.
- Registry governance packet is cloud-published through Airlock branch `wip/20260801T0945-18c7a54c94a57d30` at the latest scorecard snapshot.

## Promotion lanes

| PR | Head | Scope | Current disposition |
|---|---|---|---|
| #441 | `040eb7d` | pheno-errors reversible tombstone evidence | content-ready; required contexts await CI repair promotion and human approval |
| #442 | `817a497` | four-source provenance metadata and key normalization | review-fix pushed; Kilo re-review pending; required contexts await CI repair promotion and human approval |
| #432 | `495d69b9` | broad absorption/OMLX preservation packet | hold/rework; `phenotype-omlx` gitlink `a7118ed9...` is not cloud-resolvable |
| #443 | `756ee14` | coverage workflow recovery trigger and protected check names | draft maintenance PR; `ci / lint` and `ci / test` pass on its head; docs-build and unrelated secret-guard baselines remain red |

Repository Actions are enabled. PR #443 proves `coverage.yml` can emit `ci / lint` and `ci / test`; #441 and #442 still require a post-#443 synchronization after the workflow repair is promoted.
