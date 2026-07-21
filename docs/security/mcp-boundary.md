---
title: MCP Security Boundary Policies
status: AUTHORITATIVE
domain: security
effective_date: 2026-06-18
audience: coding-agents (forge, codex, claude) + humans
supersedes: ad-hoc MCP security guidance in McpKit/docs/SSOT.md and McpKit/SECURITY.md
replaced_by: null
see_also:
  - ../../../POLICY.md
  - ../../../GOVERNANCE_INDEX.md
  - ../../../governance/org-strategy/org-product-doctrine.md
  - https://github.com/KooshaPari/McpKit
  - https://github.com/KooshaPari/PhenoMCP
  - https://github.com/KooshaPari/phenotype-ops-mcp
  - ADR-001 (transport-layer decisions: SSE vs stdio)
  - ADR-017 (MCP polyrepo / framework-vs-runtime boundaries)
  - phenokits-commons #3 (governance templates)
---

# MCP Security Boundary Policies

This document consolidates the Model Context Protocol (MCP) security patterns
that were first articulated inside `KooshaPari/McpKit` (`docs/SSOT.md`,
`SECURITY.md`) and lifts them into org-level governance so every MCP server,
client, and gateway in the Phenotype fleet inherits the same boundary
contract. It is **ENFORCEMENT**-class policy per the 4-role spine in
[`POLICY.md`](../../../POLICY.md).

Authority order when guidance conflicts:

1. The latest `effective_date:` field in this repo's `governance/` or
   `docs/security/` tree (whichever is later).
2. The 4-role spine and product doctrine
   ([`governance/org-strategy/org-product-doctrine.md`](../../../governance/org-strategy/org-product-doctrine.md)).
3. ADR-017 (MCP polyrepo boundaries) and ADR-001 (transport-layer decisions).

If a sibling repo's MCP implementation disagrees with this file, raise the
conflict in the PR per doctrine §8 — do not silently pick a side.

---

## 1. Scope and threat model

An MCP server in the Phenotype fleet exposes tools, resources, and prompts
that an LLM agent can invoke. The security boundary is the surface between
the **LLM-driven agent runtime** and the **MCP server process** (and from
there, the underlying capability: filesystem, git, browser, internal API,
etc.). The boundary is crossed in three places, each with its own policy:

| Crossing | What crosses it | Why it is dangerous |
|----------|-----------------|---------------------|
| Transport | JSON-RPC frames over SSE, stdio, or HTTP | Eavesdropping, replay, MITM, message smuggling |
| Schema | Tool input/output JSON Schema | Schema-confusion, prototype pollution, oversized payloads |
| Session | Session-id-bearing requests | Cross-session leakage, session fixation, replay |

Threat actors considered: malicious tool output (prompt-injection that
escapes the tool sandbox), compromised agent runtime, network attacker on
local-but-shared transport (e.g. a dev box running multiple MCP servers),
and a malicious or compromised downstream capability (filesystem path
traversal, SSRF via a fetch tool, etc.).

Non-goals: this file does **not** define prompt-injection defenses for the
LLM itself — that is a separate layer. MCP boundaries stop the blast radius
of a compromised tool call; they do not make the agent trustworthy.

---

## 2. Transport security (per ADR-001)

ADR-001 decides transport per deployment shape. The security-relevant
contract is:

### stdio transport (per-process)

- **Use when:** the MCP server runs as a child process spawned by the agent
  runtime on the same host. This is the default for `McpKit`, `PhenoMCP`,
  and `phenotype-ops-mcp` when launched by a local coding agent.
- **Security contract:**
  - Process is single-tenant; no auth header is possible because there is no
    network.
  - Trust is established by **parent-child process lineage** (PID, argv
    inspection at startup), not by tokens.
  - The server **must refuse** to bind any TCP listener unless explicitly
    configured (`MCP_LISTEN_TCP=1`). Default-deny.
  - stdin/stdout are the only channels; the server must not log to stdout
    in production (corrupts the JSON-RPC stream) — log to stderr or a
    structured sink.
- **Forbidden:** binding 0.0.0.0, accepting connections from non-parent
  PIDs, or accepting stdio from a process whose argv does not match the
  expected agent binary allowlist.

### SSE / streamable-HTTP transport (network)

- **Use when:** the MCP server is remote (container, VM, shared dev host)
  or when multiple agent runtimes need to share one server. This is the
  default for `phenotype-ops-mcp` when it fronts shared org tooling.
- **Security contract (mandatory):**
  - TLS 1.2+ (TLS 1.3 preferred). No plaintext HTTP on any non-loopback
    interface. Localhost HTTP is permitted **only** when the listener is
    bound to `127.0.0.1` and the org's local-allowlist convention is in
    effect; document the deviation in the repo's SECURITY.md.
  - Origin / `Host` header validation against an explicit allowlist; reject
    anything else with `403`. This blocks DNS-rebinding attacks against a
    browser-resident agent.
  - SSE endpoint must enforce `Content-Type: text/event-stream` and reject
    any request that attempts to negotiate a different content type for
    the same path.
  - Reverse-proxy headers (`X-Forwarded-For`, `X-Forwarded-Proto`) are
    honored **only** when the proxy is in the org's allowlist; otherwise
    they are stripped and the request is treated as direct.
  - Rate limiting: per-IP and per-session. Burst budget documented in the
    server's README.
- **Forbidden:** wildcard CORS, `Access-Control-Allow-Origin: *` on
  authenticated endpoints, self-signed certs in any non-dev environment,
  exposing the SSE endpoint without authentication (see §4).

### Transport selection rule

Default to stdio when the agent and server are co-located. Promote to
SSE/HTTP only when (a) multiple runtimes share the server, or (b) the
server must outlive the agent process (long-lived stateful workflows). A
"transient" remote server is an anti-pattern — if it is remote, give it
real auth, TLS, and observability. The McpKit `docs/SSOT.md` transport
matrix is the authoritative reference.

---

## 3. Schema validation (the schema boundary)

Every MCP tool **must** declare a JSON Schema for its input and output.
This is not a docs convention — it is the **schema boundary** that
prevents the next two classes of attack:

1. **Schema confusion:** the LLM emits a payload that the server happily
   accepts because the server does not validate. Fix: strict-mode
   validation (additionalProperties: false, no `any`-equivalent types).
2. **Payload-size DoS:** the LLM emits a 50 MB string and the server
   streams it to a downstream capability. Fix: explicit `maxLength`,
   `maxItems`, `maxProperties` on every field.

Mandatory schema rules:

- **Strict by default.** `additionalProperties: false` on every object;
  `required` lists the full key set; no implicit-accept of unknown keys.
- **Bounded sizes.** Every string has `maxLength`; every array has
  `maxItems`; every object has `maxProperties`. Numbers carry
  `minimum`/`maximum`/`multipleOf` where meaningful.
- **No `oneOf` ambiguity.** A `oneOf` schema that accepts every payload
  is a validation hole. When using `oneOf`, include a discriminator
  property and reject schemas that match more than one branch.
- **Schema is the contract.** A tool whose runtime accepts a superset of
  its declared schema is a defect, not a feature — surface the drift in a
  PR titled `fix(mcp): align tool input schema with runtime validation`.
- **Versioning.** A breaking schema change is a **major** version bump on
  the MCP server crate / package; clients pinning to the old schema must
  fail loudly (not silently coerce).

The `McpKit` schema-validation crate (`mcp-schema` in the Rust workspace)
is the reference implementation. New MCP servers in the org should
depend on it or replicate its rules verbatim.

---

## 4. Authentication patterns

MCP has no native auth layer; the org fills the gap with the following
contract, lifted from `McpKit/SECURITY.md` and the SSE/HTTP transport
section above.

### Tier A — stdio (no auth header possible)

- Trust = parent-process lineage. The server inspects its parent PID at
  startup and refuses to start if the parent is not on the org's
  MCP-runtime allowlist (`codex`, `claude`, `forge`, `phenotype-*` agent
  binaries).
- Session continuity is per-process. There is no session id to forge.
- Any additional capability (filesystem root, network egress) is granted
  to the process at spawn time via the parent; the server does not
  re-grant.

### Tier B — SSE / HTTP (auth required)

Pick exactly **one** of the following auth shapes per server; do not
mix:

| Shape | When to use | Token source | Rotation |
|-------|-------------|--------------|----------|
| **Bearer JWT** | Multi-tenant org servers (`phenotype-ops-mcp`, shared cloud deployments) | Org identity provider; signed with org JWKS | Short-lived (≤1h) access tokens; refresh via org IdP |
| **mTLS** | High-trust internal mesh (PhenoMCP ↔ phenotype-ops-mcp) | Per-workload cert from org CA | Cert lifetime ≤24h; rotation automated |
| **Static API key** | Dev / staging only | Org secrets manager, env-injected at runtime | Manual rotation; **never** in-repo |

Rules:

- **No `?token=` query-string auth.** Tokens go in `Authorization: Bearer`
  (HTTP) or in a header on the SSE handshake. Query strings leak into
  access logs.
- **No auth on the same listener as health/metrics.** Health endpoints
  bind to a separate port or path with no auth; metrics require
  scrape-token auth (Prometheus bearer or mTLS).
- **Session management:** after auth, the server issues an opaque session
  id bound to (subject, client fingerprint, transport). The session id
  is a credential — treat it like a token (do not log it, do not put it
  in URLs, rotate on privilege escalation).
- **Replay defense:** every authenticated request carries a nonce or
  timestamp window; the server rejects replays outside the window.

### Tier C — shared dev hosts

If multiple humans share a dev box and each runs an MCP server, each
server picks a non-default port and binds to `127.0.0.1` only. The org
provides a port-allocation registry (`phenotype-infra/mcp-ports.json`,
TBD) so collisions are detected at agent startup, not at runtime.

---

## 5. Framework / runtime boundary (per ADR-017)

ADR-017 splits MCP into two surfaces:

- **Framework surface** — the SDK that defines the JSON-RPC server, tool
  registry, schema validation, and session manager. Lives in
  `McpKit` (Rust), `phenotype-ops-mcp` (Python), and `fastmcp`-derived
  libraries.
- **Runtime surface** — the concrete tool implementations (filesystem,
  git, browser, internal API adapters). Lives in `PhenoMCP`,
  `phenotype-ops-mcp/tools/*`, and per-product MCP packages.

The boundary rule:

- **Framework code never imports runtime tools directly.** The framework
  exposes a `Tool` trait / interface; runtime tools implement it. This
  prevents a runtime-tool bug from leaking into the framework and
  silently affecting every MCP server that depends on it.
- **Runtime tools never call framework internals.** A tool that reaches
  into the JSON-RPC dispatcher or the session store is a layering
  violation — surface it as a refactor candidate.
- **Shared types** (tool-id, error-envelope, request-id) live in a
  dedicated crate/package per language and are depended on by both
  surfaces. They do **not** live in the framework crate.

When reviewing an MCP-related PR, the first question is: "does this PR
cross the framework/runtime boundary?" If yes, split the PR or surface
the violation in the description.

---

## 6. Reusable workflow surface

Per doctrine §10, ENFORCEMENT lives in this repo. The org expects the
following reusable artifacts to be added (tracked as separate work;
this file documents the policy, not the workflow itself):

- `deny.toml` baseline extended with an MCP-specific advisory section
  (crates: `mcp-schema`, `fastmcp`, `mcp-server`).
- `scripts/mcp-conventions-lint.sh` — checks that every repo under
  `phenotype-ops-mcp/`, `McpKit/`, and `PhenoMCP/` has a `SECURITY.md`
  that references this file and a declared transport tier.
- `.github/workflows/reusable-mcp-security.yml` — runs the lint plus a
  smoke test that boots each MCP server on stdio and asserts the schema
  strictness flag is set.

These are out of scope for this document but are listed so reviewers
know the policy is meant to be **checkable**, not aspirational.

---

## 7. Required actions for new MCP servers

A new MCP server (any language) in the Phenotype fleet must, before
merging:

1. Declare its transport tier (A stdio, B HTTP/SSE, or C shared-dev) in
   the repo's README and SECURITY.md.
2. Reference this file by URL in SECURITY.md and link the specific
   subsections it implements.
3. Ship a JSON Schema for every tool with `additionalProperties: false`
   and explicit size bounds (§3).
4. Configure auth per §4; no plaintext HTTP listener on a non-loopback
   interface.
5. Pass `scripts/mcp-conventions-lint.sh` (once shipped) in CI.
6. Add an entry to `phenotype-registry/ECOSYSTEM_MAP.md` if it is a new
   canonical MCP server — do not let MCP servers drift outside the
   registry.

A PR that introduces an MCP server without satisfying 1–4 will be
blocked by the conventions-lint gate once the MCP lint is added.

---

## 8. References

- `KooshaPari/McpKit/docs/SSOT.md` — transport matrix, schema rules.
- `KooshaPari/McpKit/SECURITY.md` — standard policy template that
  derived this file.
- ADR-001 — transport-layer decisions (SSE vs stdio). **Authority** for
  §2.
- ADR-017 — MCP polyrepo boundaries. **Authority** for §5.
- [`governance/org-strategy/org-product-doctrine.md`](../../../governance/org-strategy/org-product-doctrine.md) — 4-role spine, naming,
  registry pattern, conflict-surfacing rules.
- phenokits-commons #3 — governance templates; this file is the MCP
  specialization of that template.
- [`POLICY.md`](../../../POLICY.md) — ENFORCEMENT-surface role of this repo.

---

## 9. Refresh cadence

- This document is enforced from its `effective_date`.
- Quarterly review: re-read ADR-017 and the McpKit `docs/SSOT.md` for
  drift. Sync any rule changes back to McpKit first, then update this
  file in the same PR.
- Override mechanism: per doctrine §8, an override is recorded under
  `governance/overrides/<date>-<repo>-<rule>.md`. An unrecorded override
  is treated as a violation.