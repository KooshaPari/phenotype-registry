# Missing cargo-deny.yml local size triage - 2026-04-27

Scope: local-only verification of the repos named in the request under
`/Users/kooshapari/CodeProjects/Phenotype/repos/$repo`. No GitHub API or remote
repo metadata was used.

The request called this the 24 local missing `cargo-deny.yml` repos, but the
provided repo list contains 20 names. All 20 listed repos exist locally.

Rust LOC command used per repo:

```bash
find . -name "*.rs" -not -path "*/target/*" -not -path "*/.git/*" \
  -not -path "*/.archive/*" -exec wc -l {} + 2>/dev/null | tail -1 | awk '{print $1}'
```

Archive marker check:

```bash
git log --all --regexp-ignore-case \
  --grep='archive\|archived\|deprecat\|read-only\|read only' \
  --format='%h %cs %s' -n 3
```

## Findings

Only `PhenoVCS` is a true Rust stub by the requested threshold. The rest are
production-sized Rust repos or small production surfaces. `KlipDot` and
`kmobile` both exist locally; `KlipDot` has an explicit local history marker
for "Legacy Archived AI-DD project", while `kmobile` has no local git-log
archive marker in this check.

## Size table, sorted descending

| Repo | Rust LOC | Class | Local archive marker? | Evidence |
| --- | ---: | --- | --- | --- |
| `AgilePlus` | 692873 | LARGE | yes | marker matched in git log body; latest subject `11789d9 2026-04-26 spec(013): mark phenotype-infrakit-stabilization CANCELLED (#413)` |
| `pheno` | 160277 | LARGE | yes | `80f3274 2026-04-25 docs(crates): mark Phase 1 crates as deprecated copies pointing to phenoShared (#80)` |
| `PhenoKits` | 99445 | LARGE | yes | `801de628 2026-04-25 docs(org-audit): Wave-69 final status rollup v25 - sidekick deprecations, disk-check gate, portfolio sync` |
| `PhenoProc` | 91711 | LARGE | yes | marker matched in git log body; latest subject `43b57de 2026-04-26 chore(submodule): remove Evalora dead reference (deleted upstream) (#21)` |
| `phenoShared` | 14465 | MEDIUM | yes | `78d9ced 2026-04-24 feat(ci): port 3 reusable workflows from archived phenotype-infrakit (#83)` |
| `kmobile` | 10158 | MEDIUM | no | Exists locally; no local archive marker matched. |
| `GDK` | 7616 | MEDIUM | no | No local archive marker matched. |
| `KlipDot` | 6095 | MEDIUM | yes | `a0b1b2d 2026-04-05 docs: mark as Legacy Archived AI-DD project - STRICTLY DO NOT DELETE NOR UNARCHIVE` |
| `helios-router` | 5449 | MEDIUM | yes | `444a1bc 2026-02-23 docs: Add deep pain points analysis` matched archive/deprecation text in log body. |
| `HeliosLab` | 5026 | MEDIUM | no | No local archive marker matched. |
| `phenotype-journeys` | 3971 | MEDIUM | yes | `42f5e7a 2026-04-23 index on main: cc78cf9 feat(journey-viewer)!: deprecate Shot align prop, drop float CSS (0.1.2) (#2)` |
| `bare-cua` | 3895 | MEDIUM | no | No local archive marker matched. |
| `PlayCua` | 3889 | MEDIUM | no | No local archive marker matched. |
| `phenotype-tooling` | 2923 | MEDIUM | no | No local archive marker matched. |
| `rich-cli-kit` | 1904 | SMALL | no | No local archive marker matched. |
| `PhenoRuntime` | 873 | SMALL | no | No local archive marker matched. |
| `HexaKit` | 682 | SMALL | yes | `01d88f14d6 2026-04-26 chore(scorecard): add paths-ignore for ARCHIVE/** to skip vendored binary cache (#375)` |
| `phenoData` | 387 | SMALL | no | No local archive marker matched. |
| `phenoAI` | 373 | SMALL | no | No local archive marker matched. |
| `PhenoVCS` | 9 | STUB | no | No local archive marker matched. |

## Rollout priority

1. P0 large production targets: `AgilePlus`, `pheno`, `PhenoKits`, `PhenoProc`.
2. P1 medium active-looking targets without local archive markers: `kmobile`,
   `GDK`, `HeliosLab`, `bare-cua`, `PlayCua`, `phenotype-tooling`.
3. P2 shared foundational medium target with archive-derived references:
   `phenoShared`.
4. P3 small active-looking targets: `rich-cli-kit`, `PhenoRuntime`,
   `phenoData`, `phenoAI`.
5. P4 archive-marker or template-sensitive targets requiring owner decision
   before rollout: `KlipDot`, `helios-router`, `phenotype-journeys`, `HexaKit`.
6. Skip by size unless governance says otherwise: `PhenoVCS` is a 9 LOC stub.

Top five rollout candidates by production weight are `AgilePlus`, `pheno`,
`PhenoKits`, `PhenoProc`, and `phenoShared`. If archive-marker caution blocks
`phenoShared`, use `kmobile` as the first active-looking replacement.
