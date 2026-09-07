# -*- coding: utf-8 -*-
"""Measure minimum stroke width per mark, verifying alignment before trusting it.

Two things this guards against, both of which silently produced wrong numbers
before: a screenshot taller than Chrome's ~16384 px capture cap, where the stitch
below the seam is garbage, and the red key stamp being counted as ink. The stamp
is now the alignment check, and the ink mask is colour-aware so the stamp itself
never contributes.
"""
import json, sys
from PIL import Image, ImageChops, ImageFilter

W = 1200
SHOTS = {0: r'C:\Users\bobbr\Claude\c0.png',
         1: r'C:\Users\bobbr\Claude\c1.png',
         2: r'C:\Users\bobbr\Claude\c2.png'}


def black_mask(rgb):
    """Ink = dark in all three channels, so the red key stamp is excluded."""
    r, g, b = rgb.split()
    f = lambda v: 255 if v < 100 else 0
    m = ImageChops.darker(ImageChops.darker(r.point(f), g.point(f)), b.point(f))
    return m


def has_stamp(rgb):
    r, g, b = rgb.split()
    red = ImageChops.darker(r.point(lambda v: 255 if v > 150 else 0),
                            ImageChops.darker(g.point(lambda v: 255 if v < 90 else 0),
                                              b.point(lambda v: 255 if v < 90 else 0)))
    return sum(red.histogram()[128:]) > 40


def opening_loss(mask, k):
    o = mask
    for _ in range(k): o = o.filter(ImageFilter.MinFilter(3))
    for _ in range(k): o = o.filter(ImageFilter.MaxFilter(3))
    a0 = sum(mask.histogram()[128:]); a1 = sum(o.histogram()[128:])
    return (a0 - a1) / a0 * 100.0 if a0 else 0.0


index = json.load(open('measure_index.json'))
res, bad = {}, []
for ci, page in enumerate(index):
    im = Image.open(SHOTS[ci]).convert('RGB')
    if im.height != page['height']:
        sys.exit('  chunk %d height %d != expected %d' % (ci, im.height, page['height']))
    for t in page['tiles']:
        tile = im.crop((0, t['y'], W, t['y'] + t['h']))
        if not has_stamp(tile.crop((0, 0, 400, 26))):
            bad.append(t['key']); continue
        m = black_mask(tile)
        res[t['key']] = dict(dtg=round(opening_loss(m, 2), 1),
                             emb=round(opening_loss(m, 6), 1))

for k, v in res.items():
    e = v['emb']
    v['verdict'] = ('safe for embroidery and print' if e < 12 else
                    'print fine, embroidery needs it larger' if e < 30 else
                    'print only at this size')

print('  measured %d marks, %d failed the alignment check' % (len(res), len(bad)))
if bad:
    print('  FAILED:', ', '.join(bad))
old = json.load(open('strokes.json'))
json.dump(res, open('strokes.json', 'w'), indent=1)

print()
print('  %-26s %14s %14s' % ('mark', 'old (suspect)', 'verified'))
moved = 0
for k in sorted(res):
    o, n = old.get(k), res[k]
    if not o: continue
    d = abs(o['emb'] - n['emb'])
    if d >= 0.5:
        moved += 1
        print('  %-26s %6.1f/%5.1f%%  %6.1f/%5.1f%%   %+.1f' %
              (k, o['dtg'], o['emb'], n['dtg'], n['emb'], n['emb'] - o['emb']))
print()
print('  %d of %d marks changed by 0.5 points or more' % (moved, len(res)))
