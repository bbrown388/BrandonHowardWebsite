# -*- coding: utf-8 -*-
"""Build the stroke-measurement pages in chunks.

Chrome caps a full-page screenshot at roughly 16384 px tall. Past that the
capture is stitched wrong, so tiles below the seam get measured against whatever
artwork happens to land there. A single tall page silently produced bogus numbers
for every mark past the seam, and the numbers looked plausible, which is worse.

Chunking keeps every page comfortably under the cap. Each chunk also stamps its
key into the tile so alignment can be verified from the image itself rather than
trusted.
"""
import json, io, os

W = 1200
MAX_H = 12000          # well under the 16384 cap, with room for any single tile

marks = json.load(open('out/marks.json', encoding='utf-8'))
chunks, cur, cur_h = [], [], 0
for m in marks:
    x0, y0, w, h = m['box']
    H = int(round(W * h / w))
    if cur and cur_h + H > MAX_H:
        chunks.append(cur); cur, cur_h = [], 0
    cur.append((m, H)); cur_h += H
if cur:
    chunks.append(cur)

index = []
for ci, ch in enumerate(chunks):
    figs, offs, y = [], [], 0
    for m, H in ch:
        x0, y0, w, h = m['box']
        figs.append('<div style="width:%dpx;height:%dpx;position:relative">'
                    '<div style="position:absolute;left:4px;top:2px;font:13px monospace;'
                    'color:#f00;z-index:2">%s</div>'
                    '<svg viewBox="%.2f %.2f %.2f %.2f" width="%d" height="%d">'
                    '<g fill="#000">%s</g></svg></div>'
                    % (W, H, m['key'], x0, y0, w, h, W, H, m['body']))
        offs.append(dict(key=m['key'], y=y, h=H)); y += H
    io.open('measure_%d.html' % ci, 'w', encoding='utf-8', newline='\n').write(
        '<meta charset="utf-8"><style>*{margin:0;padding:0}body{background:#fff;'
        'width:%dpx}svg{display:block}</style>%s' % (W, ''.join(figs)))
    index.append(dict(page='measure_%d.html' % ci, height=y, tiles=offs))
    print('  measure_%d.html  %2d tiles  %5d px' % (ci, len(offs), y))

json.dump(index, open('measure_index.json', 'w'), indent=1)
print('  %d chunks, tallest %d px (cap is 16384)' % (len(index), max(i['height'] for i in index)))
