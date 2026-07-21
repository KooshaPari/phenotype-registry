#!/usr/bin/env bash
set -uo pipefail

LOG_FILE="/tmp/pr_creation.log"
TITLE_WORKFLOW="ci(cargo-deny): add scheduled scan + workflow_dispatch (zero-advisory floor)"
TITLE_DENY="ci(cargo-deny): add starter deny.toml baseline"
TITLE_FULL="ci(cargo-deny): enroll repository in scheduled scan baseline"
BODY_FULL="Closes the cargo-deny workflow gap from CARGO_DENY_TRUE_COVERAGE_2026_04_27.md (4a2a608). Adds starter deny.toml plus the BytePort-template cargo-deny.yml workflow with Monday cron and workflow_dispatch."
BODY_ROLLOUT="Closes the cargo-deny workflow gap from CARGO_DENY_TRUE_COVERAGE_2026_04_27.md (4a2a608). Adds the cargo-deny.yml workflow with Monday cron and workflow_dispatch, plus deny.toml where this rollout branch includes it."
BODY_DISPATCH="Adds workflow_dispatch to the existing cargo-deny workflow so the repository supports on-demand verification alongside scheduled scans. Tracked by CARGO_DENY_ROLLOUT_FINAL_2026_04_27.md."

# Explicit repo / branch / body tuples from:
# - org-audit-2026-04/CARGO_DENY_ROLLOUT_FINAL_2026_04_27.md
# - script baseline commit 37754de, expanded to 27 current branches
PR_ITEMS=(
  $'AgilePlus\tci/cargo-deny-full-rollout-2026-04-27\t'"$BODY_FULL"
  $'GDK\tci/cargo-deny-rollout-2026-04-27\t'"$BODY_ROLLOUT"
  $'HeliosLab\tci/cargo-deny-rollout-2026-04-27\t'"$BODY_ROLLOUT"
  $'HexaKit\tci/cargo-deny-rollout-20260427\t'"$BODY_ROLLOUT"
  $'KDesktopVirt\tci/cargo-deny-full-rollout-2026-04-27\t'"$BODY_FULL"
  $'pheno\tci/cargo-deny-rollout-2026-04-27\t'"$BODY_ROLLOUT"
  $'phenoAI\tci/cargo-deny-full-rollout-2026-04-27\t'"$BODY_FULL"
  $'phenoData\tci/cargo-deny-full-rollout-2026-04-27\t'"$BODY_FULL"
  $'PhenoKits\tci/cargo-deny-full-rollout-2026-04-27\t'"$BODY_FULL"
  $'PhenoProc\tci/cargo-deny-full-rollout-2026-04-27\t'"$BODY_FULL"
  $'PhenoRuntime\tci/cargo-deny-full-rollout-2026-04-27\t'"$BODY_FULL"
  $'phenoShared\tci/cargo-deny-rollout-2026-04-27\t'"$BODY_ROLLOUT"
  $'phenotype-journeys\tci/cargo-deny-full-rollout-2026-04-27\t'"$BODY_FULL"
  $'phenotype-tooling\tci/cargo-deny-full-rollout-2026-04-27\t'"$BODY_FULL"
  $'PhenoVCS\tci/cargo-deny-full-rollout-2026-04-27\t'"$BODY_FULL"
  $'PlayCua\tci/cargo-deny-full-rollout-2026-04-27\t'"$BODY_FULL"
  $'rich-cli-kit\tci/cargo-deny-full-rollout-2026-04-27\t'"$BODY_FULL"
  $'thegent-dispatch\tci/cargo-deny-full-rollout-2026-04-27\t'"$BODY_FULL"
  $'thegent-workspace\tci/cargo-deny-full-rollout-2026-04-27\t'"$BODY_FULL"
  $'Tokn\tci/cargo-deny-full-rollout-2026-04-27\t'"$BODY_FULL"
  $'Tracely\tci/cargo-deny-full-rollout-2026-04-27\t'"$BODY_FULL"
  $'Civis\tci/cargo-deny-add-workflow-dispatch-2026-04-27\t'"$BODY_DISPATCH"
  $'Configra\tci/cargo-deny-add-workflow-dispatch-2026-04-27\t'"$BODY_DISPATCH"
  $'Eidolon\tci/cargo-deny-add-workflow-dispatch-2026-04-27\t'"$BODY_DISPATCH"
  $'eyetracker\tci/cargo-deny-add-workflow-dispatch-2026-04-27\t'"$BODY_DISPATCH"
  $'heliosCLI\tci/cargo-deny-add-workflow-dispatch-2026-04-27\t'"$BODY_DISPATCH"
  $'Metron\tci/cargo-deny-add-workflow-dispatch-2026-04-27\t'"$BODY_DISPATCH"
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
