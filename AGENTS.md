# phenotype-org-governance — AGENTS.md

## Project Overview

TypeScript/JavaScript governance documentation and tooling for the Phenotype organization.

## Stack

- Language: JavaScript/TypeScript (per GitHub language detection)
- Package manager: npm or pnpm (verify `package.json`)
- Verify build/test tooling locally

## Key Commands

```bash
# Verify project structure
ls -la package.json tsconfig.json 2>/dev/null

# Install deps
npm install  # or pnpm install

# Build/test
npm run build
npm test
```

## Mandatory Reading

Before proposing a new repo, crate, package, doc, workflow, or registry entry:

- [`governance/org-strategy/org-product-doctrine.md`](governance/org-strategy/org-product-doctrine.md) — **AUTHORITATIVE** org product posture (effective 2026-06-11). Covers super-bundle SDKs, repo naming, registry pattern, and the "treat every repo as a product competing for OSS share" rule. Surface conflicts with this file in the PR; do not silently pick a side.

## Notes

- **Active** — verify language and build system locally before running commands
- Authority order for conflicting guidance: latest `effective_date:` in `governance/` wins.
