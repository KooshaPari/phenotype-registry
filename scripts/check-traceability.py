#!/usr/bin/env python3
"""Validate the requirements-to-tests manifest and report exact coverage."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "requirements" / "traceability.json"
MINIMUM_PERCENT = 85.0


def fail(message: str) -> None:
    print(f"traceability: FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    requirements = data.get("requirements")
    if data.get("schema_version") != 1 or not isinstance(requirements, list):
        fail("manifest must use schema_version 1 and contain a requirements list")
    if not requirements:
        fail("manifest contains no requirements")

    ids: set[str] = set()
    traced = 0
    e2e_total = 0
    e2e_traced = 0

    for requirement in requirements:
        requirement_id = requirement.get("id")
        if not isinstance(requirement_id, str) or not re.fullmatch(
            r"FR-[A-Z]+-\d{3}", requirement_id
        ):
            fail(f"invalid requirement id: {requirement_id!r}")
        if requirement_id in ids:
            fail(f"duplicate requirement id: {requirement_id}")
        ids.add(requirement_id)

        if not requirement.get("description"):
            fail(f"{requirement_id} has no description")
        level = requirement.get("level")
        if level not in {"unit", "e2e"}:
            fail(f"{requirement_id} has invalid level: {level!r}")

        tests = requirement.get("tests")
        valid_tests = 0
        if not isinstance(tests, list):
            fail(f"{requirement_id} tests must be a list")
        for test in tests:
            relative_path = test.get("path")
            test_name = test.get("name")
            if not isinstance(relative_path, str) or not isinstance(test_name, str):
                fail(f"{requirement_id} has an invalid test reference")
            test_path = (ROOT / relative_path).resolve()
            if ROOT not in test_path.parents or not test_path.is_file():
                fail(f"{requirement_id} references missing test file: {relative_path}")
            source = test_path.read_text(encoding="utf-8")
            pattern = rf"#\[test\]\s*(?:\r?\n\s*)fn\s+{re.escape(test_name)}\s*\("
            if not re.search(pattern, source):
                fail(
                    f"{requirement_id} references missing #[test] function "
                    f"{test_name} in {relative_path}"
                )
            if level == "e2e" and not relative_path.startswith("tests/"):
                fail(f"{requirement_id} E2E test must live under tests/")
            valid_tests += 1

        if valid_tests:
            traced += 1
        if level == "e2e":
            e2e_total += 1
            if valid_tests:
                e2e_traced += 1

    traceability = traced / len(requirements) * 100
    e2e_coverage = e2e_traced / e2e_total * 100 if e2e_total else 0.0
    print(
        f"traceability: {traced}/{len(requirements)} requirements "
        f"({traceability:.2f}%)"
    )
    print(
        f"e2e requirements: {e2e_traced}/{e2e_total} "
        f"({e2e_coverage:.2f}%)"
    )
    if traceability < MINIMUM_PERCENT or e2e_coverage < MINIMUM_PERCENT:
        fail(f"coverage must be at least {MINIMUM_PERCENT:.0f}%")


if __name__ == "__main__":
    main()
