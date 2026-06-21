# Event substrate reconciliation: Eventra and phenoEvents

Date: 2026-06-21

## Executive decision

KEEP_BOTH.

- phenoEvents is the canonical reusable event-bus substrate.
- Eventra is not a duplicate event-bus repo; it owns CQRS/event-sourcing framework work and event contracts.
- Eventra must not be deleted as part of the phenotype-bus drain without a separate deletion-justification package.

## Evidence

### phenoEvents

Observed target files:

- phenoEvents/README.md
- phenoEvents/src/bus/mod.rs
- phenoEvents/src/bus/in_memory.rs
- phenoEvents/src/core/envelope.rs
- phenoEvents/src/projection/mod.rs
- phenoEvents/src/schema/registry.rs
- phenoEvents/docs/security/THREAT_MODEL.md

Observed responsibility:

- EventEnvelope-shaped event bus.
- SqliteBus with outbox, retry, DLQ, idempotency, and delivery bookkeeping.
- InMemoryBus for non-persistent in-process fanout.
- Schema registry and SQL read-model projections.
- Observability around event flow.

### Eventra

Observed source files:

- Eventra/README.md
- Eventra/SPEC.md
- Eventra/src/domain/event.rs
- Eventra/src/application/event_bus.rs
- Eventra/src/application/projection.rs
- Eventra/rust/phenotype-event-contracts/src/*
- Eventra/rust/phenotype-event-bus/src/*
- Eventra/rust/phenotype-event-sourcing/src/*
- Eventra/docs/disposition/p4-contracts-slice3-event-bus.md

Observed responsibility:

- Event-driven architecture framework.
- CQRS and Event Sourcing.
- EventStore and ProjectionRunner support.
- Trait-only event/bus contracts extracted from phenoShared and HexaKit.
- Publish-only, pub/sub, store, envelope, metadata, and error contract surfaces.

## Boundary matrix

| Responsibility | Canonical owner | Status | Rationale |
|---|---|---|---|
| Runtime event bus substrate | phenoEvents | KEEP | Owns SqliteBus, InMemoryBus, EventEnvelope, outbox, retry, DLQ, schema registry, projections. |
| CQRS/event-sourcing framework | Eventra | KEEP | README/SPEC describe CQRS, event sourcing, EventStore, ProjectionRunner, aggregate/command model. |
| Trait-only event contracts | Eventra | KEEP | docs/disposition/p4-contracts-slice3-event-bus.md names Eventra as terminal owner for event/bus traits. |
| Deleted phenotype-bus source history | phenotype-registry | DONE | Preserved in docs/absorption/phenotype-bus/ via PR #336. |
| Future bus implementation work | phenoEvents first, Eventra contracts only if trait surface changes | SPLIT | Avoid duplicating runtime adapters in Eventra unless explicitly part of CQRS/event-sourcing framework. |

## Local work preservation

Eventra had local propagated boundary/intent docs on 2026-06-21. They were preserved to:

- KooshaPari/Eventra:wip/2026-06-21-eventra-boundary-preserve
- commit 77508ac docs: preserve Eventra boundary taxonomy refresh

## Required follow-up

- Keep phenoEvents and Eventra.
- Do not delete either repo from the phenotype-bus deletion decision.
- If future absorption is proposed, require a full deletion-justification matrix for that specific repo.
- Normalize naming in registry references to phenoEvents for the repository and pheno-events for the Rust crate package name.
