---
name: seo-roast
description: >-
  Runs a brutal, revenue-first SEO teardown of a site or codebase.
  Identifies fatal crawl blockers, indexation self-owns, rendering traps,
  and conversion leaks, triageing issues into FATAL, REVENUE, COMPOUNDING,
  and FLUFF tiers. Ends in immediate code fixes rather than bloated checklists.
  Use when the user asks to "roast my SEO", "why don't we rank", asks why organic
  traffic/signups are flat, or wants an unfiltered revenue-focused teardown.
user-invocable: true
argument-hint: "[target-url-or-repo-path]"
metadata:
  version: "1.0.0"
  category: seo
---

# SEO Roast: Revenue-First Teardown That Ends in a Merged PR

Most traditional SEO audits dump a 60-page PDF listing 350 minor warnings: alt text missing on decorative svgs, meta descriptions 3 characters too long, H3 tags out of order. The company continues losing revenue because the 2 fatal bugs that actually matter sit buried on page 42.

**An SEO Roast does the exact opposite:** find what is actively killing revenue or indexation, state it bluntly in plain English, ship the fix immediately in code, and rank everything else by dollars.

---

## The Prime Directive: Fatal First, Fluff Never

```
Identified Issue
├── FATAL: Completely blocks crawling, indexing, or rendering of revenue pages
│   └── ACTION: Fix immediately in this PR. Zero other work ships until fatal is dead.
├── REVENUE: Page indexes but cannot rank for buyer intent or cannot convert traffic
│   └── ACTION: Fix in this PR if under 1 hour of code, else top of roadmap.
├── COMPOUNDING: Authority, topic clusters, internal links, AI search citability
│   └── ACTION: Prioritized in the roadmap with concrete owners and deliverables.
└── FLUFF: Alt text on icons, meta length off by 5 chars, heading tag levels on footer
    └── ACTION: Quarantine at the bottom. Never touch fluff while fatal or revenue rows remain.
```

---

## The 6 Fatal Blocker Checks

Run these 6 checks first. If any check fails, sound the alarm and generate the fix immediately:

### 1. The Self-Own Robots & Meta Blocker
- **The Crime:** Leaking staging configurations to production: `User-agent: * Disallow: /` or `<meta name="robots" content="noindex, nofollow">` on live money pages.
- **The Test:** Check `/robots.txt` and raw server response headers for `X-Robots-Tag: noindex`.
- **The Fix:** Replace with explicit allow rules and restrict disallow to sensitive endpoints (`/admin/`, `/api/`, `/checkout/`).

### 2. The Client-Side JavaScript Ghost Town
- **The Crime:** Modern SPA frameworks rendering empty `<div id="root"></div>` or `<div id="__next"></div>` with all copy, navigation, and links injected via client-side `useEffect` or client bundles.
- **The Test:** Fetch the page with JavaScript disabled (`curl -sL [URL]` or disable JS in browser). If the page is blank or lacks body copy and primary navigation links, crawlers see nothing.
- **The Fix:** Migrate to Server-Side Rendering (SSR), Static Site Generation (SSG), or Incremental Static Regeneration (ISR).

### 3. The Broken Canonical Trap
- **The Crime:**
  - Setting canonical tags that point to HTTP instead of HTTPS.
  - Setting canonical tags that point to a URL that returns a 301 redirect or 404 error.
  - Setting canonical tags that point to a different category or homepage.
  - Inconsistent trailing slashes: internal links point to `/page/` but canonical declares `/page`.
- **The Test:** Curl the canonical target URL and verify it returns HTTP status `200 OK` with identical URL casing.
- **The Fix:** Standardize canonical URLs programmatically from the router environment variable.

### 4. Accidental Soft 404s & Redirect Loops
- **The Crime:** Server returns HTTP 200 OK for missing or invalid items (e.g., deleted products or empty search queries) showing a "Sorry, not found" message, or circular redirects (`/a` $\to$ `/b` $\to$ `/a`).
- **The Test:** Request non-existent slug `/this-slug-must-not-exist-xyz123`. Verify it returns genuine HTTP `404` or `410`.
- **The Fix:** Return an actual 404/410 status code in the server route handler.

### 5. High-Intent Traffic with Zero Conversion Path
- **The Crime:** An informational guide or comparison page ranks #3 for a high-value commercial query, but has no clear value proposition, no visible signup button, no inline interactive tool, and hides pricing behind a "Contact Sales" form with 12 fields.
- **The Test:** Review above-the-fold viewport on mobile (390px width). Is there a clear headline, proof point, and single-click CTA visible without scrolling?
- **The Fix:** Insert an above-the-fold conversion card with social proof and a friction-free call to action.

### 6. AI Engine Blackout (GEO Denial)
- **The Crime:** Disallowing `GPTBot`, `PerplexityBot`, `ClaudeBot`, or `Google-Extended` in `robots.txt` out of paranoia, completely erasing the brand from Google AI Overviews, Perplexity answers, and ChatGPT Search.
- **The Test:** Inspect `robots.txt` for AI crawler disallows.
- **The Fix:** Explicitly allow generative bots to crawl public content while disallowing private application and user data routes.

---

## Roast Execution Procedure

1. **Intake (1 minute):**
   - Identify the primary money pages (Homepage, Pricing, Core Features, Top Comparison Page).
   - Identify the conversion goal (Free trial, newsletter, paid checkout, demo booking).
2. **Execute the 6 Fatal Blocker Checks:**
   - Immediately flag any fatal blocker found.
3. **Formulate the Blunt Verdict:**
   - Open the roast with a single, unvarnished sentence describing the exact state of the site.
   - *Example:* "Your site is invisible to every engine except Google because your robots.txt denies all AI bots, and your pricing page canonical points to a 404."
4. **Draft the Code Fix PR:**
   - Provide exact code replacements for all FATAL issues.
5. **Output the Revenue-Ordered Roadmap:**

```markdown
# 🔥 The SEO Roast: [Target Name / Domain]

> **The Verdict:** [One-line blunt statement of reality]

## Tier 1: FATAL BLOCKERS (Killed in this PR)
- [ ] **Issue:** [Description]
  - **Why it kills revenue:** [Explanation]
  - **Code Fix:**
    ```diff
    - Disallow: /
    + Allow: /
    ```

## Tier 2: REVENUE LEAKS (Fix This Week)
- [ ] **[Page/Route]:** [Issue description] | Est. Dev Time: [X] hours | Expected Lift: [Y]%

## Tier 3: COMPOUNDING GAINS (Roadmap)
- [ ] **Internal Linking Silo:** [Action]
- [ ] **Proof KB Integration:** [Action]

## Tier 4: FLUFF (Do Not Touch Until Tiers 1-3 Are Complete)
- Missing alt text on 4 decorative icons
- Meta description on /about is 168 characters
```
