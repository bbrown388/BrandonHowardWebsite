# -*- coding: utf-8 -*-
"""Copy update: the arrow is now the traced public domain drawing."""
import io

s = io.open('sheet.py', encoding='utf-8').read()
old = s[s.index("      title='Arrow rules', tag='Chosen',"):s.index(" dict(k='am-sancreek-crow'")]
new = """      title='Arrow rules', tag='Chosen',
      faces='Sancreek, with a traced public domain arrow',
      body='The rules themselves become arrows, pointing out from the centre with '
           'THE and BAND sitting in the breaks. The arrow is the drawing you '
           'found, traced to vector rather than redrawn: genuinely hand-inked, '
           'and better than anything I was going to arrive at from a description. '
           'It is public domain from publicdomainpictures.net, so it is free for '
           'merchandise with no attribution owed. The cost is the same one any '
           'inked arrow carries: all that fine barb work is thin ink, so this '
           'measures 23.1 per cent at full size and 19.7 on a hat, against 18.4 '
           'and 9.4 for the bare wordmark. It does not clear embroidery.'),
"""
s = s.replace(old, new)
io.open('sheet.py', 'w', encoding='utf-8', newline='\n').write(s)
print('  sheet.py updated')

t = io.open('shell.py', encoding='utf-8').read()

old = t[t.index('You picked that one, so the arrows were rebuilt to'):t.index('</p>', t.index('You picked that one, so the arrows were rebuilt to'))]
new = """You picked that one, and the arrow is now the
drawing you supplied, traced to vector rather than redrawn from it. It is public
domain, from publicdomainpictures.net, which makes it free to use on merchandise
with no attribution owed. It is also plainly better than what I was producing by
working from a description, and using it directly was the right call"""
t = t.replace(old, new)

old = t[t.index('<div class="callout">\n<p><strong>The detailed arrow costs you embroidery'):t.index('</div>', t.index('<div class="callout">\n<p><strong>The detailed arrow costs you embroidery'))]
new = """<div class="callout">
<p><strong>An inked arrow costs embroidery, and the number is worth seeing.</strong>
All that fine barb work is thin ink. The mark measures 23.1 per cent too fine at
full size and 19.7 on a hat, against 18.4 and 9.4 for bare Sancreek with no
arrows at all. So the wordmark is fine and the fletching is what costs, and this
holds whether the arrow is the traced one or the plain one I drew.</p>
<p>Three ways to take it. Use it everywhere and accept that hats lose the
feathering to fill-in. Keep it for shirts, posters and the site and run something
plainer on hats, which is the two-file family already used in the dance hall
direction; <code>ornament.ARROW_STYLE</code> switches to a drawn arrow that
measures 11.2 and 6.9. Or have the traced artwork simplified for stitching, which
is a normal thing to ask an embroidery digitiser to do.</p>
"""
t = t.replace(old, new)

t = t.replace(
    """<li><strong>The chosen mark now needs a decision about hats.</strong> With the
hand-inked arrow it measures 23.6 per cent full size and 20.0 on a hat, where the
plain arrow it replaced was 11.2 and 6.9. Bare Sancreek without any arrows is 18.4
and 9.4, so the wordmark itself is fine; it is the fletching that costs. Rye stays
print only at 47 per cent regardless.</li>""",
    """<li><strong>The chosen mark needs a decision about hats.</strong> With the
traced arrow it measures 23.1 per cent full size and 19.7 on a hat. Bare Sancreek
without arrows is 18.4 and 9.4, so the wordmark is fine and the fletching is what
costs. A plainer drawn arrow is one setting away at 11.2 and 6.9. Rye stays print
only at 47 per cent regardless.</li>""")
io.open('shell.py', 'w', encoding='utf-8', newline='\n').write(t)
print('  shell.py updated')
