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


def arrow(x0, x1, y, thick, head=None, fletch=None, barb=None):
    """A horizontal arrow pointing right, fletched the way a real one is drawn.

    Three parts unioned by a nonzero fill: shaft, barbed head with its base cut
    back between the barbs, and a feather at the tail drawn as individual barbs
    radiating off the shaft.

    The barbs are the whole point. A filled vane closes into a solid paddle no
    matter how elegantly it is shaped, because the halves meet across the shaft,
    and that paddle is what made two earlier attempts look cheap. Separate
    strokes keep the shaft visible through the feather and stay legible small,
    because the eye reads the rhythm rather than the mass. Barb length follows a
    profile peaking about a third along, which gives the silhouette of a real
    fletching without drawing its outline.
    """
    hl = head if head is not None else thick * 5.4
    hw = barb if barb is not None else thick * 2.5
    n = int(fletch) if fletch is not None else 7
    t2 = thick / 2.0

    parts = [_pts([(x0 + thick * 0.8, y - t2), (x1 - hl * 0.9, y - t2),
                   (x1 - hl * 0.9, y + t2), (x0 + thick * 0.8, y + t2)]),
             _pts([(x1, y), (x1 - hl, y - hw),
                   (x1 - hl * 0.62, y), (x1 - hl, y + hw)]),
             _pts([(x0, y - thick * 1.45), (x0 + thick * 0.85, y - thick * 1.45),
                   (x0 + thick * 0.85, y + thick * 1.45), (x0, y + thick * 1.45)])]

    L, maxh, lean, w = thick * 9.0, thick * 3.3, 0.55, thick * 0.68
    for s in (-1, 1):
        for i in range(n):
            u = i / float(n - 1)
            prof = math.sin(math.pi * (0.18 + 0.72 * u)) ** 0.65
            h = maxh * prof
            bx = x0 + thick * 0.7 + L * u
            parts.append(_pts([(bx, y + s * t2 * 0.6),
                               (bx + w, y + s * t2 * 0.6),
                               (bx + w - lean * h, y + s * h),
                               (bx - lean * h, y + s * h)]))
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
