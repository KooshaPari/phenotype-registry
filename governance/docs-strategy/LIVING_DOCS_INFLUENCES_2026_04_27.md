# Living Docs Strategy — Influences & Adoption Plan (2026-04-27)

Synthesized from Kimi-researched patterns: Karpathy LLM wiki, Eugene Yan/Lilian Weng surveys, Maggie Appleton digital garden, Simon Willison TILs.

## Pattern 1: Karpathy "session log" style (raw + annotated)
**Source:** nanoGPT/llm.c READMEs + training annotations.

**Format:**
```markdown
## Tooling
$ cargo-deny --version          # 0.14.20
$ git rev-parse HEAD            # a3f7d2e
$ date -u +%Y-%m-%dT%H:%M:%SZ

## Raw Execution
$ cargo-deny check --format=json 2>&1 | tee /tmp/deny.json
**Output:** {"fields":{"message":"RUSTSEC-2024-0344"},"level":"ERROR"}
**Annotation:** *Ignore — transitive dev-dep of criterion. Tracked in #442.*

## Policy Delta
Added to `deny.toml`: ignore = ["RUSTSEC-2024-0344"]

## Verification
$ cargo-deny check  # Re-run confirms 0 errors
```

**Rules:**
1. Never edit logs — append corrections as new blocks
2. Policy lives in code + annotations — no external "Audit Standards PDF"
3. CI emits identical logs — if the markdown doesn't contain raw stderr, the audit didn't happen

**Adoption:** Replace formal audit doc style with `session-logs/YYYY-MM-DD-<topic>.md` for new audits.

## Pattern 2: Maggie Appleton growth stages
**Source:** maggieappleton.com/garden — `seedling | budding | evergreen` markers.

**Mapping for Phenotype-org:**
- **Evergreen (immutable):** CHARTER.md, CODE_OF_CONDUCT.md, cargo-deny TRUE coverage canonical (audited, tagged)
- **Budding (developing, bi-weekly review):** 30_DAY_ROADMAP, active RFCs, migration guides
- **Seedling (raw thought capture):** memory/ directory, draft ADRs, incident hypotheses

**Bidirectional links:** `[[doc-slug]]` inline + `↑ see also [[source]]` backlinks. VitePress plugin: `markdown-it-wikilinks` or custom `transformPageData` hook auto-injecting "Backlinks" section at build.

## Pattern 3: Yan/Weng survey-style canonicals
**Source:** eugeneyan.com + lilianweng.github.io — high-citation LLM surveys that compress scattered work into linkable references.

**5 surveys Phenotype-org should produce (compress 80+ scattered audit docs):**

1. **Bus-Factor Immunization for Technical Orgs** — implicit knowledge → executable runbooks + automated failover + cross-training. Feeds: org-risk/*, knowledge-transfer/*.

2. **Rust Supply-Chain Defense in Depth** — reproducible builds + crate attestation + CI poisoning mitigations + SBOM validation. Feeds: rust/*cargo-supplychain*, security/*ci-hardening*.

3. **Cognitive-Load Minimization in DevTooling** — unified observability + declarative configs + drift detection. Feeds: dx/*, internal-tooling/*.

4. **Observability-Native Verification Patterns** — contract validation + shadow traffic + chaos invariants. Feeds: testing/*e2e-reliability*, reliability/*prod-verification*.

5. **Zero-to-Production Documentation Architecture** — living docs + ADR automation + decision records + architectural fitness functions. Feeds: docs/*readme-rot*, architecture/*decay-tracking*.

## Pattern 4: Simon Willison TILs (Today I Learned)
**Source:** til.simonwillison.net — short, dated, one-trick-per-page.

**Adoption:** Add `governance/til/<YYYY-MM-DD-<command>>.md` for one-shell-trick discoveries (e.g., today's `gh api PUT branches/main/protection` rollout). Each ≤30 lines, raw command + 2-line context.

## Pattern 5: Pinned references at top of repo READMEs
**Source:** Karpathy llm.c — pinned commit hashes for verification reproducibility.

**Adoption:** Each repo README links to:
- `phenotype-org-governance/SUPERSEDED.md` (canonical authority pointer)
- Latest cargo-deny VICTORY snapshot
- Repo-specific session log

## Implementation roadmap
1. **Now:** Convert next session's audit work to Karpathy-format session-log (single file, raw + annotated)
2. **Week 1:** Tag existing 80+ audit docs with `stage: seedling|budding|evergreen` frontmatter
3. **Week 2:** Author the first survey doc (#2 Rust Supply-Chain Defense in Depth) — directly fed by today's cargo-deny + CodeQL + cargo-audit rollouts
4. **Week 3:** VitePress plugin for bidirectional `[[wikilink]]` resolution + backlinks
5. **Week 4:** TIL feed at phenotype.space/til with RSS

## Cross-references
- Memory: `feedback_dashboard_actuals_only.md` (already aligns with Karpathy's "raw is canonical" principle)
- Memory: `feedback_audit_freshness_decay.md` (the audit-decay × 4 we hit today is exactly what session-logs prevent)
- Existing: SUPERSEDED.md (already implements Appleton supersession concept partially)
