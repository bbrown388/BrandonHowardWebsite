# -*- coding: utf-8 -*-
"""Copy update for the hand-inked arrow and the cost it carries."""
import io

s = io.open('sheet.py', encoding='utf-8').read()
old = s[s.index("      title='Arrow rules', tag='Chosen',"):s.index(" dict(k='am-sancreek-crow'")]
new = """      title='Arrow rules', tag='Chosen',
      faces='Sancreek',
      body='The rules themselves become arrows, pointing out from the centre with '
           'THE and BAND sitting in the breaks. The arrows are drawn to the '
           'hand-inked reference you sent: fletching as fifteen fine barbs a '
           'side, a shaft that runs the whole length with a hairline split down '
           'it, and a head with concave flanks and blunt-ended barbs. It costs '
           'something real, and the number below is it. All that fine detail is '
           'thin ink, so this went from 11.2 per cent to 23.6 at full size and '
           'from 6.9 to 20.0 on a hat. It no longer clears embroidery. The plain '
           'version that did is one setting away, see the note under this '
           'section.'),
"""
s = s.replace(old, new)
io.open('sheet.py', 'w', encoding='utf-8', newline='\n').write(s)
print('  sheet.py updated')

t = io.open('shell.py', encoding='utf-8').read()
old = t[t.index('You picked that one, so the arrows were rebuilt from'):t.index('</p>', t.index('You picked that one, so the arrows were rebuilt from'))]
new = """You picked that one, so the arrows were rebuilt to
the hand-inked reference you sent. What makes that drawing work is the fletching:
fifteen fine barbs a side rather than a few bars, leaning back, with the white
gaps falling out of the spacing. The shaft runs the whole length underneath so
the two vanes meet on it, and carries a hairline split, which is most of the
hand-drawn quality. The head has concave flanks, dead straight inner edges, and
barbs that end in a short flat instead of a knife point"""
t = t.replace(old, new)

anchor = t.index('<div class="callout">\n<p><strong>On the crow, plainly')
insert = """<div class="callout">
<p><strong>The detailed arrow costs you embroidery, and the number is worth
seeing.</strong> All that fine barb work is thin ink. Against the plain curved
arrow it was replacing, this version goes from 11.2 per cent too fine to 23.6 at
full size, and from 6.9 to 20.0 on a hat. It no longer clears the embroidery
threshold, and even the print figure moved from 1.7 to 10.2.</p>
<p>That is the same trade this project keeps running into: detail at rule scale
does not survive being stitched. Three ways to take it. Use this everywhere and
accept hats will lose the feathering. Keep it for shirts, posters and the site
and put the plain version on hats, which is the two-file family already used in
the dance hall direction. Or thin the difference by cutting the barb count and
thickening what remains, which is two numbers in <code>ornament.fletching</code>.</p>
<p>The plain arrow has not been thrown away. <code>src/arrow3.py</code> still
holds it along with three other tails.</p>
</div>
"""
t = t[:anchor] + insert + t[anchor:]

t = t.replace(
    """<li><strong>The chosen mark is in good shape.</strong> Sancreek with arrow rules
measures 11.2 per cent full size and 6.9 on a hat, so it clears embroidery at both
sizes. Rye stays print only at 47 per cent, and that is the face rather than the
direction: Sancreek, Bevan and Rammetto all clear in small format.</li>""",
    """<li><strong>The chosen mark now needs a decision about hats.</strong> With the
hand-inked arrow it measures 23.6 per cent full size and 20.0 on a hat, where the
plain arrow it replaced was 11.2 and 6.9. Bare Sancreek without any arrows is 18.4
and 9.4, so the wordmark itself is fine; it is the fletching that costs. Rye stays
print only at 47 per cent regardless.</li>""")
io.open('shell.py', 'w', encoding='utf-8', newline='\n').write(t)
print('  shell.py updated')
