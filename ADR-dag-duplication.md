# ADR: DAG Crate Duplication

## Status

Accepted

## Context

`pheno-dag` (phenotype-registry) was extracted from `byteport-dag` (BytePort) during the foundation automation effort. The 4 core source files (`dag.rs`, `topo.rs`, `schema.rs`, `serialize.rs`) are byte-for-byte identical. The only difference is `Cargo.toml` (byteport-dag has extra deps: tokio, rayon, futures, sha2, tempfile, uuid).

## Decision

Maintain both crates as separate copies for now, with a CI dedup check (`dedup-check.yml`) that flags divergence.

### Why not publish a shared crate?

- Publishing to crates.io adds a release process for what's internal infrastructure
- Cross-repo git dependencies create fragile coupling between repos
- The codebase is small (~1,000 lines) and changes infrequently

### When to consolidate

- If either crate adds domain-specific logic that should be shared
- If the codebase grows beyond ~2,000 lines
- If a monorepo migration is undertaken

## Consequences

- Divergence is detected by CI (dedup-check.yml)
- Both repos must be updated manually when the DAG schema changes
- The `pheno-dag` Cargo.toml intentionally has fewer deps (no tokio/rayon) for lighter builds
