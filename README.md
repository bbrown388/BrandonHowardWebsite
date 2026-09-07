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

## Photographs — read this

`images/hero.jpg`, `feature.jpg` and `about.jpg` were **downloaded from
howardcountymusic.com** and resized for web. They are photographs of Brandon, from a site
about Brandon.

**But the photographer's rights are unknown, and that site may be controlled by the former
management.** Before this goes on a real domain, Brandon should either confirm he holds
rights to these images or supply his own. Swapping them is a file replacement, nothing more.

**Randy Rogers Band images were not used and must never be.** They are another band's
copyrighted photographs of their own members. Using them, even as a placeholder, would be
both infringement and misrepresentation.

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

Per Bob's notes, **Broken Road Productions was formerly Howard County's label and
management, and that relationship ended.** So the site the public finds first still routes
Brandon's bookings to a former manager.

That is very likely why this repo exists, and it is why the booking field here is empty
rather than copied across. **The entire point of a new site is that the contact on it is
Brandon's own.** Populate it from Brandon directly and no other source.

### 2. Merch link

Currently points at **`bobdavismusic.com/merch.html`** per Bob's instruction.

**That store does not carry Howard County products.** Until it does, the button sends
Brandon's fans to buy Bob's merch, which does not serve Brandon. Two ways to resolve:

- **Add Howard County products** to the Bob Davis store. Needs an arrangement about who
  collects, what split, who fulfils and who handles returns — revenue would land in Bob
  Davis Music LLC.
- **Or hide the section** until there is something to sell. One line to comment out.

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
