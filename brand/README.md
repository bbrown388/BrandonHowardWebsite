# Brandon Howard, merch marks

First pass at a logo for merch. Nothing here is approved yet. Open
`marks-sheet.html` in a browser to compare everything side by side on light and
dark garments with the measurements attached.

## The two directions

Bob named two references, so both are built.

**Dance hall** follows the Gruene Hall sign: a word arched across the top, a
large script beneath it carrying a swash, and a small letterspaced strap line
under that. BRANDON takes the GRUENE slot, Howard takes the Hall slot, and the
strap line carries his motto where Gruene carries "Texas' Oldest Dance Hall".

**Marquee** follows the Alamo Drafthouse marquee from the original photo: heavy
caps stacked tight, hairline rules above and below, tagline underneath.

On that sign the word ALAMO and the words DRAFTHOUSE CINEMA are set in two
different faces. DRAFTHOUSE CINEMA is plain Futura Std Bold, which the Alamo
brand manual names as its primary face. ALAMO is a custom logotype, confirmed by
the manual itself, so there is no font to buy. `am-alamo` rebuilds it.

## Files

| File | What it is |
|---|---|
| `marks/gh-bodoni.svg` | Dance hall, Bodoni Moda Black + Alex Brush. Closest to the Gruene reference. |
| `marks/gh-bodoni-tag.svg` | Same, strap line swapped for the tagline. |
| `marks/gh-bodoni-hat.svg` | Same, strap line removed for small placements. |
| `marks/gh-playfair.svg` | Dance hall, Playfair Display Black + Kaushan Script. Heavier script. |
| `marks/gh-playfair-hat.svg` | Same, small format. The only dance hall mark that clears embroidery. |
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

The headline result: at hat size the Bodoni and Alex Brush mark loses 31 percent
of its ink to strokes too fine to stitch, while the Playfair and Kaushan small
format lockup loses 12 percent and clears. The Alamo lettering is the strongest
distinctive option in the set, losing nothing at all below the print threshold
and clearing embroidery outright in small format at 10.6 percent. This is the same class of failure
already seen on Bob's BD mark, where fine strokes dropped out below about three
and a half inches on DTG.

So the intended shape is a small family rather than one file. In the dance hall
direction that means the Bodoni mark for tee fronts, posters and the website with
the Playfair small format lockup for hats and pockets. The Alamo lettering needs
no such split, since it holds up at both sizes on its own.

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

- Which direction, and which strap line. Both current options came off the
  website copy and neither has been through him.
- Whether he wants a monogram, a BH mark for sleeves, hat backs and a favicon.
- Final files follow the pick: transparent PNG at print resolution, one colour
  and reversed versions, and a stitch ready simplification if hats go ahead.
