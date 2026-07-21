# Governance Repo Taxonomy Proposal (Kimi-generated 2026-04-27)

## Current state
80+ docs in `org-audit-2026-04/` flat folder. Scales poorly past 200 docs.

## Recommended 10-folder taxonomy (scales to 200+)

```
phenotype-org-governance/
├── 00-templates/         (PR/CONTRIBUTING/SECURITY/CODEOWNERS templates)
├── 01-current/            (canonical, authoritative state docs — dashboards, indices)
├── 02-superseded/         (archived dashboards w/ supersede-by pointers)
├── 03-archived/           (truly historical, rarely referenced)
├── supply-chain/          (cargo-deny, dependabot, SBOM, supply-chain audits)
├── static-analysis/       (CodeQL, clippy, semantic checks, fuzzing)
├── platform-ops/          (CI workflows, billing, runners, infrastructure)
├── access-mgmt/           (CODEOWNERS, branch protection, rulesets, SSO)
├── compliance-soc2/       (SOC2 control mappings)
└── compliance-iso/        (ISO27001 control mappings)
```

## Migration path
1. Create folders empty
2. Move existing docs by topic match (cargo-deny → supply-chain/, codeql → static-analysis/, etc)
3. Update internal cross-refs (find/replace `org-audit-2026-04/` paths)
4. Keep `org-audit-2026-04/` as a date-bucketed convenience symlink-or-redirect to topic folders

## Tradeoffs
- ✅ scales to 200+ docs without folder bloat
- ✅ enables agent navigation by intent
- ❌ requires migration effort
- ❌ may break external links to specific audit doc paths
