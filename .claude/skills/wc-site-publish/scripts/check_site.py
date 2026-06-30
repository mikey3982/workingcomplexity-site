#!/usr/bin/env python3
"""Consistency checker for the workingcomplexity.health static site.

Run from the repo root (or pass the root as the first argument):

    python3 .claude/skills/wc-site-publish/scripts/check_site.py

Exits non-zero if any check fails. Checks:

  1. Unified navigation — every page carries the same six nav links in the
     same order (Philosophy, Approach, Themes, About, Blog, Contact) and
     the "Get in touch" CTA.
  2. Mobile menu — every page has the .nav-toggle button and its script.
  3. Canonicals — every page has exactly one canonical tag, using the clean
     URL (no .html) that matches the file's path.
  4. Internal links and anchors — every internal href resolves to a file,
     and every #fragment resolves to an id in the target page.
  5. Post navigation — every post carries a .post-nav block, and prev/next
     links are reciprocal (if A says next is B, B must say prev is A).
"""
import glob
import os
import re
import sys

SITE = "https://workingcomplexity.health"
NAV_LABELS = ["Philosophy", "Approach", "Themes", "About", "Blog", "Contact"]
NAV_CTA = "Get in touch"

# Pages that are not posts (no post-nav expected)
NON_POSTS = {"index.html", "blog/index.html", "blog/heuristics/index.html"}


def site_files(root):
    files = ["index.html"]
    found = glob.glob(os.path.join(root, "blog", "**", "*.html"), recursive=True)
    files += sorted(os.path.relpath(f, root) for f in found)
    return [f for f in files if os.path.isfile(os.path.join(root, f))]


def read(root, f):
    with open(os.path.join(root, f), encoding="utf-8") as fh:
        return fh.read()


def expected_canonical(f):
    if f == "index.html":
        return SITE
    if f.endswith("/index.html"):
        return SITE + "/" + os.path.dirname(f) + "/"
    return SITE + "/" + f[: -len(".html")]


def check(root):
    errors = []
    files = site_files(root)
    srcs = {f: read(root, f) for f in files}
    ids = {f: set(re.findall(r'id="([^"]+)"', s)) for f, s in srcs.items()}

    # 1 + 2: nav and mobile menu
    for f, src in srcs.items():
        m = re.search(r'<ul class="(?:wc-)?nav-links">(.*?)</ul>', src, re.S)
        if not m:
            errors.append(f"{f}: no nav-links list found")
        else:
            labels = re.findall(r">([^<]+)</a>", m.group(1))
            if labels != NAV_LABELS:
                errors.append(f"{f}: nav links are {labels}, expected {NAV_LABELS}")
        c = re.search(r'class="(?:wc-)?nav-cta">([^<]*)<', src)
        cta_text = c.group(1).strip() if c else None
        if cta_text != NAV_CTA:
            errors.append(f"{f}: nav CTA is {cta_text!r}, expected {NAV_CTA!r}")
        if 'class="nav-toggle"' not in src:
            errors.append(f"{f}: missing mobile menu button (.nav-toggle)")
        if "nav.classList.toggle" not in src:
            errors.append(f"{f}: missing mobile menu toggle script")

    # 3: canonicals
    for f, src in srcs.items():
        canons = re.findall(r'<link rel="canonical" href="([^"]+)"', src)
        if len(canons) != 1:
            errors.append(f"{f}: expected exactly one canonical tag, found {len(canons)}")
        elif canons[0] != expected_canonical(f):
            errors.append(f"{f}: canonical {canons[0]} != expected {expected_canonical(f)}")

    # 4: internal links and anchors
    for f, src in srcs.items():
        base = os.path.dirname(f)
        for href in re.findall(r'href="([^"]+)"', src):
            if href.startswith(("mailto:", "data:", "javascript:")):
                continue
            if href.startswith("http"):
                if "workingcomplexity.health" not in href:
                    continue  # external link, not checked
                path = href.split("workingcomplexity.health", 1)[1]
            elif href.startswith("#"):
                # template literals in inline JS are not links
                if href == "#" or "${" in href:
                    continue
                if href[1:] not in ids[f]:
                    errors.append(f"{f}: dead same-page anchor {href}")
                continue
            else:
                path = href
            frag = ""
            if "#" in path:
                path, frag = path.split("#", 1)
            if path in ("", "/"):
                target = "index.html"
            elif path.endswith("/"):
                target = path.strip("/") + "/index.html"
            elif path.startswith("/"):
                p = path.lstrip("/")
                target = p if os.path.exists(os.path.join(root, p)) else p + ".html"
            else:
                p = os.path.normpath(os.path.join(base, path))
                target = p if os.path.exists(os.path.join(root, p)) else p + ".html"
            if not os.path.exists(os.path.join(root, target)):
                errors.append(f"{f}: broken link {href} -> {target}")
            elif frag and "${" not in frag and frag not in ids.get(target, set()):
                errors.append(f'{f}: dead anchor {href} (no id="{frag}" in {target})')

    # 5: post-nav presence and reciprocity
    def url_of(f):
        return "/" + f[: -len(".html")]

    posts = [f for f in files if f not in NON_POSTS]
    nav_of = {}
    for f in posts:
        src = srcs[f]
        if 'class="post-nav"' not in src:
            errors.append(f"{f}: missing post-nav block (prev/next/all-writing)")
            continue
        prev = re.search(r'class="post-nav-prev" href="([^"]+)"', src)
        nxt = re.search(r'class="post-nav-next" href="([^"]+)"', src)
        nav_of[url_of(f)] = (prev.group(1) if prev else None, nxt.group(1) if nxt else None)
    for url, (prev, nxt) in nav_of.items():
        if nxt and nxt in nav_of and nav_of[nxt][0] != url:
            errors.append(f"{url}: next points to {nxt}, but its prev is {nav_of[nxt][0]}")
        if prev and prev in nav_of and nav_of[prev][1] != url:
            errors.append(f"{url}: prev points to {prev}, but its next is {nav_of[prev][1]}")

    return errors, len(files)


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    errors, n = check(root)
    if errors:
        print(f"FAIL — {len(errors)} problem(s) across {n} pages:\n")
        print("\n".join("  " + e for e in errors))
        sys.exit(1)
    print(f"OK — {n} pages checked: nav, mobile menu, canonicals, links, post chain all consistent.")


if __name__ == "__main__":
    main()
