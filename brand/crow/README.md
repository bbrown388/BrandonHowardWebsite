# Crow

A realistic side profile, taken from a public domain Audubon study rather than
drawn from scratch.

## Source and licence

**John James Audubon, "English crow"** — Houghton Library MS Am 21 (72), via
Wikimedia Commons. **Public domain.** Free for commercial use including
merchandise, with no attribution required. Audubon died in 1851, so the work is
long out of copyright, and the Commons record carries a public domain tag rather
than a restrictive licence on the photograph of it.

The untouched plate is kept here as `source-plate.jpg` so the provenance travels
with the artwork, and `source.json` holds the Commons record.

## Files

| File | Use |
|---|---|
| `crow-realistic.png` | The painted bird, cut out on transparency. Keeps the blue-black sheen and every feather. For anything printed in full colour. |
| `crow-silhouette.svg` / `.png` | Solid single colour, dark ink. For the mark, single-colour print, and embroidery. |
| `crow-silhouette-white.svg` / `.png` | Same, in paper `#F2EADC`, for dark garments. |

## What was done to it

The original plate carries a second study of a head, a caption under it, and
inscriptions along the bottom. Those were removed row by row off the bird's own
left edge rather than with a rectangle, because the beak reaches further left at
the top than the breast does lower down, so any straight cut either clipped the
beak or left the caption.

Seven small strays survived that pass. They were removed by labelling connected
components on a reduced copy and keeping only the largest, which is the bird.
That took out 369 pixels, a tenth of a percent of the ink.

The cut-out uses a soft alpha ramp between paper and ink rather than a hard
threshold, so the painted edge stays intact instead of going jagged.

## Why this rather than a drawn one

Five hand-coded attempts at a crow failed, and were rejected twice as not looking
like a crow. Hand-placing polygon coordinates is a reasonable way to draw an
arrow and a poor way to draw an animal: every correction is a guess at a number
rather than a line you can see while pulling it. Starting from a real drawing
solved it in one pass, exactly as it did for the arrow.
