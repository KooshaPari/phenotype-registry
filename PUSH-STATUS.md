# L7-001 — Push Status

**Date:** 2026-06-18 00:35 PDT
**Task:** L7-001 docs/intent+boundary contract + Mac+Windows prompt curation sweep
**Worklog:** [`worklogs/L7-001-intent-boundary-curation-2026-06-17.json`](worklogs/L7-001-intent-boundary-curation-2026-06-17.json)

## What was pushed

| Branch | Size | Status | URL |
|---|---|---|---|
| `chore/l7-001-contract-only-orphan-2026-06-17` | 87 KB | ✅ LIVE | [github.com/KooshaPari/phenotype-registry/tree/chore/l7-001-contract-only-orphan-2026-06-17](https://github.com/KooshaPari/phenotype-registry/tree/chore/l7-001-contract-only-orphan-2026-06-17) |
| `chore/l7-001-contract-only-2026-06-17` (full corpus, 3.2 GB) | 3.2 GB | ⏸ LOCAL only | `/Users/kooshapari/CodeProjects/Phenotype/repos/phenotype-registry-intent-bundle/` |

## What's on the orphan branch (live on GitHub)

- `docs/intent/` — 122 per-repo intent files + README (the contract) + REGISTRY + `_template`
- `docs/boundary/` — 121 per-repo boundary files + `_template`
- `scripts/` — `scrape.py`, `run-all.sh`, `run-windows.sh`, `render-per-repo.py`
- `worklogs/L7-001-intent-boundary-curation-2026-06-17.json`
- `.gitignore`

**Total: 262 tree entries, ~87 KB.**

## What's on the local-only branch

- All of the above **PLUS** the full curated corpus:
  - `docs/curated-prompts/{claude-code,codex,cursor-agent,forge,droid,aider,other}/<YYYY-MM>/<id>.md` — **52,116 files** (~3.2 GB)
  - `docs/curated-plans/...` — subagent plans, intent seeds
  - `docs/curated-responses/...` — codex memories, agent specs
- `scripts/_*.json|jsonl|md|txt` — supporting state for re-rendering
- `_curated.jsonl` — the merged Mac+Win curated corpus (45,091 unique records)

## Why two branches?

The local-only branch (`chore/l7-001-contract-only-2026-06-17`) carries 52,116 curated
files as git objects. Git `pack-objects` on the local registry repo has to walk a
2.0 GB existing pack to find deltas, and the I/O was thrashing under contention
with the user's parallel pushes. The full push stalled for >30 min.

The orphan branch was created via:

```bash
git checkout --orphan chore/l7-001-contract-only-orphan-2026-06-17
git rm -rf .
git checkout chore/l7-001-contract-only-2026-06-17 -- docs scripts worklogs .gitignore
git commit -m "feat(registry): L7-001 ..."
git bundle create /tmp/contract-orphan.bundle chore/l7-001-contract-only-orphan-2026-06-17
# then from a fresh shallow clone:
git fetch /tmp/contract-orphan.bundle refs/heads/...
git push --force origin chore/l7-001-contract-only-orphan-2026-06-17
```

This works because the orphan root has **no shared history** with the local
repo's packs — `pack-objects` has nothing to walk, so the bundle is just 87 KB
of fresh objects.

## To push the full 3.2 GB curated corpus later

```bash
cd /Users/kooshapari/CodeProjects/Phenotype/repos/phenotype-registry-intent-bundle
# Create orphan branch with full curated corpus
git checkout --orphan chore/l7-001-curation-snapshot-orphan-2026-06-17
git rm -rf .
git checkout chore/l7-001-contract-only-2026-06-17 -- docs
git commit -m "feat(registry): L7-001 full curation corpus"
git bundle create /tmp/curation.bundle chore/l7-001-curation-snapshot-orphan-2026-06-17

# From a fresh shallow clone:
git clone --filter=blob:none --no-tags https://github.com/KooshaPari/phenotype-registry.git /tmp/pheno-registry-push
cd /tmp/pheno-registry-push
git fetch /tmp/curation.bundle refs/heads/chore/l7-001-curation-snapshot-orphan-2026-06-17:refs/heads/chore/l7-001-curation-snapshot-orphan-2026-06-17
git push --force origin chore/l7-001-curation-snapshot-orphan-2026-06-17
```

## Curation scale (Mac + Windows merged)

| Source | Records kept | Repos bound | Notes |
|---|---|---|---|
| claude-code | 31,061 | 41 | `~/.claude/{history, projects, plans, idea-seeds, evidence, civilization, file-history, todos, sessions}` |
| codex | 14,335 | 62 | `~/.codex/{history, sessions/**/rollout-*.jsonl, session-archive/logs/*, prompts, rules, skills, memories, external_agent_session_imports.json, sqlite/codex-dev.db}` |
| cursor-agent | 19 | 4 | `~/.cursor/{prompt_history.json, ai-tracking/ai-code-tracking.db, plans, commands, rules, skills}` |
| forge | 12 | 2 | `~/Library/Application Support/forge/conversations/*.jsonl` (Mac is mostly smoke-test data) |
| aider | (sparse) | 1 | `~/.aider/{analytics.json, caches/*}` |
| droid | n/a (Mac) / n/a (Win) | 0 | Droid CLI not installed on either device |
| **TOTAL** | **45,091** | **82** | Merged Mac + Windows |

## Top 15 repos by prompt count

| Repo | Prompts | Plans | Responses |
|---|---:|---:|---:|
| phenotype-registry | 18,119 | 0 | 0 |
| phenoVibeproxy | 1,389 | 0 | 0 |
| Dino | 1,228 | 0 | 0 |
| thegent | 747 | 3 | 11 |
| cliproxyapi-plusplus | 401 | 0 | 0 |
| phenotype-journeys | 368 | 0 | 0 |
| DINOForge-UnityDoorstop | 362 | 0 | 0 |
| FocalPoint | 170 | 0 | 0 |
| vibeproxy | 151 | 0 | 0 |
| AuthKit | 139 | 0 | 0 |
| HeliosCLI | 130 | 0 | 0 |
| pheno-otel | 127 | 0 | 0 |
| phenotype-hub | 123 | 0 | 0 |
| Civis | 122 | 0 | 0 |
| PhenoMCP | 113 | 0 | 0 |

(`phenotype-registry` is high because every conversation in the monorepo root
`repos/` projects there — that's the meta-repo bucket, by design.)

## Next steps (human)

1. Review each `docs/intent/<repo>.md` to fill in the Intent Statement prose
2. Review each `docs/boundary/<repo>.md` to fill in the In Scope / Out of Scope lists
3. Resolve repo-name collisions (Dino vs DINOForge-UnityDoorstop, helios-cli vs HeliosCLI, focalpoint vs FocalPoint, agileplus vs AgilePlus) — likely the lowercase variants are typos or worktrees
4. Consider extracting orphan records into a `_meta/` intent file rather than dropping
5. Schedule weekly refresh cadence per ADR-024
6. Push the full 3.2 GB curated corpus to `chore/l7-001-curation-snapshot-orphan-2026-06-17` when network is idle (use orphan-bundle strategy above)