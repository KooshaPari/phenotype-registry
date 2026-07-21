# Cargo Deny Local Run Results - 2026-04-27

Local-only verification from `/Users/kooshapari/CodeProjects/Phenotype/repos`.
Runner: `cargo-deny 0.19.0`.

Requested target count note: prompt said 18 pre-session-enrolled foundational repos, but listed 10 targets. This report covers the 10 listed targets.

Summary:
- Clean exit code 0: 2
- Non-zero exit code: 5
- Skipped: 3
- Resolved summaries with `advisories ok`: 6 of 7 executed repos
- Advisory IDs observed in local output: `RUSTSEC-2024-0437`, `RUSTSEC-2025-0134`, `RUSTSEC-2025-0140`, `RUSTSEC-2026-0049`, `RUSTSEC-2026-0105`

## Failures First

| Repo | Exit | Advisory state | Top error lines |
| --- | ---: | --- | --- |
| BytePort | 4 | `advisories ok` | `error[rejected]: failed to satisfy license requirements` |
| FocalPoint | 4 | `advisories ok` | `error[rejected]: failed to satisfy license requirements`; `error[unlicensed]: agent-orchestrator = 0.1.0 is unlicensed`; `error[unlicensed]: bench-guard = 0.0.12 is unlicensed`; `error[unlicensed]: demo-walkthrough = 0.0.1 is unlicensed`; `error[unlicensed]: focuspoint-e2e = 0.0.1 is unlicensed` |
| PhenoObservability | 4 | `advisories ok` | `error[rejected]: failed to satisfy license requirements`; `error[unlicensed]: pheno-questdb = 0.1.0 is unlicensed`; `error[unlicensed]: phenotype-observably-macros = 0.1.1 is unlicensed` |
| hwLedger | 1 | no final cargo-deny summary | `error: duplicate key`; `error: no matching package named phenotype-error-core found` |
| Sidekick | 4 | `advisories ok` | `error[rejected]: failed to satisfy license requirements` |

### BytePort

Command: `cd BytePort && cargo deny check 2>&1 | tail -5`

Exit code: `4`

```text
                  │   └── tauri-utils v2.8.3 (*)
                  ├── tauri-codegen v2.5.5 (*)
                  └── tauri-utils v2.8.3 (*)

advisories ok, bans ok, licenses FAILED, sources ok
```

`grep "^error" | sort -u | head -5`:

```text
error[rejected]: failed to satisfy license requirements
```

### FocalPoint

Command: `cd FocalPoint && cargo deny check 2>&1 | tail -5`

Exit code: `4`

```text
                  │   └── wasmtime-wasi v43.0.1 (*)
                  └── wiggle v43.0.1
                      └── wasmtime-wasi v43.0.1 (*)

advisories ok, bans ok, licenses FAILED, sources ok
```

`grep "^error" | sort -u | head -5`:

```text
error[rejected]: failed to satisfy license requirements
error[unlicensed]: agent-orchestrator = 0.1.0 is unlicensed
error[unlicensed]: bench-guard = 0.0.12 is unlicensed
error[unlicensed]: demo-walkthrough = 0.0.1 is unlicensed
error[unlicensed]: focuspoint-e2e = 0.0.1 is unlicensed
```

### PhenoObservability

Command: `cd PhenoObservability && cargo deny check 2>&1 | tail -5`

Exit code: `4`

```text
29 │ advisory = "RUSTSEC-2024-0437"
30 │ reason = "protobuf: LOW severity uncontrolled recursion crash. Awaiting upstream fix."
   │           ─────────────────────────────────────────────────────────────────────────── reason

advisories ok, bans ok, licenses FAILED, sources ok
```

`grep "^error" | sort -u | head -5`:

```text
error[rejected]: failed to satisfy license requirements
error[unlicensed]: pheno-questdb = 0.1.0 is unlicensed
error[unlicensed]: phenotype-observably-macros = 0.1.1 is unlicensed
```

### hwLedger

Command: `cd hwLedger && cargo deny check 2>&1 | tail -5`

Exit code: `1`

```text
  | ^^^^^^^^^^^
error: no matching package named `phenotype-error-core` found
location searched: Git repository https://github.com/KooshaPari/phenoShared.git?branch=main
required by package `hwledger-core v0.0.1 (/Users/kooshapari/CodeProjects/Phenotype/repos/hwLedger/crates/hwledger-core)`

```

`grep "^error" | sort -u | head -5`:

```text
error: duplicate key
error: no matching package named `phenotype-error-core` found
```

### Sidekick

Command: `cd Sidekick && cargo deny check 2>&1 | tail -5`

Exit code: `4`

```text
   │                 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ wildcard dependency
   │
   ├ sidekick-messaging v0.0.1

advisories ok, bans ok, licenses FAILED, sources ok
```

`grep "^error" | sort -u | head -5`:

```text
error[rejected]: failed to satisfy license requirements
```

## Clean

| Repo | Exit | Tail result |
| --- | ---: | --- |
| helios-cli | 0 | `advisories ok, bans ok, licenses ok, sources ok` |
| Tasken | 0 | `advisories ok, bans ok, licenses ok, sources ok` |

### helios-cli

Command: `cd helios-cli && cargo deny check 2>&1 | tail -5`

Exit code: `0`

```text
   │             ━━━━━━━━━━━━━━━━━             ───────────────────────────────────────────────────────────────────────────────── ignore reason
   │             │
   │             no crate matched advisory criteria

advisories ok, bans ok, licenses ok, sources ok
```

### Tasken

Command: `cd Tasken && cargo deny check 2>&1 | tail -5`

Exit code: `0`

```text
   │             ━━━━━━━━━━━━━━━━━             ───────────────────────────────────────────────────────────────────────────────── ignore reason
   │             │
   │             no crate matched advisory criteria

advisories ok, bans ok, licenses ok, sources ok
```

## Skipped

| Repo | Reason |
| --- | --- |
| FocalPoint-vitepress | missing checkout at `/Users/kooshapari/CodeProjects/Phenotype/repos/FocalPoint-vitepress` |
| agentkit | missing checkout at `/Users/kooshapari/CodeProjects/Phenotype/repos/agentkit` |
| agentapi-plusplus | checkout exists, but root `deny.toml` is missing |

