# -*- coding: utf-8 -*-
"""Give a geometric black face a flat-topped A, with the shoulder as a dial.

The Alamo A is a full half-round arch on two vertical legs. Copying that exactly
is the most recognisable thing about their lettering, so `arch` here controls how
much of it to take: 1.0 is the literal semicircle, 0.0 is a squared flat top, and
the middle is a flat top with softened shoulders that reads as its own letter.

The A is constructed from the base font's own stem width and cap height and
written into the glyf table, so shaping, kerning and every existing code path
keep working with no special cases at the composition layer.
"""
import os
from fontTools.ttLib import TTFont
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.boundsPen import BoundsPen

K = 0.5522847498307936        # circle-to-cubic constant


def ink(gs, name):
    bp = BoundsPen(gs)
    gs[name].draw(bp)
    return bp.bounds


def draw_A(pen, W, H, S, Rc, bar_y, bar_t):
    """Flat-topped A with shoulder radius Rc. Author coords are y-up."""
    ri = Rc - S                                  # inner shoulder radius

    pen.moveTo((0, 0))
    pen.lineTo((0, H - Rc))
    if Rc > 0:
        pen.curveTo((0, H - Rc + Rc * K), (Rc - Rc * K, H), (Rc, H))
        pen.lineTo((W - Rc, H))
        pen.curveTo((W - Rc + Rc * K, H), (W, H - Rc + Rc * K), (W, H - Rc))
    else:
        pen.lineTo((0, H))
        pen.lineTo((W, H))
    pen.lineTo((W, 0))

    pen.lineTo((W - S, 0))
    if ri > 0:
        pen.lineTo((W - S, H - Rc))
        pen.curveTo((W - S, H - Rc + ri * K), (W - Rc + ri * K, H - S), (W - Rc, H - S))
        pen.lineTo((Rc, H - S))
        pen.curveTo((Rc - ri * K, H - S), (S, H - Rc + ri * K), (S, H - Rc))
    else:
        pen.lineTo((W - S, H - S))
        pen.lineTo((S, H - S))
    pen.lineTo((S, 0))
    pen.closePath()

    # Separate contour. The area under the shoulder has winding zero because the
    # shape is open along the baseline, so a nonzero fill paints this bar in
    # whichever direction it happens to be wound.
    pen.moveTo((S, bar_y))
    pen.lineTo((W - S, bar_y))
    pen.lineTo((W - S, bar_y + bar_t))
    pen.lineTo((S, bar_y + bar_t))
    pen.closePath()


def build(src, dst, arch=1.0, bar_frac=0.20, bar_weight=0.92, width_from='O'):
    f = TTFont(src)
    gs = f.getGlyphSet()
    upem = f['head'].unitsPerEm

    hb, ib, wb = ink(gs, 'H'), ink(gs, 'I'), ink(gs, width_from)
    H = hb[3] - hb[1]                 # cap height
    S = ib[2] - ib[0]                 # stem width
    W = wb[2] - wb[0]                 # match the round letters' width
    Rc = (W / 2.0) * arch

    tpen = TTGlyphPen(gs)
    draw_A(Cu2QuPen(tpen, max_err=upem / 2000.0),
           W, H, S, Rc, H * bar_frac, S * bar_weight)
    glyph = tpen.glyph()
    glyph.recalcBounds(f['glyf'])
    f['glyf']['A'] = glyph
    f['hmtx']['A'] = (f['hmtx']['O'][0], wb[0])

    for rec in f['name'].names:                   # avoid clashing with real Poppins
        try:
            v = rec.toUnicode()
        except Exception:
            continue
        if 'Poppins' in v:
            rec.string = v.replace('Poppins', 'AlamoLike')
    f.save(dst)
    return dict(dst=dst, arch=arch, H=H, S=S, W=W, Rc=Rc)


if __name__ == '__main__':
    # 0.35 is the shipping default: a flat top with softened shoulders, which
    # keeps the geometric family resemblance without reproducing the Alamo
    # semicircle. 0.00 is the squared alternate and is the least derivative
    # letter of the set.
    for dst, a in [('fonts/AlamoLike-Black.ttf', 0.35),
                   ('fonts/AlamoLike-Flat.ttf', 0.00)]:
        r = build('fonts/Poppins-Black.ttf', dst, arch=a)
        print('  arch %-5.2f  shoulder radius %4.0f of half-width %4.0f  -> %s'
              % (a, r['Rc'], r['W'] / 2, os.path.basename(r['dst'])))
