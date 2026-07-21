---
title: Phenotype Org Product Doctrine
status: AUTHORITATIVE
domain: org-strategy
effective_date: 2026-06-11
audience: coding-agents (forge, codex, claude) + humans
supersedes: ad-hoc verbal statements; recurring feedback in worklogs
replaced_by: null
see_also:
  - POLICY.md
  - GOVERNANCE_INDEX.md
  - https://github.com/KooshaPari/phenotype-registry/blob/main/ECOSYSTEM_MAP.md
  - https://github.com/KooshaPari/PhenoHandbook
---

# Phenotype Org Product Doctrine

This document records the org-level product posture that every agent must internalize before naming a repo, splitting a crate, picking a dependency, or proposing a "new project." It is **opinionated on purpose** — we lose more to unopinionated drift than we lose to opinionated rework.

---

## 1. We assume competitors and we want to win OSS market share

**Treat every repo as if it were a product on the scale of fastmcp, React, or Next.js.** That means:

- A repo that nobody outside the org would discover is a **failure of packaging**, not just marketing.
- A README that only makes sense to a KooshaPari contributor is a **product bug**.
- A config that diverges from the most-popular ecosystem default is a **tax on adoption**.
- A "private" repo that we depend on internally is a **migration bomb** waiting to explode.

When a fork of `codex-monorepo` or `DINOForge-UnityDoorstop` exists in this org, it exists because we have a real product reason — not because we wanted to bump a version. If the reason evaporates, retire the fork.

If a project has no conceivable external user, that is a signal to **kill it**, not to soften the docs.

---

## 2. Super-bundle SDKs beat per-project re-implementation

Most of our projects will share opinionated dev/prod infrastructure (otel, docs, landing, dev-env, task runner, CI). We have **two** valid shapes; everything else is anti-DRY in a way that costs us tokens and human breath:

### Shape A — "superbundle" repo
A single repo like `phenodocs` that contains *everything* a project is strapped with: docs templates, layouts, assets, MD-as-config, style choices, and a code generator that emits per-project scaffolding.

**Use when:** the bundle is dense, opinionated, and rarely needs to be split (the consumer is mostly consuming the bundle as a unit).

### Shape B — "SDK as dependency" with a config overlay
A repo like `phenodocs` (npm/VitePress) and a future `phenoLandings` (Astro) that **projects depend on as a package**, and override **only config and assets** at the project level. The smart-update story must exist: bump the dep, get the new docs/landing features.

**Use when:** consumers will diverge on content but not on style/layout, or when the bundle is too small to justify a separate per-project copy.

### Both shapes are valid; pick explicitly per surface and document the choice.

### Anti-patterns (forbidden by default)

- **Each project writes its own docs/landing/ci/dev-env from scratch.** This is the inverse-DRY trap. The marginal cost of "just my own config" is 10× higher than the marginal cost of "another opinion I don't agree with," once you multiply by 50+ projects.
- **A "generic" base repo with no opinions.** "Generic" is just "I haven't decided yet, and now you have to." A base that doesn't take a stance on layout, style, task runner, or CI is a base that forces every project to rediscover each stance independently.
- **An "unopinionated" library in place of a "shared" one.** A library that wraps `tokio` and adds nothing is a wrapper tax. A library that wraps `tokio` and *codifies our patterns* (tracing conventions, retry semantics, error envelopes) is the value-add. We are allowed to be opinionated — that is the point.

---

## 3. Repo naming is product naming

- A repo name is the **public face** of the product. The name has to do two things at once: (a) tell an outsider what the repo is for, (b) tell the registry/agent which *category* it belongs to.
- **Catch-all names are forbidden by default.** `phenotype-tooling` is a current offender — it is a junk drawer. When we split it, the names must be **specific to the why and the what**:
  - `infraTools` → merge into `phenotype-infra` (it's infra-shaped, not a separate "tools" surface).
  - `devTools` → candidate, but only if the contents are clearly developer-experience and *not* infra.
  - `agentTools`, `obsTools`, `evalTools` → fine if the contents match.
- **The opposite failure mode is also bad:** nine `*-standard`, `*-platform`, `*-kit`, `*-hub`, `*-landing` repos with overlapping scope. This is what we currently have. The right move is **consolidate to the canonical name, then unarchive the losers as historical-archive branches**, not "transient push if the name is not better."
  - `phenostandard` ↔ `phenoStandard` are the same idea. We pick one (`phenoStandards` per the ECOSYSTEM_MAP, currently marked deprecated).
  - `platformkit` is a real "kit" name and overlaps with `PlatformKit`. Pick one.
  - `traceon` is the same project as `Traceon`. Lowercase `t` is just a typing error; the right name is the one the registry has.
  - `phenoHub` / `phenotype-hub` / `phenohub` / `pheno-hub` / `Pheno-Hub` are **the same repo five different ways**. Stop. Use one.
  - `x-landings` / `phenotype-landing` / `odin-landing` / `projects-landing` / `phenokits-landing` / `byteport-landing` / `hwledger-landing` / `agileplus-landing` / `thegent-landing` are **eight landing repos for one product line**. The ECOSYSTEM_MAP Cluster K already says: consolidate into `phenotype-landing/packages/<name>`. Do that.
- **The "transient push" pattern is a smell.** A "transient push to a different-named repo" is a "we couldn't decide" push, and a repo nobody can find is worse than a repo with a slightly worse name. If the name is wrong, fix the name; do not push to a temporary mirror.

### Naming rules (default)

1. **One canonical name per product.** The other casings/aliases point to it via README and a `superseded by` line, then get archived.
2. **No catch-all names.** If a repo's contents span two products, split the repo. If they span one product, name the repo after that product.
3. **No `*-kit` for a single-crate SDK.** Use `phenotype-<domain>` for Rust, `phenotype-<domain>-py` for Python, `phenotype-<domain>-go` for Go. The `*Kit` suffix is reserved for *collections* of small libraries (e.g. `PhenoKits` as an index), not single-purpose SDKs.
4. **No two repos may differ only in casing, hyphens, or `pheno`/`phenotype` prefix.**
5. **A repo's name must be greppable in the ECOSYSTEM_MAP role table** (so reviewers can place it in one cluster immediately).

---

## 4. Registry pattern: one canonical index, one canonical home per surface

We already have the spine:

| Repo | Role |
|------|------|
| `phenotype-registry` | **INDEX** — canonical `ECOSYSTEM_MAP.md` |
| `PhenoSpecs` | ADRs / API contracts / specs |
| `PhenoHandbook` | CONVENTIONS / patterns |
| `phenotype-org-governance` (this repo) | **ENFORCEMENT** — `deny.toml`, advisory baseline, conventions-lint, **and (newly) product doctrine** |

**Anything that wants to call itself a "registry" must do exactly one of these:**

- Be the **canonical index** (currently `phenotype-registry`).
- Be a **collection of small things, each with its own canonical home elsewhere**, and index them (e.g. `phenoRouterMonitor/phenotype-registry/projects/*.json` is a project-metadata registry, *not* a source-of-truth for repo state).

A repo that "tracks other repos" but is not the index is an **anti-pattern**: it competes with the index, drifts from reality, and lies. The `phenoRouterMonitor/phenotype-registry/projects/phenoPatch.json` line that says `"status": "complete"` for an empty stub is the canonical example of why this matters.

**`phenotype-registry` itself is the only place that may claim "what repos exist."** Everything else either:
1. **Cites it** (in README/CLAUDE.md/governance docs), or
2. **Generates a derivative** (a project-list, a project-state JSON, a dashboard) by reading it.

Derivative registries must include a `generated_from: phenotype-registry@<sha>` header and a `staleness_decay` policy. If a derivative disagrees with the index, the index wins.

---

## 5. What to do when a repo looks redundant with an existing one

**Default order, highest preference first:**

1. **Re-use the existing repo as a dep** (add a sub-crate, a sub-package, or a sub-folder). Stop.
2. **Unarchive the existing archived repo and resume work there**, with a proper git-history merge. Do this when the target name is "not better."
3. **Fork the existing repo into the new shape** when the rewrite is justified and the old is no longer the canonical home. Use a real `git filter-branch` or `git subtree` so history survives. Not a "transient push."
4. **Create a new repo with a justified, distinct name** — only when the existing repo is the wrong product boundary. This should be rare. When it happens, the proposal must include (a) why the existing repo cannot be extended, (b) which cluster the new repo belongs to in the ECOSYSTEM_MAP, (c) the future consolidation plan.

The "4-already-archived-but-still-useful" state (PolicyStack, DataKit, Traceon, PlatformKit, plus phenostandard, and `x-landing` variants) is the **failure mode we are explicitly avoiding**: a population of partially-useful archived repos that we keep meaning to merge but never do. The current ECOSYSTEM_MAP role table already classifies them — when the classification says "merge into phenotype-python-sdk" or "merge into phenoObservability," that is the action, not a future action.

---

## 6. Dep / lib choices are product choices

We will not reach for the most-popular library if the most-popular library is generic and the alternative that codifies our patterns is also maintained. Examples (non-exhaustive):

- **`tokio` — WRAP, never replace.** It's not our value-add.
- **`tracing` — WRAP + extend.** Our `phenotype-telemetry` crate exists to codify span naming, error-context propagation, and OTel export shape across the org. It's not a tracing replacement; it's our conventions on top of tracing.
- **`reqwest` — handroll aspects** when we need tracing integration, header propagation, and retry semantics that `reqwest` doesn't share with our other crates. The "wrap everything in a thin facade" is fine; "wrap and never expose reqwest's types" is bad when the user has a real reason to need them.
- **A "generic" CLI parser on top of `clap` is a wrapper tax** — we should depend on `clap` directly. A `clap`-derived helper that bakes in our color/output conventions is a value-add.
- **A "generic" config loader on top of `serde`+`figment` is a wrapper tax.** A `Settly`-derived helper that bakes in our schema-validation and env-override patterns is a value-add.

**Rule of thumb:** if a thin wrapper does not change a default, rename a thing, enforce a convention, or expose a higher-level mental model, delete it.

---

## 7. Anti-patterns (forbidden by default)

- **README-only or scaffold-only repos** that describe a product and ship zero working code. If the product is real, ship a stub that compiles and one test that exercises the public API. If the product is not real, do not create the repo.
- **A spec/code/tests mismatch** where the SPEC.md says Go, the code is Python, the tests are YAML, and the PLAN.md is `TBD`. This is the Gastown-rig / LLM-assisted-bootstrap signature. We do not adopt it.
- **A "pheno"-prefixed re-implementation** of an existing non-pheno upstream library, with no new abstraction, no new convention, no new value. If the upstream is good, depend on it; if it is bad, fork and *change something*.
- **A duplicated registry** that disagrees with `phenotype-registry`. The index is the index.
- **A test-coverage matrix doc without a `tests/` dir.** A markdown table that says "covered" without a file that imports the symbol is the same as a lie.
- **An "active" repo in the ECOSYSTEM_MAP whose `gh api` returns `archived: true`.** When that drift is detected, the agent must (a) update the map, (b) update the registry JSON, (c) raise a PR titled `chore(registry): sync ECOSYSTEM_MAP role with archive state`.
- **A landing repo per product.** All landings are `phenotype-landing/packages/<name>`. Eight landing repos is not a "rich" ecosystem; it is a copy-paste debt.
- **A "transient push" to a temporarily-named mirror.** If the name is wrong, rename; do not push to a different name and promise to "consolidate later." "Later" never comes.
- **A wrapper that just re-exports upstream symbols with a `phenotype_` prefix.** That is namespace squatting, not engineering. Re-export only when the wrapper *changes the default*.

---

## 8. What agents must do when they encounter a violation

When **forge, codex, or claude** sees a repo that violates this doctrine during any audit, fix-up, or generation task:

1. **Do not silently comply.** Do not push code that depends on a README-only repo, do not import a wrapper that re-exports upstream without adding value, do not document a landing strategy that copies a known-anti-pattern.
2. **Cite the doctrine section** in the PR description: `governs: §3 (naming), §4 (registry), §7 (anti-patterns)`.
3. **Propose the canonical-home action** in the same PR, not "as a follow-up." If the canonical home is `phenotype-registry`, link to the cluster verdict in the ECOSYSTEM_MAP.
4. **If a conflict between this doctrine and the ECOSYSTEM_MAP role table is found**, raise it in the PR; do not pick a side silently. The doctrine is the *posture*; the ECOSYSTEM_MAP is the *current state*. They can both be true and still be in conflict — the resolution is a sync PR.
5. **If the user (Koosha) overrides the doctrine in a specific case**, record the override in `governance/overrides/<date>-<repo>-<rule>.md` with the rule overridden, the reason, and the exit condition. An override that is not recorded is an override that will be re-litigated forever.

---

## 9. Counting policy

When asked "how many repos do we have," the agent must:

1. Read `phenotype-registry/ECOSYSTEM_MAP.md` `Generated:` date. If the date is older than 30 days, flag staleness and offer to regenerate.
2. List all repos under the `KooshaPari` org via `gh search repos --owner KooshaPari --limit 200 --json name,isArchived,isPrivate`.
3. Report three numbers:
   - **Total** (including archived, including private, including local-only-not-yet-pushed).
   - **Active canonical** (per the ECOSYSTEM_MAP role table, regardless of `gh api archived: true` drift — and flag the drift).
   - **Active non-canonical** (the rest, minus explicit `archived` and explicit `superseded` rows in the map).
4. **Do not round.** Saying "around 190" when the canonical count is 111 is the kind of round that loses audits.

The org was at **111** canonical repos per the 2026-05-30 ECOSYSTEM_MAP. Local-only and not-yet-pushed work is the variable; do not lump it with the published count.

---

## 10. The four roles of any artifact (decision tree)

When an agent is asked to create or rename any artifact — repo, crate, package, doc, workflow, registry entry — they must classify it into one of the four spine roles and one of the ECOSYSTEM_MAP clusters **before** writing any code:

```
What am I creating?
├── INDEX (canonical map, taxonomy, role table)
│     → lives in phenotype-registry, cite everything else from here
├── ADR / spec / contract
│     → lives in PhenoSpecs, no implementation
├── CONVENTION / pattern / rule
│     → lives in PhenoHandbook OR phenotype-org-governance (this file)
│     → must be checkable in CI via conventions-lint or cargo-deny
├── ENFORCEMENT (policy, baseline, lint, gate)
│     → lives in phenotype-org-governance
│     → consumed by siblings as reusable workflow
├── IMPLEMENTATION (crate, package, module, repo)
│     → must declare which cluster it belongs to (Cluster A-K of ECOSYSTEM_MAP)
│     → must declare its canonical home explicitly
│     → if it duplicates an existing canonical home, STOP and propose the merge
└── UNKNOWN
      → do not create. Ask which cluster. Refuse to guess.
```

**"UNKNOWN" is the only safe answer to give back to the user when the cluster is unclear.** Guessing the cluster is the cause of the eight-landing-repo and five-hub-repo state we are in.

---

## 11. Refresh cadence

This document is enforced from its `effective_date`. It is **not** a frozen artifact. The owner (`phenotype-org-governance`) must:

- Re-read this file on every quarterly review.
- Sync any role-table drift with `phenotype-registry/ECOSYSTEM_MAP.md` within 14 days of a cluster verdict change.
- Track overrides under `governance/overrides/`; an override older than 90 days is automatically re-litigated.

---

*This document is the org's product posture. If a coding agent (forge, codex, claude) finds itself in conflict between "what the user just said" and "what this file says," the agent must surface the conflict, not silently pick a side.*
