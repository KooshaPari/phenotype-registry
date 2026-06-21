# Known Issues

## Network-Restricted Cargo Index

`cargo test --workspace` attempted to refresh the crates.io index and failed
because the sandbox could not resolve `index.crates.io`.

Resolution: reran the Rust gates with `--offline`; the cached dependencies were
available and the test/clippy gates passed.
