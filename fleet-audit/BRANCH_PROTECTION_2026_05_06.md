# Branch Protection Audit — 2026-05-06

## Executive Summary

| Category | Count | Action |
|----------|-------|--------|
| **Total Repos** | 169 | — |
| **Protected** | 118 | 69.8% |
| **Unprotected** | 51 | 30.2% |
| CRITICAL (deploy config) | 0 | — |
| HIGH (2+ workflows) | 17 | Apply protection |
| LOW (personal/minor) | 34 | Consider archiving or protection |

---

## CRITICAL (Need Immediate Protection)

*None identified.* No unprotected repos have Dockerfile, k8s/, or docker-compose files.

---

## HIGH (Should Have Protection)

Repos with 2+ CI/CD workflows but no branch protection:

| Repo | Workflows | Description | Notes |
|------|----------|-------------|-------|
| Pyron | 42 | Python middleware and utilities | **Highest priority** — 42 workflows |
| PhenoRuntime | 15 | ARCHIVED: placeholder only | Archive candidate |
| Planify | 12 | Deprecated fork of Plane.so | Deprecated; default branch=master |
| PlayCua | 11 | Bare-metal computer-use agent | Active project |
| MCPForge | 9 | MCP language server integration | Active project |
| PhenoCompose | 8 | Unified Process Compose with NVMS | Active project |
| .github | 8 | Organization-wide GitHub configs | Special case |
| phenoVessel | 8 | DEPRECATED: merged into PhenoPlugins | Deprecate/delete |
| DINOForge-UnityDoorstop | 3 | Unity doorstop C# integration | Active project |
| KaskMan | 4 | KaskManager R&D Platform | Active project |
| tehgent | 2 | AI-powered code review assistant | Active project |
| atoms.tech | 6 | Vercel-hosted application | Active project |
| netweave-final2 | 5 | — | Needs review |
| RIP-Fitness-App | 5 | Fitness app with MacroFactor | Active project |
| phenoTypes | 5 | DEPRECATED: empty skeleton | Deprecate/delete |
| sharecli | 5 | Shared CLI process manager | Active project |
| helios-cli-backup | 18 | DEPRECATED: backup of HexaKit/helios-cli | Deprecate/delete |

---

## LOW (Nice to Have)

Repos with 0-1 workflows or personal/minor tooling:

| Repo | Workflows | Description |
|------|----------|-------------|
| 472-P2-Flame-War | 1 | ASU FSE100 Project |
| Cryptora | 1 | Simple cryptography |
| Diffuse | 1 | Diff/patch library |
| Eventra | 1 | Event-driven architecture framework |
| Guardrail | 1 | Rate limiting, circuit breaking |
| KVirtualStage | 0 | STRICTLY DO NOT DELETE — Personal Project |
| KWatch | 0 | Kubernetes monitoring |
| KodeVibe | 0 | Code quality guardian |
| KommandLineAutomation | 1 | Playwright equivalent for CLI |
| Logify | 0 | Structured logging framework |
| P2 | 0 | — |
| Prismal | 1 | React component library |
| Profila | 1 | Profiling toolkit |
| Project-Spyn | 0 | ASU FSE100 Project |
| Servion | 1 | Service registry/discovery |
| Traceon | 1 | Distributed tracing |
| acp | 0 | — |
| agentapi | 1 | API gateway for AI agents |
| agslag | 0 | — |
| agslag-dash | 0 | — |
| agslag-docs | 0 | — |
| argisexec | 0 | — |
| canvasApp | 1 | — |
| forge | 1 | CLI task runner |
| go-nippon | 0 | — |
| kmobile | 1 | Mobile development CLI |
| model-conductor-hub | 0 | — |
| pheno-sdk | 0 | ATOMS-PHENO SDK |
| phenoPatch | 1 | phenotype-patch library |
| phenoStandards | 1 | DEPRECATED: empty skeleton |
| phenotype-colab-extensions | 0 | Colab extensions |
| router-docs | 0 | — |
| slickport | 1 | — |
| thegent-sharecli | 1 | Shared CLI (duplicate of sharecli?) |

---

## Protected Repos (118)

These repos have branch protection enabled on `main`:

AgentMCP, Agentora, AgilePlus, Apisync, AppGen, AtomsBot, AuthKit, Authvault, Benchora, BytePort, Civis, Configra, Conft, DataKit, DevHex, Dino, Eidolon, FocalPoint, GDK, HeliosLab, HexaKit, Httpora, KDesktopVirt, KlipDot, KodeVibeGo, McpKit, Metron, ObservabilityKit, OmniRoute, Paginary, Parpoura, PhenoAgent, PhenoDevOps, PhenoHandbook, PhenoKits, PhenoLang, PhenoMCP, PhenoObservability, PhenoPlugins, PhenoProc, PhenoProject, PhenoSpecs, PhenoVCS, Pine, PlatformKit, PolicyStack, QuadSGM, Quillr, ResilienceKit, Settly, Sidekick, Stashly, Tasken, TestingKit, Tokn, Tracely, Tracera, Zerokit, agent-devops-setups, agent-user-status, agentapi-plusplus, agileplus-landing, argis-extensions, bifrost, byteport-landing, chatta, cheap-llm-mcp, cliproxyapi-plusplus, dinoforge-packs, eyetracker, foqos-private, forgecode, helios-cli, helios-router, heliosApp, heliosBench, helioscope, hwLedger, hwledger-landing, kwality, localbase3, nanovms, odin-landing, pheno, phenoAI, phenoData, phenoDesign, phenoForge, phenoResearchEngine, phenoRouterMonitor, phenoShared, phenoUtils, phenoXdd, phenoXddLib, phenodocs, phenokits-landing, phenotype-auth-ts, phenotype-bus, phenotype-dep-guard, phenotype-hub, phenotype-infra, phenotype-journeys, phenotype-omlx, phenotype-ops-mcp, phenotype-org-audits, phenotype-org-governance, phenotype-registry, phenotype-tooling, portage, projects-landing, rich-cli-kit, thegent, thegent-dispatch, thegent-landing, thegent-workspace, vibeproxy, vibeproxy-monitoring-unified, worktree-manager

---

## Recommendations

### Immediate (HIGH Priority)

1. **Apply branch protection to all 17 HIGH-priority repos**:
   ```bash
   # Example: Protect main branch for a repo
   gh api repos/KooshaPari/{REPO}/branches/main/protection -X PUT \
     -f required_status_checks[contexts][]= \
     -f enforce_admins=true \
     -f required_pull_request_reviews=required
   ```

2. **Investigate Pyron** (42 workflows) — verify it needs protection or should be deprecated

3. **Review Planify** — deprecated fork of Plane.so; consider archiving instead of protecting

### Short-term

4. **Address deprecated repos**:
   - `phenoVessel` — merged into PhenoPlugins
   - `phenoTypes` — moved to HexaKit
   - `helios-cli-backup` — use HexaKit/helios-cli
   - `PhenoRuntime` — archived placeholder
   - `phenoStandards` — moved to HexaKit

   Action: Archive or delete these repos to reduce attack surface.

5. **Handle `.github` special case**:
   - Has 8 workflows (organization-wide configs)
   - Consider using a dedicated bot account for changes
   - May not need traditional branch protection

### Long-term

6. **Set default branch protection for new repos** via GitHub Organization settings:
   - Require PR reviews before merging
   - Require status checks (CI, tests, lint)
   - Include administrators in protection

7. **Consider archiving inactive repos**:
   - Repos with 0 workflows and no recent commits
   - Personal projects with no active development
   - Deprecated/forks of abandoned projects

---

## Metrics

- **Compliance rate**: 69.8% (118/169 repos protected)
- **Risk exposure**: 17 repos with significant CI but no protection
- **Cleanup candidates**: 5 deprecated/archived repos without protection
- **Potential improvement**: Protect HIGH repos → 89.9% compliance (152/169)
