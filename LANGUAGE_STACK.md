# Language Stack — Core, Edges, and Deferred Work

> **Status:** Org-wide default for *where code should live*. Complements
> `BOUNDARY_OWNERS.md` (capability boundaries) and `ECOSYSTEM_MAP.md` (repo index).
>
> **Principle:** Maximize **Rust / Zig / Mojo** in the core. Place **Go** only with
> written justification. Use **edge languages** strictly for interfacing, thin facades,
> or cases where re-implementing a large foreign surface in the core stack is not
> worthwhile. Do not park large feature chunks in worse-fit languages.

---

## Tier 1 — Core (preferred)

| Language | Role | Typical boundaries |
|----------|------|------------------|
| **Rust** | Primary systems core | Agent runtime (`Agentora`), observability (`PhenoObservability`), auth (`Authvault`), data paths, MCP server binaries, routing substrate (`Tokn`), most `phenotype-*` crates |
| **Zig** | Core where C ABI / no runtime / explicit alloc wins | FFI bridges, hot paths, tooling kernels (evaluate per crate; no blanket Zig repos) |
| **Mojo** | Numeric / GPU-adjacent core experiments | Only when Rust/Zig cannot meet perf target *and* Mojo ownership is justified in an ADR |

**Target:** `phenotype-rust-sdk` (and future zig/mojo siblings) hold **optional domain modules**;
HexaKit holds **templates** that scaffold Tier-1 layouts — not a lib warehouse.

---

## Tier 2 — Go (justified edges only)

Go is allowed when **all** of the following are true:

1. ADR or boundary doc names the consumer (e.g. existing microservice fleet, K8s operator ecosystem).
2. The feature is an **edge** (daemon, sidecar, gRPC gateway) — not a second canonical implementation of Rust-owned logic.
3. A path to thin-wrapper-over-Rust (FFI, gRPC to core) is documented or in flight.

| Allowed | Not allowed |
|---------|-------------|
| `phenotype-go-sdk`, `PhenoMCP/go`, PlatformKit devenv edges | Duplicate auth/observability/resilience **business logic** in Go |
| Infra CLIs already committed to Go (`BytePort` if kept) | New “kit monorepo” domains without Rust canonical crate |

---

## Tier 3 — Edge / interfacing (thin facades)

Use only at **boundaries** — HTTP/CLI UX, enterprise interop, agent ergonomics — not for core algorithms.

| Stack | Pin | Role |
|-------|-----|------|
| **Python 3.14 + uv** | `requires-python >= 3.14`, uv workspaces | `thegent`, `phenotype-python-sdk` packages, notebooks, ML glue, test/QA harnesses |
| **Bun + TypeScript 7 (preview)** | `packageManager: bun`, TS 7 preview where stable enough | `OmniRoute`, `Conft`, landings, dashboards, design tokens (`phenoDesign`) |
| **C# / Java** | LTS versions per product ADR | Enterprise adapters, JVM/.NET interop, **no** new canonical Phenotype domains |
| **Other** | Case-by-case ADR | FFI shims, vendor SDK wrappers, one-off microservices |

**Rule:** If a feature is >~500 LOC of non-trivial logic and not pure I/O glue, default to Tier 1.

---

## Deferred — “schizo tier” (last)

> **Do not rationalize, absorb, or expand these until every other active boundary
> in `BOUNDARY_OWNERS.md` is closed** — unless explicitly un-deferred by user sign-off.

| Repo | Status | Note |
|------|--------|------|
| **GDK** | Archived | **Skip in full.** General Development Kit / Rust monorepo experiment — no absorption, no unarchive, no boundary ownership work. |
| **hwLedger** | Active | Hardware ledger product — defer all merge/audit waves. |
| **FocalPoint** | Active | Dependency/focus tooling — **not** HexaKit policy merge until un-deferred; was slated for HexaKit absorption — **superseded by this deferral**. |
| **KaskMan** | Archived | KaskManager R&D platform — same bucket as GDK; pet project only after fleet complete. |

These repos may receive security patches if critical, but **no** ecosystem-map priority, gap ports, or delete/unarchive decisions until the deferral list is cleared.

---

## Decision checklist (new code)

```text
1. Can this live in Rust (or Zig/Mojo) as the canonical implementation? → Tier 1
2. Is this a thin facade over Tier 1? → Python / TS / C# / Java edge only
3. Is Go the only viable edge for this deployment shape? → ADR + Tier 2
4. Is the repo GDK | hwLedger | FocalPoint | KaskMan? → STOP (deferred tier)
```

---

## References

- `BOUNDARY_OWNERS.md` — capability owners (scaffold vs SDK vs workspace)
- `ECOSYSTEM_MAP.md` — repo roles (deferred repos tagged in §1.1)
- `docs/registries.md` — HexaKit scaffold role
