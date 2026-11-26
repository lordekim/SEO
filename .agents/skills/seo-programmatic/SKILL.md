---
name: seo-programmatic
description: >-
  Designs, architects, and validates Programmatic SEO systems and database-driven landing pages.
  Ensures high data defensibility, unique content generation per route, dynamic metadata/canonicalization,
  and programmatic sitemap partitioning while strictly preventing Google doorway/thin content penalties.
  Use when creating programmatic directories, integration pages, location pages,
  or evaluating whether a scaled page set will rank.
user-invocable: true
argument-hint: "[plan|audit|schema] [dataset-or-route]"
metadata:
  version: "1.0.0"
  category: seo
---

# Programmatic SEO & Scaled Page Architecture

Programmatic SEO allows teams to capture thousands of long-tail, high-intent search queries by combining structured datasets with dynamic template engineering.

However, modern search algorithms ruthlessly penalize **doorway pages** and **thin content**—pages created simply by swapping a keyword into an otherwise identical template.

---

## The Hierarchy of Data Defensibility

A programmatic SEO project will only succeed if the underlying dataset provides unique utility that competitors cannot replicate:

```
Defensibility Hierarchy
├── 1. Proprietary Telemetry / Data (Calculated in-house, private benchmarks, user statistics) -> HIGHEST
├── 2. Enriched / Synthesized Data (Public datasets merged, cross-correlated, and scored)
├── 3. Curated Data (Manually verified lists with expert annotations)
└── 4. Raw Public APIs / Scraped Data (Easily copied by competitors; high risk of demotion) -> LOWEST
```

---

## 4 Core Rules to Prevent Thin Content Penalties

1. **The 30% Unique Body Rule:**
   - At least 30% of the visible rendered prose on every programmatic page must be unique to that specific record (e.g., specific benchmark results, regional compliance laws, specific API methods).
   - If a record only has 2 unique fields (e.g., `City Name` and `Zip Code`), **do not create a standalone page**. Group them into a parent regional page.
2. **Conditional Rendering of Incomplete Records:**
   - If a database entity lacks sufficient enrichment (e.g., zero user reviews, missing pricing data), return HTTP 404 or apply `<meta name="robots" content="noindex">`.
   - Never index empty shell pages with "No data available yet".
3. **Deterministic Dynamic Canonicalization:**
   - Each dynamic route must explicitly canonicalize to its clean, lowercased parameter URL:
     ```typescript
     // app/integrations/[slug]/page.tsx
     export async function generateMetadata({ params }): Promise<Metadata> {
       return {
         title: `${integration.name} Integration for Real-Time Sync | Brand`,
         alternates: {
           canonical: `https://yourdomain.com/integrations/${params.slug.toLowerCase()}`,
         },
       };
     }
     ```
4. **Partitioned Programmatic XML Sitemaps:**
   - Never dump 40,000 programmatic URLs into a single monolithic sitemap.
   - Use a sitemap index referencing partitioned sub-sitemaps (e.g., `sitemap-integrations.xml`, `sitemap-glossary-1.xml`). Each file must contain $\le$ 10,000 URLs.

---

## Programmatic Template Anatomy

Every programmatic template must include 5 structural components:

```
Programmatic Page Layout
├── 1. Dynamic Hero (Single H1, primary entity name, declarative one-sentence definition)
├── 2. Entity-Specific Metric Card (Proprietary data, latency, pricing, compatibility matrix)
├── 3. Semantic Comparison / Specs Table (HTML <table> comparing this entity against standards)
├── 4. Concrete Code Snippet / Integration Recipe (Copyable, syntax-highlighted code block)
└── 5. Dynamic Breadcrumbs & Related Cluster Links (BreadcrumbList JSON-LD + 4 related entities)
```

---

## Programmatic Quality Gate Checklist

Before deploying a programmatic page set, run this gate:
- [ ] Underlying dataset contains proprietary or heavily enriched fields.
- [ ] Template contains conditional blocks so missing data never outputs empty whitespace.
- [ ] Programmatic URLs use clean kebab-case without database primary keys (e.g., `/integrations/stripe`, not `/integrations?id=492`).
- [ ] Self-referential canonical tags correctly populated across all variations.
- [ ] BreadcrumbList Schema.org JSON-LD dynamically generated for every record.
- [ ] No duplicate content generated across faceted query parameters (`?sort=`, `?filter=`).
