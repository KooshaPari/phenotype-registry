# phenoForge deletion package

Date: 2026-06-20
Decision: DELETE
Confidence: medium-high

## Executive decision

phenoForge can be deleted after preservation. Its docs/specs describe an ambitious Rust build/task runner, but the implementation is a minimal TaskGraph resolver and CLI stub. Tasken is the better end product because it already owns active task execution, workflow orchestration, scheduling, plugin architecture, adapters, storage, CLI integration, tests, and governance. The phenoForge product contract and SOTA research are preserved in Tasken via Tasken PR #56. Source code and local dirty docs are preserved here as evidence.

## Absorption matrix

| Source Item | Source Evidence | Category | Source State | Target Repo | Target Evidence | Status | Deletion Justification | Risk if Deleted | Required Action |
|-------------|-----------------|----------|--------------|-------------|-----------------|--------|------------------------|-----------------|-----------------|
| Build/task-runner product contract | phenoForge/README.md, SPEC.md, PRD.md, FUNCTIONAL_REQUIREMENTS.md | Product intent | docs-only/stronger than code | Tasken | docs/history/archived-repos/phenoForge/*, Tasken PR #56 | DONE | Contract preserved in active task orchestration target | low | none |
| SOTA build systems research | phenoForge/SOTA_RESEARCH.md | Research | docs-only | Tasken | docs/history/archived-repos/phenoForge/SOTA_RESEARCH.md, PR #56 | DONE | Research retained as Tasken historical input | low | none |
| Minimal TaskGraph resolver | phenoForge/src/lib.rs | Public Rust code | implemented small subset | Tasken | Tasken src/domain/workflows.rs, src/domain/tasks.rs, src/domain/scheduler.rs plus source-code copy here | SUPERSEDED_BETTER | Tasken has broader active domain model and runtime architecture | low-medium; exact simple API deleted | none |
| CLI stub | phenoForge/src/main.rs | CLI | scaffold | Tasken | Tasken src/adapters/primary/cli.rs and src/main.rs | SUPERSEDED_BETTER | Tasken has real async CLI adapter; phenoForge only prints task/watch | low | none |
| Integration/proptest tests | phenoForge/tests/* | Tests | partial/scaffold | Tasken/phenotype-registry | Tasken tests plus source-code/tests copy here | SUPERSEDED_BETTER | Tasken has broader runtime/CLI tests; source tests preserved | low | none |
| Plugin/cache/remote execution promises | phenoForge README/SPEC | Feature claims | docs-only/unimplemented | Tasken | Tasken plugins/cache/domain modules and phenoForge docs in PR #56 | PARTIAL | Target covers plugin/cache/task orchestration but remote build execution remains historical requirement | medium; future roadmap requirement lost if not preserved | none |
| Local dirty intent/boundary docs | phenoForge/docs/boundary/phenoForge.md, docs/intent/phenoForge.md | Local docs | dirty local | phenotype-registry | patches/local-dirty-docs.patch | DONE | Dirty docs preserved before deletion | medium | none |
| Branch-only/local commits | local branches not on remote tracking branch | Historical work | branch-only | phenotype-registry | patches/local-branches.patch | DONE | Branch deltas preserved if present | medium | none |
| Archived source repo state | GitHub archive true; ARCHIVED.md | Governance | deprecated | Tasken/phenotype-registry | Tasken PR #56 and this package | INTENTIONALLY_DEPRECATED | Active target is Tasken; source archived and now covered | low | none |

## Gaps and exceptions

No LAST_RESORT_EXCEPTION remains. Remote execution/build-cache details are not claimed implemented in Tasken at parity; they are preserved as product requirements/research under Tasken history rather than treated as completed features.

## Final deletion recommendation

DELETE phenoForge after this registry PR merges.
