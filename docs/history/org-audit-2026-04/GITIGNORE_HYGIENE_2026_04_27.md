# Gitignore Hygiene Audit - 2026-04-27

Local-only audit of immediate non-hidden child repos under `/Users/kooshapari/CodeProjects/Phenotype/repos`. Skipped `.archive`, `.worktrees`, `worktrees`, hidden cache/venv directories, and `*-wtrees`/worktree-like directories. The repo-root `.gitignore` and nested `.gitignore` files are out of scope.

## Convention

- Core checked patterns: `target/`, `dist/`, `node_modules/`, `.env*`, `.DS_Store`.
- Additional convention patterns: `*.log`, `.vscode/`, `.idea/`.

## Coverage

- Repos with `/repos/<name>/.gitignore` audited: 78.
- Fully aligned across all convention patterns: 5/78.
- Aligned on requested core patterns: 9/78.
- Skipped non-repo/worktree-like dirs that also had `.gitignore`: 3.

## Top 5 Worst

| Rank | Repo | Missing Count | Missing Patterns |
|---:|---|---:|---|
| 1 | `chatta` | 8 | `target/`, `dist/`, `node_modules/`, `.env*`, `.DS_Store`, `*.log`, `.vscode/`, `.idea/` |
| 2 | `DataKit` | 8 | `target/`, `dist/`, `node_modules/`, `.env*`, `.DS_Store`, `*.log`, `.vscode/`, `.idea/` |
| 3 | `foqos-private` | 8 | `target/`, `dist/`, `node_modules/`, `.env*`, `.DS_Store`, `*.log`, `.vscode/`, `.idea/` |
| 4 | `heliosBench` | 8 | `target/`, `dist/`, `node_modules/`, `.env*`, `.DS_Store`, `*.log`, `.vscode/`, `.idea/` |
| 5 | `MCPForge` | 8 | `target/`, `dist/`, `node_modules/`, `.env*`, `.DS_Store`, `*.log`, `.vscode/`, `.idea/` |

## Full Results

| Repo | Missing Count | Missing Core | Additional Gaps | Present |
|---|---:|---|---|---|
| `chatta` | 8 | `target/`, `dist/`, `node_modules/`, `.env*`, `.DS_Store` | `*.log`, `.vscode/`, `.idea/` | None |
| `DataKit` | 8 | `target/`, `dist/`, `node_modules/`, `.env*`, `.DS_Store` | `*.log`, `.vscode/`, `.idea/` | None |
| `foqos-private` | 8 | `target/`, `dist/`, `node_modules/`, `.env*`, `.DS_Store` | `*.log`, `.vscode/`, `.idea/` | None |
| `heliosBench` | 8 | `target/`, `dist/`, `node_modules/`, `.env*`, `.DS_Store` | `*.log`, `.vscode/`, `.idea/` | None |
| `MCPForge` | 8 | `target/`, `dist/`, `node_modules/`, `.env*`, `.DS_Store` | `*.log`, `.vscode/`, `.idea/` | None |
| `netweave-final2` | 8 | `target/`, `dist/`, `node_modules/`, `.env*`, `.DS_Store` | `*.log`, `.vscode/`, `.idea/` | None |
| `ObservabilityKit` | 8 | `target/`, `dist/`, `node_modules/`, `.env*`, `.DS_Store` | `*.log`, `.vscode/`, `.idea/` | None |
| `phenotype-ops-mcp` | 8 | `target/`, `dist/`, `node_modules/`, `.env*`, `.DS_Store` | `*.log`, `.vscode/`, `.idea/` | None |
| `phenotype-ops-mcp-fix` | 8 | `target/`, `dist/`, `node_modules/`, `.env*`, `.DS_Store` | `*.log`, `.vscode/`, `.idea/` | None |
| `ResilienceKit` | 8 | `target/`, `dist/`, `node_modules/`, `.env*`, `.DS_Store` | `*.log`, `.vscode/`, `.idea/` | None |
| `TestingKit` | 8 | `target/`, `dist/`, `node_modules/`, `.env*`, `.DS_Store` | `*.log`, `.vscode/`, `.idea/` | None |
| `AgilePlus` | 7 | `target/`, `dist/`, `node_modules/`, `.DS_Store` | `*.log`, `.vscode/`, `.idea/` | `.env*` |
| `AppGen` | 7 | `target/`, `dist/`, `.env*`, `.DS_Store` | `*.log`, `.vscode/`, `.idea/` | `node_modules/` |
| `BytePort` | 7 | `dist/`, `node_modules/`, `.env*`, `.DS_Store` | `*.log`, `.vscode/`, `.idea/` | `target/` |
| `helios-router` | 7 | `dist/`, `node_modules/`, `.env*`, `.DS_Store` | `*.log`, `.vscode/`, `.idea/` | `target/` |
| `Httpora` | 7 | `dist/`, `node_modules/`, `.env*`, `.DS_Store` | `*.log`, `.vscode/`, `.idea/` | `target/` |
| `KlipDot` | 7 | `dist/`, `node_modules/`, `.env*`, `.DS_Store` | `*.log`, `.vscode/`, `.idea/` | `target/` |
| `Metron` | 7 | `dist/`, `node_modules/`, `.env*`, `.DS_Store` | `*.log`, `.vscode/`, `.idea/` | `target/` |
| `Tasken` | 7 | `dist/`, `node_modules/`, `.env*`, `.DS_Store` | `*.log`, `.vscode/`, `.idea/` | `target/` |
| `Tokn` | 7 | `dist/`, `node_modules/`, `.env*`, `.DS_Store` | `*.log`, `.vscode/`, `.idea/` | `target/` |
| `DINOForge-UnityDoorstop` | 6 | `target/`, `dist/`, `node_modules/`, `.env*` | `*.log`, `.idea/` | `.DS_Store`, `.vscode/` |
| `Configra` | 6 | `dist/`, `node_modules/`, `.DS_Store` | `*.log`, `.vscode/`, `.idea/` | `target/`, `.env*` |
| `heliosApp` | 6 | `target/`, `.env*`, `.DS_Store` | `*.log`, `.vscode/`, `.idea/` | `dist/`, `node_modules/` |
| `phenoResearchEngine` | 6 | `target/`, `node_modules/`, `.DS_Store` | `*.log`, `.vscode/`, `.idea/` | `dist/`, `.env*` |
| `phenotype-auth-ts` | 6 | `target/`, `.env*`, `.DS_Store` | `*.log`, `.vscode/`, `.idea/` | `dist/`, `node_modules/` |
| `phenotype-tooling` | 6 | `dist/`, `node_modules/`, `.env*` | `*.log`, `.vscode/`, `.idea/` | `target/`, `.DS_Store` |
| `PolicyStack` | 6 | `target/`, `.env*`, `.DS_Store` | `*.log`, `.vscode/`, `.idea/` | `dist/`, `node_modules/` |
| `cheap-llm-mcp` | 5 | `target/`, `node_modules/`, `.env*` | `.vscode/`, `.idea/` | `dist/`, `.DS_Store`, `*.log` |
| `agent-devops-setups` | 5 | `target/`, `.env*` | `*.log`, `.vscode/`, `.idea/` | `dist/`, `node_modules/`, `.DS_Store` |
| `AtomsBot` | 5 | `target/`, `.DS_Store` | `*.log`, `.vscode/`, `.idea/` | `dist/`, `node_modules/`, `.env*` |
| `dispatch-mcp` | 5 | `target/`, `node_modules/` | `*.log`, `.vscode/`, `.idea/` | `dist/`, `.env*`, `.DS_Store` |
| `cliproxyapi-plusplus` | 4 | `target/`, `dist/`, `node_modules/` | `*.log` | `.env*`, `.DS_Store`, `.vscode/`, `.idea/` |
| `Eidolon` | 4 | `dist/`, `node_modules/`, `.env*` | `*.log` | `target/`, `.DS_Store`, `.vscode/`, `.idea/` |
| `GDK` | 4 | `dist/`, `node_modules/`, `.env*` | `*.log` | `target/`, `.DS_Store`, `.vscode/`, `.idea/` |
| `phenotype-org-audits` | 4 | `dist/`, `node_modules/`, `.env*` | `*.log` | `target/`, `.DS_Store`, `.vscode/`, `.idea/` |
| `agent-user-status` | 4 | `node_modules/`, `.env*` | `.vscode/`, `.idea/` | `target/`, `dist/`, `.DS_Store`, `*.log` |
| `atoms.tech` | 4 | `target/`, `dist/` | `*.log`, `.vscode/` | `node_modules/`, `.env*`, `.DS_Store`, `.idea/` |
| `Parpoura` | 4 | `target/`, `dist/` | `.vscode/`, `.idea/` | `node_modules/`, `.env*`, `.DS_Store`, `*.log` |
| `phenoDesign` | 4 | `target/`, `.env*` | `.vscode/`, `.idea/` | `dist/`, `node_modules/`, `.DS_Store`, `*.log` |
| `agileplus-landing` | 4 | `target/` | `*.log`, `.vscode/`, `.idea/` | `dist/`, `node_modules/`, `.env*`, `.DS_Store` |
| `byteport-landing` | 4 | `target/` | `*.log`, `.vscode/`, `.idea/` | `dist/`, `node_modules/`, `.env*`, `.DS_Store` |
| `hwledger-landing` | 4 | `target/` | `*.log`, `.vscode/`, `.idea/` | `dist/`, `node_modules/`, `.env*`, `.DS_Store` |
| `phenokits-landing` | 4 | `target/` | `*.log`, `.vscode/`, `.idea/` | `dist/`, `node_modules/`, `.env*`, `.DS_Store` |
| `phenoShared` | 4 | `.env*` | `*.log`, `.vscode/`, `.idea/` | `target/`, `dist/`, `node_modules/`, `.DS_Store` |
| `thegent-landing` | 4 | `target/` | `*.log`, `.vscode/`, `.idea/` | `dist/`, `node_modules/`, `.env*`, `.DS_Store` |
| `PhenoKits` | 3 | `dist/`, `node_modules/`, `.env*` | None | `target/`, `.DS_Store`, `*.log`, `.vscode/`, `.idea/` |
| `hwLedger` | 3 | `dist/`, `node_modules/` | `*.log` | `target/`, `.env*`, `.DS_Store`, `.vscode/`, `.idea/` |
| `cloud` | 3 | `target/` | `*.log`, `.vscode/` | `dist/`, `node_modules/`, `.env*`, `.DS_Store`, `.idea/` |
| `HeliosLab` | 3 | `dist/` | `*.log`, `.vscode/` | `target/`, `node_modules/`, `.env*`, `.DS_Store`, `.idea/` |
| `phenotype-journeys` | 3 | `.env*` | `.vscode/`, `.idea/` | `target/`, `dist/`, `node_modules/`, `.DS_Store`, `*.log` |
| `portage` | 3 | `node_modules/` | `.vscode/`, `.idea/` | `target/`, `dist/`, `.env*`, `.DS_Store`, `*.log` |
| `projects-landing` | 3 | `target/` | `.vscode/`, `.idea/` | `dist/`, `node_modules/`, `.env*`, `.DS_Store`, `*.log` |
| `bare-cua` | 2 | `node_modules/`, `.env*` | None | `target/`, `dist/`, `.DS_Store`, `*.log`, `.vscode/`, `.idea/` |
| `FocalPoint` | 2 | `dist/`, `node_modules/` | None | `target/`, `.env*`, `.DS_Store`, `*.log`, `.vscode/`, `.idea/` |
| `nanovms` | 2 | `target/`, `.env*` | None | `dist/`, `node_modules/`, `.DS_Store`, `*.log`, `.vscode/`, `.idea/` |
| `phenotype-omlx` | 2 | `target/`, `node_modules/` | None | `dist/`, `.env*`, `.DS_Store`, `*.log`, `.vscode/`, `.idea/` |
| `PlayCua` | 2 | `node_modules/`, `.env*` | None | `target/`, `dist/`, `.DS_Store`, `*.log`, `.vscode/`, `.idea/` |
| `AuthKit` | 2 | `.env*` | `*.log` | `target/`, `dist/`, `node_modules/`, `.DS_Store`, `.vscode/`, `.idea/` |
| `McpKit` | 2 | `.env*` | `*.log` | `target/`, `dist/`, `node_modules/`, `.DS_Store`, `.vscode/`, `.idea/` |
| `Planify` | 2 | `target/` | `*.log` | `dist/`, `node_modules/`, `.env*`, `.DS_Store`, `.vscode/`, `.idea/` |
| `Civis` | 2 | None | `.vscode/`, `.idea/` | `target/`, `dist/`, `node_modules/`, `.env*`, `.DS_Store`, `*.log` |
| `Dino` | 2 | None | `*.log`, `.vscode/` | `target/`, `dist/`, `node_modules/`, `.env*`, `.DS_Store`, `.idea/` |
| `AgentMCP` | 1 | `target/` | None | `dist/`, `node_modules/`, `.env*`, `.DS_Store`, `*.log`, `.vscode/`, `.idea/` |
| `helios-cli` | 1 | `target/` | None | `dist/`, `node_modules/`, `.env*`, `.DS_Store`, `*.log`, `.vscode/`, `.idea/` |
| `heliosCLI` | 1 | `target/` | None | `dist/`, `node_modules/`, `.env*`, `.DS_Store`, `*.log`, `.vscode/`, `.idea/` |
| `kmobile` | 1 | `dist/` | None | `target/`, `node_modules/`, `.env*`, `.DS_Store`, `*.log`, `.vscode/`, `.idea/` |
| `phenodocs` | 1 | `target/` | None | `dist/`, `node_modules/`, `.env*`, `.DS_Store`, `*.log`, `.vscode/`, `.idea/` |
| `phenodocs-scorecard-remediation` | 1 | `target/` | None | `dist/`, `node_modules/`, `.env*`, `.DS_Store`, `*.log`, `.vscode/`, `.idea/` |
| `QuadSGM` | 1 | `target/` | None | `dist/`, `node_modules/`, `.env*`, `.DS_Store`, `*.log`, `.vscode/`, `.idea/` |
| `thegent` | 1 | `.env*` | None | `target/`, `dist/`, `node_modules/`, `.DS_Store`, `*.log`, `.vscode/`, `.idea/` |
| `Tracera-recovered` | 1 | `target/` | None | `dist/`, `node_modules/`, `.env*`, `.DS_Store`, `*.log`, `.vscode/`, `.idea/` |
| `agentapi-plusplus` | 1 | None | `.idea/` | `target/`, `dist/`, `node_modules/`, `.env*`, `.DS_Store`, `*.log`, `.vscode/` |
| `phenoXdd` | 1 | None | `.idea/` | `target/`, `dist/`, `node_modules/`, `.env*`, `.DS_Store`, `*.log`, `.vscode/` |
| `argis-extensions` | 0 | None | None | `target/`, `dist/`, `node_modules/`, `.env*`, `.DS_Store`, `*.log`, `.vscode/`, `.idea/` |
| `kwality` | 0 | None | None | `target/`, `dist/`, `node_modules/`, `.env*`, `.DS_Store`, `*.log`, `.vscode/`, `.idea/` |
| `pheno` | 0 | None | None | `target/`, `dist/`, `node_modules/`, `.env*`, `.DS_Store`, `*.log`, `.vscode/`, `.idea/` |
| `phenotype-infra` | 0 | None | None | `target/`, `dist/`, `node_modules/`, `.env*`, `.DS_Store`, `*.log`, `.vscode/`, `.idea/` |
| `vibeproxy` | 0 | None | None | `target/`, `dist/`, `node_modules/`, `.env*`, `.DS_Store`, `*.log`, `.vscode/`, `.idea/` |

## Method

Each `.gitignore` was read locally. Blank lines, comments, and negation lines were ignored. Pattern detection accepts root, segment, and recursive forms such as `/target/`, `target/`, and `**/target/`; `.env` and `.env*` both satisfy the environment-file convention.
