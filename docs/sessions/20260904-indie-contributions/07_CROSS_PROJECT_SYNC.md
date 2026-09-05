# Publication and cross-project synchronization

| Field | Value |
|---|---|
| Canonical repository | KooshaPari/phenotype-registry |
| Publication branch | docs/indie-contribution-plan-20260904 |
| Session path | docs/sessions/20260904-indie-contributions/ |
| Source baseline | 8b7e91ab32fc6ba45a915de77f671b5f4681402c |
| Upstream PRs submitted | None |
| Upstream code modified | None |
| Absorption or retirement | None |

AgilePlus registration succeeded with feature `indie-contribution-program-20260904` (Created -> Specified). The actual specification is `.agileplus/indie-contribution-program-20260904/spec.md`; the CLI printed a stale `kitty-specs/` location, so the filesystem was checked. The tracked SQLite database passed `PRAGMA integrity_check`.

Validation on September 5 UTC: 10 plan files, 50 unique proposal IDs, 50 unique research candidates, zero broken local file links, and all 96 declared upstream source-path references found in complete GitHub trees. `bun run docs:build` passed; only the existing bundle-size advisory appeared. Proposed upstream changes have not been runtime-tested.

The branch commit is the immutable publication unit. Verify publication with `git ls-remote origin refs/heads/docs/indie-contribution-plan-20260904` and compare against the local commit. Remote merge is not part of the requested documentation push.

## Source-tree verification snapshots

These are Git tree object IDs returned by the GitHub recursive-tree endpoint, not claimed commit IDs.

| Upstream | Verified tree |
|---|---|
| bestruirui/octopus | 27aa40dc0f3b2902bce3e96ccdba019d17041606 |
| Javis603/token-monitor | 19ff91191cff8c658dc5b3325eb9dc34d4701f41 |
| mydisha/keirouter | 633ad720955d974bddf291fa79e3a84a0c0aaec0 |
| starbaser/ccproxy | f2c47695b0835da023257aee0ac2a3dffd9fe570 |
| tbphp/gpt-load | c86a9ad1da1398c16954ef40f3d02b77bb41abfa |
| hewigovens/jayjay | 5d8a6fab4a034526d5987867ffba586a5055da56 |
| moona3k/macparakeet | 70dfbf5afdff1d09bc0822a2bc5c2de90e430b9e |
| Fast-Editor/Lynkr | b2fd256e75f43e344b6b576f0d04d60187002303 |
| pacifio/atlas | 7abe155908f66efc05851f9f0fb9d30f91fcfe8a |
| melgarafael/DeskcommCRM | 38d1d2bb0073b37f035268d78e869df7c6091f57 |

