#!/usr/bin/env bash
# .github/workflows/naming-conventions.sh
# Called by .github/workflows/naming-conventions.yml on every PR touching
# registry.yaml / disposition-index.json. Enforces the 3 approved naming
# patterns from operating-contract §13:
#   pheno-<word>          (lowercase, kebab)
#   Pheno<Word>           (PascalCase, single token)
#   phenotype-<word>      (lowercase, kebab, full prefix)
# Exempts repos under zz-archive-* and any already-archived repo.
set -euo pipefail

ORG="${ORG:-KooshaPari}"
APPROVED_PATTERNS=(
  '^pheno-[a-z][a-z0-9-]*$'           # pheno-short:  pheno-harness, pheno-tracing
  '^Pheno[A-Z][a-zA-Z0-9]*$'          # PhenoPascal:  PhenoCompose, PhenoContracts
  '^phenotype-[a-z][a-z0-9-]*$'       # phenotype-full: phenotype-router, phenotype-org-audits
)
EXEMPT_PREFIX='^zz-archive-'
FAIL_FAST="${FAIL_FAST:-false}"

fail_count=0
warn_count=0
total=0

while IFS=$'\t' read -r name archived; do
  total=$((total + 1))

  # Skip exempt (archived repos under zz-archive-*)
  if [[ "$name" =~ $EXEMPT_PREFIX ]]; then
    continue
  fi

  # Skip archived-but-not-prefixed (already-archived, transitional)
  if [ "$archived" = "true" ]; then
    continue
  fi

  # Check pattern
  matched=0
  for p in "${APPROVED_PATTERNS[@]}"; do
    if [[ "$name" =~ $p ]]; then
      matched=1
      break
    fi
  done

  if [ "$matched" = "0" ]; then
    echo "::error file=naming::Repo '$name' does not match any approved pattern"
    echo "  Approved: pheno-<word>, Pheno<Word>, phenotype-<word>"
    fail_count=$((fail_count + 1))
    if [ "$FAIL_FAST" = "true" ]; then
      exit 1
    fi
  fi
done < <(gh repo list "$ORG" --limit 400 --json name,isArchived \
            --template '{{range .}}{{.name}}{{"\t"}}{{.isArchived}}{{"\n"}}{{end}}')

echo "::notice::checked $total repos, $fail_count violations"
exit $fail_count
