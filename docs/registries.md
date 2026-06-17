# Registry Reference

## PhenoSpecs

Use PhenoSpecs when the question is about what should be built.

- Specifications by domain
- Architecture decisions
- OpenAPI contracts
- Traceability from requirement to implementation

## PhenoHandbook

Use PhenoHandbook when the question is about how Phenotype software should be
designed or operated.

- Patterns and anti-patterns
- Coding and operational guidelines
- Methodologies such as TDD, BDD, and DDD
- Review checklists and release practices

## HexaKit

Use HexaKit when the question is about scaffolding a new repo or repeated
project structure.

- Language templates
- Project templates
- Architecture templates
- Template registry metadata

## Registry Flow

1. Specs define desired behavior.
2. Handbook patterns explain the preferred implementation model.
3. HexaKit templates scaffold projects that follow those patterns.
4. Implementation repos link back to the source spec and pattern decisions.

## Language stack

See [`LANGUAGE_STACK.md`](../LANGUAGE_STACK.md) for core (Rust/Zig/Mojo), justified Go edges,
Python 3.14+uv / Bun+TS facades, and deferred repos (GDK, hwLedger, FocalPoint, KaskMan).

## Boundary owners and rationalization

Use phenotype-registry when the question is **who owns this capability** or **what merges next**.

- [`BOUNDARY_OWNERS.md`](../BOUNDARY_OWNERS.md) — scaffold vs SDK vs domain workspace; delete gate
- [`ZERO_LOOP_ECOSYSTEM_PLAN.md`](./rationalization/ZERO_LOOP_ECOSYSTEM_PLAN.md) — master DAG, phases, metrics
- [`ECOSYSTEM_DAG.md`](./rationalization/ECOSYSTEM_DAG.md) — 20-lane parallel recipe
- [`SESSION_ARTIFACT_PROTOCOL.md`](./rationalization/SESSION_ARTIFACT_PROTOCOL.md) — agent session folders
- [`RATIONALIZATION_EXECUTION.md`](../RATIONALIZATION_EXECUTION.md) — merge order + archive shortlist

**AgilePlus** owns spec lifecycle; **phenokits-commons** owns governance templates; this repo owns boundary SSOT.

---

## Rich Media Stubs

<!-- RICH-MEDIA-STUB type="recording-gif" subject="Registry lookup workflow — finding a canonical source of truth" journey="" status="TODO" -->
> **[RICH MEDIA PLACEHOLDER]** *GIF walkthrough of navigating from Registry Reference to the correct canonical repo.*
<!-- END-RICH-MEDIA-STUB -->
