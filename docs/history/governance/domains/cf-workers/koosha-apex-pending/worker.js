addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {
  const html = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Koosha Pari</title>
<style>
:root {
  color-scheme: dark;
}
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
body {
  background: #0d1117;
  color: #c9d1d9;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  line-height: 1.6;
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
  min-height: 100vh;
}
h1 {
  color: #f0f6fc;
  margin-bottom: 0.5rem;
  font-size: 2.5rem;
  font-weight: 600;
  letter-spacing: -0.02em;
}
.tagline {
  color: #8b949e;
  margin-bottom: 3rem;
  font-size: 1.1rem;
}
section {
  margin-bottom: 3rem;
}
h2 {
  color: #f0f6fc;
  margin-bottom: 1rem;
  font-size: 1.2rem;
  border-bottom: 1px solid #30363d;
  padding-bottom: 0.5rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
ul {
  list-style: none;
}
li {
  margin-bottom: 0.75rem;
}
a {
  color: #58a6ff;
  text-decoration: none;
  transition: opacity 0.2s;
}
a:hover {
  text-decoration: underline;
  opacity: 0.8;
}
.subdomains {
  margin-left: 1.5rem;
  margin-top: 0.5rem;
  border-left: 2px solid #30363d;
  padding-left: 1rem;
}
.subdomains li {
  margin-bottom: 0.4rem;
}
.subdomains a {
  color: #79c0ff;
  font-size: 0.95rem;
}
</style>
</head>
<body>
  <section class="hero">
    <h1>Koosha Pari</h1>
    <p class="tagline">Software phenotyping & agentic systems</p>
  </section>
  
  <section class="projects">
    <h2>Active Projects</h2>
    <ul>
      <li><a href="https://phenotype.space">phenotype.space</a></li>
      <li class="subdomains">
        <ul>
          <li><a href="https://tokn.phenotype.space">tokn.phenotype.space</a></li>
          <li><a href="https://thegent.phenotype.space">thegent.phenotype.space</a></li>
          <li><a href="https://policystack.phenotype.space">policystack.phenotype.space</a></li>
          <li><a href="https://hexakit.phenotype.space">hexakit.phenotype.space</a></li>
          <li><a href="https://helioslab.phenotype.space">helioslab.phenotype.space</a></li>
          <li><a href="https://focalpoint.phenotype.space">focalpoint.phenotype.space</a></li>
          <li><a href="https://agileplus.phenotype.space">agileplus.phenotype.space</a></li>
        </ul>
      </li>
    </ul>
  </section>
  
  <section class="org">
    <h2>Org</h2>
    <ul>
      <li><a href="https://github.com/KooshaPari">github.com/KooshaPari</a></li>
      <li><a href="https://phenotype.space">phenotype.space</a></li>
    </ul>
  </section>
</body>
</html>`

  return new Response(html, {
    headers: {
      'content-type': 'text/html; charset=utf-8',
      'cache-control': 'public, max-age=300'
    }
  })
}
