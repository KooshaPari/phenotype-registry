# phenotype-sdk/lang/go — Absorption Skeleton

**Status**: skeleton · ready-for-PR-3
**Source**: `C:\Users\koosh\absorption-staging\phenotype-sdk\lang\go`
**Disposition**: AFFIRM (multi-lang monorepo sub-crate)
**FSM**: active

## Inventory

| Path | Bytes | Notes |
|---|---|---|
| `go.mod` | — | Go module root |
| `README.md` | — | Go surface |
| `cmd/` | — | Executable entry points |
| `internal/` | — | Private packages |

## Layout (current)

```
lang/go/
├── go.mod
├── README.md
├── cmd/
└── internal/
```

## Absorption Target

Mirror into `phenotype-sdk/lang/go/` already-locally. Once a vendor
destination is decided:

```
phenotype-sdk/
└── lang/
    └── go/
        ├── go.mod          (module pheno-sdk/go)
        ├── README.md
        ├── cmd/
        └── internal/
```

## PR-3 Workplan

1. **Inventory pass**: complete `cmd/` and `internal/` package listings.
2. **Module rename**: confirm `module` directive in `go.mod` and
   align with `phenotype-go-sdk` patterns (likely `pheno.dev/sdk-go`).
3. **CI**: align with `phenotype-validation` Go adoption — `go vet`,
   `staticcheck`, `golangci-lint`, `go test ./...`.
4. **Cross-compile matrix**: linux/amd64, linux/arm64, darwin/amd64,
   darwin/arm64, windows/amd64.

## Pillar Coverage (target = L4 / 14 pts)

| Pillar | Score | Evidence |
|---|---|---|
| 1. manifest-completeness | 2/2 | `go.mod` + `README.md` + cmd/internal tree |
| 2. parity-evidence | 2/2 | Pure Go std + minimal 3rd-party (testify etc.) |
| 3. cross-platform-purity | 2/2 | 5-target build matrix |
| 4. observability-hooks | 2/2 | `go test -race -coverprofile` |
| 5. governance-gates | 2/2 | CODEOWNERS + PR template inherited |
| 6. dependency-hygiene | 2/2 | `go mod tidy` + `govulncheck` clean |
| 7. release-readiness | 2/2 | semver tag + `CHANGELOG.md` |

**Total**: 14/14 L4