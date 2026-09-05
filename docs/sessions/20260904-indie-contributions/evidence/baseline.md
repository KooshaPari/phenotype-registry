# OmniRoute contribution baseline and previous report corrections

Evidence retrieved September 4, 2026 Pacific time (September 5 UTC), using GitHub REST and public primary-source pages. This report owns only this new artifact; no repository source, Git refs, or external accounts were changed.

## Finding

The user's correction is supported by OmniRoute's early PR history: outsiders could contribute substantial product features and have Diego merge them within hours. Maintainer willingness to integrate outside work is a stronger selection criterion than technical similarity or institutional prestige.

## Historical external PR examples

Every PR below was merged by `diegosouzapw`. Timestamps are UTC. Counts come from the individual GitHub pull-request REST objects.

| PR | Contributor | Scope | Created | Merged | Elapsed |
| --- | --- | --- | --- | --- | --- |
| [94](https://github.com/diegosouzapw/OmniRoute/pull/94) | StealthIQ | JWT setup and login; 7 files, +213/-57 | 2026-02-21 02:50:47 | 2026-02-21 09:55:40 | 7h 04m 53s |
| [109](https://github.com/diegosouzapw/OmniRoute/pull/109) | nyatoru | Codex workspace binding; 7 files, +262/-83 | 2026-02-22 18:15:18 | 2026-02-22 19:34:19 | 1h 19m 01s |
| [118](https://github.com/diegosouzapw/OmniRoute/pull/118) | nyatoru | API manager, permissions and UI; 8 files, +1313/-281 | 2026-02-23 17:01:01 | 2026-02-23 19:58:20 | 2h 57m 19s |
| [127](https://github.com/diegosouzapw/OmniRoute/pull/127) | npmSteven | Multiplatform Docker workflow; 1 file, +78/-16 | 2026-02-24 18:28:20 | 2026-02-25 09:03:47 | 14h 35m 27s |
| [140](https://github.com/diegosouzapw/OmniRoute/pull/140) | npmSteven | Split-port runtime; 22 files, +375/-47 | 2026-02-26 15:16:45 | 2026-02-27 19:30:29 | 28h 13m 44s |
| [150](https://github.com/diegosouzapw/OmniRoute/pull/150) | benzntech | Electron desktop application; 18 files, +7080/-78 | 2026-02-28 05:12:34 | 2026-02-28 10:52:31 | 5h 39m 57s |
| [174](https://github.com/diegosouzapw/OmniRoute/pull/174) | MAINER4IK | Themes and internationalization; 35 files, +956/-39 | 2026-03-02 13:43:42 | 2026-03-02 15:14:07 | 1h 30m 25s |

This is a deliberately selected illustrative sample, not an acceptance-rate denominator. Current `author_association: CONTRIBUTOR` does not establish first-time status when submitted. Lines changed include all files and are not a measure of engineering quality.

## Automated review qualification

Early OmniRoute already used automated review. PR 94 had a Gemini review. PR 118 had two Gemini reviews and 22 inline review comments. PR 150 had Gemini and Kilo reviews and 10 inline comments. The review texts included security concerns; this audit did not validate those findings or their resolution. The PRs nevertheless merged quickly.

Accordingly, bot presence alone is a poor exclusion rule. Evaluate review turnaround, actionable scope, human maintainer engagement, and actual external merges. Do not equate quick merging with absent scrutiny or with verified code quality.

Primary evidence endpoints: `https://api.github.com/repos/diegosouzapw/OmniRoute/pulls/94/reviews`, `/pulls/118/reviews`, and `/pulls/150/reviews` under the same repository API path.

## Origin and maintainer background

- [OmniRoute README acknowledgments](https://github.com/diegosouzapw/OmniRoute#-acknowledgments) explicitly describe origin as a fork of [9router](https://github.com/decolua/9router) and a TypeScript port of [CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI). The REST repository object currently reports `fork: false` and `parent: null`; that metadata does not disprove source ancestry. This audit did not independently compare historical source trees.
- [Diego's GitHub profile](https://github.com/diegosouzapw) lists CDWA Solutions. The [profile README](https://github.com/diegosouzapw/diegosouzapw) links that business and describes his practical AI infrastructure and community work.
- [His public LinkedIn page](https://br.linkedin.com/in/diegosouzapw) describes hands-on architecture/backend experience. A public post calls OmniRoute his first open-source project, arising from subscription and model-switching frustration, and reports finding 9router at approximately 1,500 stars. These are self-reported statements, not independently established historical metrics. The indexed page supports practical professional background; it does not establish every claimed SMB/enterprise detail.
- Terms such as amateur or no-name are not established competence findings. Public evidence supports an individually led, practical project and receptive early maintainer.
- GitHub REST snapshot: repository created `2026-02-13T12:38:31Z`; **61,287 stars** at audit time. OmniRoute now exceeds the user's 50,000 ceiling and serves as a historical reference rather than an eligible new candidate.

## Corrections to the previous response

1. The purported 50-candidate pool contains **49 rows**: 6 + 12 + 31.
2. AgentOps appears in its top 10 but does not appear in its candidate pool.
3. OpenFeature Spec at the response's stated 1,250 stars was incorrectly placed in the 100-1,000 band.
4. The response's citations are malformed or not recoverable as evidence from the supplied conversation. Its asserted current star snapshot lacks inspectable support here. Treat those figures as unsupported rather than asserting they were proven fabricated.
5. The developer roster emphasized institutional position and module ownership. That establishes possible technical relevance, but does not demonstrate unfamiliar outside contributors can land the proposed changes.
6. Assertions that particular maintainers are approachable require actual response/merge evidence. Conversely, this audit does not establish that every institutional maintainer will reject outside PRs.

## Measurable replacement rubric

| Criterion | Evidence to collect | Interpretation |
| --- | --- | --- |
| Outside contribution acceptance | 10-20 recent external PRs, including open and closed-unmerged; separate owner and bots | Highest weight; do not cherry-pick only merged examples |
| Independent contributors | Substantive merged PRs from at least two independent people | Better evidence than maintainer self-merges |
| Acceptance denominator | Merged / closed external PRs, pending count and age | Explicit sample boundaries; not all-time probability |
| Review turnaround | First human response and open-to-merge time | Prefer median response under 72h and merge under seven days; proposed preferences, not universal facts |
| Accepted scope | Features, integrations, deployment fixes, refactors versus docs-only changes | Tests whether the desired contribution type actually lands |
| Owner participation | Actual responder and merger identity, recent activity | Identify a reachable decision maker, not merely a famous executive |
| Review friction | Assignment rules, scope restrictions, stale queues, explained closures | Penalize costly barriers and poor contributor treatment |
| Product fit | Personal utility, self-hosting, integration potential, backlog within our capabilities | At least three starter choices should directly support current work |
| Momentum | Dated star history when available | A current count alone cannot establish rising popularity |
| Credit | Attribution preserved across merge or replacement | Supports resume value and a sustainable relationship |

The target is a useful growing product with an active owner who demonstrably welcomes outside implementation. Quality, responsiveness, and room for meaningful contribution can coexist.

## Reproduction

Read-only commands used included `gh api repos/diegosouzapw/OmniRoute`, `gh api users/diegosouzapw`, individual `gh api repos/diegosouzapw/OmniRoute/pulls/NUMBER`, and their `/reviews` endpoints. Earliest PR discovery used the repository pulls endpoint sorted by creation ascending and GitHub issue search bounded before March 15, 2026, followed by individual PR verification. No acceptance rate was inferred from those discovery results.
