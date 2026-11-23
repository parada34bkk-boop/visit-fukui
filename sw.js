/* Visit Fukui offline support.
   - The app itself (this site's files): try the network first so updates show up, fall back to the saved copy offline.
   - Map tiles, map fonts and Google fonts: use the saved copy if there is one, refresh it in the background.
     Only places you've already looked at are saved, and the tile store is kept to a fixed size.
   - Discover Fukui photos are not saved (they belong to Discover Fukui and would fill the phone). */
const APP = "vf-app-v1";
const TILES = "vf-tiles-v1";
const MAX_TILES = 1500;
const SHELL = ["./", "index.html", "data.js", "fukui-shape.js", "manifest.webmanifest",
  "vendor/maplibre/maplibre-gl.js", "vendor/maplibre/maplibre-gl.css",
  "images/ono-castle-sky-s.jpg", "icons/icon-192.png"];

self.addEventListener("install", e => {
  e.waitUntil(caches.open(APP).then(c => c.addAll(SHELL)).then(() => self.skipWaiting()));
});
self.addEventListener("activate", e => {
  e.waitUntil(caches.keys()
    .then(keys => Promise.all(keys.filter(k => k !== APP && k !== TILES).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
});

async function trim(){
  const c = await caches.open(TILES), keys = await c.keys();
  for (let i = 0; i < keys.length - MAX_TILES; i++) await c.delete(keys[i]);
}

self.addEventListener("fetch", e => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);

  if (url.origin === location.origin){
    e.respondWith(fetch(req).then(res => {
      if (res.ok){ const copy = res.clone(); caches.open(APP).then(c => c.put(req, copy)); }
      return res;
    }).catch(() => caches.match(req, {ignoreSearch: true}).then(r => r || caches.match("index.html"))));
    return;
  }

  if (/(^|\.)openfreemap\.org$|fonts\.(googleapis|gstatic)\.com$/.test(url.hostname)){
    e.respondWith(caches.open(TILES).then(async c => {
      const hit = await c.match(req);
      const net = fetch(req).then(res => {
        if (res.ok){ c.put(req, res.clone()); trim(); }
        return res;
      }).catch(() => hit);
      return hit || net;
    }));
  }
});
