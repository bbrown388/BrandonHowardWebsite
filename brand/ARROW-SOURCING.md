# Sourcing an arrow: what is actually free, and what is actually good

Searched for an open-licence arrow rather than drawing another one. Short answer:
the genuinely free libraries do not have one that suits this mark, and the reason
is worth writing down so nobody repeats the search.

## What was checked, with licences verified

| Source | Licence | Result |
|---|---|---|
| [Openclipart](https://openclipart.org) | Public domain, confirmed on each item page | 82 arrow clips found, 36 downloaded and reviewed |
| [Public Domain Vectors](https://publicdomainvectors.org) | CC0, no attribution | 840 arrows catalogued, 41 decorative-looking ones checked |
| [Wikimedia Commons](https://commons.wikimedia.org) | Mixed; PD and CC0 items identified via API metadata | Almost entirely heraldry, flags and map markers |
| Bundled OFL fonts | SIL OFL, already cleared for merch | 16 of the 40 carry a U+2192 arrow glyph |
| SVG Repo | Mixed CC0 / MIT | Blocked automated access, HTTP 429 |

## Why none of it works

**The clipart libraries are clipart.** The CC0 arrow inventory is cartoon
bow-and-arrow scenes, cupids, archery targets, and gradient-filled 3D arrows.
The handful of clean ones are line art: `fill="none" stroke="#000"`, fourteen
points, a hollow outline. Dropping one of those next to Sancreek would look more
like clip art, not less, which is the opposite of the brief.

**The font arrows are the wrong proportion.** Sixteen bundled faces have a proper
typographic arrow, professionally drawn and already licensed. They are also
inline text arrows: short shaft, chunky head, built to sit inside a sentence. The
mark needs a long thin rule spanning a wordmark. Right quality, wrong shape.

**One hazard worth naming.** A Commons search for "crossed arrows" returns
emblems of the Arrow Cross Party, the Hungarian fascist movement. Several are
public domain and would pass any licence filter cleanly. Do not let an automated
asset search near this without looking at what it returns.

## Where the good ones actually are

[The Noun Project](https://thenounproject.com) is the right place. Thousands of
properly drawn boho, tribal and archery arrows, in the exact long-shaft
proportion this mark wants.

- Free tier is CC BY: usable commercially but requires crediting the creator.
  Awkward on a garment, though crediting on the website would satisfy it.
- Paid is a few dollars for a single icon, or roughly forty a year, and drops the
  attribution requirement. **For merch, take the paid tier**, so there is no
  credit obligation attached to a shirt.

Creative Market and Envato Elements also sell arrow and ornament packs with
extended licences that cover merchandise, usually ten to twenty dollars.

## Recommendation

The drawn arrow currently in the mark is competitive with everything free that
was found, and unlike any of it, it is weight-matched to Sancreek and sized for
the rule it sits in. Keep it unless Brandon wants something with more character.

If he does, buy one from the Noun Project. Any downloaded SVG drops straight into
the build: `logolib` already consumes path data, so an outline arrow becomes a
one-line swap in `ornament.ARROW_STYLE`. The only requirement is that it be a
**filled** silhouette rather than a stroked outline, since the mark is single
colour and there is no stroke-to-path step in the pipeline.
