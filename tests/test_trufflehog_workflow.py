"""Contract tests for the TruffleHog GitHub Actions workflow."""

from pathlib import Path
import re

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
WORKFLOW_PATH = REPO_ROOT / ".github/workflows/trufflehog.yml"
PR_BASE = "${{ github.event.pull_request.base.sha }}"
PR_HEAD = "${{ github.event.pull_request.head.sha }}"
SUPPORTED_INPUTS = {"path", "base", "head", "extra_args", "version", "image"}


def _workflow() -> dict:
    """Load GitHub Actions YAML without coercing the ``on`` trigger key."""
    with WORKFLOW_PATH.open() as workflow_file:
        workflow = yaml.load(workflow_file, Loader=yaml.BaseLoader)
    assert isinstance(workflow, dict)
    return workflow


def _trufflehog_jobs(workflow: dict) -> dict[str, dict]:
    """Return jobs that invoke the pinned TruffleHog action."""
    jobs = workflow.get("jobs")
    assert isinstance(jobs, dict)
    return {
        name: job
        for name, job in jobs.items()
        if isinstance(job, dict)
        and any(
            isinstance(step, dict)
            and step.get("uses", "").startswith("trufflesecurity/trufflehog@")
            for step in job.get("steps", [])
        )
    }


def _trufflehog_steps(job: dict) -> list[dict]:
    """Return TruffleHog action steps in a job."""
    return [
        step
        for step in job.get("steps", [])
        if isinstance(step, dict)
        and step.get("uses", "").startswith("trufflesecurity/trufflehog@")
    ]


def _trufflehog_lanes_for_events(
    workflow: dict, events: tuple[str, ...]
) -> list[tuple[str, dict, dict]]:
    """Return action lanes selected by their job or TruffleHog step condition."""
    return [
        (name, job, action)
        for name, job in _trufflehog_jobs(workflow).items()
        for action in _trufflehog_steps(job)
        if any(
            event in condition
            for condition in (str(job.get("if", "")), str(action.get("if", "")))
            for event in events
        )
    ]


def _pr_trufflehog_lanes(workflow: dict) -> list[tuple[str, dict, dict]]:
    """Return TruffleHog action lanes selected for pull-request events."""
    return _trufflehog_lanes_for_events(workflow, ("pull_request",))


def _history_trufflehog_lanes(workflow: dict) -> list[tuple[str, dict, dict]]:
    """Return TruffleHog action lanes selected for history events."""
    history_events = ("push", "schedule", "workflow_dispatch")
    return _trufflehog_lanes_for_events(workflow, history_events)


def _values(value: object) -> list[str]:
    """Flatten YAML values so event-only expressions can be checked."""
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        return [item for child in value.values() for item in _values(child)]
    if isinstance(value, list):
        return [item for child in value for item in _values(child)]
    return []


def test_lane_discovery_accepts_renamed_split_action_jobs_and_step_conditions() -> None:
    """Action-bearing lanes are discovered without relying on job names or condition scope."""
    pr_job_lane = {
        "if": "github.event_name == 'pull_request'",
        "steps": [{"uses": "trufflesecurity/trufflehog@pinned-sha"}],
    }
    pr_step_lane = {
        "steps": [
            {
                "if": "github.event_name == 'pull_request'",
                "uses": "trufflesecurity/trufflehog@pinned-sha",
            }
        ],
    }
    history_job_lane = {
        "if": "github.event_name == 'schedule'",
        "steps": [{"uses": "trufflesecurity/trufflehog@pinned-sha"}],
    }
    history_step_lane = {
        "steps": [
            {
                "if": "github.event_name == 'workflow_dispatch'",
                "uses": "trufflesecurity/trufflehog@pinned-sha",
            }
        ],
    }
    mixed_lane = {
        "steps": [
            {
                "if": "github.event_name == 'pull_request'",
                "uses": "trufflesecurity/trufflehog@pinned-sha",
            },
            {
                "if": "github.event_name == 'schedule'",
                "uses": "trufflesecurity/trufflehog@pinned-sha",
            },
        ]
    }
    workflow = {
        "jobs": {
            "secrets-pr-differential": pr_job_lane,
            "secrets-pr-recheck": pr_step_lane,
            "secrets-history-scheduled": history_job_lane,
            "secrets-history-manual": history_step_lane,
            "secrets-mixed": mixed_lane,
            "unrelated": {"steps": [{"uses": "actions/checkout@pinned-sha"}]},
        }
    }

    assert [name for name, _, _ in _pr_trufflehog_lanes(workflow)] == [
        "secrets-pr-differential",
        "secrets-pr-recheck",
        "secrets-mixed",
    ]
    assert [name for name, _, _ in _history_trufflehog_lanes(workflow)] == [
        "secrets-history-scheduled",
        "secrets-history-manual",
        "secrets-mixed",
    ]


def test_trufflehog_uses_differential_pr_scans_and_separate_history_lanes() -> None:
    """PR scans must be base/head differential; history scans need separate triggers."""
    workflow = _workflow()
    triggers = workflow.get("on")
    assert isinstance(triggers, dict)

    pull_request = triggers.get("pull_request")
    push = triggers.get("push")
    assert isinstance(pull_request, dict)
    assert isinstance(push, dict)
    assert pull_request.get("branches") == ["main"]
    assert push.get("branches") == ["main"]
    assert isinstance(triggers.get("schedule"), list)
    assert "workflow_dispatch" in triggers

    pr_lanes = _pr_trufflehog_lanes(workflow)
    assert pr_lanes, "a pull-request TruffleHog invocation is required"
    for _, _, trufflehog in pr_lanes:
        inputs = trufflehog.get("with", {})
        assert inputs.get("base") == PR_BASE
        assert inputs.get("head") == PR_HEAD
        assert "base_depth" not in inputs
        assert "debug" not in inputs


def test_trufflehog_lanes_are_event_aware() -> None:
    """PR and full-history jobs must not share event-specific expressions."""
    workflow = _workflow()
    pr_lanes = _pr_trufflehog_lanes(workflow)
    history_lanes = _history_trufflehog_lanes(workflow)
    assert pr_lanes, "PR differential scan needs an event-conditional action"
    assert history_lanes, "main/scheduled/manual history scan needs an event-conditional action"

    for _, _, action in pr_lanes:
        inputs = action.get("with", {})
        assert inputs.get("base") == PR_BASE
        assert inputs.get("head") == PR_HEAD

    for _, _, action in history_lanes:
        values = _values(action)
        assert PR_BASE not in values
        assert PR_HEAD not in values
        assert set(action.get("with", {})).issubset(SUPPORTED_INPUTS)


def test_trufflehog_action_and_checkout_are_pinned_and_inputs_allowlisted() -> None:
    """Every scan lane must pin actions, retain history, and use documented inputs."""
    jobs = _trufflehog_jobs(_workflow())
    sha = re.compile(r"@[0-9a-f]{40}$")

    for job in jobs.values():
        checkout = next(
            step for step in job["steps"] if step.get("uses", "").startswith("actions/checkout@")
        )
        assert sha.search(checkout["uses"]), checkout["uses"]
        for trufflehog in _trufflehog_steps(job):
            assert sha.search(trufflehog["uses"]), trufflehog["uses"]
            inputs = trufflehog.get("with", {})
            assert set(inputs).issubset(SUPPORTED_INPUTS)
