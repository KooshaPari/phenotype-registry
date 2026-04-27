# Cargo-Deny Live Results - 2026-04-27

Live verification after the requested `sleep 300` delay for the 42 local Rust repos.
Latest run source command per repo: `gh run list --repo KooshaPari/$repo --workflow=cargo-deny.yml --limit 1 --json conclusion,headSha,databaseId,createdAt 2>&1`.
Failure headline source: latest run SHA plus `gh run view <id> --log-failed | head -10`, with an additional concise cause line where GitHub exposed one.

## Tally

| Conclusion | Count |
|---|---:|
| failure | 36 |
| success | 6 |
| in_progress | 0 |
| total | 42 |

## Results

| Repo | Conclusion | Headline | Head SHA | Run ID | Created At |
|---|---|---|---|---:|---|
| AgilePlus | failure | warning[license-not-encountered]: license was not encountered | `ac741e7f67f3` | 24987410559 | 2026-04-27T09:32:35Z |
| bare-cua | failure | error[rejected]: failed to satisfy license requirements | `55bfcf847154` | 24987500776 | 2026-04-27T09:34:40Z |
| BytePort | failure | error[rejected]: failed to satisfy license requirements | `d429eceb08ae` | 24987416402 | 2026-04-27T09:32:43Z |
| Civis | failure | log not found: 73164144882 | `995894ff331a` | 24987418891 | 2026-04-27T09:32:47Z |
| Configra | failure | log not found: 73164154241 | `4fb9011153ea` | 24987421598 | 2026-04-27T09:32:51Z |
| Eidolon | failure | log not found: 73164163858 | `b5543f7d43af` | 24987424623 | 2026-04-27T09:32:55Z |
| eyetracker | failure | error[rejected]: failed to satisfy license requirements | `efecd1699abb` | 24987427943 | 2026-04-27T09:33:00Z |
| FocalPoint | failure | 2026-04-27 09:39:29 [ERROR] failed to fetch crates: error: failed to load manifest for workspace member `/github/workspace/crates/focus-always-on` | `df7df7926d57` | 24987430818 | 2026-04-27T09:33:04Z |
| GDK | failure | 2026-04-27 09:37:50 [ERROR] failed to fetch crates: error: failed to parse lock file at: /github/workspace/Cargo.lock | `650242f09272` | 24987434322 | 2026-04-27T09:33:08Z |
| helios-cli | failure | warning[license-not-encountered]: license was not encountered | `14c8e1a81797` | 24987437195 | 2026-04-27T09:33:12Z |
| helios-router | failure | log not found: 73164215811 | `7c7089b3824d` | 24987440021 | 2026-04-27T09:33:16Z |
| heliosCLI | failure | warning[license-not-encountered]: license was not encountered | `6e305e28b790` | 24987442822 | 2026-04-27T09:33:20Z |
| HeliosLab | failure | warning[no-license-field]: license expression was not specified in manifest for crate 'pheno-cli = 0.1.1' | `5df9be10b4df` | 24987445312 | 2026-04-27T09:33:24Z |
| hwLedger | failure | 2026-04-27 09:39:21 [ERROR] failed to fetch crates:     Updating git repository `https://github.com/KooshaPari/phenoShared.git` | `38d505ea9bc6` | 24987450133 | 2026-04-27T09:33:30Z |
| KDesktopVirt | failure | log not found: 73164258093 | `a8345bed6db2` | 24987452528 | 2026-04-27T09:33:34Z |
| KlipDot | failure | workflow cargo-deny.yml not found on the default branch (https://api.github.com/repos/KooshaPari/KlipDot/actions/workflows/cargo-deny.yml) |  |  |  |
| kmobile | failure | workflow cargo-deny.yml not found on the default branch (https://api.github.com/repos/KooshaPari/kmobile/actions/workflows/cargo-deny.yml) |  |  |  |
| Metron | failure | error[rejected]: failed to satisfy license requirements | `00f9e61b9e9a` | 24987458400 | 2026-04-27T09:33:42Z |
| pheno | failure | 2026-04-27 09:39:54 [ERROR] failed to fetch crates:     Updating crates.io index | `b91b9a2d86f6` | 24987461100 | 2026-04-27T09:33:46Z |
| phenoAI | failure | 2026-04-27 09:38:44 [ERROR] failed to fetch crates: error: invalid unquoted key, expected letters, numbers, `-`, `_` | `6099b1fea73b` | 24987463520 | 2026-04-27T09:33:49Z |
| phenoData | failure | error[rejected]: failed to satisfy license requirements | `509777bb05e1` | 24987466076 | 2026-04-27T09:33:53Z |
| PhenoKits | failure | cargo-deny	Run cargo-deny	﻿2026-04-27T09:38:08.9509912Z ##[group]Run EmbarkStudios/cargo-deny-action@v2 | `35d67ed93ece` | 24987468695 | 2026-04-27T09:33:56Z |
| PhenoPlugins | failure | 2026-04-27 09:38:32 [ERROR] failed to fetch crates: error: failed to load manifest for workspace member `/github/workspace/crates/pheno-plugin-core` | `20dc016fecea` | 24987476667 | 2026-04-27T09:34:07Z |
| PhenoProc | failure | error[rejected]: failed to satisfy license requirements | `6a602fddaa67` | 24987479312 | 2026-04-27T09:34:11Z |
| phenoShared | failure | 2026-04-27 09:39:12 [ERROR] failed to fetch crates: error: duplicate key | `28c76f171501` | 24987484346 | 2026-04-27T09:34:18Z |
| phenotype-bus | failure | log not found: 73164373092 | `c28edc25b9e1` | 24987486976 | 2026-04-27T09:34:21Z |
| phenotype-journeys | failure | log not found: 73164382167 | `eb710c061e9c` | 24987489721 | 2026-04-27T09:34:25Z |
| phenotype-tooling | failure | warning[no-license-field]: license expression was not specified in manifest for crate 'agent-orchestrator = 0.1.0' | `37c1f20b9330` | 24987492388 | 2026-04-27T09:34:29Z |
| phenoUtils | failure | warning[no-license-field]: license expression was not specified in manifest for crate 'pheno-crypto = 0.1.0' | `d7c01124c307` | 24987495248 | 2026-04-27T09:34:32Z |
| PhenoVCS | failure | error[rejected]: failed to satisfy license requirements | `863ce3c27a04` | 24987497863 | 2026-04-27T09:34:36Z |
| PlayCua | failure | error[rejected]: failed to satisfy license requirements | `55bfcf847154` | 24987500776 | 2026-04-27T09:34:40Z |
| rich-cli-kit | failure | log not found: 73164426350 | `97614c478de3` | 24987503434 | 2026-04-27T09:34:43Z |
| Sidekick | failure | log not found: 73164435424 | `84eb00d28d9f` | 24987506208 | 2026-04-27T09:34:47Z |
| thegent-dispatch | failure | log not found: 73164453939 | `fa1593261483` | 24987511744 | 2026-04-27T09:34:55Z |
| thegent-workspace | failure | log not found: 73164462642 | `6e6b1e9ea304` | 24987514379 | 2026-04-27T09:34:59Z |
| Tracely | failure | log not found: 73164482762 | `b81eca8ddb2f` | 24987520193 | 2026-04-27T09:35:07Z |
| HexaKit | success |  | `56805f3080bc` | 24987447775 | 2026-04-27T09:33:27Z |
| PhenoMCP | success |  | `3bfe84ab67c7` | 24987471470 | 2026-04-27T09:34:00Z |
| PhenoObservability | success |  | `7600908e4823` | 24987473915 | 2026-04-27T09:34:04Z |
| PhenoRuntime | success |  | `64530f267ae9` | 24987481890 | 2026-04-27T09:34:14Z |
| Tasken | success |  | `aceccbdc3895` | 24987509024 | 2026-04-27T09:34:51Z |
| Tokn | success |  | `41bd0532f1a3` | 24987517256 | 2026-04-27T09:35:03Z |

## Captured First 10 Failed-Log Lines

The command requested first-10-line capture for each failed run. Rows where GitHub returned `log not found` are preserved as observed.

### AgilePlus (24987410559, ac741e7f67f3)

```text
cargo-deny	Run cargo-deny	﻿2026-04-27T09:37:35.7279975Z ##[group]Run EmbarkStudios/cargo-deny-action@v2
cargo-deny	Run cargo-deny	2026-04-27T09:37:35.7280294Z with:
cargo-deny	Run cargo-deny	2026-04-27T09:37:35.7280470Z   rust-version: stable
cargo-deny	Run cargo-deny	2026-04-27T09:37:35.7280669Z   command: check
cargo-deny	Run cargo-deny	2026-04-27T09:37:35.7280878Z   arguments: --all-features
cargo-deny	Run cargo-deny	2026-04-27T09:37:35.7281105Z   manifest-path: ./Cargo.toml
cargo-deny	Run cargo-deny	2026-04-27T09:37:35.7281311Z   log-level: warn
cargo-deny	Run cargo-deny	2026-04-27T09:37:35.7281493Z   use-git-cli: false
cargo-deny	Run cargo-deny	2026-04-27T09:37:35.7281670Z env:
cargo-deny	Run cargo-deny	2026-04-27T09:37:35.7281842Z   CARGO_HOME: /home/runner/.cargo
```

### bare-cua (24987500776, 55bfcf847154)

```text
cargo-deny	Run cargo-deny	﻿2026-04-27T09:38:00.1149118Z ##[group]Run EmbarkStudios/cargo-deny-action@v2
cargo-deny	Run cargo-deny	2026-04-27T09:38:00.1149423Z with:
cargo-deny	Run cargo-deny	2026-04-27T09:38:00.1149591Z   rust-version: stable
cargo-deny	Run cargo-deny	2026-04-27T09:38:00.1149787Z   command: check
cargo-deny	Run cargo-deny	2026-04-27T09:38:00.1149972Z   arguments: --all-features
cargo-deny	Run cargo-deny	2026-04-27T09:38:00.1150195Z   manifest-path: ./Cargo.toml
cargo-deny	Run cargo-deny	2026-04-27T09:38:00.1150413Z   log-level: warn
cargo-deny	Run cargo-deny	2026-04-27T09:38:00.1150591Z   use-git-cli: false
cargo-deny	Run cargo-deny	2026-04-27T09:38:00.1150765Z env:
cargo-deny	Run cargo-deny	2026-04-27T09:38:00.1150938Z   CARGO_HOME: /home/runner/.cargo
```

### BytePort (24987416402, d429eceb08ae)

```text
cargo-deny	Run cargo-deny	﻿2026-04-27T09:37:19.4188093Z ##[group]Run EmbarkStudios/cargo-deny-action@v2
cargo-deny	Run cargo-deny	2026-04-27T09:37:19.4188397Z with:
cargo-deny	Run cargo-deny	2026-04-27T09:37:19.4188567Z   rust-version: stable
cargo-deny	Run cargo-deny	2026-04-27T09:37:19.4188755Z   command: check
cargo-deny	Run cargo-deny	2026-04-27T09:37:19.4188938Z   arguments: --all-features
cargo-deny	Run cargo-deny	2026-04-27T09:37:19.4189150Z   manifest-path: ./Cargo.toml
cargo-deny	Run cargo-deny	2026-04-27T09:37:19.4189477Z   log-level: warn
cargo-deny	Run cargo-deny	2026-04-27T09:37:19.4189650Z   use-git-cli: false
cargo-deny	Run cargo-deny	2026-04-27T09:37:19.4189823Z env:
cargo-deny	Run cargo-deny	2026-04-27T09:37:19.4189988Z   CARGO_HOME: /home/runner/.cargo
```

### Civis (24987418891, 995894ff331a)

```text
log not found: 73164144882
```

### Configra (24987421598, 4fb9011153ea)

```text
log not found: 73164154241
```

### Eidolon (24987424623, b5543f7d43af)

```text
log not found: 73164163858
```

### eyetracker (24987427943, efecd1699abb)

```text
cargo-deny	Run cargo-deny	﻿2026-04-27T09:41:22.3537381Z ##[group]Run EmbarkStudios/cargo-deny-action@v2
cargo-deny	Run cargo-deny	2026-04-27T09:41:22.3537704Z with:
cargo-deny	Run cargo-deny	2026-04-27T09:41:22.3537895Z   rust-version: stable
cargo-deny	Run cargo-deny	2026-04-27T09:41:22.3538091Z   command: check
cargo-deny	Run cargo-deny	2026-04-27T09:41:22.3538286Z   arguments: --all-features
cargo-deny	Run cargo-deny	2026-04-27T09:41:22.3538510Z   manifest-path: ./Cargo.toml
cargo-deny	Run cargo-deny	2026-04-27T09:41:22.3538720Z   log-level: warn
cargo-deny	Run cargo-deny	2026-04-27T09:41:22.3538899Z   use-git-cli: false
cargo-deny	Run cargo-deny	2026-04-27T09:41:22.3539073Z env:
cargo-deny	Run cargo-deny	2026-04-27T09:41:22.3539240Z   CARGO_HOME: /home/runner/.cargo
```

### FocalPoint (24987430818, df7df7926d57)

```text
cargo-deny	Run cargo-deny	﻿2026-04-27T09:38:56.6101837Z ##[group]Run EmbarkStudios/cargo-deny-action@v2
cargo-deny	Run cargo-deny	2026-04-27T09:38:56.6102148Z with:
cargo-deny	Run cargo-deny	2026-04-27T09:38:56.6102333Z   rust-version: stable
cargo-deny	Run cargo-deny	2026-04-27T09:38:56.6102554Z   command: check
cargo-deny	Run cargo-deny	2026-04-27T09:38:56.6102758Z   arguments: --all-features
cargo-deny	Run cargo-deny	2026-04-27T09:38:56.6102998Z   manifest-path: ./Cargo.toml
cargo-deny	Run cargo-deny	2026-04-27T09:38:56.6103216Z   log-level: warn
cargo-deny	Run cargo-deny	2026-04-27T09:38:56.6103407Z   use-git-cli: false
cargo-deny	Run cargo-deny	2026-04-27T09:38:56.6103591Z env:
cargo-deny	Run cargo-deny	2026-04-27T09:38:56.6103798Z   CARGO_HOME: /home/runner/.cargo
```

### GDK (24987434322, 650242f09272)

```text
cargo-deny	Run cargo-deny	﻿2026-04-27T09:37:36.8304035Z ##[group]Run EmbarkStudios/cargo-deny-action@v2
cargo-deny	Run cargo-deny	2026-04-27T09:37:36.8304351Z with:
cargo-deny	Run cargo-deny	2026-04-27T09:37:36.8304535Z   rust-version: stable
cargo-deny	Run cargo-deny	2026-04-27T09:37:36.8304746Z   command: check
cargo-deny	Run cargo-deny	2026-04-27T09:37:36.8304951Z   arguments: --all-features
cargo-deny	Run cargo-deny	2026-04-27T09:37:36.8305209Z   manifest-path: ./Cargo.toml
cargo-deny	Run cargo-deny	2026-04-27T09:37:36.8305436Z   log-level: warn
cargo-deny	Run cargo-deny	2026-04-27T09:37:36.8305631Z   use-git-cli: false
cargo-deny	Run cargo-deny	2026-04-27T09:37:36.8305823Z env:
cargo-deny	Run cargo-deny	2026-04-27T09:37:36.8306009Z   CARGO_HOME: /home/runner/.cargo
```

### helios-cli (24987437195, 14c8e1a81797)

```text
cargo-deny	Run cargo-deny	﻿2026-04-27T09:38:15.2421182Z ##[group]Run EmbarkStudios/cargo-deny-action@v2
cargo-deny	Run cargo-deny	2026-04-27T09:38:15.2421490Z with:
cargo-deny	Run cargo-deny	2026-04-27T09:38:15.2421660Z   rust-version: stable
cargo-deny	Run cargo-deny	2026-04-27T09:38:15.2421899Z   manifest-path: ./codex-rs/Cargo.toml
cargo-deny	Run cargo-deny	2026-04-27T09:38:15.2422134Z   command: check
cargo-deny	Run cargo-deny	2026-04-27T09:38:15.2422325Z   arguments: --all-features
cargo-deny	Run cargo-deny	2026-04-27T09:38:15.2422527Z   log-level: warn
cargo-deny	Run cargo-deny	2026-04-27T09:38:15.2422710Z   use-git-cli: false
cargo-deny	Run cargo-deny	2026-04-27T09:38:15.2422883Z env:
cargo-deny	Run cargo-deny	2026-04-27T09:38:15.2423058Z   CARGO_HOME: /home/runner/.cargo
```

### helios-router (24987440021, 7c7089b3824d)

```text
log not found: 73164215811
```

### heliosCLI (24987442822, 6e305e28b790)

```text
cargo-deny	Run cargo-deny	﻿2026-04-27T09:38:12.5488970Z ##[group]Run EmbarkStudios/cargo-deny-action@v2
cargo-deny	Run cargo-deny	2026-04-27T09:38:12.5489282Z with:
cargo-deny	Run cargo-deny	2026-04-27T09:38:12.5489450Z   rust-version: stable
cargo-deny	Run cargo-deny	2026-04-27T09:38:12.5489668Z   manifest-path: ./codex-rs/Cargo.toml
cargo-deny	Run cargo-deny	2026-04-27T09:38:12.5489914Z   command: check
cargo-deny	Run cargo-deny	2026-04-27T09:38:12.5490101Z   arguments: --all-features
cargo-deny	Run cargo-deny	2026-04-27T09:38:12.5490303Z   log-level: warn
cargo-deny	Run cargo-deny	2026-04-27T09:38:12.5490480Z   use-git-cli: false
cargo-deny	Run cargo-deny	2026-04-27T09:38:12.5490650Z env:
cargo-deny	Run cargo-deny	2026-04-27T09:38:12.5490816Z   CARGO_HOME: /home/runner/.cargo
```

### HeliosLab (24987445312, 5df9be10b4df)

```text
cargo-deny	Run cargo-deny	﻿2026-04-27T09:37:12.7444695Z ##[group]Run EmbarkStudios/cargo-deny-action@v2
cargo-deny	Run cargo-deny	2026-04-27T09:37:12.7445318Z with:
cargo-deny	Run cargo-deny	2026-04-27T09:37:12.7445497Z   rust-version: stable
cargo-deny	Run cargo-deny	2026-04-27T09:37:12.7445702Z   command: check
cargo-deny	Run cargo-deny	2026-04-27T09:37:12.7445890Z   arguments: --all-features
cargo-deny	Run cargo-deny	2026-04-27T09:37:12.7446121Z   manifest-path: ./Cargo.toml
cargo-deny	Run cargo-deny	2026-04-27T09:37:12.7446337Z   log-level: warn
cargo-deny	Run cargo-deny	2026-04-27T09:37:12.7446517Z   use-git-cli: false
cargo-deny	Run cargo-deny	2026-04-27T09:37:12.7446704Z env:
cargo-deny	Run cargo-deny	2026-04-27T09:37:12.7446887Z   CARGO_HOME: /home/runner/.cargo
```

### hwLedger (24987450133, 38d505ea9bc6)

```text
cargo-deny	Run cargo-deny	﻿2026-04-27T09:39:08.1690714Z ##[group]Run EmbarkStudios/cargo-deny-action@v2
cargo-deny	Run cargo-deny	2026-04-27T09:39:08.1691063Z with:
cargo-deny	Run cargo-deny	2026-04-27T09:39:08.1691245Z   rust-version: stable
cargo-deny	Run cargo-deny	2026-04-27T09:39:08.1691454Z   command: check
cargo-deny	Run cargo-deny	2026-04-27T09:39:08.1691657Z   arguments: --all-features
cargo-deny	Run cargo-deny	2026-04-27T09:39:08.1691898Z   manifest-path: ./Cargo.toml
cargo-deny	Run cargo-deny	2026-04-27T09:39:08.1692122Z   log-level: warn
cargo-deny	Run cargo-deny	2026-04-27T09:39:08.1692312Z   use-git-cli: false
cargo-deny	Run cargo-deny	2026-04-27T09:39:08.1692501Z env:
cargo-deny	Run cargo-deny	2026-04-27T09:39:08.1692686Z   CARGO_HOME: /home/runner/.cargo
```

### KDesktopVirt (24987452528, a8345bed6db2)

```text
log not found: 73164258093
```

### Metron (24987458400, 00f9e61b9e9a)

```text
cargo-deny	Run cargo-deny	﻿2026-04-27T09:39:08.2691886Z ##[group]Run EmbarkStudios/cargo-deny-action@v2
cargo-deny	Run cargo-deny	2026-04-27T09:39:08.2692201Z with:
cargo-deny	Run cargo-deny	2026-04-27T09:39:08.2692373Z   rust-version: stable
cargo-deny	Run cargo-deny	2026-04-27T09:39:08.2692572Z   command: check
cargo-deny	Run cargo-deny	2026-04-27T09:39:08.2692762Z   arguments: --all-features
cargo-deny	Run cargo-deny	2026-04-27T09:39:08.2692989Z   manifest-path: ./Cargo.toml
cargo-deny	Run cargo-deny	2026-04-27T09:39:08.2693198Z   log-level: warn
cargo-deny	Run cargo-deny	2026-04-27T09:39:08.2693392Z   use-git-cli: false
cargo-deny	Run cargo-deny	2026-04-27T09:39:08.2693562Z env:
cargo-deny	Run cargo-deny	2026-04-27T09:39:08.2693730Z   CARGO_HOME: /home/runner/.cargo
```

### pheno (24987461100, b91b9a2d86f6)

```text
cargo-deny	Run cargo-deny	﻿2026-04-27T09:39:22.8171845Z ##[group]Run EmbarkStudios/cargo-deny-action@v2
cargo-deny	Run cargo-deny	2026-04-27T09:39:22.8172165Z with:
cargo-deny	Run cargo-deny	2026-04-27T09:39:22.8172345Z   rust-version: stable
cargo-deny	Run cargo-deny	2026-04-27T09:39:22.8172553Z   command: check
cargo-deny	Run cargo-deny	2026-04-27T09:39:22.8172747Z   arguments: --all-features
cargo-deny	Run cargo-deny	2026-04-27T09:39:22.8172988Z   manifest-path: ./Cargo.toml
cargo-deny	Run cargo-deny	2026-04-27T09:39:22.8173212Z   log-level: warn
cargo-deny	Run cargo-deny	2026-04-27T09:39:22.8173403Z   use-git-cli: false
cargo-deny	Run cargo-deny	2026-04-27T09:39:22.8173585Z env:
cargo-deny	Run cargo-deny	2026-04-27T09:39:22.8173787Z   CARGO_HOME: /home/runner/.cargo
```

### phenoAI (24987463520, 6099b1fea73b)

```text
cargo-deny	Run cargo-deny	﻿2026-04-27T09:38:31.3408975Z ##[group]Run EmbarkStudios/cargo-deny-action@v2
cargo-deny	Run cargo-deny	2026-04-27T09:38:31.3409327Z with:
cargo-deny	Run cargo-deny	2026-04-27T09:38:31.3409519Z   rust-version: stable
cargo-deny	Run cargo-deny	2026-04-27T09:38:31.3409744Z   command: check
cargo-deny	Run cargo-deny	2026-04-27T09:38:31.3409954Z   arguments: --all-features
cargo-deny	Run cargo-deny	2026-04-27T09:38:31.3410203Z   manifest-path: ./Cargo.toml
cargo-deny	Run cargo-deny	2026-04-27T09:38:31.3410440Z   log-level: warn
cargo-deny	Run cargo-deny	2026-04-27T09:38:31.3410663Z   use-git-cli: false
cargo-deny	Run cargo-deny	2026-04-27T09:38:31.3410862Z env:
cargo-deny	Run cargo-deny	2026-04-27T09:38:31.3411058Z   CARGO_HOME: /home/runner/.cargo
```

### phenoData (24987466076, 509777bb05e1)

```text
cargo-deny	Run cargo-deny	﻿2026-04-27T09:37:32.9000762Z ##[group]Run EmbarkStudios/cargo-deny-action@v2
cargo-deny	Run cargo-deny	2026-04-27T09:37:32.9001077Z with:
cargo-deny	Run cargo-deny	2026-04-27T09:37:32.9001262Z   rust-version: stable
cargo-deny	Run cargo-deny	2026-04-27T09:37:32.9001447Z   command: check
cargo-deny	Run cargo-deny	2026-04-27T09:37:32.9001641Z   arguments: --all-features
cargo-deny	Run cargo-deny	2026-04-27T09:37:32.9001860Z   manifest-path: ./Cargo.toml
cargo-deny	Run cargo-deny	2026-04-27T09:37:32.9002086Z   log-level: warn
cargo-deny	Run cargo-deny	2026-04-27T09:37:32.9002259Z   use-git-cli: false
cargo-deny	Run cargo-deny	2026-04-27T09:37:32.9002440Z env:
cargo-deny	Run cargo-deny	2026-04-27T09:37:32.9002605Z   CARGO_HOME: /home/runner/.cargo
```

### PhenoKits (24987468695, 35d67ed93ece)

```text
cargo-deny	Run cargo-deny	﻿2026-04-27T09:38:08.9509912Z ##[group]Run EmbarkStudios/cargo-deny-action@v2
cargo-deny	Run cargo-deny	2026-04-27T09:38:08.9510238Z with:
cargo-deny	Run cargo-deny	2026-04-27T09:38:08.9510411Z   rust-version: stable
cargo-deny	Run cargo-deny	2026-04-27T09:38:08.9510606Z   command: check
cargo-deny	Run cargo-deny	2026-04-27T09:38:08.9510793Z   arguments: --all-features
cargo-deny	Run cargo-deny	2026-04-27T09:38:08.9511021Z   manifest-path: ./Cargo.toml
cargo-deny	Run cargo-deny	2026-04-27T09:38:08.9511244Z   log-level: warn
cargo-deny	Run cargo-deny	2026-04-27T09:38:08.9511425Z   use-git-cli: false
cargo-deny	Run cargo-deny	2026-04-27T09:38:08.9511597Z env:
cargo-deny	Run cargo-deny	2026-04-27T09:38:08.9511768Z   CARGO_HOME: /home/runner/.cargo
```

### PhenoPlugins (24987476667, 20dc016fecea)

```text
cargo-deny	Run cargo-deny	﻿2026-04-27T09:38:18.0530354Z ##[group]Run EmbarkStudios/cargo-deny-action@v2
cargo-deny	Run cargo-deny	2026-04-27T09:38:18.0530676Z with:
cargo-deny	Run cargo-deny	2026-04-27T09:38:18.0530866Z   rust-version: stable
cargo-deny	Run cargo-deny	2026-04-27T09:38:18.0531076Z   command: check
cargo-deny	Run cargo-deny	2026-04-27T09:38:18.0531283Z   arguments: --all-features
cargo-deny	Run cargo-deny	2026-04-27T09:38:18.0531525Z   manifest-path: ./Cargo.toml
cargo-deny	Run cargo-deny	2026-04-27T09:38:18.0531754Z   log-level: warn
cargo-deny	Run cargo-deny	2026-04-27T09:38:18.0531950Z   use-git-cli: false
cargo-deny	Run cargo-deny	2026-04-27T09:38:18.0532141Z env:
cargo-deny	Run cargo-deny	2026-04-27T09:38:18.0532333Z   CARGO_HOME: /home/runner/.cargo
```

### PhenoProc (24987479312, 6a602fddaa67)

```text
cargo-deny	Run cargo-deny	﻿2026-04-27T09:40:01.9610413Z ##[group]Run EmbarkStudios/cargo-deny-action@v2
cargo-deny	Run cargo-deny	2026-04-27T09:40:01.9610722Z with:
cargo-deny	Run cargo-deny	2026-04-27T09:40:01.9610898Z   rust-version: stable
cargo-deny	Run cargo-deny	2026-04-27T09:40:01.9611097Z   command: check
cargo-deny	Run cargo-deny	2026-04-27T09:40:01.9611285Z   arguments: --all-features
cargo-deny	Run cargo-deny	2026-04-27T09:40:01.9611513Z   manifest-path: ./Cargo.toml
cargo-deny	Run cargo-deny	2026-04-27T09:40:01.9611729Z   log-level: warn
cargo-deny	Run cargo-deny	2026-04-27T09:40:01.9611915Z   use-git-cli: false
cargo-deny	Run cargo-deny	2026-04-27T09:40:01.9612095Z env:
cargo-deny	Run cargo-deny	2026-04-27T09:40:01.9612272Z   CARGO_HOME: /home/runner/.cargo
```

### phenoShared (24987484346, 28c76f171501)

```text
cargo-deny	Run cargo-deny	﻿2026-04-27T09:38:57.3197458Z ##[group]Run EmbarkStudios/cargo-deny-action@v2
cargo-deny	Run cargo-deny	2026-04-27T09:38:57.3197761Z with:
cargo-deny	Run cargo-deny	2026-04-27T09:38:57.3197924Z   rust-version: stable
cargo-deny	Run cargo-deny	2026-04-27T09:38:57.3198117Z   command: check
cargo-deny	Run cargo-deny	2026-04-27T09:38:57.3198296Z   arguments: --all-features
cargo-deny	Run cargo-deny	2026-04-27T09:38:57.3198520Z   manifest-path: ./Cargo.toml
cargo-deny	Run cargo-deny	2026-04-27T09:38:57.3198735Z   log-level: warn
cargo-deny	Run cargo-deny	2026-04-27T09:38:57.3198905Z   use-git-cli: false
cargo-deny	Run cargo-deny	2026-04-27T09:38:57.3199071Z env:
cargo-deny	Run cargo-deny	2026-04-27T09:38:57.3199237Z   CARGO_HOME: /home/runner/.cargo
```

### phenotype-bus (24987486976, c28edc25b9e1)

```text
log not found: 73164373092
```

### phenotype-journeys (24987489721, eb710c061e9c)

```text
log not found: 73164382167
```

### phenotype-tooling (24987492388, 37c1f20b9330)

```text
cargo-deny	Run cargo-deny	﻿2026-04-27T09:40:24.3527005Z ##[group]Run EmbarkStudios/cargo-deny-action@v2
cargo-deny	Run cargo-deny	2026-04-27T09:40:24.3527338Z with:
cargo-deny	Run cargo-deny	2026-04-27T09:40:24.3527519Z   rust-version: stable
cargo-deny	Run cargo-deny	2026-04-27T09:40:24.3527738Z   command: check
cargo-deny	Run cargo-deny	2026-04-27T09:40:24.3527930Z   arguments: --all-features
cargo-deny	Run cargo-deny	2026-04-27T09:40:24.3528161Z   manifest-path: ./Cargo.toml
cargo-deny	Run cargo-deny	2026-04-27T09:40:24.3528376Z   log-level: warn
cargo-deny	Run cargo-deny	2026-04-27T09:40:24.3528564Z   use-git-cli: false
cargo-deny	Run cargo-deny	2026-04-27T09:40:24.3528753Z env:
cargo-deny	Run cargo-deny	2026-04-27T09:40:24.3528934Z   CARGO_HOME: /home/runner/.cargo
```

### phenoUtils (24987495248, d7c01124c307)

```text
cargo-deny	Run cargo-deny	﻿2026-04-27T09:38:47.6723700Z ##[group]Run EmbarkStudios/cargo-deny-action@v2
cargo-deny	Run cargo-deny	2026-04-27T09:38:47.6723945Z with:
cargo-deny	Run cargo-deny	2026-04-27T09:38:47.6724100Z   rust-version: stable
cargo-deny	Run cargo-deny	2026-04-27T09:38:47.6724262Z   command: check
cargo-deny	Run cargo-deny	2026-04-27T09:38:47.6724427Z   arguments: --all-features
cargo-deny	Run cargo-deny	2026-04-27T09:38:47.6724615Z   manifest-path: ./Cargo.toml
cargo-deny	Run cargo-deny	2026-04-27T09:38:47.6724791Z   log-level: warn
cargo-deny	Run cargo-deny	2026-04-27T09:38:47.6724947Z   use-git-cli: false
cargo-deny	Run cargo-deny	2026-04-27T09:38:47.6725092Z env:
cargo-deny	Run cargo-deny	2026-04-27T09:38:47.6725245Z   CARGO_HOME: /home/runner/.cargo
```

### PhenoVCS (24987497863, 863ce3c27a04)

```text
cargo-deny	Run cargo-deny	﻿2026-04-27T09:37:44.3264077Z ##[group]Run EmbarkStudios/cargo-deny-action@v2
cargo-deny	Run cargo-deny	2026-04-27T09:37:44.3264381Z with:
cargo-deny	Run cargo-deny	2026-04-27T09:37:44.3264859Z   rust-version: stable
cargo-deny	Run cargo-deny	2026-04-27T09:37:44.3265080Z   command: check
cargo-deny	Run cargo-deny	2026-04-27T09:37:44.3265275Z   arguments: --all-features
cargo-deny	Run cargo-deny	2026-04-27T09:37:44.3265496Z   manifest-path: ./Cargo.toml
cargo-deny	Run cargo-deny	2026-04-27T09:37:44.3265704Z   log-level: warn
cargo-deny	Run cargo-deny	2026-04-27T09:37:44.3265880Z   use-git-cli: false
cargo-deny	Run cargo-deny	2026-04-27T09:37:44.3266048Z env:
cargo-deny	Run cargo-deny	2026-04-27T09:37:44.3266215Z   CARGO_HOME: /home/runner/.cargo
```

### PlayCua (24987500776, 55bfcf847154)

```text
cargo-deny	Run cargo-deny	﻿2026-04-27T09:38:00.1149118Z ##[group]Run EmbarkStudios/cargo-deny-action@v2
cargo-deny	Run cargo-deny	2026-04-27T09:38:00.1149423Z with:
cargo-deny	Run cargo-deny	2026-04-27T09:38:00.1149591Z   rust-version: stable
cargo-deny	Run cargo-deny	2026-04-27T09:38:00.1149787Z   command: check
cargo-deny	Run cargo-deny	2026-04-27T09:38:00.1149972Z   arguments: --all-features
cargo-deny	Run cargo-deny	2026-04-27T09:38:00.1150195Z   manifest-path: ./Cargo.toml
cargo-deny	Run cargo-deny	2026-04-27T09:38:00.1150413Z   log-level: warn
cargo-deny	Run cargo-deny	2026-04-27T09:38:00.1150591Z   use-git-cli: false
cargo-deny	Run cargo-deny	2026-04-27T09:38:00.1150765Z env:
cargo-deny	Run cargo-deny	2026-04-27T09:38:00.1150938Z   CARGO_HOME: /home/runner/.cargo
```

### rich-cli-kit (24987503434, 97614c478de3)

```text
log not found: 73164426350
```

### Sidekick (24987506208, 84eb00d28d9f)

```text
log not found: 73164435424
```

### thegent-dispatch (24987511744, fa1593261483)

```text
log not found: 73164453939
```

### thegent-workspace (24987514379, 6e6b1e9ea304)

```text
log not found: 73164462642
```

### Tracely (24987520193, b81eca8ddb2f)

```text
log not found: 73164482762
```

