"""scrape_basic.py - fetch the title and meta description of a few public pages.

Usage:  python scrape_basic.py urls.txt page_facts.csv
Polite by design: checks robots.txt, identifies itself, waits between requests.
"""
import csv
import sys
import time
import urllib.request
import urllib.robotparser
from datetime import datetime, timezone
from html.parser import HTMLParser
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit

USER_AGENT = "GTM-Learning-Bot/0.1 (portfolio practice project)"
DELAY_SECONDS = 2
MAX_BYTES = 500_000
FIELDS = ["url", "status", "title", "description", "fetched_at", "note"]


class FactParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.title = ""
        self.description = ""

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.in_title = True
        elif tag == "meta":
            a = {k.lower(): (v or "") for k, v in attrs}
            if a.get("name", "").lower() == "description" and not self.description:
                self.description = a.get("content", "")

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data


def allowed_by_robots(url):
    """Return (allowed, reason). If robots.txt can't be read, do not fetch."""
    parts = urlsplit(url)
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(f"{parts.scheme}://{parts.netloc}/robots.txt")
    try:
        rp.read()
    except Exception:
        return False, "could not read robots.txt"
    if rp.can_fetch(USER_AGENT, url):
        return True, ""
    return False, "disallowed by robots.txt"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=10) as resp:
        raw = resp.read(MAX_BYTES)
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.status, raw.decode(charset, errors="replace")


def main(src, dst):
    with open(src, encoding="utf-8") as f:
        urls = [u.strip() for u in f if u.strip() and not u.startswith("#")]

    rows = []
    for i, url in enumerate(urls):
        row = dict.fromkeys(FIELDS, "")
        row["url"] = url
        ok, reason = allowed_by_robots(url)
        if not ok:
            row["note"] = f"skipped ({reason})"
        else:
            try:
                status, html = fetch(url)
                parser = FactParser()
                parser.feed(html)
                row["status"] = status
                row["title"] = " ".join(parser.title.split())
                row["description"] = " ".join(parser.description.split())
            except (HTTPError, URLError, TimeoutError, ValueError, OSError) as e:
                row["note"] = f"error: {e}"
            row["fetched_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
        rows.append(row)
        print(f"{url} -> {row['note'] or row['status']}")
        if i < len(urls) - 1:
            time.sleep(DELAY_SECONDS)

    with open(dst, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Done: {len(rows)} URLs, saved to {dst}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: python scrape_basic.py urls.txt page_facts.csv")
    main(sys.argv[1], sys.argv[2])