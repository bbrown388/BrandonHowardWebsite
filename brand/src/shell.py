# -*- coding: utf-8 -*-
import io
dance, marq = io.open('sheet_body.html', encoding='utf-8').read().split('\x00')

HEAD = """<title>Brandon Howard Marks</title>
<style>
/* Palette is lifted from Brandon's site tokens so this sits inside the identity
   that already exists: ink, paper, brass. Neutrals are warmed toward the brass
   rather than left as flat grey. The page face is deliberately the plain system
   stack: ten logotypes are the subject here, and any characterful page type
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
<h1>Brandon Howard</h1>
<p class="lead">Six candidate marks in two directions, each shown on a light and a
dark garment, then tested at the size that actually breaks logos: a four inch hat
front.</p>

<div class="callout">
<p><strong>Two directions, because you named two references.</strong> The first was
the Alamo Drafthouse marquee, which is heavy squared caps. The second was the
Gruene Hall sign, which is a different animal: a word arched across the top, a
big script underneath carrying a swash, and a small letterspaced strap line below
that. Both are built here so you can see them side by side.</p>
</div>

<section>
<div class="sechead">
<h2>Direction one, dance hall</h2>
<h3 style="font-size:22px;margin-top:4px">BRANDON arched, Howard in script</h3>
<p>The Gruene layout you described, with BRANDON where GRUENE sits and Howard
where Hall sits. The strap line at the bottom is where Gruene puts its own
"Texas' Oldest Dance Hall" line, so it is carrying his motto instead.</p>
</div>
__DANCE__
</section>

<section>
<div class="sechead">
<h2>Direction two, marquee</h2>
<h3 style="font-size:22px;margin-top:4px">Stacked caps in a ruled panel</h3>
<p>The original Alamo Drafthouse reference. Heavy caps, wide tracking, hairline
rules above and below, tagline underneath.</p>
</div>
__MARQ__
</section>

<section>
<div class="sechead">
<h2>What the numbers mean</h2>
</div>
<p>Every mark was rendered at exactly four inches wide at 300 dpi and measured for
how much of its ink sits in strokes too fine for a given process. A morphological
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
<li><strong>Bodoni + Alex Brush</strong> as the primary. It is the one that
actually looks like the reference you sent, and it is the right mark for tee
fronts, posters, backdrops and the website.</li>
<li><strong>Playfair + Kaushan, small format</strong> for hats and pockets. Same
layout and the same idea, built to survive stitching. It is the only dance hall
option that clears the embroidery threshold.</li>
<li>The marquee direction is the fallback if Brandon wants something blunter.
<strong>Archivo Expanded</strong> is the closest to your original photo.</li>
</ul>
</section>

<section>
<div class="sechead">
<h2>Licensing and two cautions</h2>
</div>
<p><strong>Fonts are clear.</strong> Every face here is under the SIL Open Font
License: Bodoni Moda, Alex Brush, Playfair Display, Kaushan Script, Rye, Great
Vibes, Archivo, Jost and Anton. That licence permits commercial use including
merchandise sold for money, with no fee and no attribution needed on the product.
This was chosen deliberately over the actual Alamo faces, which are commercial
licences he would have to buy.</p>
<p><strong>On the Gruene resemblance.</strong> What is borrowed is a layout
convention, an arched word over a script over a strap line, which is common to
dozens of Texas dance halls and roadhouses and is not something anyone owns. The
typefaces are different, the swash is drawn from scratch rather than traced, and
the words are his. That is the line to stay on. What would not be fine is
reproducing Gruene's own artwork or trading on their name, so the mark should
never appear alongside anything implying a connection to the venue.</p>
<p><strong>The strap line is a placeholder.</strong> It currently reads "Real
Songs, No Apologies" with a tagline alternate. Both came off the website copy and
neither has been through Brandon.</p>
</section>

<section>
<div class="sechead">
<h2>To finish this</h2>
</div>
<ul>
<li>Which direction, and which strap line.</li>
<li>Whether he wants a monogram, a BH mark for sleeves, hat backs and a favicon.</li>
<li>Final files follow on the pick: layered SVG, transparent PNG at print
resolution, one colour and reversed versions, and a stitch ready simplification
if hats are going ahead.</li>
</ul>
</section>
</div>
"""

io.open('brandon-marks.html', 'w', encoding='utf-8', newline='\n').write(
    HEAD + BODY.replace('__DANCE__', dance).replace('__MARQ__', marq))
print('  brandon-marks.html written')
