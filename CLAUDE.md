# CLAUDE.md — Phenotype Registry

Extends parent governance. See the following for canonical definitions:
- **Global baseline:** `~/.claude/CLAUDE.md`
- **Phenotype root:** `/Users/kooshapari/CodeProjects/Phenotype/repos/CLAUDE.md`

## Project Overview

- **Name:** phenotype-registry
- **Description:** Library research registry and spec indexing system for Phenotype org
- **Location:** repos/phenotype-registry
- **Language Stack:** TypeScript/JavaScript (npm), Markdown documentation
- **Status:** Active development

## Quality Checks

```bash
npm install
npm test
npm run build
```

## AgilePlus Mandate

All work MUST be tracked in AgilePlus:
- CLI: `cd /Users/kooshapari/CodeProjects/Phenotype/repos/AgilePlus && agileplus <command>`
- Check for existing specs before implementing
- Create spec for new work: `agileplus specify --title "<feature>" --description "<desc>"`
- No code without corresponding AgilePlus spec

## Governance

- `SPEC.md` — Project specification
- `PLAN.md` — Implementation plan
- `docs/` — Supporting documentation
- `LIBRARY_RESEARCH_REGISTRY.md` — Library research index
