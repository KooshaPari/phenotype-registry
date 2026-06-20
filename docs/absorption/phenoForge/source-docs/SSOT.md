# SSOT — Single Source of Truth (phenotype-forge)

This document records the canonical authority for cross-cutting facts in the
phenotype-forge repository. When a fact conflicts across docs, the source listed
here wins.

## Scope

| Domain | Authoritative source |
| --- | --- |
| Build & test commands | `Justfile` / `Cargo.toml` |
| Release & versioning | `cliff.toml` + `CHANGELOG.md` (git-cliff generated) |
| Security disclosure process | `SECURITY.md` |
| Dependency updates | `.github/dependabot.yml` |
| Branch & commit policy | `AGENTS.md` |
| Editor / formatting baseline | `.editorconfig` |
| Agent operating model | `AGENTS.md` |
| License | `LICENSE-MIT` + `LICENSE-APACHE` |

## Precedence order

1. Executable config (`Cargo.toml`, `Justfile`, workflows) — observed behavior.
2. `*.md` governance files in this SSOT table.
3. `AGENTS.md` operating-loop rules.
4. Anything else.

## Updating this file

- Keep the table narrow and unambiguous.
- Cite the canonical file by path; do not duplicate content.
- Update via a `chore(governance):` commit referencing the change.
