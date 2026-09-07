# -*- coding: utf-8 -*-
"""Update copy for the rebuilt arrow."""
import io

s = io.open('sheet.py', encoding='utf-8').read()
s = s.replace(
    """           'THE and BAND sitting in the breaks. The arrows are now drawn the way '
           'the ones in the band badge are: a feather at the tail built from '
           'individual barbs radiating off the shaft, so the shaft stays visible '
           'through it. That detail is the whole difference. A filled vane closes '
           'into a solid paddle however elegantly it is shaped, because the halves '
           'meet across the shaft, and that paddle is what made two earlier '
           'attempts look cheap. The head is barbed with its base cut back between '
           'the barbs. Letterforms untouched.'),""",
    """           'THE and BAND sitting in the breaks. The arrows were rebuilt from '
           'scratch after four attempts that all looked like clip art. Two things '
           'were wrong. Every shape was made of straight segments, because the path '
           'helper only ever emitted line commands, so a polygon head and a '
           'rectangular shaft could never look drawn however the proportions were '
           'tuned. And they were designed zoomed in, where a feather can carry '
           'detail, when in the mark the arrow is a rule sitting beside small caps '
           'and none of that detail can resolve. These are curves, with far fewer '
           'parts: a shaft that tapers, a point with slightly concave flanks, and '
           'two swept ticks at the tail. Letterforms untouched.'),""")
io.open('sheet.py', 'w', encoding='utf-8', newline='\n').write(s)
print('  sheet.py updated')

t = io.open('shell.py', encoding='utf-8').read()
t = t.replace(
    """You picked that one, so the arrows themselves have been
redrawn three times, and the last pass was against the arrows in the band badge
you sent. Those draw the feather as individual barbs radiating off the shaft,
which keeps the shaft visible through the fletching. A filled vane closes into a
solid paddle however elegantly it is shaped, because the two halves meet across
the shaft, and that paddle is what made the earlier attempts look cheap.</p>""",
    """You picked that one, so the arrows were rebuilt from
scratch. Four earlier attempts all read as clip art for two reasons. Every shape
was made of straight segments, since the path helper only ever emitted line
commands, so a polygon head on a rectangular shaft could never look drawn no
matter how the proportions were tuned. And each was designed zoomed in, where a
feather can carry detail, when in the mark the arrow is a rule beside small caps
and that detail only ever prints as fuzz. These are curves with far fewer parts:
a tapering shaft, a point with slightly concave flanks, and two swept ticks at
the tail. They were judged at the size they are actually used at.</p>""")

t = t.replace(
    """<li><strong>The chosen mark is in good shape.</strong> Sancreek with arrow rules
measures 12.7 per cent full size and 8.9 on a hat, which clears embroidery. Rye
stays print only at 47 per cent, and that is the face rather than the direction:
Sancreek, Bevan and Rammetto all clear in small format.</li>""",
    """<li><strong>The chosen mark is in good shape.</strong> Sancreek with arrow rules
measures 11.2 per cent full size and 6.9 on a hat, so it clears embroidery at both
sizes. Rye stays print only at 47 per cent, and that is the face rather than the
direction: Sancreek, Bevan and Rammetto all clear in small format.</li>""")

t = t.replace(
    """Rye alone measures 47.1 per cent too fine and the same Rye with arrows
and a crow measures 37.4, which is that effect at its real size.""",
    """Rye alone measures 47.1 per cent too fine and the same Rye with arrows
and a crow measures 41.1, which is that effect at its real size.""")
io.open('shell.py', 'w', encoding='utf-8', newline='\n').write(t)
print('  shell.py updated')
