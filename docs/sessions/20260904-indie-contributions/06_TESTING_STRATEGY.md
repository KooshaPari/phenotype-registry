# Validation strategy

Documentation validation: verify ten plan files, five IDs per repository, fifty distinct IDs, fifty unique discovery repository rows, local Markdown links, and git diff --check. Record actual validation outcomes in the publication document.

No code behavior changes in phenotype-registry. A documentation build may be attempted if dependencies are available; report any pre-existing or environment failure separately. Do not equate local docs checks with hosted CI success.

During later upstream implementation use each plan's concrete scenarios and current project commands. Record source SHA, command, exit result, and environment; exercise the reported failure before the fix and verify it after. Do not claim a future test has passed.

