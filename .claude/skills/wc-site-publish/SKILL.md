---
name: wc-site-publish
description: Publishes new material to the workingcomplexity.health website with guaranteed structural consistency — nav, mobile menu, canonical URLs, blog index card, and the prev/next post chain. Use this skill whenever Mike wants to add, upload, publish, or post anything to the site — a new essay, blog post, series, or page — or asks to update, fix, or check the website, even if he just says "put this on the site", "add this to the blog", or shares a draft and mentions the site. Also use it before any commit that touches index.html or blog/, to run the consistency check.
---

# Publishing to workingcomplexity.health

The site is hand-built static HTML — every page self-contained, consistency
held by convention rather than tooling. In mid-2026 the site had drifted into
six different navigation variants, dead anchors, and posts that dead-ended.
This skill exists so that never happens again: new material is cloned from
pages that are already correct, woven into the post chain, and verified by a
checker before anything is committed.

## Before anything else

1. Read `BRAND.md` at the repo root (§3 Voice especially). Non-negotiable for
   any WC output.
2. Read `references/conventions.md` in this skill — the structural rules for
   nav, canonicals, the post chain, doc codes, and index cards.

## Workflow for a new post

**1. Understand the material.** Is it a standalone essay, a new part of an
existing series, or a new series? Ask Mike if genuinely unclear — placement
decides the chain position, the index card type, and whether the home page
changes. Personal/reflective drafts are in Mike's own voice: edit lightly,
never overwrite his hand with a house register.

**2. Clone, don't create.** Copy an existing article page as the scaffold —
`blog/the-pull-of-complexity.html` is a good canonical example of the light
article shell. Cloning is the consistency mechanism: the nav, mobile menu,
fonts, and closing block come along already correct. Then replace only the
content: `<title>`, canonical (clean URL, no `.html`), doc code (next
`WC-BLOG-NNN`), kicker, title, subtitle, meta (author / date / honest reading
time), body, and the closing statement.

**3. Weave it into the site.** This is the step that was historically missed,
so treat it as part of "writing the post", not an extra:
   - **Post chain** — set the new post's prev/next and update *both
     neighbours* (three files change, not one). Chain order mirrors the blog
     index listing.
   - **Blog index** — add a card (`post-card` for essays, `post-featured`
     with parts list and `— start here` marker for series); remove the piece
     from "Coming next" if it was teased there.
   - **Home page** — only for a new series: add a Thinking-section card.

**4. Verify.** From the repo root:

```bash
python3 .claude/skills/wc-site-publish/scripts/check_site.py
```

It must report OK. It checks unified nav, mobile menu presence, canonical
correctness, every internal link and anchor, and prev/next reciprocity — a
missed neighbour edit or a stale canonical fails loudly. Fix and re-run; never
hand-wave a failure.

Then preview in a real browser: the `wc-blog` server in `.claude/launch.json`
(plain `python3 -m http.server`, so use the `.html` path locally — clean URLs
only work on Netlify). Check the new page at mobile width too: hamburger
opens, nothing overflows horizontally.

**5. Ship only when asked.** Commit with a `WC-SITE:` prefixed message. Push
to `main` deploys to production via Netlify automatically — so don't push
until Mike says to publish. After pushing, confirm the new URL is live.

## Editing existing pages

Same discipline, smaller scope: make the edit, run the checker, preview if the
change is visual. If an edit renames or removes a page, the checker's link
scan will surface every page that pointed at it.

## Just checking the site

If Mike asks whether the site is consistent (or before any commit touching
`index.html` or `blog/`), run the checker and report what it says — it is
cheap and exact.
