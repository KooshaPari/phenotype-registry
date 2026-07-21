# IN-CLI `/loop` System — 2026-04-27

## Summary

Created `/loop` functionality for CLIs lacking built-in scheduled task support:
- **OmniRoute** (OpenCode) — uses FreeTier, no API credits
- **Codex** — full GPT capability with tool use
- **Forge** — MiniMax backend for mechanical tasks

## Components

| Component | Location | Purpose |
|-----------|----------|---------|
| loop-setup.sh | `~/.loop/bin/` | Emits shell functions per CLI |
| loop-daemon | `~/.loop/bin/` | Background scheduler |
| loop-support skill | `~/.claude/skills/` | Documentation |
| README | `~/.loop/README.md` | Full user guide |

## Usage

```bash
# Load functions
eval "$(~/.loop/bin/loop-setup.sh omniroute)"

# Start loop
/loop 10m "Check CI status and report failures"

# Manage
/loop-status
/loop-stop
```

## Duration Formats

- `30s`, `5m`, `1h`, `2h30m`, or plain number (default minutes)

## Logs

Stored in `~/.loop/logs/<cli>-YYYY-MM-DD-HH-MM-SS.log`

## Factory Droid Extension

Ready for Factory Droid when CLI available — add `droid)` case to daemon and setup script.

## Comparison with Claude Code

| Feature | Claude Code | IN-CLI Loop |
|---------|-------------|-------------|
| Built-in | ✅ | ❌ (shell function) |
| Agent spawning | ✅ | ⚠️ Single-shot |
| Tool use | ✅ | CLI-dependent |
| Status cmd | ❌ | ✅ `/loop-status` |
| Stop cmd | ❌ | ✅ `/loop-stop` |

## Files Created

```
~/.loop/
├── bin/
│   ├── loop-setup.sh      # Shell function generator
│   └── loop-daemon        # Background scheduler
├── logs/                  # Execution logs
└── README.md              # User documentation

~/.claude/skills/loop-support/
└── SKILL.md               # Skill documentation
```
