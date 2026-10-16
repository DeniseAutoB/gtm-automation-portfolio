# GTM Automation Portfolio

I spent 8+ years in Accounting and Finance Operations (A/R, A/P, Payroll, Month-end Close) and I'm moving into GTM Engineering. This repo is a sprint of hands-on builds in outbound systems: Prospecting, Deliverability, Cold Email, Automation, and the Data Work underneath them.

**Everything here ran on fake, sample, or public data. Nothing was sent to a real prospect.** Each build has its own README that says what I made, what broke, and what I'd improve.

🌐 Site: [gtm-engineer-portfolio.replit.app](https://gtm-engineer-portfolio.replit.app) · 💼 [LinkedIn](https://www.linkedin.com/in/deniseb7)

## Sprint Scorecard
Planned as 7 days, finished in about 10 (Oct 6 to Oct 16, 2026). The extra time went on proving the email test through my own domain, and on moving that domain between mail providers (see Day 4).

| Day | Build | Result | Folder |
|---|---|---|---|
| 1 | Prospect list in Clay | 38 companies → 14 contacts → 10 verified emails, with openers I fact-checked against each company's site | [clay](clay/) |
| 2 | Email Deliverability | SPF, DKIM, and DMARC set up on a separate sending domain: all three pass in Gmail's headers, mail-tester 10/10 | [deliverability](deliverability/) |
| 3 | Cold Email Sequences | Two 3-email variants, each with a hypothesis, plus a test plan and its sample-size limits | [campaigns](campaigns/) |
| 4 | Campaigns in Instantly | Both variants built; Variant A test-sent to three inboxes I own. SPF, DKIM, DMARC pass, all three messages reached my inbox Primary tab, the one-click unsubscribe headers are present, and the unsubscribe link works | [campaigns](campaigns/) |
| 5 | n8n Workflows | A lead becomes a HubSpot contact tagged Clay; a reply triggers a Slack alert. Both tested with fake payloads | [n8n-workflows](n8n-workflows/) |
| 6 | Python Tools | A lead CSV cleaner and a scraper that checks robots.txt first, on fake and public practice data | [scripts](scripts/) |
| Extra | Daily Streak Tracker (n8n) | Checked this repo each night, calculated a streak with one rest day a week, logged it to a sheet, and posted to Slack. [Ran during the sprint; stopped when the n8n trial ended] | [n8n-workflows](n8n-workflows/) |

## The Builds

### 1. Clay prospect list
A verified list for a practice offer (bookkeeping cleanup for small US marketing agencies). I filtered, enriched, and verified every stage, and cut the list down instead of keeping weak rows. AI-written openers were checked by hand against each company's own site, because the facts changed between runs. → [clay/](clay/)

### 2. Deliverability Setup
A practice sending domain with a mailbox, MX, SPF, DKIM, and DMARC, tested in Gmail's "Show original" and on mail-tester. DMARC reports go to a parser, a suggestion from a LinkedIn commenter that I acted on. → [deliverability/](deliverability/)

### 3. Cold Email Sequences
Two variants for the same offer, one built on visibility ("clear numbers") and one on agency-specific pain. Rules: plain text, one soft ask, an opt-out line, and no claimed results. The test plan says what I'd measure (positive replies, not opens) and why ten contacts is too few to call a winner. → [campaigns/](campaigns/)

### 4. Instantly Campaigns and a real self-test
Both variants built as campaigns, then Variant A sent to three inboxes I own through a Google Workspace mailbox on my practice domain. Confirmed: authentication passes, all three messages reached my inbox (not spam), the one-click unsubscribe headers are present, and the unsubscribe link works. Not confirmed: placement for recipients other than me, since a brand-new domain has no sending history with their filters. → [campaigns/](campaigns/)

### 5. n8n Workflows
Two webhook-driven workflows: Lead → HubSpot Contact (matched on email, Lead source = Clay), and reply → Slack alert. Both were unpublished after testing, because the webhooks have no authentication. → [n8n-workflows/](n8n-workflows/)

### 6. Python Tools
`clean_leads.py` tidies and flags a lead file and reports what it changed. `scrape_basic.py` fetches a page's title and description, skips anything it can't read or isn't allowed to fetch, and prints the reason for each skip. → [scripts/](scripts/)

## How I work
- **A README for every build.** Each one covers the problem, what I made, what broke, the limits, and what I'd improve.
- **I label what I tested.** Sample data is called sample data, and a test is called a test. Three sends to my own inbox are documented as exactly that.
- **I check the details before trusting a result.** That caught stray quotation marks in an import, a one-letter webhook typo, and a verified email on the wrong domain.
- **I fact-check AI output.** The AI-written openers changed between runs, so I verified each one against the company's own site before keeping it.
- **I write down what I didn't prove.** Every README has a "Not confirmed" or "Limits" section.
- **Using AI.** I used Claude as a coach and pair programmer: it helped me plan the sprint and draft code and copy. I ran, tested, debugged, and documented everything myself, and I decided what to keep. I didn't use Claude Code for these builds.

## Limits
- No real prospects, clients, or campaigns. Results describe tests, not performance
- Sample sizes are far too small to prove which email variant works better
- The webhooks have no authentication, and the scripts have no retries or proxies. Those are deliberate gaps for practice tools
- Several tools ran on free trials that have ended or will end
- Inbox placement was confirmed only for my own addresses. A first send from a new domain to strangers could land differently, so no placement claim beyond that

## What I'm looking for
An entry-level or junior role in GTM engineering or RevOps, remote. I bring finance-grade accuracy, process discipline, and a habit of documenting what I build.
