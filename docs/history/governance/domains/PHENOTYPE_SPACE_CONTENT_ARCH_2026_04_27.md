# phenotype.space content architecture (Kimi-generated 2026-04-27)

>>> dispatch-worker tier=nvidia/moonshotai/kimi-k2.5 model=nvidia/moonshotai/kimi-k2.5 endpoint=http://localhost:20128/v1
>>> routed to backend: moonshotai/kimi-k2.5
 Root phenotype.space hosts the narrative landing—vision, roadmap, team, and entry points. Paths (/blog, /roadmap) hold dynamic organizational content. Subdomains isolate heavy corpora: docs.phenotype.space for technical specs, governance.phenotype.space for the 80+ audit documents (trust-critical, require immutable versioning), and dedicated subdomains (e.g., explorer.phenotype.space, status.phenotype.space) for the seven live GitHub Pages sites that serve distinct applications.

Ship phenotype-org-governance to governance.phenotype.space with permanent release tags. Consolidate the seven scattered GitHub Pages properties: elevate tools with standalone user bases to their own subdomains; merge utility or plugin docs into docs.phenotype.space sections. Reserve paths only for tightly-coupled project metadata that updates frequently and does not require independent versioning.

Link graph: Hub-and-spoke from root. Root header links to docs, governance, and active tool subdomains; each subdomain carries a persistent "Home" return to root and footer links to siblings. Cross-link docs↔governance for audit trail references, but keep tools isolated to prevent navigation drift. Canonicalize all routes to prevent duplicate content across GitHub Pages and phenotype.space domains.
