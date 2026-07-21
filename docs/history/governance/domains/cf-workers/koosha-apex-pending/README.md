# kooshapari-apex-landing — PENDING USER REVIEW

LLM-generated (Kimi K2.5 via OmniRoute) draft of a Cloudflare Worker for the
kooshapari.com apex landing page.

**Status:** NOT deployed. The autonomous /loop session generated this asset
but auto-deployment to the personal production apex was correctly blocked by
the sandbox — only phenotype.space / pheno.studio / pheno.shop deployments
were pre-authorized.

**To deploy** (after review):
```bash
TOKEN=$(grep oauth_token ~/.config/.wrangler/config/default.toml | head -1 | cut -d'"' -f2)
ACCT=$(curl -s -H "Authorization: Bearer $TOKEN" https://api.cloudflare.com/client/v4/accounts | jq -r '.result[0].id')
curl -X PUT -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/javascript" \
  --data-binary @worker.js \
  "https://api.cloudflare.com/client/v4/accounts/$ACCT/workers/scripts/kooshapari-apex-landing"
curl -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  -d '{"pattern":"kooshapari.com/*","script":"kooshapari-apex-landing"}' \
  "https://api.cloudflare.com/client/v4/zones/6c9edab581e9c7b8fdb6a83adc6878ea/workers/routes"
```

**Zone ID:** 6c9edab581e9c7b8fdb6a83adc6878ea (kooshapari.com, active)

**Source:** `/tmp/loop-2026-04-27-late/kimi-koosha-apex2.log` (Kimi K2.5 retry)
