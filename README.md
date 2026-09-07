# Brandon Howard — starter site

Single-page site for **Brandon Howard**, performing with his band **Howard County**.
Built 7 Sep 2026.

One file, `index.html`, plus `images/`. No build step, no framework. Edit, commit, and
GitHub Pages redeploys.

**Live preview:** https://bbrown388.github.io/BrandonHowardWebsite/

---

## This is a separation, not a rename

**Brandon has left Howard County.** He is the former lead singer. This site is his own
presence under his own name.

That distinction matters and an earlier draft of this file got it wrong. It argued for
keeping "Howard County" visible and secondary for search continuity, which is the right
advice for a *rename* — same act, new name. It is the wrong advice here, and possibly worse
than wrong: if the band name is entangled with the former management, leaning on it is a
problem rather than an asset.

**Every reference has been removed except one**, kept because it is a plain biographical
fact and it explains the connection to anyone who knew the band:

> He is the former lead singer of Howard County.

It sits in the About paragraph, deliberately not in the branding. **Delete that one line and
the name is gone entirely** — no other change needed.

---

## OPEN QUESTION: do these accounts belong to Brandon?

**This is the most important thing in this file after the booking contact.** The page links
to three external accounts and it is not clear he controls any of them:

| Link | Whose? |
|---|---|
| `facebook.com/HowardCountyMusic` | **The band's page.** He is the former lead singer, so this may not be his |
| `redironpush.bandcamp.com` | "Red Iron Push" — a label or collective, not his name |
| `open.spotify.com/artist/2fB4ElpylR4ujb0J3mnUvu` | Unverified. More than one artist shares the name |

**If he does not control them, they should come off the page.** Linking a former band's
Facebook from the site that exists to separate him from that band is the same failure as
putting the former manager's booking email on it. It sends his own fans somewhere he has no
say over.

They were left in place rather than deleted because **many artists keep the page and simply
rename it**, in which case the link is correct and removing it would lose his audience. One
answer from Brandon settles it.

The song list is a separate question. Those are songs he **wrote and sang**, so listing them
is factual whoever owns the masters. But if he wants to lead with new material instead, it is
a six-line edit.

---

## Design

Built in the **standard Texas country band convention**: full-bleed photo hero with a dark
scrim, condensed uppercase display type, dark ground, anchor nav, social row. That layout
is genre furniture, not any one band's invention — randyrogersband.com was the reference
for *structure and hierarchy* only.

**Nothing was copied.** No markup, no CSS, no images, no copy from any other band's site.
Palette, type scale and section design are original to this page.

| Token | Value | |
|---|---|---|
| `--ink` | `#0A0A0A` | ground |
| `--paper` | `#F2EADC` | display + body text |
| `--brass` | `#C89B4A` | accent |
| `--display` | Oswald | headings, condensed caps |

**One external dependency:** Oswald from Google Fonts, loaded in `<head>`. It is what makes
the display type work. Swap it for a self-hosted copy if that dependency is unwanted.

---

## Photos and videos

`photos-videos.html`, linked from the nav, plus a four-shot strip on the home page.

### Photos

**Twelve, chosen for range from a much larger iCloud library**, not everything Brandon has.
Extracted at full resolution and resized to 1600px, with a square 640px thumbnail each.

**To change the selection**, edit the `PHOTOS` array near the bottom of
`photos-videos.html`. Each entry needs `images/gallery/<name>.jpg` for the lightbox and
`<name>-t.jpg` for the grid. Removing an entry removes the tile. The home-page strip is
four hard-coded `<img>` tags in `index.html`, changed the same way.

The grid opens a keyboard-navigable lightbox using a native `<dialog>`, so arrow keys and
Escape work without a library.

### Videos

**Eight from `youtube.com/channel/UCzDMR8d3snpksXqSAm3SwYw`**, ordered to lead with the four
songs that also appear on the home page, then recent originals. Meme and joke posts were
skipped. Edit the `VIDEOS` array to change them.

**Loaded as click-to-play facades, not iframes.** Eight real embeds would pull YouTube's
player and its cookies on every page load; instead each tile shows a thumbnail and swaps in
a `youtube-nocookie.com` iframe only when clicked. Verified: **zero iframes present until
someone plays something.**

**Note the channel is still named "Howard County".** Another asset under the old brand.
Worth renaming as part of the same move, since the site now points at it.

---

## Photographs

**`images/hero.jpg` came from Bob**, via an iCloud link, and is the better-provenance image
of the two sources here. Sepia profile shot in a prairie field, flat-bill cap, bolo tie. It
was cropped out of the iCloud viewer at full resolution and resized to 1920px.

**`images/feature.jpg` was downloaded from howardcountymusic.com** and resized. It is a
photograph of Brandon, from a site about Brandon, **but the photographer's rights are unknown
and that site may be controlled by the former management.** Before this goes on a real domain,
Brandon should confirm he holds rights or supply a replacement. It is a file swap, nothing more.

**Randy Rogers Band images were not used and must never be.** They are another band's
copyrighted photographs of their own members. Using them, even as a placeholder, would be
both infringement and misrepresentation.

### Hero tuning, if the photo is ever replaced

Two settings are specific to this picture and will need revisiting:

- **The scrim** in `.hero::before` is tuned for a bright sepia image, mean luminance 208/255.
  Weight sits at the top, where cream nav crosses bright sky, and at the bottom for the fade
  into the page. The middle is deliberately light so the photograph reads.
- **`align-items: flex-end`** rather than centre. At this photo's aspect ratio the image fits
  the viewport height exactly, so `background-position` cannot move the subject, and centred
  type lands across his jaw. Dropping the block puts it over his chest and the field instead.

---

## Every fact on the page is sourced

Nothing was invented. Where a real value was unavailable it is marked `PLACEHOLDER` rather
than filled with a plausible guess, because this is a real person's public page and a wrong
detail is worse than a blank one.

| Fact | Source |
|---|---|
| Gospel, blues, country; Southwest Louisiana, Kansas, Colorado, North Texas | howardcountymusic.com |
| First song at 11, 300+ songs written | howardcountymusic.com |
| 2024 Future Faces of Texas Country, TRRMA | howardcountymusic.com |
| 2024 Champion, Texas State Songwriters Association | howardcountymusic.com |
| Tiny Town, Top 20 Texas Country Music Chart | search, corroborated |
| Girl I See You, Louisiana Growler, Cowboy Cry, Jolene | search |
| I Ain't Comfortable | redironpush.bandcamp.com |
| Facebook, /HowardCountyMusic | live page |

**The prose was written fresh from those facts, not pasted.** The copy on
howardcountymusic.com is someone else's work; lifting it would be both a copyright question
and the wrong voice for a site Brandon controls.

---

## What still needs filling in

### 1. Booking contact — the important one

**howardcountymusic.com is live right now** and its booking section reads:

```
Howard County, contact:
Neil Sparkman, Business Manager
214-869-7580
howardcounty@brokenroadtx.com
```

Per Bob's notes, **Broken Road Productions was formerly the label and management, and that
relationship ended.** So the site the public finds first still routes Brandon's bookings to a
former manager. That is very likely why this repo exists. **Populate the address from Brandon
directly and no other source.**

#### The form

There is a booking form and a visible email address, both currently pointing at
**`booking@brandonhowardmusic.com`, which does not exist yet.**

It posts to **FormSubmit**, chosen because the endpoint IS the address, so there is no account
to create and no dashboard to hand over. Swapping in the real address is **two edits in
`index.html`**: the `action` on `.booking-form`, and the `mailto:` in `.booking-direct`.

**FormSubmit will not deliver anything until the first submission is confirmed** from that
inbox. Send one test message and click the link they email back.

The form carries a hidden honeypot (`_honey`), a set subject line, and table-formatted
delivery. Fields are name, email, date, venue or city, and details.

**Deliberately not routed through GigSync**, or through anything else Bob owns. Bob's call,
and it is the same principle that keeps the former manager's address off this page: **Brandon's
booking should not depend on infrastructure another person controls.** A site built to get him
out of one dependency should not quietly create a new one. FormSubmit is a commodity that can
be swapped for any equivalent in two edits, and Brandon can take the whole thing elsewhere
without asking anyone.

Same reasoning applies to the merch link below, which is a temporary arrangement rather than
an architecture.

### 2. Merch store

`merch.html`, reached from the top nav rather than as a section on the home page.

**It is wired to Bob's Shopify store as a temporary stand-in**, so every item shown is Bob's
product and every sale is Bob's money. A visible notice on the page says so.

#### Switching to Brandon's store

**Two values at the top of `merch.html`. Nothing else on the page changes.**

```js
const SHOP_DOMAIN      = '6anqxb-rt.myshopify.com';
const STOREFRONT_TOKEN = '2a7e0382b6e5915658809f9549bb28a7';
```

Get the token from Shopify admin, **Settings → Apps and sales channels → Develop apps →
Configure Storefront API scopes**, with `unauthenticated_read_product_listings`. A Storefront
token is designed to be public and read-only; it is not a secret and is safe in client-side
source.

#### How it works, and what it deliberately does not do

Reads the catalogue over the Storefront API and renders a grid. Buying goes straight to a
**Shopify cart permalink**, `/cart/{variantId}:1`, which drops the item in the cart and lands
the visitor on Shopify's own checkout.

**There is no cart on this page, on purpose.** A borrowed storefront is not worth a
`localStorage` cart that would have to be migrated the day the store changes. When Brandon has
his own store this page keeps working unchanged, and anyone who wants a full cart can build
one then.

The catalogue request fires in `<head>` before the body parses, so it is in flight while the
browser is still building the DOM.

### 3. Shows

No dates were invented. Replace the placeholder with a list, or embed Bandsintown or
Songkick so it maintains itself.

### 4. Spotify link — unverified

`open.spotify.com/artist/2fB4ElpylR4ujb0J3mnUvu` came up in search as "Brandon Howard" but
**could not be confirmed as the right one**; Spotify serves a JavaScript shell to fetchers
and more than one artist shares that name. **Open it and check before this goes public.**

### 5. Analytics

None installed. Bob's Google Analytics tag was deliberately left off so Brandon's traffic is
not reported into Bob's property. Add Brandon's own if he wants one.

---

## The domain situation

Checked 7 Sep 2026.

| Domain | Registered | Expires | Nameservers | State |
|---|---|---|---|---|
| `howardcountymusic.com` | 2023-03-25 | 2027-03-25 | GoDaddy | **LIVE**, old brand, former-manager booking contact |
| `howardcountyband.com` | 2025-11-26 | **2026-11-26** | `radiopromoguy.com` | registered, **does not resolve** |
| `brandonhowardmusic.com` | — | **2027-01-16** | `radiopromoguy.com` | registered, **does not resolve** |

**The rebrand was already started and stalled.** Two domains were registered on the same
nameservers, belonging to a radio promotion company, and neither serves anything. Google
still has `howardcountyband.com` indexed under the title "Brandon Howard Music || Official
Website", which is the rebrand showing through.

Meanwhile the only site that actually loads is the old one, under the old brand, routing
bookings to the former manager.

**`brandonhowardmusic.com` is the right long-term home.** It matches the new brand exactly,
it is already registered, and it runs to January 2027. This site exists to fill it.

**Two dates somebody needs to be told:**

- **`howardcountyband.com` expires 26 November 2026** — about eleven weeks out.
- **`brandonhowardmusic.com` expires 16 January 2027.**

If Brandon does not control those registrations, that is the first thing to sort out, ahead
of any design work. A rebrand that depends on someone else's renewal is not a rebrand.

**Still available if a fresh start is easier:** `brandonhowardband.com`,
`brandonhowardtx.com`. (`brandonhoward.com` is taken by an unrelated party on GoDaddy
nameservers.)

---

## Deploying

### Now: the GitHub Pages URL

Settings → Pages → Source: **Deploy from a branch**, `main`, `/`. Already enabled.

Unlinked and unindexed — good enough for Brandon to review before anything points at it.

### Later: a custom domain

**There is deliberately no `CNAME` file yet.** Adding one makes GitHub Pages redirect the
`github.io` URL to the custom domain, so if DNS is not ready the site is unreachable at
*both* addresses. Create it only once DNS exists.

**For a bobdavismusic.com subdomain**, add at Cloudflare:

| Type | Name | Target | Proxy |
|---|---|---|---|
| CNAME | `howardcounty` | `bbrown388.github.io` | **DNS only** — grey cloud |

Then add a file named `CNAME` containing exactly `howardcounty.bobdavismusic.com`.

**A path like `bobdavismusic.com/howardcounty` is not possible from this repo.** GitHub
Pages serves one repository per hostname and the apex is already served by
`bbrown388/bobdavismusicwebsite`. A separate repo requires a subdomain.

**For `brandonhowardmusic.com`**, the preferred destination, use four `A` records at
GitHub's Pages IPs plus a `CNAME` file containing the apex domain. This requires control of
the registration, which currently sits on a third party's nameservers.

**SEO continuity when the domain changes.** Once the new domain is live, put a 301 redirect
from `howardcountymusic.com` to it so existing links and search history carry over. That
needs control of the old domain, which may not be available — another reason to establish
who holds what before committing to a destination.
