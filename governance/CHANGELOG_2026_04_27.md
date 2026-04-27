## Phenotype-Org Governance CHANGELOG — 2026-04-27 sprint

(Kimi-generated 2026-04-27)

>>> dispatch-worker tier=nvidia/moonshotai/kimi-k2.5 model=nvidia/moonshotai/kimi-k2.5 endpoint=http://localhost:20128/v1
>>> routed to backend: moonshotai/kimi-k2.5
 ```markdown
## [Governance Rollout 2026.04.27] - 2026-04-27

### Added
- On-chain delegation registry with 7-day revocation timeouts
- Proposal lifecycle automation (draft → voting → execution)
- Emergency council multisig (3-of-5) for critical parameter patches
- Automated delegation vote counting via snapshot indexer
- Role-based access control (RBAC) for working-group treasuries

### Changed
- Voting period shortened from 7 days to 5 days for standard proposals
- Quorum calculation now weights reputation score over raw token balance
- Execution delay reduced from 48 hours to 24 hours for non-fiscal updates
- Proposal submission bond increased from 100 to 250 PHENO tokens

### Fixed
- Race condition in concurrent proposal tallying across multiple chains
- Metadata validation bypass allowing empty execution hashes
- Snapshot block calculation drift when bridging delegates from L1 to L2
- Edge case where abstain votes incorrectly counted toward quorum

### Deprecated
- Legacy v1 proposal schemas (sunset 2026-06-01)
- Manual CSV uploads for delegate verification (migrate to API)
- Direct admin override functions (replaced by emergency timelock)
- Discord/Discord-only signaling for soft-consensus (formalize via on-chain poll)

### Memory
- Decision record: rationale for 3-of-5 emergency threshold (see ADR-042)
- Archive: debate summary on quadratic vs. linear voting (April 2026)
- Migration notes: delegate registry state transfer validation steps
- Retrospective: April 20th sync delay root cause and remediation path
```
