#!/usr/bin/env python3
"""
propagate-intent-to-repos.py
=============================

For every repo bound in _bindings.json (from phenotype-registry curation sweep),
copy the corresponding docs/intent/<repo>.md and docs/boundary/<repo>.md into
<monorepo-root>/<repo>/docs/intent/ and <monorepo-root>/<repo>/docs/boundary/.

Skips:
- phenotype-registry itself (the source repo)
- repos that don't exist on disk (orphans / archived)
- already-present files (unless --force)

Adds a `<!-- propagated-from: phenotype-registry/chore/l7-001-...-->` header.
"""
import json
import shutil
import sys
import argparse
from pathlib import Path

REPO_ROOT = Path("/Users/kooshapari/CodeProjects/Phenotype/repos")
SOURCE_INTENT = REPO_ROOT / "phenotype-registry-curation-data" / "docs" / "intent"
SOURCE_BOUNDARY = REPO_ROOT / "phenotype-registry-curation-data" / "docs" / "boundary"
SOURCE_BINDINGS = REPO_ROOT / "phenotype-registry-curation-data" / "_bindings.json"

PROPAGATION_BANNER = """<!--
propagated-from: KooshaPari/phenotype-registry @ chore/l7-001-curation-snapshot
date: 2026-06-17
source-commit: a1aa44660
do-not-edit-locally: regenerate via scripts/propagate-intent-to-repos.py
                     or update in the source-of-truth registry repo
-->
"""


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--force", action="store_true", help="Overwrite existing files")
    p.add_argument("--dry-run", action="store_true", help="Print plan without copying")
    p.add_argument("--repo", help="Only propagate to a single repo")
    args = p.parse_args()

    if not SOURCE_BINDINGS.exists():
        sys.exit(f"ERR: {SOURCE_BINDINGS} not found")
    if not SOURCE_INTENT.exists():
        sys.exit(f"ERR: {SOURCE_INTENT} not found")
    if not SOURCE_BOUNDARY.exists():
        sys.exit(f"ERR: {SOURCE_BOUNDARY} not found")

    bindings = json.load(open(SOURCE_BINDINGS, encoding="utf-8"))
    repos = sorted(bindings.keys()) if not args.repo else [args.repo]

    success, skipped_missing, skipped_existing, failed = [], [], [], []
    for repo in repos:
        repo_dir = REPO_ROOT / repo
        if repo == "phenotype-registry" or repo_dir.name == "phenotype-registry":
            skipped_existing.append((repo, "source repo"))
            continue
        if not repo_dir.is_dir():
            skipped_missing.append(repo)
            continue

        intent_dst = repo_dir / "docs" / "intent" / f"{repo}.md"
        boundary_dst = repo_dir / "docs" / "boundary" / f"{repo}.md"
        intent_src = SOURCE_INTENT / f"{repo}.md"
        boundary_src = SOURCE_BOUNDARY / f"{repo}.md"

        if not intent_src.exists() and not boundary_src.exists():
            skipped_missing.append((repo, "no source files"))
            continue

        ops = []
        if intent_src.exists():
            if intent_dst.exists() and not args.force:
                skipped_existing.append((repo, str(intent_dst.relative_to(REPO_ROOT))))
            else:
                intent_dst.parent.mkdir(parents=True, exist_ok=True)
                if not args.dry_run:
                    with intent_src.open("r", encoding="utf-8") as f:
                        content = f.read()
                    if not content.startswith("<!--\npropagated-from:"):
                        content = PROPAGATION_BANNER + content
                    intent_dst.write_text(content, encoding="utf-8")
                ops.append(f"intent->{intent_dst.relative_to(REPO_ROOT)}")

        if boundary_src.exists():
            if boundary_dst.exists() and not args.force:
                skipped_existing.append((repo, str(boundary_dst.relative_to(REPO_ROOT))))
            else:
                boundary_dst.parent.mkdir(parents=True, exist_ok=True)
                if not args.dry_run:
                    with boundary_src.open("r", encoding="utf-8") as f:
                        content = f.read()
                    if not content.startswith("<!--\npropagated-from:"):
                        content = PROPAGATION_BANNER + content
                    boundary_dst.write_text(content, encoding="utf-8")
                ops.append(f"boundary->{boundary_dst.relative_to(REPO_ROOT)}")

        if ops:
            success.append((repo, ops))

    print(f"\n=== Propagation Report ===")
    print(f"Total repos in bindings: {len(repos)}")
    print(f"✅ propagated:           {len(success)}")
    print(f"⏭  skipped (existing):   {len(skipped_existing)}")
    print(f"⚠️  skipped (missing):    {len(skipped_missing)}")
    if failed:
        print(f"❌ failed:                {len(failed)}")

    if args.dry_run:
        print("\nDRY RUN — no files written")
    else:
        print(f"\n✅ Wrote {len(success)} repo docs/intent+docs/boundary pairs")

    if success:
        print(f"\n=== First 15 successes ===")
        for repo, ops in success[:15]:
            print(f"  {repo}:")
            for op in ops:
                print(f"    {op}")

    if skipped_missing:
        print(f"\n=== Missing (won't propagate) ===")
        for r in skipped_missing[:30]:
            print(f"  {r}")
        if len(skipped_missing) > 30:
            print(f"  ... and {len(skipped_missing) - 30} more")

    return 0


if __name__ == "__main__":
    sys.exit(main())