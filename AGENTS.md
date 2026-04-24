# phenotype-org-audits — AGENTS.md

Automation and agent instructions for audit repository.

## Quarterly Audit Automation

**Trigger**: GitHub Actions cron `0 14 1 1,4,7,10 *` (1st of month, 9am ET)

**Agent**: `quarterly-audit-agent` (Rust-based aggregator)

**Flow**:
1. Clone all active Phenotype org repos (from REPOS_MANIFEST.txt)
2. Run aggregator on each repo (LOC, test stats, governance coverage)
3. Generate INDEX.md, STATUS_AT_<date>.md, SYSTEMIC_ISSUES.md
4. Commit to `audits/<YYYY-MM-DD>/` branch
5. Open PR to main with quarterly findings

**Inputs**:
- `REPOS_MANIFEST.txt` (list of repos to audit)
- `aggregator` binary (from phenotype-tooling)
- `audit-schema.toml` (aggregator config)

**Outputs**:
- `audits/<YYYY-MM-DD>/INDEX.md`
- `audits/<YYYY-MM-DD>/STATUS_AT_<date>.md`
- `audits/<YYYY-MM-DD>/SYSTEMIC_ISSUES.md`
- `audits/<YYYY-MM-DD>/full_dep_matrix.md`
- `audits/<YYYY-MM-DD>/governance_adoption.md`
- `audits/<YYYY-MM-DD>/fr_scaffolding.md`

## Worklog Aggregation

**Trigger**: Manual or scheduled (monthly)

**Agent**: `worklog-aggregator-agent` (shell wrapper → Rust aggregator)

**Purpose**: Pull cross-repo worklogs into `worklogs/` for longitudinal tracking

**Script**: `tooling/worklog-aggregator.sh`

## Data Retention Cleanup

**Trigger**: Manual or scheduled (quarterly, after audit completes)

**Agent**: `audit-archiver-agent`

**Policy**:
- Keep current + 3 prior quarters in `audits/` (detailed)
- Archive older than 1 year to `.archive/<YYYY>/`
- Delete `.archive/` entries older than 3 years

**Script** (TBD): `tooling/archive-old-audits.sh`

## Manual Audit (Ad-Hoc)

Run aggregator directly:

```bash
cd /Users/kooshapari/CodeProjects/Phenotype/repos/phenotype-tooling
./aggregator \
  --repos-manifest /path/to/repos.txt \
  --output-dir ../phenotype-org-audits/audits/$(date +%Y-%m-%d) \
  --schema audit-schema.toml
```

Then commit:

```bash
cd /Users/kooshapari/CodeProjects/Phenotype/repos/phenotype-org-audits
git add audits/$(date +%Y-%m-%d)/
git commit -m "audit: snapshot as of $(date +%Y-%m-%d)"
```

## Notification & Escalation

On audit completion:
- Systemic issues with impact >10 repos → escalate to AgilePlus as eco-NNN spec
- Governance gaps (e.g., <50% CLAUDE.md coverage) → flag in GOVERNANCE.md
- Test traceability <80% → create unblocking task in AgilePlus

## Related Agents

- `phenotype-tooling-aggregator` — core audit logic (maintained in phenotype-tooling)
- `worklog-aggregator` — cross-repo worklog pull (maintained in worklogs/)
- `quarterly-version-alignment-wave` — launched after audit, updates deps based on snapshot

## Testing

All audit scripts must:
- Exit with error if input repos don't exist or are missing CLAUDE.md
- Generate valid markdown (no syntax errors, UTF-8 encoding)
- Produce consistent output (deterministic sort order, timestamps)
- Validate count totals (LOC, test count, repo count)

Test on dry run before merging:

```bash
./aggregator --dry-run --repos-manifest test-repos.txt
```
