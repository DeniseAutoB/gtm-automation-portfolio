"""clean_leads.py - clean a messy lead CSV.

Usage:  python clean_leads.py messy_leads.csv cleaned_leads.csv
"""
import csv
import re
import sys
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+\-]+@[A-Za-z0-9\-]+(\.[A-Za-z0-9\-]+)*\.[A-Za-z]{2,}$")
TRACKING_KEYS = {"fbclid", "gclid", "mc_cid", "mc_eid"}
REQUIRED = ["first_name", "email", "company"]
OUT_FIELDS = ["first_name", "last_name", "email", "company", "website", "flags"]


def squash(text):
    """Trim the ends and collapse repeated spaces."""
    return re.sub(r"\s+", " ", text or "").strip()


def fix_case(text):
    """Title-case a value only if it is ALL CAPS or all lowercase."""
    text = squash(text)
    if text and (text.isupper() or text.islower()):
        return " ".join(
            "-".join(p.capitalize() for p in w.split("-")) for w in text.split(" ")
        )
    return text


def clean_url(raw):
    """Add https://, drop www., strip tracking parameters and trailing slash."""
    raw = squash(raw)
    if not raw:
        return ""
    if "://" not in raw:
        raw = "https://" + raw
    parts = urlsplit(raw)
    host = parts.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    keep = [
        (k, v)
        for k, v in parse_qsl(parts.query)
        if not k.lower().startswith("utm_") and k.lower() not in TRACKING_KEYS
    ]
    return urlunsplit(
        (parts.scheme.lower(), host, parts.path.rstrip("/"), urlencode(keep), "")
    )


def main(src, dst):
    with open(src, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    stats = {
        "rows_in": len(rows),
        "duplicates_removed": 0,
        "invalid_email": 0,
        "rows_missing_fields": 0,
        "urls_changed": 0,
    }
    seen, cleaned = set(), []

    for raw in rows:
        row = {(k or "").strip().lower().replace(" ", "_"): v for k, v in raw.items()}
        rec = {
            "first_name": fix_case(row.get("first_name")),
            "last_name": fix_case(row.get("last_name")),
            "email": squash(row.get("email")).lower(),
            "company": fix_case(row.get("company")),
            "website": clean_url(row.get("website")),
        }

        if rec["email"] and rec["email"] in seen:
            stats["duplicates_removed"] += 1
            continue
        if rec["email"]:
            seen.add(rec["email"])

        flags = [f"missing_{k}" for k in REQUIRED if not rec[k]]
        if rec["email"] and not EMAIL_RE.match(rec["email"]):
            flags.append("invalid_email")
            stats["invalid_email"] += 1
        if any(f.startswith("missing_") for f in flags):
            stats["rows_missing_fields"] += 1
        if rec["website"] != squash(row.get("website")):
            stats["urls_changed"] += 1

        rec["flags"] = ";".join(flags)
        cleaned.append(rec)

    with open(dst, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=OUT_FIELDS)
        writer.writeheader()
        writer.writerows(cleaned)

    flagged = sum(1 for r in cleaned if r["flags"])
    report = (
        f"Rows in: {stats['rows_in']}\n"
        f"Rows out: {len(cleaned)}\n"
        f"Duplicates removed (by email): {stats['duplicates_removed']}\n"
        f"Invalid emails flagged: {stats['invalid_email']}\n"
        f"Rows missing a required field: {stats['rows_missing_fields']}\n"
        f"Websites tidied: {stats['urls_changed']}\n"
        f"Rows with any flag: {flagged}\n"
    )
    print(report)
    with open(dst.replace(".csv", "_report.txt"), "w", encoding="utf-8") as f:
        f.write(report)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: python clean_leads.py input.csv output.csv")
    main(sys.argv[1], sys.argv[2])