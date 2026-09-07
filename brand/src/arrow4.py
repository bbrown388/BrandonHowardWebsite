# -*- coding: utf-8 -*-
"""Hand-inked arrow, built to the supplied reference.

What makes that reference work, and what every earlier attempt of mine missed:

  * The fletching is many fine barbs, not a few. Around fifteen a side, thin and
    closely spaced, leaning back. The white gaps between them come free because
    they are separate strokes, and that rhythm is what reads as feather.
  * The vane is a long wedge, tallest at the nock and running down to nothing
    where it meets the shaft. The barbs lean back far enough that the leftmost
    ones overhang the tail, which is what makes the swallowtail notch.
  * The shaft carries a hairline split down its length. That single detail is
    most of the hand-drawn quality; a solid bar always looks printed.
  * The head has concave swept barbs with a slit inside each, not a filled
    triangle.

Slits are cut with reverse-wound subpaths so a nonzero fill reads them as holes,
the same way a font builds the counter of an O.
"""


class P(object):
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
    return str(P().M(a).L(b).L(c).L(d).Z())


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
    p = P().M((x1, y))
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
    p = P().M((x0, y - t * 0.44)).L((x1, y - t * 0.50))            .L((x1, y + t * 0.50)).L((x0, y + t * 0.44)).Z()
    g = t * split / 2.0
    inset = (x1 - x0) * 0.04
    p.add(str(P().M((x0 + inset, y + g)).L((x1 - inset, y + g * 0.65))
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


def arrow(x0, x1, y, t):
    hl = t * 4.6
    return ' '.join([shaft(x0 + t * 1.2, x1 - hl * 0.40, y, t),
                     fletching(x0, y, t),
                     head(x1, y, t)])
