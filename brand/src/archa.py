# -*- coding: utf-8 -*-
"""Give a geometric black face the Alamo arch-A.

The Alamo wordmark is custom lettering, not a typeface, and its single most
distinctive move is the A: no pointed apex, just a half-round arch on two
vertical legs with a low crossbar, exactly like an 'n' with a bar. No shipping
font has that letter, so it is constructed here from the base font's own stem
width and cap height and written back into the glyf table. Doing it inside the
font rather than at the composition layer means shaping, kerning and every
existing code path keep working untouched.
"""
import sys, os
from fontTools.ttLib import TTFont
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.boundsPen import BoundsPen

K = 0.5522847498307936        # circle-to-cubic constant


def ink(font, gs, name):
    bp = BoundsPen(gs)
    gs[name].draw(bp)
    return bp.bounds


def draw_arch_A(pen, W, H, S, bar_y, bar_t):
    """An 'n' arch with a crossbar. Author coords are y-up, like the font."""
    R = W / 2.0
    r = R - S
    cy = H - R                      # centre of the arch

    pen.moveTo((0, 0))
    pen.lineTo((0, cy))
    # outer half circle, left shoulder then right shoulder
    pen.curveTo((0, cy + R * K), (R - R * K, H), (R, H))
    pen.curveTo((R + R * K, H), (W, cy + R * K), (W, cy))
    pen.lineTo((W, 0))
    pen.lineTo((W - S, 0))
    pen.lineTo((W - S, cy))
    # inner half circle, coming back the other way
    pen.curveTo((W - S, cy + r * K), (R + r * K, H - S), (R, H - S))
    pen.curveTo((R - r * K, H - S), (S, cy + r * K), (S, cy))
    pen.lineTo((S, 0))
    pen.closePath()

    # The bar is its own contour. The area under the arch has winding zero
    # because the shape is open along the baseline, so a nonzero fill paints
    # this rectangle in whichever direction it is wound.
    pen.moveTo((S, bar_y))
    pen.lineTo((W - S, bar_y))
    pen.lineTo((W - S, bar_y + bar_t))
    pen.lineTo((S, bar_y + bar_t))
    pen.closePath()


def build(src, dst, bar_frac=0.20, bar_weight=0.92, width_from='O'):
    f = TTFont(src)
    gs = f.getGlyphSet()
    upem = f['head'].unitsPerEm

    hb = ink(f, gs, 'H')
    ib = ink(f, gs, 'I')
    wb = ink(f, gs, width_from)

    H = hb[3] - hb[1]                 # cap height
    S = ib[2] - ib[0]                 # stem width
    W = wb[2] - wb[0]                 # match the round letters' width

    tpen = TTGlyphPen(gs)
    pen = Cu2QuPen(tpen, max_err=upem / 2000.0)
    draw_arch_A(pen, W, H, S, H * bar_frac, S * bar_weight)
    glyph = tpen.glyph()

    # Sit the new A on the baseline and give it the round letters' sidebearings
    lsb = wb[0]
    glyph.recalcBounds(f['glyf'])
    f['glyf']['A'] = glyph
    adv_o = f['hmtx']['O'][0]
    f['hmtx']['A'] = (adv_o, lsb)

    # rename so nothing collides with a real Poppins install
    for rec in f['name'].names:
        try:
            v = rec.toUnicode()
        except Exception:
            continue
        if 'Poppins' in v:
            rec.string = v.replace('Poppins', 'AlamoLike')
    f.save(dst)
    print('  %s  cap %d  stem %d  width %d  bar at %.0f%% x %.2f stem'
          % (os.path.basename(dst), H, S, W, bar_frac * 100, bar_weight))
    return dst


if __name__ == '__main__':
    build('fonts/Poppins-Black.ttf', 'fonts/AlamoLike-Black.ttf')
