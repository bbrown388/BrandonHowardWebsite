# The Brandon Howard Band, merch marks

First pass at a logo for merch. Nothing here is approved yet. Open
`marks-sheet.html` in a browser to compare everything side by side on light and
dark garments with the measurements attached.

## The two directions

Bob named two references, so both are built.

**Dance hall** follows the Gruene Hall sign: a word arched across the top, a
large script beneath it carrying a swash, and a small letterspaced strap line
under that. BRANDON takes the GRUENE slot, Howard takes the Hall slot, THE sits
above the arch, and BAND takes the strap line position where Gruene carries
"Texas' Oldest Dance Hall". The whole name then reads straight down the mark.

`gh-bodoni-tag` maps the name the other way, and is actually the closer parallel:
Gruene arches the identifying word and puts the type word in script, so that
variant arches BRANDON HOWARD and lets Band carry the script.

**Marquee** follows the Alamo Drafthouse marquee from the original photo: heavy
caps stacked tight, hairline rules above and below, tagline underneath. THE and
BAND are set into breaks in those rules rather than given lines of their own,
which keeps BRANDON and HOWARD as the only full height lines instead of turning
the mark into a four deck stack.

On that sign the word ALAMO and the words DRAFTHOUSE CINEMA are set in two
different faces. DRAFTHOUSE CINEMA is plain Futura Std Bold, which the Alamo
brand manual names as its primary face. ALAMO is a custom logotype, confirmed by
the manual itself, so there is no font to buy. `am-alamo` rebuilds it.

## Files

| File | What it is |
|---|---|
| `marks/gh-bodoni.svg` | Dance hall, Bodoni Moda Black + Alex Brush. Closest to the Gruene reference. |
| `marks/gh-bodoni-tag.svg` | Dance hall, the other mapping: BRANDON HOWARD arched over Band in script. |
| `marks/gh-bodoni-hat.svg` | Same, strap line removed for small placements. |
| `marks/gh-playfair.svg` | Dance hall, Playfair Display Black + Kaushan Script. Heavier script. |
| `marks/gh-playfair-hat.svg` | Same, small format. Strongest of the dance hall set. |
| `marks/gh-rye.svg` | Dance hall, Rye + Great Vibes. Reads more saloon. |
| `marks/am-slab.svg` | Marquee, Alfa Slab One. Heavy Americana slab. |
| `marks/am-slab-ultra.svg` | Marquee, Ultra. Same idea, heavier and quirkier. |
| `marks/am-oswald.svg` | Marquee, Oswald Bold. Condensed gothic, and his existing website face. |
| `marks/am-stencil.svg` | Marquee, Black Ops One. Stencil. |
| `marks/am-varsity.svg` | Marquee, Graduate. Collegiate varsity slab. |
| `marks/am-alamo.svg` | Marquee, the rebuilt ALAMO lettering. Kept for comparison; Brandon turned the face down. |

### Western

Iterating on Rye. Its problem was never the character, it is that the spurs are
hairlines, so it loses 46 percent of its ink at hat size. These hold the flavour
while carrying more weight.

| File | What it is | Embroidery, hat |
|---|---|---|
| `marks/am-rye.svg` | Rye. Spurred western slab, the original. | 42.9% |
| `marks/am-sancreek.svg` | Sancreek. Same western language, more ink in the stems. | **14.3%** |
| `marks/am-swanky.svg` | Fontdiner Swanky. Flared spurs, more swagger. | 20.0% |
| `marks/am-bevan.svg` | Bevan. Heavy Egyptian slab. | 26.8% |
| `marks/am-rammetto.svg` | Rammetto One. Poster weight, softened corners. | 15.8% |

Nothing in the western group clears the 12 percent embroidery threshold, and that
is the direction rather than the face choice: spurs, serif brackets and thin
horizontals are what make lettering read western, and they are exactly what a
stitch cannot hold. Sancreek is the best available compromise and turns Rye's 46
percent into 14.

Bevan is worth a note because it contradicts the obvious guess. It looks like the
robust one, since it has no spurs at all, and it measures worst at full size.

### Arrows and crows

The A in Sancreek already reads a little like an arrow. The first attempt leaned
on that directly, adding mirrored barbs at the apex to make the existing spur
look deliberate, and it did not work. The apex of these faces is a fine point
sitting well above the widest part of the letter, so anything positioned off the
letter box lands in mid air and reads as a detached shape hovering over the A.
Making it work means editing the glyph outline itself, adding barbs as real
nodes and rebalancing the apex around them. That is a type designer in a vector
editor, and worth commissioning if the idea is wanted badly enough.

So the arrows went into the structure of the mark instead of into the letters.

| File | What it is | Embroidery, hat |
|---|---|---|
| `marks/am-sancreek-arrows.svg` | **Chosen.** The rules become arrows pointing out from the centre. | 15.7% |
| `marks/am-sancreek-crow.svg` | A crow perched on the top rule. | 9.3% |
| `marks/am-rye-arrows-crow.svg` | Both devices, on Rye. | 17.8% |
| `marks/am-sancreek-crossed.svg` | Crossed arrows under the mark. | 6.5% |

`src/ornament.py` draws all of it: arrowheads, arrows, crossed arrows and the
crow, as flat single colour paths sized off one dimension.

**The measurements in this group are misleading and the sheet says so.** The
metric is a share of total ink, so a solid crow or a pair of heavy arrows raises
the denominator and the percentage falls without any hairline getting thicker.
Rye alone measures 45.7 percent too fine; Rye with arrows and a crow measures 9.6
percent, and nothing about the letters changed. Judge letterforms by the face
numbers in the western table.

Standalone devices are in `marks/device-arrow.svg`,
`marks/device-crossed-arrows.svg` and `marks/device-crow.svg`, usable on their
own for a sleeve, a hat back or a setlist stamp.

The arrows took three goes, the last against the arrows in the band's own
circular badge. Those draw the feather as individual barbs radiating off the
shaft, so the shaft stays visible through the fletching, and that is the detail
that decides it. A filled vane closes into a solid paddle however elegantly it is
shaped, because the two halves meet across the shaft; both earlier attempts
failed that way, once as a leaf and once as a spade. The shipping arrow has a
barbed head with its base cut back between the barbs, and a seven-barb feather
whose barb length follows a profile peaking about a third along.

`src/arrowtest.py` and `src/arrowtest2.py` hold the ten constructions compared
side by side at two sizes, so the next change here is a comparison rather than a
guess.

**The crow is not finished, and should not ship as it stands.** Five redraws
against a supplied reference and it still reads closer to a grackle. The method
is the problem rather than the proportions: hand coding polygon coordinates is a
fine way to draw an arrow and a poor way to draw an animal, because each
correction is a guess at a number rather than a line you can see while pulling
it. The realistic options are to license a vector crow (the Alamy reference costs
tens of dollars and settles the rights question at once), to commission one if
the bird is going to carry the brand, or to keep iterating with falling returns.

The arrow mark stands on its own without a bird, which is why it is the pick.

Every marquee mark has a `-hat` small format twin with the tagline removed.

Each SVG is a single flat fill, so recolouring is one attribute and a reversed
version needs no separate file.

## Why these are outlines, not text

The SVGs carry real glyph outlines as `<path>` data rather than `<text>`
elements. A printer or an embroidery digitiser can open them without having the
fonts installed, and there is no chance of a silent substitution changing the
letterforms between here and the garment. Shaping ran through HarfBuzz so the
script faces keep their proper kerning.

The swash under the script word is drawn, not set. No font ships that gesture,
and it is the thing that makes the layout read as a dance hall sign rather than
an underline.

## The rebuilt Alamo A

Poppins Black is the base because it matches the reference on the two things
that can actually be measured off the artwork: stem width to cap height, 0.314
against roughly 0.31, and an O with an aspect ratio of 1.001, meaning a true
circle. Every other candidate was further off on one or both.

What Poppins does not have is the A. The Alamo A has no pointed apex. It is a
half round arch on two vertical legs with a low crossbar, essentially an `n`
with a bar through it. `src/archa.py` constructs that letter from the base
font's own stem width and cap height and writes it back into the `glyf` table,
so shaping, kerning and every existing code path keep working with no special
cases.

How much of that arch to take is a dial, because copying it outright is the most
recognisable thing about their lettering. The `arch` argument runs from 1.0, the
literal semicircle, down to 0.0, a squared flat top.

| Value | Result | Shipped as |
|---|---|---|
| 1.00 | The literal Alamo semicircle | not used |
| **0.35** | **Flat top with softened shoulders** | **`AlamoLike-Black.ttf`, the default** |
| 0.00 | Squared flat top, least derivative of the set | `AlamoLike-Flat.ttf`, the alternate |

0.35 is the shipping default. It keeps a flat-topped geometric A that reads as
deliberate and sits properly next to the circular O, without reproducing their
letter.

His name needs only that one substitution. The other oddities on the sign are
the angled foot on the L and the arch built M, and neither letter appears in
BRANDON HOWARD.

Typeface designs are not copyrightable in the United States, and this is a
letter drawn from geometry rather than a copy of anyone's outline. Their logo as
a whole is protected, which is why none of the marquee housing, the badge shape
or their name appears anywhere here.

## The measurements

`src/strokes.json` holds a measured, not estimated, figure for every mark: the
share of its ink sitting in strokes too fine for a given process, taken at four
inches wide at 300 dpi. The method is a morphological opening, which removes
exactly the ink thinner than a given width.

**These figures were re-measured after a harness bug, and roughly two thirds of
them moved.** Every mark used to be rendered onto one very tall page and captured
in a single screenshot. Chrome caps a full page capture at about 16384 pixels and
the stitch below that seam is wrong, so every mark past it was measured against
whatever artwork landed in its slot. The results looked plausible, which is why it
went unnoticed for several rounds, and in the worst case it reversed a conclusion:
Bevan was reported as the weakest western face at 51.6 percent and actually
measures 15.1.

`src/measure_pages.py` now splits the marks across chunks well under the cap and
stamps each tile with its key. `src/measure_run.py` verifies that stamp before
trusting a tile, refuses to run if a chunk screenshot is not the expected height,
and masks ink on all three colour channels so the stamp itself is never counted.

| Threshold | Process | Meaning |
|---|---|---|
| 0.42 mm | Screen print, DTG | Below this, ink bridges or drops out. Every mark here is comfortable. |
| 1.10 mm | Embroidery | A stitch cannot render a finer stroke. This is what decides hats. |

The headline result: Oswald Bold measures best of everything at 11.0 percent full
size and 6.5 on a hat. The chosen mark, Sancreek with arrow rules, is 12.7 percent
full size and 8.9 on a hat, which clears embroidery. Rye is print only at 47
percent, which is the face rather than the western direction, since Sancreek,
Bevan and Rammetto all clear in small format. No dance hall version clears.

The longer name cost something real here. Before BAND was added, the Playfair and
Kaushan small format lockup cleared embroidery at 11.8 percent. A motto can be
dropped for a small placement; BAND cannot, and the extra fine ink pushed that
mark back to 13.6 percent. No dance hall version clears embroidery at four inches
any more. This is the same class of failure
already seen on Bob's BD mark, where fine strokes dropped out below about three
and a half inches on DTG.

Brandon turned down the face on the Alamo mark, so the marquee layout was kept
and the typeface treated as the variable. Five new directions were tried, each
moving away from geometric in a different way rather than five shades of one
idea, all normalised to a common cap height so a condensed gothic could be
compared fairly against a fat slab.

Oswald Bold came out well ahead on measurement, at 6.9 percent full size and 2.4
percent on a hat where nothing else gets under 10, and it is already the display
face on his website. Alfa Slab One is the strongest answer to the actual
objection and still clears embroidery small at 10.2 percent. Rye is the most
Texan and is print only, losing 46 percent of its ink at hat size to hairline
spurs.

So the intended shape is a small family rather than one file: the Bodoni mark for
tee fronts, posters and the website, and whichever marquee face he picks wherever
something has to survive small. The Alamo lettering needs no split of its own, since it holds up at
both sizes.

Hats need a decision either way. Three ways out: run the mark larger, since many
hat fronts take four and a half to five inches; put the Alamo mark on hats and the
dance hall mark on shirts; or have BAND redrawn heavier for the stitched version
only.

## Licensing

All faces are SIL Open Font License 1.1, which permits merchandise sold for
money with no fee and no attribution on the product. That was a deliberate
choice over the actual Alamo faces, which are commercial licences that would
have to be bought. `AlamoLike-Black.ttf` is a derivative of Poppins and inherits
the same licence, which the OFL expressly permits provided it is not sold on its
own as a font. Poppins declares no Reserved Font Name, so renaming was not
strictly required; it was renamed anyway so it cannot collide with a real
Poppins install. Notices are in `fonts/LICENSES.md` and must stay with the
font files.

## The Gruene resemblance

What is borrowed is a layout convention, an arched word over a script over a
strap line, which is common to dozens of Texas dance halls and roadhouses and is
not something anyone owns. The typefaces are different, the swash is drawn from
scratch rather than traced, and the words are his.

What would not be fine is reproducing Gruene's own artwork or trading on their
name. The mark should never appear alongside anything implying a connection to
the venue.

## Rebuilding

```
cd src
python archa.py     # builds AlamoLike-Black.ttf, the arch-A derivative
python build.py     # regenerates every SVG into ../marks
python sheet.py     # builds the option cards
python shell.py     # assembles marks-sheet.html
```

`build.py` needs `fontTools` and `uharfbuzz`. Arc radius, tracking, script size
and strap line are all parameters on the `dancehall()` and `marquee()` calls, so
tuning does not mean touching the geometry code in `logolib.py`.

## Open questions for Brandon

- Which direction, and which of the two ways of mapping the name.
- Whether hats are definitely happening, since that decides how hard the
  embroidery constraint bites.
- The motto and tagline are placeholders. Both came off the website copy and
  neither has been through him. They are optional in every mark, unlike BAND.
- Whether he wants a monogram, a BH mark for sleeves, hat backs and a favicon.
- Final files follow the pick: transparent PNG at print resolution, one colour
  and reversed versions, and a stitch ready simplification if hats go ahead.
