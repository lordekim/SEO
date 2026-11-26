---
name: seo-analytics-mcp
description: >-
  Connects to real search and analytics data via MCP (Model Context Protocol),
  integrating Google Search Console, GA4, Ryze MCP connector, and DataForSEO.
  Tracks real AI referral traffic (ChatGPT, Perplexity, Claude, Gemini), measures rank movers,
  identifies high-value striking-distance keywords (#4–#15), diagnoses CTR anomalies,
  and analyzes competitor keyword gaps and backlink profiles.
  Use when connecting live SEO data, checking keyword rankings, tracking AI citations
  in GA4, or analyzing Search Console queries.
user-invocable: true
argument-hint: "[ai-traffic|rank-track|striking-distance|backlinks] [domain]"
metadata:
  version: "1.0.0"
  category: seo
---

# Live SEO Analytics & MCP Data Integration

Most SEO audits run on static crawl approximations and prompt sampling guesses. Real SEO decisions must be driven by **actual user data, live Google Search Console queries, and verified GA4 referral sessions**.

This skill interfaces directly with real search data via MCP servers (such as the free Ryze connector or direct API connectors).

---

## 1. Connecting the MCP Server

To enable live data calls inside Claude Code, Antigravity, or Cursor, connect the MCP endpoint:

```bash
# Register Ryze MCP Connector (HTTP transport)
# Connects Google Search Console, GA4, Google Ads, and DataForSEO
claude mcp add ryze --transport http https://connector.get-ryze.ai/mcp
```

Or configure via `mcp_config.json` in Antigravity:
```json
{
  "mcpServers": {
    "ryze": {
      "url": "https://connector.get-ryze.ai/mcp"
    }
  }
}
```

---

## 2. Tracking Real AI Referral Traffic (GA4)

Third-party AI visibility tools guess by sampling prompts. GA4 records the exact clicks and conversions delivered by AI engines.

### Measuring AI Engine Referral Traffic:
Query GA4 filtered by known AI search referrers:
- `chatgpt.com` / `android-app://com.openai.chatgpt`
- `perplexity.ai`
- `gemini.google.com`
- `claude.ai`
- `copilot.microsoft.com`

### Workflow:
1. **Sessions by Engine:** Compare AI referral sessions (current 30 days vs previous 30 days) to calculate growth velocity.
2. **Proven-Citable Landing Pages:** Identify the specific URLs receiving AI traffic. Inspect their structure: note their heading clarity, definitions, and data tables. This is your proven citation recipe.
3. **The Misses (High GSC Impressions, Zero AI Referrals):** Identify pages that rank on page 1 of Google organic search but get zero AI referral traffic. Restructure them using the `seo-geo` inverted pyramid pattern.

---

## 3. Rank Tracking & "Striking Distance" Query Hunting

Instead of paying for third-party rank tracker subscriptions, query real Google Search Console data:

### Hunting Striking Distance Keywords (#4 to #15):
Striking distance queries are the fastest organic revenue growth opportunities in SEO:
```
Filter GSC Data:
- Average Position: >= 4.0 and <= 15.0
- Impressions: >= 500 / month
- CTR: < 3.0%
```

### Remediation Protocol:
1. **Title & Meta CTR Optimization:** The page already ranks on page 1 or top of page 2, but searchers aren't clicking. Update the title tag with a clearer benefit or power modifier, and craft an active CTA in the meta description.
2. **Targeted Subheading Injection:** Add an explicit `<h2>` or `<h3>` matching the exact query string, followed by a concise 50-word answer.
3. **Internal Linking Boost:** Add 2-3 contextual internal links from high-authority pages on the site pointing directly to this URL using the striking-distance keyword in the anchor text.

---

## 4. CTR Anomaly Detection

A query with position #1 or #2 typically captures a 25%–35% CTR. If a query ranks #2 but only earns a 4% CTR, a **CTR Anomaly** exists.

### Root Causes & Fixes:
- **Title Tag Truncation:** Title is over 600px wide, cutting off the value proposition on mobile screens. Shorten to 55 characters.
- **SERP Feature Crowding:** The query triggers a massive Google Ads block, Map Pack, or AI Overview pushing organic #2 below the fold. Target the PAA (People Also Ask) or AI Overview passage to regain above-the-fold visibility.
- **Intent Mismatch:** The query is navigational (users seeking a login page), but the ranking page is an informational blog post.

---

## 5. Competitor Keyword Gap & Backlink Analysis

When DataForSEO or Ahrefs MCP tools are active:

1. **Competitor Keyword Gap:**
   - Input your domain vs 2 primary competitors.
   - Filter for keywords where Competitor ranks in top 10, but your domain does not rank in the top 100.
   - Categorize by intent: flag commercial comparison queries for `seo-competitor-pages`.
2. **Backlink Quality Audit:**
   - Review referring domains, Domain Authority/Rating, and anchor text distribution.
   - Check for toxic spam link spikes or sudden losses in referring domains.
