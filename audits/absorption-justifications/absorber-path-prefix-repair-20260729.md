# absorber-path-prefix-repair-20260729

## Scope
All `projects/*.json` records with `disposition == "ABSORB"` where `path` started with `repos/` and was normalized.

## Change
Removed the stale leading `repos/` segment from `path`.

## Files touched
- AgilePlus.json
- Apisync.json
- Compound-Spheres-3D-Backup.json
- Conft.json
- Dino.json
- FocalPoint.json
- HeliosLab.json
- HexaKit.json
- KWatch.json
- KodeVibe.json
- PhenoHandbook.json
- PhenoLang.json
- PhenoMCPServers.json
- PhenoRuntime.json
- Pine.json
- PlayCua.json
- PlusForges.json
- PolicyStack.json
- Tasken.json
- UnityDoorstop-NexusPatched.json
- WorldSphereMod.json
- agent-user-status.json
- agileplus-spec-harmonizer.json
- clap-ext.json
- context-mode-plusplus.json
- grapheon-bindings.json
- heliosBench.json
- omniroute-rs.json
- phench.json
- pheno-cdylib-bridge.json
- pheno-forge-smoke.json
- pheno-mcp-router.json
- pheno-otel.json
- phenodag.json
- phenotype-gfx.json
- phenotype-go-kit.json
- phenotype-hub.json
- phenotype-infrakit.json
- phenotype-pm-core.json
- phenotypeActions.json
- tehgent.json
- template-commons.json
- thegent-sharecli.json

## Notes
Only metadata normalization was applied. No status/disposition changes, merges, archival actions, or deletions.
