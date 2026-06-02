# PlayCua Repo Discovery - 2026-04-27

## Scope

Local-only discovery audit for:

`/Users/kooshapari/CodeProjects/Phenotype/repos/PlayCua`

## Commands and Results

### Git Status

```text
## master...origin/master [behind 26]
 M Cargo.lock
 M Cargo.toml
 M SPEC.md
 M docs/worklogs/README.md
?? ADR-001-hexagonal-architecture.md
?? ADR-002-stdio-json-rpc-ipc.md
?? ADR-003-cross-platform-capture.md
?? ADR.md
?? CHARTER.md
?? Cargo.toml.bak
?? PRD.md
?? RESEARCH.md
?? deny.toml
?? docs/FUNCTIONAL_REQUIREMENTS.md
?? docs/adr/
?? docs/research/
?? native/tests/smoke_test.rs
?? worklog.md
```

### Cargo Check Warning/Error Sample

Command:

```bash
timeout 60 cargo check --workspace 2>&1 | grep -E "^error|^warning:" | sort -u | head -15
```

Output:

```text
warning: profiles for the non root package will be ignored, specify profiles at the workspace root:
```

### Rust TODO/FIXME/XXX/HACK Sample

```text
./native/src/adapters/macos/nsworkspace.rs:4://! Full NSWorkspace/AppleScript window focus is a TODO;
./native/src/adapters/macos/nsworkspace.rs:67:        // TODO: implement using NSWorkspace / AppleScript activate.
./native/src/adapters/linux/ewmh.rs:4://! Full x11rb EWMH implementation for window focus is a TODO;
./native/src/adapters/linux/ewmh.rs:67:        // TODO: implement using x11rb _NET_ACTIVE_WINDOW ClientMessage.
./native/src/window/macos.rs:28:    // TODO: use NSApplication/AppleScript to focus window by ID.
./native/src/window/linux.rs:2://! Full x11rb implementation is a TODO -- xcap covers the common case.
./native/src/window/linux.rs:29:    // TODO: use x11rb to raise/focus the window.
```

### Rust Line Count

```text
3889 total
```

### Cargo Package Count

Command:

```bash
cargo metadata --no-deps 2>&1 | jq -r '.packages[].name' 2>/dev/null | wc -l
```

Output:

```text
0
```

## Findings

PlayCua is not clean locally: `master` is 26 commits behind origin and has modified and untracked files. The 60-second workspace check surfaced a workspace profile placement warning. Rust TODO debt is concentrated in Linux/macOS window focus and platform adapter implementations. The scanned Rust surface is 3,889 lines. The requested cargo metadata package-count pipeline returned `0`, which indicates metadata did not yield parseable package names through the jq pipeline in this local state.
