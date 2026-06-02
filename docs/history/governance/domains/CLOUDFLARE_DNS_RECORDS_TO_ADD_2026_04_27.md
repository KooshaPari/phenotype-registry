# Cloudflare DNS Records to Add — 2026-04-27

## Status
- ✅ All 4 zones present in Cloudflare: `kooshapari.com`, `phenotype.space`, `pheno.studio`, `pheno.shop`
- ✅ Porkbun nameservers updated to Cloudflare (per user 2026-04-27)
- ✅ wrangler OAuth token authenticated (kooshapari@gmail.com)
- ❌ wrangler OAuth scopes lack `dns:edit` — DNS API calls return `10000 Authentication error`

## What's blocking
The wrangler OAuth token has these scopes:
```
account:read user:read workers:write workers_kv:write workers_routes:write
workers_scripts:write workers_tail:read d1:write pages:write zone:read
ssl_certs:write ai:write ai-search:write queues:write pipelines:write
secrets_store:write artifacts:write flagship:write containers:write
cloudchamber:write connectivity:admin email_routing:write email_sending:write
browser:write offline_access
```

Note: ❌ NO `dns:edit` scope. DNS record creation requires either:
1. New CF API token with `Zone.DNS:Edit` scope (user creates in dashboard), OR
2. Re-auth wrangler with broader scopes (`wrangler logout` then `wrangler login`)

## DNS records needed (zone: phenotype.space)

Add these CNAME records via Cloudflare dashboard → phenotype.space → DNS → Records:

| Name | Type | Content | Proxy | TTL |
|---|---|---|---|---|
| tokn | CNAME | kooshapari.github.io | ✅ Proxied | Auto |
| thegent | CNAME | kooshapari.github.io | ✅ Proxied | Auto |
| policystack | CNAME | kooshapari.github.io | ✅ Proxied | Auto |
| hexakit | CNAME | kooshapari.github.io | ✅ Proxied | Auto |
| helioslab | CNAME | kooshapari.github.io | ✅ Proxied | Auto |
| focalpoint | CNAME | kooshapari.github.io | ✅ Proxied | Auto |
| agileplus | CNAME | kooshapari.github.io | ✅ Proxied | Auto |

(Each CNAME creates `<name>.phenotype.space → kooshapari.github.io`. CNAME files are already merged in each repo at root + `docs/.vitepress/public/CNAME` per session 2026-04-27 work.)

## DNS records needed (zone: pheno.studio + pheno.shop)

For 301 redirects via Cloudflare Workers, deploy a single Worker that handles `*.pheno.studio` and `*.pheno.shop`:

| Zone | Pattern | Worker |
|---|---|---|
| pheno.studio | `pheno.studio/*` | studio-redirect |
| pheno.studio | `www.pheno.studio/*` | studio-redirect |
| pheno.shop | `pheno.shop/*` | shop-redirect |
| pheno.shop | `www.pheno.shop/*` | shop-redirect |

Worker `studio-redirect` content:
```js
addEventListener('fetch', e => {
  const u = new URL(e.request.url);
  e.respondWith(Response.redirect('https://phenotype.space/studio' + u.pathname + u.search, 301));
});
```

Worker `shop-redirect` is identical but redirects to `https://phenotype.space/shop` + path.

The `workers:write` and `workers_routes:write` scopes ARE present, so these Workers + routes CAN be deployed via wrangler now. DNS A/AAAA records for the zones are auto-managed by CF when Workers routes are bound.

## Verification (post-DNS)
```bash
# Wait 60s after creating CNAME
curl -sI https://tokn.phenotype.space/ | head -3
# Expected: HTTP 200 + content-type text/html (GitHub Pages serving Tokn docs)
```

## State (verified via wrangler/curl 2026-04-27)
- All 4 zones present
- Account ID: `49dce512822987e0522f0faeffbcc0c8`
- phenotype.space zone ID: `e0aeb3a118c02ae30dbfeaa6c4eaec25`
- pheno.studio zone ID: (see `wrangler whoami`)
- pheno.shop zone ID: (see `wrangler whoami`)

## Cross-references
- CNAME files merged in 7 repos via session 2026-04-27 (Tokn #27, thegent #986, PolicyStack #18, HexaKit #120, HeliosLab #69, FocalPoint #27, AgilePlus #443)
- Terraform plan (alternative): `governance/domains/PHENOTYPE_DOMAINS_TF_PLAN_2026_04_27.md`
- Memory: `reference_phenotype_domains.md`
