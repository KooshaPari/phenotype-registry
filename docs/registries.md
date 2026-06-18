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

## phenotype-registry (this repo) — Capability & Intent SSOT

Use phenotype-registry when the question is **who owns this capability**,
**what is this repo supposed to do**, or **what did the human intend it for**.

Two new SSOT layers (added L7-001, 2026-06-17):

- [`docs/intent/`](../intent/) — one `<repo>.md` per bound repo with the
  intent statement, the originating prompts that established the contract, and
  the bound plans/responses that justify the role. **L7 sweep counts:**
  108 bound repos, 45,091 curated prompts/plans/responses.
- [`docs/boundary/`](../boundary/) — one `<repo>.md` per bound repo with
  in-scope / out-of-scope / crossings / review cadence. **L7 sweep counts:**
  108 boundary files.
- [`docs/curated-prompts/`](../curated-prompts/) — full curated corpus sliced
  by source tool (`claude-code`, `codex`, `cursor-agent`, `forge`, `droid`,
  `aider`, `other`) then by month then by id. The provenance trail goes:
  `repos/<X>/docs/intent/<X>.md` → `phenotype-registry/docs/intent/<X>.md`
  → `phenotype-registry/docs/curated-prompts/.../id`.md → the original
  prompt in `~/.claude` / `~/.codex` / `~/.cursor`.

Re-rendering & re-propagation scripts:

- [`scripts/scrape.py`](https://github.com/KooshaPari/phenotype-registry/blob/chore/l7-001-contract-only-orphan-2026-06-17/scripts/scrape.py) — incremental extractor
- [`scripts/render-per-repo.py`](https://github.com/KooshaPari/phenotype-registry/blob/chore/l7-001-contract-only-orphan-2026-06-17/scripts/render-per-repo.py)
- [`scripts/propagate-intent-to-repos.py`](https://github.com/KooshaPari/phenotype-registry/blob/chore/l7-001-contract-only-orphan-2026-06-17/scripts/propagate-intent-to-repos.py)
- [`scripts/resolve-collision.py`](https://github.com/KooshaPari/phenotype-registry/blob/chore/l7-001-contract-only-orphan-2026-06-17/scripts/resolve-collision.py)

Live (small-footprint) branch: [`chore/l7-001-contract-only-orphan-2026-06-17`](https://github.com/KooshaPari/phenotype-registry/tree/chore/l7-001-contract-only-orphan-2026-06-17).
Local-only (full 3.2 GB curated corpus) worktree: `../phenotype-registry-curation-data/`.

## Registry Flow

1. Specs define desired behavior.
2. Handbook patterns explain the preferred implementation model.
3. HexaKit templates scaffold projects that follow those patterns.
4. Implementation repos link back to the source spec and pattern decisions.
5. **L7+ addendum**: each implementation repo also has a `docs/intent/<repo>.md`
   and `docs/boundary/<repo>.md` propagated from `phenotype-registry/docs/intent/`
   so the human's stated intent is visible at the repo level.

## Archive Migration Redirects (2026-06-16)

Deleted or absorbed source repos retain history in `projects/*.json` with `absorbed_into` and `absorption_note`. Resolve capabilities at the canonical owner:

| Retired source | Canonical owner |
|----------------|-----------------|
| phenoVessel | [PhenoPlugins/pheno-plugin-vessel](https://github.com/KooshaPari/PhenoPlugins) |
| phenoTypes | [phenotype-types](https://github.com/KooshaPari/phenotype-types) |
| phenoPatch, Diffuse | [phenotype-tooling/phenotype-diff](https://github.com/KooshaPari/phenotype-tooling) |
| Servion | [phenotype-tooling/phenotype-service-registry](https://github.com/KooshaPari/phenotype-tooling) |
| Guardrail | [phenotype-tooling/phenotype-resilience](https://github.com/KooshaPari/phenotype-tooling) |
| Cryptora | [phenoUtils/pheno-crypto](https://github.com/KooshaPari/phenoUtils) |
| forge, phenoForge | [Tasken](https://github.com/KooshaPari/Tasken) |
| router-docs | [OmniRoute/docs/research/archive/router-docs/](https://github.com/KooshaPari/OmniRoute/tree/main/docs/research/archive/router-docs) |

## Boundary owners and rationalization

Use phenotype-registry when the question is **who owns this capability** or **what merges next**.

- [`BOUNDARY_OWNERS.md`](https://github.com/KooshaPari/phenotype-registry/blob/main/BOUNDARY_OWNERS.md) — scaffold vs SDK vs domain workspace; delete gate
- [`ZERO_LOOP_ECOSYSTEM_PLAN.md`](./rationalization/ZERO_LOOP_ECOSYSTEM_PLAN.md) — master DAG, phases, metrics
- [`ECOSYSTEM_DAG.md`](./rationalization/ECOSYSTEM_DAG.md) — 20-lane parallel recipe
- [`SESSION_ARTIFACT_PROTOCOL.md`](./rationalization/SESSION_ARTIFACT_PROTOCOL.md) — agent session folders
- [`RATIONALIZATION_EXECUTION.md`](https://github.com/KooshaPari/phenotype-registry/blob/main/RATIONALIZATION_EXECUTION.md) — merge order + archive shortlist
- [`../intent/`](../intent/) — per-repo **intent statements** (what was said)
- [`../ALIASES.md`](../ALIASES.md) — auto-generated repo-name alias map (L7-002)
- [`../PUSH-STATUS.md`](../PUSH-STATUS.md) — push state, scale, future-push strategy

**AgilePlus** owns spec lifecycle; **phenokits-commons** owns governance templates; this repo owns boundary SSOT.

---

## Rich Media Stubs

<!-- RICH-MEDIA-STUB type="recording-gif" subject="Registry lookup workflow — finding a canonical source of truth" journey="" status="TODO" -->
> **[RICH MEDIA PLACEHOLDER]** *GIF walkthrough of navigating from Registry Reference to the correct canonical repo.*
<!-- END-RICH-MEDIA-STUB -->
