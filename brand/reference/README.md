# Drop supplied artwork here

Put a reference image in this folder and it can go straight into the mark:

    cd ../src
    python trace_png.py ../reference/arrow.png

That writes `arrow-traced.svg` beside it, as real vector paths, which the build
can consume the same way it consumes glyph outlines.

## Why it has to be traced rather than pasted

The marks are single flat fills. A raster cannot scale for print, cannot be
recoloured for a dark garment, and is not much use to an embroidery digitiser.
Tracing turns supplied artwork into the same kind of path data everything else
in the mark already is.

## What traces well

Clean black on white, as large as available. Anti-aliased edges are fine.
Anything with a drop shadow, a gradient or a photographic background will need
cleaning up first, since the tracer works off a single brightness threshold.

## The gotcha

`potracer` treats a True cell in its bitmap as BACKGROUND, not foreground, which
is the opposite of what the name suggests. Getting it backwards traces the page
rather than the artwork and returns a solid block with the drawing knocked out of
it. `trace_png.py` defaults to dark ink on a light ground; pass
`light_ink=True` for white-on-black source.

## Before using anything here on merch

Know where it came from. Anything sold needs a licence that covers commercial
use, and a good-looking image found online usually does not have one by default.
See `../ARROW-SOURCING.md`.
