# Archived Repo Orphan Commit Audit - 2026-04-27

Scope: `AtomsBot`, `chatta`, `KaskMan`, `KlipDot`, `kmobile`, `KVirtualStage`.

Method:

- Remote archive metadata: `gh repo view KooshaPari/<repo> --json archivedAt,defaultBranchRef,pushedAt,isArchived`.
- Remote latest default-branch commits: `gh api repos/KooshaPari/<repo>/commits --jq '.[0:3] | .[] | {sha:.sha[0:7], date:.commit.author.date, msg:.commit.message[0:60]}'`.
- Orphan rule: a commit is an orphan when its author date is after the repository `archivedAt` timestamp.
- Follow-up local check: where a local checkout exists, `git log --all` was compared to `archivedAt` to catch unpublished governance commits that the archived GitHub remote did not accept.

## Summary

| Repo | archivedAt | pushedAt | Default branch | Remote latest-3 orphan flag | Local post-archive orphan count | Notes |
| --- | --- | --- | --- | --- | ---: | --- |
| AtomsBot | 2026-04-03T05:35:06Z | 2026-03-05T06:15:29Z | main | No | 11 | Local checkout has post-archive governance commits; remote default branch has none. |
| chatta | 2026-04-01T08:09:09Z | 2026-03-27T12:12:07Z | main | No | 18 | Local checkout has post-archive governance commits; remote default branch has none. |
| KaskMan | 2026-04-01T02:10:05Z | 2026-03-31T02:15:40Z | main | No | N/A | No local checkout under `repos/`. |
| KlipDot | 2026-04-26T00:13:18Z | 2026-04-05T13:04:45Z | main | No | 1 | Local commit `3d477cd` is after archive time; remote default branch has none. |
| kmobile | 2026-03-29T04:48:39Z | 2025-07-10T01:50:14Z | main | No | 13 | Local checkout has post-archive governance commits; remote default branch has none. |
| KVirtualStage | 2026-04-05T13:29:23Z | 2025-07-13T00:06:15Z | main | No | N/A | No local checkout under `repos/`. |

## Remote Latest Default-Branch Commits

### AtomsBot

| SHA | Date | Message prefix | Orphan |
| --- | --- | --- | --- |
| f9ad96c | 2025-09-09T07:11:41Z | new | No |
| 420be74 | 2025-09-07T06:18:46Z | rm redis nat sstabilize | No |
| b8e04a1 | 2025-09-04T23:51:24Z | tmp | No |

### chatta

| SHA | Date | Message prefix | Orphan |
| --- | --- | --- | --- |
| b02a42c | 2026-03-27T12:12:02Z | docs: add VitePress docsite (#8) | No |
| fc0d1a7 | 2026-03-27T11:10:17Z | docs: add real spec docs (PRD, FR, ADR, CLAUDE.md) (#7) | No |
| a742382 | 2026-03-27T10:58:04Z | docs: add CLAUDE.md agent instructions (#6) | No |

### KaskMan

| SHA | Date | Message prefix | Orphan |
| --- | --- | --- | --- |
| 72ae463 | 2026-03-31T02:15:39Z | chore(deps-dev): bump @typescript-eslint/eslint-plugin (#79) | No |
| 2e1d396 | 2026-03-31T02:09:46Z | ci(deps): bump codecov/codecov-action from 3 to 6 (#77) | No |
| 03a79cf | 2026-03-31T02:09:43Z | chore(deps-dev): bump typescript from 5.9.3 to 6.0.2 (#78) | No |

### KlipDot

| SHA | Date | Message prefix | Orphan |
| --- | --- | --- | --- |
| a0b1b2d | 2026-04-05T13:04:44Z | docs: mark as Legacy Archived AI-DD project - STRICTLY DO NO | No |
| 0522365 | 2026-04-05T06:21:41Z | chore: add AgilePlus scaffolding | No |
| 9914758 | 2026-04-04T10:47:19Z | ci(legacy-enforcement): add legacy tooling anti-pattern gate | No |

### kmobile

| SHA | Date | Message prefix | Orphan |
| --- | --- | --- | --- |
| c6f0f0c | 2025-07-10T01:50:11Z | Fix | No |
| 20e8738 | 2025-07-09T03:23:14Z | Fix release permissions: add contents write access | No |
| f835f32 | 2025-07-09T03:16:42Z | Enable CI workflow trigger on tag pushes | No |

### KVirtualStage

| SHA | Date | Message prefix | Orphan |
| --- | --- | --- | --- |
| 050a603 | 2025-07-13T00:05:47Z | Initial KVirtualStage Implementation | No |
| 68aaa3b | 2025-07-11T18:29:10Z | ENTERPRISE PRODUCTION READINESS: MISSION ACCOMPLISHED | No |
| 93ddcc8 | 2025-07-11T18:02:12Z | Add Comprehensive KVirtualStage Evolution Plan | No |

## Local Post-Archive Orphan Evidence

These are local refs only where the checkout exists under `/Users/kooshapari/CodeProjects/Phenotype/repos`. They are not visible in the GitHub latest default-branch commit API results above.

| Repo | Count | Representative SHAs |
| --- | ---: | --- |
| AtomsBot | 11 | `a71649d`, `7cf1968`, `1b31b41`, `82a61f1`, `4d06afa`, `5f6fa0e`, `b402176`, `dff0fd5`, `53bdc07`, `6fa0b9d`, `9c9777c` |
| chatta | 18 | `d974fb8`, `2b37044`, `1489868`, `914c9dc`, `0630351`, `8d77b8d`, `9e05bc5`, `6d5a996`, `b3d5530`, `9a04827`, `1b1c52d`, `51f64aa`, `7138446`, `7bf2381`, `32b9557`, `b57fea8`, `28e2e73`, `ba099b3` |
| KaskMan | N/A | Local checkout missing. |
| KlipDot | 1 | `3d477cd` |
| kmobile | 13 | `ad56b63`, `c7c6d66`, `77b900e`, `58d3c83`, `29c552c`, `f4e952d`, `38b41a5`, `b2f5c5b`, `f84ea79`, `08b64e4`, `20fa9fd`, `ba49cd8`, `c7c9f9d` |
| KVirtualStage | N/A | Local checkout missing. |

## Conclusion

The required GitHub API scan found no remote default-branch commits after `archivedAt` for the six archived repositories. The orphan-governance pattern is present in local archived checkouts for `AtomsBot`, `chatta`, `KlipDot`, and `kmobile`; those commits should remain unpushed while the repositories stay archived/read-only.
