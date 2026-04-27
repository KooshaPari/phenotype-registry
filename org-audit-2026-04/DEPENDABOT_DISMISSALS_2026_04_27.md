# Dependabot Dismissals - 2026-04-27

Scope: non-archived KooshaPari GitHub repositories with local Rust content under
`/Users/kooshapari/CodeProjects/Phenotype/repos`.

Rule: dismiss only open Dependabot alerts whose advisory maps to a RUSTSEC ID
that is explicitly present in `[advisories].ignore` / `[[advisories.ignore]]`
in the repo's `deny.toml`.

RustSec advisory DB used:
`/Users/kooshapari/.cargo/advisory-dbs/advisory-db-3157b0e258782691`
at `930c3aa2323b1f94427f9abca7e939ec50e998b5`.

Repos scanned: 59

Repos with `deny.toml` RUSTSEC suppressions: 18

Eligible dismissals found: 1

Dismissal cap: 30

| Repo | AlertNum | GHSA | RUSTSEC | Result |
| --- | ---: | --- | --- | --- |
| heliosCLI | 30 | GHSA-pwjx-qhcg-rvj4 | RUSTSEC-2026-0049 | Dismissed as `tolerable_risk`; comment: `suppressed in deny.toml as RUSTSEC-2026-0049 (codex-rs/deny.toml)` |
