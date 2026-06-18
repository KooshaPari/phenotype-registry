# Propagation Report — 2026-06-18

**Source:** `phenotype-registry/chore/l7-001-curation-snapshot` (commit `a1aa44660`)
**Script:** `scripts/propagate-intent-to-repos.py`
**Result:** **95 repos propagated** with `docs/intent/<repo>.md` and `docs/boundary/<repo>.md`

## Skipped (13 — file already existed, kept local version)

These repos already had intent/boundary files in place from a prior run; left untouched. To overwrite, re-run with `--force`.

```
```

## Skipped (23 — repo not on disk)

These repos appear in `_bindings.json` (have curated prompts) but the directory does not exist on this Mac. They are archived, worktree-only, or worktree-of-another-repo. Prompts are still preserved in the registry's `docs/curated-prompts/_orphan/` bucket.

| Repo | Likely reason |
|---|---|
| Authvault | archived per ADR-007 |
| PhenoMCP-cheap | deprecated per ADR-006 |
| PhenotypeMCP | renamed to PhenoMCP |
| Stashly | archived per ADR-017 |
| bifrost | archived |
| helios-cli | lowercase variant; canonical is `HeliosCLI` |
| odin-landing | archived landing page |
| pheno-contracts | lowercase variant; canonical is `PhenoContracts` |
| phenoAgents | lowercase variant; canonical is `PhenoAgent` |
| phenoConfig | lowercase variant; canonical is `pheno-config` |
| phenoErrors | lowercase variant; canonical is `pheno-errors` |
| phenoPortAdapter | lowercase variant; canonical is `pheno-port-adapter` |
| phenoResearch | lowercase variant; canonical is `phenoResearchEngine` |
| phenoRouterMonitor | archived |
| phenoTracing | lowercase variant; canonical is `pheno-otel` |
| phenoVibeproxy | lowercase variant; canonical is `vibeproxy` |
| phenoWtrees | worktree container; not a buildable repo |
| phenotype-observability | renamed to PhenoObservability |
| phenotype-org | archived org tooling |
| phenotype-resilience | renamed to ResilienceKit |
| phenotype-vessel | deprecated per ADR-019 |
| phenotype-wtrees | worktree container; not a buildable repo |
| thegent-landing | archived landing page |

## Skipped (1 — source repo)

`phenotype-registry` itself — propagated content lives at the registry's own `docs/intent/` and `docs/boundary/`.

## How to re-propagate

```bash
cd /Users/kooshapari/CodeProjects/Phenotype/repos/phenotype-registry
python3 scripts/propagate-intent-to-repos.py            # normal
python3 scripts/propagate-intent-to-repos.py --dry-run  # preview
python3 scripts/propagate-intent-to-repos.py --force    # overwrite existing
python3 scripts/propagate-intent-to-repos.py --repo AgilePlus   # one repo
```

## How propagated files are marked

Each propagated file starts with this banner:

```html
<!--
propagated-from: KooshaPari/phenotype-registry @ chore/l7-001-curation-snapshot
date: 2026-06-17
source-commit: a1aa44660
do-not-edit-locally: regenerate via scripts/propagate-intent-to-repos.py
                     or update in the source-of-truth registry repo
-->
```

This makes it unambiguous where the file came from and where to update it.