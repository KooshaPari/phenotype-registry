# Cargo Workspace Health - 2026-04-27

Local-only audit of the requested cargo workspaces under `/Users/kooshapari/CodeProjects/Phenotype/repos`.

Commands:

```bash
timeout 90 cargo metadata --no-deps 2>&1 | jq -r '.packages[] | .name' 2>/dev/null | wc -l
timeout 60 cargo check --workspace --quiet 2>&1 | grep -c "^error"
```

Note: Cargo 1.95 emits a metadata format warning unless `--format-version 1` is supplied, so member counts below use `cargo metadata --quiet --no-deps --format-version 1` to preserve JSON parsing. `cargo check` uses the requested 60 second timeout.

| Repo | Member Count | Error Count | Check Result |
| --- | ---: | ---: | --- |
| FocalPoint | 61 | 25 | failed |
| hwLedger | 37 | 4 | failed |
| PhenoObservability | 12 | 2 | failed |
| AgilePlus | 43 | 1 | failed |
| PhenoPlugins | 0 | 1 | failed; metadata cannot load missing workspace member |
| BytePort | 1 | 0 | clean |
| helios-cli | 1 | 0 | clean |
| PhenoMCP | 4 | 0 | timed out after 60s |

