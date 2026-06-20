# phenokits-commons boundary decision

Date: 2026-06-20
Decision: 

## Rationale

 looked like a broad super-repo because it contained runtime libraries under , , and . Those runtime surfaces are now removed from commons via  after absorption/preservation evidence closed source-loss risk.

The remaining intended boundary is governance/templates/policies/docs/shared artifact patterns. This is still broad, but it is not a runtime package substrate and should not receive executable libraries.

## Matrix

| Source Item | Source Evidence | Category | Source State | Target Repo | Target Evidence | Status | Deletion Justification | Risk if Deleted | Required Action |
|---|---|---|---|---|---|---|---|---|---|
| Go runtime libs |  | Runtime libraries | removed |  |  merged |  | Removed from commons after SDK absorption | low | none |
| Python config kit |  | Runtime/scaffold package | removed |  |  merged |  | Removed from commons after SDK absorption | low | none |
| Other Python libs |  | Runtime libraries | removed |  | file-equivalent target packages observed |  | Removed from commons after parity | low | none |
| TypeScript libs |  | Runtime libraries | removed |  preservation |  |  | Removed from commons, preserved pending real TS target | medium | create real TS target if needed |
| Governance docs/templates | , ,  | Governance artifacts | active |  | repo remains active after runtime cleanup |  | This is the narrowed surviving purpose | high if deleted | preserve repo |
| Templates/policies/config examples | , , , , ,  | Shared artifact patterns | active |  | remaining repo boundary |  | This is the narrowed surviving purpose | high if deleted | preserve repo |

## Final recommendation

Do not delete . Keep it active but narrowed. Future runtime libraries must go to tight SDK/package repos, not this commons repo.
