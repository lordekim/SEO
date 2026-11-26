---
name: seo-content
description: >-
  Develops high-information-gain content strategies, generates structured SEO content briefs,
  classifies search intent, orchestrates topic clusters, and revitalizes decaying articles.
  Ensures content meets Google E-E-A-T criteria and avoids commodity AI text.
  Use when the user asks to write or outline an SEO article, generate a content brief,
  plan topic clusters, or refresh underperforming blog posts.
user-invocable: true
argument-hint: "[brief|refresh|cluster] [topic-or-path]"
metadata:
  version: "1.0.0"
  category: seo
---

# High-Information-Gain Content & E-E-A-T Strategy

Generative AI has commoditized derivative, low-effort web content. Search engines demote repetitive AI text and reward pages exhibiting high **Information Gain**—unique data, concrete primary research, firsthand expertise, and clear structural hierarchy.

---

## The 4 Search Intent Archetypes

Every piece of content must strictly align with one primary search intent. Mismatched intent leads to high bounce rates and ranking collapse:

| Intent Type | User Goal | Page Format | Primary CTA |
| :--- | :--- | :--- | :--- |
| **Informational** | Understand a concept, debug an error, learn how to do X | In-depth Technical Guide, Tutorial, Documentation | Newsletter, bookmark, related guide |
| **Commercial Investigation** | Compare options, evaluate pricing, assess trade-offs | `[A] vs [B]` Page, Alternatives List, Benchmark Matrix | Free trial, product demo, interactive calculator |
| **Transactional** | Buy, sign up, download, deploy | Product Landing Page, Pricing Page, Sign-Up Flow | Direct purchase, instant account creation |
| **Navigational** | Locate a specific brand resource | Homepage, Login, Docs Root | Direct navigation link |

---

## Structured SEO Content Brief Template

When generating an SEO Content Brief for an author or AI drafter, output this exact structure:

```markdown
# SEO Content Brief: [Target Topic / Primary Keyword]

## 1. Intent & Positioning
- **Primary Target Keyword:** [e.g., "distributed caching patterns"]
- **Secondary / Semantic Keywords:** [e.g., "cache invalidation strategies", "redis vs memcached", "p99 latency"]
- **Search Intent:** [Informational / Commercial Investigation / Transactional]
- **Target Audience:** [e.g., Staff Software Engineers, Cloud Architects]
- **Core Value Proposition / Angle:** [What unique insight or data does this page provide that #1 currently lacks?]

## 2. Meta Specification
- **Title Tag (50-60 chars):** `Primary Keyword – Unique Benefit | Brand`
- **Meta Description (140-160 chars):** Active hook with primary keyword, core promise, and active CTA.
- **URL Slug:** `/clean-kebab-case-slug`

## 3. Structural Document Outline (Heading Hierarchy)
- **<h1>:** [Compelling Title Matching Intent]
  - *Direct Answer / Executive Summary (40–60 words immediately below)*
- **<h2>:** [Section 1 - Core Problem / Architectural Context]
  - **<h3>:** [Specific failure mode or challenge]
- **<h2>:** [Section 2 - Comparative Benchmark or Direct Solution]
  - *Semantic HTML <table> comparing options across 4+ concrete metrics*
- **<h2>:** [Section 3 - Step-by-Step Implementation Recipe]
  - *Working code snippet with explicit dependencies*
- **<h2>:** [Frequently Asked Questions]
  - *3-4 questions targeting People Also Ask (PAA) queries*

## 4. First-Hand Proof & E-E-A-T Requirements
- [ ] At least one concrete production benchmark or measured latency/cost metric.
- [ ] Working code snippet tested against modern LTS versions.
- [ ] Author Person bio node linked to official engineering credentials.

## 5. Topic Cluster & Internal Link Plan
- **Parent Pillar Page Target:** Link back to `[Pillar URL]` with anchor text: `[Natural descriptive phrase]`
- **Spoke Links (Outgoing):** Link out to 2-3 related sub-topic articles.
- **Target Spoke Links (Incoming):** Update existing articles at `[URL A]` and `[URL B]` to point to this new post.

## 6. Required Schema.org Markup
- `@type`: `BlogPosting` or `TechArticle`
- Embedded `author` and `publisher` node IDs.
```

---

## Topic Cluster (Hub & Spoke) Architecture

```
Pillar Page (Broad Industry Guide, e.g. /cloud-architecture)
├── Spoke 1: Deep Dive (/cloud-architecture/distributed-caching)
├── Spoke 2: Deep Dive (/cloud-architecture/multi-region-failover)
├── Spoke 3: Deep Dive (/cloud-architecture/zero-trust-gateways)
└── Spoke 4: Deep Dive (/cloud-architecture/database-replication)
```

### Internal Linking Protocol:
1. Every Spoke links to the parent Pillar page within the first 30% of its body copy.
2. The Pillar links down to every Spoke within its respective sub-section.
3. Spokes link cross-sectionally to related sister Spokes when contextual relevance exists.
4. Anchor text must be descriptive and varied (e.g., *"explore our guide to [multi-region failover strategies]"*). Ban naked URLs and generic "click here" anchors.

---

## Content Decay & Revitalization Protocol

When a historically ranking article loses rank or traffic in Google Search Console:

1. **Query Gap Analysis:** Compare historical top queries (12 months ago) vs current queries in Search Console. Identify lost keywords.
2. **Freshness & Fact Check:** Update deprecated API methods, stale screenshots, or outdated year references (e.g., update 2024 benchmarks to 2026 data).
3. **Information Gain Injection:** Add a newly measured benchmark, comparison table, or diagram that competitors do not possess.
4. **Passage Optimization:** Rewrite the first paragraph under the main `<h2>` into a 40–60 word declarative direct answer for AI Overviews.
5. **Update Timestamp:** Update the `<lastmod>` in the sitemap and `dateModified` in the JSON-LD schema.
