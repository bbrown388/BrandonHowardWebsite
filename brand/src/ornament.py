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
    """A horizontal arrow pointing right: fletching, shaft, barbed head.

    The head is properly barbed, with a notch cut back into its base, and the
    fletching is two swept vanes off a nock rather than a pair of ticks. Both
    matter at sign size: a plain triangle on a stick reads as a UI glyph, and
    this has to read as a drawn arrow.

    Emitted as several subpaths in one string. They overlap only on the shaft,
    and a nonzero fill unions them, so it behaves as one object.
    """
    hl = head if head is not None else thick * 4.2      # head length
    hw = barb if barb is not None else thick * 2.0      # head half width
    fl = fletch if fletch is not None else thick * 4.6  # fletching length
    t2 = thick / 2.0

    shaft = _pts([(x0 + fl * 0.20, y - t2), (x1 - hl * 0.55, y - t2),
                  (x1 - hl * 0.55, y + t2), (x0 + fl * 0.20, y + t2)])

    # barbed head: tip, back to the barb, in to the notch, out to the far barb
    point = _pts([(x1, y),
                  (x1 - hl, y - hw),
                  (x1 - hl * 0.62, y),
                  (x1 - hl, y + hw)])

    # nock at the very end, so the tail reads as the back of an arrow
    nock = _pts([(x0, y - t2 * 1.5), (x0 + fl * 0.22, y - t2),
                 (x0 + fl * 0.22, y + t2), (x0, y + t2 * 1.5)])

    vanes = []
    for s in (-1, 1):
        vanes.append(_pts([(x0 + fl * 0.06, y + s * t2),
                           (x0 + fl * 0.30, y + s * thick * 2.3),
                           (x0 + fl * 1.00, y + s * thick * 1.05),
                           (x0 + fl * 0.86, y + s * t2 * 0.6)]))
    return ' '.join([shaft, point, nock] + vanes)


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
