# REPO_MAP Extension Proposal - 2026-04-27

Pages enablement for the first 100 non-archived `kooshapari` repos was verified live. The current
`REPO_MAP` already covers `tokn`, `thegent`, `policystack`, `hexakit`, `helioslab`, `focalpoint`,
and `agileplus`, so this proposal only includes Pages-enabled repos that are not already mapped.

| repo | hasPages | proposed-subdomain | confidence |
| --- | --- | --- | --- |
| agentapi-plusplus | true | agentapi | 0.74 |
| Civis | true | civis | 0.99 |
| cliproxyapi-plusplus | true | cliproxyapi | 0.75 |
| Dino | true | dino | 0.99 |
| heliosApp | true | heliosapp | 0.99 |
| hwLedger | true | hwledger | 0.99 |
| hwledger-landing | true | hwledger-landing | 0.98 |
| KDesktopVirt | true | kdesktopvirt | 0.99 |
| Parpoura | true | parpoura | 0.99 |
| pheno | true | pheno | 0.99 |
| phenokits-landing | true | phenokits-landing | 0.98 |
| projects-landing | true | projects-landing | 0.98 |

Notes:

- The live GitHub GraphQL schema in this environment does not expose `Repository.hasPages`, so Pages
  enablement was confirmed through the REST `/repos/{owner}/{repo}/pages` endpoint.
- `agentapi-plusplus` and `cliproxyapi-plusplus` are lower-confidence because the proposed
  subdomain is a brand-cleaned form of the repo slug rather than a direct slug mirror.
