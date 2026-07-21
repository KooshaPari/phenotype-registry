addEventListener('fetch', event => {
  event.respondWith(handle(event.request));
});

function html() {
  return `<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="color-scheme" content="dark" />
    <title>Phenotype</title>
    <style>
      :root {
        color-scheme: dark;
        --bg: #090b0f;
        --panel: rgba(15, 18, 24, 0.86);
        --text: #eef2f7;
        --muted: #95a0b1;
        --line: rgba(151, 165, 184, 0.16);
        --accent: #d7e2f1;
      }

      * {
        box-sizing: border-box;
      }

      html,
      body {
        margin: 0;
        min-height: 100%;
        background:
          radial-gradient(circle at top, rgba(59, 76, 99, 0.24), transparent 42%),
          linear-gradient(180deg, #0d1117 0%, var(--bg) 100%);
        color: var(--text);
        font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      }

      body {
        display: grid;
        place-items: center;
        padding: 32px 20px;
      }

      main {
        width: min(720px, 100%);
        padding: 32px;
        border: 1px solid var(--line);
        border-radius: 24px;
        background: var(--panel);
        box-shadow: 0 24px 80px rgba(0, 0, 0, 0.35);
        backdrop-filter: blur(18px);
      }

      .wordmark {
        margin: 0 0 12px;
        font-size: clamp(2.6rem, 9vw, 5.2rem);
        line-height: 0.95;
        letter-spacing: -0.06em;
        font-weight: 700;
      }

      .tagline {
        margin: 0 0 28px;
        max-width: 36rem;
        color: var(--muted);
        font-size: 1.05rem;
        line-height: 1.6;
      }

      .grid {
        display: grid;
        gap: 12px;
      }

      .section-label {
        margin: 0 0 8px;
        color: var(--muted);
        font-size: 0.78rem;
        letter-spacing: 0.14em;
        text-transform: uppercase;
      }

      .links {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
      }

      a {
        color: var(--text);
        text-decoration: none;
      }

      .tech-link {
        display: inline-flex;
        align-items: center;
        gap: 0.45rem;
        padding: 10px 12px;
        border: 1px solid var(--line);
        border-radius: 999px;
        background: rgba(255, 255, 255, 0.03);
        font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, monospace;
        font-size: 0.94rem;
        transition: transform 140ms ease, border-color 140ms ease, background 140ms ease;
      }

      .tech-link:hover {
        transform: translateY(-1px);
        border-color: rgba(215, 226, 241, 0.4);
        background: rgba(255, 255, 255, 0.06);
      }

      .footer {
        margin-top: 28px;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        gap: 16px;
        color: var(--muted);
        font-size: 0.92rem;
      }

      .source {
        color: var(--accent);
      }

      @media (max-width: 520px) {
        main {
          padding: 24px;
          border-radius: 20px;
        }

        .footer {
          flex-direction: column;
        }
      }
    </style>
  </head>
  <body>
    <main>
      <h1 class="wordmark">Phenotype</h1>
      <p class="tagline">Software phenotyping &amp; agentic systems.</p>

      <div class="grid">
        <p class="section-label">Products</p>
        <nav class="links" aria-label="Phenotype products">
          <a class="tech-link" href="https://tokn.phenotype.space">tokn</a>
          <a class="tech-link" href="https://thegent.phenotype.space">thegent</a>
          <a class="tech-link" href="https://agileplus.phenotype.space">agileplus</a>
          <a class="tech-link" href="https://hexakit.phenotype.space">hexakit</a>
          <a class="tech-link" href="https://helioslab.phenotype.space">helioslab</a>
          <a class="tech-link" href="https://heliosapp.phenotype.space">heliosapp</a>
          <a class="tech-link" href="https://policystack.phenotype.space">policystack</a>
          <a class="tech-link" href="https://focalpoint.phenotype.space">focalpoint</a>
          <a class="tech-link" href="https://hwledger.phenotype.space">hwledger</a>
          <a class="tech-link" href="https://civis.phenotype.space">civis</a>
          <a class="tech-link" href="https://pheno.phenotype.space">pheno</a>
          <a class="tech-link" href="https://cliproxyapi.phenotype.space">cliproxyapi</a>
        </nav>

        <p class="section-label" style="margin-top:16px">Demos</p>
        <nav class="links" aria-label="Phenotype demos">
          <a class="tech-link" href="https://dino.phenotype.space">dino</a>
          <a class="tech-link" href="https://parpoura.phenotype.space">parpoura</a>
        </nav>

        <p class="section-label" style="margin-top:16px">Landings</p>
        <nav class="links" aria-label="Phenotype landings">
          <a class="tech-link" href="https://hwledger-landing.phenotype.space">hwledger-landing</a>
          <a class="tech-link" href="https://phenokits-landing.phenotype.space">phenokits-landing</a>
          <a class="tech-link" href="https://projects-landing.phenotype.space">projects-landing</a>
        </nav>
      </div>

      <div class="footer">
        <span>phenotype.space</span>
        <a class="source" href="https://github.com/KooshaPari" rel="noreferrer">View source</a>
      </div>
    </main>
  </body>
</html>`;
}

async function handle(request) {
  if (request.method === 'HEAD') {
    return new Response(null, {
      headers: {
        'content-type': 'text/html; charset=utf-8',
      },
    });
  }

  return new Response(html(), {
    headers: {
      'content-type': 'text/html; charset=utf-8',
      'cache-control': 'public, max-age=300',
    },
  });
}
