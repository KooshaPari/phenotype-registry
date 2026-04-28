// Proxies *.phenotype.space → kooshapari.github.io/<repo>/<path>
// Subdomain → repo mapping
const REPO_MAP = {
  'tokn': 'Tokn',
  'thegent': 'thegent',
  'policystack': 'PolicyStack',
  'hexakit': 'HexaKit',
  'helioslab': 'HeliosLab',
  'focalpoint': 'FocalPoint',
  'agileplus': 'AgilePlus',
};

addEventListener('fetch', event => {
  event.respondWith(handle(event.request));
});

async function handle(request) {
  const url = new URL(request.url);
  const host = url.hostname;
  
  // Extract subdomain from host (e.g., "tokn.phenotype.space" → "tokn")
  const subdomain = host.split('.')[0];
  const repo = REPO_MAP[subdomain.toLowerCase()];
  
  if (!repo) {
    return new Response(`No mapping for subdomain: ${subdomain}\n\nKnown: ${Object.keys(REPO_MAP).join(', ')}`, { status: 404 });
  }
  
  // Map to GitHub Pages
  const ghPath = `/${repo}${url.pathname}`;
  const ghUrl = `https://kooshapari.github.io${ghPath}${url.search}`;
  
  const ghReq = new Request(ghUrl, {
    method: request.method,
    headers: request.headers,
    body: request.body,
    redirect: 'follow',
  });
  
  const ghRes = await fetch(ghReq);
  
  // Return response with CORS + canonical link
  const newHeaders = new Headers(ghRes.headers);
  newHeaders.set('X-Phenotype-Origin', 'kooshapari.github.io');
  newHeaders.set('X-Phenotype-Repo', repo);
  
  return new Response(ghRes.body, {
    status: ghRes.status,
    statusText: ghRes.statusText,
    headers: newHeaders,
  });
}
