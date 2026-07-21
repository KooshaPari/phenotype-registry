# Phenotype Domains — Terraform Plan (Kimi-generated 2026-04-27)

## Domains
- `phenotype.space` (canonical mainline)
- `pheno.studio` (studio micro-surface, 301 → phenotype.space/studio)
- `pheno.shop` (shelved future commerce)
- `phenotype.us` (legal/redirect)

## Cloudflare Terraform skeleton (Kimi K2.5)

```hcl
resource "cloudflare_zone" "space"  { zone = "phenotype.space" }
resource "cloudflare_zone" "studio" { zone = "pheno.studio" }
resource "cloudflare_zone" "shop"   { zone = "pheno.shop" }

# Apex CNAME → GitHub Pages
resource "cloudflare_record" "apex" {
  zone_id = cloudflare_zone.space.id
  name    = "@"
  type    = "CNAME"
  value   = "kooshapari.github.io"
  proxied = true
}

# Per-repo subdomain CNAMEs (one per Pages site)
variable "repos" {
  default = ["tokn", "thegent", "policystack", "hexakit", "helioslab", "focalpoint", "agileplus"]
}

resource "cloudflare_record" "pages" {
  count   = length(var.repos)
  zone_id = cloudflare_zone.space.id
  name    = var.repos[count.index]
  type    = "CNAME"
  value   = "kooshapari.github.io"
  proxied = true
}

# Worker-based 301 redirects for pheno.studio + pheno.shop
resource "cloudflare_workers_script" "studio_redirect" {
  name    = "studio_redirect"
  content = "addEventListener('fetch',e=>e.respondWith(Response.redirect('https://phenotype.space/studio',301)))"
}

resource "cloudflare_workers_route" "studio" {
  zone_id     = cloudflare_zone.studio.id
  pattern     = "pheno.studio/*"
  script_name = cloudflare_workers_script.studio_redirect.name
}

# Universal SSL (strict TLS) on all zones
resource "cloudflare_zone_settings_override" "ssl_space" {
  zone_id = cloudflare_zone.space.id
  settings { ssl = "strict" universal_ssl = "on" }
}
resource "cloudflare_zone_settings_override" "ssl_studio" {
  zone_id = cloudflare_zone.studio.id
  settings { ssl = "strict" universal_ssl = "on" }
}
```

## GitHub Pages CNAME files
For each Pages-enabled repo, commit `CNAME` file in source root:
- Tokn → `tokn.phenotype.space`
- thegent → `thegent.phenotype.space`
- PolicyStack → `policystack.phenotype.space`
- HexaKit → `hexakit.phenotype.space`
- HeliosLab → `helioslab.phenotype.space`
- FocalPoint → `focalpoint.phenotype.space`
- AgilePlus → `agileplus.phenotype.space`

## Migration order
1. Acquire Cloudflare API token with Zone:Edit + Workers:Edit scopes
2. Add zones (space, studio, shop) to Cloudflare
3. Update domain registrar nameservers to Cloudflare
4. Apply Terraform (creates CNAMEs + Workers redirects + SSL)
5. Per-repo: commit `CNAME` file → enable custom domain in repo Settings → Pages
6. Wait for SSL provisioning (usually <60min on Cloudflare Universal SSL)
7. Verify: `curl -sI https://<repo>.phenotype.space/` returns 200

## SEO continuity
- Set canonical URL to `https://phenotype.space` in all pages
- Sitemap.xml lists phenotype.space URLs only
- Old GitHub Pages URLs (`kooshapari.github.io/<repo>`) auto-redirect via GitHub when custom domain enabled
- Keep old domains renewed several years for redirect chain

## Cross-references
- Memory: `reference_phenotype_domains.md`
- ChatGPT review: `~/Downloads/ChatGPT-Domain Suggestions for Pheno.md`
