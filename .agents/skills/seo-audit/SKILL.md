---
name: seo-audit
description: >-
  Executes comprehensive 9-category technical and on-page SEO audits for websites
  or specific code routes. Analyzes crawlability, indexability, Core Web Vitals (LCP, INP, CLS),
  rendering, semantic markup, canonicals, redirects, and sitemaps. Computes an objective
  0–100 SEO Health Score and produces a prioritized code remediation matrix.
  Use when the user asks for a site audit, technical SEO review, page speed/CWV check,
  or pre-launch quality gate.
user-invocable: true
argument-hint: "[url-or-local-path]"
metadata:
  version: "1.0.0"
  category: seo
---

# Technical & Comprehensive SEO Audit

This skill performs a rigorous, systematic inspection across 9 foundational SEO disciplines. It translates high-level search engine requirements into direct codebase fixes.

---

## The 9-Category Audit Framework

```
Site / Route Audit Target
├── 1. Crawlability & Indexability (robots.txt, HTTP headers, status codes, sitemaps)
├── 2. Canonicalization & Routing (canonical tags, trailing slashes, 301 redirects)
├── 3. Rendering & Hydration (SSR/SSG vs Client-Side JS SPA, fallback markup)
├── 4. Semantic Document Architecture (single H1, heading outline H2-H6, semantic tags)
├── 5. Metadata Engineering (title width 480-580px, meta description 140-160 chars, OG/Twitter)
├── 6. Structured Data & Knowledge Graph (JSON-LD validation, @graph node linking)
├── 7. Performance & Core Web Vitals (LCP < 2.5s, INP < 200ms, CLS < 0.1, hero preloading)
├── 8. Media & Asset Hygiene (WebP/AVIF format, descriptive alt tags, explicit width/height)
└── 9. Internationalization & Geo-Targeting (hreflang annotations, x-default fallback)
```

---

## 9-Category Detailed Audit Checklist

### 1. Crawlability & Indexability
- [ ] `robots.txt` present at root (`/robots.txt`), returns HTTP 200, valid syntax.
- [ ] No unintended `Disallow: /` blocking production crawlers.
- [ ] AI scrapers (`Google-Extended`, `PerplexityBot`, `ChatGPT-User`, `ClaudeBot`) explicitly allowed for GEO visibility.
- [ ] `X-Robots-Tag` or `<meta name="robots">` does not contain accidental `noindex` or `nofollow` on production routes.
- [ ] Sitemaps declared in `robots.txt` pointing to live XML sitemap.
- [ ] Sitemaps contain only 200 OK canonical URLs (zero 301, 302, 404, or `noindex` entries).

### 2. Canonicalization & Routing
- [ ] Every indexable page features an explicit self-referential `<link rel="canonical" href="...">`.
- [ ] Canonical URLs use lowercase characters, correct protocol (`https`), and single trailing slash convention.
- [ ] Clean status codes: 200 OK for canonical targets; 301 for legacy/normalized variants; 410 for permanently removed resources.
- [ ] Zero circular redirect chains or redirect hops exceeding 2 jumps.

### 3. Rendering & Hydration
- [ ] Critical content rendered in initial server HTML (SSR or SSG / ISR).
- [ ] No blank body tags requiring client-side JavaScript execution to reveal text or links to search crawlers.
- [ ] Dynamic internal navigation uses standard `<a href="...">` anchor tags, never `onClick` JavaScript handlers.

### 4. Semantic Hierarchy & Document Outline
- [ ] Strictly **one `<h1>` element** per page matching user search intent.
- [ ] Logical heading hierarchy (`<h2>` $\to$ `<h3>` $\to$ `<h4>`) with zero skipped levels.
- [ ] Heading tags are not used for visual layout in navigation bars, sidebars, or footers.
- [ ] Semantic HTML5 elements (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`) enclose content.

### 5. Metadata Engineering
- [ ] **Title Tag:** 50–60 characters (480–580px). Format: `Primary Keyword – Benefit/Spec | Brand`. Zero keyword stuffing.
- [ ] **Meta Description:** 140–160 characters. Includes primary search phrase, clear value proposition, and an imperative call to action.
- [ ] **Social Graph:** Fully populated `og:title`, `og:description`, `og:image` (1200x630px), `og:url`, `twitter:card` (`summary_large_image`).

### 6. Structured Data (Schema.org JSON-LD)
- [ ] Valid JSON-LD embedded inside `<script type="application/ld+json">`.
- [ ] Interconnected `@graph` structure linking `#organization`, `#website`, `#author`, and `#webpage`.
- [ ] Page-specific schemas present: `SoftwareApplication` for SaaS, `Product` for stores, `Article` for blogs, `FAQPage` for Q&A, `LocalBusiness` for physical premises.
- [ ] Strict match rule: Every datum in the schema is visibly rendered on the page.

### 7. Core Web Vitals & Performance
- [ ] **LCP (< 2.5s):** Hero image preloaded via `<link rel="preload" as="image">` or Next.js `priority={true}`.
- [ ] **INP (< 200ms):** No heavy main-thread blocking scripts. Third-party tags deferred or loaded via Web Workers.
- [ ] **CLS (< 0.1):** All images, videos, embeds, and iframes declare explicit `width` and `height` attributes or CSS `aspect-ratio`. Zero unreserved layout shifts.

### 8. Media & Asset Hygiene
- [ ] All images serve modern formats (WebP or AVIF).
- [ ] Descriptive, non-stuffed `alt` text on all content images.
- [ ] Purely decorative images marked with `alt=""` and `aria-hidden="true"`.
- [ ] Font files self-hosted with `font-display: swap` to prevent FOIT (Flash of Invisible Text).

### 9. Internationalization & Security
- [ ] Bidirectional `hreflang` tags on all localized alternates with valid ISO 639-1 language and ISO 3166-1 alpha-2 region codes.
- [ ] Fallback `hreflang="x-default"` present.
- [ ] HTTP Strict Transport Security (HSTS) and modern security headers configured.

---

## Scoring Methodology (0–100 Health Score)

Weights across the 9 categories:
- **Crawlability & Indexability:** 25 points (fatal blocker if failed)
- **Canonicalization & Routing:** 15 points
- **Rendering & Semantic HTML:** 15 points
- **Core Web Vitals & Speed:** 15 points
- **Structured Data:** 10 points
- **Metadata & Social:** 10 points
- **Media Hygiene:** 5 points
- **Internationalization / Security:** 5 points

---

## Output Format: Prioritized Fix Matrix

Always generate results in this structured format with exact drop-in code fixes:

```markdown
# SEO Technical Audit Report: [Target URL / Route]
**SEO Health Score:** [Score]/100
**Archetype Detected:** [SaaS / E-commerce / Local / Publisher / DevTool]

### Critical Issues (Score Impact: -15 to -25 pts)
| # | Issue | File Location | Impact | Code Fix |
|---|---|---|---|---|
| 1 | Missing self-referential canonical | `app/services/page.tsx` | Index fragmentation | [Exact Code Snippet] |

### Warnings (Score Impact: -5 to -10 pts)
...

### Opportunities (Score Impact: -1 to -4 pts)
...

### Verified Code Replacements
```typescript
// Replace lines X-Y in target file with:
...
```
