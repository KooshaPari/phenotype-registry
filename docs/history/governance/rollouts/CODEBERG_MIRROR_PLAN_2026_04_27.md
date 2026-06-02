# Codeberg Mirror Plan (Kimi-generated 2026-04-27)

## Why
GitHub Actions billing-blocked org-wide. Mirror to Codeberg as backup + alternative hosting + lock-in mitigation. 30-day roadmap item #5.

## Setup
1. Register at codeberg.org; create "KooshaPari" organization
2. Generate Personal Access Token at Settings → Applications → repository scope
3. Save `mirror.sh` (below); schedule via cron `0 2 * * * /path/to/mirror.sh`

## Script

```bash
#!/bin/bash
# Phenotype-org → Codeberg nightly mirror
TOKEN="${CODEBERG_PAT}"
ORG="KooshaPari"
for d in ~/CodeProjects/Phenotype/repos/*/; do
  cd "$d" || continue
  [ ! -d ".git" ] && continue
  repo=$(basename "$d")
  case "$repo" in *-wtrees|.archive*|worktrees) continue ;; esac
  
  git remote add codeberg "https://oauth2:${TOKEN}@codeberg.org/${ORG}/${repo}.git" 2>/dev/null
  git fetch origin --quiet 2>&1
  git push codeberg --all --force-with-lease 2>&1 | tail -3
  git push codeberg --tags 2>&1 | tail -3
  
  # LFS objects (skip if repo is LFS-free)
  if [ -f ".gitattributes" ] && grep -q "filter=lfs" .gitattributes; then
    git lfs push codeberg --all 2>&1 | tail -3
  fi
done
```

## Auth
- Use `oauth2:${TOKEN}` HTTPS URL OR Codeberg deploy keys via SSH for better security
- chmod 600 mirror.sh
- Restrict TOKEN scope to repository (not user)

## LFS
Codeberg supports Git LFS. Add `git lfs push codeberg --all` inside loop after standard push if repos use LFS.

## Verification
After first nightly run: `gh repo list KooshaPari --json name | jq '.[] | .name' | wc -l` = Codeberg /api/v1/orgs/KooshaPari/repos?limit=50 count.

## Cross-references
- 30-day roadmap item #5: `governance/rollouts/30_DAY_ROADMAP_2026_04_27.md`
- Memory: `feedback_billing_blocked_rules.md`
