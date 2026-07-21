# Disk Usage Deep Audit - 2026-04-27

Scope: local-only audit of direct child repository `target/`, `node_modules/`, and `.git/`
directories under `/Users/kooshapari/CodeProjects/Phenotype/repos`, plus matching `/tmp`
Claude/temp leftovers. No prune actions were performed.

## Filesystem Snapshot

```text
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   926Gi    23Gi    84Gi    22%    447k  885M    0%   /
```

## Top target/ dirs

```text
1.6G  /Users/kooshapari/CodeProjects/Phenotype/repos/eyetracker/target
1.3G  /Users/kooshapari/CodeProjects/Phenotype/repos/FocalPoint/target
1.1G  /Users/kooshapari/CodeProjects/Phenotype/repos/Tokn/target
815M  /Users/kooshapari/CodeProjects/Phenotype/repos/PhenoObservability/target
781M  /Users/kooshapari/CodeProjects/Phenotype/repos/heliosCLI/target
746M  /Users/kooshapari/CodeProjects/Phenotype/repos/bare-cua/target
687M  /Users/kooshapari/CodeProjects/Phenotype/repos/BytePort/target
643M  /Users/kooshapari/CodeProjects/Phenotype/repos/HeliosLab/target
626M  /Users/kooshapari/CodeProjects/Phenotype/repos/PhenoProc/target
615M  /Users/kooshapari/CodeProjects/Phenotype/repos/phenotype-journeys/target
```

Measured direct-child `target/` total: about 12.7G.

## Top node_modules/ dirs

```text
2.5G  /Users/kooshapari/CodeProjects/Phenotype/repos/cloud/node_modules
876M  /Users/kooshapari/CodeProjects/Phenotype/repos/heliosApp/node_modules
768M  /Users/kooshapari/CodeProjects/Phenotype/repos/AtomsBot/node_modules
595M  /Users/kooshapari/CodeProjects/Phenotype/repos/AppGen/node_modules
343M  /Users/kooshapari/CodeProjects/Phenotype/repos/phenotype-previews-smoketest/node_modules
255M  /Users/kooshapari/CodeProjects/Phenotype/repos/chatta/node_modules
229M  /Users/kooshapari/CodeProjects/Phenotype/repos/agileplus-landing/node_modules
140M  /Users/kooshapari/CodeProjects/Phenotype/repos/heliosCLI/node_modules
139M  /Users/kooshapari/CodeProjects/Phenotype/repos/phenodocs/node_modules
98M   /Users/kooshapari/CodeProjects/Phenotype/repos/PhenoHandbook/node_modules
```

Measured direct-child `node_modules/` total: about 6.2G.

## Top .git/ dirs (likely pack-corruption suspects)

```text
2.6G  /Users/kooshapari/CodeProjects/Phenotype/repos/FocalPoint/.git
1.9G  /Users/kooshapari/CodeProjects/Phenotype/repos/PhenoKits/.git
1.0G  /Users/kooshapari/CodeProjects/Phenotype/repos/thegent/.git
870M  /Users/kooshapari/CodeProjects/Phenotype/repos/vibeproxy/.git
817M  /Users/kooshapari/CodeProjects/Phenotype/repos/hwLedger/.git
655M  /Users/kooshapari/CodeProjects/Phenotype/repos/kwality/.git
522M  /Users/kooshapari/CodeProjects/Phenotype/repos/Dino/.git
306M  /Users/kooshapari/CodeProjects/Phenotype/repos/PhenoProc/.git
303M  /Users/kooshapari/CodeProjects/Phenotype/repos/helios-cli/.git
301M  /Users/kooshapari/CodeProjects/Phenotype/repos/cliproxyapi-plusplus/.git
```

These are not direct deletion candidates. Treat the largest `.git/` directories as suspects for
local object bloat, stale refs, or pack issues; verify each with local git diagnostics before any
cleanup.

## /tmp leftovers

```text
60M  /tmp/claude-501
```

Measured matching `/tmp/claude*` and `/tmp/tmp.*` total: about 0.1G.

## Recommended prune actions (don't prune, just recommend)

- Highest-confidence reclaim path: remove or rebuild direct `target/` directories after confirming
  no active build is using them. Top-10 `target/` entries account for about 8.5G; all measured
  direct `target/` directories account for about 12.7G.
- Second-highest reclaim path: remove direct `node_modules/` directories for repos not under active
  development, then reinstall from lockfiles as needed. Top-10 `node_modules/` entries account for
  about 5.9G; all measured direct `node_modules/` directories account for about 6.2G.
- For `.git/` bloat, do not delete directories. Run local-only checks such as
  `git count-objects -vH`, `git fsck`, and `git gc --prune=now` per repo only after confirming the
  checkout is clean and no other agent is operating there.
- `/tmp` leftovers are minor in this sample. `/tmp/claude-501` is only 60M, so it is not material to
  the dispatch budget.

Estimated reclaimable cache/build footprint from direct `target/`, direct `node_modules/`, and the
matched `/tmp` leftovers is about 19.0G. Additional space may be recoverable from `.git/` object
maintenance, but that requires per-repo validation and should not be counted as guaranteed reclaim.
