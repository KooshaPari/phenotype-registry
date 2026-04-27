#!/usr/bin/env bash
set -uo pipefail

LOG_FILE="/tmp/pr_creation.log"
TITLE_WORKFLOW="ci(cargo-deny): add scheduled scan + workflow_dispatch (zero-advisory floor)"
TITLE_DENY="ci(cargo-deny): add starter deny.toml baseline"
TITLE_FULL="ci(cargo-deny): enroll repository in scheduled scan baseline"

# Explicit repo / branch / body tuples from:
# - org-audit-2026-04/CARGO_DENY_ROLLOUT_BRANCHES_2026_04_27.md (e8275b3)
# - org-audit-2026-04/CARGO_DENY_ROLLOUT_FINAL_2026_04_27.md (e0f2fc8)
PR_ITEMS=(
  $'bare-cua\tci/cargo-deny-full-rollout-2026-04-27\tCloses the cargo-deny workflow gap from CARGO_DENY_TRUE_COVERAGE_2026_04_27.md (4a2a608). Adds starter deny.toml where needed plus the BytePort-template cargo-deny.yml workflow with Monday cron and workflow_dispatch.'
  $'GDK\tci/add-starter-deny-toml-20260427\tAdds the starter deny.toml baseline required before cargo-deny workflow enrollment. Tracked by CARGO_DENY_ROLLOUT_FINAL_2026_04_27.md (e0f2fc8).'
  $'GDK\tci/cargo-deny-rollout-2026-04-27\tCloses the cargo-deny workflow gap from CARGO_DENY_TRUE_COVERAGE_2026_04_27.md (4a2a608). Adds the BytePort-template cargo-deny.yml workflow with Monday cron and workflow_dispatch.'
  $'helios-router\tci/add-starter-deny-toml-20260427\tAdds the starter deny.toml baseline required before cargo-deny workflow enrollment. Tracked by CARGO_DENY_ROLLOUT_FINAL_2026_04_27.md (e0f2fc8).'
  $'HeliosLab\tci/cargo-deny-rollout-2026-04-27\tCloses the cargo-deny workflow gap from CARGO_DENY_TRUE_COVERAGE_2026_04_27.md (4a2a608). Adds the BytePort-template cargo-deny.yml workflow with Monday cron and workflow_dispatch.'
  $'HexaKit\tci/cargo-deny-rollout-20260427\tCloses the cargo-deny workflow gap from CARGO_DENY_TRUE_COVERAGE_2026_04_27.md (4a2a608). Adds the cargo-deny workflow rollout branch tracked in the e0f2fc8 final summary.'
  $'pheno\tci/cargo-deny-rollout-2026-04-27\tCloses the cargo-deny workflow gap from CARGO_DENY_TRUE_COVERAGE_2026_04_27.md (4a2a608). Adds the BytePort-template cargo-deny.yml workflow with Monday cron and workflow_dispatch.'
  $'phenoAI\tci/cargo-deny-full-rollout-2026-04-27\tCloses the cargo-deny workflow gap from CARGO_DENY_TRUE_COVERAGE_2026_04_27.md (4a2a608). Adds starter deny.toml where needed plus the BytePort-template cargo-deny.yml workflow with Monday cron and workflow_dispatch.'
  $'phenoData\tci/cargo-deny-full-rollout-2026-04-27\tCloses the cargo-deny workflow gap from CARGO_DENY_TRUE_COVERAGE_2026_04_27.md (4a2a608). Adds starter deny.toml where needed plus the BytePort-template cargo-deny.yml workflow with Monday cron and workflow_dispatch.'
  $'PhenoKits\tci/cargo-deny-full-rollout-2026-04-27\tCloses the cargo-deny workflow gap from CARGO_DENY_TRUE_COVERAGE_2026_04_27.md (4a2a608). Adds starter deny.toml where needed plus the BytePort-template cargo-deny.yml workflow with Monday cron and workflow_dispatch.'
  $'PhenoProc\tci/cargo-deny-full-rollout-2026-04-27\tCloses the cargo-deny workflow gap from CARGO_DENY_TRUE_COVERAGE_2026_04_27.md (4a2a608). Adds starter deny.toml where needed plus the BytePort-template cargo-deny.yml workflow with Monday cron and workflow_dispatch.'
  $'PhenoRuntime\tci/cargo-deny-full-rollout-2026-04-27\tCloses the cargo-deny workflow gap from CARGO_DENY_TRUE_COVERAGE_2026_04_27.md (4a2a608). Adds starter deny.toml where needed plus the BytePort-template cargo-deny.yml workflow with Monday cron and workflow_dispatch.'
  $'phenoShared\tci/cargo-deny-rollout-2026-04-27\tCloses the cargo-deny workflow gap from CARGO_DENY_TRUE_COVERAGE_2026_04_27.md (4a2a608). Adds the BytePort-template cargo-deny.yml workflow with Monday cron and workflow_dispatch.'
  $'phenotype-journeys\tci/cargo-deny-full-rollout-2026-04-27\tCloses the cargo-deny workflow gap from CARGO_DENY_TRUE_COVERAGE_2026_04_27.md (4a2a608). Adds starter deny.toml where needed plus the BytePort-template cargo-deny.yml workflow with Monday cron and workflow_dispatch.'
  $'phenotype-tooling\tci/cargo-deny-full-rollout-2026-04-27\tCloses the cargo-deny workflow gap from CARGO_DENY_TRUE_COVERAGE_2026_04_27.md (4a2a608). Adds starter deny.toml where needed plus the BytePort-template cargo-deny.yml workflow with Monday cron and workflow_dispatch.'
  $'PhenoVCS\tci/cargo-deny-full-rollout-2026-04-27\tCloses the cargo-deny workflow gap from CARGO_DENY_TRUE_COVERAGE_2026_04_27.md (4a2a608). Adds starter deny.toml where needed plus the BytePort-template cargo-deny.yml workflow with Monday cron and workflow_dispatch.'
  $'PlayCua\tci/cargo-deny-full-rollout-2026-04-27\tCloses the cargo-deny workflow gap from CARGO_DENY_TRUE_COVERAGE_2026_04_27.md (4a2a608). Adds starter deny.toml where needed plus the BytePort-template cargo-deny.yml workflow with Monday cron and workflow_dispatch.'
  $'rich-cli-kit\tci/cargo-deny-full-rollout-2026-04-27\tCloses the cargo-deny workflow gap from CARGO_DENY_TRUE_COVERAGE_2026_04_27.md (4a2a608). Adds starter deny.toml where needed plus the BytePort-template cargo-deny.yml workflow with Monday cron and workflow_dispatch.'
)

timestamp() {
  date -u +"%Y-%m-%dT%H:%M:%SZ"
}

log() {
  printf '[%s] %s\n' "$(timestamp)" "$*" | tee -a "$LOG_FILE"
}

is_rate_limit_error() {
  local message="$1"
  grep -Eiq 'rate limit|secondary rate|API rate limit|abuse detection|retry later' <<<"$message"
}

title_for_branch() {
  local branch="$1"

  if [[ "$branch" == *add-starter-deny-toml* ]]; then
    printf '%s\n' "$TITLE_DENY"
  elif [[ "$branch" == *full-rollout* ]]; then
    printf '%s\n' "$TITLE_FULL"
  else
    printf '%s\n' "$TITLE_WORKFLOW"
  fi
}

create_pr() {
  local repo="$1"
  local branch="$2"
  local body="$3"
  local title output status

  title="$(title_for_branch "$branch")"
  output="$(
    gh pr create \
      --repo "KooshaPari/${repo}" \
      --base main \
      --head "$branch" \
      --title "$title" \
      --body "$body" 2>&1
  )"
  status=$?
  printf '%s\n' "$output"
  return "$status"
}

main() {
  : >"$LOG_FILE"
  log "Starting cargo-deny PR creation for ${#PR_ITEMS[@]} branch tuples."

  local item repo branch body output status
  for item in "${PR_ITEMS[@]}"; do
    IFS=$'\t' read -r repo branch body <<<"$item"
    log "Creating PR for KooshaPari/${repo}:${branch}"

    output="$(create_pr "$repo" "$branch" "$body")"
    status=$?
    log "$output"

    if [[ $status -ne 0 ]] && is_rate_limit_error "$output"; then
      log "Rate limit detected for ${repo}:${branch}; sleeping 60s, then retrying once."
      sleep 60
      output="$(create_pr "$repo" "$branch" "$body")"
      status=$?
      log "$output"
    fi

    if [[ $status -eq 0 ]]; then
      log "OK ${repo}:${branch}"
    else
      log "FAILED ${repo}:${branch} status=${status}"
    fi

    sleep 2
  done

  log "Finished cargo-deny PR creation loop."
}

main "$@"
