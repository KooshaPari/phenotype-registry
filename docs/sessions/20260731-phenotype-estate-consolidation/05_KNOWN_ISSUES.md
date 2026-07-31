# Known Issues

| Severity | Issue | Mitigation |
|---|---|---|
| Blocker | Several lanes have dirty/local-only payloads not yet reconciled to live remote refs | preserve and publish exact refs before promotion |
| Blocker | OmniRoute, portage, SessionLedger, phenoAI, and registry PR gates are failing or behind | repair only after current-main reconciliation |
| Blocker | thegent-sharecli is archived/read-only | request unarchive; do not create an alternate repo |
| High | AgilePlus checked-in SQLite DB fails WAL pragma with disk I/O error | use isolated DB; retain existing dirty snapshot; do not delete DB files |
| High | Workspace has critically low free space | route heavy builds to isolated target/cache or heavy runner |
| Non-blocker | Tracera workspace-wide format check has pre-existing `tracera-cli` drift | keep focused fixture gate separate and record baseline debt |
| Blocker | AgilePlus governance validation currently finds 0/6 required CI/review evidence items | attach remote CI and review artifacts before implementing/validating the feature |
| Deferred | AgilePlus reactivation and any archive/delete action | sponsor gate only |
