# Cargo-Deny TRUE Coverage — 2026-04-27 LATE3 (Parent-Direct Local Probe)

## Honest framing
Earlier dashboards (v62 through v66) claimed cargo-deny rollout coverage of "36/36" (v62), then "61/61 = 100%" (v66 correction). **Both were wrong.** This doc is a parent-direct probe of local /repos/*/ canonical clones.

## Method
```
for d in /repos/*/; do
  [ ! -f "$d/Cargo.toml" ] && continue
  has_yml=[ -f "$d/.github/workflows/cargo-deny.yml" ]
  has_dispatch=grep "workflow_dispatch:" "$d/.github/workflows/cargo-deny.yml"
  has_deny_toml=[ -f "$d/deny.toml" ]
done
```

## TRUE state (local, 2026-04-27 ~01:30 PDT)
| Metric | Count | % |
|---|---|---|
| Total local Rust repos | 42 | 100% |
| has cargo-deny.yml | 18 | 43% |
| has workflow_dispatch in cargo-deny.yml | 5 | 12% |
| has deny.toml | 35 | 83% |

## Repos MISSING cargo-deny.yml (24 of 42 local)
AgilePlus, bare-cua, GDK, helios-router, HeliosLab, HexaKit, KlipDot, kmobile, pheno, phenoAI, phenoData, PhenoKits, PhenoProc, PhenoRuntime, phenoShared, phenotype-journeys, phenotype-tooling, PhenoVCS, PlayCua, rich-cli-kit, [+4 truncated by parent display].

## Why previous audits were wrong
1. `gh api repos/.../contents/<file>` returns empty content (not 404) when file is missing → audits mis-classified as HAS_FILE_NO_DISPATCH
2. base64 decode noise on empty content lines silently dropped detection
3. v66 inherited the bug; "100% file presence" was a hallucination

## Action items for next /loop fire (when rate limit resets at 09:11 UTC)
1. Open PRs to add cargo-deny.yml + workflow_dispatch to 24 missing repos (cap 5 per session for billing)
2. Mark v62/v63/v64/v65/v66 dashboards as SUPERSEDED-BY-CORRECTION; do NOT re-cite their "100%" claims
3. Re-verify the 18 HAS files actually run (most are NEVER_RAN per cron-only triggers)

## Cross-references
- Memory: feedback_cargo_deny_real_coverage_2026_04_27.md
- Memory: feedback_audit_decode_false_positives.md
- Memory: feedback_audit_freshness_decay.md
- Superseded: ORG_DASHBOARD_v66_2026_04_27_CORRECTED.md, CARGO_DENY_DISPATCH_GAP_2026_04_27.md (commit d2e1eec), cargo-deny rollout completion (commit 1cef9cd)
