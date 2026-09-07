# -*- coding: utf-8 -*-
import io
dance, marq, west, orn = io.open('sheet_body.html', encoding='utf-8').read().split(chr(0))

HEAD = """<title>Brandon Howard Band Marks</title>
<style>
/* Palette is lifted from Brandon's site tokens so this sits inside the identity
   that already exists: ink, paper, brass. Neutrals are warmed toward the brass
   rather than left as flat grey. The page face is deliberately the plain system
   stack: the logotypes are the subject here, and any characterful page type
   would compete with the thing being judged. */
:root {
  --bg:#FBF7EF; --surface:#FFFFFF; --line:#E0D6C4; --line2:#EFE7D9;
  --fg:#1A1713; --muted:#6E6455; --brass:#9A6F1E;
  --ok:#3F6B3A; --warn:#8A5A12; --bad:#8E3A2C;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg:#14120F; --surface:#1D1A16; --line:#332E27; --line2:#262220;
    --fg:#EFE7D9; --muted:#9C9184; --brass:#C89B4A;
    --ok:#7FB177; --warn:#D5A048; --bad:#D97B67;
  }
}
:root[data-theme="dark"] {
  --bg:#14120F; --surface:#1D1A16; --line:#332E27; --line2:#262220;
  --fg:#EFE7D9; --muted:#9C9184; --brass:#C89B4A;
  --ok:#7FB177; --warn:#D5A048; --bad:#D97B67;
}
*{box-sizing:border-box}
body{
  margin:0; background:var(--bg); color:var(--fg);
  font:16px/1.62 ui-sans-serif,system-ui,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  -webkit-font-smoothing:antialiased;
}
.wrap{max-width:1080px;margin:0 auto;padding:52px 22px 96px}
h1{font-size:clamp(30px,5vw,46px);line-height:1.06;margin:0 0 14px;letter-spacing:-.018em;text-wrap:balance}
h2{font-size:13px;letter-spacing:.19em;text-transform:uppercase;color:var(--brass);
   margin:0 0 6px;font-weight:700}
h3{font-size:20px;margin:0;letter-spacing:-.01em}
p{margin:0 0 14px;max-width:66ch}
.lead{font-size:18px;color:var(--muted);max-width:62ch}
.eyebrow{font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:var(--muted);margin:0 0 10px}
.dl{font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);margin:0 0 8px}

section{margin-top:56px}
.sechead{border-top:1px solid var(--line);padding-top:22px;margin-bottom:26px}
.sechead p{margin:8px 0 0}

.card{background:var(--surface);border:1px solid var(--line);border-radius:3px;
      padding:24px;margin-bottom:26px}
.ch{display:flex;gap:16px;align-items:flex-start;justify-content:space-between;
    flex-wrap:wrap;margin-bottom:18px}
.faces{font-size:13px;color:var(--muted);margin:4px 0 0}
.pill{font-size:11px;letter-spacing:.13em;text-transform:uppercase;color:var(--brass);
      border:1px solid var(--brass);border-radius:999px;padding:5px 12px;white-space:nowrap}

/* Garment swatches hold their own colours in both themes. They stand for actual
   fabric, so flipping them with the page theme would misrepresent the print. */
.sw{border-radius:2px;padding:22px;display:flex;justify-content:center;align-items:center}
.sw.light{background:#F2EADC;border:1px solid var(--line)}
.sw.dark{background:#121110;border:1px solid #2A2724;margin-top:12px}
.sw svg{width:100%;max-width:620px;height:auto;display:block}
.sw.small svg{max-width:340px}
.alt{margin-top:20px;padding-top:18px;border-top:1px dashed var(--line)}
.hat{margin-top:20px;padding-top:18px;border-top:1px dashed var(--line)}
.hatsw{padding:16px}
.hatsw svg{width:384px;max-width:100%}

.note{margin:18px 0 0;color:var(--fg);font-size:15px}
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px;margin-top:18px}
.data{border:1px solid var(--line2);border-radius:2px;padding:13px 15px;background:var(--bg)}
.data dl{margin:0;display:flex;gap:22px;flex-wrap:wrap}
.data dl div{margin:0}
dt{font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
dd{margin:2px 0 0;font-size:17px;font-variant-numeric:tabular-nums}
dd.ok{color:var(--ok)} dd.warn{color:var(--warn)} dd.bad{color:var(--bad)}
.verdict{font-size:12.5px;margin:10px 0 0;max-width:none}
.verdict.ok{color:var(--ok)} .verdict.warn{color:var(--warn)} .verdict.bad{color:var(--bad)}

.callout{border-left:3px solid var(--brass);background:var(--surface);
         border-radius:0 3px 3px 0;padding:16px 20px;margin:22px 0}
.callout p:last-child{margin-bottom:0}
ul{margin:0 0 14px;padding-left:20px;max-width:66ch}
li{margin-bottom:7px}
table{border-collapse:collapse;width:100%;font-size:14px;margin-bottom:14px}
th,td{text-align:left;padding:9px 12px;border-bottom:1px solid var(--line2)}
th{font-size:11px;letter-spacing:.13em;text-transform:uppercase;color:var(--muted);font-weight:600}
.scroll{overflow-x:auto}
a{color:var(--brass)}
@media (max-width:640px){ .wrap{padding:34px 15px 70px} .card{padding:16px} .sw{padding:14px} }
</style>
"""

BODY = """
<div class="wrap">
<p class="eyebrow">Merch identity, first pass</p>
<h1>The Brandon Howard Band</h1>
<p class="lead">Seventeen candidate marks in four directions, each shown on a
light and a dark garment, then tested at the size that actually breaks logos: a
four inch hat front.</p>

<div class="callout">
<p><strong>Now built for the full band name.</strong> Four words need two more
slots than either reference gives you, and the two layouts solve it differently.
The dance hall marks put THE above the arch and BAND in the strap line slot, so
the name reads straight down. The marquee marks set THE and BAND into breaks in
the rules, which keeps the two big words as the only full height lines.</p>
<p>It cost something, and the cost is in the numbers below. A motto can be
dropped for a small placement. BAND cannot, so the small format lockups no longer
get to shed their finest ink.</p>
</div>

<div class="callout">
<p><strong>Four directions now.</strong> The first was
the Alamo Drafthouse marquee, specifically the ALAMO word rather than the
DRAFTHOUSE CINEMA line under it, which are two different faces. The second was the
Gruene Hall sign, which is a different animal: a word arched across the top, a
big script underneath carrying a swash, and a small letterspaced strap line below
that. Both are built here so you can see them side by side.</p>
</div>

<section>
<div class="sechead">
<h2>Direction one, dance hall</h2>
<h3 style="font-size:22px;margin-top:4px">BRANDON arched, Howard in script</h3>
<p>The Gruene layout you described, with BRANDON where GRUENE sits and Howard
where Hall sits. THE goes above the arch and BAND takes the strap line slot,
where Gruene puts its own "Texas' Oldest Dance Hall" line.</p>
<p>There is a second way to map the name onto this layout, shown inside the first
card: arch BRANDON HOWARD and let Band carry the script. That is actually the
closer parallel, since Gruene arches the identifying word and puts the type word
in script. It reads differently, so it is worth a look before you settle.</p>
</div>
__DANCE__
</section>

<section>
<div class="sechead">
<h2>Direction two, marquee</h2>
<h3 style="font-size:22px;margin-top:4px">Stacked caps in a ruled panel</h3>
<p>Brandon did not like the face on the first version of this, so the layout is
unchanged and the typeface is the variable. Five new directions below, then the
original at the bottom so the comparison is honest.</p>
<p>The likely problem with the first one is that its base is a geometric sans:
circular O, even strokes, no serifs, which reads clean and friendly. Every option
here moves away from that, and each moves in a different direction rather than
five shades of the same idea. THE and BAND stay set into breaks in the rules
throughout.</p>
<p>All six are normalised to the same cap height rather than the same point size,
which is the only fair way to compare a condensed gothic against a fat slab.</p>
</div>
__MARQ__
</section>

<section>
<div class="sechead">
<h2>Direction three, western</h2>
<h3 style="font-size:22px;margin-top:4px">Spurs, slabs and rodeo bills</h3>
<p>Iterating on Rye, which stays at the top of the group so it can be compared
directly. Its problem was never the character. The spurs are hairlines, so it
loses 46 per cent of its ink at hat size, and the four below hold the flavour
while carrying more weight.</p>
<p>Worth saying plainly: this direction is expensive for embroidery no matter
which face you pick. Spurs, brackets and thin horizontals are what make lettering
read as western, and they are exactly what a stitch cannot hold. Nothing in this
group clears the embroidery threshold. Sancreek gets closest and turns Rye 46 per
cent into 14.</p>
</div>
__WEST__
</section>

<section>
<div class="sechead">
<h2>Direction four, arrows and crows</h2>
<h3 style="font-size:22px;margin-top:4px">Devices rather than decoration</h3>
<p>You were right that the A in Sancreek already reads a little like an arrow,
and the first thing I tried was leaning on exactly that: mirrored barbs at the
apex to make the existing spur look deliberate.</p>
<p><strong>It did not work, and it is worth saying why.</strong> The apex of
these faces is a fine point sitting well above the widest part of the letter, so
anything positioned from the letter box lands in mid air and reads as a small
detached shape hovering over the A rather than part of it. Making that idea work
means editing the outline of the glyph itself, adding the barbs as real nodes on
the A and rebalancing the apex around them. That is a type designer sitting in a
vector editor for an hour, not something worth faking, and it is a reasonable
thing to commission if you like the idea enough.</p>
<p>So the arrows went where they read: into the structure of the mark instead of
into the letters. You picked that one, so the arrows themselves have been
redrawn three times, and the last pass was against the arrows in the band badge
you sent. Those draw the feather as individual barbs radiating off the shaft,
which keeps the shaft visible through the fletching. A filled vane closes into a
solid paddle however elegantly it is shaped, because the two halves meet across
the shaft, and that paddle is what made the earlier attempts look cheap.</p>
</div>
__ORN__
<div class="callout">
<p><strong>On the crow, plainly: it is not there.</strong> That is five redraws
against your reference and it still reads closer to a grackle than a crow. The
idea is good and the placement works. The bird is the problem, and the problem is
the method: hand coding polygon coordinates is a reasonable way to draw an arrow
and a poor way to draw an animal, because every correction is a guess at a number
rather than a line you can see while you pull it.</p>
<p>Three honest ways forward, in the order I would take them. <strong>License a
vector crow.</strong> The image you sent is Alamy stock and licensing it outright
is usually tens of dollars, which buys a finished silhouette immediately and
settles the rights question at the same time. <strong>Commission one</strong>, if
the bird is going to carry the brand rather than decorate it. Or <strong>keep me
at it</strong>, which I am happy to do, but the returns per attempt are clearly
falling and you should know that before spending more of the session on it.</p>
<p>Meanwhile the arrow mark stands on its own without a bird, and that is what
the top of this section shows.</p>
</div>
<div class="callout">
<p><strong>Read the measurements in this section carefully.</strong> The metric
is a share of total ink, so adding a solid crow or a pair of heavy arrows raises
the denominator and the percentage falls without a single hairline getting any
thicker. Rye on its own measures 45.7 per cent too fine; the same Rye with arrows
and a crow measures 9.6 per cent. Nothing about the letters changed. Judge
letterforms by the face numbers in the western section.</p>
</div>
</section>

<section>
<div class="sechead">
<h2>What the numbers mean</h2>
</div>
<p>Twelve marks were rendered at exactly four inches wide at 300 dpi and measured
for how much of their ink sits in strokes too fine for a given process. A morphological
opening removes precisely the ink thinner than a given width, so the percentages
are measured rather than estimated.</p>
<div class="scroll">
<table>
<tr><th>Column</th><th>Threshold</th><th>Why it matters</th></tr>
<tr><td>Screen / DTG</td><td>0.42 mm</td><td>Below this, ink bridges or drops out on a direct to garment print. Every option here is comfortable.</td></tr>
<tr><td>Embroidery</td><td>1.10 mm</td><td>A stitch cannot render a stroke finer than roughly a millimetre. This is the column that decides hats.</td></tr>
</table>
</div>
<p>This is the same failure already seen on the BD mark, where fine strokes
dropped out below about three and a half inches on DTG. Embroidery is stricter
again.</p>
</section>

<section>
<div class="sechead">
<h2>Recommendation</h2>
</div>
<p>Treat it as a small family rather than one file, which is normal for an artist
mark:</p>
<ul>
<li><strong>Oswald Bold is the surprise.</strong> It is the best performing mark
in the entire set by a wide margin, 6.9 per cent full size and 2.4 per cent on a
hat, where nothing else gets under 10. It is also already the display face on his
website, so it is the only option that joins the mark to something that exists
instead of opening a second visual language. If he is at all warm to it, it
solves the hat problem outright.</li>
<li><strong>Alfa Slab One if he wants character over convenience.</strong> It is
the strongest answer to the specific objection, since it is about as far from
clean and geometric as you can get without a novelty face, and it still clears
embroidery in small format at 10.2 per cent.</li>
<li><strong>If the western direction wins, it is Sancreek and it costs you
hats.</strong> Rye is print only at 46 per cent, and Sancreek is the best of the
group at 14, but nothing western clears the embroidery bar. That is not a bad
face choice, it is the direction itself: spurs and brackets are what make
lettering read western and they are what a stitch cannot hold.</li>
<li><strong>Bodoni + Alex Brush</strong> stays the pick in the dance hall
direction, for tee fronts, posters, backdrops and the website.</li>
</ul>
</ul>
</section>

<section>
<div class="sechead">
<h2>Licensing and two cautions</h2>
</div>
<p><strong>Fonts are clear.</strong> Every face here is under the SIL Open Font
License: Bodoni Moda, Alex Brush, Playfair Display, Kaushan Script, Rye, Great
Vibes, Alfa Slab One, Oswald, Black Ops One, Graduate, Ultra, Sancreek, Fontdiner
Swanky, Bevan, Rammetto One and Poppins. That licence permits commercial use including
merchandise sold for money, with no fee and no attribution needed on the product.
This was chosen deliberately over the actual Alamo faces, which are commercial
licences he would have to buy.</p>
<p><strong>On the rebuilt Alamo A.</strong> Typeface designs are not copyrightable
in the United States, and this is in any case a letter drawn from geometry rather
than a copy of their outline. What is protected is their logo as a whole, which
is why none of the marquee housing, the badge shape or their name appears
anywhere here.</p>
<p><strong>On the Gruene resemblance.</strong> What is borrowed is a layout
convention, an arched word over a script over a strap line, which is common to
dozens of Texas dance halls and roadhouses and is not something anyone owns. The
typefaces are different, the swash is drawn from scratch rather than traced, and
the words are his. That is the line to stay on. What would not be fine is
reproducing Gruene's own artwork or trading on their name, so the mark should
never appear alongside anything implying a connection to the venue.</p>
<p><strong>The motto and tagline are placeholders.</strong> "Real Songs, No
Apologies" and "No Pretty Boy Country" both came off the website copy and neither
has been through Brandon. They are optional in every mark here, unlike BAND.</p>
</section>

<section>
<div class="sechead">
<h2>To finish this</h2>
</div>
<ul>
<li>Which direction, and which of the two ways of mapping the name.</li>
<li>Whether hats are definitely happening, since that decides how hard the
embroidery constraint bites.</li>
<li>Whether he wants a monogram, a BH mark for sleeves, hat backs and a favicon.</li>
<li>Final files follow on the pick: layered SVG, transparent PNG at print
resolution, one colour and reversed versions, and a stitch ready simplification
if hats are going ahead.</li>
</ul>
</section>
</div>
"""

io.open('brandon-marks.html', 'w', encoding='utf-8', newline='\n').write(
    HEAD + BODY.replace('__DANCE__', dance)
               .replace('__MARQ__', marq)
               .replace('__WEST__', west)
               .replace('__ORN__', orn))
print('  brandon-marks.html written')
