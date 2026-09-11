# Lefthook CI repair

Repair only phenotype-registry Lefthook CI installation and immediately related execution/security defects. Both install sites must use official Lefthook v2.1.12 Linux x86_64 binaries with the published SHA-256 verified before execution. Never use Cargo for this Go tool. Treat PR titles as data, validate conventional messages, preserve unrelated work, and publish a focused non-force branch and PR without merging or creating a worktree.

Acceptance: workflow syntax checks pass, checksum matches downloaded artifact, negative checksum and malicious-title tests pass, actual Lefthook CLI runs compatible commands. Record unrelated baseline CI failures separately.
