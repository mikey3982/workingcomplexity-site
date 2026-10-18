---
name: wc-site-publish
description: Publishes new material to the workingcomplexity.health website with guaranteed structural consistency — nav, mobile menu, canonical URLs, blog index card, and the prev/next post chain. Use this skill whenever Mike wants to add, upload, publish, or post anything to the site — a new essay, blog post, series, or page — or asks to update, fix, or check the website, even if he just says "put this on the site", "add this to the blog", or shares a draft and mentions the site. Also use it before any commit that touches index.html, blog/ or briefings/, to run the consistency check.
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
correctness, every internal link and anchor, and prev/next reciprocity across
the home page, `blog/` and `briefings/`, plus the links on standalone root
pages — a missed neighbour edit or a stale canonical fails loudly. Fix and
re-run; never hand-wave a failure.

Then preview in a real browser. Serve the repo root with
`python3 -m http.server 8000` and open the `.html` path (clean URLs only work
on Netlify). Check the new page at desktop width and at 390px: the hamburger
opens, nothing overflows horizontally. In a cloud session, Chromium and
Playwright are pre-installed — take screenshots at both widths and look at
them rather than assuming the layout holds.

**5. Ship through a preview.** Commit with a `WC-SITE:` prefixed message on
a branch, not `main` — a push to `main` deploys to production straight away.
Push the branch and open a pull request when Mike asks; Netlify posts a deploy
preview link on the PR (see `references/conventions.md`). Send Mike that link
so he can check the page as it will look live. Merge only when he says to
publish, then confirm the clean URL is live on workingcomplexity.health.

If Mike explicitly asks to push straight to `main`, do that — but run the
checker first.

## Editing existing pages

Same discipline, smaller scope: make the edit, run the checker, preview if the
change is visual. If an edit renames or removes a page, the checker's link
scan will surface every page that pointed at it.

## Just checking the site

If Mike asks whether the site is consistent (or before any commit touching
`index.html`, `blog/` or `briefings/`), run the checker and report what it
says — it is cheap and exact.
