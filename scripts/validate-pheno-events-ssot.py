#!/usr/bin/env python3
"""Validate the authoritative 2phenoEvents/phenoEvents reconciliation."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE_SHA = "5bb0c894e44a50079035b3d5ab5d31946fc445c1"
CANONICAL_SHA = "be6573c68797cc611a99533bca6dc1c3dcdb0c88"


def load_json(relative_path: str) -> dict:
    return json.loads((ROOT / relative_path).read_text(encoding="utf-8"))


def require(errors: list[str], condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    errors: list[str] = []
    alias = load_json("projects/2phenoEvents.json")
    canonical = load_json("projects/phenoEvents.json")
    index = load_json("registry/disposition-index.json")

    require(errors, alias.get("status") == "archived", "2phenoEvents must be archived")
    require(
        errors,
        alias.get("disposition") == "HISTORICAL_ALIAS_TOMBSTONE",
        "2phenoEvents must be a historical alias tombstone",
    )
    require(errors, alias.get("canonical_lineage") == "phenoEvents", "alias must name phenoEvents")
    require(errors, alias.get("source_commit") == SOURCE_SHA, "alias must retain source SHA")
    require(
        errors,
        alias.get("current_remote_status") == "not_found_404",
        "alias must record the current 404 remote state",
    )

    require(
        errors,
        canonical.get("disposition") == "KEEP_CANONICAL_STANDALONE",
        "phenoEvents must remain canonical standalone",
    )
    require(errors, canonical.get("remote_head_sha") == CANONICAL_SHA, "canonical SHA must be current")
    require(
        errors,
        canonical.get("historical_absorption_status") == "unverified",
        "pheno claim must be historical and unverified",
    )

    rows = index.get("rows", [])
    alias_rows = [row for row in rows if row.get("id") == "alias-2phenoEvents"]
    require(errors, len(alias_rows) == 1, "index must contain one alias-2phenoEvents row")
    if alias_rows:
        require(
            errors,
            alias_rows[0].get("source_commit") == SOURCE_SHA,
            "index alias row must retain source SHA",
        )
        require(
            errors,
            alias_rows[0].get("canonical_owner") == "KooshaPari/phenoEvents",
            "index alias row must name canonical owner",
        )

    pheno_rows = [row for row in rows if row.get("path") == "KooshaPari/phenoEvents"]
    require(errors, bool(pheno_rows), "index must retain phenoEvents rows")
    for row in pheno_rows:
        require(
            errors,
            row.get("disposition") == "KEEP_CANONICAL_STANDALONE",
            f"{row.get('id')} must not retain an active ABSORB disposition",
        )
        require(errors, row.get("fsm") == "live", f"{row.get('id')} must remain live")
        require(
            errors,
            row.get("historical_absorption_status") == "unverified",
            f"{row.get('id')} must classify the pheno claim as unverified",
        )

    required_docs = {
        "docs/boundary/2phenoEvents.md": ("HISTORICAL_ALIAS_TOMBSTONE", SOURCE_SHA),
        "docs/boundary/phenoEvents.md": ("KEEP_CANONICAL_STANDALONE", CANONICAL_SHA),
        "docs/boundary/phenotype-event-bus.md": ("historical and unverified", "phenoEvents"),
        "docs/absorption/phenoEvents/README.md": ("Historical and unverified", "phenoEvents"),
        "audits/absorption-justifications/phenoEvents-2026-07-17.md": (
            "Historical and unverified",
            "not current ownership evidence",
        ),
        "audits/absorption-justifications/2phenoEvents-reconciliation-20260805.md": (
            SOURCE_SHA,
            "not found",
        ),
    }
    for relative_path, markers in required_docs.items():
        path = ROOT / relative_path
        require(errors, path.exists(), f"missing reconciliation document: {relative_path}")
        if path.exists():
            content = path.read_text(encoding="utf-8")
            for marker in markers:
                require(errors, marker in content, f"{relative_path} missing marker: {marker}")

    if errors:
        for error in errors:
            print(f"FAIL  {error}")
        return 1

    print("PASS  2phenoEvents/phenoEvents authoritative records agree")
    return 0


if __name__ == "__main__":
    sys.exit(main())
