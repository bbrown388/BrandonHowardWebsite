# -*- coding: utf-8 -*-
"""Trace a black-on-white raster into SVG path data.

Lets supplied artwork be used as it is rather than redrawn. The mark is a single
flat fill, so anything dropped into it has to end up as paths: a raster cannot
scale for print, cannot be recoloured for a dark garment, and cannot be handed to
an embroidery digitiser in a useful form.

potracer is the pure-python port of potrace, the same algorithm Inkscape and
Illustrator use behind their autotrace commands.
"""
import sys
import numpy as np
from PIL import Image
import potrace


def _pt(p):
    """potracer returns _Point objects, which are not iterable."""
    return (p.x, p.y)


def trace(path, threshold=128, turdsize=12, alphamax=1.0, light_ink=False):
    im = Image.open(path)
    if im.mode in ('RGBA', 'LA', 'P'):
        im = im.convert('RGBA')
        bg = Image.new('RGB', im.size, 'white')
        bg.paste(im, mask=im.split()[-1])
        im = bg
    g = np.array(im.convert('L'))
    # potracer treats a True cell as BACKGROUND, not foreground, which is the
    # opposite of what the name Bitmap suggests. Getting this backwards traces
    # the page instead of the artwork and yields a solid block with the drawing
    # knocked out of it. Default here is dark ink on a light ground.
    mask = (g < threshold) if light_ink else (g > threshold)
    plist = potrace.Bitmap(mask).trace(turdsize=turdsize, alphamax=alphamax)

    out = []
    for curve in plist:
        sx, sy = _pt(curve.start_point)
        d = ['M %.2f %.2f' % (sx, sy)]
        for seg in curve:
            ex, ey = _pt(seg.end_point)
            if seg.is_corner:
                cx, cy = _pt(seg.c)
                d.append('L %.2f %.2f L %.2f %.2f' % (cx, cy, ex, ey))
            else:
                ax, ay = _pt(seg.c1)
                bx, by = _pt(seg.c2)
                d.append('C %.2f %.2f, %.2f %.2f, %.2f %.2f' % (ax, ay, bx, by, ex, ey))
        d.append('Z')
        out.append(' '.join(d))
    return ' '.join(out), im.size


def to_svg(src, dst=None, **kw):
    d, (w, h) = trace(src, **kw)
    dst = dst or src.rsplit('.', 1)[0] + '-traced.svg'
    open(dst, 'w').write(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d">'
        '<path fill="#141210" d="%s"/></svg>' % (w, h, w, h, d))
    return dst, d


if __name__ == '__main__':
    dst, d = to_svg(sys.argv[1])
    print('  %s -> %s' % (sys.argv[1], dst))
    print('  %d subpaths, %d chars of path data' % (d.count('M '), len(d)))
