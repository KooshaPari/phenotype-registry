# Wave D — stashly relocation

**Date:** 2026-06-17  
**Disposition id:** 46 (ADR-ECO-001)  
**Source:** HexaKit `crates/stashly`  
**Target:** `phenoShared/crates/stashly` (ResilienceKit archived — infra cache lives in phenoShared)

## Rationale

ResilienceKit remains archived per boundary audit; cache/resilience primitives consolidate into **phenoShared** dynamic-keep infra until a dedicated resilience workspace is unarchived.

## Status

Physical copy landed in `feat/wave-d-stashly-reloc`.
