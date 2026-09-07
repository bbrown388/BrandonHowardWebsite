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
| `marks/am-alamo.svg` | Marquee, the rebuilt ALAMO lettering. Poppins Black with a constructed arch A. |
| `marks/am-alamo-hat.svg` | Same, small format. |
| `marks/am-alamo-flat.svg` | Same, squared flat-top A instead of a softened shoulder. |
| `marks/am-archivo.svg` | Marquee, Archivo Expanded Black. Closest to the marquee photo. |
| `marks/am-archivo-hat.svg` | Same, small format. |
| `marks/am-jost.svg` | Marquee, Jost. Jost is an open Futura, and Futura Std Bold is what the Alamo brand manual actually specifies. |
| `marks/am-anton.svg` | Marquee, Anton. Best measurements of the set, least distinctive. |

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

| Threshold | Process | Meaning |
|---|---|---|
| 0.42 mm | Screen print, DTG | Below this, ink bridges or drops out. Every mark here is comfortable. |
| 1.10 mm | Embroidery | A stitch cannot render a finer stroke. This is what decides hats. |

The headline result: at hat size the Bodoni and Alex Brush mark loses 33 percent
of its ink to strokes too fine to stitch. The Alamo lettering is the strongest
distinctive option, losing nothing at all below the print threshold and clearing
embroidery in small format at 11.1 percent.

The longer name cost something real here. Before BAND was added, the Playfair and
Kaushan small format lockup cleared embroidery at 11.8 percent. A motto can be
dropped for a small placement; BAND cannot, and the extra fine ink pushed that
mark back to 13.6 percent. No dance hall version clears embroidery at four inches
any more. This is the same class of failure
already seen on Bob's BD mark, where fine strokes dropped out below about three
and a half inches on DTG.

So the intended shape is a small family rather than one file: the Bodoni mark for
tee fronts, posters and the website, and the Alamo mark wherever something has to
survive small. The Alamo lettering needs no split of its own, since it holds up at
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
