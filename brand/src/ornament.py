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
    """A horizontal arrow: fletching, shaft, head. Points right.

    Returned as several subpaths in one string. They only ever overlap on the
    shaft, and a nonzero fill unions them, so the result reads as one object.
    """
    head = head if head is not None else thick * 3.4
    barb = barb if barb is not None else thick * 2.6
    fletch = fletch if fletch is not None else thick * 3.0
    half = thick / 2.0

    shaft = _pts([(x0 + fletch * 0.35, y - half), (x1 - head, y - half),
                  (x1 - head, y + half), (x0 + fletch * 0.35, y + half)])
    point = _pts([(x1, y), (x1 - head, y - barb / 2.0),
                  (x1 - head, y + barb / 2.0)])
    # two swept feathers, angled back off the shaft
    f1 = _pts([(x0, y - barb * 0.62), (x0 + fletch, y - half),
               (x0 + fletch, y + half * 0.4), (x0 + fletch * 0.30, y - half * 0.2)])
    f2 = _pts([(x0, y + barb * 0.62), (x0 + fletch, y + half),
               (x0 + fletch, y - half * 0.4), (x0 + fletch * 0.30, y + half * 0.2)])
    return ' '.join([shaft, point, f1, f2])


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


def crow(x, y, h, facing=-1):
    """A perched crow in silhouette, facing left by default.

    The bill is the whole tell. A crow carries a long, deep, dagger of a bill
    roughly two thirds the length of its head and about as deep at the base as a
    songbird bill is long; draw it small and pointed and you get a finch no
    matter what the rest of the body does. The other corvid markers are a flat
    crown running straight into that bill with no rounded forehead step, shaggy
    throat hackles, a deep chest, heavy legs, and a squared-off tail rather than
    a fine taper.

    Straight segments throughout, so the silhouette stays faceted and blunt.
    Feather detail is the first thing to close up on a garment, and a cut notch
    would not work anyway: these fill with a nonzero rule, so an inner contour
    adds ink instead of removing it.

    h is crown to feet. Overall length lands near 1.6h.
    """
    def P(px, py):
        return (x + px * h * facing, y + py * h)

    outline = [
        (0.000, 0.250),                     # bill tip
        (0.090, 0.200), (0.220, 0.162),     # heavy upper mandible
        (0.310, 0.120), (0.410, 0.098),     # forehead runs flat off the bill
        (0.510, 0.100), (0.580, 0.135),     # flat crown, nape
        (0.625, 0.210), (0.670, 0.285),     # neck into shoulder
        (0.810, 0.340), (0.980, 0.400),     # back
        (1.170, 0.450),
        (1.430, 0.512), (1.512, 0.548),     # tail, genuinely squared at the tip
        (1.498, 0.652), (1.170, 0.602),
        (1.010, 0.610), (0.860, 0.648),     # deep belly
        (0.710, 0.678), (0.570, 0.686),
        (0.440, 0.656), (0.340, 0.586),     # chest
        (0.278, 0.498), (0.242, 0.424),
        (0.205, 0.372), (0.232, 0.338),     # shaggy throat hackle
        (0.200, 0.310), (0.100, 0.288),     # lower mandible
    ]
    d = _pts([P(px, py) for px, py in outline])

    # Set wide enough apart to stay two legs. At 0.48 and 0.60 the shafts very
    # nearly touch and the bird reads as though it is standing on a post.
    lw = h * 0.042
    for lx in (0.445, 0.635):
        a_, b_ = P(lx, 0.660), P(lx, 1.000)
        d += ' ' + _pts([(a_[0] - lw, a_[1]), (a_[0] + lw, a_[1]),
                         (b_[0] + lw, b_[1]), (b_[0] - lw, b_[1])])
    return d


def crow_on_rule(cx, rule_y, h, facing=-1):
    """Place a crow so its feet land exactly on a rule."""
    return crow(cx, rule_y - h, h, facing)
