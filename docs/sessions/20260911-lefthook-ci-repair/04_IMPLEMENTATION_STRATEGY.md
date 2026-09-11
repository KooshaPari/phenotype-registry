# Implementation strategy

Both jobs use the same inline download recipe with centrally pinned version and SHA-256.
The Linux x86_64 platform is checked before download. Curl fails on HTTP errors, retries
transient failures and writes an unexecutable file into a unique runner temporary directory.
GNU sha256sum validates the pinned digest before chmod or execution. The binary version is
checked before exposing its directory through GITHUB_PATH. No sudo, Cargo or remote script.

Pin the touched workflow's existing checkout/setup-python actions to the exact SHAs shown
in the failing run, without changing versions. Restrict workflow token to contents:read.

Actions already provides CI=true. Remove nonexistent --env-ci=true and disable implicit
hook installation with --no-auto-install. Real Lefthook testing exposed that shell $1 is
empty in the inline command. Correct it to the documented quoted {1} argument template.

Only the fixed file path reaches the hook template. PR title arrives in step env, never
inside shell source, and printf preserves special characters as literal message data.
