# -*- coding: utf-8 -*-
"""Build the Brandon Howard Band merch logo candidates."""
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

CX = 700.0


def shift(body, pts, dy):
    """Move a finished run vertically, keeping its bounds honest."""
    return ('<g transform="translate(0,%.3f)">%s</g>' % (dy, body),
            [(x, y + dy) for x, y in pts])


def dancehall(key, label, arc_font, script_font,
              pre='THE', arc_text='BRANDON', script_text='Howard', post='BAND',
              tagline=None,
              arc_size=150, arc_track=34, arc_radius=1450, arc_top=196,
              script_size=430, script_base=560,
              pre_size=52, pre_track=32, post_size=68, post_track=36,
              tag_size=40, tag_track=15, caps_font=None, note=''):
    """The Gruene Hall vernacular.

    Gruene stacks GRUENE arched, Hall in script under a swash, then a small
    letterspaced strap line. A four word name needs two more slots than that, so
    THE sits above the arch and BAND takes the strap line position, which leaves
    the whole name reading straight down the mark.
    """
    a, sc = face(arc_font), face(script_font)
    cf = face(caps_font or arc_font)
    pts, body = [], []

    # cy is derived so the crown of the arc lands at arc_top whatever the radius
    p, _, q = run_arc(a, arc_text, arc_size, arc_radius,
                      tracking=arc_track, cx=CX, cy=arc_top + arc_radius)
    body.append(p); pts += q
    arc_ceiling = min(y for x, y in q)

    if pre:
        # sits off the measured top of the arch, not a guessed offset, so it
        # clears the crown whatever radius and size the arch ends up at
        p, _, q = run_straight(cf, pre, pre_size, tracking=pre_track, cx=CX, baseline=0)
        top = max(y for x, y in q)
        p, q = shift(p, q, arc_ceiling - pre_size * 0.42 - top)
        body.append(p); pts += q

    p, _, q = run_straight(sc, script_text, script_size, cx=CX, baseline=script_base)
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

    y = sy1 + script_size * 0.30
    if post:
        p, _, q = run_straight(cf, post, post_size, tracking=post_track, cx=CX, baseline=y)
        body.append(p); pts += q
        y = max(yy for xx, yy in q) + post_size * 0.62

    if tagline:
        p, _, q = run_straight(cf, tagline, tag_size, tracking=tag_track, cx=CX, baseline=y)
        body.append(p); pts += q

    marks.append(dict(key=key, label=label, family='dancehall', note=note,
                      body='\n'.join(body), box=list(crop(pts, 46))))


def marquee(key, label, font, pre='THE', lines=('BRANDON', 'HOWARD'), post='BAND',
            tagline=None, size=170, track=26, gap=1.30, note=''):
    """The Alamo vernacular: heavy caps stacked tight inside a ruled panel.

    THE and BAND are set into breaks in the rules rather than given lines of
    their own. That is a real marquee device, it keeps the two big words as the
    only full-height lines, and it absorbs the extra words a band name brings
    without turning the mark into a five deck stack.
    """
    f = face(font)
    pts, body = [], []
    widest = 0.0
    for i, line in enumerate(lines):
        p, w, q = run_straight(f, line, size, tracking=track, cx=CX, baseline=size * gap * i)
        body.append(p); pts += q
        widest = max(widest, w)

    x0, x1 = CX - widest / 2, CX + widest / 2
    th = size * 0.055
    top = min(y for x, y in pts) - size * 0.34
    bot = max(y for x, y in pts) + size * 0.34

    def rule(y, word):
        if not word:
            body.append('<rect x="%.2f" y="%.2f" width="%.2f" height="%.2f"/>'
                        % (x0, y, widest, th))
            pts.extend([(x0, y), (x1, y + th)])
            return
        ws = size * 0.235
        p, w, q = run_straight(f, word, ws, tracking=size * 0.09, cx=CX, baseline=0)
        wtop, wbot = min(yy for xx, yy in q), max(yy for xx, yy in q)
        # drop the word so its cap height straddles the rule
        p, q = shift(p, q, y + th / 2 - (wtop + wbot) / 2)
        body.append(p); pts.extend(q)
        half = (max(xx for xx, yy in q) - min(xx for xx, yy in q)) / 2 + size * 0.16
        for a, b in ((x0, CX - half), (CX + half, x1)):
            if b > a:
                body.append('<rect x="%.2f" y="%.2f" width="%.2f" height="%.2f"/>'
                            % (a, y, b - a, th))
                pts.extend([(a, y), (b, y + th)])

    rule(top, pre)
    rule(bot, post)

    if tagline:
        base = max(y for x, y in pts) + size * 0.52
        p, _, q = run_straight(f, tagline, size * 0.215, tracking=size * 0.10,
                               cx=CX, baseline=base)
        body.append(p); pts += q

    marks.append(dict(key=key, label=label, family='marquee', note=note,
                      body='\n'.join(body), box=list(crop(pts, 46))))


MOTTO = 'REAL SONGS, NO APOLOGIES'
TAG   = 'NO PRETTY BOY COUNTRY'

# ── Dance hall ───────────────────────────────────────────────────────────────
dancehall('gh-bodoni', 'Bodoni + Alex Brush', 'BodoniModa-Black.ttf',
          'AlexBrush-Regular.ttf',
          note='Closest to the Gruene sign. The full name reads straight down the mark.')

# The other way to map a two part name onto this layout, and the one that copies
# Gruene most exactly: the identifying words arched, the type word in script,
# strap line underneath. GRUENE over Hall becomes BRANDON HOWARD over Band.
dancehall('gh-bodoni-tag', 'Bodoni + Alex Brush, Gruene parallel', 'BodoniModa-Black.ttf',
          'AlexBrush-Regular.ttf', pre=None, arc_text='BRANDON HOWARD',
          script_text='Band', post=None, tagline=MOTTO,
          arc_size=116, arc_track=26, arc_radius=1250, arc_top=170,
          note='Maps the name the way Gruene maps its own: place words arched, type word in script.')

dancehall('gh-bodoni-hat', 'Bodoni + Alex Brush, small format', 'BodoniModa-Black.ttf',
          'AlexBrush-Regular.ttf', post_size=76, post_track=40,
          note='Hat and pocket lockup. BAND set heavier since it cannot be dropped.')

dancehall('gh-playfair', 'Playfair + Kaushan', 'Playfair-Black.ttf',
          'KaushanScript-Regular.ttf', script_size=330, arc_track=30, arc_radius=1300,
          note='Heavier brush script. Thicker strokes survive small print and stitching.')

dancehall('gh-playfair-hat', 'Playfair + Kaushan, small format', 'Playfair-Black.ttf',
          'KaushanScript-Regular.ttf', script_size=330, arc_track=30, arc_radius=1300,
          post_size=76, post_track=40,
          note='Hat and pocket lockup, on the heavier script.')

dancehall('gh-rye', 'Rye + Great Vibes', 'Rye-Regular.ttf', 'GreatVibes-Regular.ttf',
          arc_size=132, arc_track=22, script_size=380, arc_radius=1250,
          caps_font='BodoniModa-Bold.ttf',
          note='Western slab arch. Reads more saloon, less dance hall.')

# ── Marquee ──────────────────────────────────────────────────────────────────
# The wordmark on that marquee is custom lettering, not a typeface, so this is
# Poppins Black (which matches it on stem to cap and has a truly circular O)
# carrying a constructed flat topped A with the shoulder pulled back to 0.35 of
# a full semicircle. Tracking is tighter here because the reference sets tight.
marquee('am-alamo', 'Alamo lettering', 'AlamoLike-Black.ttf', tagline=TAG,
        size=168, track=13,
        note='Flat-topped A with a softened shoulder, built rather than set.')

marquee('am-alamo-hat', 'Alamo lettering, small format', 'AlamoLike-Black.ttf',
        tagline=None, size=168, track=13,
        note='Hat and pocket lockup, tagline removed.')

marquee('am-alamo-flat', 'Alamo lettering, squared A', 'AlamoLike-Flat.ttf', tagline=TAG,
        size=168, track=13,
        note='Same mark with a squared flat top instead of a softened shoulder.')

marquee('am-archivo', 'Archivo Expanded Black', 'Archivo-ExpBlack.ttf', tagline=TAG,
        note='Wide heavy grotesque, closest to the marquee lettering in the photo.')

marquee('am-archivo-hat', 'Archivo Expanded Black, small format', 'Archivo-ExpBlack.ttf',
        tagline=None, note='Hat and pocket lockup, tagline removed.')

marquee('am-jost', 'Jost (Futura)', 'Jost-Bold.ttf', tagline=TAG, size=165, track=34,
        note='Jost is an open Futura. Futura Std Bold is what the Alamo manual specifies for DRAFTHOUSE CINEMA.')

marquee('am-anton', 'Anton', 'Anton-Regular.ttf', tagline=TAG, size=190, track=14,
        note='Condensed and very heavy. Most poster-like of the three.')

for m in marks:
    io.open(os.path.join(OUT, m['key'] + '.svg'), 'w', encoding='utf-8', newline='\n').write(
        svg(m['body'], m['box'], fg='#141210'))

io.open(os.path.join(OUT, 'marks.json'), 'w', encoding='utf-8').write(
    json.dumps(marks, indent=1))

for m in marks:
    x, y, w, h = m['box']
    print('  %-16s %-38s %5.0f x %-5.0f' % (m['key'], m['label'], w, h))
