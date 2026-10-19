"""
Extract a 2-stop gradient (--c1, --c2) for a project card's .cover background,
sampled from that project's actual case-study cover image — so the card's
color matches what's really in the photo instead of a hand-picked guess.

STANDING RULE (see README.md in this folder): every new case study's homepage
card cover must use colors pulled from its own real cover image via this
script, not arbitrary hex values. Text-only covers (no image yet) are exempt
until a real image is added for them.

USAGE
  python extract-palette.py <path-to-cover-image>

It prints the full quantized palette (hex, lightness, saturation, pixel
count) so you can pick a good --c1 (usually a dark, high-count anchor) and
--c2 (usually a brighter, more saturated accent that's still genuinely
present in the image) by eye — this script does not auto-pick for you,
because "looks good as a gradient" still needs a human judgment call about
which two swatches actually represent the image.

Guidance for picking the pair once you see the palette:
  - --c1: usually the darkest color with a high pixel count (the dominant
    background/shadow tone) — this sits at the gradient's 135deg start.
  - --c2: usually the most saturated/brightest color that still has a
    meaningful pixel count (not a 1%-of-image outlier) — the accent the
    gradient lifts into.
  - If the image is mostly neutral/grey (e.g. a studio product shot), it's
    fine for --c2 to also be a muted tone — don't invent saturation that
    isn't in the photo.
"""
import sys
from PIL import Image
import colorsys

def get_palette(path, n=8):
    im = Image.open(path).convert('RGB')
    im = im.resize((200, 200))
    pal = im.quantize(colors=n, method=Image.MEDIANCUT)
    palette = pal.getpalette()
    color_counts = sorted(pal.getcolors(), reverse=True)
    out = []
    for count, idx in color_counts:
        r, g, b = palette[idx*3:idx*3+3]
        h, l, s = colorsys.rgb_to_hls(r/255, g/255, b/255)
        out.append({'hex': f'#{r:02x}{g:02x}{b:02x}', 'count': count, 'l': l, 's': s})
    return out

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: python extract-palette.py <path-to-cover-image>")
        sys.exit(1)
    path = sys.argv[1]
    print(f"Palette for {path}:\n")
    for c in get_palette(path):
        print(f"  {c['hex']}  L={c['l']:.2f}  S={c['s']:.2f}  count={c['count']}")
