# Research

- Owner/scope: KooshaPari/phenotype-registry CI only. No cross-repo absorption or sibling changes.
- Read AGENTS.md (Windows-1252), CLAUDE.md, and session artifact protocol. Existing worktrees inspected, none created. Main is dirty with unrelated audit and registry work. Publish using a separate Git index and commit based on origin/main without switching or changing shared main.
- Actual failed run: https://github.com/KooshaPari/phenotype-registry/actions/runs/34578596742 (PR #555). Both installation jobs fail. At 08:19:23 UTC the pre-commit job records curl HTTP 404, then `mv: cannot stat './bin/lefthook'`.
- Independently requested https://raw.githubusercontent.com/evilmartians/lefthook/master/install.sh and received HTTP 404.
- Official documentation: https://lefthook.dev/install/ describes a standalone no-dependency binary. https://github.com/evilmartians/lefthook identifies Go implementation. Cargo installation is incorrect.
- Selected official release https://github.com/evilmartians/lefthook/releases/tag/v2.1.12. Downloaded Linux x86_64 and macOS arm64 binaries plus lefthook_checksums.txt. GitHub asset digests, release checksums and locally computed SHA-256 agree.
- Linux x86_64 SHA-256: `22ff1ad48d1a0f4dca8d6b7e920056c6a9015f9204e5b693858ed9c2db759a16`.
- macOS arm64 SHA-256 (local CLI validation only): `9917087099678f8ee2be031494a9b53eae49717eea2023abf4fae11c8bb64e54`.
- Real v2.1.12 CLI rejects `--env-ci=true` with exit 1. Use Actions-provided CI environment, `--no-auto-install`, and documented positional arguments.
- PR title is currently directly interpolated into shell source twice. Replace with step environment data and quoted printf.
- Existing pre-commit workflow-action-guard scans every workflow, including unrelated mutable references. Do not broaden this repair into fleet-wide action pinning.
- AgilePlus feature `lefthook-ci-repair` created from 02_SPECIFICATIONS.md. Tracking database remains local, excluded from focused PR.
