addEventListener('fetch', event => {
  const url = new URL(event.request.url);
  const target = 'https://phenotype.space/shop' + url.pathname + url.search;
  event.respondWith(Response.redirect(target, 301));
});
