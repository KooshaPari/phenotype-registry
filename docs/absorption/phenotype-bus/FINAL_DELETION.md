# phenotype-bus deletion-justification package

## EXECUTIVE_DECISION

DELETE_AFTER_REGISTRY_MERGE

Confidence: medium.

The source repo is archived/read-only and its README states it was absorbed into PhenoEvents via PR #9. Direct target inspection confirms PhenoEvents owns the event-bus boundary with a broader event substrate: EventEnvelope, InMemoryBus, SqliteBus, outbox, at-least-once delivery, retry/DLQ, idempotency, schema registry, projections, and observability. Source API parity is not exact, so source history and local ahead work are preserved in this registry package before deletion.

## SOURCE_INVENTORY

- Product intent: typed async pub/sub bus for cross-collection Phenotype communication.
- Source API: Event, EventBus, InMemoryBus, Ack, Subscription, Handler, IdempotentHandler, RetryPolicy, topic routing.
- Source modules: src/lib.rs, src/config.rs, src/events/bus.rs, src/events/subscription.rs, src/events/mod.rs, src/observability.rs.
- Tests: src/lib.rs unit tests plus tests/smoke.rs and tests/smoke_test.rs.
- Docs/governance: README.md, FUNCTIONAL_REQUIREMENTS.md, docs/boundary, docs/intent, integration docs, worklogs, CI, deny, release, scorecard, SLSA, security.
- Local branch work: ahead commits and archived-marker docs preserved as patches in patches/local-ahead.patch.
- Generated artifacts: target/ and build caches excluded from source snapshot.

## BRANCH_INVENTORY

- Local branch before preservation: chore/l7-105-phenotype-bus-pre-archive-cleanup-2026-06-18, ahead 3 over origin.
- Local preservation branch/commit: wip/2026-06-21-pre-delete-preserve at 594e109 docs: preserve phenotype-bus archived markers.
- Remote WIP from earlier work exists: origin/wip/2026-06-20-local-ahead-preserve at 88b571f.
- Push to source repo failed because GitHub reports the repository is archived/read-only.
- Required mitigation: preserve the full local-ahead patch in this registry package before deletion.

## TARGET_PARITY_SUMMARY

Primary target: KooshaPari/phenoEvents.

Target evidence observed locally:
- phenoEvents/README.md describes Rust event-bus library with SQLite outbox, at-least-once delivery, idempotency, DLQ, schema registry, and SQL read-model projections.
- phenoEvents/src/lib.rs documents two bus implementations: bus::SqliteBus and bus::InMemoryBus.
- phenoEvents/src/bus/mod.rs defines Bus, Handler, Ack, PublishError, SubscribeError, Subscription, and SqliteBus.
- phenoEvents/src/bus/in_memory.rs states it was lifted from phenotype-bus/src/events/bus.rs and adapted to the EventEnvelope contract.
- phenoEvents/src/bus/in_memory.rs implements InMemoryBus with per-subscriber queues, fanout, duplicate detection, and subscriber cleanup.
- phenoEvents contains adjacent substrate modules for core envelopes, observability, projections, and schema registry.

## ABSORPTION_MATRIX

| Source Item | Source Evidence | Category | Source State | Target Repo | Target Evidence | Status | Deletion Justification | Risk if Deleted | Required Action |
|-------------|-----------------|----------|--------------|-------------|-----------------|--------|------------------------|-----------------|-----------------|
| Typed async pub/sub product intent | phenotype-bus/README.md, FUNCTIONAL_REQUIREMENTS.md | Product intent | deprecated/docs + implemented | phenoEvents | phenoEvents/README.md, src/lib.rs | SUPERSEDED_BETTER | Target expands bus into durable event substrate with outbox, DLQ, schema registry, projections, and observability. | low: duplicate repo intent | none |
| In-memory bus pattern | phenotype-bus/src/events/bus.rs | Public API/module | implemented | phenoEvents | phenoEvents/src/bus/in_memory.rs | SUPERSEDED_BETTER | Target source explicitly says it was lifted from phenotype-bus and adapted to EventEnvelope. | low: source duplicate after preservation | none |
| EventBus trait and handler model | phenotype-bus/src/events/bus.rs | Protocol/API claim | implemented | phenoEvents | phenoEvents/src/bus/mod.rs Bus, Handler, Subscription | PARTIAL | Target model is not exact API parity; it replaces dyn Event with EventEnvelope and Bus/Handler. Source snapshot preserves API history. | medium: direct API compatibility lost | archive |
| Topic routing and wildcard subscribers | phenotype-bus/src/events/bus.rs tests | User-facing feature | implemented/tested | phenoEvents | phenoEvents/src/bus/in_memory.rs fanout/subscribers; SqliteBus subscribe loop | PARTIAL | Target supports fanout but differs from exact topic/wildcard source API; preserve source. | medium: topic API nuance loss | archive |
| Retry and idempotent handlers | phenotype-bus/src/events/bus.rs IdempotentHandler, RetryPolicy | User-facing feature | implemented/tested | phenoEvents | phenoEvents/README.md, src/bus/mod.rs retries/DLQ/idempotency, src/bus/in_memory.rs duplicate ack | SUPERSEDED_BETTER | Target provides stronger durable retries, DLQ, and duplicate tracking. | low: old in-memory implementation loss | none |
| Subscription lifecycle | phenotype-bus/src/events/subscription.rs | Public API/module | implemented/tested | phenoEvents | phenoEvents/src/bus/mod.rs Subscription Drop aborts worker; in_memory subscriber cleanup | SUPERSEDED_PARITY | Target has equivalent subscription lifecycle in a different handle shape. | low: duplicate lifecycle helper | none |
| Config and observability hooks | phenotype-bus/src/config.rs, src/observability.rs | Internal architecture | implemented | phenoEvents | phenoEvents/src/observability.rs, README observability claims | SUPERSEDED_BETTER | Target integrates observability into broader event substrate. | low | none |
| Source tests and FR claims | phenotype-bus/FUNCTIONAL_REQUIREMENTS.md, src/lib.rs tests, tests/smoke*.rs | Tests | implemented | phenoEvents + registry package | phenoEvents README says 22 unit tests; source tests preserved in snapshot | PARTIAL | Target test inventory was not run here; source tests preserved. | medium: unverified target test coverage | archive |
| Governance/CI/release/security docs | .github/workflows, deny.toml, SECURITY.md, docs/slsa.md | Governance artifacts | docs/config | phenoEvents + registry package | phenoEvents CI/security/governance files; source snapshot | SUPERSEDED_PARITY | Target has active governance and source governance is preserved. | low | archive |
| Local ahead/dirty work | commits e6ac028, 073e125, 88b571f, 594e109 | Branch/local work | branch-only/local-only | phenotype-registry | patches/local-ahead.patch | DONE | Source remote is archived/read-only, so local work is preserved as replayable patch. | low after merge | none |
| Generated Rust build output | phenotype-bus/target/ | Generated files | generated | none | n/a | NO_MERIT | Build output is reproducible and excluded. | low | none |
| Full non-generated source snapshot | source-snapshot/phenotype-bus-source-snapshot.tar.gz | Preservation artifact | preserved | phenotype-registry | this package | DONE | Full source state preserved before deletion. | low after merge | none |

## GAPS_AND_EXCEPTIONS

- Exact source API parity is not claimed because phenoEvents intentionally uses EventEnvelope and a broader durable bus model.
- The source repo is archived/read-only, so local preservation is via registry patch rather than pushed source branch.
- No tests were run in this audit; target parity is based on static source and docs inspection.

## LAST_RESORT_EXCEPTIONS

None after this registry package is merged. Before merge, the local-ahead patch and source snapshot are deletion blockers.

## DELETION_JUSTIFICATION_ESSAY

PhenoEvents owns the surviving event-bus responsibility. It is a better target because it provides the in-memory bus plus durable SQLite outbox, at-least-once delivery, idempotency, DLQ, schema registry, projections, and observability under one event substrate boundary.

The old phenotype-bus API still has merit as API history and as evidence of topic routing/retry/idempotency behavior. Because the target model is not exact API parity, the source snapshot and local-ahead patch are preserved in registry.

Final recommendation: delete KooshaPari/phenotype-bus only after this registry package is merged. If merge cannot be completed, preserve the archived repo.
