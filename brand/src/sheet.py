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
 dict(k='gh-bodoni', g='dance', hat='gh-bodoni-hat', alt='gh-bodoni-tag',
      altlab='The other way to map the name onto this layout',
      title='Bodoni + Alex Brush', tag='Closest to the Gruene sign',
      faces='Bodoni Moda Black, Alex Brush',
      body='The high contrast serif and the fine looping script are what make the '
           'Gruene sign read the way it does, so this is the nearest thing to what '
           'you pointed at. THE sits above the arch and BAND takes the strap line '
           'slot, so the whole name reads straight down the mark. It is also the '
           'most fragile of the set: those hairlines are why the embroidery number '
           'below is poor. The version underneath maps the name the other way, the '
           'way Gruene maps its own, with the identifying words arched and the type '
           'word carrying the script.'),
 dict(k='gh-playfair', g='dance', hat='gh-playfair-hat',
      title='Playfair + Kaushan', tag='Best of the dance hall set',
      faces='Playfair Display Black, Kaushan Script',
      body='Same layout, heavier brush script. It gives up a little of the vintage '
           'delicacy and gets back a far more robust mark. Worth knowing what the '
           'longer name cost here: before BAND was added this cleared embroidery at '
           'hat size outright. BAND cannot be dropped the way a motto can, and the '
           'extra fine ink pushed it back over the line. It is still comfortably '
           'the strongest of the three dance hall options for print.'),
 dict(k='gh-rye', g='dance', hat='gh-rye',
      title='Rye + Great Vibes', tag='More saloon than dance hall',
      faces='Rye, Great Vibes',
      body='A western slab arch over a formal script. It leans further into old '
           'Texas than the Gruene sign does. Worth seeing, but the thinnest of the '
           'set by a distance.'),
 dict(k='am-slab', g='marq', hat='am-slab-hat', alt='am-slab-ultra',
      altlab='Ultra, the same idea pushed heavier and quirkier',
      title='Alfa Slab One', tag='The honky-tonk poster',
      faces='Alfa Slab One',
      body='A heavy Americana slab, and the furthest thing here from geometric '
           'without being a novelty face. Bracketed serifs, a lot of ink, and it '
           'looks like it was printed on a letterpress bill for a Saturday night '
           'show. If the objection to the first one was that it felt too clean '
           'and modern, this is the direct answer.'),
 dict(k='am-oswald', g='marq', hat='am-oswald-hat',
      title='Oswald Bold', tag='Already his website face',
      faces='Oswald Bold',
      body='Condensed gothic. Lean, hard and modern, with none of the roundness '
           'of the first attempt. It is also the display face already running on '
           'his site, so this is the only option that ties the mark to something '
           'that exists rather than starting a second visual language.'),
 dict(k='am-stencil', g='marq', hat='am-stencil-hat',
      title='Black Ops One', tag='Least pretty by a distance',
      faces='Black Ops One',
      body='Stencil, with the breaks cut through the strokes. It reads military '
           'more than country, which may be too far, but for a band whose tagline '
           'is No Pretty Boy Country it is the one that argues hardest for the '
           'line.'),
 dict(k='am-varsity', g='marq', hat='am-varsity-hat',
      title='Graduate', tag='Vintage varsity',
      faces='Graduate',
      body='Collegiate slab, the lettering off an old letterman jacket or a '
           'stadium scoreboard. It reads American and vintage without going to '
           'the saloon, which makes it the most versatile of the set. It is also '
           'the lightest, so watch the measurements.'),
 dict(k='am-alamo', g='marq', hat='am-alamo-hat',
      title='Alamo lettering', tag='What he turned down',
      faces='Poppins Black with a constructed flat-topped A',
      body='Kept here only so the comparison is honest. This is the rebuild of the '
           'custom ALAMO lettering, and the reason it probably did not land is that '
           'the underlying face is geometric and round, which reads friendly. Every '
           'option above moves away from that in a different direction.'),
 dict(k='am-rye', g='west', hat='am-rye-hat',
      title='Rye', tag='The one you liked',
      faces='Rye',
      body='Spurred western slab. Saloon door, rodeo bill, Lone Star, and the '
           'least ambiguous about where the band is from of anything built so far. '
           'The problem was never the character. It is that the spurs are '
           'hairlines, so it loses 46 per cent of its ink at hat size. Everything '
           'below keeps the flavour and adds weight.'),
 dict(k='am-sancreek', g='west', hat='am-sancreek-hat',
      title='Sancreek', tag='Best of the western set',
      faces='Sancreek',
      body='The same spurred western language with more ink in the stems. If what '
           'you liked was specifically the western lettering rather than the general '
           'vintage feel, this is the one to hold up against Rye first. It is also '
           'the strongest of this group on the measurements by a clear margin, '
           'turning Rye 46 per cent into 14.'),
 dict(k='am-swanky', g='west', hat='am-swanky-hat',
      title='Fontdiner Swanky', tag='More swagger',
      faces='Fontdiner Swanky',
      body='Vintage American with flared spurs rather than square ones. Less rodeo, '
           'more roadhouse sign, with a bit of movement in the letterforms that the '
           'straighter faces do not have.'),
 dict(k='am-bevan', g='west', hat='am-bevan-hat',
      title='Bevan', tag='Looks tougher than it measures',
      faces='Bevan',
      body='Heavy Egyptian slab, and unmistakably old American printing. I expected '
           'this to be the durable one, since it drops the spurs entirely, and the '
           'measurement says otherwise: its serif brackets and the thin horizontals '
           'in the small type give it the worst full size number in the western set. '
           'Good for shirts and posters, poor for stitching.'),
 dict(k='am-rammetto', g='west', hat='am-rammetto-hat',
      title='Rammetto One', tag='Heaviest of the group',
      faces='Rammetto One',
      body='The heaviest thing in the whole set. Poster weight with softened '
           'corners. Furthest from Rye in detail, but doing the same job: loud, '
           'vintage and American, and it holds at any size you throw at it.'),
 dict(k='am-sancreek-arrows', g='orn', hat='am-sancreek-arrows-hat',
      title='Arrow rules', tag='The one that works',
      faces='Sancreek',
      body='The rules themselves become arrows, pointing out from the centre with '
           'THE and BAND sitting in the breaks. This is the version that reads as '
           'deliberate rather than decorated: the arrows are unmistakable at any '
           'size, they use structure the mark already had, and they leave the '
           'letterforms completely alone.'),
 dict(k='am-sancreek-crow', g='orn', hat='am-sancreek-crow-hat',
      title='Crow on the rule', tag='A bird on a sign',
      faces='Sancreek',
      body='A crow perched on the top rule, off to one side, the way a bird sits on '
           'a real roadside sign. It is a drawn silhouette rather than clip art, '
           'built blunt on purpose so it holds at small sizes. Worth saying it is a '
           'first pass: an illustrator would push the bill heavier and the tail '
           'longer, and that is a job worth paying for if this direction wins.'),
 dict(k='am-rye-arrows-crow', g='orn', hat='am-rye-arrows-crow-hat',
      title='Arrows and crow, on Rye', tag='Both devices at once',
      faces='Rye',
      body='Both ideas together on the face you started from, with the crow perched '
           'on the arrow rather than a plain rule. Read the measurements on this one '
           'carefully, see the note below the section.'),
 dict(k='am-sancreek-crossed', g='orn', hat='am-sancreek-crossed-hat',
      title='Crossed arrows', tag='Quietest option',
      faces='Sancreek',
      body='Letters untouched, crossed arrows sitting under the mark as a device you '
           'could also use on its own: a sleeve print, a hat back, a stamp on a '
           'setlist. The most separable of the four, and the easiest to drop when it '
           'is not wanted.'),
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

dance = ''.join(card(c) for c in CARDS if c.get('g') == 'dance')
groups = ('dance', 'marq', 'west', 'orn')
io.open('sheet_body.html', 'w', encoding='utf-8', newline='\n').write(
    chr(0).join(''.join(card(c) for c in CARDS if c.get('g') == g) for g in groups))
print('  cards built: ' + ', '.join(
    '%d %s' % (sum(1 for c in CARDS if c.get('g') == g), g) for g in groups))
