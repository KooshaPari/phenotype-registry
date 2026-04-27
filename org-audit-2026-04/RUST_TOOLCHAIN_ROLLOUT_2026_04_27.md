# rust-toolchain.toml Rollout — 2026-04-27

11 PRs merged pinning Rust 1.83 + rustfmt+clippy:
PhenoKits #69, Tracely #19, Eidolon #20, eyetracker #24, rich-cli-kit #16, thegent-dispatch #15, thegent-workspace #16, phenotype-bus #14, phenotype-journeys #22, PhenoProc #31, +1 more

## Template
```toml
[toolchain]
channel = "1.83"
components = ["rustfmt", "clippy"]
profile = "minimal"
```

Standardizes MSRV across the org. cargo automatically downloads on first use.
