# -*- coding: utf-8 -*-
"""Build the Brandon Howard merch logo candidates."""
import sys, os, io, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from logolib import Face, run_arc, run_straight, swash, crop, svg

F = {}
def face(n):
    if n not in F:
        F[n] = Face(os.path.join('fonts', n))
    return F[n]

OUT = 'out'
os.makedirs(OUT, exist_ok=True)
marks = []


def dancehall(key, label, arc_font, script_font, tagline,
              arc_size=150, arc_track=34, arc_radius=1450, arc_top=150,
              script_size=430, tag_size=44, tag_track=14, tag_font=None,
              note=''):
    """The Gruene Hall vernacular: arched surname-town at the top, a big script
    below carrying a swash, a letterspaced strap line under it all."""
    a, sc = face(arc_font), face(script_font)
    tf = face(tag_font or arc_font)
    pts, body = [], []

    # cy is derived so the crown of the arc lands at arc_top whatever the radius.
    p, _, q = run_arc(a, 'BRANDON', arc_size, arc_radius,
                      tracking=arc_track, cx=700, cy=arc_top + arc_radius)
    body.append(p); pts += q

    p, _, q = run_straight(sc, 'Howard', script_size, cx=700, baseline=560)
    body.append(p); pts += q

    # Swash is positioned off the script's measured ink, not guessed, so it
    # tucks under the word whatever the face's own width turns out to be.
    sx0 = min(x for x, y in q); sx1 = max(x for x, y in q)
    sy1 = max(y for x, y in q)
    L = (sx1 - sx0) * 0.98
    body.append('<path d="%s"/>' % swash(sx0 + (sx1 - sx0) * 0.02,
                                         sy1 + script_size * 0.045,
                                         L, script_size * 0.052, script_size * 0.030))
    pts += [(sx0, sy1), (sx0 + L, sy1 + script_size * 0.20)]

    if tagline:
        p, _, q = run_straight(tf, tagline, tag_size, tracking=tag_track,
                               cx=700, baseline=sy1 + script_size * 0.30)
        body.append(p); pts += q

    box = crop(pts, 46)
    marks.append(dict(key=key, label=label, family='dancehall', note=note,
                      body='\n'.join(body), box=list(box)))


def marquee(key, label, font, tagline, size=170, track=26, gap=1.30,
            rules=True, note=''):
    """The Alamo vernacular: heavy caps stacked tight, hairline rules top and
    bottom, everything squared off like a painted marquee panel."""
    f = face(font)
    pts, body = [], []
    p, w1, q = run_straight(f, 'BRANDON', size, tracking=track, cx=700, baseline=0)
    body.append(p); pts += q
    p, w2, q = run_straight(f, 'HOWARD', size, tracking=track, cx=700, baseline=size * gap)
    body.append(p); pts += q

    wide = max(w1, w2)
    if rules:
        top = min(y for x, y in pts) - size * 0.30
        bot = max(y for x, y in pts) + size * 0.30
        th = size * 0.055
        for y in (top, bot):
            body.append('<rect x="%.2f" y="%.2f" width="%.2f" height="%.2f"/>'
                        % (700 - wide / 2, y, wide, th))
            pts += [(700 - wide / 2, y), (700 + wide / 2, y + th)]

    if tagline:
        base = max(y for x, y in pts) + size * 0.52
        p, _, q = run_straight(f, tagline, size * 0.235, tracking=size * 0.10,
                               cx=700, baseline=base)
        body.append(p); pts += q

    box = crop(pts, 46)
    marks.append(dict(key=key, label=label, family='marquee', note=note,
                      body='\n'.join(body), box=list(box)))


MOTTO = 'REAL SONGS, NO APOLOGIES'
TAG   = 'NO PRETTY BOY COUNTRY'

dancehall('gh-bodoni', 'Bodoni + Alex Brush', 'BodoniModa-Black.ttf',
          'AlexBrush-Regular.ttf', MOTTO, arc_top=170,
          note='Closest to the Gruene sign: high-contrast serif arch, fine looping script.')

dancehall('gh-bodoni-tag', 'Bodoni + Alex Brush, tagline', 'BodoniModa-Black.ttf',
          'AlexBrush-Regular.ttf', TAG, arc_top=170,
          note='Same mark carrying the tagline instead of the motto.')

dancehall('gh-playfair', 'Playfair + Kaushan', 'PlayfairDisplay-Black.ttf'
          if os.path.exists('fonts/PlayfairDisplay-Black.ttf') else 'Playfair-Black.ttf',
          'KaushanScript-Regular.ttf', MOTTO, script_size=330, arc_track=30, arc_radius=1300,
          note='Heavier brush script. Thicker strokes survive small print and stitching.')

dancehall('gh-rye', 'Rye + Great Vibes', 'Rye-Regular.ttf',
          'GreatVibes-Regular.ttf', MOTTO, arc_size=132, arc_track=22, script_size=380, arc_radius=1250,
          tag_font='BodoniModa-Bold.ttf',
          note='Western slab arch. Reads more saloon, less dance hall.')

marquee('am-archivo', 'Archivo Expanded Black', 'Archivo-ExpBlack.ttf', TAG,
        note='Wide heavy grotesque, closest to the marquee lettering in your photo.')

marquee('am-jost', 'Jost (Futura)', 'Jost-Bold.ttf', TAG, size=165, track=34,
        note='Jost is an open Futura. Futura Std Bold is what the Alamo brand manual actually specifies.')

marquee('am-anton', 'Anton', 'Anton-Regular.ttf', TAG, size=190, track=14,
        note='Condensed and very heavy. Most poster-like of the three.')

# The Alamo direction proper. The wordmark on that marquee is custom lettering,
# not a typeface, so this is Poppins Black (which matches it on stem-to-cap and
# has a truly circular O) carrying a constructed flat-topped A. The shoulder is
# pulled back to 0.35 of a full semicircle: enough to keep the geometric family
# resemblance, not so much that it reproduces the Alamo letter. Tracking is
# tighter than the other marquee marks because the reference sets tight.
marquee('am-alamo', 'Alamo lettering', 'AlamoLike-Black.ttf', TAG, size=168, track=13,
        note='Flat-topped A with a softened shoulder, built rather than set.')

marquee('am-alamo-hat', 'Alamo lettering, small format', 'AlamoLike-Black.ttf', None,
        size=168, track=13,
        note='Hat and pocket lockup, strap line removed.')

marquee('am-alamo-flat', 'Alamo lettering, squared A', 'AlamoLike-Flat.ttf', TAG,
        size=168, track=13,
        note='Same mark with a squared flat top instead of a softened shoulder.')

# Small-format lockups. The strap line is the finest ink in the mark, so on a
# hat front or a pocket it is the first thing to fill in or drop stitches.
# These drop it and let the wordmark grow into the same area instead.
dancehall('gh-bodoni-hat', 'Bodoni + Alex Brush, small format', 'BodoniModa-Black.ttf',
          'AlexBrush-Regular.ttf', None, arc_top=170,
          note='Hat and pocket lockup. Strap line removed so the wordmark can run larger.')

dancehall('gh-playfair-hat', 'Playfair + Kaushan, small format', 'Playfair-Black.ttf',
          'KaushanScript-Regular.ttf', None, script_size=330, arc_track=30, arc_radius=1300,
          note='Hat and pocket lockup, on the heavier script.')

marquee('am-archivo-hat', 'Archivo Expanded Black, small format', 'Archivo-ExpBlack.ttf', None,
        note='Hat and pocket lockup. Rules kept, strap line removed.')

for m in marks:
    io.open(os.path.join(OUT, m['key'] + '.svg'), 'w', encoding='utf-8', newline='\n').write(
        svg(m['body'], m['box'], fg='#141210'))

io.open(os.path.join(OUT, 'marks.json'), 'w', encoding='utf-8').write(
    json.dumps(marks, indent=1))

for m in marks:
    x, y, w, h = m['box']
    print('  %-14s %-26s %5.0f x %-5.0f  %s' % (m['key'], m['label'], w, h, m['note'][:52]))
