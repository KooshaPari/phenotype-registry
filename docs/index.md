# Phenotype Registry

Phenotype Registry is the public navigation layer for the Phenotype registry
system. It connects specification sources, pattern guidance, reusable templates,
and library research into one reference surface.

## Core Registries

| Registry | Purpose | Canonical Surface |
| --- | --- | --- |
| PhenoSpecs | Product specifications, ADRs, and API contracts | [`KooshaPari/PhenoSpecs`](https://github.com/KooshaPari/PhenoSpecs) |
| PhenoHandbook | Patterns, anti-patterns, guidelines, and methodologies | [`KooshaPari/PhenoHandbook`](https://github.com/KooshaPari/PhenoHandbook) |
| HexaKit | Template and scaffold registry | [`KooshaPari/HexaKit`](https://github.com/KooshaPari/HexaKit) |
| Library Research | Wrap-vs-handroll evidence and dependency catalog | [`LIBRARY_RESEARCH_REGISTRY.md`](https://github.com/KooshaPari/phenotype-registry/blob/main/LIBRARY_RESEARCH_REGISTRY.md) |

## Quick Paths

- Use [Registry Reference](./registries.md) to find the correct source of truth.
- Use [Library Research](./library-research.md) before introducing a new
  dependency or hand-rolling a capability.
- Use [Zero-Loop Ecosystem Plan](./rationalization/ZERO_LOOP_ECOSYSTEM_PLAN.md) for
  boundary absorption DAG, AgilePlus governance, and agent session protocol.
- Keep this repo as a navigation hub. Implementation work belongs in the
  referenced registries or product repos.

## Rationalization (2026-06)

| Doc | Purpose |
| --- | --- |
| [ZERO_LOOP_ECOSYSTEM_PLAN](./rationalization/ZERO_LOOP_ECOSYSTEM_PLAN.md) | Master plan: metrics, phases, PR fleet, spec catalog |
| [ECOSYSTEM_DAG](./rationalization/ECOSYSTEM_DAG.md) | 20-lane parallel recipe with deps |
| [SESSION_ARTIFACT_PROTOCOL](./rationalization/SESSION_ARTIFACT_PROTOCOL.md) | Resumable session folder contract |
| [BOUNDARY_OWNERS](../BOUNDARY_OWNERS.md) | Capability SSOT (repo root) |
| [ADR-004..006](./adr/) | Staging vs canonical, AgilePlus, zero-loop sessions |

## Operating Contract

- Registry links should point at canonical repositories, not local worktrees.
- Registry entries should explain why the destination exists and when to use it.
- Library decisions should cite the evidence surface that informed them.
- This docs shell is static and published through GitHub Pages.

---

## Rich Media Stubs

<!-- RICH-MEDIA-STUB type="annotated-screenshot" subject="Phenotype Registry navigation hub overview" journey="" status="TODO" -->
> **[RICH MEDIA PLACEHOLDER]** *Annotated screenshot of the registry hub showing the four registry tiles and quick-path navigation.*
<!-- END-RICH-MEDIA-STUB -->
