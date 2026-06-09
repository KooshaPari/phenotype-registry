# Standard justfile for phenotype-registry
# Org standard recipes for hygiene, quality, and release flow.

set shell := ["bash", "-uc"]
set dotenv-load := true

# Default recipe — list available targets
default:
	@just --list

# --- hygiene ----------------------------------------------------------------

# Install pre-commit hooks
hooks:
	pre-commit install

# Run pre-commit hooks against all files
hooks-all:
	pre-commit run --all-files

# Normalize editorconfig and trailing whitespace
normalize:
	@command -v editorconfig >/dev/null 2>&1 || { echo "editorconfig (node) not installed" >&2; exit 1; }
	editorconfig-tools fix

# --- quality ----------------------------------------------------------------

# Run linters (placeholder — wire to project stack)
lint:

# Run type checks (placeholder)
check:

# Run tests (placeholder)
test:

# --- docs -------------------------------------------------------------------

# Build docs site (placeholder)
docs:

# --- release ----------------------------------------------------------------

# Show git status / branch hygiene
status:
	@git status --short --branch

# Show top of the working tree
top:
	@git rev-parse --show-toplevel
