# User Decisions Backlog — 2026-04-27

Items from the 2026-04-27 Phenotype-org session that are blocked on user input. Agents cannot proceed autonomously on any of these without a decision, a permission grant, or a manual action.

## Items requiring user decision

### 1. GDK + KlipDot `.mcp.json` repair

- **Status:** BLOCKED — Edit/Write permission denied to subagent; secret-rotation also required.
- **What's blocked:** Forge sessions in GDK and KlipDot error out on "Context7 unknown field". Both `.mcp.json` files are invalid JSON for Claude Code's schema — they contain Cline/Roo schema fields (`autoApprove`, `disabled`, `timeout`, `transportType`) that Claude Code does not accept.
- **What user needs to do:**
  1. Approve write permission for the prepared fix (strip non-Claude fields, wrap all servers in a single `mcpServers` object), OR apply the fix manually.
  2. **Before any commit/push:** rotate the embedded `coda` `API_KEY` in GDK `.mcp.json` (looks like a real secret — gitleaks will trip otherwise) and replace with `${CODA_API_KEY}` env-var reference.
- **Artifacts:** subagent-prepared diff (held in session context, not yet written).

### 2. argis-extensions recovery option choice

- **Status:** BLOCKED — three non-destructive options documented; user must pick.
- **What's blocked:** Local branch (24 Bifrost API commits) and `origin/main` (11 mixed Dependabot + governance commits) have UNRELATED histories. No merge-base. Direct merge produces 34 conflicts.
- **What user needs to do:** Choose one of:
  - (A) `git replace --graft` to stitch lineages together.
  - (B) Cherry-pick local commits onto upstream.
  - (C) Keep both as separate branches.
- **Artifacts:** `phenotype-org-governance/governance/argis_recovery_options_2026_04_27.md`.

### 3. PhenoProc dirty tree

- **Status:** BLOCKED — unknown-provenance local changes; needs intent confirmation.
- **What's blocked:**
  - `crates/phenotype-shared` submodule pointer moved locally (`8369060` → `03c92be`) with no corresponding origin change. Real local work of unknown provenance.
  - ~70 untracked files at root (`ADR.md`, `AGENTS.md`, `Duple/`, `Finalis/`, etc.) — looks like staged-but-not-committed structural reorg.
  - cargo-deny enrollment for PhenoProc (item #7 below) is gated on this resolution.
- **What user needs to do:** Decide:
  - Commit the submodule bump intentionally, OR `git checkout -- crates/phenotype-shared` to discard.
  - Same disposition for the ~70 untracked files (commit, archive, or remove).
- **Artifacts:** `git status` in `/repos/PhenoProc/`.

### 4. /repos canonical pack-gc

- **Status:** BLOCKED — Bash sandbox permission still denied.
- **What's blocked:** Pack corruption recovery on the `/repos` canonical worktree. Diagnosis and exact commands are ready; agents cannot execute them under sandbox.
- **What user needs to do:** Run the gc themselves, OR grant a one-time bash permission for the documented command sequence.
- **Artifacts:** `phenotype-org-governance/governance/pack_corruption_diagnosis_2026_04_26.md`.

### 5. Custom-domain Cloudflare 530s

- **Status:** BLOCKED — Cloudflare-side provisioning required.
- **What's blocked:** The following return HTTP 530 (Cloudflare origin/SSL not provisioned for `*.kooshapari.com` Pages CNAMEs):
  - `focalpoint.kooshapari.com`
  - `kdv.kooshapari.com`
  - `helioslab.kooshapari.com`
  - `policystack.kooshapari.com`
  - `tokn.kooshapari.com`
  - `github.io` URLs work for repos where deploys succeeded.
- **What user needs to do:** Provision custom-domain SSL at the Pages level (or at the DNS layer) for `*.kooshapari.com` Pages CNAMEs.

### 6. OmniRoute v3.7.0 broken on darwin-arm64

- **Status:** WORKAROUND IN PLACE (rolled back to v3.4.1).
- **What's blocked:** v3.7.0 ships with missing `wreq-js` native module for darwin-arm64; rolled back to v3.4.1 (working).
- **What user needs to do:** Either stay on v3.4.1, OR file an upstream issue and wait for v3.7.1+.

### 7. PhenoObservability + PhenoProc cargo-deny enrollment

- **Status:** PARTIAL — PhenoObservability enrolled upstream (no action needed); PhenoProc gated on item #3.
- **What's blocked:** PhenoProc cargo-deny enrollment cannot proceed until the dirty-tree resolution in item #3 lands.
- **What user needs to do:** Resolve item #3; enrollment then proceeds autonomously.
