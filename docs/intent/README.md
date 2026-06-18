# Docs/Intent Contract — Phenotype Registry

**Status:** ACTIVE (2026-06-17)
**Owner:** worklog-schema circle
**Source of truth:** this file
**Worklog:** `worklogs/L7-001-intent-boundary-curation-2026-06-17.md`
**Related ADRs:** ADR-024 (71-pillar), ADR-025 (worklog v2.1), ADR-026 (Factory AI Agent Readiness)

---

## 1. Purpose

Every `phenotype-*` / `pheno-*` / canonical ecosystem repo binds a `docs/intent/` bundle that records the **provenance of intent** for that repo. The intent is sourced from explicit prompts the human owner (KooshaPari) issued to coding agents (`claude-code`, `codex`, `cursor-agent`, `forge`, `droid`, `aider`) and from agent-approved plans, ideas, and specifications that flowed back from those agents. This creates a tamper-evident, citable trail from a single human yap → agent interpretation → plan → spec → repo → PR.

**The point:** if a repo is ever questioned ("why does this exist? what problem does it solve? is it still relevant? when did it last see real use?"), the answer is **findable in one directory** — `docs/intent/<repo>.md` — which links to the originating prompts and approved plans. This kills:

- Re-litigating already-settled decisions
- Losing institutional memory when chat logs are wiped (Claude intermittently drops, Cursor/Codex were wiped 2 months at a time, Feb 2026 and earlier still hold gold)
- Orphan plans that never made it to a repo (still findable as `docs/curated-plans/orphan/`)

---

## 2. Scope — what is bound

`docs/intent/<repo>.md` is the canonical binding for one repo. It must contain:

1. **Frontmatter** — `repo`, `aliases`, `role` (per `ECOSYSTEM_MAP.md` taxonomy), `status`, `last_verified`, `bound_prompts` count, `bound_plans` count, `bound_responses` count.
2. **Intent Statement** — 3-7 sentences capturing what the repo exists to do, in the human owner's own voice, sourced from the most recent binding prompt.
3. **Bound Prompts** — list of one or more prompt files in `docs/curated-prompts/<source>/<date>/<id>.md`, each with a one-line summary of why it bound to this repo.
4. **Bound Plans** — list of plan files in `docs/curated-plans/<source>/<date>/<id>.md` that were approved by an agent and that drove a change in this repo.
5. **Bound Responses** — list of agent-produced spec/idea/plan files in `docs/curated-responses/<source>/<date>/<id>.md` that crystallized into this repo.
6. **Boundary** — link to the per-repo `docs/boundary/<repo>.md` (in this same registry repo) defining in-scope vs. out-of-scope.
7. **Ecosystem Role** — one-line restatement of role + dependencies from `ECOSYSTEM_MAP.md`.
8. **Open Questions** — issues currently being worked on, sourced from the latest prompt on this repo.

`docs/boundary/<repo>.md` is the canonical scoping doc for one repo. It must contain:

1. **Frontmatter** — `repo`, `role`, `in_scope`, `out_of_scope`, `depends_on`, `depended_on_by`, `last_boundary_review`.
2. **In Scope** — bulleted list of capabilities the repo owns.
3. **Out of Scope** — bulleted list of capabilities the repo explicitly does NOT own (and where they live instead).
4. **Boundary Crossings** — interface points with other repos; if a feature is on the wrong side of the boundary, the table is the authoritative place to record it pending relocation.
5. **Last Boundary Review** — date and link to the worklog or finding that ratified the current shape.

---

## 3. Sourcing — where the prompts come from

The curated corpus lives at `docs/curated-prompts/`, `docs/curated-plans/`, `docs/curated-responses/`. Each is organized by source then by date:

| Source        | Raw location (Mac)                       | Raw location (Windows)               | Curated to                          |
| ------------- | ---------------------------------------- | ------------------------------------ | ----------------------------------- |
| `claude-code` | `~/.claude/{history.jsonl,projects/*,plans/*,idea-seeds/*,evidence/*,civilization/*}` | `%USERPROFILE%\.claude\...`         | `docs/curated-{prompts,plans,responses}/claude-code/` |
| `codex`       | `~/.codex/{history.jsonl,sessions/*/rollout-*.jsonl,session-archive/logs/*,prompts/*,rules/*,skills/*}` | `%USERPROFILE%\.codex\...`          | `docs/curated-{prompts,plans,responses}/codex/` |
| `cursor-agent`| `~/.cursor/{prompt_history.json,projects/*/agent-transcripts/*.jsonl,ai-tracking/ai-code-tracking.db,plans/*,commands/*,rules/*,skills/*}` | `%USERPROFILE%\.cursor\...`         | `docs/curated-{prompts,plans,responses}/cursor-agent/` |
| `forge`       | `~/Library/Application Support/forge/{conversations/*,config/*}` + `~/.config/forge*/` | `%APPDATA%\forge\...`                | `docs/curated-{prompts,plans,responses}/forge/` |
| `droid`       | n/a on Mac (Mac user uses Code path)     | `%USERPROFILE%\.droid\...`           | `docs/curated-{prompts,plans,responses}/droid/` |
| `aider`       | `~/.aider/{analytics.json,caches/*}`     | `%USERPROFILE%\.aider\...`           | `docs/curated-{prompts,plans,responses}/aider/` |
| `other`       | iMessage, Notes, `~/.claude/downloads/`, etc. | OneNote, Sticky Notes, Outlook drafts | `docs/curated-{prompts,plans,responses}/other/` |

**Sources that have been "wiped"** (Cursor, Codex) are reconstructed from: `~/.claude/idea-seeds/` (auto-saved Cursor Agent transcripts), Codex rollouts (still on disk even when chat UI is wiped), Claude Code `projects/<dir>/<uuid>.jsonl` (the full session log).

---

## 4. Curation — what we keep, what we drop

**Mechanical filter (always applied):**

| Pattern | Disposition | Reason |
| ------- | ----------- | ------ |
| Slash command only (e.g. `/model`, `/clear`, `/commit`) | DROP | not intent; ephemeral UI |
| Single-word confirmations (`yes`, `ok`, `y`, `n`, `thanks`, `👍`) | DROP | not intent |
| Empty prompts / null `display` / null `text` | DROP | not intent |
| Identical repeated "go on" / "continue" / "next" in same session | DROP first N-1, keep last | not intent |
| Truncated pasted-content (where `pastedContents` is non-empty but `display` is empty) | KEEP with `pasted_content_path` link | real intent (user pasted something) |
| Tool-result echoes (e.g. user typed nothing, agent echoed) | DROP | not intent |

**Semantic filter (LLM-assisted, applied to remaining):**

| Pattern | Disposition | Reason |
| ------- | ----------- | ------ |
| Defines a new repo / project / crate / module | KEEP, tag `repo-defining` | high-value |
| Sets policy / governance / rule / ADR | KEEP, tag `policy-setting` | high-value |
| Brainstorm / idea dump | KEEP, tag `idea` | medium-value (crystallizes intent) |
| Debugging or "fix this" with a specific error | KEEP, tag `bugfix` | medium-value |
| Implementation request ("build X with Y") | KEEP, tag `implementation` | high-value |
| Status check / "what is X doing" | KEEP only if repo-defining | low-value otherwise |
| Pure narration of completed work | KEEP, tag `narrative` | medium-value |
| Approval / sign-off ("yes go", "approved") | KEEP only with `parent_prompt` link | context only |
| Pure chitchat ("how are you", "let's take a break") | DROP | not intent |

The full filter log lives at `docs/curated-prompts/FILTER-LOG.md` and is regenerated each run.

---

## 5. Tools — how the scraping works

The scraper is a Python 3.11+ script in `scripts/scrape.py` that:

1. Takes a `--device {mac,win}` flag and a `--out <dir>` path.
2. Walks every raw source in § 3 for the given device.
3. Emits a JSONL of raw extracted records to `<out>/_raw.jsonl`.
4. Applies the mechanical filter (§ 4) → `<out>/_mechanical.jsonl`.
5. Runs the semantic filter via local LLM (default: headless `codex --model codex-mini-medium` invoked via subprocess for batches of 200) → `<out>/_curated.jsonl`.
6. Renders each curated record as a Markdown file with frontmatter → `docs/curated-{prompts,plans,responses}/<source>/<YYYY-MM>/<id>.md`.
7. Generates an updated `docs/curated-{prompts,plans,responses}/INDEX.md` per source.
8. Auto-binds prompts to repos via project-folder → repo-path mapping (`/Users/kooshapari/CodeProjects/Phenotype/repos/HexaKit/` → `HexaKit`) and the ECOSYSTEM_MAP repo list. Unbound prompts go to `docs/curated-prompts/<source>/<YYYY-MM>/_orphan/`.
9. Writes a `worklogs/L7-NNN-<slug>-<date>.json` worklog entry per ADR-015 v2.1 schema (with `device:` field).

The orchestrator script `scripts/run-all.sh` runs scrape on both devices and merges.

---

## 6. Quality bar

A new `docs/intent/<repo>.md` is acceptable iff:

- [ ] Frontmatter is complete and valid
- [ ] Intent statement is sourced (links to a bound prompt)
- [ ] At least one bound prompt and at least one bound plan
- [ ] Boundary link resolves
- [ ] No `TODO` left in frontmatter values

A new `docs/boundary/<repo>.md` is acceptable iff:

- [ ] Frontmatter is complete and valid
- [ ] In/Out of scope are non-empty
- [ ] Boundary crossings table is filled or explicitly N/A
- [ ] Last review date is within 30 days (or `status: dormant`)

Both are scored under the **L64-L68 Documentation & SSOT** pillars of the 71-pillar audit. See `findings/71-pillar-2026-06-17-schema.md` § Documentation & SSOT for the rubric.

---

## 7. Refresh cadence

- **Mechanical scrape**: weekly (every Monday 06:00 PDT) via `scripts/scrape.py --device mac && scripts/scrape.py --device win`
- **Semantic curation**: on-demand after every major batch of new prompts (or weekly if >100 new prompts in a week)
- **Per-repo `docs/intent/<repo>.md`**: refreshed when a new prompt binds, or on every ADR that touches the repo
- **Per-repo `docs/boundary/<repo>.md`**: reviewed every 30 days, or when an ecosystem rationalization ADR is published (see `ECOSYSTEM_MAP.md` § 6)

---

## 8. Exceptions / Known gaps

- **Droid on Mac**: not installed. Mac-user Droid prompts, if any, would have to come from Codex or Cursor Agent. (Droid is Windows-primary.)
- **Claude intermittently loses chat logs**: the registry commit is the authoritative copy once a prompt is bound.
- **Cursor UI wipes (Feb 2026 and earlier)**: reconstructed from `~/.claude/idea-seeds/` (auto-saved Cursor Agent transcripts) where present; some prompts are unrecoverable.
- **Windows pheno-gpu (Linux desktop, 44d offline on tailscale)**: skipped this run; the user can re-run `scripts/scrape.py --device linux` when it is online.
- **Orphan prompts** (no repo binding): still curated, listed under `docs/curated-{prompts,plans,responses}/<source>/<YYYY-MM>/_orphan/`, and surfaced in the weekly review.

---

## 9. How to add a new binding

```bash
# 1. Run the scraper (incremental — picks up only new entries)
python3 scripts/scrape.py --device mac --incremental

# 2. Inspect newly curated prompts
ls docs/curated-prompts/<source>/<YYYY-MM>/

# 3. Manually create the intent + boundary if the repo has none yet
cp docs/intent/_template.md docs/intent/<repo>.md
cp docs/boundary/_template.md docs/boundary/<repo>.md
$EDITOR docs/intent/<repo>.md  # fill frontmatter, intent statement, links

# 4. Commit
git add docs/intent docs/boundary docs/curated-*
git commit -m "docs(intent): bind <repo> to <N> prompts, <M> plans, <K> responses"
```

---

*This contract supersedes any prior `docs/intent/` work in any sub-repo. Any local `docs/intent/` in a `pheno-*` / `phenotype-*` repo that is not bound to this registry is deprecated.*
