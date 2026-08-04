# Research

## Canonical boundary owner

`phenotype-registry` is the governance and boundary SSOT. Runtime ownership remains repository-specific; this session does not move runtime code without a separate contract and PR.

## Current authoritative lanes

| Lane | Remote evidence | Local risk |
|---|---|---|
| OmniRoute | PR #481 open/behind; #483 blocked | dirty feature branch and failing checks |
| Tracera | `main=774c0061e886`; PR #748 merged; corrected preservation ref `wip/20260731T0748-18c750581389c880` | dirty preserve packet is recoverable but not a release merge |
| phenotype-tooling | PR #252 merged | post-merge branch diverges 57 ahead/9 behind |
| portage | PR #495 open/dirty | security, lint, type, test, verify failures |
| phenotype-registry | PR #432 blocked | local branch 28 ahead and dirty |
| SessionLedger | PR #391 behind | visual/e2e/provenance failures |
| phenoAI | #68 merged; #69/#70 unstable | behind/ahead divergence and dirty state |
| phenotype-omlx | remote comparison 44 ahead/15 behind | feature branch requires reconciliation |

## Existing boundary decisions

- sharecli and thegent-sharecli remain separate runtimes under `coordination-lock-queue-v1`.
- cliproxyapi-plusplus and OmniRoute remain separate with explicit path provenance.
- PhenoObservability is the telemetry substrate; Tracera is the durable evidence/audit consumer.
- Agentora owns canonical runtime behavior; legacy PhenoAgent is preserved evidence.
- `.tmp-phenotypes-boundary` is a duplicate checkout and is not authoritative.
- AgilePlus is parked outside the active merge train.

## Explicit dependencies

- thegent-sharecli is archived; sponsor policy is to request unarchive, not bypass protections.
- Local GitHub tracking refs may be stale; GitHub remote state wins.
- The filesystem has critically low free space; avoid broad scans and cache-producing builds.

## sharecli and thegent-sharecli boundary checkpoint (2026-08-04)

- `sharecli` remains the canonical standalone Rust runtime. Its ownership and release
  boundary are not transferred by this evidence record.
- The archived Python `thegent-sharecli` facade is substantially absorbed at
  `thegent/sharecli`: 14 of its 16 compared Python blobs are exact blob matches.
- This is implementation provenance only, not cross-language equivalence. The two
  non-matching Python blobs, Rust/Python API and behavior parity, consumer manifests,
  release/installed-artifact checks, and archived-repository hosted state still need
  verification.
- No cross-language merge, extraction, tombstone, archive/unarchive, redirect, or
  canonical-owner change is authorized from the 14/16 result. Keep the archived Python
  lineage preserved and use the existing coordination parity fixture before any sponsor
  gate.
