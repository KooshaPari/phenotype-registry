# Cross-Repo Duplicate Discovery — 2026-04-27

**Scope:** Local-only Rust duplicate-code audit under
`/Users/kooshapari/CodeProjects/Phenotype/repos`.

**Commands requested / run:**

```bash
find /Users/kooshapari/CodeProjects/Phenotype/repos -maxdepth 5 -name "*.rs" -not -path "*/target/*" -not -path "*/.archive/*" -not -path "*/.worktrees/*" 2>/dev/null > /tmp/all_rs.txt
wc -l /tmp/all_rs.txt
```

**Manifest result:** `3909 /tmp/all_rs.txt`

**Protocol inputs used:**

- `feedback_dead_dep_removal_pattern.md`: verify source-level use before
  recommending dependency bumps or shared-crate work. Zero real source use means
  remove or ignore, not extract.
- Phenotype Org Cross-Project Reuse Protocol: prefer extraction over duplicate
  local implementations, but log candidates with evidence and avoid treating
  docs or declarations as adoption.
- `shared-crates-canonical-home-adr-2026-04.md`: canonical home for shared Rust
  infrastructure crates is `phenoShared`.

## Top Rust Repos By Local LOC

The requested max-depth scan treats top-level directories as repos. That means
`*-wtrees` mirrors can appear as top repos even when they are not canonical
project homes.

| Rank | Repo dir | Rust LOC | Rust files |
|---:|---|---:|---:|
| 1 | `helios-cli` | 319,606 | 641 |
| 2 | `heliosCLI` | 194,907 | 469 |
| 3 | `FocalPoint` | 62,237 | 213 |
| 4 | `pheno` | 48,068 | 290 |
| 5 | `hwLedger` | 42,706 | 185 |
| 6 | `thegent` | 40,873 | 134 |
| 7 | `AgilePlus` | 38,550 | 210 |
| 8 | `KDesktopVirt-wtrees` | 35,923 | 52 |
| 9 | `KDesktopVirt` | 35,923 | 52 |
| 10 | `AgilePlus-wtrees` | 33,665 | 145 |

Sensitivity check excluding top-level `*-wtrees`: the first eight canonical-ish
entries remain `helios-cli`, `heliosCLI`, `FocalPoint`, `pheno`, `hwLedger`,
`thegent`, `AgilePlus`, `KDesktopVirt`; then `Tokn` and `PhenoProc` enter the
top ten.

## Signature Scan Summary

Method: for the top ten LOC directories, grep-equivalent scan for line-start
Rust function signatures matching `^fn ` and `^pub fn `, then grouped by
signature/name/repo spread. I also grouped line-start `impl ...` blocks and
approximate normalized function-body hashes to identify duplicate implementation
patterns.

| Signal | Cross-repo duplicate groups |
|---|---:|
| Exact `fn` / `pub fn` signatures | 1,736 |
| Function names | 1,732 |
| `impl` headers | 864 |
| Normalized function bodies | 1,213 |

High-count exact signature examples:

- `fn main()` appears 35 times across `FocalPoint`, `helios-cli`, `heliosCLI`,
  `hwLedger`, `pheno`, `thegent`.
- `fn main() -> Result<(), Box<dyn std::error::Error>>` appears 38 times across
  `AgilePlus`, `AgilePlus-wtrees`, `FocalPoint`, `pheno`, `thegent`.
- `fn main() -> Result<()>` appears 38 times across `FocalPoint`, `helios-cli`,
  `heliosCLI`, `hwLedger`, `thegent`.
- AgilePlus test contract helpers such as `fn api_url() -> String`,
  `fn api_key() -> String`, and `fn build_valid_audit_chain(...)` repeat across
  `pheno`, `AgilePlus`, and `AgilePlus-wtrees`, but these are mostly mirror
  copies or test fixtures, not shared-crate candidates.

## Top Duplication Candidates

### 1. Event Sourcing / Audit Event Core

**Evidence:**

- `pheno/crates/phenotype-event-sourcing/src/hash.rs:14` —
  `pub fn compute_hash(...)`
- `pheno/crates/agileplus-events/src/hash.rs:27` —
  `pub fn compute_hash(...)`
- `hwLedger/vendor/phenotype-event-sourcing/src/hash.rs:18` —
  `pub fn compute_hash(...)`
- `AgilePlus/crates/agileplus-events/src/hash.rs:27` —
  `pub fn compute_hash(...)`
- `FocalPoint/crates/focus-eval/src/lib.rs:524` —
  `impl InMemoryEventStore`
- `FocalPoint/crates/focus-eval/src/lib.rs:531` —
  `impl EventStore for InMemoryEventStore`
- `pheno/crates/phenotype-event-sourcing/src/memory.rs:28` —
  `impl InMemoryEventStore`
- `pheno/crates/phenotype-event-sourcing/src/memory.rs:65` —
  `impl EventStore for InMemoryEventStore`
- `hwLedger/vendor/phenotype-event-sourcing/src/memory.rs:36` and `:59` —
  same store pattern.

**Candidate extraction:** finish consolidation into
`phenoShared/crates/phenotype-event-sourcing`, then migrate product-specific
event crates to wrap the canonical store/hash/snapshot APIs rather than
vendoring or reimplementing them.

**Priority:** P0. This aligns directly with the accepted shared-crates ADR and
has both canonical-crate and vendored-copy evidence.

### 2. Health Monitor / Health Check Config

**Evidence:**

- `pheno/crates/phenotype-health/src/lib.rs:87` —
  `impl Default for HealthCheckConfig`
- `pheno/crates/phenotype-health/src/lib.rs:113` —
  `impl HealthMonitor`
- `pheno/crates/phenotype-health/src/lib.rs:181` —
  `impl Default for HealthMonitor`
- `pheno/libs/nexus/src/health.rs:32`, `:116`, `:183` — parallel Nexus copy.
- `thegent/libs/nexus/src/health.rs:32`, `:116`, `:183` — same Nexus copy.
- `AgilePlus/libs/nexus/src/health.rs:32`, `:116`, `:186` — same health
  monitor shape.
- `AgilePlus/libs/health-monitor/src/monitor.rs:23` —
  separate `impl HealthMonitor`.
- `KDesktopVirt/src/containerization.rs:928` —
  another `impl HealthMonitor`.

**Candidate extraction:** promote a single `phenotype-health` API in
`phenoShared` and migrate `nexus` copies plus local container health monitors to
consume it. Keep product-specific probes as adapters.

**Priority:** P0/P1. This is the broadest non-test implementation duplicate in
the scan.

### 3. Rate Limiting / Token Bucket Infrastructure

**Evidence:**

- `pheno/crates/phenotype-infrastructure/src/rate_limit.rs:36` —
  `impl TokenBucket`
- `pheno/crates/phenotype-infrastructure/src/rate_limit.rs:92` —
  `impl RateLimiter`
- `pheno/agileplus/crates/agileplus-cache/src/limiter.rs:16` —
  `impl RateLimiter`
- `AgilePlus/crates/agileplus-cache/src/limiter.rs:16` —
  `impl RateLimiter`
- `AgilePlus/crates/agileplus-plane/src/client/rate_limit.rs:11` —
  `impl TokenBucket`
- `AgilePlus/crates/agileplus-github/src/client.rs:31` —
  `impl TokenBucket`
- `FocalPoint/crates/focus-webhook-server/src/rate_limit.rs:15` and `:50` —
  token bucket plus limiter wrapper.
- `FocalPoint/services/graphql-gateway/src/rate_limit.rs:19` and
  `FocalPoint/services/templates-registry/src/ratelimit.rs:24` —
  local limiter copies.
- `heliosCLI/crates/harness_scaling/src/lib.rs:271` —
  `impl TokenBucket`.

**Candidate extraction:** `phenotype-rate-limit` or a promoted
`phenoShared` limiter crate with small sync/async adapters. The extraction
should include clock injection and endpoint/client-key policy hooks.

**Priority:** P1. Many copies are small, but they implement the same production
control primitive.

### 4. Circuit Breaker / Resilience Primitive

**Evidence:**

- `pheno/crates/phenotype-infrastructure/src/circuit.rs:56` —
  `impl CircuitBreaker`
- `heliosCLI/crates/harness_scaling/src/lib.rs:188` —
  `impl CircuitBreaker`
- `thegent/crates/thegent-runtime/src/main.rs:25` —
  `impl CircuitBreaker`
- `thegent/crates/thegent-memory/src/client.rs:27` —
  `impl CircuitBreaker`

**Candidate extraction:** shared `phenotype-resilience` primitive with failure
window, recovery delay, and state-transition telemetry. Keep consumer-specific
error classifiers at call sites.

**Priority:** P1/P2. Lower LOC than health/rate limit, but the semantic risk of
divergent resilience behavior is high.

### 5. Repository Root / Canonical JSON Utilities

**Evidence:**

- `helios-cli/codex-rs/core/src/external_agent_config.rs:442` —
  `fn find_repo_root(cwd: Option<&Path>) -> io::Result<Option<PathBuf>>`
- `heliosCLI/codex-rs/core/src/external_agent_config.rs:316` —
  same signature.
- `FocalPoint/tooling/fr-coverage/src/main.rs:68` and
  `FocalPoint/tooling/release-cut/src/main.rs:93` —
  `fn find_repo_root() -> Result<PathBuf>`
- `hwLedger/tools/run-journeys/src/main.rs:194` —
  `fn find_repo_root() -> Result<PathBuf>`
- `helios-cli/codex-rs/config/src/fingerprint.rs:51` and
  `heliosCLI/codex-rs/config/src/fingerprint.rs:51` —
  `fn canonical_json(value: &JsonValue) -> JsonValue`
- `hwLedger/crates/hwledger-attest/src/lib.rs:119` —
  `pub fn canonical_json(v: &serde_json::Value) -> String`
- `FocalPoint/crates/focus-ir/src/lib.rs:672` —
  `fn canonical_json(doc: &Document) -> Result<String, IrError>`

**Candidate extraction:** split into two candidates:

1. `phenotype-repo-root` for upward `.git`/workspace discovery.
2. `phenotype-canonical-json` for stable JSON ordering and fingerprint inputs.

**Priority:** P2. These are small utilities, but they are good starter
extractions because interfaces are narrow and testable.

## Non-Candidates / Discounted Signals

- `helios-cli` vs `heliosCLI` duplicates are mostly fork/mirror lineage. Treat
  as repo-consolidation or rename cleanup, not shared-crate extraction.
- `KDesktopVirt` vs `KDesktopVirt-wtrees` is a worktree mirror. Do not extract
  from that signal alone.
- `AgilePlus` vs `AgilePlus-wtrees` and nested `pheno/agileplus` duplicates are
  mostly workspace/worktree mirrors. Use them as evidence only when the same
  implementation also appears in a distinct product repo.
- `fn main*` signatures are mostly binary/test entrypoints. They are useful for
  volume sanity but not for shared crates.
- Test fixture duplicates in `tests/contracts`, `tests/bdd`, and
  `tests/fixtures` should be cleaned with fixture consolidation inside the owning
  repo first, not extracted into org crates.

## Recommended Next Actions

1. Start with `phenotype-event-sourcing`: it already has an accepted canonical
   home decision and concrete duplicates in `pheno`, `AgilePlus`, `hwLedger`,
   and `FocalPoint`.
2. Add a focused `phenotype-health` migration spec for Nexus/health monitor
   copies across `pheno`, `thegent`, `AgilePlus`, and `KDesktopVirt`.
3. Open a scoped rate-limiter extraction spec after checking real imports in
   each candidate repo, following the dead-dep rule before adding dependencies.
4. Keep circuit breaker and utility extractions as small P2 follow-ups once the
   larger state/health/rate-limit work is moving.

## Evidence Artifacts

- Rust file manifest: `/tmp/all_rs.txt`
- Generated duplicate-analysis scratch artifact:
  `/tmp/rust_dup_analysis.json`
