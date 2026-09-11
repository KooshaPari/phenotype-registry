# Known issues and scope limits

- The existing pre-commit workflow-action-guard scans all workflows. It fails on mutable
  action references outside this repair. This PR pins its touched workflow only and does
  not weaken or bypass the repository-wide guard.
- The existing editorconfig command uses xargs/test with no staged files, which may fail on
  a clean CI checkout. This staged-file policy is outside the installation/title repair.
- Linux release bytes were downloaded and SHA-256 verified on macOS. Native real-hook
  behavior is exercised using the separately verified official macOS binary of the same
  version. Hosted Linux execution will be recorded from the PR workflow.
- Initial local installer-success test failed because macOS BSD sha256sum lacks --strict.
  The test now uses installed GNU gsha256sum on macOS, matching Ubuntu's sha256sum.
- Recursive worker spawning is disabled in this session. Validation and review performed
  directly instead. No child agents were created.
