# cliff.toml (git-cliff) Rollout — 2026-04-27

## Status
**18 PRs merged** adding cliff.toml automated CHANGELOG generation.

## Merged
phenoAI #23, phenoData #25, PhenoKits #68, PhenoVCS #37, Tracely #18, PlayCua #49, Civis #268, Eidolon #19, eyetracker #23, GDK #37, Metron #26, rich-cli-kit #15, phenotype-bus #13, phenotype-journeys #21, phenotype-tooling #31, phenoUtils #19, PhenoProc #30, PhenoRuntime #35

## Template
- Conventional Commits parser (feat/fix/perf/refactor/docs/chore/ci/test/security)
- Keep-a-Changelog format header
- Group commits: Added/Fixed/Performance/Changed/Documentation/Dependencies/Maintenance/CI/Testing/Security
- Tag pattern: `v[0-9]*` (semver releases only)

## Usage
After merge to main with conventional commits:
```bash
git cliff -o CHANGELOG.md          # full history
git cliff --tag v0.2.0 -o CHANGELOG.md  # specific release
git cliff --unreleased -o UNRELEASED.md # pending
```

## Cross-references
- Memory: `reference_versioning_strategy.md` — CalVer (thegent) + SemVer hybrid
