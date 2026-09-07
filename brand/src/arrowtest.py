# -*- coding: utf-8 -*-
"""Arrow studies. Pointing right, x0..x1, centred on y, shaft thickness t."""
import io, sys
sys.path.insert(0, '.')
from logolib import svg


def _p(pts):
    return 'M %.2f %.2f ' % pts[0] + ' '.join('L %.2f %.2f' % q for q in pts[1:]) + ' Z'


def shaft(x0, x1, y, t):
    return _p([(x0, y - t / 2), (x1, y - t / 2), (x1, y + t / 2), (x0, y + t / 2)])


def head_tri(x1, y, t, k=5.0, w=2.3):
    """Clean isoceles point."""
    return _p([(x1, y), (x1 - t * k, y - t * w), (x1 - t * k, y + t * w)])


def head_barb(x1, y, t, k=5.4, w=2.5, notch=0.62):
    """Point with the base cut back between the barbs."""
    return _p([(x1, y), (x1 - t * k, y - t * w),
               (x1 - t * k * notch, y), (x1 - t * k, y + t * w)])


def nock(x0, y, t, w=2.0):
    return _p([(x0, y - t * w), (x0 + t, y - t * w), (x0 + t, y + t * w), (x0, y + t * w)])


def feathers(x0, y, t, n=3, lean=1.1, reach=2.6, gap=2.4, back=True):
    """n parallel bars crossing the shaft, leaning back toward the nock."""
    out = []
    s = -1 if back else 1
    for i in range(n):
        bx = x0 + t * gap * i + t * 1.2
        out.append(_p([(bx + s * t * lean, y - t * reach),
                       (bx + s * t * lean + t * 0.95, y - t * reach),
                       (bx - s * t * lean + t * 0.95, y + t * reach),
                       (bx - s * t * lean, y + t * reach)]))
    return ' '.join(out)


def vanes(x0, y, t, L=5.0):
    """Two swept solid vanes, kept slim so they do not fuse into a lump."""
    out = []
    for s in (-1, 1):
        out.append(_p([(x0, y + s * t * 0.5),
                       (x0 + t * L * 0.30, y + s * t * 2.5),
                       (x0 + t * L, y + s * t * 1.15),
                       (x0 + t * L * 0.70, y + s * t * 0.45)]))
    return ' '.join(out)


VARIANTS = {
 'A  triangle head, nock only':
    lambda x0, x1, y, t: ' '.join([shaft(x0 + t, x1 - t * 4.4, y, t),
                                   head_tri(x1, y, t), nock(x0, y, t)]),
 'B  triangle head, three feathers':
    lambda x0, x1, y, t: ' '.join([shaft(x0 + t, x1 - t * 4.4, y, t),
                                   head_tri(x1, y, t), feathers(x0, y, t)]),
 'C  barbed head, three feathers':
    lambda x0, x1, y, t: ' '.join([shaft(x0 + t, x1 - t * 4.2, y, t),
                                   head_barb(x1, y, t), feathers(x0, y, t)]),
 'D  triangle head, slim vanes':
    lambda x0, x1, y, t: ' '.join([shaft(x0 + t, x1 - t * 4.4, y, t),
                                   head_tri(x1, y, t), vanes(x0, y, t)]),
 'E  fine: long shaft, small sharp head, two feathers':
    lambda x0, x1, y, t: ' '.join([shaft(x0, x1 - t * 3.4, y, t * 0.72),
                                   head_tri(x1, y, t, k=3.6, w=1.7),
                                   feathers(x0, y, t, n=2, reach=2.2, gap=2.2)]),
 'F  current (for comparison)': None,
}

if __name__ == '__main__':
    import ornament as orn
    cells = []
    for name, fn in VARIANTS.items():
        for t, tag in ((16, 'large'), (7, 'small')):
            d = orn.arrow(20, 470, 55, t) if fn is None else fn(20, 470, 55, t)
            cells.append(('%s  %s' % (name, tag),
                          svg('<path d="%s"/>' % d, (0, 0, 490, 110), fg='#141210')))
    rows = ['<div class="c"><div class="lab">%s</div>%s</div>' % (n, b) for n, b in cells]
    io.open('arrowtest.html', 'w', encoding='utf-8', newline='\n').write(
        '<meta charset="utf-8"><style>body{background:#F5F0E6;margin:0;padding:14px;'
        'font:12px system-ui;display:flex;flex-wrap:wrap;gap:10px}'
        '.c{background:#fff;border:1px solid #ddd;padding:8px}'
        '.lab{font-size:10px;letter-spacing:.11em;text-transform:uppercase;color:#999;'
        'margin-bottom:4px}svg{width:340px;height:auto;display:block}</style>' + ''.join(rows))
    print('  arrowtest.html: %d studies' % len(cells))
