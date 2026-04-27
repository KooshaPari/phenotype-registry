# Per-staged-file pre-commit hook (Kimi-generated 2026-04-27)

>>> dispatch-worker tier=nvidia/moonshotai/kimi-k2.5 model=nvidia/moonshotai/kimi-k2.5 endpoint=http://localhost:20128/v1
>>> routed to backend: moonshotai/kimi-k2.5
 **(1) `.pre-commit-config.yaml`**

```yaml
repos:
- repo: local
  hooks:
  - id: rust-governance
    name: cargo-deny + clippy
    entry: ./scripts/rust-check.sh
    language: script
    files: \.rs$
    pass_filenames: true
```

**(2) `scripts/rust-check.sh`**

```bash
#!/bin/bash
set -e
declare -A roots
for f; do
  d=$(dirname "$f")
  while [[ "$d" != "." && "$d" != "/" && ! -f "$d/Cargo.toml" ]]; do
    d=$(dirname "$d")
  done
  [[ -f "$d/Cargo.toml" ]] && roots[$d]=1
done
for d in "${!roots[@]}"; do
  (cd "$d" && cargo clippy -- -D warnings && cargo deny check)
done
```
