#!/usr/bin/env python3
"""
render-per-repo.py — Read _bindings.json (and _bindings.win.json if present) and
generate a docs/intent/<repo>.md + docs/boundary/<repo>.md for every bound repo.

Skips repos that already have an intent file (to preserve human edits).
Emits a summary to _rendered.md.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--force", action="store_true", help="Overwrite existing intent/boundary files")
    ap.add_argument("--only", help="Comma-separated repo names to render (skip others)")
    args = ap.parse_args()

    reg = args.out
    bindings_path = reg / "_bindings.json"
    if not bindings_path.exists():
        print(f"[render] no _bindings.json at {bindings_path}; run scrape first", file=sys.stderr)
        return 1

    bindings: dict = json.loads(bindings_path.read_text())
    if (reg / "_bindings.win.json").exists():
        wb = json.loads((reg / "_bindings.win.json").read_text())
        for repo, kinds in wb.items():
            for kind, ids in kinds.items():
                bindings.setdefault(repo, {}).setdefault(kind, [])
                # de-dup
                existing = set(bindings[repo][kind])
                for i in ids:
                    if i not in existing:
                        bindings[repo][kind].append(i)
                        existing.add(i)

    # Reverse lookup: id → (source, kind, relative md path)
    id_to_path: dict[str, Path] = {}
    for md in (reg / "docs" / "curated-prompts").rglob("*.md"):
        m = re.match(r"^---\s*\nid:\s*\"([0-9a-f]{16})\"", md.read_text()[:600])
        if m:
            id_to_path[m.group(1)] = md
    for md in (reg / "docs" / "curated-plans").rglob("*.md"):
        m = re.match(r"^---\s*\nid:\s*\"([0-9a-f]{16})\"", md.read_text()[:600])
        if m:
            id_to_path.setdefault(m.group(1), md)
    for md in (reg / "docs" / "curated-responses").rglob("*.md"):
        m = re.match(r"^---\s*\nid:\s*\"([0-9a-f]{16})\"", md.read_text()[:600])
        if m:
            id_to_path.setdefault(m.group(1), md)

    intent_dir = reg / "docs" / "intent"
    boundary_dir = reg / "docs" / "boundary"
    intent_dir.mkdir(parents=True, exist_ok=True)
    boundary_dir.mkdir(parents=True, exist_ok=True)

    rendered = []
    only = set([s.strip() for s in (args.only or "").split(",") if s.strip()]) or None
    for repo, kinds in sorted(bindings.items()):
        if only and repo not in only:
            continue
        intent_path = intent_dir / f"{repo}.md"
        boundary_path = boundary_dir / f"{repo}.md"
        if not args.force:
            if intent_path.exists() and intent_path.stat().st_size > 800:
                print(f"[render] SKIP {repo} (intent file already present at {intent_path})", file=sys.stderr)
                continue
            if boundary_path.exists() and boundary_path.stat().st_size > 400:
                print(f"[render] SKIP {repo} (boundary file already present)", file=sys.stderr)
                continue
        prompts = kinds.get("prompt", [])
        plans = kinds.get("plan", [])
        responses = kinds.get("response", [])
        # Intent
        body = f"""---
repo: "{repo}"
aliases: []
role: unknown
status: active
last_verified: 2026-06-17
bound_prompts: {len(prompts)}
bound_plans: {len(plans)}
bound_responses: {len(responses)}
device: macbook
---

# Intent — {repo}

## Intent Statement

<To be filled in by hand from the most recent binding prompt. This repo is bound to {len(prompts)} prompts, {len(plans)} plans, and {len(responses)} agent responses captured between 2025-08 and 2026-06-17.>

## Bound Prompts

| Date | Source | File | Tag |
| ---- | ------ | ---- | --- |
"""
        for pid in prompts[:50]:
            md = id_to_path.get(pid)
            if not md:
                body += f"| ? | ? | `{pid}.md` (not rendered) | ? |\n"
                continue
            rel = md.relative_to(reg)
            # Extract timestamp + tag from frontmatter
            txt = md.read_text()[:600]
            ts_m = re.search(r'timestamp:\s*"([^"]*)"', txt)
            tag_m = re.search(r'tag:\s*"([^"]*)"', txt)
            body += f"| {ts_m.group(1)[:10] if ts_m else '?'} | {md.parts[2]} | `{rel}` | {tag_m.group(1) if tag_m else '?'} |\n"
        if len(prompts) > 50:
            body += f"\n_…and {len(prompts)-50} more. See `_bindings.json` for full list._\n"
        body += "\n## Bound Plans\n\n| Date | Source | File | Status |\n| ---- | ------ | ---- | ------ |\n"
        for pid in plans[:30]:
            md = id_to_path.get(pid)
            if not md:
                body += f"| ? | ? | `{pid}.md` | ? |\n"
                continue
            rel = md.relative_to(reg)
            txt = md.read_text()[:600]
            ts_m = re.search(r'timestamp:\s*"([^"]*)"', txt)
            body += f"| {ts_m.group(1)[:10] if ts_m else '?'} | {md.parts[2]} | `{rel}` | approved |\n"
        body += "\n## Bound Responses (specs, ideas, plans from agents)\n\n| Date | Source | File | Kind |\n| ---- | ------ | ---- | ---- |\n"
        for pid in responses[:30]:
            md = id_to_path.get(pid)
            if not md:
                body += f"| ? | ? | `{pid}.md` | ? |\n"
                continue
            rel = md.relative_to(reg)
            txt = md.read_text()[:600]
            ts_m = re.search(r'timestamp:\s*"([^"]*)"', txt)
            kind_m = re.search(r'kind:\s*"([^"]*)"', txt)
            body += f"| {ts_m.group(1)[:10] if ts_m else '?'} | {md.parts[2]} | `{rel}` | {kind_m.group(1) if kind_m else '?'} |\n"
        body += f"""
## Boundary

See: [`docs/boundary/{repo}.md`](../boundary/{repo}.md)

## Ecosystem Role

<See `ECOSYSTEM_MAP.md` for the canonical ecosystem role.>

## Open Questions

- <To be filled from the latest prompt on this repo.>

## Change Log

| Date | Change | Worklog |
| ---- | ------ | ------- |
| 2026-06-17 | Initial binding (L7-001 sweep) | `worklogs/L7-001-intent-boundary-curation-2026-06-17.json` |
"""
        intent_path.write_text(body)
        # Boundary
        if not boundary_path.exists():
            boundary_path.write_text(f"""---
repo: "{repo}"
role: unknown
status: active
last_boundary_review: 2026-06-17
review_cadence: 30d
in_scope:
  - "<to be filled>"
out_of_scope:
  - "<to be filled>"
---

# Boundary — {repo}

## In Scope

<To be filled.>

## Out of Scope

| Not here | Lives in | Reason |
| -------- | -------- | ------ |
| <capability> | <other-repo-or-N/A> | <why> |

## Boundary Crossings

| Crossing | Direction | Surface | Status |
| -------- | --------- | ------- | ------ |
| <capability or interface> | <this-repo→other or other→this-repo> | <Trait / HTTP / CLI / file / event> | <green or amber or red> |

## Last Boundary Review

**Date:** 2026-06-17
**Reviewer:** forge subagent (L7-001 sweep)
**Worklog / finding:** `worklogs/L7-001-intent-boundary-curation-2026-06-17.json`
**Decisions:**
- Initial scaffolding; needs human review.

**Next review:** 2026-07-17
""")
        rendered.append((repo, len(prompts), len(plans), len(responses)))
        print(f"[render] {repo}: prompts={len(prompts)} plans={len(plans)} responses={len(responses)}", file=sys.stderr)

    # Summary
    summary = reg / "_rendered.md"
    summary.write_text(
        "# L7-001 Render Summary\n\n"
        f"Rendered {len(rendered)} repos.\n\n"
        "| Repo | Prompts | Plans | Responses |\n"
        "| ---- | ------- | ----- | --------- |\n"
        + "\n".join(f"| {r} | {p} | {pl} | {re_} |" for r, p, pl, re_ in sorted(rendered, key=lambda x: -x[1]))
    )
    print(f"[render] summary at {summary}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
