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
| C4 | [wip] | Classify residual generated/local payloads and stash provenance | pheno source follow-up `ee890798`, OmniRoute `03c6b8a`/`omniroute-stash-0..5`, forgecode `ab49d70`, and thegent `thegent-stash-0..4` are preserved; stash payload classification and pheno-harness checksum review remain |
| C5 | [hold] | Merge/archive/tombstone packets | sponsor approval, green protected checks, reversible evidence, and OMLX pointer decision; current `60243d...` gitlink is not cloud-resolvable |

AgilePlus is a governance dependency, not a prerequisite for preserving source state. AgilePlus's checked-in DB could not open WAL on the full volume; planning used an isolated DB and the limitation is recorded in session overview.

## 2026-08-03 capture/gate checkpoint

```text
K0 current-main + hosted PR snapshot
  -> K1 preserve-only refs and local-only boundary classification
      -> K2 semantic/ancestry/consumer proof
          -> K3 sponsor-selected PR synchronization
              -> K4 protected ci / lint + ci / test
                  -> K5 merge or archive packet (sponsor gate)
```

| Node | State | Evidence / next gate |
|---|---|---|
| K0 | [ok] | live registry `main=3b3edc2`; local docs `0a5eead1`; Airlock `wip/20260803T0019-18c8239a3080e110` |
| K1 | [ok] | pheno `ee890798`, forgecode `ab49d70`, thegent `b9ce6c1`, ResearchLedger `3b3facc`, phenotype-tooling inbox delta `a24b0329` |
| K2 | [wip] | pheno-rt-spec-probe 8/9 absorbed-file divergences; Planify2 fork/site/infra proof; next-20 consumer/ancestry checks |
| K3 | [hold] | #391/#392/#399/#432/#440/#441/#442/#443/#445/#446/#447/#449/#450/#451 behind; #393/#426/#427/#444/#452 dirty |
| K4 | [hold] | strict protected contexts `ci / lint` and `ci / test` are not green across candidate heads |
| K5 | [hold] | no merge/archive/tombstone authorized; require sponsor selection and reversible packet |

## 2026-08-03 source-capture and hosted-gate refresh (05:49 UTC)

The following are the authoritative refs observed from the live remotes during this
refresh.  The earlier disputed prefixes are now directly cloud-verifiable:
`7c3a043f8245e206fc90c9bbf64c6220fdf32a72` on
`ResearchLedger:wip/preserve-20260803/researchledger-github-source-delta`, and
`dd03d08584e839356743d5955ae27f398a62661d` on
`KooshaPari/forgecode:wip/preserve-20260803/forgecode-source-delta`.  No merge,
archive, tombstone, delete, reset, or force-push was performed.

```text
ResearchLedger
  capture  c501b0e66c591cb14737d6a8c356101d14a21000
  parent   7f4736f401fc225c0594ece59efe1f726df6ec03
  tree     76b907905358f70fc15695c249c2612cc1e5bcc8
  diff256  83cf54eb26dd136ceb9a0ed813155d48904e325baa3ea2b95e856257c5289b7a
  remote   wip/preserve-20260803/researchledger-github-dirty-capture

forgecode
  capture  8ff6fcbe1d2e5490664ddc0a7d4fe126c1c1c56e
  parent   74464752a22e5d53138a821a186c2f78278f670f
  tree     a7bedd100d01c76ef99b7aa27aa2f041c45a774c
  diff256  38510ad684888a82444061a8d4c062cd0049f09bf0e7cea93beb8f9695656c25
  remote   wip/preserve-20260803/forgecode-dirty-capture
  installer 6d7ca1265d95fda230ddacf21c6206710d8a2b30 (same tree/diff)

phenotype-tooling
  capture  a24b0329f6249538094276e8f35b54388f54cf63
  parent   134d35599d76273c7d404e377834ab30db54c9f1
  tree     829c3d4258079a5033993a10005d31338fd05908
  diff256  121411aacf00592bb198c56e49743577728da9e2741b7e8544361cb60415934b
  remote   wip/preserve-20260803/phenotype-tooling-inbox-delta

thegent
  source   0e719cf15d4b8f618674acc4726bb7db8e86b0d8
  parent   d0f31a24d61e7abcd90cb077073f5444892396da
  tree     1bdf7688795bd372cf4ef04e98879dcacce3b018
  diff256  6c4d3ba162911ba5e132d5f5c7a24f339abbee4e1fe8745262d0c246125854e3
  remote   wip/preserve-20260803/thegent-source-delta
```

The forgecode installer capture and phenotype-tooling capture are source-only
preservation refs.  Current working-tree deltas remain separate evidence and must
be captured before rebase or parent selection.  The live registry parent is
`main=3b3edc26864bc60878192828a186db04c37fed9d`; hosted PR heads remain behind or
dirty, and strict `ci / lint` plus `ci / test` are not a fleet-wide green gate.

## Prompt-to-gate coverage ledger (2026-08-03)

| Sponsor mandate | State | Evidence / gap that remains |
|---|---|---|
| Preserve-first; no destructive reset, delete, prune, force-push, or hidden archive | evidenced | Checkpoints above record preserve-only refs and no destructive action; promotion/retirement remains gated. |
| Find and consolidate at least 20 small repositories into correct parent boundaries | in progress | Next-20 rows classify Benchora, PhenoPlugins, PlayCua, asset-engine, nanovms, and RepoLedger; complete 20 scored rows with consumer, ancestry, hash, and owner proofs. |
| Collect local worktrees, unpushed branches, and loose source to the cloud | in progress | Captures include ResearchLedger `c501b0e`, forgecode `8ff6fcb`/installer `6d7ca12`, OmniRoute `e4c5385`, `9a77bea`, `df070a3`, and thegent helper `7cda67f`; current dirty follow-ups and hfscope classification remain. |
| Mature enterprise-grade registry/governance tree | in progress | Live `main=3b3edc26864bc60878192828a186db04c37fed9d` and protected contexts are recorded; open PRs remain stale/dirty and non-required hosted failures remain. |
| Maintain split boundaries and avoid premature absorption | evidenced / in progress | Tracera, sharecli, AgilePlus, and HexaKit boundaries are classified; consumer/API/ancestry parity is still required before parent or archive action. |
| Use delegated agents with Sol as coordinator; close idle workers | in progress | Agent-produced evidence packets are incorporated; worker lifecycle is orchestration metadata and must be closed/verified outside repository commits. |
| Self-approval only within Koosha-owned repos while respecting branch protection | externally gated | Protection requires strict `ci / lint` and `ci / test`, linear history, and conversation resolution; no bypass or merge is claimed. |
| Maintain a rich forward DAG/WBS with critical gates | evidenced | P0-P9 and K0-K5 above define inventory, preservation, proof, checks, promotion, dogfood, and sponsor gates. |
| Validate Luna configuration before claiming Luna execution | in progress | `codex-cli 0.146.0` accepted `gpt-5.6-luna` probe output `LUNA_MODEL_PROBE_OK`; no agent-file selector is documented and full dispatch hung on stdin, so no worker audit is claimed. |
| Preserve all session goals, prompts, ideas, and decisions without drift | in progress | This ledger maps the principal mandates; exhaustive historical prompt-to-evidence reconciliation remains open. |
| Keep a dashboard repo-state bracket with exact SHA, gate, and next action | evidenced / in progress | Current scorecard and hosted checkpoints provide SHA/gate brackets; refresh timestamps and newly captured refs before promotion. |
