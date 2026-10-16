# Scripts: Lead CSV Cleaner and a Polite Page Scraper

**Outcome:** Two small Python tools for outbound data work: one cleans a messy lead file, the other fetches public page facts while respecting robots.txt. Both use only Python's standard library and ran on fake or public practice data.

**How I built them:** I wrote them with Claude's help in chat, then ran, tested, and debugged them myself on Windows. I didn't use Claude Code for these.

## 1. `clean_leads.py`
**Problem:** Lead files arrive with extra spaces, shouting capitals, tracking junk in URLs, duplicate rows, and malformed emails.

**What it does**
- Trims whitespace and fixes ALL CAPS or all-lowercase names and companies (mixed case is left alone, so
  names like McDonald aren't damaged)
- Strips `utm_` and click-ID parameters, `www.`, and trailing slashes from websites
- Removes duplicates by email
- Flags rows with an invalid email format or a missing first name, email, or company, and keeps them in the
   output with a `flags` column
- Writes a report of what changed

**Run**
```
python clean_leads.py messy_leads.csv cleaned_leads.csv
```

**Result on my sample (7 rows, all invented)**
```
Rows in: 7
Rows out: 6
Duplicates removed (by email): 1
Invalid emails flagged: 1
Rows missing a required field: 2
Websites tidied: 6
Rows with any flag: 3
```

## 2. `scrape_basic.py`
**Problem:** A one-line fact about a company (a page title or description) can feed a personalized opener,
  but scraping should be polite.

**What it does**
- Checks each site's robots.txt first, and skips any page it can't read or isn't allowed to fetch
- Identifies itself with a clear user agent, waits 2 seconds between requests, and caps the download size
- Saves the status, page title, meta description, and a timestamp to a CSV, with a note explaining any skip

**Run**
```
python scrape_basic.py urls.txt page_facts.csv
```

**Result:** Two practice sites built for scraping demos returned `200` with their titles. My own portfolio
site was skipped, because the script received a robots.txt response that blocked it, and I did not work around it.

## What broke
- **A name-lookup failure.** Two test sites were skipped with `getaddrinfo failed`. My first version hid the cause, so I changed it to print the exact reason. `nslookup` showed the shared Wi-Fi's DNS server answering that `example.com` didn't exist, while Cloudflare's public resolver (`1.1.1.1`) returned its addresses. Because I was on someone else's network, I didn't change their DNS settings. I switched to practice sites that resolved, and I didn't re-test the example.com sites afterward.
- **An indentation error** from editing one line in Notepad. I replaced the whole function instead of
    patching it.
- **Python wasn't installed.** `py` wasn't recognized, and I installed Python with "Add to PATH" ticked.

## Limits
- The cleaner flags a bad email only by its format, and doesn't check that the mailbox exists. Verification is a separate step (I used a verifier in the Clay build)
- It de-duplicates on exact email match, and it doesn't catch the same person with two addresses
- The scraper reads only the HTML a server returns, so pages that build their content with JavaScript can come back with empty fields
- It fetches one page per site, with no retries, no proxies, and no following of links. That's deliberate for a practice tool
- Both ran on fake or public data only

## What I'd improve
- Add a `--dry-run` option and a summary of which rows changed and why
- Fuzzy-match company names to catch near-duplicates
- Feed the scraper's description column into the opener step of my Clay table, with a human fact-check before use
- Add tests for the edge cases (empty file, odd encodings, blank headers)
