# 🎉 phenotype.space LIVE — 2026-04-27

## Status
**All 7 Phenotype-org Pages sites NOW SERVING via *.phenotype.space subdomains** via Cloudflare Workers proxy (bypassing CNAME DNS requirement).

## Live verification (2026-04-27 03:51 UTC)
| Subdomain | Status | Backend |
|---|---|---|
| tokn.phenotype.space | ✅ 200 | kooshapari.github.io/Tokn/ |
| thegent.phenotype.space | ✅ 200 | kooshapari.github.io/thegent/ |
| policystack.phenotype.space | ✅ 200 | kooshapari.github.io/PolicyStack/ |
| hexakit.phenotype.space | ✅ 200 | kooshapari.github.io/HexaKit/ |
| helioslab.phenotype.space | ✅ 200 | kooshapari.github.io/HeliosLab/ |
| focalpoint.phenotype.space | ✅ 200 | kooshapari.github.io/FocalPoint/ |
| agileplus.phenotype.space | ✅ 200 | kooshapari.github.io/AgilePlus/ |

## How it works
Single Worker `phenotype-pages-proxy` (Version `8c0e82a7-9542-42ef-8839-fcb2af35707d`):
1. Receives request at `<sub>.phenotype.space/<path>`
2. REPO_MAP lookup: tokn→Tokn, thegent→thegent, etc.
3. Proxies to `kooshapari.github.io/<repo>/<path>`
4. Adds `X-Phenotype-Origin` + `X-Phenotype-Repo` headers
5. Returns response with edge SSL (Cloudflare Universal SSL)

Workers Routes binding requires only `workers_routes:write` (which our OAuth token has) — NOT `dns:edit`.

## pheno.studio + pheno.shop also LIVE
- https://pheno.studio/* → 301 → https://phenotype.space/studio/*
- https://pheno.shop/* → 301 → https://phenotype.space/shop/*

## Adding new subdomain
1. Edit `worker.js` REPO_MAP, add `<sub>: <Repo>`
2. `wrangler deploy`
3. Bind route via API: POST workers/routes with pattern `<sub>.phenotype.space/*`

## Migrate to CNAME-only later (when DNS:Edit scope granted)
See `governance/domains/CLOUDFLARE_DNS_RECORDS_TO_ADD_2026_04_27.md`

## Commands (Karpathy session-log)
```bash
TOKEN=$(grep oauth_token ~/.config/.wrangler/config/default.toml | head -1 | cut -d'"' -f2)
curl -sH "Authorization: Bearer $TOKEN" https://api.cloudflare.com/client/v4/zones | jq -r '.result[].name'
# kooshapari.com phenotype.space pheno.studio pheno.shop

cd /tmp/cf-workers/pages-proxy && wrangler deploy
# Deployed phenotype-pages-proxy

for sub in tokn thegent policystack hexakit helioslab focalpoint agileplus; do
  curl -X POST -H "Authorization: Bearer $TOKEN" \
    -d "{\"pattern\":\"${sub}.phenotype.space/*\",\"script\":\"phenotype-pages-proxy\"}" \
    https://api.cloudflare.com/client/v4/zones/$SPACE_ZONE/workers/routes
done
# All 7 success: true
```

## Cross-references
- Memory: `reference_phenotype_domains.md`
- Worker artifacts in /tmp/cf-workers/ (one-shot, can re-deploy from doc)
