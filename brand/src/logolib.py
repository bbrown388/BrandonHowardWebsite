"""Type-on-a-path logo builder.

Emits real glyph outlines as SVG <path> data rather than <text>, so the result
is a self-contained vector any printer or embroidery digitiser can open without
needing the font installed. Shaping goes through HarfBuzz so script faces get
their proper kerning and contextual alternates.

Every run also returns its transformed ink corners, which is what lets the
caller crop a composition tightly without needing a rasteriser on the box.
"""
import math
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen


class Face:
    def __init__(self, path):
        self.data = open(path, 'rb').read()
        self.hbfont = hb.Font(hb.Face(hb.Blob(self.data)))
        self.tt = TTFont(path)
        self.upem = self.tt['head'].unitsPerEm
        self.gs = self.tt.getGlyphSet()
        self.order = self.tt.getGlyphOrder()
        self._p = {}
        self._b = {}

    def shape(self, text):
        buf = hb.Buffer()
        buf.add_str(text)
        buf.guess_segment_properties()
        hb.shape(self.hbfont, buf, {"kern": True, "liga": True, "calt": True})
        return [(self.order[i.codepoint], p.x_advance, p.x_offset, p.y_offset)
                for i, p in zip(buf.glyph_infos, buf.glyph_positions)]

    def path(self, gname):
        if gname not in self._p:
            pen = SVGPathPen(self.gs)
            self.gs[gname].draw(pen)
            self._p[gname] = pen.getCommands()
        return self._p[gname]

    def bounds(self, gname):
        if gname not in self._b:
            bp = BoundsPen(self.gs)
            self.gs[gname].draw(bp)
            self._b[gname] = bp.bounds
        return self._b[gname]


def _widths(face, text, size, tracking):
    s = size / face.upem
    glyphs = face.shape(text)
    ws = [g[1] * s + tracking for g in glyphs]
    total = sum(ws) - (tracking if glyphs else 0.0)
    return s, glyphs, ws, total


def run_straight(face, text, size, tracking=0.0, cx=0.0, baseline=0.0):
    """A flat line of type, centred on cx. tracking is in output units."""
    s, glyphs, ws, total = _widths(face, text, size, tracking)
    x = cx - total / 2.0
    out, pts = [], []
    for (gn, adv, dx, dy), w in zip(glyphs, ws):
        d = face.path(gn)
        if d:
            tx, ty = x + dx * s, baseline - dy * s
            out.append('<path transform="translate(%.4f,%.4f) scale(%.6f,%.6f)" d="%s"/>'
                       % (tx, ty, s, -s, d))
            b = face.bounds(gn)
            if b:
                pts += [(tx + b[0] * s, ty - b[1] * s), (tx + b[2] * s, ty - b[3] * s)]
        x += w
    return '\n'.join(out), total, pts


def run_arc(face, text, size, radius, tracking=0.0, cx=0.0, cy=0.0):
    """Type set on a circular arc.

    The arc centre is (cx, cy) and the baseline rides a circle of `radius` above
    it, so the word bows upward the way a dance-hall sign does. Each glyph is
    rotated tangent to the curve and centred on its own slice of the arc.
    """
    s, glyphs, ws, total = _widths(face, text, size, tracking)
    theta = -total / (2.0 * radius)          # start angle, so the run centres on top
    out, pts = [], []
    for (gn, adv, dx, dy), w in zip(glyphs, ws):
        d = face.path(gn)
        mid = theta + (w / 2.0) / radius
        if d:
            X = cx + radius * math.sin(mid)
            Y = cy - radius * math.cos(mid)
            deg = math.degrees(mid)
            ox = -(adv * s) / 2.0
            out.append('<path transform="translate(%.4f,%.4f) rotate(%.4f) '
                       'translate(%.4f,0) scale(%.6f,%.6f)" d="%s"/>'
                       % (X, Y, deg, ox, s, -s, d))
            b = face.bounds(gn)
            if b:
                r = math.radians(deg)
                co, si = math.cos(r), math.sin(r)
                for px, py in ((b[0], b[1]), (b[2], b[1]), (b[0], b[3]), (b[2], b[3])):
                    lx, ly = ox + px * s, -py * s
                    pts.append((X + lx * co - ly * si, Y + lx * si + ly * co))
        theta += w / radius
    return '\n'.join(out), total, pts


def swash(x0, y0, length, depth, thick):
    """A hand-drawn tapered underline sweep.

    Pointed at both ends and fattest around a third of the way along, rising to
    a flick at the right. This gesture is the signature of a dance-hall wordmark
    and no font ships it, so it is drawn rather than set.
    """
    x1 = x0 + length
    xa, xb = x0 + length * 0.26, x0 + length * 0.78
    # The right end lifts well above where the stroke started, which is the flick
    # that makes this read as a drawn flourish rather than a plain underline.
    tipy = y0 - depth * 2.10
    return ('M %.2f %.2f C %.2f %.2f, %.2f %.2f, %.2f %.2f '
            'C %.2f %.2f, %.2f %.2f, %.2f %.2f Z'
            % (x0, y0,
               xa, y0 + depth * 1.30, xb, y0 + depth * 0.95, x1, tipy,
               xb, y0 + depth * 0.95 + thick * 1.15, xa, y0 + depth * 1.30 + thick * 1.45, x0, y0))


def crop(pts, pad):
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    x0, y0, x1, y1 = min(xs) - pad, min(ys) - pad, max(xs) + pad, max(ys) + pad
    return x0, y0, x1 - x0, y1 - y0


def svg(body, box, fg='#111111', bg=None):
    x, y, w, h = box
    ground = ('<rect x="%.2f" y="%.2f" width="%.2f" height="%.2f" fill="%s"/>'
              % (x, y, w, h, bg)) if bg else ''
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="%.2f %.2f %.2f %.2f" '
            'width="%.0f" height="%.0f">%s<g fill="%s">%s</g></svg>'
            % (x, y, w, h, w, h, ground, fg, body))
