# Prospect List: Bookkeeping Cleanup for Agencies

**Outcome:** 38 US marketing agencies narrowed to 10 contactable prospects with verified emails and fact-checked openers.

## The problem
Outbound lists fail on data quality: wrong countries, companies that aren't a fit, contacts with no decision-making power, and unverified emails. I built a small list and cleaned it at every stage, so each row left is one I would actually email.

## Brief
- **Offer:** Done-for-you bookkeeping cleanup and monthly close for small agencies
- **Ideal customer:** US digital marketing agencies, 11-50 employees
- **Target roles:** Founder/Owner, COO, Head of Finance or Operations
- **Trigger signals:** Hiring for a finance/bookkeeping role, recent growth, or messy-ops language on their site

## Funnel
| Stage | Count |
|---|---|
| Companies from Clay search (marketing services, 11-50 employees, US, agency keywords) | 38 |
| Contacts after removing non-US rows, poor fits, and rows with no decision-maker | 14 |
| Work emails found | 10 |
| Emails verified valid | 10 |
| Openers hand-checked against company websites | 10 ([X] correct, [Y] fixed) |

## Workflow
Company search > Company enrichment > People search (Surfe, with Icypeas as a second source) > Work email finder > ZeroBounce verification > AI opener > Manual fact-check

## Tools used
Clay (search, enrichment, AI column), Surfe, Icypeas, ZeroBounce

## What I learned
- The AI opener drifted into pitching in its first version. A stricter prompt (one sentence, one fact, no pitch) fixed most of it, but facts still changed between runs, so every opener needed a manual check against the company's own site.
- The first people search missed some companies, and a second provider helped fill gaps, though it returned poor matches (wrong titles and countries) when run on every row.
- One email domain didn't match the company name, which is why I compare domains before trusting a verified email.

## Credits
About [X] of 1,000 free-plan credits used.

## Files
- [prospect-list-sample - Prospects (redacted).csv](<prospect-list-sample - Prospects (redacted).csv>): company, domain, industry, size, state, email status, and the checked opener. Contact emails, last names, and LinkedIn links are not included.

## What I'd improve
- Add a second email provider for the 4 contacts with no result
- Score companies by hiring signals for finance roles
- Pull a bigger starting list so more rows survive each filter
