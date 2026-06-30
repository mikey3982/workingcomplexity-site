# workingcomplexity.health — site structural conventions

These are the conventions every page on the site follows. They were unified in
June 2026 after the site drifted into six different navigation variants; the
point of this document is that the drift never happens again. The checker
script (`scripts/check_site.py`) enforces the testable ones.

## Layout of the site

- Repo root **is** the deployed site. `index.html` is the home page.
- Posts live in `blog/`, the heuristics essay series in `blog/heuristics/`.
- Each page is fully self-contained: its own inline `<style>`, no build step,
  no shared CSS file. Consistency is by convention, not by tooling — which is
  why new pages are cloned from existing ones, never written from scratch.
- Netlify deploys automatically on push to `main` (GitHub
  `mikey3982/workingcomplexity-site`). Netlify serves clean URLs (`/blog/foo`
  for `blog/foo.html`) and strips `data-netlify` from the live form HTML —
  that is normal, not a bug.

## Navigation (identical on all pages)

Six links in this exact order, then the CTA. The `<ul>` class is
`nav-links` on the home page and blog index, `wc-nav-links` on article pages —
keep whichever the cloned page already uses; the CSS depends on it.

| Label      | href (home page) | href (all other pages) |
|------------|------------------|-------------------------|
| Philosophy | `#pillars`       | `/#pillars`             |
| Approach   | `#approach`      | `/#approach`            |
| Services   | `#services`      | `/#services`            |
| About      | `#about`         | `/#about`               |
| Blog       | `/blog/`         | `/blog/` (+ `class="active"`) |
| Contact    | `#contact`       | `/#contact`             |

CTA: `Start a Conversation`, href `#contact` (home) or `/#contact` (elsewhere),
class `nav-cta` / `wc-nav-cta` to match the page.

## Mobile menu

Every page carries three pieces (a cloned post already has all of them —
just don't delete them):

1. CSS block commented `── Mobile nav (hamburger) ──` inside the page styles.
2. `<button class="nav-toggle" …>` as the last child of `<nav>`.
3. The toggle `<script>` just before `</body>` (contains
   `nav.classList.toggle('nav-open')`).

## Head metadata

- Exactly one canonical tag, clean URL (never `.html`):
  `<link rel="canonical" href="https://workingcomplexity.health/blog/<slug>" />`
- `<title>Post title — Working Complexity</title>` — the part before the
  em dash is reused by neighbouring posts' prev/next labels.
- Internal links everywhere use clean URLs (`/blog/foo`, not `/blog/foo.html`).

## Article page anatomy (light "paper" pages)

In order: nav → `<header class="article-cover">` (doc code, kicker, title,
subtitle, meta with author/date/reading time) → article body →
`<nav class="post-nav">` → `<footer class="article-close">` (dark closing
statement block) → mobile menu script.

- **Doc code**: `WC-BLOG-NNN / SHOUTY TITLE / REV.A`. NNN is sequential —
  find the next number with `grep -rho 'WC-BLOG-[0-9]*' blog/ | sort -u`.
- **Reading time**: word count ÷ ~220, rounded; stated honestly.

## The post chain (prev/next)

Every post carries:

```html
<nav class="post-nav" aria-label="More writing">
    <a class="post-nav-prev" href="/blog/<prev>">&larr; <Prev title></a>
    <a class="post-nav-all" href="/blog/">All writing</a>
    <a class="post-nav-next" href="/blog/<next>"><Next title> &rarr;</a>
</nav>
```

The chain order mirrors the blog index listing (series first, then essays,
then The Cast last). Inserting a post means **three edits**: the new post's
prev/next, the previous neighbour's next, and the next neighbour's prev.
First post has no prev link; last has no next. The checker verifies
reciprocity, so a missed neighbour edit will fail the build check.

## Blog index (`blog/index.html`)

- Standalone essays get a `post-card`; series get a `post-featured` card with
  a parts list. Clone an existing card of the right kind.
- On series cards, part 01 in the parts list carries the gold
  `— start here` marker (`<em style="font-style:normal; color:#C4A46B; …">`).
- If the piece was listed under "Coming next", remove it from there.

## Home page touch-points

- New **series** → add a card in the Thinking section (`#blog`), cloned from
  the existing series cards, using the same description copy as the index.
- Standalone essays don't appear on the home page unless Mike asks.

## Voice (see BRAND.md §3 for the full system)

UK English. Sentence case everywhere, including labels and buttons. Em dashes
used to hold two ideas in relation. Never "simply", "leverage", "unlock",
"stakeholders". Personal/reflective pieces are first person singular and stay
in Mike's own hand — edit lightly.
