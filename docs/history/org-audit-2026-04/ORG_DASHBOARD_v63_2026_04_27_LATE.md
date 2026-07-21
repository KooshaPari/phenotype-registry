# ORG_DASHBOARD v63 — Phenotype-Org Late-Session Continuation 2026-04-27

## Headline

Phenotype-org late-session continuation 2026-04-27. Cargo-deny rollout extended **+7 repos** (eyetracker, Configra, PhenoMCP, Eidolon, phenotype-bus, phenoUtils, Metron). PolicyStack + HeliosLab + Tokn Pages workflow fixes landed. AgilePlus parking_lot regression already-fixed on `main` (carry-over OBSOLETE).

## PRs / Pushes Landed

| Repo | Action | SHA | Notes |
|---|---|---|---|
| eyetracker | + cargo-deny.yml | `e00f6595` | rebased + pushed |
| Configra | + cargo-deny.yml | `a83535c8` | rebased + pushed |
| PhenoMCP | + cargo-deny.yml | `8fbf7235` | clean fast-forward |
| Eidolon | + cargo-deny.yml | `9175e99` | mass-rollout batch |
| phenotype-bus | + cargo-deny.yml | `c9e9d25` | mass-rollout batch |
| phenoUtils | + cargo-deny.yml | `6996cbe` | mass-rollout batch |
| Metron | + deny.toml + cargo-deny.yml | `e0e3220` | first-time enrollment |
| HeliosLab | fix `deploy-docs.yml` | PR #60 squash | 0s parse fail resolved |
| PolicyStack | fix `pages-deploy.yml` SHA-comment + `with` collision | `08e2467` | run `24976610254` queued |
| Tokn | fix vitepress `base.config` import | `c581938` | run `24976866683` queued |
| phenotype-org-governance | argis recovery + dashboard v62 | `e8fd4b2` | persisted |
| phenotype-org-governance | user-decisions backlog | `f4ebde9` | 7-item user-gated list |

## Cargo-Deny Coverage

- **Pre-session:** BytePort, FocalPoint (2)
- **This session (+7):** eyetracker, Configra, PhenoMCP, Eidolon, phenotype-bus, phenoUtils, Metron
- **Already-upstream:** PhenoObservability (1)
- **Total enrolled: 10** — gap remaining ~25 Rust repos.

## Pages State

| Repo | Verdict |
|---|---|
| FocalPoint | LIVE (github.io 200) |
| HeliosLab | `deploy-docs.yml` parse fixed; downstream `npm ci` issue separate |
| KDV | BILLING-BLOCKED |
| PolicyStack | Workflow now schedules; was 0s parse fail |
| Tokn | `base.config` import fixed; build now hits malformed Vue tag in `docs/research/INDEX.md:5` (separate fix) |

All 5 custom-domain CNAMEs return **530** (Cloudflare SSL not provisioned; user-gated).

## User Decisions Backlog

See `governance/USER_DECISIONS_BACKLOG_2026_04_27.md` (commit `f4ebde9`). 7 items:

1. GDK + KlipDot `.mcp.json` (incl. embedded `coda` `API_KEY`)
2. argis option choice
3. PhenoProc submodule pointer move
4. `/repos` pack-gc
5. Cloudflare 530s
6. OmniRoute v3.7.0 darwin-arm64
7. PhenoProc cargo-deny enrollment

## New Memory Patterns

- `feedback_dispatch_worker_text_only.md` — workers fabricate execution reports; **always verify**.
- `feedback_audit_freshness_decay.md` re-validated: hwLedger flagged for cleanup but found already-enrolled this session.

## Honest Framing

Numbers reflect actual commits/PRs. **AgilePlus parking_lot_core carry-over is OBSOLETE** — `origin/main` builds clean.
