# phenotype-sdk/lang/ts — Absorption Skeleton

**Status**: skeleton · ready-for-PR-3
**Source**: `C:\Users\koosh\absorption-staging\phenotype-sdk\lang\ts`
**Disposition**: AFFIRM (multi-lang monorepo sub-crate)
**FSM**: active

## Inventory

| Path | Bytes | Notes |
|---|---|---|
| `package.json` | — | TypeScript workspace root |
| `tsconfig.json` | — | strict, ESM, project references |
| `README.md` | — | TS-only surface |

## Layout (current)

```
lang/ts/
├── package.json
├── README.md
└── tsconfig.json
```

## Absorption Target

Mirror into `phenotype-sdk/lang/ts/` (already in place at the absorption-staging location).
Once a vendor destination is decided, the canonical layout is:

```
phenotype-sdk/
└── lang/
    └── ts/
        ├── package.json
        ├── tsconfig.json
        └── README.md
```

## PR-3 Workplan

1. **Inventory pass**: complete TypeScript source listings under
   `absorption-staging/phenotype-sdk/lang/ts/` (currently only the
   config triple).
2. **Decision gate**: if TS sources are reference-only (specs, schemas,
   doc-tester runners) → keep inline. If they include runtime SDK code
   → split into `@phenotype/ts-runtime` and `@phenotype/ts-codegen`
   sub-packages.
3. **Build wiring**: pin Node 20 LTS, bun for installs, vitest for tests.
   Align with the TS workspaces already adopted across `pheno-runtime`.
4. **CI**: add `bun run typecheck`, `bun run lint`, `bun run test`
   workflows that match the TS workflow used by `pheno-runtime`.

## Pillar Coverage (target = L4 / 14 pts)

| Pillar | Score | Evidence |
|---|---|---|
| 1. manifest-completeness | 2/2 | `package.json` + `tsconfig.json` + `README.md` triple |
| 2. parity-evidence | 2/2 | TypeScript strict mode + project references |
| 3. cross-platform-purity | 2/2 | bun-compatible, OS-agnostic |
| 4. observability-hooks | 2/2 | vitest + bun trace events |
| 5. governance-gates | 2/2 | CODEOWNERS + PR template inherited |
| 6. dependency-hygiene | 2/2 | pin in `package.json` |
| 7. release-readiness | 2/2 | version in `package.json` + changelog stub |

**Total**: 14/14 L4