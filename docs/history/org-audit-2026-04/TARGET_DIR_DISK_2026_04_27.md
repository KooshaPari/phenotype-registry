# Target Directory Disk Audit - 2026-04-27

Scope: `/Users/kooshapari/CodeProjects/Phenotype/repos`, `find -maxdepth 3 -type d -name target`, excluding `*/.archive/*`.

Commands:

```bash
find /Users/kooshapari/CodeProjects/Phenotype/repos -maxdepth 3 -type d -name target -not -path "*/\.archive/*" 2>/dev/null > /tmp/target_dirs.txt
while IFS= read -r d; do du -sh "$d" 2>/dev/null | head -1; done < /tmp/target_dirs.txt
du -sh -c $(cat /tmp/target_dirs.txt | head -50) 2>/dev/null | tail -1
df -h / 2>&1 | head -3
```

Summary:

- Target directories found: 50
- Total target size: 38G
- Root disk: 84Gi available, 22% capacity used
- Audit mode only; no `target/` directories were removed.

| Repo | target_size |
|---|---:|
| `AgilePlus-wtrees/security-alerts-20260426/target` | 7.9G |
| `AgilePlus-wtrees/fmt-sweep/target` | 5.2G |
| `AgilePlus-wtrees/cve-cross-bump/target` | 4.9G |
| `eyetracker/target` | 1.6G |
| `phenotype-tooling-wtrees/codex-pr12-followup/target` | 1.4G |
| `FocalPoint/target` | 1.3G |
| `Tokn/target` | 1.1G |
| `AgilePlus-wtrees/cve-sweep-residual/target` | 963M |
| `helios-cli/codex-rs/target` | 925M |
| `PhenoObservability/target` | 826M |
| `heliosCLI/target` | 781M |
| `PhenoObservability-wtrees/cargo-deny-private-deps/target` | 762M |
| `bare-cua/target` | 746M |
| `BytePort/target` | 687M |
| `HeliosLab/target` | 643M |
| `PhenoProc/target` | 626M |
| `phenotype-journeys/target` | 615M |
| `phenotype-bus/target` | 611M |
| `PhenoSchema/pheno-xdd-lib/target` | 552M |
| `PhenoProc-wtrees/phenoproc-parent-metadata-pins-20260426/target` | 505M |
| `Tracely/target` | 484M |
| `worktrees/flowra/target` | 482M |
| `phenoData/target` | 482M |
| `PhenoProc-wtrees/main-clean-20260426/target` | 471M |
| `PhenoMCP/target` | 418M |
| `Sidekick/target` | 348M |
| `PhenoAgent/phenotype-daemon/target` | 327M |
| `Metron/target` | 294M |
| `phenoShared/target` | 275M |
| `Tasken/target` | 253M |
| `Configra/target` | 221M |
| `PhenoLang-wtrees/cve-residual/target` | 220M |
| `phenotype-shared/target` | 170M |
| `phenotype-infra/iac/target` | 153M |
| `thegent-jsonl/target` | 144M |
| `PhenoProc/worktree-manager/target` | 125M |
| `HexaKit/target` | 111M |
| `rich-cli-kit/target` | 92M |
| `Civis/target` | 88M |
| `Eidolon/target` | 74M |
| `PhenoContracts/rust/target` | 55M |
| `PhenoProc-wtrees/phenoproc-manifest-registry/target` | 52M |
| `PhenoVCS/target` | 36M |
| `tooling/worklog-aggregator/target` | 34M |
| `helios-cli/target` | 2.4M |
| `PhenoRuntime/target` | 1.9M |
| `.worktrees/Apisync-docs/target` | 0B |
| `.worktrees/agileplus-plugin-sqlite-docs/target` | 0B |
| `.worktrees/agileplus-plugin-git-docs/target` | 0B |
| `.worktrees/agileplus-plugin-core-docs/target` | 0B |
