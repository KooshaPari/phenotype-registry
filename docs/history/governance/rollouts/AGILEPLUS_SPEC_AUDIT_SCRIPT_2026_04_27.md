# AgilePlus spec audit script (Kimi-generated 2026-04-27)

>>> dispatch-worker tier=nvidia/moonshotai/kimi-k2.5 model=nvidia/moonshotai/kimi-k2.5 endpoint=http://localhost:20128/v1
>>> routed to backend: moonshotai/kimi-k2.5
 Audit script for `kitty-specs/` feature health. It loops subdirectories, flagging missing plan.md or tasks.md, checking for unchecked task boxes (`[ ]`), and detecting staleness via `find` (no files touched in 30 days).

```bash
#!/bin/bash
echo "Auditing kitty-specs..."
for feat in kitty-specs/*/; do
  name=$(basename "$feat")
  tags=""
  [ -f "$feat/plan.md" ] || tags+="[NO-PLAN] "
  [ -f "$feat/tasks.md" ] || tags+="[NO-TASKS] "
  [ -f "$feat/tasks.md" ] && ! grep -q '\[ \]' "$feat/tasks.md" && tags+="[ALL-DONE] "
  [ -z "$(find "$feat" -type f -mtime -30 2>/dev/null)" ] && tags+="[STALE] "
  [ -n "$tags" ] && echo "$name: $tags"
done
```
