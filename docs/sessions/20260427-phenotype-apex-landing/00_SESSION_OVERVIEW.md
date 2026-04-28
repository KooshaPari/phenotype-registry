# Session Overview

## Goal
Create and deploy a Cloudflare Worker for the `phenotype.space` apex that serves a minimal landing page and binds the `phenotype.space/*` route.

## Success Criteria
- Worker code exists in governance under `governance/domains/cf-workers/apex-landing/worker.js`
- Live deployment is reachable at `https://phenotype.space/`
- Route `phenotype.space/*` is bound to the new worker
- A verification curl returns HTTP 200
- Changes are committed and pushed

## Constraints
- Keep the page minimal and dark themed
- Use the existing Wrangler OAuth token
- Stop and document if the apex route is already claimed

## Current Status
- Existing subdomain route worker confirmed
- Apex route conflict check passed
- Worker uploaded as `phenotype-apex-landing`
- Route `phenotype.space/*` bound successfully
- Live verification returned HTTP 200 from `https://phenotype.space/`
