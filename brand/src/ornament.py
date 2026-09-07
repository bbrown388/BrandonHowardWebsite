# -*- coding: utf-8 -*-
"""Arrows and crows, drawn as flat SVG paths.

Everything here is authored in the same y-down space the marks are composed in,
sized off a single dimension, and returns plain path data with no styling, so it
composites into a mark as one more filled shape and stays single colour for
screen print and stitching.
"""
import math


def _pts(points, close=True):
    d = 'M %.2f %.2f ' % points[0]
    d += ' '.join('L %.2f %.2f' % p for p in points[1:])
    return d + (' Z' if close else '')


def arrowhead(cx, tip_y, w, h, notch=0.60):
    """A barbed arrowhead pointing up.

    Tip at the top, two barbs swept down and out, and a notch cut up into the
    base. The notch is what separates an arrowhead from a plain triangle.
    """
    return _pts([(cx, tip_y),
                 (cx + w / 2.0, tip_y + h),
                 (cx, tip_y + h * notch),
                 (cx - w / 2.0, tip_y + h)])


# ── Arrow ───────────────────────────────────────────────────────────────────
# Built to the hand-inked reference. What makes that drawing work:
#
#   * Fletching is many fine barbs, around fifteen a side, thin and leaning
#     back. The white gaps come free because they are separate strokes, and that
#     rhythm is what reads as feather rather than as a paddle.
#   * The shaft runs the whole length, under the fletching, so the two vanes
#     meet on it instead of floating either side of a gap. It carries a hairline
#     split, which is most of the hand-drawn quality; a solid bar looks printed.
#   * The head has concave outer flanks and dead straight inner edges. Curving
#     the inner edges turns the barbs into scythes, and the barb has to end in a
#     short flat, since running both edges to one point leaves a razor sliver.
#
# Slits are cut with reverse-wound subpaths, which a nonzero fill reads as holes.


class _P(object):
    def __init__(self):
        self.d = []

    def M(self, p):
        self.d.append('M %.2f %.2f' % p); return self

    def L(self, p):
        self.d.append('L %.2f %.2f' % p); return self

    def C(self, c1, c2, p):
        self.d.append('C %.2f %.2f, %.2f %.2f, %.2f %.2f' % (c1 + c2 + p)); return self

    def Z(self):
        self.d.append('Z'); return self

    def add(self, s):
        self.d.append(s); return self

    def __str__(self):
        return ' '.join(self.d)


def _quad(a, b, c, d):
    return str(_P().M(a).L(b).L(c).L(d).Z())


def head(x1, y, t, length=4.6, half=1.95, blunt=0.13):
    """Sharp point with barbs swept back.

    Outer flanks gently concave so the point reads as sharpened; inner edges
    dead straight from barb tip down to the shaft. Curving those was what turned
    the barbs into scythes, and slitting them was worse: the barb is thin near
    its tip, so a slit cut it clean off and left a detached bar and a stray
    hairline. The reference has a split in its head, but at the size this mark
    uses there is nothing there to split.

    Each barb ends in a short flat rather than a knife point. Running the
    concave outer curve and the straight inner edge together to a single point
    leaves a razor sliver that vanishes in print and looks like a scratch on
    screen.
    """
    hl, hw = t * length, t * half
    j = x1 - hl * 0.45
    p = _P().M((x1, y))
    p.C((x1 - hl * 0.30, y - hw * 0.18), (x1 - hl * 0.68, y - hw * 0.56), (x1 - hl, y - hw))
    p.L((x1 - hl * (1 - blunt), y - hw * 0.78))   # short flat end on the barb
    p.L((j, y - t * 0.50))
    p.L((j, y + t * 0.50))
    p.L((x1 - hl * (1 - blunt), y + hw * 0.78))
    p.L((x1 - hl, y + hw))
    p.C((x1 - hl * 0.68, y + hw * 0.56), (x1 - hl * 0.30, y + hw * 0.18), (x1, y))
    return str(p.Z())


def shaft(x0, x1, y, t, split=0.22):
    """Shaft with a hairline split down it, cut rather than drawn.

    Runs the whole length, under the fletching as well, so the two vanes meet on
    it instead of floating either side of a gap.
    """
    p = _P().M((x0, y - t * 0.44)).L((x1, y - t * 0.50))            .L((x1, y + t * 0.50)).L((x0, y + t * 0.44)).Z()
    g = t * split / 2.0
    inset = (x1 - x0) * 0.04
    p.add(str(_P().M((x0 + inset, y + g)).L((x1 - inset, y + g * 0.65))
              .L((x1 - inset, y - g * 0.65)).L((x0 + inset, y - g)).Z()))
    return str(p)


def fletching(x0, y, t, length=13.5, height=4.4, n=15, lean=0.60, w=0.40):
    """A feather as a run of fine barbs.

    Inner ends sit on the shaft, outer ends ride a line falling from the nock to
    the shaft, and every barb leans back by a fixed multiple of its own height.
    That lean is what throws the first few barbs out past the tail and cuts the
    swallowtail without it having to be drawn.
    """
    L, hmax, bw = t * length, t * height, t * w
    out = []
    for i in range(n):
        u = i / float(n - 1)
        h = t * 0.5 + (hmax - t * 0.5) * (1.0 - u) ** 0.92
        xo = x0 + L * u * 0.82
        xi = xo + lean * h
        for s in (-1, 1):
            out.append(_quad((xo, y + s * h), (xo + bw, y + s * h),
                             (xi + bw, y + s * t * 0.40), (xi, y + s * t * 0.40)))
    return ' '.join(out)



# The whole arrow needs roughly 30 shaft-thicknesses of length. In the mark it
# has to fit a rule segment, so thickness is derived from the space available
# rather than dictated: pass the nominal weight and it thins down if the segment
# is short, instead of the fletching running into the head.
ARROW_SPAN = 30.0

# 'reference' uses the traced public domain drawing; 'drawn' uses the one built
# from curves in this file. The traced artwork is the default because it is
# genuinely hand-inked and no amount of parameter tuning gets there.
ARROW_STYLE = 'reference'


def arrow(x0, x1, y, thick, head=None, fletch=None, barb=None, style=None):
    """An arrow spanning x0..x1, centred on y. Returns MARKUP, not path data.

    It has to be markup: the traced artwork is placed with a transform rather
    than by rewriting its coordinates, and a transform cannot live inside a d
    attribute.
    """
    if (style or ARROW_STYLE) == 'reference':
        import refarrow
        _, _, vw, vh = refarrow.VIEWBOX
        s = (x1 - x0) / vw
        return ('<g transform="translate(%.3f,%.3f) scale(%.5f)"><path d="%s"/></g>'
                % (x0, y - vh * s / 2.0, s, refarrow.PATH))

    t = min(thick, (x1 - x0) / ARROW_SPAN)
    hl = t * 4.6
    d = ' '.join([shaft(x0 + t * 1.2, x1 - hl * 0.40, y, t),
                  fletching(x0, y, t),
                  globals()['head'](x1, y, t)])
    return '<path d="%s"/>' % d


def crossed_arrows(cx, cy, length, thick, angle=17.0):
    """Two arrows crossing, pointing opposite ways. A plains-country device."""
    out = []
    for sign in (1, -1):
        a = math.radians(angle * sign)
        out.append('<g transform="translate(%.2f,%.2f) rotate(%.2f) scale(%d,1)">%s</g>'
                   % (cx, cy, math.degrees(a), sign,
                      arrow(-length / 2.0, length / 2.0, 0, thick)))
    return ''.join(out)


def crow(x, y, h, facing=1):
    """A crow standing in profile, facing right by default.

    Drawn from reference for pose and proportion only, never traced. What makes
    it read as a crow: an upright standing posture rather than a horizontal
    perch, the head carried high and clear of the shoulders, a long deep bill
    with a slight hook, shaggy throat hackles, a deep barrel of a body, and a
    long wing and tail sweeping back and down to finish near the level of the
    feet.

    The body has to be genuinely deep. At around a third of the height across
    the chest it reads as a bird; much narrower and the whole silhouette
    collapses into a hook, which is the failure mode of every thin bird drawing.

    Straight segments throughout, since this has to hold on a garment where
    feather detail closes up first. The contour is a single simple polygon: a
    nonzero fill would turn any inner contour into more ink rather than less.

    h is crown to feet; overall width lands near 1.09h.
    """
    def P(px, py):
        return (x + px * h * facing, y + py * h)

    outline = [
        (0.430, 0.000), (0.545, 0.012),     # crown
        (0.640, 0.048), (0.705, 0.090),     # forehead running flat into the bill
        (0.845, 0.135), (0.950, 0.178),     # bill: deep at the base, not a needle
        (0.845, 0.203), (0.720, 0.200),     # under the bill
        (0.655, 0.232), (0.608, 0.300),     # chin into throat
        (0.590, 0.390),                     # shaggy hackles
        (0.594, 0.480), (0.570, 0.575),     # deep chest
        (0.528, 0.665), (0.468, 0.726),     # belly
        (0.380, 0.762),                     # vent
        # Wing and tail together: one long low sweep back and down, close to the
        # length of the bird itself. This is the shape that says corvid; a short
        # tail on a big head is a kingfisher every time.
        (0.250, 0.812), (0.040, 0.872),
        (-0.200, 0.920), (-0.420, 0.950),   # tip of the sweep
        (-0.440, 0.876),
        (-0.220, 0.828), (0.010, 0.778),
        (0.200, 0.716), (0.268, 0.664),
        (0.232, 0.575), (0.228, 0.468),     # back
        (0.252, 0.358), (0.290, 0.250),
        (0.336, 0.147), (0.378, 0.062),     # nape into the back of the crown
    ]
    d = _pts([P(px, py) for px, py in outline])

    lw = h * 0.032
    for lx in (0.380, 0.478):
        a_, b_ = P(lx, 0.735), P(lx, 0.982)
        d += ' ' + _pts([(a_[0] - lw, a_[1]), (a_[0] + lw, a_[1]),
                         (b_[0] + lw, b_[1]), (b_[0] - lw, b_[1])])
        # a foot with a forward toe and a short spur back, so it grips the rule
        f = P(lx, 0.982)
        d += ' ' + _pts([(f[0] - lw * 3.2 * facing, f[1]),
                         (f[0] + lw * 6.5 * facing, f[1]),
                         (f[0] + lw * 6.5 * facing, f[1] + lw * 1.4),
                         (f[0] - lw * 3.2 * facing, f[1] + lw * 1.4)])
    return d


def crow_on_rule(cx, rule_y, h, facing=-1):
    """Place a crow so its feet land exactly on a rule."""
    return crow(cx, rule_y - h, h, facing)
