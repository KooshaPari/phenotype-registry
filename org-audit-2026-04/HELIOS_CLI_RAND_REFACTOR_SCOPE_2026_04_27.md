# helios-cli rand 0.9 refactor scope - 2026-04-27

## Scope

Local audit only. No `helios-cli` code was changed.

Audit command requested:

```bash
grep -rn "rand::rng()\|rand::thread_rng()\|rand::rngs::" --include="*.rs" . 2>/dev/null \
  | grep -v "/target/\|/codex-rs/target/" \
  | head -30
```

The requested command returned 28 Rust matches. A broader `rand::` pass found one
additional rand 0.9 production call site hidden behind `use rand::rng` in
`codex-rs/core/src/unified_exec/mod.rs`.

## Summary

| Category | Count | Notes |
| --- | ---: | --- |
| Crypto / security-sensitive | 8 production call sites plus 1 already-safe `OsRng` use | Refactor first. Must use `OsRng` or a narrowly wrapped CSPRNG source. |
| Random sample / non-crypto | 13 production call sites | Prefer a small helper if `OsRng` is acceptable ergonomically; otherwise isolate advisory-suppressed usage behind one module. |
| Test-only deterministic RNG | 8 requested matches | No advisory implications for runtime behavior. Keep deterministic `StdRng` unless tests no longer need reproducibility. |

## Crypto-first refactor scope

| Priority | File / module | Matched usage | Classification | Future refactor |
| --- | --- | --- | --- | --- |
| P0 | `codex-rs/login/src/pkce.rs` / PKCE verifier generation | `rand::thread_rng().fill_bytes(&mut bytes)` | Crypto | Replace with `OsRng.try_fill_bytes`; fail closed on RNG errors. |
| P0 | `codex-rs/login/src/server.rs` / OAuth state generation | `rand::thread_rng().fill_bytes(&mut bytes)` | Crypto | Replace with `OsRng.try_fill_bytes`; propagate/handle generation failure. |
| P0 | `codex-rs/windows-sandbox-rs/src/sandbox_users.rs` / sandbox account password | `use rand::rngs::SmallRng`; actual use `SmallRng::from_entropy().fill_bytes(...)` | Crypto | Replace password bytes with `OsRng.try_fill_bytes`; avoid modulo bias if password charset mapping remains. |
| P0 | `codex-rs/windows-sandbox-rs/src/elevated/runner_pipe.rs` / elevated runner pipe names | `use rand::rngs::SmallRng`; actual use `SmallRng::from_entropy().gen::<u128>()` | Crypto | Generate pipe nonce with `OsRng`; security boundary IPC names should not depend on `SmallRng`. |
| P0 | `codex-rs/windows-sandbox-rs/src/elevated_impl.rs` / elevated runner pipe names | `use rand::rngs::SmallRng`; actual use `SmallRng::from_entropy().gen::<u128>()` | Crypto | Same as `runner_pipe.rs`; consolidate through one helper. |
| P1 | `codex-rs/windows-sandbox-rs/src/cap.rs` / capability SID strings | `use rand::rngs::SmallRng`; actual use `SmallRng::from_entropy().next_u32()` | Security-sensitive identifier | Use `OsRng` for SID components, or document why uniqueness-only is sufficient. Prefer `OsRng` because SIDs define sandbox isolation artifacts. |
| P1 | `codex-rs/windows-sandbox-rs/src/desktop.rs` / private desktop name | `use rand::rngs::SmallRng`; actual use `SmallRng::from_entropy().gen::<u128>()` | Security-sensitive identifier | Use shared secure nonce helper if the desktop name is intended to be unguessable; otherwise classify as uniqueness-only in code comments. |
| P1 | `codex-rs/secrets/src/local.rs` / secrets passphrase generation | `use rand::rngs::OsRng` | Crypto, already safe | Keep as exemplar pattern for the refactor. |

## Random sample / non-crypto production scope

| File / module | Matched usage | Classification | Future refactor |
| --- | --- | --- | --- |
| `codex-rs/codex-client/src/retry.rs` / retry backoff | `rand::thread_rng().random_range(0.9..1.1)` | Random sample | Backoff jitter can use `OsRng` or a local non-crypto helper if advisory posture permits. |
| `codex-rs/core/src/util.rs` / auth retry backoff | `rand::thread_rng().random_range(0.9..1.1)` | Random sample | Same backoff jitter helper as client retry. |
| `codex-rs/core/src/unified_exec/process_manager.rs` / reserved process id | `rand::thread_rng().random_range(1_000..100_000)` | Random sample | Use helper; uniqueness is checked against reserved IDs. |
| `codex-rs/core/src/unified_exec/mod.rs` / chunk id | `use rand::rng`; actual use `rng().random_range(0..16)` | Random sample | Broader audit hit outside requested grep. Replace or wrap with same helper. |
| `codex-rs/core/src/agent/guards.rs` / nickname start offset | `rand::thread_rng().random_range(0..names.len())` | Random sample | Non-security UI/selection randomness. |
| `codex-rs/core/src/agent/registry.rs` / agent nickname choice | two `choose(&mut rand::thread_rng())` calls | Random sample | Non-security UI/selection randomness. |
| `codex-rs/tui/src/ascii_animation.rs` / animation variant | `rand::thread_rng()` | Random sample | Non-security UI randomness. |
| `codex-rs/tui_app_server/src/ascii_animation.rs` / animation variant | `rand::thread_rng()` | Random sample | Mirror of TUI path. |
| `codex-rs/tui/src/chatwidget.rs` / startup placeholder | three `rand::thread_rng()` call sites | Random sample | Non-security UI placeholder selection. |
| `codex-rs/tui_app_server/src/chatwidget.rs` / startup placeholder | `rand::thread_rng()` | Random sample | Mirror of TUI path. |
| `codex-rs/tui/src/tooltips.rs` / tooltip selection | `rand::thread_rng()` | Random sample | Non-security UI tooltip selection. |
| `codex-rs/tui_app_server/src/tooltips.rs` / tooltip selection | `rand::thread_rng()` | Random sample | Mirror of TUI path. |

## Test-only deterministic scope

| File / module | Matched usage | Classification | Future refactor |
| --- | --- | --- | --- |
| `codex-rs/tui/src/tooltips.rs` / tests | `use rand::rngs::StdRng` | Test-only | Keep deterministic seeded RNG unless the test design changes. |
| `codex-rs/tui_app_server/src/tooltips.rs` / tests | `use rand::rngs::StdRng` | Test-only | Mirror of TUI tests. |
| `codex-rs/tui/src/bottom_pane/textarea.rs` / tests | `rand::rngs::StdRng` helper and seeded construction | Test-only | Keep deterministic seeded RNG. |
| `codex-rs/tui_app_server/src/bottom_pane/textarea.rs` / tests | `rand::rngs::StdRng` helper and seeded construction | Test-only | Mirror of TUI tests. |

## Recommended approach

1. Add a small `secure_random` helper near existing platform utilities, modeled on
   `codex-rs/secrets/src/local.rs` and based on `OsRng.try_fill_bytes`.
2. Convert P0 crypto call sites first: PKCE verifier, OAuth state, sandbox
   passwords, and elevated runner pipe names.
3. Convert P1 sandbox identifiers next, or explicitly document any uniqueness-only
   cases before leaving them outside crypto scope.
4. For non-crypto jitter/UI sampling, either use `OsRng` for simplicity or isolate
   `rand` advisory exposure behind one reviewed non-crypto helper.
5. Leave deterministic `StdRng` test-only usages as-is unless test reproducibility
   requirements change.

