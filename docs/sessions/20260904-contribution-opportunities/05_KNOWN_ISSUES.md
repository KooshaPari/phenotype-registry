# Known issues and gates

## AgilePlus program tracking unavailable

On September 5, 2026 UTC the mandated fallback command `/Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus/agileplus-agents/bin/agileplus-status health` exited 127: `zsh:1: no such file or directory`. No AgilePlus MCP tool is exposed to this publishing agent. No program spec ID was created or inferred.

Historical registry commit `924022f0` reported a healthy MCP and a queued specification for a DIFFERENT Grapheon program whose subsequent lifecycle lookup returned NOT_FOUND. That history does not establish current service health or tracking for this contribution plan. Explicitly authorized documentation publication proceeds with this limitation recorded; AgilePlus compliance and implementation/merge gates remain unsatisfied. No daemon restart or synthetic lifecycle record is attempted.

## Research limits

- Star totals are snapshots; all ten historical-star requests failed. Rising is UNKNOWN.
- PR samples are bounded, not acceptance probabilities. Maintainer willingness can change.
- Existing open issues can already be fixed: agmsg #1011 was excluded after inspecting merged #1013.
- Headroom and several other proposals are source-informed hypotheses or coverage opportunities, not reproduced bugs. Each must establish a real gap before becoming implementation.
- NadirClaw Noncommercial terms and commercial contribution grant constrain business assumptions. llmtrim also requires a commercial contribution grant. Those decisions remain pending.
- Exact source HEAD pins are provided where captured; moving main links and bounded title searches need refreshing before coding.
- Test commands in plans were not run during this documentation task. Their availability does not imply passing tests, hosted CI or accepted upstream work.
