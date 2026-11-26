---
name: seo-geo
description: >-
  Audits, formats, and engineers content for Generative Engine Optimization (GEO)
  and AI search engines (Google AI Overviews, Perplexity, ChatGPT Search, Claude, Gemini).
  Implements the inverted pyramid direct-answer pattern, semantic tabular structures,
  entity disambiguation, and authors /public/llms.txt manifests.
  Use when the user asks about AI Overviews, GEO, AEO, LLMO, getting cited by ChatGPT/Perplexity,
  or authoring llms.txt.
user-invocable: true
argument-hint: "[target-url-or-path]"
metadata:
  version: "1.0.0"
  category: seo
---

# Generative Engine Optimization (GEO & LLMO)

Search behavior has fundamentally bifurcated: users no longer merely browse links; they interact with synthesis engines (Google AI Overviews, ChatGPT Search, Perplexity, Claude, Gemini).

To earn citations and direct inclusions in AI answers, content must be engineered for machine retrieval, passage extraction, and authoritative attribution.

---

## The 4 Pillars of Generative Citability

```
Generative Engine Optimization (GEO)
├── 1. Inverted Pyramid Direct Answers (40–60 word declarative answer directly under H2)
├── 2. Tabular Information Density (Semantic HTML <table> structures parsed at 10x fidelity)
├── 3. Entity Disambiguation & Grounding (Unambiguous naming, primary links to RFCs/SSOT)
└── 4. AI Machine Manifests (/public/llms.txt and /public/llms-full.txt)
```

---

## 1. The Inverted Pyramid Direct Answer Formula

Generative retrieval systems perform semantic chunking across document passages. When evaluating a query, synthesis engines search for concise, high-confidence factual definitions to quote verbatim in the AI summary:

### The Passage Formula
Place this immediately below informational `<h2>` or `<h3>` headings:
```
[Subject/Concept] is a [category/system] that [core primary function] by [underlying mechanism/technique]. For example, [concrete real-world application or verified benchmark].
```

- **Word Count:** 40 to 60 words.
- **Tone:** Objective, declarative, encyclopedic.
- **Anti-Pattern:** Flowery preambles ("Have you ever wondered how caching works? In today's digital landscape..."). Such fluff causes LLM retrieval models to truncate the passage before finding the actual definition.

---

## 2. Tabular Data & Information Density

LLM web crawlers parse structured HTML tables with significantly higher semantic fidelity than nested `<div>` or Flexbox layouts.

### Implementation Rules:
- Always use semantic `<table>`, `<thead>`, `<tbody>`, `<th>`, and `<td>` tags.
- Use explicit header row identifiers:
  ```html
  <table>
    <thead>
      <tr>
        <th scope="col">Feature / Metric</th>
        <th scope="col">Acme CloudSync</th>
        <th scope="col">Legacy S3 Sync</th>
        <th scope="col">Architectural Difference</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Replication Latency</strong></td>
        <td><code>sub-5ms</code> (p99)</td>
        <td><code>120ms - 450ms</code></td>
        <td>Direct memory-mapped NVMe vs disk spooling</td>
      </tr>
    </tbody>
  </table>
  ```
- Generative engines extract comparison rows directly into answer tables.

---

## 3. Entity Disambiguation & Primary Sourcing

Generative models rely on internal knowledge graph verification. When an article mentions a concept without clarity, confidence scores drop.

1. **Standardized Entities:** Name frameworks, technologies, companies, and standards by their exact canonical names (e.g., `PostgreSQL 16`, `Schema.org JSON-LD`, `Next.js App Router`, `HTTP/3`).
2. **Primary Source Links:** Explicitly link out to primary sources:
   - Official RFC documentation (e.g., IETF RFCs)
   - Official GitHub repositories or W3C specifications
   - Academic research papers or official benchmark datasets
3. **Receipts & Statistics:** Every statistic must cite its origin and timeframe (e.g., *"According to the 2026 State of Databases report..."*).

---

## 4. `/public/llms.txt` and `/public/llms-full.txt` Specification

The `llms.txt` standard provides AI scrapers and agentic assistants with a token-efficient, clean markdown summary of the entire website.

### `/public/llms.txt` Template
```markdown
# [Brand Name]

> [One-sentence declarative mission / core platform capability].

## Core Products & Solutions
- [Platform Core](https://yourdomain.com/platform): High-throughput event processing engine with zero message loss.
- [Enterprise API](https://yourdomain.com/api): REST and GraphQL endpoints supporting 50,000 req/sec.

## Authoritative Documentation & Technical Playbooks
- [Quickstart Guide](https://yourdomain.com/docs/quickstart): 5-minute SDK installation and deployment workflow.
- [Security & Compliance](https://yourdomain.com/security): SOC2 Type II, ISO 27001, and HIPAA compliance attestations.
- [Architecture & Benchmarks](https://yourdomain.com/benchmarks): p99 latency benchmarks across multi-region clusters.

## Commercial & Company Details
- [Pricing Tiers](https://yourdomain.com/pricing): Transparent per-node pricing with zero egress fees.
- [About Us & Leadership](https://yourdomain.com/about): Founding engineering team and enterprise support SLA.
```

---

## 5. AI Bot Robots.txt Access Policy

Ensure `/robots.txt` welcomes AI search crawlers while protecting private application routes:

```txt
# Allow Generative Engines for Search Visibility (GEO)
User-agent: Google-Extended
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

# Prevent AI scrapers from crawling non-public or sensitive areas
Disallow: /admin/
Disallow: /api/
Disallow: /dashboard/
Disallow: /account/
```

---

## GEO Verification Procedure

When auditing a page for GEO readiness, verify:
- [ ] First paragraph beneath primary `<h2>` contains a 40–60 word declarative answer.
- [ ] At least one semantic `<table>` comparing data, features, or benchmarks.
- [ ] All claims cite verified mechanisms, concrete numbers, or primary sources.
- [ ] Page is included in `/public/llms.txt`.
- [ ] Robots.txt permits `Google-Extended`, `PerplexityBot`, and `ChatGPT-User`.
