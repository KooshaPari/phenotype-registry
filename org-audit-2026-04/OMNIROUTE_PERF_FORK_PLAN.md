# OmniRoute High-Performance Fork — Plan

**Date:** 2026-04-30
**Status:** DRAFT — awaiting user approval
**Task:** #198

---

## Context

OmniRoute is a TypeScript/Next.js AI gateway proxy (~104K LOC across the app + open-sse sub-package). It handles:
- Multi-provider LLM routing (OpenAI, Claude, Gemini, custom backends)
- JWT auth + API key management
- Quota caching, circuit breakers, fallback policies
- SSE/streaming with format translation
- Token health checks, usage analytics, semantic cache

**User directive:** General overhaul fork for high performance. Likely Go or Rust rewrite.

---

## Current Architecture Assessment

### Stack
- **Runtime:** Node.js 22 (Next.js 14 app router, TypeScript)
- **Sub-packages:** `@omniroute/open-sse` (local npm workspace)
- **Storage:** SQLite (`better-sqlite3`) for settings/quota
- **Proxy:** Native `fetch` + `jose` for JWT
- **Total LOC:** ~104,440 lines (app) + ~104K more in sub-packages

### Performance-Critical Paths

| File | LOC | Role | Bottleneck Risk |
|---|---|---|---|
| `proxy.ts` | 169 | Middleware (auth, body guard, drain) | Medium |
| `sse/handlers/chat.ts` | 895 | Main SSE/streaming handler | **HIGH** — SSE streaming hot path |
| `domain/quotaCache.ts` | 416 | Quota tracking per model/provider | **HIGH** — in-memory map, no TTL |
| `lib/cloudflaredTunnel.ts` | 748 | Cloudflared tunnel management | Medium |
| `lib/pricingSync.ts` | 397 | Pricing sync | Low |
| `lib/semanticCache.ts` | 386 | Response caching | Medium |
| `lib/tokenHealthCheck.ts` | 311 | Token validation | Medium |
| `lib/usageAnalytics.ts` | 322 | Usage logging | Low |
| `domain/degradation.ts` | 253 | Degradation rules | Low |
| `domain/costRules.ts` | 228 | Cost calculation | Low |

### Key Hot Path (chat.ts handler)
1. **Parse body + telemetry start**
2. **Input sanitization** (prompt injection guard)
3. **Auth extraction** (API key, provider creds)
4. **Model resolution** (getComboForModel)
5. **Task-aware routing** (applyTaskAwareRouting)
6. **Format detection** (detectFormatFromEndpoint)
7. **Circuit breaker check** (getCircuitBreaker)
8. **Quota check** (markAccountExhaustedFrom429)
9. **handleChatCore** — upstream LLM call
10. **Token refresh** (checkAndRefreshToken)
11. **Telemetry record** (recordTelemetry)
12. **Compliance log** (logAuditEvent)

Each hop adds latency. Node.js single-threaded for sync work, but all I/O is async — main gains come from:
- Reducing sync JS work per request
- Avoiding unnecessary await chains
- Moving stateful hot-path logic (quota, circuit) to shared memory or fast DB
- Parallelizing independent checks

---

## Rewrite Options

### Option A: Go Rewrite (RECOMMENDED)
**Language:** Go 1.23+
**Why:** Best fit for high-concurrency network proxy with minimal GC pressure.

| Component | Go Pattern | Benefit |
|---|---|---|
| SSE/streaming | goroutines + `net/http` + `httputil.ReverseProxy` | 1 goroutine per request, no Node.js event loop overhead |
| Quota cache | `sync.Map` + TTL map (e.g. `github.com/patrickmn/go-cache`) | Sub-microsecond in-memory reads |
| Circuit breaker | `sony/gobreaker` | Battle-tested, minimal allocations |
| Auth/JWT | `golang-jwt/jwt/v5` + `jose` compat | Faster crypto ops |
| SQLite | `mattn/go-sqlite3` | CGO but extremely fast; or use BadgerDB for pure Go |
| Format translation | Go port of `open-sse` translator | ~10x throughput vs TS |
| Concurrent proxy | Worker pool with `errgroup` | Bound concurrency, backpressure |
| Config/DB | Viper + SQLite or Badger | Hot reload without restart |

**Estimated LOC:** ~15-20K Go (vs 104K TS) — leaner core, same features.
**Performance target:** 3-10x throughput, <1ms P99 latency on hot path.

**Risks:** Go rewrite of `open-sse` translator (~50K LOC of format detection/translation) is significant. Recommend a **hybrid approach**.

### Option B: Rust Rewrite (HIGH RISK)
**Language:** Rust with `hyper` + `axum`
**Why:** Maximum performance, memory safety.

| Component | Rust Crate | Benefit |
|---|---|---|
| HTTP server | `hyper` + `axum` | Async, zero-cost abstractions |
| SSE streaming | `tokio` + `futures` stream | True async streaming |
| Quota cache | `dashmap` + `ttl_cache` | Lock-free concurrent map |
| JWT | `jsonwebtoken` | Fast crypto |
| Circuit breaker | `polaro` or custom | Compile-time safety |
| Format translation | Port TS `open-sse` | Significant effort |

**Estimated LOC:** ~8-12K Rust (vs 104K TS)
**Performance target:** 10-20x throughput vs Node.js
**Risks:**
- `open-sse` translator port is 50K+ LOC of complex logic (model parsing, provider format detection)
- Rust async ecosystem less mature than Go for HTTP proxy use cases
- Longer time-to-production (weeks vs days for Go)
- Team's Rust expertise is in the Phenotype ecosystem (Rust projects), not OmniRoute

### Option C: Go Core + TS Frontend (HYBRID — RECOMMENDED ALTERNATIVE)
**Architecture:**
- **Go proxy core** (rewritten in Go): hot path (SSE chat, format translation, auth, quota, circuit breaker)
- **Next.js frontend** stays: dashboard, settings, onboarding UI (unchanged)
- **IPC:** Unix domain socket or localhost HTTP between Go core and Next.js
- **Shared config:** SQLite (Go writes, TS reads) or config file

| Layer | Language | Scope |
|---|---|---|
| Gateway proxy | **Go** | `/api/v1/*` SSE, auth, quota, routing, format translation |
| Dashboard UI | **TypeScript/Next.js** | `/dashboard/*`, settings, onboarding |
| Config layer | **Go + SQLite** | Shared via file lock or IPC |

**Estimated LOC:** ~8K Go (proxy core) + 104K TS (frontend, unchanged)
**Performance target:** 5-8x throughput on hot path; gradual migration; frontend unchanged.
**Risk:** Low — can migrate incrementally, hot path first.

---

## Recommended Approach: Option C (Go Core + TS Frontend)

### Migration Phases

#### Phase 1: Extract and Measure (Week 1)
1. **Benchmark current OmniRoute hot path** — capture baseline P50/P95/P99 latency + RPS
2. **Identify exact slowdowns** — instrument `chat.ts` with timing breaks
3. **Define API contract** — document `/api/v1/chat/completions`, `/api/v1/embeddings`, etc. as stable interfaces
4. **Set success metrics** — e.g. P99 <50ms (from current ~200ms), 5x RPS

#### Phase 2: Go Proxy Core (Weeks 2-4)
**Target modules to rewrite in Go:**

1. **Auth middleware** (JWT verify, API key extract) — `proxy.ts` lines 40-75
2. **Chat handler** (`sse/handlers/chat.ts`) — full hot path
3. **Format translator** — port of `open-sse/services/provider.ts` + `open-sse/services/model.ts`
4. **Quota cache** — `domain/quotaCache.ts` (416 LOC) — use `go-cache` or `ttlcache`
5. **Circuit breaker** — `shared/utils/circuitBreaker.ts` — use `gobreaker`
6. **Model availability** — `domain/modelAvailability.ts` — simple in-memory map
7. **Fallback policy** — `domain/fallbackPolicy.ts` — stateless routing rules
8. **Token refresh** — `services/tokenRefresh.ts`

**Go modules:**
```
proxy-core/
  cmd/server/main.go       # Entry point
  internal/
    auth/                  # JWT verify, API key
    chat/                  # Chat completions handler
    proxy/                 # Reverse proxy + format translation
    quota/                 # Quota cache + tracking
    circuit/               # Circuit breaker
    fallback/              # Fallback routing
    translate/             # Format translation (OpenAI↔Claude↔Gemini)
    model/                 # Model parsing + combo resolution
    token/                 # Token refresh
  pkg/
    types/                 # Shared types (match Next.js API contracts)
    db/                    # SQLite or Badger for state
```

#### Phase 3: Coexist + Smoke Test (Week 5)
1. Deploy Go proxy on `:20129` alongside Node.js on `:20128`
2. Traffic split: 10% → Go, 90% → Node.js
3. Compare latency, error rates, throughput
4. Fix divergences

#### Phase 4: Full Cutover (Week 6)
1. Point all traffic to Go proxy
2. Keep Next.js for dashboard only (can be separate deployment)
3. Monitor for 1 week, then archive old TS proxy code

---

## Fork Location

**Proposed:** `https://github.com/KooshaPari/omniroute-core`
(Or use `omniroute-gateway`, `omniroute-proxy`, etc. — user to decide)

All work in the fork, not the upstream npm package.

---

## Immediate Next Steps

1. **Benchmark current hot path** — run a load test against localhost OmniRoute to capture baseline metrics before any rewrite work begins.
2. **User decision:** Go or Rust? (This plan recommends Go for speed-to-market, Rust for max performance.)
3. **Create fork repo** and push initial Go skeleton.
4. **Port auth middleware first** — it's self-contained and measurable.

---

## Open Questions

1. **Go or Rust?** User preference determines the stack.
2. **Keep Next.js dashboard?** If yes, Go core serves at separate port. If not, rewrite the dashboard in Go/HTMX or a lightweight framework.
3. **Database:** SQLite (Go native via mattn/go-sqlite3) or migrate to BadgerDB (pure Go, no CGO)?
4. **Feature freeze?** Should new OmniRoute features land in the old TS codebase during the rewrite, or should all development pause until the fork is stable?
5. **Test migration:** E2E tests in `app/tests/e2e/` — port to Go or keep as TypeScript contract tests that hit the Go proxy?

---

## Appendix: Current OmniRoute LOC Breakdown

| Package | LOC |
|---|---|
| app/src (all) | ~104,440 |
| open-sse (sub-package) | ~104,000+ |
| **Total** | **~208,000+** |

Hot-path files (<1000 LOC each, easily portable):
- `sse/handlers/chat.ts` — 895 LOC
- `domain/quotaCache.ts` — 416 LOC
- `domain/configAudit.ts` — 285 LOC
- `lib/cloudflaredTunnel.ts` — 748 LOC (likely NOT in hot path)
- `lib/tokenHealthCheck.ts` — 311 LOC
- `lib/semanticCache.ts` — 386 LOC
- `lib/proxyHealth.ts` — 140 LOC

**Estimated hot-path rewrite:** ~3,000-5,000 LOC in Go (quota cache, circuit, auth, chat handler, format translation core).
