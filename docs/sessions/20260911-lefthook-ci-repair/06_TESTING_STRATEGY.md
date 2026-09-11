# Validation

## Commands

```sh
LEFTHOOK_TEST_BINARY=/path/to/verified/lefthook_2.1.12_MacOS_arm64 \
  python3 -m unittest discover -s tests -p 'test_*.py' -v
actionlint .github/workflows/lefthook-check.yml
python3 scripts/workflow-action-guard.py .github/workflows/lefthook-check.yml
git diff --check
```

Existing Makefile test target runs Cargo crate tests, not Python/workflow tests. No cli.py
exists, so use direct unittest and workflow validators. Python tests require PyYAML,
already installed locally. On macOS installer tests require GNU gsha256sum from coreutils.

## Coverage

- Exact version/digest, both install sites identical, verification precedes executable bit.
- Successful verified install, digest mismatch, failed download and wrong architecture.
- Literal PR titles containing command substitution, backticks, quotes, newlines,
  backslashes, option-like strings and empty text do not execute shell payloads.
- Real verified v2.1.12 binary accepts conventional titles, rejects invalid/empty titles,
  keeps malicious-looking title text literal, and does not install Git hooks.
- Existing secret guard regression tests remain included.
- Actual published Linux asset checksum agrees with both release checksum file and API digest.

Hosted CI and unrelated baseline failures must be reported separately from local tests.

## Observed local results

2026-09-11: all 11 unittest tests passed (111.623 seconds), including real Lefthook
invocations. actionlint (with embedded ShellCheck), the scoped workflow action guard,
and git diff --check all passed. No tests skipped.
