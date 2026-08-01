# Current Estate Scorecard

Date: 2026-08-01

Evidence window: `2026-08-01 08:32:46Z-08:35:27Z`

Evidence source: [PR #450](https://github.com/KooshaPari/phenotype-registry/pull/450), head
`b31203dd4b72afd81fb608e7c1b91b5438931a7c`

Baseline: `phenotype-registry/main` at `052c5eff4856cf800db0776c286bd53e18f84318`

## Executive state

The current GitHub metadata snapshot resolves all twenty intake names into four observable
classes. It contradicts the older consolidation packet's statement that only docket #1 was
archived and the other nineteen remained HOLD or VERIFY-ONLY. The snapshot is authoritative for
current repository metadata, but it does not identify the actor, transition event, or sponsor
authorization. This scorecard therefore records a contradiction, not an unauthorized-action
finding.

```text
11 archive-named target/archived  +  2 archived in place  +  3 owner API path unavailable  +  4 active  = 20 intake names
```

## Gate scorecard

| Gate | Result | Evidence / exit condition |
|---|---|---|
| Intake coverage | PASS | PR #450 records 20/20 intake names and full default-branch metadata |
| Current cloud classification | PASS | 11 archive-named target/archived, 2 in-place archived, 3 owner API paths unavailable under current credentials, 4 active |
| Ref/evidence preservation | HOLD | Preserve every current head and locally retained source artifact; 404 rows need durable bundles, redirects, or audit evidence |
| Transition provenance | BLOCKED | Obtain GitHub actor/time receipts for each rename/archive transition |
| Sponsor authorization | BLOCKED | Obtain an explicit sponsor receipt or prior approved execution packet; current metadata is not authorization |
| Registry reconciliation | BLOCKED | Do not edit `registry/disposition-index.json` until provenance and authorization gates pass |
| Protected CI promotion | DEFERRED | Resume after contradiction gates and independent registry/CI review are resolved |

## Current-state classes

| Class | Count | Safe conclusion | Next proof |
|---|---:|---|---|
| Archive-named target/archived | 11 | Current `zz-archive-*` path and default head are observable | GitHub audit actor/time plus sponsor receipt |
| Archived in place | 2 | `router-docs` and `template-commons` remain addressable and archived | Archive event and boundary receipt |
| Owner API path unavailable | 3 | `AgilePlus-recovery-evidence-20260714`, `agileplus-spec-harmonizer-tool-archive-2026-07-14`, and `4sgm-archive` returned 404 under the current credentials | Search/redirect/audit evidence or a durable preservation bundle; do not infer deletion intent |
| Active | 4 | `PriceyApp` is an untouched fork; `Quillr`, `Stashly`, and `phenotype-teamcomm` are active non-forks | Preserve current refs and re-check disposition before any proposal |

## Reconciliation policy

Until both blocked gates close:

1. Freeze destructive follow-up: no restore, archive, unarchive, rename, delete, force-push, or
   history rewrite.
2. Preserve current remote refs and any local/source evidence already retained.
3. Reconcile the session packet and registry only through a separately reviewed,
   sponsor-approved change.
4. Keep `PriceyApp` untouched as a fork and keep the three 404 rows unresolved rather than
   recreating or deleting anything.

The older packet remains useful historical evidence, but its prior disposition totals must not be
treated as current cloud truth until this reconciliation completes. PR #450 is the current
metadata evidence window for this scorecard; it does not authorize remote or registry mutation.

## Next exit criteria

```text
PR #450 evidence
      |
      +--> immutable per-row refs / bundles
      +--> actor + transition timestamps
      +--> sponsor authorization receipt
                    |
                    v
         approved session + registry reconciliation
                    |
                    v
          resume protected CI-gated promotion
```
