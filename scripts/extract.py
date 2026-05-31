#!/usr/bin/env python3
"""
Extract dentedreality.com.au content from the Wayback Machine
and output Hugo-compatible markdown files.

Usage:
    python3 scripts/extract.py                    # full run
    python3 scripts/extract.py --limit 50         # test with 50 posts
    python3 scripts/extract.py --resume            # resume from last position
    python3 scripts/extract.py --pages-only        # extract static pages only
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from urllib.parse import unquote

import yaml

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

DOMAIN = "dentedreality.com.au"
CDX_API = "https://web.archive.org/cdx/search/cdx"
WM_BASE = "https://web.archive.org/web"
CONTENT_DIR = Path("content/posts")
PAGES_DIR = Path("content")
IMAGES_DIR = Path("static/images/uploads")
STATE_FILE = Path("scripts/.extract-state.json")
RATE_LIMIT = 1.0  # seconds between requests

SESSION = requests.Session()
SESSION.headers.update({
    "User-Agent": "DentedReality-Archive-Rebuild/1.0 (personal site restoration)"
})


def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"completed": [], "failed": [], "last_index": 0}


def save_state(state):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2))


def fetch_post_urls():
    """Get all unique post URLs from the CDX API."""
    print("Fetching post index from CDX API...")
    params = {
        "url": f"{DOMAIN}/*",
        "output": "json",
        "fl": "timestamp,original,statuscode,mimetype",
        "filter": ["statuscode:200", "mimetype:text/html"],
        "collapse": "urlkey",
    }
    resp = SESSION.get(CDX_API, params=params, timeout=120)
    resp.raise_for_status()
    data = resp.json()

    posts = []
    for row in data[1:]:  # skip header
        timestamp, url, status, mime = row
        path = re.sub(r"https?://(www\.)?dentedreality\.com\.au(:80)?", "", url)

        # Skip junk URLs
        if any(c in path for c in ["&&", "==", "!=", "style.", "offsetWidth"]):
            continue
        if len(path) > 150:
            continue
        # Skip query-string variants and amp pages
        if "?" in path or "/amp/" in path or path.endswith("/amp"):
            continue
        # Match post URLs: /YYYY/MM/DD/slug/
        if re.match(r"/\d{4}/\d{2}/\d{2}/[^/]+/?$", path):
            posts.append({"timestamp": timestamp, "url": url, "path": path})

    print(f"Found {len(posts)} posts")
    return posts


def fetch_page_urls():
    """Get static page URLs from the CDX API using targeted queries."""
    print("Fetching page index from CDX API...")
    page_paths = [
        "about/", "about/business/", "about/hire-me/",
        "about/philosophy/", "about/site/", "about/standards/",
        "about/technical-documentation/", "about/gravatar-wall/",
        "projects/", "explore/", "contact/", "copyright/",
    ]

    pages = []
    for page_path in page_paths:
        params = {
            "url": f"{DOMAIN}/{page_path}",
            "output": "json",
            "fl": "timestamp,original,statuscode",
            "filter": "statuscode:200",
            "limit": "1",
            "sort": "closest",
            "from": "20220101",
        }
        try:
            resp = SESSION.get(CDX_API, params=params, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            if len(data) > 1:
                row = data[1]
                pages.append({
                    "timestamp": row[0],
                    "url": row[1],
                    "path": f"/{page_path}",
                })
        except requests.RequestException:
            print(f"  WARN: could not find /{page_path}")

    print(f"Found {len(pages)} static pages")
    return pages


def download_page(timestamp, url):
    """Download a page from the Wayback Machine."""
    wm_url = f"{WM_BASE}/{timestamp}id_/{url}"
    try:
        resp = SESSION.get(wm_url, timeout=30)
        resp.raise_for_status()
        return resp.text
    except requests.RequestException:
        # Fallback: try without id_ modifier (needs strip_wayback later)
        wm_url = f"{WM_BASE}/{timestamp}/{url}"
        try:
            resp = SESSION.get(wm_url, timeout=30)
            resp.raise_for_status()
            return resp.text
        except requests.RequestException as e:
            print(f"  FAILED: {e}")
            return None


def strip_wayback(html):
    """Remove Wayback Machine injected code from HTML."""
    # Remove WM toolbar
    html = re.sub(
        r"<!-- BEGIN WAYBACK TOOLBAR INSERT -->.*?<!-- END WAYBACK TOOLBAR INSERT -->",
        "", html, flags=re.DOTALL,
    )
    # Remove WM scripts
    html = re.sub(
        r'<script[^>]*src="[^"]*archive\.org[^"]*"[^>]*></script>',
        "", html,
    )
    html = re.sub(
        r"<script[^>]*>.*?__wm\..*?</script>", "", html, flags=re.DOTALL
    )
    # Remove WM CSS
    html = re.sub(
        r'<link[^>]*href="[^"]*archive\.org[^"]*"[^>]*/?>', "", html
    )
    # Clean WM URL rewrites
    html = re.sub(
        r"https?://web\.archive\.org/web/\d+(?:im_|if_|js_|cs_)?/", "", html
    )
    return html


def clean_url(url):
    """Remove Wayback Machine URL wrapping."""
    url = re.sub(r"https?://web\.archive\.org/web/\d+(?:im_|if_|js_|cs_)?/", "", url)
    return url


def parse_post(html, path):
    """Parse a post's HTML and extract structured content."""
    html = strip_wayback(html)
    soup = BeautifulSoup(html, "html.parser")

    article = soup.find("article")
    if not article:
        return None

    post_div = article.find("div", class_=re.compile(r"^post-\d+"))
    if not post_div:
        post_div = article

    result = {"path": path}

    # Post format
    article_class = article.get("class", [])
    article_cls = " ".join(article_class) if isinstance(article_class, list) else article_class
    format_match = re.search(r"\bf-(\w+)", article_cls)
    result["format"] = format_match.group(1) if format_match else "standard"

    # Service (keyring)
    post_classes = " ".join(post_div.get("class", []))
    service_match = re.search(r"keyring_services-(\w+)", post_classes)
    result["service"] = service_match.group(1) if service_match else ""

    # Categories
    cats = re.findall(r"category-([\w-]+)", post_classes)
    result["categories"] = [c for c in cats if c != "uncategorized"]

    # Title
    title_el = article.find(class_="entry-title")
    if title_el:
        title_a = title_el.find("a")
        result["title"] = title_a.get_text(strip=True) if title_a else title_el.get_text(strip=True)
        if title_a:
            result["external_url"] = clean_url(title_a.get("href", ""))
    else:
        result["title"] = ""

    # For non-link posts, external_url should not be set to the post's own URL
    if result["format"] != "link":
        own_url = f"https://dentedreality.com.au{path}"
        if result.get("external_url", "").rstrip("/") == own_url.rstrip("/"):
            result["external_url"] = ""
        own_url_http = f"http://dentedreality.com.au{path}"
        if result.get("external_url", "").rstrip("/") == own_url_http.rstrip("/"):
            result["external_url"] = ""

    # Date from URL path
    date_match = re.match(r"/(\d{4})/(\d{2})/(\d{2})/", path)
    if date_match:
        y, m, d = date_match.groups()
        result["date"] = f"{y}-{m}-{d}"

    # Try to get precise time from entry-meta
    meta = article.find(class_="entry-meta")
    if meta:
        permalink = meta.find(attrs={"data-datetime": True})
        if permalink:
            result["date"] = permalink["data-datetime"]

    # Tags
    tags_el = article.find(class_="tags")
    if tags_el:
        result["tags"] = [a.get_text(strip=True) for a in tags_el.find_all("a")]
    else:
        result["tags"] = []

    # Geo coordinates (check-ins)
    geo = article.find(class_="geo")
    if geo:
        lat = geo.find(class_="latitude")
        lon = geo.find(class_="longitude")
        if lat and lon:
            result["latitude"] = lat.get_text(strip=True)
            result["longitude"] = lon.get_text(strip=True)

    # Link URL (for link-format posts)
    link_url_el = article.find(class_="post-format-link-url")
    if link_url_el:
        link_a = link_url_el.find("a")
        if link_a:
            result["external_url"] = clean_url(link_a.get("href", ""))

    # Content
    content_el = article.find(class_="entry-content")
    if content_el:
        # Remove sharing widgets
        for el in content_el.find_all(class_="sharedaddy"):
            el.decompose()
        for el in content_el.find_all(class_="jp-relatedposts"):
            el.decompose()

        # Clean image URLs
        for img in content_el.find_all("img"):
            src = img.get("src", "")
            if src:
                img["src"] = clean_url(src)
            # Handle lazy-loaded images
            lazy_src = img.get("data-lazy-src", "")
            if lazy_src and "is-pending-load" not in lazy_src:
                img["src"] = clean_url(lazy_src)
            # Remove srcset with data URIs
            if img.get("srcset", "").startswith("data:"):
                del img["srcset"]

        # Convert to markdown
        content_html = str(content_el)
        result["content"] = md(content_html, heading_style="ATX", strip=["script", "style"])
    else:
        result["content"] = ""

    # Image URL for photo posts
    img_el = article.find(class_="keyring-img")
    if img_el:
        result["image"] = clean_url(img_el.get("src", ""))

    return result


def post_to_markdown(post):
    """Convert parsed post data to Hugo markdown with frontmatter."""
    fm = {
        "title": post["title"],
        "date": post["date"],
    }

    if post.get("format") and post["format"] != "standard":
        fm["format"] = post["format"]
    if post.get("service"):
        fm["service"] = post["service"]
    if post.get("tags"):
        fm["tags"] = post["tags"]
    if post.get("categories"):
        fm["categories"] = post["categories"]
    if post.get("external_url"):
        fm["external_url"] = post["external_url"]
    if post.get("latitude"):
        fm["latitude"] = post["latitude"]
        fm["longitude"] = post.get("longitude", "")
    if post.get("image"):
        fm["image"] = post["image"]

    frontmatter = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
    content = post.get("content", "").strip()
    return f"---\n{frontmatter}---\n\n{content}"


def save_post(post, base_dir):
    """Save a parsed post as a Hugo markdown file."""
    # Determine output path from URL path
    # /2023/01/15/management-debt/ -> content/posts/2023/01/15/management-debt/index.md
    slug = post["path"].strip("/").split("/")[-1]
    date_parts = post["path"].strip("/").split("/")[:3]
    if len(date_parts) == 3:
        out_dir = base_dir / "/".join(date_parts) / slug
    else:
        out_dir = base_dir / slug

    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "index.md"

    markdown = post_to_markdown(post)
    out_file.write_text(markdown, encoding="utf-8")
    return out_file


def main():
    parser = argparse.ArgumentParser(description="Extract dentedreality.com.au from Wayback Machine")
    parser.add_argument("--limit", type=int, help="Limit number of posts to extract")
    parser.add_argument("--resume", action="store_true", help="Resume from last position")
    parser.add_argument("--pages-only", action="store_true", help="Extract static pages only")
    parser.add_argument("--delay", type=float, default=RATE_LIMIT, help="Delay between requests (seconds)")
    args = parser.parse_args()

    state = load_state() if args.resume else {"completed": [], "failed": [], "last_index": 0}
    completed_set = set(state["completed"])

    if args.pages_only:
        pages = fetch_page_urls()
        for page in pages:
            path = page["path"]
            if path in completed_set:
                print(f"  SKIP (done): {path}")
                continue
            print(f"Downloading page: {path}")
            html = download_page(page["timestamp"], page["url"])
            if html:
                parsed = parse_post(html, path)
                if parsed:
                    # Save to content/<path>/index.md
                    slug = path.strip("/").replace("/", "-") or "home"
                    out_dir = PAGES_DIR / path.strip("/")
                    out_dir.mkdir(parents=True, exist_ok=True)
                    out_file = out_dir / "_index.md"
                    markdown = post_to_markdown(parsed)
                    out_file.write_text(markdown, encoding="utf-8")
                    print(f"  Saved: {out_file}")
            time.sleep(args.delay)
        return

    posts = fetch_post_urls()
    start_idx = state["last_index"] if args.resume else 0
    limit = args.limit or len(posts)
    end_idx = min(start_idx + limit, len(posts))

    print(f"Processing posts {start_idx + 1} to {end_idx} of {len(posts)}")
    print(f"Rate limit: {args.delay}s between requests")
    print()

    CONTENT_DIR.mkdir(parents=True, exist_ok=True)

    for i in range(start_idx, end_idx):
        post = posts[i]
        path = post["path"]

        if path in completed_set:
            print(f"  [{i+1}/{end_idx}] SKIP (done): {path}")
            continue

        print(f"  [{i+1}/{end_idx}] {path}")

        html = download_page(post["timestamp"], post["url"])
        if not html:
            state["failed"].append(path)
            state["last_index"] = i + 1
            save_state(state)
            time.sleep(args.delay)
            continue

        parsed = parse_post(html, path)
        if not parsed:
            print(f"    WARN: Could not parse article from {path}")
            state["failed"].append(path)
            state["last_index"] = i + 1
            save_state(state)
            time.sleep(args.delay)
            continue

        out_file = save_post(parsed, CONTENT_DIR)
        print(f"    -> {out_file}")

        state["completed"].append(path)
        completed_set.add(path)
        state["last_index"] = i + 1

        # Save state every 50 posts
        if (i + 1) % 50 == 0:
            save_state(state)
            print(f"    [checkpoint saved at {i + 1}]")

        time.sleep(args.delay)

    save_state(state)
    print()
    print(f"Done. {len(state['completed'])} completed, {len(state['failed'])} failed.")
    if state["failed"]:
        print(f"Failed URLs saved to state file: {STATE_FILE}")


if __name__ == "__main__":
    main()
