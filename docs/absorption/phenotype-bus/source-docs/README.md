# phenotype-bus

> ⚠️ **DEPRECATED 2026-06-18** — This crate has been absorbed into
> [PhenoEvents](https://github.com/KooshaPari/phenoEvents) (PR #9). The
> in-memory bus pattern is now available at
> `pheno_events::bus::InMemoryBus`. This repo will be archived on
> 2026-06-25 (read-only marker applied; deletion follows after 90-day
> GitHub retention).

## Migration

Replace the `phenotype-bus` dependency with `pheno-events` and update
imports. The Wave-2 API is the canonical surface going forward.

```toml
# Cargo.toml — before
phenotype-bus = "0.1"
```

```toml
# Cargo.toml — after
pheno-events = "0.1"
```

```rust,ignore
// before
use phenotype_bus::{Event, EventBus, InMemoryBus};

// after
use pheno_events::bus::{Event, EventBus, InMemoryBus};
```

## What was here

`phenotype-bus` was a typed async pub/sub bus for cross-collection
communication in the Phenotype org. The crate carried two API
revisions:

- **Wave-1** (`Bus`, `Event`, `BusError`, broadcast-channel based) —
  superseded by Wave-2, removed in this cleanup.
- **Wave-2** (`events::InMemoryBus`, `events::Event`, topic routing,
  retry, idempotent handlers) — lifted to PhenoEvents.

The crate is now a thin shim around `pheno_events::bus` and is kept
temporarily for downstream consumers that haven't migrated yet. New
code should depend on `pheno-events` directly.

## Status

| Field | Value |
|---|---|
| Deprecated | 2026-06-18 |
| `InMemoryBus` lifted to PhenoEvents | PR `KooshaPari/phenoEvents#9` |
| Source archive | 2026-06-25 (read-only) |
| Source delete | 2026-09-23 (90-day retention) |
| Replacement | [`pheno-events`](https://github.com/KooshaPari/phenoEvents) |

## License

Apache-2.0 — see [LICENSE](LICENSE).
