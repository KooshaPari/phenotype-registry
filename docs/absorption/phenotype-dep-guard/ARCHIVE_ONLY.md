# phenotype-dep-guard archive-only package

Date: 2026-06-20
Source: KooshaPari/phenotype-dep-guard
Decision: ARCHIVE_ONLY
Confidence: medium

| Source Item | Source Evidence | Category | Source State | Target Repo | Target Evidence | Status | Deletion Justification | Risk if Deleted | Required Action |
|---|---|---|---|---|---|---|---|---|---|
| Dependency guard concept | repo description Dependency guard for pheno repos; RATIONALIZATION_PLAN says keep supply-chain audit | Product intent | docs-only / empty scaffold | phenotype-registry / future substrate | RATIONALIZATION_PLAN row: Keep (supply-chain audit; Python, different domain) | PARTIAL | Source has little implementation, but the domain is not formally absorbed into a tighter owner yet. | medium - deletes named supply-chain audit placeholder before replacement is declared | last-resort exception |
| Local governance scaffold commit | local phenotype-dep-guard main...origin/main ahead 1, commit f3a25af; adds CODEOWNERS, issue/PR templates, changelog, justfile | Governance artifacts | local-only | none | preserved by this package summary; local repo remains | BRANCH_ONLY | Not deletion-safe until the local commit is either pushed to a WIP branch or intentionally dropped as no-merit governance scaffold. | medium - loses local branch work | preserve branch or document no-merit |

Executive decision: ARCHIVE_ONLY. Do not delete yet. Minimum next action: either push local f3a25af to a WIP branch after temporarily unarchiving, or preserve a patchset in registry and explicitly mark the repo NO_MERIT/DELETE in a follow-up PR.
