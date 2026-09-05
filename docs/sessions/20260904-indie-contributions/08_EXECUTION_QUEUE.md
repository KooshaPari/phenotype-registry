# Refined execution queue

The sponsor asked to refine, optimize, and expand the plan. This adds sequencing, effort controls, and measurable evidence requirements without increasing the ten-repository scope or submitting upstream changes.

## First wave

| Order | Proposal | Why first | Entry gate | Success evidence |
|---|---|---|---|---|
| 1 | [LY01](plans/lynkr.md#ly01-correct-contributor-runtime-and-commands) | Small documented mismatch, low implementation uncertainty | Recheck current guide and manifest | Fresh contributor can run the exact documented commands |
| 2 | [TM02](plans/token-monitor.md#tm02-restore-linux-floating-bubble-size) | Concrete reported UX bug | Reproduce on available Linux desktop; otherwise choose TM03 | Repeat collapse/expand without incorrect window bounds |
| 3 | [KR03](plans/keirouter.md#kr03-provider-throttling-classification-fixtures) | Direct gateway compatibility | Obtain sanitized missing provider fixture; existing passing case is not enough | Correct throttle versus credit-exhaustion classification |
| 4 | [GL04](plans/gpt-load.md#gl04-subscription-account-weight-editor) | Bounded UI gap with existing backend contract | Confirm current omission and maintainer ownership | Weight change persists; error rollback works |
| 5 | [MP01](plans/macparakeet.md#mp01-stable-opencode-go-session-headers) | Direct provider compatibility | Independently verify provider requirement and issue ownership | Correct session continuity without header leakage to other providers |

Suggested active work cap: two implementation lanes total, one open contribution per upstream initially. The queue is a priority judgment, not predicted acceptance. Reproduction and scope can reorder it.

## Expanded proposal classification

- Source mismatch: LY01 has inspected documentation/manifest disagreement; verify current HEAD before editing.
- Reported bugs: TM02, MP03, GL01, DC02-DC05 have linked user/maintainer reports but are not reproduced locally in this session.
- Feature requests: require clear maintainer agreement on the proposed smaller slice.
- Coverage/behavior hypotheses: KR01-KR04, LY02/LY04/LY05, AT05 and several CP entries require a demonstrated missing case. Do not create test-only churn where coverage is already adequate.
- Holds: all CP entries require current maintainer responsiveness and architecture agreement; DC01 must coordinate with the reporter who already offers a patch.

## Optimize engineering effort

Timebox initial issue/HEAD/overlap checks to 30-60 minutes and reproduction to an initial two-hour investigation. These are review checkpoints, not forced abandonment of a valuable hard problem. If no gap is demonstrated, record the result and choose the next proposal.

Reuse sanitized protocol fixtures and measurement methods across our private verification work where licenses permit. Keep each upstream patch native to its project; avoid introducing a shared framework or coupling repositories.

For each eventual PR record: source SHA; issue owner; baseline reproduction; changed behavior; tests and commands; first human response; review rounds; merge/rejection outcome; release containing the change; and downstream dogfood result. This creates actual acceptance data for the next selection review.

## Business, brand, and experience

| Work area | Practical benefit | Strong portfolio evidence |
|---|---|---|
| Gateways | More reliable provider behavior and configuration | Reproduced failure removed; compatibility fixture accepted |
| Usage tooling | Clearer cost attribution and useful desktop UX | Correct accounting/display under named edge cases |
| Local developer apps | Better daily workflows | Demonstrable before/after usability with platform validation |
| CRM | Fewer customer-facing data/automation errors | Route or workflow correctness with production-like fixtures |

Avoid claiming business adoption, performance improvement, or popularity growth before measuring it. Contribution credit and learning are useful even where commercial code reuse is restricted.
