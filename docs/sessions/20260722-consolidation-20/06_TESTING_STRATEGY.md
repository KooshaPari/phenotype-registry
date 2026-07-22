# Testing Strategy

## Packet Validation

- Verify all eight required session files exist.
- Verify the exact 20 repository names appear in the packet and no candidate is omitted.
- Verify HOLD, VERIFY-ONLY, fork, and no-READY rules match the specification.
- Run whitespace/error validation on the patch.
- Run targeted Markdown link and local-file-presence checks for this packet.

## Future Evidence Gates

For each possible disposition change, independently prove:

1. actual source default branch;
2. source and destination SHA parity;
3. source and destination content parity;
4. correct Batch A placement;
5. fork preservation and absence of remote mutation.

The known ecosystem-validator baseline and Vue missing-end-tag docs-build failure are pre-existing
blockers, not acceptance waivers.
