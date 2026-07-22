# Known Issues

| Issue | Impact | Mitigation |
|---|---|---|
| Seven remote repositories have no refs | Cloud capture may be incomplete | Search local clones/worktrees before archive |
| AgilePlus canonical checkout contains runtime/build dirt | Unsafe integration surface | Use isolated worktrees only |
| OMLX `tmp/main` is not represented | One history line remains at risk | Import missing ref before archive proposal |
| `omniroute-rust` has 13 crates | Parent cannot be chosen per repository name | Run crate-level boundary audit |
| `thegent-sharecli` dedupe is incomplete | Possible unique behavior | Compare with `thegent-cli-share` and `sharecli` |
| phenoVessel head is not reachable in PhenoPlugins | Absorption claim is unproven | Preserve tag/release and prove parity |
