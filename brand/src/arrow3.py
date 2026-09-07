# -*- coding: utf-8 -*-
"""Arrow, restarted with the scale problem taken seriously.

Every version so far was designed while zoomed in, where a feather can carry
detail. In the mark the arrow is a rule: long, thin, flanking small caps. At that
size, barbs and slits and serrations cannot resolve, so they turn into fuzz, and
fuzz is what reads as clip art. The fix is not better detail, it is less of it.

So these are built for the size they are actually used at. Curves throughout,
because straight segments were the other half of the problem, but the vocabulary
is deliberately small: a shaft that tapers, a head with slightly concave flanks,
and at most one restrained tail mark.
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
    p = P().M((x1, y))
    p.C((x1 - hl * 0.38, y - hw * (0.30 - waist)), (x1 - hl * 0.72, y - hw * (0.68 - waist)),
        (x1 - hl, y - hw))
    p.L((x1 - hl, y + hw))
    p.C((x1 - hl * 0.72, y + hw * (0.68 - waist)), (x1 - hl * 0.38, y + hw * (0.30 - waist)),
        (x1, y))
    return str(p.Z())


def shaft(x0, x1, y, t, taper=0.66):
    """Tapered: thin at the nock, full under the head. Gives the line life."""
    a, b = t * taper / 2.0, t / 2.0
    return str(P().M((x0, y - a)).L((x1, y - b)).L((x1, y + b)).L((x0, y + a)).Z())


def chevron(x, y, t, s=1.0, w=1.9, h=1.6, thick=0.42):
    """One swept tick off the shaft, tapering to a point."""
    W, H, k = t * w, t * h * s, t * thick
    p = P().M((x + W, y + H))
    p.C((x + W * 0.45, y + H * 0.55), (x + W * 0.20, y + H * 0.20), (x, y))
    p.L((x + k * 0.9, y))
    p.C((x + W * 0.30, y + H * 0.22), (x + W * 0.55, y + H * 0.58), (x + W + k * 0.5, y + H))
    return str(p.Z())


def nock_bar(x, y, t, h=1.35, w=0.5):
    return str(P().M((x, y - t * h)).L((x + t * w, y - t * h))
               .L((x + t * w, y + t * h)).L((x, y + t * h)).Z())


def vane(x0, y, t, s, length=8.0, height=1.15):
    """A single shallow feather on one side only.

    One vane rather than two. A pair always closes across the shaft into a
    paddle; one reads as a feather seen side on, which is what an arrow actually
    looks like from this angle anyway.
    """
    fl, fh = t * length, t * height * s
    p = P().M((x0 + fl, y + s * t * 0.22))
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


VARIANTS = [('A  point and taper, nothing else', plain),
            ('B  point, taper, nock bar', barred),
            ('C  point, taper, two swept ticks', chevrons),
            ('D  point, taper, one shallow vane', single_vane)]
