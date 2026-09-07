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
# Rebuilt from scratch. Two things had been wrong with every earlier version.
# Everything was made of straight segments, because the path helper only emitted
# L commands, so a polygon head and a rectangular shaft read as clip art however
# the proportions were tuned. And it was designed while zoomed in, where a
# feather can carry detail; in the mark the arrow is a rule, long and thin beside
# small caps, and at that size barbs and serrations cannot resolve, so they print
# as fuzz. The fix was fewer parts, drawn with curves.
#
# ARROW_STYLE picks the tail: 'plain', 'bar', 'ticks' or 'vane'.
ARROW_STYLE = 'ticks'


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

    def __str__(self):
        return ' '.join(self.d)


def head(x1, y, t, length=4.0, half=1.55, waist=0.10):
    """A solid point with slightly concave flanks and a flat back.

    No notch. A notch cut into the base is the single thing that pushed earlier
    versions toward looking like a harpoon, and at rule size it just prints as a
    white nick. The flanks bow inward by a tenth of the half width, which is
    enough to read as sharpened and little enough to survive small.
    """
    hl, hw = t * length, t * half
    p = _P().M((x1, y))
    p.C((x1 - hl * 0.38, y - hw * (0.30 - waist)), (x1 - hl * 0.72, y - hw * (0.68 - waist)),
        (x1 - hl, y - hw))
    p.L((x1 - hl, y + hw))
    p.C((x1 - hl * 0.72, y + hw * (0.68 - waist)), (x1 - hl * 0.38, y + hw * (0.30 - waist)),
        (x1, y))
    return str(p.Z())


def shaft(x0, x1, y, t, taper=0.66):
    """Tapered: thin at the nock, full under the head. Gives the line life."""
    a, b = t * taper / 2.0, t / 2.0
    return str(_P().M((x0, y - a)).L((x1, y - b)).L((x1, y + b)).L((x0, y + a)).Z())


def chevron(x, y, t, s=1.0, w=1.9, h=1.6, thick=0.42):
    """One swept tick off the shaft, tapering to a point."""
    W, H, k = t * w, t * h * s, t * thick
    p = _P().M((x + W, y + H))
    p.C((x + W * 0.45, y + H * 0.55), (x + W * 0.20, y + H * 0.20), (x, y))
    p.L((x + k * 0.9, y))
    p.C((x + W * 0.30, y + H * 0.22), (x + W * 0.55, y + H * 0.58), (x + W + k * 0.5, y + H))
    return str(p.Z())


def nock_bar(x, y, t, h=1.35, w=0.5):
    return str(_P().M((x, y - t * h)).L((x + t * w, y - t * h))
               .L((x + t * w, y + t * h)).L((x, y + t * h)).Z())


def vane(x0, y, t, s, length=8.0, height=1.15):
    """A single shallow feather on one side only.

    One vane rather than two. A pair always closes across the shaft into a
    paddle; one reads as a feather seen side on, which is what an arrow actually
    looks like from this angle anyway.
    """
    fl, fh = t * length, t * height * s
    p = _P().M((x0 + fl, y + s * t * 0.22))
    p.C((x0 + fl * 0.74, y + fh * 0.60), (x0 + fl * 0.52, y + fh * 0.96), (x0 + fl * 0.34, y + fh))
    p.C((x0 + fl * 0.22, y + fh * 1.02), (x0 + fl * 0.10, y + fh * 0.80), (x0 + fl * 0.02, y + fh * 0.40))
    p.C((x0 + fl * 0.02, y + fh * 0.20), (x0 + fl * 0.06, y + s * t * 0.26), (x0 + fl * 0.12, y + s * t * 0.22))
    return str(p.L((x0 + fl, y + s * t * 0.22)).Z())


# ── the four candidates ──────────────────────────────────────────────────────
def plain(x0, x1, y, t):
    return ' '.join([shaft(x0, x1 - t * 4.0 * 0.98, y, t), head(x1, y, t)])


def barred(x0, x1, y, t):
    return ' '.join([shaft(x0 + t * 0.5, x1 - t * 3.92, y, t), head(x1, y, t),
                     nock_bar(x0, y, t)])


def chevrons(x0, x1, y, t, n=2):
    parts = [shaft(x0 + t * 0.4, x1 - t * 3.92, y, t), head(x1, y, t)]
    for i in range(n):
        cx = x0 + t * (0.6 + 1.5 * i)
        parts.append(chevron(cx, y, t, -1))
        parts.append(chevron(cx, y, t, 1))
    return ' '.join(parts)


def single_vane(x0, x1, y, t):
    return ' '.join([shaft(x0 + t * 0.4, x1 - t * 3.92, y, t), head(x1, y, t),
                     nock_bar(x0, y, t), vane(x0 + t * 0.6, y, t, -1)])



def arrow(x0, x1, y, thick, head=None, fletch=None, barb=None, style=None):
    """A drawn arrow pointing right: tapered shaft, sharpened point, quiet tail."""
    t = thick
    s = style or ARROW_STYLE
    parts = [shaft(x0 + t * 0.4, x1 - t * 3.92, y, t), globals()['head'](x1, y, t)]
    if s == 'bar':
        parts.append(nock_bar(x0, y, t))
    elif s == 'ticks':
        parts.append(nock_bar(x0, y, t))
        for i in range(2):
            cx = x0 + t * (0.9 + 1.5 * i)
            parts.append(chevron(cx, y, t, -1))
            parts.append(chevron(cx, y, t, 1))
    elif s == 'vane':
        parts.append(nock_bar(x0, y, t))
        parts.append(vane(x0 + t * 0.6, y, t, -1))
    return ' '.join(parts)


def crossed_arrows(cx, cy, length, thick, angle=17.0):
    """Two arrows crossing, pointing opposite ways. A plains-country device."""
    out = []
    for sign in (1, -1):
        a = math.radians(angle * sign)
        co, si = math.cos(a), math.sin(a)
        d = arrow(-length / 2.0, length / 2.0, 0, thick)
        out.append('<g transform="translate(%.2f,%.2f) rotate(%.2f) scale(%d,1)">'
                   '<path d="%s"/></g>' % (cx, cy, math.degrees(a), sign, d))
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
