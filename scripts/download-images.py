#!/usr/bin/env python3
"""Download images referenced in content from Wayback Machine.

Only needed if the S3 bucket (dentedreality-content.s3.amazonaws.com)
goes down. Check with:
    curl -sI "https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2002/09/14183934/8054783_d9734076e4_o.jpg"
"""

import re
import time
from pathlib import Path

import requests

CONTENT_DIR = Path("content/posts")
IMAGES_DIR = Path("static/images/uploads")
SESSION = requests.Session()


def find_image_urls():
    """Scan all markdown files for S3 image references."""
    urls = set()
    for md_file in CONTENT_DIR.rglob("index.md"):
        text = md_file.read_text()
        matches = re.findall(
            r"https?://dentedreality-content\.s3\.amazonaws\.com/([^\s\)\"]+)",
            text,
        )
        urls.update(matches)
    return urls


def download_image(path):
    """Download an image from the Wayback Machine."""
    wm_url = f"https://web.archive.org/web/2022/https://dentedreality-content.s3.amazonaws.com/{path}"
    out_path = IMAGES_DIR / path
    if out_path.exists():
        return True
    out_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        resp = SESSION.get(wm_url, timeout=30)
        resp.raise_for_status()
        out_path.write_bytes(resp.content)
        return True
    except Exception as e:
        print(f"  FAILED {path}: {e}")
        return False


def rewrite_urls():
    """Rewrite S3 URLs in markdown to local paths."""
    for md_file in CONTENT_DIR.rglob("index.md"):
        text = md_file.read_text()
        new_text = text.replace(
            "https://dentedreality-content.s3.amazonaws.com/",
            "/images/uploads/",
        )
        if new_text != text:
            md_file.write_text(new_text)


def main():
    urls = find_image_urls()
    print(f"Found {len(urls)} unique image URLs")

    success = 0
    for i, path in enumerate(sorted(urls)):
        print(f"  [{i+1}/{len(urls)}] {path}")
        if download_image(path):
            success += 1
        time.sleep(0.5)

    print(f"\nDownloaded {success}/{len(urls)} images")
    print("Rewriting URLs in markdown files...")
    rewrite_urls()
    print("Done.")


if __name__ == "__main__":
    main()
