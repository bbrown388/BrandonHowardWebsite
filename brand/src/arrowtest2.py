# -*- coding: utf-8 -*-
"""Fletching studies against the arrows-in-the-back reference.

The reference draws real feather vanes: long, tapered, pointed at the front and
cut square at the nock. That is what the earlier solid-vane attempt was reaching
for and missed by making them short and fat, which fused them into a lump.
"""
import io, sys
sys.path.insert(0, '.')
from logolib import svg


def _p(pts):
    return 'M %.2f %.2f ' % pts[0] + ' '.join('L %.2f %.2f' % q for q in pts[1:]) + ' Z'


def shaft(x0, x1, y, t):
    return _p([(x0, y - t / 2), (x1, y - t / 2), (x1, y + t / 2), (x0, y + t / 2)])


def head(x1, y, t, k=5.4, w=2.5, notch=0.62):
    return _p([(x1, y), (x1 - t * k, y - t * w), (x1 - t * k * notch, y), (x1 - t * k, y + t * w)])


def nock(x0, y, t):
    return _p([(x0, y - t * 1.5), (x0 + t * 0.9, y - t * 1.5),
               (x0 + t * 0.9, y + t * 1.5), (x0, y + t * 1.5)])


def vane(x0, y, t, s, L=8.0, rise=3.2, tip=0.35, back=0.5):
    """One long tapered feather. s is +1 below the shaft, -1 above."""
    return _p([(x0 + t * back, y + s * t * 0.35),
               (x0 + t * back, y + s * t * rise),
               (x0 + t * L * 0.42, y + s * t * rise * 0.92),
               (x0 + t * L * 0.78, y + s * t * rise * 0.55),
               (x0 + t * L, y + s * t * tip)])


def vane_swept(x0, y, t, s, L=8.5, rise=3.4):
    """Same idea with the rear corner raked back, so it reads as swept."""
    return _p([(x0, y + s * t * 0.30),
               (x0 + t * 1.6, y + s * t * rise),
               (x0 + t * L * 0.50, y + s * t * rise * 0.86),
               (x0 + t * L * 0.82, y + s * t * rise * 0.48),
               (x0 + t * L, y + s * t * 0.32)])


def bars(x0, y, t, n=3):
    out = []
    for i in range(n):
        bx = x0 + t * 2.4 * i + t * 1.2
        out.append(_p([(bx - t * 1.1, y - t * 2.6), (bx - t * 1.1 + t * 0.95, y - t * 2.6),
                       (bx + t * 1.1 + t * 0.95, y + t * 2.6), (bx + t * 1.1, y + t * 2.6)]))
    return ' '.join(out)


import math


def barbs(x0, y, t, s, n=9, FL=9.0, maxh=3.3, lean=0.55, w=0.5):
    """A feather drawn as individual barbs radiating off the shaft.

    This is how the reference draws it, and it is the only construction that
    survives: a filled vane, however elegantly shaped, closes into a solid paddle
    because the halves meet across the shaft. Separate strokes keep the shaft
    visible and read as feather all the way down.

    Barb length follows a profile that peaks about a third along, which is what
    gives the silhouette of a real fletching without drawing its outline.
    """
    out = []
    L = t * FL
    for i in range(n):
        u = i / float(n - 1)
        prof = math.sin(math.pi * (0.18 + 0.72 * u)) ** 0.65   # peaks early, tapers forward
        h = t * maxh * prof
        bx = x0 + t * 0.6 + L * u
        out.append(_p([(bx, y + s * t * 0.30),
                       (bx + t * w, y + s * t * 0.30),
                       (bx + t * w - t * lean * (h / t), y + s * h),
                       (bx - t * lean * (h / t), y + s * h)]))
    return ' '.join(out)


def vane_gapped(x0, y, t, s, L=9.0, rise=3.2, gap=1.1):
    """A solid vane held off the shaft, so the shaft still shows through."""
    g = t * gap
    return _p([(x0 + t * 0.5, y + s * g),
               (x0 + t * 0.9, y + s * t * rise),
               (x0 + t * L * 0.46, y + s * t * rise * 0.90),
               (x0 + t * L * 0.80, y + s * t * rise * 0.52),
               (x0 + t * L, y + s * g)])


V = {
 'E  feather barbs, nine strokes':
   lambda x0, x1, y, t: ' '.join([shaft(x0 + t, x1 - t * 4.8, y, t), head(x1, y, t), nock(x0, y, t),
                                  barbs(x0, y, t, -1), barbs(x0, y, t, 1)]),
 'F  feather barbs, six heavier strokes':
   lambda x0, x1, y, t: ' '.join([shaft(x0 + t, x1 - t * 4.8, y, t), head(x1, y, t), nock(x0, y, t),
                                  barbs(x0, y, t, -1, n=6, w=0.72),
                                  barbs(x0, y, t, 1, n=6, w=0.72)]),
 'G  solid vanes held off the shaft':
   lambda x0, x1, y, t: ' '.join([shaft(x0 + t, x1 - t * 4.8, y, t), head(x1, y, t), nock(x0, y, t),
                                  vane_gapped(x0, y, t, -1), vane_gapped(x0, y, t, 1)]),
 'D  three bars (shipping now)':
   lambda x0, x1, y, t: ' '.join([shaft(x0 + t, x1 - t * 4.8, y, t), head(x1, y, t), bars(x0, y, t)]),
}

if __name__ == '__main__':
    cells = []
    for name, fn in V.items():
        for t, tag in ((16, 'large'), (7, 'small')):
            cells.append(('%s  %s' % (name, tag),
                          svg('<path d="%s"/>' % fn(20, 470, 55, t), (0, 0, 490, 110), fg='#141210')))
    rows = ['<div class="c"><div class="lab">%s</div>%s</div>' % (n, b) for n, b in cells]
    io.open('arrowtest3.html', 'w', encoding='utf-8', newline='\n').write(
        '<meta charset="utf-8"><style>body{background:#F5F0E6;margin:0;padding:14px;'
        'font:12px system-ui;display:flex;flex-wrap:wrap;gap:10px}'
        '.c{background:#fff;border:1px solid #ddd;padding:8px}'
        '.lab{font-size:10px;letter-spacing:.11em;text-transform:uppercase;color:#999;'
        'margin-bottom:4px}svg{width:340px;height:auto;display:block}</style>' + ''.join(rows))
    print('  arrowtest3.html: %d studies' % len(cells))
