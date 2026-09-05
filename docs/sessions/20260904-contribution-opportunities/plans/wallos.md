# Wallos: five proposed contributions

Repository: https://github.com/ellite/Wallos. Evidence inspected September 5 UTC / September 4 Pacific: HEAD tree, issue bodies, webhook test source, [CONTRIBUTING.md](https://github.com/ellite/Wallos/blob/main/CONTRIBUTING.md), `dev/test.sh`, [open issues/PRs](https://github.com/ellite/Wallos/issues?q=is%3Aopen), and [recent closed PRs](https://github.com/ellite/Wallos/pulls?q=is%3Apr+is%3Aclosed+sort%3Aupdated-desc). All named existing paths were confirmed. Issue existence is verified; behavior was not reproduced locally. Estimates are engineering days, not merge forecasts.

Repository policy: one feature/fix per PR, bugs prioritized. Existing actual test command is `CONTAINER_ENGINE=docker dev/test.sh` (or `dev/test.sh` for Podman); tests exercise real database creation and migration chain. Add targeted PHP cases to this existing harness. For UI work additionally capture comparable desktop/mobile screenshots and validate light/dark modes. Recheck full issue timelines and targeted open PR searches before assigning work. Exclude occupied upcoming-payment count #1191, theme cookie #1190, stats #1183, folders #1156 and mark-paid #1139; auth #1181/#1184 already merged.

## WALLOS-01: Diagnose and fix payment-method insertion failures

- Evidence: VERIFIED report [#1185](https://github.com/ellite/Wallos/issues/1185) describes AMEX/Discover insertion failing despite successful logo lookup. HTTP 200 alone does not establish successful storage; root cause unknown.
- Scope: `endpoints/payments/add.php`, `endpoints/payments/search.php`, `tests/run.php` harness with proposed new payment-method case. Reproduce using real migrated schema and sanitized icon metadata; change only the failing validation/storage path. No payment gateway integration or wholesale error framework.
- Acceptance: valid AMEX/Discover insertion and subsequent retrieval succeed, duplicate policy remains clear, malformed logo/input fails safely, per-user isolation holds; no secrets in diagnostics. Run `CONTAINER_ENGINE=docker dev/test.sh` and endpoint smoke in local container.
- Overlap: no matching payment insert PR in sample; refresh payment search. First, 1-3 days. Request exact container version/reproducer if current release works. Value: practical SMB workflow reliability and PHP/SQLite debugging experience.

## WALLOS-02: Add optional Telegram topic ID to notifications

- Evidence: VERIFIED feature request [#1189](https://github.com/ellite/Wallos/issues/1189): notifications currently go to a group's general topic.
- Scope: `endpoints/notifications/savetelegramnotifications.php`, `endpoints/notifications/testtelegramnotifications.php`, `endpoints/cronjobs/sendnotifications.php`, `scripts/notifications.js`, and the next new migration if storage requires it. Inspect UI settings binding before adding fields. Optional explicit topic ID; no overloading group ID or Telegram bot provisioning.
- Acceptance: absent topic preserves existing payload, configured valid topic is included in test and scheduled sends, malformed values are rejected consistently, migrated existing users remain unaffected. Use a local fake Telegram endpoint/request seam; no live messages during tests. Run `CONTAINER_ENGINE=docker dev/test.sh` plus UI smoke.
- Overlap: refresh Telegram-related issues/PRs; no matching PR in sample. Second, independent, 2-3 days. Owner agrees settings/storage shape. Value: enterprise/team notification interoperability and useful SMB automation.

## WALLOS-03: Keep subscription columns aligned with long currency values

- Evidence: VERIFIED UI report [#1149](https://github.com/ellite/Wallos/issues/1149) supplies differing currency widths and expected stable billing/date columns.
- Scope: `scripts/dashboard.js`, `styles/styles.css`, and actual markup in `index.php` after confirming renderer; all exist in inspected tree. Use a constrained layout fix for the affected list. No dashboard redesign, font replacement or unrelated responsive overhaul.
- Acceptance: short/long currency amounts, 320-pixel viewport, 200-percent zoom and translated labels preserve readable amounts and aligned columns without horizontal clipping; light/dark modes remain legible. Capture before/after screenshots with synthetic subscriptions. Run `CONTAINER_ENGINE=docker dev/test.sh`; browser checks are additional, not claimed existing automated coverage.
- Overlap: compare open #1191 dashboard count and #1156 folders changes before editing. Third, independent, 1-2 days. Confirm reproduction on current release. Value: polished international billing UI and a concise visual portfolio artifact.

## WALLOS-04: Honor selected currency display behavior on dashboard previews

- Evidence: VERIFIED request/report [#1142](https://github.com/ellite/Wallos/issues/1142) expects USD amounts displayed in INR after conversion setup. Whether this is a bug or existing setting behavior must be established.
- Scope: `scripts/dashboard.js`, `includes/currency_rates.php`, `includes/currency_formatter.php`, and `endpoints/settings/convert_currency.php`; test via existing `tests/cases/currency_rates_test.php` and proposed dashboard case. Do not change stored original prices or aggregate conversion rules.
- Acceptance: chosen converted/original display mode is consistent on preview tiles, fallback for absent rates is explicit, two users' preferred currencies remain isolated, historical prices are not mutated. Run `CONTAINER_ENGINE=docker dev/test.sh currency`, full suite, and dashboard screenshot check.
- Overlap: recent closed #1165/#1166 already concern rate scope/performance; verify those changes and current settings before coding. Fourth, 1-3 days; serialize with WALLOS-03 renderer edits. Owner agreement on intended setting semantics required. Value: trustworthy spend dashboards across currencies.

## WALLOS-05: Make JSON webhook payload mode explicit and consistent

- Evidence: VERIFIED report [#990](https://github.com/ellite/Wallos/issues/990) shows n8n interpreting payload as form data. Inspected `endpoints/notifications/testwebhooknotifications.php` sets raw POSTFIELDS and only caller-provided headers; this suggests a Content-Type/configuration gap, not a proven serialization bug.
- Scope: that test endpoint, `endpoints/notifications/savewebhooknotifications.php`, `endpoints/cronjobs/sendnotifications.php`, and `scripts/notifications.js`. Reproduce with local receiver; define explicit JSON behavior while preserving intentional custom/form payloads. No arbitrary template engine or SSRF policy weakening.
- Acceptance: JSON mode emits application/json with valid escaped values, custom mode preserves user headers/body, test and scheduled sends agree, malformed JSON fails clearly, quotes/newlines in subscription notes cannot break JSON. Run `CONTAINER_ENGINE=docker dev/test.sh` plus local receiver integration fixtures.
- Overlap: #1000 requests generic notification templating; keep scope narrower. Fifth, 2-4 days. Maintainer must agree backward-compatible mode/default semantics. Value: useful n8n/SMB automation and robust HTTP integration experience.
