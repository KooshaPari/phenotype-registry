# Committed Build Artifacts Audit - 2026-04-27

Scope: non-archived `KooshaPari/*` repositories from live GitHub metadata.
Method: `gh api repos/<owner>/<repo>/git/trees/HEAD?recursive=1 --jq .tree[].path`; flags are committed tree paths only.

## Summary

- Repositories scanned: 103
- Repositories with violations: 8
- Violation-kind count: 12
- Committed artifact paths under target/dist/build/out/node_modules: 17614
- Repositories with Cargo backup duplicate violations: 0

## Findings

| Rank | Repository | Violation Kinds | Artifact Path Count | Cargo Backup Count | Top Offending Paths |
| ---: | --- | ---: | ---: | ---: | --- |
| 1 | `KooshaPari/agentapi-plusplus` | 3 (dist/, build/, node_modules/) | 8063 | 0 | `docs/.vitepress/dist`<br>`docs/.vitepress/dist/404.html`<br>`docs/.vitepress/dist/CHANGELOG.html`<br>`docs/.vitepress/dist/PRD.html`<br>`docs/.vitepress/dist/SPEC.html` |
| 2 | `KooshaPari/helios-router` | 3 (dist/, build/, node_modules/) | 7975 | 0 | `docs/.vitepress/dist`<br>`docs/node_modules`<br>`docs/node_modules/.bin`<br>`docs/node_modules/.bin/esbuild`<br>`docs/node_modules/.bin/nanoid` |
| 3 | `KooshaPari/Dino` | 1 (target/) | 760 | 0 | `src/Tools/AssetPipelineRust/target`<br>`src/Tools/AssetPipelineRust/target/.rustc_info.json`<br>`src/Tools/AssetPipelineRust/target/CACHEDIR.TAG`<br>`src/Tools/AssetPipelineRust/target/release`<br>`src/Tools/AssetPipelineRust/target/release/.cargo-lock` |
| 4 | `KooshaPari/thegent` | 1 (out/) | 28 | 0 | `crates/thegent-hooks/src/out`<br>`crates/thegent-hooks/src/out/mod.rs`<br>`extensions/vscode/out`<br>`extensions/vscode/out/__tests__`<br>`extensions/vscode/out/__tests__/agentServerClient.test.js` |
| 5 | `KooshaPari/Tracera` | 1 (out/) | 781 | 0 | `ARCHIVE/CONFIG/default/@nodelib/fs.scandir@2.1.5@@@1/out`<br>`ARCHIVE/CONFIG/default/@nodelib/fs.scandir@2.1.5@@@1/out/adapters`<br>`ARCHIVE/CONFIG/default/@nodelib/fs.scandir@2.1.5@@@1/out/adapters/fs.d.ts`<br>`ARCHIVE/CONFIG/default/@nodelib/fs.scandir@2.1.5@@@1/out/adapters/fs.js`<br>`ARCHIVE/CONFIG/default/@nodelib/fs.scandir@2.1.5@@@1/out/constants.d.ts` |
| 6 | `KooshaPari/HexaKit` | 1 (build/) | 4 | 1 | `templates/zig/templates/zig/.zig-cache/o/7dfd98b2a4c5d9e682510ba8038ab741/build`<br>`templates/zig/templates/zig/.zig-cache/o/aa4d5a1581dcd56b0fc18c874cb38ac6/build`<br>`templates/zig/templates/zig/.zig-cache/o/c61c93e231e25fc185b2afb88c9d4f0a/build`<br>`templates/zig/templates/zig/.zig-cache/o/c84c9b68cee80cbbc65f4cab02d02525/build` |
| 7 | `KooshaPari/phenotype-infra` | 1 (dist/) | 2 | 0 | `iac/oci-lottery/dist`<br>`iac/oci-lottery/dist/phenotype-oci-lottery.plist` |
| 8 | `KooshaPari/heliosCLI` | 1 (dist/) | 1 | 0 | `docs/.vitepress/dist` |

## Per-Repository Detail

### KooshaPari/agentapi-plusplus

- Violation kinds: 3 (dist/, build/, node_modules/)
- Artifact counts: target/=0, dist/=3051, build/=10, out/=0, node_modules/=5002
- Cargo.lock present: no
- Cargo backup counts: Cargo.lock.bak=0, Cargo.toml.bak=0
- Top offending paths:
  - `docs/.vitepress/dist`
  - `docs/.vitepress/dist/404.html`
  - `docs/.vitepress/dist/CHANGELOG.html`
  - `docs/.vitepress/dist/PRD.html`
  - `docs/.vitepress/dist/SPEC.html`

### KooshaPari/helios-router

- Violation kinds: 3 (dist/, build/, node_modules/)
- Artifact counts: target/=0, dist/=2969, build/=10, out/=0, node_modules/=4996
- Cargo.lock present: yes
- Cargo backup counts: Cargo.lock.bak=0, Cargo.toml.bak=0
- Top offending paths:
  - `docs/.vitepress/dist`
  - `docs/node_modules`
  - `docs/node_modules/.bin`
  - `docs/node_modules/.bin/esbuild`
  - `docs/node_modules/.bin/nanoid`

### KooshaPari/Dino

- Violation kinds: 1 (target/)
- Artifact counts: target/=760, dist/=0, build/=0, out/=0, node_modules/=0
- Cargo.lock present: yes
- Cargo backup counts: Cargo.lock.bak=0, Cargo.toml.bak=0
- Top offending paths:
  - `src/Tools/AssetPipelineRust/target`
  - `src/Tools/AssetPipelineRust/target/.rustc_info.json`
  - `src/Tools/AssetPipelineRust/target/CACHEDIR.TAG`
  - `src/Tools/AssetPipelineRust/target/release`
  - `src/Tools/AssetPipelineRust/target/release/.cargo-lock`

### KooshaPari/thegent

- Violation kinds: 1 (out/)
- Artifact counts: target/=0, dist/=0, build/=0, out/=28, node_modules/=0
- Cargo.lock present: no
- Cargo backup counts: Cargo.lock.bak=0, Cargo.toml.bak=0
- Top offending paths:
  - `crates/thegent-hooks/src/out`
  - `crates/thegent-hooks/src/out/mod.rs`
  - `extensions/vscode/out`
  - `extensions/vscode/out/__tests__`
  - `extensions/vscode/out/__tests__/agentServerClient.test.js`

### KooshaPari/Tracera

- Violation kinds: 1 (out/)
- Artifact counts: target/=0, dist/=0, build/=0, out/=781, node_modules/=0
- Cargo.lock present: no
- Cargo backup counts: Cargo.lock.bak=0, Cargo.toml.bak=0
- Top offending paths:
  - `ARCHIVE/CONFIG/default/@nodelib/fs.scandir@2.1.5@@@1/out`
  - `ARCHIVE/CONFIG/default/@nodelib/fs.scandir@2.1.5@@@1/out/adapters`
  - `ARCHIVE/CONFIG/default/@nodelib/fs.scandir@2.1.5@@@1/out/adapters/fs.d.ts`
  - `ARCHIVE/CONFIG/default/@nodelib/fs.scandir@2.1.5@@@1/out/adapters/fs.js`
  - `ARCHIVE/CONFIG/default/@nodelib/fs.scandir@2.1.5@@@1/out/constants.d.ts`

### KooshaPari/HexaKit

- Violation kinds: 1 (build/)
- Artifact counts: target/=0, dist/=0, build/=4, out/=0, node_modules/=0
- Cargo.lock present: yes
- Cargo backup counts: Cargo.lock.bak=0, Cargo.toml.bak=1
- Top offending paths:
  - `templates/zig/templates/zig/.zig-cache/o/7dfd98b2a4c5d9e682510ba8038ab741/build`
  - `templates/zig/templates/zig/.zig-cache/o/aa4d5a1581dcd56b0fc18c874cb38ac6/build`
  - `templates/zig/templates/zig/.zig-cache/o/c61c93e231e25fc185b2afb88c9d4f0a/build`
  - `templates/zig/templates/zig/.zig-cache/o/c84c9b68cee80cbbc65f4cab02d02525/build`

### KooshaPari/phenotype-infra

- Violation kinds: 1 (dist/)
- Artifact counts: target/=0, dist/=2, build/=0, out/=0, node_modules/=0
- Cargo.lock present: yes
- Cargo backup counts: Cargo.lock.bak=0, Cargo.toml.bak=0
- Top offending paths:
  - `iac/oci-lottery/dist`
  - `iac/oci-lottery/dist/phenotype-oci-lottery.plist`

### KooshaPari/heliosCLI

- Violation kinds: 1 (dist/)
- Artifact counts: target/=0, dist/=1, build/=0, out/=0, node_modules/=0
- Cargo.lock present: yes
- Cargo backup counts: Cargo.lock.bak=0, Cargo.toml.bak=0
- Top offending paths:
  - `docs/.vitepress/dist`
