# Routing / local AI audit redo

Observed 2026-09-05 02:47-03:29 UTC (September 4 Pacific). Live gh REST API. Growth UNKNOWN (no historical star series). All listed counts are exact snapshots. This is evidence of sampled merges, not forecast acceptance. Proxy for outsiders: authors with NONE or CONTRIBUTOR association, excluding bots. Contributor can still be affiliated; Fast-Editor and GoModel especially require affiliation caution. Sample is up to 100 most recently updated closed PRs, not a random sample or acceptance rate, and excludes currently open PRs.

| Repository | Stars | Human outsider-proxy merged / closed sampled | Evidence |
|---|---:|---:|---|
| mostlygeek/llama-swap | 5577 | 24/51 (of 100) | [1053](https://github.com/mostlygeek/llama-swap/pull/1053) config,server: add startup profile hook |
| thushan/olla | 293 | 5/7 (of 100) | [188](https://github.com/thushan/olla/pull/188) Add native `GET /internal/metrics` |
| raullenchai/Rapid-MLX | 3659 | 1/3 (of 100) | [2878](https://github.com/raullenchai/Rapid-MLX/pull/2878) Desktop: default to 7659 (RMLX) and add GUI port control — avoid 8000 collisions |
| madroidmaq/mlx-omni-server | 741 | 18/39 (of 56) | [120](https://github.com/madroidmaq/mlx-omni-server/pull/120) feat: Add mlx_vlm support for Gemma 4 and VLM-only models |
| NadirRouter/NadirClaw | 645 | 16/28 (of 65) | [84](https://github.com/NadirRouter/NadirClaw/pull/84) fix(server): reconcile request params the routed model rejects (#83) |
| RelayPlane/proxy | 200 | 0/2 (of 3) | [11](https://github.com/RelayPlane/proxy/pull/11) Add Codex CLI delegated subagents |
| LeenHawk/gproxy | 228 | 0/8 (of 100) | [202](https://github.com/LeenHawk/gproxy/pull/202) channel(custom): forward inbound user-agent upstream |
| ENTERPILOT/GoModel | 1111 | 75/85 (of 100) | [877](https://github.com/ENTERPILOT/GoModel/pull/877) feat(config): add GOMODEL_OFFLINE switch and local file model catalog source |
| gglucass/headroom-desktop | 535 | 4/5 (of 72) | [50](https://github.com/gglucass/headroom-desktop/pull/50) feat(windows): experimental Windows support |
| fkiene/llmtrim | 226 | 3/3 (of 100) | [258](https://github.com/fkiene/llmtrim/pull/258) fix(memo): preserve current cache breakpoints |
| rynfar/meridian | 1983 | 0/31 (of 100) | [922](https://github.com/rynfar/meridian/pull/922) fix(session): stop refusing the loser of a declared concurrent race (#870) |
| Fast-Editor/Lynkr | 547 | 41/55 (of 70) | [103](https://github.com/Fast-Editor/Lynkr/pull/103) fix(ci): make npm audit resilient to registry advisory-endpoint outages |
| majiayu000/litellm-rs | 110 | 1/1 (of 100) | [1124](https://github.com/majiayu000/litellm-rs/pull/1124) fix(factory): auto-detect private network for localhost |
| inference-gateway/inference-gateway | 211 | 11/13 (of 100) | [579](https://github.com/inference-gateway/inference-gateway/pull/579) docs: fix dead CONTRIBUTING links and complete README provider and example lists |
| toby-bridges/api-relay-audit | 824 | 3/6 (of 57) | [46](https://github.com/toby-bridges/api-relay-audit/pull/46) test: cover tool rewrite edge cases |
| diegosouzapw/OmniGlyph | 107 | 0/0 (of 55) | No outsider evidence |
| Xerxes-2/clewdr | 1257 | 35/47 (of 75) | [151](https://github.com/Xerxes-2/clewdr/pull/151) Preserve thinking.display field when streaming to display thinking for newer opus models |
| Nano-Collective/nanocoder | 2451 | 1/3 (of latest 10 closed by creation, different sample) | [1101](https://github.com/Nano-Collective/nanocoder/pull/1101) CI coverage checks |

## Best four: actual limits

### fkiene/llmtrim
- [PR 258](https://github.com/fkiene/llmtrim/pull/258), adandedjan-stephane: fix(memo): preserve current cache breakpoints. Created 2026-08-10T11:44:47Z; merged 2026-08-11T16:04:25Z; 28.3 hours.
- [PR 257](https://github.com/fkiene/llmtrim/pull/257), adandedjan-stephane: fix(proxy): trust Windows certificate roots for upstream TLS. Created 2026-08-10T08:39:31Z; merged 2026-08-11T15:33:24Z; 30.9 hours.
- [PR 196](https://github.com/fkiene/llmtrim/pull/196), jmyoung: Implement new `llmtrim setup --env` feature flag for outputting envvars to stdout. Created 2026-07-19T11:02:56Z; merged 2026-07-20T11:42:24Z; 24.7 hours.

### gglucass/headroom-desktop
- [PR 50](https://github.com/gglucass/headroom-desktop/pull/50), aashishtamsya: feat(windows): experimental Windows support. Created 2026-08-06T13:25:06Z; merged 2026-08-07T09:38:37Z; 20.2 hours.
- [PR 52](https://github.com/gglucass/headroom-desktop/pull/52), alon3153: Flip the watchdog bypass before capturing give-up diagnostics. Created 2026-08-07T06:08:08Z; merged 2026-08-07T08:06:16Z; 2.0 hours.
- [PR 48](https://github.com/gglucass/headroom-desktop/pull/48), aashishtamsya: Add Homebrew cask distribution. Created 2026-08-01T15:45:27Z; merged 2026-08-06T14:27:39Z; 118.7 hours.
- Counterexample [37](https://github.com/gglucass/headroom-desktop/pull/37): closed unmerged 2026-07-07T08:21:41Z; Add external Headroom host/port config & detection. Closure reason not inspected; may be superseded, not rejected.

### thushan/olla
- [PR 188](https://github.com/thushan/olla/pull/188), Puupuls: Add native `GET /internal/metrics`. Created 2026-06-25T11:48:48Z; merged 2026-07-02T06:25:47Z; 162.6 hours.
- [PR 164](https://github.com/thushan/olla/pull/164), matthewjhunter: fix: make proxy response_header_timeout configurable. Created 2026-06-07T07:47:48Z; merged 2026-06-07T08:02:42Z; 0.2 hours.
- [PR 161](https://github.com/thushan/olla/pull/161), matthewjhunter: fix: route Lemonade models by mapping downloaded to available state. Created 2026-06-07T06:33:13Z; merged 2026-06-07T07:33:50Z; 1.0 hours.
- Counterexample [149](https://github.com/thushan/olla/pull/149): closed unmerged 2026-07-30T22:50:52Z; fix(openai-compat): surface availability state for OpenAI-compatible backends. Closure reason not inspected; may be superseded, not rejected.

### mostlygeek/llama-swap
- [PR 1053](https://github.com/mostlygeek/llama-swap/pull/1053), sousekd: config,server: add startup profile hook. Created 2026-08-26T12:27:33Z; merged 2026-08-29T18:26:54Z; 78.0 hours.
- [PR 1072](https://github.com/mostlygeek/llama-swap/pull/1072), tdamir: docker/unified: make CUDA version and architectures configurable. Created 2026-08-31T20:24:03Z; merged 2026-08-31T23:09:17Z; 2.8 hours.
- [PR 1063](https://github.com/mostlygeek/llama-swap/pull/1063), chrispaulm: expose context_window on models endpoint. Created 2026-08-27T16:46:38Z; merged 2026-08-28T16:58:54Z; 24.2 hours.
- Counterexample [595](https://github.com/mostlygeek/llama-swap/pull/595): closed unmerged 2026-07-10T12:37:22Z; feat: Add lifecycle hooks for model health checks and shutdown. Closure reason not inspected; may be superseded, not rejected.

## Maintainer and friction evidence

- [François Kiene](https://github.com/fkiene): 12 followers; public bio Senior Ruby on Rails engineer (7+ years, FinTech), building llmtrim in Rust. Closest substantiated modest-profile business engineer. PR258: four commits, 192 additions/26 deletions, two files, two owner reviews, no inline review comments. DCO and changelog required; owner explicitly marked further performance/tests nonblocking and added followup fixes himself. Sample supports collaborative moderate scrutiny, not anything-goes.
- [gglucass](https://github.com/gglucass): 106 followers, no public bio/company in profile. PR50 experimental Windows accepted in 20.2h but 35 commits and 18 comments; no formal reviews. PR48 Homebrew cask accepted in 118.7h. Thus broad outside features accepted, yet not automatically low churn. Useful direct desktop token-cost product.
- [Thushan Fernando](https://github.com/thushan): 98 followers; companies TensorFoundry | FernAero | SixPivot; profile languages C/C++, Rust, Go, Bash/Python. PR188 metrics accepted after 162.6h; CodeRabbit CHILL review had 3 actionable findings. Small timeout fix PR164 accepted in 14.9 minutes and Lemonade routing fix161 in 60.6 minutes. Strong small-fix lane; AI review present.
- [Benson Wong](https://github.com/mostlygeek): 403 followers; profile company Tailscale and Elethink. More experienced than desired reference profile, but actual outside contributions. PR1053 has CodeRabbit CHILL review. Good useful local model infrastructure; lower archetype fit.

## Other screening judgments

- NadirClaw: external model-provider PR80 accepted 4.7h; request reconciliation84 2.1h; classifier config77 22.0h. Strong direct router candidate, ownership background unknown. PR39 Anthropic compatibility closed unmerged, reason not inspected.
- api-relay-audit: external tool substitution fixture44 merged 1.9h; test46 12.8h; broaden refusal detection45 17.9h. Small sample but useful routing/security integration work. Latest outside78 closed unmerged after weeks; reason unknown.
- GoModel: 75/85 sample outsider proxy merges dominated by SantiagoDePolonia; may reflect affiliated core builder, do not treat as 75 independent outside contributors.
- Lynkr: 41/55 similarly dominated by veerareddyvishal144 who may be principal. Distinct binyangzhu000-sudo provider PR90 merged 14.2h, stronger outsider example.
- inference-gateway: 11/13 but concentrated TKaltofen and maintainer automation; verify relationship before ranking strongly.
- Rapid-MLX: 1/3 outsider sample; large owner+Mergify traffic. Not strong low-friction evidence.
- meridian: 0/31 outsider recent closed sample; owner changes dominate. Could supersede rather than outright reject; still avoid as easy merge recommendation.
- gproxy: 0/8 outsider sampled, many bot merges. Avoid claiming open contributions.
- RelayPlane: 0/2 outside closed PRs in entire 3-PR closed list. No demonstrated merge openness.
- mlx-omni-server: 18/39 historical outside merges but latest push May9, last actual outside merges May7 and waits 32-45 days. Watch only.
- clewdr: 35/47 outside history, but some waits 4 months; review latency variable and product focuses reverse proxy account surfaces.
- OmniGlyph: same Diego owner but zero outside human evidence in 55 closed sample. Can't infer accessibility from identity alone.
- litellm-rs: outside1124 localhost fix merged in 2.3h, only one outside example among100. Thin evidence.

## OmniRoute control

Actual current outside examples: [12650](https://github.com/diegosouzapw/OmniRoute/pull/12650) hartmark pending tracking fix created Sep3 23:58Z merged Sep4 03:03Z (3.1h); [12646](https://github.com/diegosouzapw/OmniRoute/pull/12646) dashboard conversation link, 7.0h; [12636](https://github.com/diegosouzapw/OmniRoute/pull/12636) RaviTharuma OpenCode cost metadata 7.1h. This supports real external merge throughput now, not claims about Diego's prior career or project's amateur quality. Current closed unmerged examples12748,12721,12694 prove not literally all PRs merged; reason not inspected.
