# Portfolio tooling notes

## Standing rule: match the real brand color, on the card AND the whole case-study page

Every project with a real case-study image gets retinted in two places —
both are required, not just the homepage card:

### 1. Homepage card cover gradient
The card's `.cover` background gradient (`--c1`/`--c2`) must be **extracted
from that project's actual cover image**, not hand-picked to "look about
right."

### 2. The case-study page's own accent color
The case-study HTML page itself (in `case-studies/`) must override the
site's default cyan accent with that project's own brand color, so the
*entire page* — eyebrow labels, status pill, title's italic emphasis, stat
number glow, card borders, section dividers — reads in that project's real
color, not generic site-cyan. Do this with a small inline `<style>` block
right after the `case.css` link in that page's `<head>`:

```html
<link rel="stylesheet" href="case.css">
<!-- Page accent retinted to <Project>'s own <color name>, sampled from <source> -->
<style>:root{--accent:#xxxxxx;--core:#xxxxxx;--accent-rgb:r,g,b;--core-rgb:r,g,b}</style>
```

`--accent` drives most colored text/borders; `--core` is the brighter
"glow highlight" tone (pick something lighter than `--accent`, not the same
value, or glows look flat). `--accent-rgb`/`--core-rgb` are the same colors
as comma-separated R,G,B triplets — required because `case.css` uses
`rgba(var(--accent-rgb),alpha)` for glow effects, and CSS can't derive RGB
components from a hex variable on its own.

**How to pick the colors:**
1. Run `python extract-palette.py <path-to-cover-image>` — prints the
   image's real quantized palette (hex, lightness, saturation, pixel count).
2. For the **card gradient**: pick `--c1` (usually the dominant dark/anchor
   tone) and `--c2` (the brightest tone genuinely present with a meaningful
   pixel count).
3. For the **page accent**: pick a vivid, legible-on-dark tone — this is
   often *not* the same as `--c1` (which is often too dark for text/glow
   use). Prefer the project's own documented brand hex if you've seen one
   stated in the case study's own source material (e.g. a color-palette
   slide) over a sampled pixel from a product photo — it's more precisely
   "the brand color" than whatever a JPEG happened to compress a swatch to.
4. Set the card's own `--c` (hover border glow) to one of the same two
   gradient colors, and keep the page accent consistent with it.

**Projects with no real cover image yet** (as of this note: Würth, ChatCart
Pro, People Core HR, EduPulse, SheetMind AI, VoicePilot, Shift Breaker) keep
the default site cyan and their existing hand-picked card gradients until a
real cover photo is added for them — there's nothing to extract a palette
from otherwise.

## behance-scrape.js

Browser-console scraper for pulling a Behance project's image URLs (run by
the user in their own logged-in browser, since Behance blocks automated
access). See that file's own header comment for usage.

## *-behance-images.json files

The raw scraped output from behance-scrape.js for each project that's been
turned into a case study, kept here for reference / re-curation later.
