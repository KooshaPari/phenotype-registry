# Bounded momentum check

Checked 2026-09-04 Pacific / 2026-09-05 UTC. One request per repository, parallel, no retries.

Method: gh api -i -H 'Accept: application/vnd.github.star+json' 'repos/OWNER/REPO/stargazers?per_page=100'. Intended to use Link last-page metadata for recent starring timestamps. All ten first-page requests returned HTTP 404, including independently verified Wallos. These failures establish this endpoint was unavailable in this execution context, not that repositories are nonexistent. No second-page request possible. Last-30-day additions, earliest timestamp and growth remain UNKNOWN. Existing repository star totals are separate evidence.

| Repository | Last-30-day star additions | Evidence |
|---|---|---|
| ayuayue/PiDeck | UNKNOWN | HTTP 404 from stargazers endpoint |
| Javis603/token-monitor | UNKNOWN | HTTP 404 from stargazers endpoint |
| openwong2kim/wmux | UNKNOWN | HTTP 404 from stargazers endpoint |
| fujibee/agmsg | UNKNOWN | HTTP 404 from stargazers endpoint |
| fkiene/llmtrim | UNKNOWN | HTTP 404 from stargazers endpoint |
| NadirRouter/NadirClaw | UNKNOWN | HTTP 404 from stargazers endpoint |
| toby-bridges/api-relay-audit | UNKNOWN | HTTP 404 from stargazers endpoint |
| thushan/olla | UNKNOWN | HTTP 404 from stargazers endpoint |
| gglucass/headroom-desktop | UNKNOWN | HTTP 404 from stargazers endpoint |
| ellite/Wallos | UNKNOWN | HTTP 404 from stargazers endpoint |

Do not label these ten verified rising based on this check. Current small-project candidates is supportable with independent metadata. Even observed additions would not establish net growth because unstars are unobserved.
