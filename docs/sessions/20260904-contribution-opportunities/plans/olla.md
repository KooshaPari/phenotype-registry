# Olla: five proposed contributions

Repository: https://github.com/thushan/olla. Evidence inspected September 5 UTC / September 4 Pacific: HEAD tree, body inspector source, issue bodies, [testing guide](https://github.com/thushan/olla/blob/main/docs/content/development/testing.md), [open issues/PRs](https://github.com/thushan/olla/issues?q=is%3Aopen), and [recent closed PRs](https://github.com/thushan/olla/pulls?q=is%3Apr+is%3Aclosed+sort%3Aupdated-desc). Source paths below exist in that tree. Reports are verified to exist; no defect was locally reproduced in this planning task. Refresh assignment/timeline and targeted PR searches before starting. Engineering estimates exclude review latency.

Shared validation: targeted package tests below, then `go test -race ./...` as documented by the repository. Use deterministic httptest backends, not paid services. Preserve both proxy engines and native provider paths. Open feature/design discussion for substantial changes. Maintainer openness is sampled evidence, not a promised acceptance rate. Occupied lanes excluded: #180 logging, #158 provider routing failure policy, #152 loaded-first balancing, #150 circuit-breaker cold start, #120 token metrics.

## OLLA-01: Reproduce and fix small-body model inspection failure

- Evidence: VERIFIED report [#220](https://github.com/thushan/olla/issues/220) describes roughly 60 KB requests intermittently missing model routing; reporter explicitly lacks an isolated Go reproduction. Inspected `internal/adapter/inspector/body_inspector.go` contains pooled small-body handling and a distinct large-body scan.
- Scope: reproduce in `internal/adapter/inspector/body_inspector_test.go`, then minimal inspector fix if demonstrated. Add routing integration assertion only as necessary. No blanket fallback policy or larger-body limit increase.
- Acceptance: concurrent requests, model at multiple key positions, body replay and unknown ContentLength preserve requested model and exact body; affected model reaches only its serving backend. Run `go test -race ./internal/adapter/inspector/...` and shared gate.
- Overlap: distinct from issue #127/PR #128 large requests; inspect merged hardening #212 before coding. First, 2-4 days; align sanitized reproduction with reporter. Value: direct OmniRoute routing correctness and a useful concurrency debugging case study.

## OLLA-02: Support rerank endpoint alias without changing native routes

- Evidence: VERIFIED feature request [#183](https://github.com/thushan/olla/issues/183) asks for `/olla/proxy/rerank` compatibility with `/reranking`.
- Scope: inspect route registration `internal/app/handlers/server_routes.go` and URL mapping `internal/adapter/proxy/common/url_builder.go`; add narrowly scoped alias plus existing corresponding tests. Do not rewrite arbitrary upstream URLs or impose one backend's spelling on every provider.
- Acceptance: agreed compatible provider receives the correct path and original method/body/query; native `/reranking` remains unchanged; unsupported provider returns explicit existing behavior; no alias recursion. Run `go test ./internal/app/handlers/... ./internal/adapter/proxy/common/...`, then shared gate.
- Overlap: no matching alias PR in sampled open set; refresh full rerank search. Second, independent, 1-2 days. Maintainer agreement required on which profiles expose the alias. Value: practical RAG client compatibility and a low-complexity first contribution.

## OLLA-03: Route generic OpenAI paths to nonstandard provider base paths

- Evidence: VERIFIED report [#162](https://github.com/thushan/olla/issues/162) documents Lemonade `/api/v1` and DMR `/engines/v1` compatibility/path gaps. Reporter offers to contribute; coordinate rather than duplicate their work.
- Scope: `internal/core/domain/routing.go`, `internal/adapter/proxy/common/url_builder.go`, matching `routing_test.go`/`url_builder_test.go`. Derive compatibility and path mapping from actual profile declarations after inspecting their schema. Preserve native routes and endpoint URL prefixes; no hardcoded global rewrite.
- Acceptance: generic chat requests reach both mocked base paths, standard `/v1` providers still work, native paths remain byte-equivalent, query/base prefixes are retained. Run `go test ./internal/core/domain/... ./internal/adapter/proxy/common/...`, then shared gate.
- Overlap: #161 already fixes Lemonade availability; #158 provider fail-close is occupied. Third, 3-4 days, independent of OLLA-02 but serialize shared URL edits. Ask owner/reporter for assignment and design agreement. Value: local inference interoperability directly applicable to Phenotype.

## OLLA-04: Preserve explicit vision capability for LM Studio models

- Evidence: VERIFIED report [#115](https://github.com/thushan/olla/issues/115): Qwen3-VL appears text-only in unified models. Root cause and current reproducibility remain unknown after model refresh #207.
- Scope: `internal/adapter/converter/lmstudio_converter.go`, `internal/adapter/converter/lmstudio_converter_test.go`, and `internal/core/domain/model.go` only if required. Prefer explicit provider metadata; allow a documented fallback only with maintainer agreement. No assumption that every Qwen model supports vision.
- Acceptance: captured sanitized metadata maps vision correctly, text-only sibling stays text-only, absent capability is not asserted as verified, existing unified output remains compatible. Run `go test ./internal/adapter/converter/... ./internal/core/domain/...`, then shared gate.
- Overlap: recheck merged #207 model refresh first; retire if solved. Fourth, 1-2 days; align fallback policy. Value: correct model selection for multimodal agent workloads and provider contract experience.

## OLLA-05: Implement opt-in alias-model failover on initial 429

- Evidence: VERIFIED request [#193](https://github.com/thushan/olla/issues/193) includes an author's working PoC and requests design guidance. This is collaboration on their proposal, not an unoccupied issue claim.
- Scope: `internal/adapter/proxy/core/retry.go` (identified by issue), inspected `internal/config/types.go` and `internal/core/domain/routing.go`; verify retry path at implementation checkout. Support bounded ordered model alternatives before response bytes are committed. No retries after streamed output, default silent model substitution, or generalized scheduler redesign.
- Acceptance: default off; model A 429 then B success on same endpoint; correct rewritten ContentLength; bounded tries; cancellation stops retries; committed streams never replay. Run `go test -race ./internal/adapter/proxy/... ./internal/config/... ./internal/core/domain/...`, then shared gate.
- Overlap: coordinate #144 persistent-5xx and author's PoC. Fifth, 4-6 days; blocked on maintainer/author ownership and retry semantics agreement. Value: model-level reliability and cost-aware routing; highest review burden here.
