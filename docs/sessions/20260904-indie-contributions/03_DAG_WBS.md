# Work breakdown and dependencies

[G] Publish researched plan -> [G] select a candidate and refresh source/overlap -> [G] reproduce or agree feature scope -> [P] implement one bounded change -> [G] verify -> [G] submit when authorized -> review/merge evidence -> next proposal.

## Ownership

| Lane | Plan owner in this session | PR proposals |
|---|---|---:|
| Gateways and business workflows | plan_gateways | 30 |
| Local developer tools | plan_tools | 20 |
| Registry publication and reconciliation | root | Documentation only |

Each repo has its own queue. At execution time, start with one PR per repo, and at most two active upstream contribution lanes overall. Advance subsequent proposals based on maintainer feedback. Five plans per repo are a backlog, not a requirement to flood maintainers with five simultaneous PRs.

[G] ccproxy: obtain current public maintainer response before feature investment. [G] source changes or occupied issues: re-scope before coding. [NB] historical star growth, founder employment history, and long-term breakout estimates remain unknown and do not prevent useful contributions.

Primary first wave: KR, TM. Next wave: OC, LY. Secondary projects follow after evidence of fit. Per-plan dependencies override this suggested scheduling; do not force artificial dependency chains between independent fixes.

Effort estimates in plans measure engineering work, not maintainer response time. They are preliminary until reproduction and environment setup.

