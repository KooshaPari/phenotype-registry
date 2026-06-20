# PhenoKits absorption matrix

Date: 2026-06-20
Source repo: `KooshaPari/PhenoKits`
Observed local branch: `feature/L1.4-governance-keystone-2026-06-12`
Remote state: archived/read-only; branch push blocked

## Executive decision

`ARCHIVE_ONLY`. Do not delete until TypeScript libs and template/governance surfaces are fully closed. Go and Python library absorption made concrete progress on 2026-06-20.

| Source Item | Source Evidence | Category | Source State | Target Repo | Target Evidence | Status | Deletion Justification | Risk if Deleted | Required Action |
|---|---|---|---|---|---|---|---|---|---|
| Local branch work | `feature/L1.4-governance-keystone-2026-06-12`; 8 generated patches | Branch-only work | branch-only | `phenotype-registry` | patchset previously pushed under registry absorption docs, commit `248931be` | `DONE` | Branch content is preserved outside archived source repo | low - patch replay still available | none |
| Go libs | `PhenoKits/libs/go/{pheno-core-cgo,phenotype-go-auth,phenotype-go-cli,phenotype-go-config,phenotype-go-kit,phenotype-go-middleware,phenotype-id}` | Go modules | implemented | `phenotype-go-sdk` | branch `chore/fold-phenokits-go-libs-2026-06-20`, commit `a3443fe`, copied with per-package `ORIGIN.md` | `DONE` | Go module content has a tight SDK home | low after PR merge | open/merge PR |
| Python libs except config kit | `PhenoKits/libs/python/{pheno-cli-builder,pheno-cli-kit,phenotype-id,phenotype-logging,phenotype-py-kit,phenotype-testing}` | Python packages | implemented | `phenotype-python-sdk` | `diff -qr` showed no source differences except cache dirs | `SUPERSEDED_PARITY` | Existing SDK packages are equivalent | low | none |
| Python config kit | `PhenoKits/libs/python/phenokit-config-kit` | Python package/scaffold config | implemented | `phenotype-python-sdk` | branch `chore/fold-phenokit-config-kit-2026-06-20`, commit `a611d7f`, copied with `ORIGIN.md` | `DONE` | Divergent config-kit artifacts are preserved in SDK | low after PR merge | open/merge PR |
| TypeScript libs | `PhenoKits/libs/typescript/{phenotype-core-ts,phenotype-id,plugin-typescript}` | TS packages | implemented | unresolved | `phenotype-ts-utils` does not exist under KooshaPari | `LAST_RESORT_EXCEPTION` | No real tight TS target exists yet | high - TS packages lost | create/choose TS target or preserve patchset before deletion |
| Templates | `templates/*` | Templates/generators | implemented | `phenokits-commons` | target cloned and has template dirs | `PARTIAL` | Broad structure exists, but parity not proven | medium | compare template dirs |
| Hexagon/governance docs | `hexagon/*`, `governance/*` | Governance/specs | docs-only | `phenokits-commons` / `phenotype-registry` | target has matching docs structure | `PARTIAL` | Likely preserved but not file-level closed | medium | diff and select canonical docs |

## Final recommendation

Keep `PhenoKits` archived. Deletion is still blocked by TypeScript libs and unproven template/governance parity, but Go and Python library surfaces are now substantially absorbed.
