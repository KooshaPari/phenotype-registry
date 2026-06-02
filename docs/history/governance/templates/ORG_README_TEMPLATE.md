## Org README template (Kimi-generated 2026-04-27, nvidia/moonshotai/kimi-k2.5)

>>> dispatch-worker tier=nvidia/moonshotai/kimi-k2.5 model=nvidia/moonshotai/kimi-k2.5 endpoint=http://localhost:20128/v1
>>> routed to backend: moonshotai/kimi-k2.5
 ```markdown
# {{REPO_NAME}}

{{One-line description of what this crate does.}}

[![CI](https://github.com/Phenotype-org/{{REPO_NAME}}/actions/workflows/ci.yml/badge.svg)](https://github.com/Phenotype-org/{{REPO_NAME}}/actions)
[![cargo-deny](https://github.com/Phenotype-org/{{REPO_NAME}}/actions/workflows/cargo-deny.yml/badge.svg)](https://github.com/Phenotype-org/{{REPO_NAME}}/actions)
[![CodeQL](https://github.com/Phenotype-org/{{REPO_NAME}}/actions/workflows/codeql.yml/badge.svg)](https://github.com/Phenotype-org/{{REPO_NAME}}/actions)
[![License](https://img.shields.io/github/license/Phenotype-org/{{REPO_NAME}})](LICENSE)

## Quick Start

```bash
cargo install --path .
cargo run
```

## Architecture

Brief overview of how this crate fits into the Phenotype ecosystem.
Describes core abstractions, domain boundaries, and internal invariants.
Lists key dependencies and integration points with sibling crates.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the terms in [LICENSE](LICENSE).
```
