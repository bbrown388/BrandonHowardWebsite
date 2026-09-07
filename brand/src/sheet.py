# -*- coding: utf-8 -*-
"""Build the decision sheet for the Brandon Howard merch mark."""
import json, io

marks = {m['key']: m for m in json.load(open('out/marks.json', encoding='utf-8'))}
sk = json.load(open('strokes.json', encoding='utf-8'))

INK, PAPER = '#0A0A0A', '#F2EADC'

def render(key, fill, width=None, cls=''):
    m = marks[key]; x, y, w, h = m['box']
    wa = ' width="%d" height="%d"' % (width, round(width * h / w)) if width else ''
    return ('<svg class="%s" viewBox="%.2f %.2f %.2f %.2f"%s '
            'preserveAspectRatio="xMidYMid meet" role="img" aria-label="%s">'
            '<g fill="%s">%s</g></svg>' % (cls, x, y, w, h, wa, m['label'], fill, m['body']))

def data(key, label):
    s = sk[key]
    tone = 'ok' if s['emb'] < 12 else 'warn' if s['emb'] < 30 else 'bad'
    return ('<div class="data"><div class="dl">%s</div>'
            '<dl><div><dt>Screen / DTG</dt><dd>%.1f%% fine</dd></div>'
            '<div><dt>Embroidery</dt><dd class="%s">%.1f%% fine</dd></div></dl>'
            '<p class="verdict %s">%s</p></div>'
            % (label, s['dtg'], tone, s['emb'], tone, s['verdict']))

CARDS = [
 dict(k='gh-bodoni', hat='gh-bodoni-hat', alt='gh-bodoni-tag',
      altlab='Strap line swapped for the tagline',
      title='Bodoni + Alex Brush', tag='Closest to the Gruene sign',
      faces='Bodoni Moda Black, Alex Brush',
      body='The high contrast serif and the fine looping script are what make the '
           'Gruene sign read the way it does, so this is the nearest thing to what '
           'you pointed at. It is also the most fragile: those hairlines are the '
           'reason the embroidery number below is poor.'),
 dict(k='gh-playfair', hat='gh-playfair-hat',
      title='Playfair + Kaushan', tag='The one that survives a hat',
      faces='Playfair Display Black, Kaushan Script',
      body='Same layout, heavier brush script. It gives up a little of the vintage '
           'delicacy and gets back a mark that can actually be stitched. On the '
           'measurements this is the only dance hall option that clears embroidery '
           'at hat size.'),
 dict(k='gh-rye', hat='gh-rye',
      title='Rye + Great Vibes', tag='More saloon than dance hall',
      faces='Rye, Great Vibes',
      body='A western slab arch over a formal script. It leans further into old '
           'Texas than the Gruene sign does. Worth seeing, but the thinnest of the '
           'set by a distance.'),
 dict(k='am-alamo', hat='am-alamo-hat',
      title='Alamo lettering', tag='The ALAMO word, not DRAFTHOUSE',
      faces='Poppins Black with a constructed arch A',
      body='The word ALAMO on that marquee is custom lettering rather than a '
           'typeface, which their own brand manual confirms, so there is nothing '
           'to buy. This rebuilds it. Poppins Black was picked as the base '
           'because it matches the reference on the two things that can be '
           'measured, stem to cap height within a hundredth and a genuinely '
           'circular O, and then the A was constructed: a half round arch on two '
           'vertical legs with a low crossbar, no pointed apex. His name happens '
           'to need only that one special letter, since the other oddities on the '
           'sign are the angled L foot and the arched M and neither letter is in '
           'BRANDON HOWARD.'),
 dict(k='am-archivo', hat='am-archivo-hat',
      title='Archivo Expanded Black', tag='Closest to your marquee photo',
      faces='Archivo, expanded and black',
      body='The wide heavy grotesque from the first direction, stacked and ruled '
           'like a painted marquee panel. Reads at any distance and holds up '
           'small.'),
 dict(k='am-jost', hat='am-jost',
      title='Jost', tag='What the Alamo manual actually specifies',
      faces='Jost, an open Futura',
      body='The Alamo brand manual names Futura Std Bold as its primary face. Jost '
           'is an open licensed Futura, so this is the honest version of the '
           'original ask.'),
 dict(k='am-anton', hat='am-anton',
      title='Anton', tag='Strongest small, most generic',
      faces='Anton',
      body='Condensed and very heavy. Best measurements of anything here by a wide '
           'margin, and the least distinctive. A good utility mark for small '
           'placements if the main mark goes elsewhere.'),
]

def card(c):
    extra = ''
    if c.get('alt'):
        extra = ('<div class="alt"><div class="dl">%s</div>'
                 '<div class="sw light small">%s</div></div>'
                 % (c['altlab'], render(c['alt'], INK)))
    return """
<article class="card">
  <header class="ch">
    <div><h3>%s</h3><p class="faces">%s</p></div>
    <span class="pill">%s</span>
  </header>
  <div class="sw light">%s</div>
  <div class="sw dark">%s</div>
  %s
  <div class="hat">
    <div class="dl">Actual size, 4 in hat front</div>
    <div class="sw light hatsw">%s</div>
  </div>
  <p class="note">%s</p>
  <div class="grid2">%s%s</div>
</article>""" % (c['title'], c['faces'], c['tag'],
                 render(c['k'], INK), render(c['k'], PAPER), extra,
                 render(c['hat'], INK, width=384),
                 c['body'],
                 data(c['k'], 'Full size, 4 in wide'),
                 data(c['hat'], 'Small format lockup'))

dance = ''.join(card(c) for c in CARDS[:3])
marq  = ''.join(card(c) for c in CARDS[3:])
io.open('sheet_body.html', 'w', encoding='utf-8', newline='\n').write(dance + '\x00' + marq)
print('  cards built: %d dance hall, %d marquee' % (3, 3))
