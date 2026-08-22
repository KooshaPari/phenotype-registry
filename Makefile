.PHONY: build test lint clean

# phenotype-registry DAG foundation crate

build:
	cargo build --release

test:
	cargo test

lint:
	cargo clippy -- -D warnings
	cargo fmt --check

clean:
	cargo clean
