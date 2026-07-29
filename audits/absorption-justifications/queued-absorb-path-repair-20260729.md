# queued-absorb-path-repair-20260729

## Scope
16 queued+ABSORB records in `projects/*.json`.

## Change
Normalized `path` fields by removing stale `repos/` prefix.

## Records updated
- AgilePlus → `AgilePlus`
- Compound-Spheres-3D-Backup → `Compound-Spheres-3D-Backup`
- Dino → `Dino`
- HexaKit → `HexaKit`
- PhenoMCPServers → `PhenoMCPServers`
- PhenoRuntime → `PhenoRuntime`
- PlusForges → `PlusForges`
- Tasken → `Tasken`
- UnityDoorstop-NexusPatched → `UnityDoorstop-NexusPatched`
- WorldSphereMod → `WorldSphereMod`
- pheno-mcp-router → `pheno-mcp-router`
- phenotype-go-kit → `phenotype-go-kit`
- phenotype-infrakit → `phenotype-infrakit`
- phenotypeActions → `phenotypeActions`
- tehgent → `tehgent`
- thegent-sharecli → `thegent-sharecli`

## Rationale
These path prefixes did not resolve against the expected repo-root relative path and were purely a normalization artifact. No disposition/status/category changes made.
