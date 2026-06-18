# ADR-ECO-016: phenotype-omlx platform/engine split (G18)

## Status
Accepted (2026-06-18, Wave G18)

## Context

`phenotype-omlx` is an archived fork of [jundot/omlx](https://github.com/jundot/omlx) (27 branches, macOS menu-bar MLX inference). Registry wave14 audit flagged **FINISH vs DROP** per [ADR-ECO-007 Appendix B](./ADR-ECO-007-gateway-merge-superset.md).

Split doctrine:

- **Platform branding** — org fork `phenotype-omlx` (archived, 27-branch sprawl)
- **Upstream omlx** — engine SSOT at jundot/omlx / omlx.ai

## Decision

**Path: DROP (stay archived)** — no unarchive in G18.

| Layer | Owner | Verdict |
|-------|-------|---------|
| **Engine** | `jundot/omlx` upstream | **CANONICAL** — MLX inference runtime |
| **Platform branding** | `phenotype-omlx` fork | **ARCHIVED** — pointer only; no staffing gate passed |

### Rationale (DROP)

1. phenoAI + OmniRoute + upstream omlx cover product lanes without resurrecting 27-branch fork sprawl.
2. Engine sync follows vendor-fork hygiene (monthly upstream pin), not platform superset merge.
3. macOS menu-bar UX convergence is owned by OmniRoute desktop spike ([ADR-ECO-015](./ADR-ECO-015-hybrid-gateway-app-layer.md)), not a third canonical repo.

### FINISH path (future staffing gate only)

Re-open only when **all** hold:

- Dedicated macOS MLX product owner staffed
- Upstream sync lane + branch cap (≤5) documented
- Branding layer only — engine remains jundot/omlx; no engine code in org fork

Until then: registry records DROP; `fsm: done`.

## Consequences

- `phenotype-omlx` disposition: **ARCHIVED** with `fsm: done` (DROP recorded).
- Registry `projects/phenotype-omlx.json` documents upstream pointer.
- `registry/disposition-index.json` row `gw-phenotype-omlx` links this ADR.
- Amend stale ADR-ECO-008 references in gateway docs → ADR-ECO-016 for omlx split (008 remains phenotype-events).

## Related

- [ADR-ECO-007-gateway-merge-superset](./ADR-ECO-007-gateway-merge-superset.md) — Appendix B FINISH vs DROP
- [ADR-ECO-015-hybrid-gateway-app-layer](./ADR-ECO-015-hybrid-gateway-app-layer.md) — desktop convergence
- [wave15-execution-2026-06-17.md](../operations/wave15-execution-2026-06-17.md) G18
