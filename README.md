# Howard County — starter site

A single-page starter site for **Brandon Howard / Howard County**, built 7 Sep 2026.

One file, `index.html`. No build step, no dependencies, no framework. Edit it in any
text editor, commit, and GitHub Pages redeploys.

---

## Read this before editing

**Every fact on the page is sourced. Nothing was invented.** Where a real value was not
available it is marked `PLACEHOLDER` in the HTML rather than filled with a plausible guess,
because this is a real person's public page and a wrong detail is worse than a blank one.

### What is on the page and where it came from

| Fact | Source |
|---|---|
| Gospel, blues, country; Southwest Louisiana, Kansas, Colorado, North Texas | howardcountymusic.com |
| First song at 11, 300+ songs written | howardcountymusic.com |
| 2024 Future Faces of Texas Country, TRRMA | howardcountymusic.com |
| 2024 Champion, Texas State Songwriters Association | howardcountymusic.com |
| Tiny Town, Top 20 Texas Country Music Chart | search results, corroborated |
| Girl I See You, Louisiana Growler, Cowboy Cry, Jolene | search results |
| I Ain't Comfortable | Bandcamp, redironpush.bandcamp.com |
| Facebook, /HowardCountyMusic | live page |

**The copy was written fresh from those facts, not pasted.** The prose on
howardcountymusic.com is someone else's work and lifting it would be both a copyright
question and the wrong voice for a site Brandon controls.

### What still needs filling in

1. **BOOKING CONTACT.** Blank on purpose. See the next section.
2. **SHOWS.** No dates were invented. Add real ones or drop in a Bandsintown widget.
3. **Spotify link.** `open.spotify.com/artist/2fB4ElpylR4ujb0J3mnUvu` came up in search as
   "Brandon Howard" but **could not be confirmed as the right one** — Spotify serves a
   JavaScript shell to fetchers and there is more than one artist by that name. **Open it
   and check before this goes anywhere public.**
4. **Photography.** The design carries without images deliberately, since none were
   available. A hero photo would improve it.
5. **Analytics.** None installed. Bob's Google Analytics tag was deliberately left off, so
   Brandon's traffic is not reported into Bob's property. Add Brandon's own if he wants one.

---

## Why the booking contact is blank

**howardcountymusic.com is live right now**, registered March 2023, and its booking
section reads:

```
Howard County, contact:
Neil Sparkman
Business Manager
214-869-7580
howardcounty@brokenroadtx.com
```

Per Bob's own notes, **Broken Road Productions was formerly Howard County's label and
management, and that relationship ended.** So the site the public finds first is still
routing Brandon's bookings to a former manager.

That is very likely the reason this repo exists. It is also why the booking field here was
left empty rather than copied across: **the entire point of a new site is that the contact
on it is Brandon's own.** Filling it from the old site would rebuild the problem.

**Do not populate that field from any source except Brandon directly.**

---

## The domain situation

Worth knowing before deciding where this lives.

| Domain | Registered | Expires | Nameservers | State |
|---|---|---|---|---|
| `howardcountymusic.com` | 2023-03-25 | 2027-03-25 | GoDaddy | **live**, old site, former-manager contact |
| `howardcountyband.com` | **2025-11-26** | **2026-11-26** | `radiopromoguy.com` | **registered but not resolving** |

`howardcountyband.com` is indexed by search engines under the title "Brandon Howard Music ||
Official Website" but its DNS does not resolve. It was registered in November 2025 and
**expires 26 November 2026, about eleven weeks out.**

The reading: somebody already tried to move Brandon onto a new domain and it never landed.

**If Brandon owns `howardcountyband.com`, that is the right long-term home for this site**,
not a subdomain of anyone else's domain. A working artist's booking contact, business cards
and socials should point at a domain he controls. The subdomain below is a good staging
address and a fine temporary home; it is not where this should end up.

**Whoever controls that domain should also be told it expires 26 Nov 2026.**

---

## Deploying

### Now: the free GitHub Pages URL

Settings → Pages → Source: **Deploy from a branch**, branch `main`, folder `/`.

Serves at:

```
https://bbrown388.github.io/BrandonHowardWebsite/
```

Unlinked and unindexed. Good enough for Brandon to review before anything points at it.

### Later: a real domain

**There is deliberately no `CNAME` file in this repo yet.** Adding one makes GitHub Pages
redirect the `github.io` URL to the custom domain, so if DNS is not ready the site becomes
unreachable at *both* addresses. Create it only when DNS is in place.

**For a bobdavismusic.com subdomain**, add this DNS record at Cloudflare:

| Type | Name | Target | Proxy |
|---|---|---|---|
| CNAME | `howardcounty` | `bbrown388.github.io` | **DNS only** — grey cloud, not orange |

Then add a file named `CNAME` to this repo containing exactly:

```
howardcounty.bobdavismusic.com
```

**Note:** a path such as `bobdavismusic.com/howardcounty` is *not* possible from this repo.
GitHub Pages serves one repository per hostname, and the apex `bobdavismusic.com` is already
served by `bbrown388/bobdavismusicwebsite`. A path would mean putting these files inside
Bob's repo. A separate repo requires a subdomain. That is what settled the question.

**For `howardcountyband.com`**, the same but with the apex: four `A` records at GitHub's
Pages IPs plus a `CNAME` file containing the domain.

---

## Editing

Everything is in `index.html`. The palette sits in `:root` at the top:

```css
--ground:   #101410;   /* pine dark */
--bone:     #ECE4D4;   /* text */
--copper:   #C2703F;   /* accent */
```

**It is deliberately not bobdavismusic.com's gold-on-black.** Brandon is his own artist and
should not read as a sub-brand of Bob's. Light mode is included and inverts the same tokens.
