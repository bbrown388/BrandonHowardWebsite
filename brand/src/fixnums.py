# -*- coding: utf-8 -*-
"""Correct every measured figure in the sheet after the capture-cap bug."""
import io

s = io.open('sheet.py', encoding='utf-8').read()

s = s.replace(
    "'still clears embroidery in small format at 10.2 per cent.'),",
    "'still clears embroidery in small format at 9.8 per cent.'),")

s = s.replace(
    """           'hairlines, so it loses 46 per cent of its ink at hat size. Everything '
           'below keeps the flavour and adds weight.'),""",
    """           'hairlines, so it loses 47 per cent of its ink at hat size and the '
           'small format lockup is barely better. Everything below keeps the '
           'flavour and adds weight.'),""")

s = s.replace(
    """           'vintage feel, this is the one to hold up against Rye first. It is also '
           'the strongest of this group on the measurements by a clear margin, '
           'turning Rye 46 per cent into 14.'),""",
    """           'vintage feel, this is the one to hold up against Rye first. It is also '
           'the strongest of this group on the measurements, turning Rye 47 per '
           'cent into 18 at full size, and its small format lockup clears '
           'embroidery outright at 9.4.'),""")

s = s.replace(
    """      title='Bevan', tag='Looks tougher than it measures',
      faces='Bevan',
      body='Heavy Egyptian slab, and unmistakably old American printing. I expected '
           'this to be the durable one, since it drops the spurs entirely, and the '
           'measurement says otherwise: its serif brackets and the thin horizontals '
           'in the small type give it the worst full size number in the western set. '
           'Good for shirts and posters, poor for stitching.'),""",
    """      title='Bevan', tag='Durable, as it looks',
      faces='Bevan',
      body='Heavy Egyptian slab, and unmistakably old American printing. It drops '
           'the spurs entirely and gets back exactly the durability that suggests: '
           '15.1 per cent full size and 10.9 on a hat, which clears. An earlier '
           'version of this sheet claimed the reverse, on the strength of a broken '
           'measurement. That has been corrected.'),""")

io.open('sheet.py', 'w', encoding='utf-8', newline='\n').write(s)
print('  sheet.py card figures corrected')


t = io.open('shell.py', encoding='utf-8').read()

t = t.replace(
    """<li><strong>Oswald Bold is the surprise.</strong> It is the best performing mark
in the entire set by a wide margin, 6.9 per cent full size and 2.4 per cent on a
hat, where nothing else gets under 10. It is also already the display face on his
website, so it is the only option that joins the mark to something that exists
instead of opening a second visual language. If he is at all warm to it, it
solves the hat problem outright.</li>""",
    """<li><strong>Oswald Bold still measures best</strong>, at 11.0 per cent full size
and 6.5 on a hat. It is also already the display face on his website, so it is the
only option that joins the mark to something that already exists rather than
opening a second visual language.</li>""")

t = t.replace(
    """<li><strong>Alfa Slab One if he wants character over convenience.</strong> It is
the strongest answer to the specific objection, since it is about as far from
clean and geometric as you can get without a novelty face, and it still clears
embroidery in small format at 10.2 per cent.</li>""",
    """<li><strong>Alfa Slab One if he wants character over convenience.</strong> About
as far from clean and geometric as you can get without a novelty face, and it
still clears embroidery in small format at 9.8 per cent.</li>""")

t = t.replace(
    """<li><strong>If the western direction wins, it is Sancreek and it costs you
hats.</strong> Rye is print only at 46 per cent, and Sancreek is the best of the
group at 14, but nothing western clears the embroidery bar. That is not a bad
face choice, it is the direction itself: spurs and brackets are what make
lettering read western and they are what a stitch cannot hold.</li>""",
    """<li><strong>The chosen mark is in good shape.</strong> Sancreek with arrow rules
measures 12.7 per cent full size and 8.9 on a hat, which clears embroidery. Rye
stays print only at 47 per cent, and that is the face rather than the direction:
Sancreek, Bevan and Rammetto all clear in small format.</li>""")

t = t.replace(
    """<p>Worth saying plainly: this direction is expensive for embroidery no matter
which face you pick. Spurs, brackets and thin horizontals are what make lettering
read as western, and they are exactly what a stitch cannot hold. Nothing in this
group clears the embroidery threshold. Sancreek gets closest and turns Rye 46 per
cent into 14.</p>""",
    """<p>The cost sits in the face rather than the direction. The spurs on Rye are
hairlines and it loses 47 per cent of its ink at hat size, but Sancreek, Bevan and
Rammetto all clear the embroidery threshold in small format. Sancreek is the pick:
it keeps the spurred western language and turns 47 per cent into 18 at full size
and 9.4 on a hat.</p>""")

t = t.replace(
    """<p><strong>Read the measurements in this section carefully.</strong> The metric
is a share of total ink, so adding a solid crow or a pair of heavy arrows raises
the denominator and the percentage falls without a single hairline getting any
thicker. Rye on its own measures 45.7 per cent too fine; the same Rye with arrows
and a crow measures 9.6 per cent. Nothing about the letters changed. Judge
letterforms by the face numbers in the western section.</p>""",
    """<p><strong>Read the measurements here with the ornament in mind.</strong> The
metric is a share of total ink, so a solid crow or a pair of heavy arrows raises
the denominator and pulls the percentage down without any hairline getting
thicker. Rye alone measures 47.1 per cent too fine and the same Rye with arrows
and a crow measures 37.4, which is that effect at its real size. An earlier
version of this sheet put the second figure at 9.6 and made a great deal of it.
That was a broken measurement rather than a real effect.</p>""")

t = t.replace(
    """<p>This is the same failure already seen on the BD mark, where fine strokes
dropped out below about three and a half inches on DTG. Embroidery is stricter
again.</p>""",
    """<p>This is the same failure already seen on the BD mark, where fine strokes
dropped out below about three and a half inches on DTG. Embroidery is stricter
again.</p>
<div class="callout">
<p><strong>These figures were re-measured after a bug in the harness.</strong> All
the marks were being rendered onto a single very tall page and captured in one
screenshot. Chrome caps a full page capture at roughly 16384 pixels, and below
that seam the stitched image is wrong, so every mark past it was measured against
whatever artwork happened to land in its slot. The numbers came out plausible,
which is why it survived several rounds unnoticed.</p>
<p>Measurement now runs in chunks well under the cap, every tile is stamped with
its key, and the stamp is verified before the tile is trusted. Twenty four of the
thirty five marks moved. The worst case reversed a conclusion outright: Bevan was
reported as the weakest western face at 51.6 per cent and actually measures
15.1.</p>
</div>""")

io.open('shell.py', 'w', encoding='utf-8', newline='\n').write(t)
print('  shell.py figures corrected and the bug documented')
