---
name: seo-internal-linking
description: >-
  Audits, designs, and optimizes internal linking architecture, topic clusters,
  and PageRank flow across the site. Eliminates orphan pages, minimizes crawl depth
  (keeping money pages within 3 clicks of root), enforces descriptive anchor text,
  and guarantees trailing slash consistency.
  Use when planning site architecture, auditing internal links, optimizing anchor text,
  or fixing crawl depth bottlenecks.
user-invocable: true
argument-hint: "[audit|optimize] [target-directory-or-route]"
metadata:
  version: "1.0.0"
  category: seo
---

# Internal Linking Architecture & PageRank Distribution

Internal links are the primary mechanism by which search engine spiders discover pages, map topical relationships, and distribute PageRank (link equity).

A chaotic internal linking structure with orphan pages, deep click depths, and generic anchor text ("click here") severely impairs ranking potential even for high-quality content.

---

## 4 Principles of High-Performance Site Architecture

```
Internal Linking Architecture
├── 1. Topical Siloing (Cluster spokes link strictly to parent pillar and sister spokes)
├── 2. 3-Click Rule (Every revenue or pillar page reachable within <= 3 clicks from root)
├── 3. Descriptive Anchor Text (Varied, natural, topical keyword phrases; zero "click here")
└── 4. Trailing Slash Normalization (Single deterministic URL convention across all internal links)
```

---

## 1. Topical Siloing (Hub & Spoke Model)

To build topical authority in modern search algorithms, organize content into strict thematic silos:

```
[Pillar: Cloud Infrastructure (/cloud/)]
  ├── Links DOWN to Spoke A: Distributed Caching (/cloud/caching)
  ├── Links DOWN to Spoke B: Multi-Region Failover (/cloud/failover)
  └── Links DOWN to Spoke C: Zero-Trust Network (/cloud/zero-trust)

[Spoke A: Distributed Caching]
  ├── Links UP to Pillar (/cloud/) with authoritative anchor ("cloud infrastructure architecture")
  └── Links ACROSS to Spoke B (/cloud/failover) with contextual anchor ("resilient failover pipelines")
```

> **The Siloing Rule:** Do not link randomly between unrelated silos (e.g., from an HR software blog post to a database caching guide) unless there is a genuine contextual connection. Irrelevant links dilute topical focus.

---

## 2. The 3-Click Crawl Depth Rule

Search engine crawlers allocate finite crawl budget. Pages buried 5+ clicks deep in the hierarchy are crawled infrequently and suffer lower ranking weight:

```
Click Depth 0: Homepage (/)
  └── Click Depth 1: Main Navigation Categories (/services, /pricing, /blog, /docs)
        └── Click Depth 2: Pillar Guides & Primary Landing Pages (/services/cloud-audits)
              └── Click Depth 3: Granular Articles & Case Studies (/blog/distributed-caching)
```

- **Money Pages & Conversion Pages:** Must be at **Depth 1 or Depth 2**.
- **Blog Posts & Deep Documentation:** Must never exceed **Depth 3**.
- **Breadcrumb Navigation:** Implement breadcrumbs on every subpage (`Home > Services > Cloud Audits`) with `BreadcrumbList` JSON-LD schema.

---

## 3. Anchor Text Engineering

Anchor text tells search engines what the destination page is about before they crawl it:

### The Anchor Text Rules:
- ✅ **Descriptive & Topical:** *"Read our breakdown of [Schema.org structured data for e-commerce]."*
- ✅ **Varied Semantic Phrasing:** Use synonyms and related concepts across different linking pages.
- ❌ **Generic Phrases:** Never link `[click here]`, `[learn more]`, `[read more]`, or `[this link]`.
- ❌ **Naked URLs:** Avoid pasting raw URLs `https://yourdomain.com/page` into prose.
- ❌ **Over-Optimized Exact Match Spam:** Do not repeatedly link identical 5-word keyword strings 50 times across the site.

---

## 4. Trailing Slash & Canonical Link Hygiene

Mixing trailing slashes across internal links causes unnecessary 301 redirects and wastes crawl budget:

```typescript
// ❌ WRONG: Inconsistent link formats
<Link href="/services">Services</Link>
<Link href="/services/">Services</Link>
<Link href="/services/audit">Audit</Link>

// ✅ CORRECT: Standardized single convention (choose with-slash or without-slash)
// Example (No Trailing Slash):
<Link href="/services">Services</Link>
<Link href="/services/audit">Audit</Link>
```

---

## Internal Link Audit Procedure

When auditing internal links across a codebase or route:
1. **Find Orphan Pages:** Check sitemap URLs against all internal `<a href>` references. Any URL with 0 incoming internal links is an orphan and must be linked from a category or related article.
2. **Flag Low-Value Anchors:** Grep codebase for `>click here<`, `>learn more<`, `>read more<`. Replace with descriptive targets.
3. **Inspect Broken Links:** Verify all internal relative paths resolve to live routes returning HTTP status 200.
4. **Enforce Breadcrumbs:** Verify every sub-route renders breadcrumb links back to parent categories.
