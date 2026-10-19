# Portfolio tooling notes

## Standing rule: card cover colors must match the real image

Every project card on the homepage (`.cover` with a background gradient,
`--c1`/`--c2`) that has a real case-study image as its cover must have its
gradient colors **extracted from that actual image**, not hand-picked to
"look about right." This applies to every case study going forward.

**How to do it:**
1. Run `python extract-palette.py <path-to-cover-image>` — see that file for
   details. It prints the image's real quantized palette (hex, lightness,
   saturation, pixel count).
2. Pick `--c1` (usually the dominant dark/anchor tone) and `--c2` (usually
   the brightest tone that's still genuinely present with a meaningful
   pixel count) from that real list.
3. Set them on the card's `.cover` style in `index.html`:
   `style="--c1:#xxxxxx;--c2:#xxxxxx"`, and set the card's own `--c` (used
   for the hover border glow) to one of those same two colors.

**Cards with no real cover image yet** (as of this note: Würth, ChatCart Pro,
People Core HR, EduPulse, SheetMind AI, VoicePilot, Shift Breaker) keep their
existing hand-picked gradients until a real cover photo is added for them —
there's nothing to extract a palette from otherwise.

## behance-scrape.js

Browser-console scraper for pulling a Behance project's image URLs (run by
the user in their own logged-in browser, since Behance blocks automated
access). See that file's own header comment for usage.

## *-behance-images.json files

The raw scraped output from behance-scrape.js for each project that's been
turned into a case study, kept here for reference / re-curation later.
