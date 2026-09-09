# Implementation Strategy

Use link-not-copy routing. ResearchLedger changes stay in ResearchLedger. Benchora findings stay in the Benchora artifact `audits/ci-exceptions/2026-09-08-pr107-scorecard-repair-plan.md` once its owner has an authorized checkout. The registry stores this packet and links only.

Do not mutate `domain-roles.json`, `disposition-index.json`, absorption records, schemas, or owner-repo sources. If the Benchora artifact is later committed and published, a separately reviewed registry update may replace the temporary wording with its commit SHA and remote URL.
