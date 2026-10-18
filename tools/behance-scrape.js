/*
  Behance project image scraper — run in the browser console.

  HOW TO USE
  1. Open the Behance project in your browser (e.g. behance.net/gallery/254858659/CROVE)
  2. Scroll all the way to the bottom of the page first — Behance lazy-loads
     images as you scroll, so anything never scrolled into view won't be in
     the DOM yet and this script won't see it.
  3. Open DevTools (F12 or Ctrl+Shift+I), go to the Console tab.
  4. Paste this whole script in and press Enter.
  5. It prints a list of image URLs and auto-downloads a JSON file
     (<project-name>-images.json) with url + alt text for each one.
  6. To actually download the image FILES (not just the list), run
     downloadAll() after the script finishes (see bottom) — it fetches each
     image and triggers a save-as for all of them, named in order.

  WHAT IT DOES
  - Finds every <img> whose src is a Behance project_modules CDN URL
  - Prefers the highest-resolution version available (from srcset, which
    Behance always includes a "fs_webp" full-size original alongside the
    "1400_webp" display size — this grabs the fs_webp / largest one)
  - De-dupes (Behance sometimes renders the same image in two places)
  - Skips tiny icons/avatars that aren't project content
*/
(function () {
  const seen = new Set();
  const results = [];

  function bestUrlFromSrcset(img) {
    const srcset = img.getAttribute('srcset');
    if (!srcset) return img.src;
    // srcset entries look like: "<url> 1.00x, <url> 1.00x" — Behance's first
    // entry is usually the full-size "fs_webp" original; prefer any entry
    // containing "fs_" (full size) over "_webp" sized variants like 1400_webp.
    const parts = srcset.split(',').map(s => s.trim().split(' ')[0]).filter(Boolean);
    const fullSize = parts.find(u => /\/fs_/.test(u));
    return fullSize || parts[0] || img.src;
  }

  document.querySelectorAll('img[src*="project_modules"]').forEach(img => {
    const url = bestUrlFromSrcset(img);
    if (!url || seen.has(url)) return;
    // skip obvious non-content images (tiny avatars, icons)
    const w = parseInt(img.getAttribute('width') || '0', 10);
    if (w && w < 100) return;
    seen.add(url);
    results.push({
      url,
      alt: img.getAttribute('alt') || '',
      width: img.getAttribute('width') || '',
      height: img.getAttribute('height') || ''
    });
  });

  if (results.length === 0) {
    console.warn('No project images found. Did you scroll to the bottom of the page first? Behance lazy-loads images as you scroll.');
    return;
  }

  console.log(`Found ${results.length} image(s):`);
  console.table(results);

  // auto-download the list as JSON
  const projectName = (document.title || 'behance-project')
    .replace(/\s*\|\s*Behance.*/i, '')
    .replace(/[^a-z0-9]+/gi, '-')
    .replace(/^-+|-+$/g, '')
    .toLowerCase() || 'behance-project';

  const blob = new Blob([JSON.stringify(results, null, 2)], { type: 'application/json' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = `${projectName}-images.json`;
  document.body.appendChild(a);
  a.click();
  a.remove();

  console.log(`Saved ${projectName}-images.json — this file lists every image URL + alt text.`);
  console.log('To download the actual image FILES too, run: downloadAll()');

  // expose a helper to actually fetch + save every image file, in order
  window.downloadAll = async function downloadAll() {
    for (let i = 0; i < results.length; i++) {
      const { url } = results[i];
      try {
        const res = await fetch(url);
        const blob = await res.blob();
        const ext = (url.split('.').pop() || 'png').split('?')[0];
        const a = document.createElement('a');
        a.href = URL.createObjectURL(blob);
        a.download = `${projectName}-${String(i + 1).padStart(2, '0')}.${ext}`;
        document.body.appendChild(a);
        a.click();
        a.remove();
        console.log(`Downloaded ${i + 1}/${results.length}: ${a.download}`);
        // small delay so the browser doesn't choke on firing 20 downloads at once
        await new Promise(r => setTimeout(r, 300));
      } catch (e) {
        console.error(`Failed on image ${i + 1} (${url}):`, e);
      }
    }
    console.log('Done. Check your Downloads folder (your browser may ask to allow multiple downloads — click allow).');
  };

  window.__behanceImages = results; // also left on window in case you want it directly
})();
