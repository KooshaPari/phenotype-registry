# Research

## Repo findings
- Existing Cloudflare worker directory: `governance/domains/cf-workers/`
- Existing deployed worker script: `phenotype-pages-proxy`
- Existing route bindings currently cover:
  - `tokn.phenotype.space/*`
  - `thegent.phenotype.space/*`
  - `policystack.phenotype.space/*`
  - `hexakit.phenotype.space/*`
  - `helioslab.phenotype.space/*`
  - `focalpoint.phenotype.space/*`
  - `agileplus.phenotype.space/*`
- No `phenotype.space/*` route existed when checked

## Cloudflare identity
- Account name: Kooshapari@gmail.com's Account
- Account ID: `49dce512822987e0522f0faeffbcc0c8`

## Domain notes
- Zone ID for `phenotype.space`: `e0aeb3a118c02ae30dbfeaa6c4eaec25`
- Docs already describe the subdomain proxy and route-based deployment model
- Apex needs a separate worker route because the existing proxy only handles subdomains

## Implementation choice
- Use a single HTML response with inline CSS
- Keep styling system-font based and dark-mode first
- Render tech links in monospace for a technical feel

## Deployment verification
- Worker upload method that succeeded: `PUT` to the Workers script endpoint
- Route create response confirmed:
  - pattern: `phenotype.space/*`
  - script: `phenotype-apex-landing`
- `curl -sS https://phenotype.space/` returned HTTP 200 and the new landing HTML
