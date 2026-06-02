# Cargo Deny Auto-Merge Results - 2026-04-27

Wait gates passed at 2026-04-27T02:11:48-0700: `/tmp/auto_create_prs.sh` was no longer running and GitHub core rate limit was 4942.

Only four `OK` PR URLs were present in `/tmp/cargo_deny_pr_creation.log`; all were checked against the exact title `ci(cargo-deny): add scheduled scan + workflow_dispatch (zero-advisory floor)`. No unrelated PRs were touched. Attempts were capped below the requested 27 limit.

| Repo | PR | Result | Head SHA | Merge SHA |
| --- | ---: | --- | --- | --- |
| AgilePlus | 440 | Closed before auto-merge could be enabled | `c637549ba77fb987db40b00150be56fc95009a3f` | n/a |
| GDK | 32 | Merged | `586c3c42af04cd697f85b397012625f232493279` | `ccb24e8b09fb288fbcb28dee6d96ffbbfb4a9541` |
| HeliosLab | 66 | Merged | `aa2290464131bc801bab9003bc72375431c40f73` | `5df9be10b4dfc363eb5ae83d02e5f45578988efc` |
| HexaKit | 105 | Merged | `447d8eede630f995e26d48bb6ee54ce6fef8d81d` | `2f063d2aaf5b0ba33b982f2eb36a32215e0bc1fe` |

Result log: `/tmp/cargo_deny_pr_automerge.log`.
