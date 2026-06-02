# Historical Artifact Contamination - 2026-04-27

Scope: local-only audit from `/Users/kooshapari/CodeProjects/Phenotype`.

Repository set: top-level local git checkouts under `Phenotype/` and direct
children of `Phenotype/repos/`, excluding the `repos/` shelf repository itself,
local `.archive/` paths, local worktree collections, and nested vendored
dependency checkouts.

Probe run in each repository:

```bash
git log --all --pretty=format: --name-only --diff-filter=A 2>/dev/null | sort -u | grep -E "^target/|^node_modules/" | head -5
```

## Summary

- Repositories scanned: 114
- Repositories flagged: 3
- Flag basis: any locally recorded added path matching root-level `target/` or
  `node_modules/` in any branch history
- Count basis: number of paths returned by the bounded `head -5` probe

## Findings

| Rank | Local repo | Probe count | Local HEAD SHA | Matching paths returned by probe |
| ---: | --- | ---: | --- | --- |
| 1 | `repos/GDK` | 5 | `bfb7a4fa54d5` | `target/.rustc_info.json`<br>`target/CACHEDIR.TAG`<br>`target/debug/.cargo-lock`<br>`target/debug/.fingerprint/anstream-3b58cba3ab48334f/dep-lib-anstream`<br>`target/debug/.fingerprint/anstream-3b58cba3ab48334f/invoked.timestamp` |
| 2 | `repos/thegent` | 5 | `6d05a57ce1c8` | `node_modules/.bin/esbuild`<br>`node_modules/.bin/press-export-pdf`<br>`node_modules/.bin/puppeteer`<br>`node_modules/.bin/vite`<br>`node_modules/.bin/vitepress` |
| 3 | `repos/AgilePlus` | 1 | `2b3909f4b0e1` | `target/SPEC.md` |

## Not Flagged By This Probe

The probe only matches artifact directories at the repository root:
`^target/` and `^node_modules/`. Nested artifact paths such as
`docs/node_modules/`, `apps/foo/target/`, `dist/`, `build/`, or `out/` are out
of scope for this requested local audit.

## Reproduction Notes

The scan was local-only and did not query GitHub or any remote registry for
archive state. "Non-archived" was interpreted from local checkout placement:
repositories under `.archive/` and local worktree holding areas were excluded.
