---
name: seo-schema
description: >-
  Designs, generates, validates, and embeds production-grade Schema.org JSON-LD
  structured data. Implements interconnected @graph Knowledge Graphs linking
  Organization, WebSite, Author Person (E-E-A-T), SoftwareApplication, Product,
  Article, FAQPage, and LocalBusiness nodes. Provides native Next.js, Astro, and HTML recipes.
  Use when the user asks to add or audit schema markup, structured data, JSON-LD,
  or rich search results.
user-invocable: true
argument-hint: "[generate|validate|audit] [target-url-or-route]"
metadata:
  version: "1.0.0"
  category: seo
---

# Structured Data & Knowledge Graph Engineering (Schema.org JSON-LD)

Structured data converts unstructured HTML into an explicit Knowledge Graph that traditional search engines (Google, Bing) and LLM search engines parse without ambiguity.

Always embed valid JSON-LD inside `<script type="application/ld+json">`. Never output unlinked, floating schema fragments.

---

## The Interconnected Knowledge Graph Model (`@graph`)

Rather than isolated schema tags, bundle all page entities into a single `@graph` array referencing unified `@id` nodes:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://yourdomain.com/#organization",
      "name": "Acme Technologies",
      "url": "https://yourdomain.com",
      "logo": {
        "@type": "ImageObject",
        "@id": "https://yourdomain.com/#logo",
        "url": "https://yourdomain.com/images/logo.png",
        "caption": "Acme Technologies Logo",
        "width": 600,
        "height": 60
      },
      "sameAs": [
        "https://www.linkedin.com/company/acmetech",
        "https://x.com/acmetech",
        "https://github.com/acmetech"
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://yourdomain.com/#website",
      "url": "https://yourdomain.com",
      "name": "Acme Technologies",
      "publisher": { "@id": "https://yourdomain.com/#organization" }
    },
    {
      "@type": "WebPage",
      "@id": "https://yourdomain.com/products/cloudsync#webpage",
      "url": "https://yourdomain.com/products/cloudsync",
      "name": "CloudSync Engine | Acme Technologies",
      "isPartOf": { "@id": "https://yourdomain.com/#website" },
      "breadcrumb": { "@id": "https://yourdomain.com/products/cloudsync#breadcrumb" }
    }
  ]
}
```

---

## Core Domain Schemas

### 1. SoftwareApplication / SaaS Product Schema
Use for software, SaaS platforms, developer tools, and web applications:
```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "CloudSync Engine",
  "operatingSystem": "All modern browsers, Linux, macOS, Windows",
  "applicationCategory": "DeveloperApplication",
  "offers": {
    "@type": "Offer",
    "price": "49.00",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "priceValidUntil": "2027-12-31"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": "128"
  }
}
```

### 2. E-Commerce Product & Offer Schema
For physical products and digital goods with pricing, stock, and reviews:
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Enterprise Security Gateway",
  "image": "https://yourdomain.com/images/gateway.jpg",
  "description": "Hardware-accelerated zero-trust network gateway appliance.",
  "sku": "ESG-9000",
  "brand": {
    "@type": "Brand",
    "name": "Acme Hardware"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://yourdomain.com/products/esg-9000",
    "priceCurrency": "USD",
    "price": "1299.00",
    "availability": "https://schema.org/InStock",
    "itemCondition": "https://schema.org/NewCondition"
  }
}
```

### 3. Author Profile & E-E-A-T Person Schema
Search algorithms evaluate Experience, Expertise, Authoritativeness, and Trustworthiness:
```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "https://yourdomain.com/authors/dr-alex-stone/#author",
  "name": "Dr. Alex Stone",
  "jobTitle": "Lead Distributed Systems Architect",
  "worksFor": { "@id": "https://yourdomain.com/#organization" },
  "alumniOf": {
    "@type": "EducationalOrganization",
    "name": "Stanford University"
  },
  "knowsAbout": ["Cloud Infrastructure", "Distributed Systems", "Search Architecture"],
  "sameAs": [
    "https://scholar.google.com/citations?user=...",
    "https://www.linkedin.com/in/alexstone",
    "https://github.com/alexstone"
  ]
}
```

### 4. Article & BlogPosting Schema (with Author Linkage)
```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "@id": "https://yourdomain.com/blog/distributed-caching#article",
  "headline": "Modern Distributed Caching at Scale",
  "description": "An architectural breakdown of multi-region key-value stores with sub-millisecond latencies.",
  "image": "https://yourdomain.com/images/hero-caching.jpg",
  "datePublished": "2026-10-15T09:00:00+00:00",
  "dateModified": "2026-11-20T11:45:00+00:00",
  "mainEntityOfPage": "https://yourdomain.com/blog/distributed-caching",
  "author": { "@id": "https://yourdomain.com/authors/dr-alex-stone/#author" },
  "publisher": { "@id": "https://yourdomain.com/#organization" }
}
```

### 5. FAQPage Schema (Strict Match Verification)
> **Crucial Rule:** Every Question and Answer in the schema must appear verbatim in the visible page text. Never include questions hidden in tabs or omitted from the HTML.
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the typical deployment timeline for enterprise migrations?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Enterprise migrations typically take between 4 to 8 weeks depending on database volume and custom integration requirements."
      }
    }
  ]
}
```

### 6. LocalBusiness Schema (NAP & Service Radius)
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "https://yourdomain.com/#localbusiness",
  "name": "Acme Consulting Austin",
  "image": "https://yourdomain.com/images/storefront.jpg",
  "telephone": "+1-512-555-0144",
  "email": "contact@yourdomain.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "100 Congress Ave, Suite 2000",
    "addressLocality": "Austin",
    "addressRegion": "TX",
    "postalCode": "78701",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 30.2672,
    "longitude": -97.7431
  },
  "priceRange": "$$"
}
```

---

## Framework Integration Recipes

### Next.js App Router (TypeScript Component)
Create a reusable, safe Schema component:
```typescript
// components/JsonLd.tsx
export default function JsonLd({ schema }: { schema: Record<string, any> }) {
  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }}
    />
  );
}
```
Usage in `app/blog/[slug]/page.tsx`:
```typescript
import JsonLd from '@/components/JsonLd';

export default async function BlogPostPage({ params }: { params: { slug: string } }) {
  const post = await getPost(params.slug);
  const schema = {
    '@context': 'https://schema.org',
    '@type': 'BlogPosting',
    headline: post.title,
    // ...
  };

  return (
    <article>
      <JsonLd schema={schema} />
      <h1>{post.title}</h1>
      {/* ... */}
    </article>
  );
}
```

### Astro Framework Recipe
```astro
---
// src/components/JsonLd.astro
interface Props {
  schema: Record<string, any>;
}
const { schema } = Astro.props;
---
<script type="application/ld+json" set:html={JSON.stringify(schema)} />
```

---

## Schema Anti-Patterns & Validation Rules

- ❌ **Hallucinated Data:** Schema mentioning a 4.9 rating with 120 reviews when zero reviews appear on the page. (Triggers Google manual actions).
- ❌ **Multiple Floating Schemas:** Outputting 5 separate script tags without `@id` connections.
- ❌ **Mismatched Dates:** Schema `dateModified` that contradicts visible article timestamp.
- ❌ **Fake Person Schemas:** Generic "Admin" or "Acme Team" authored articles claiming deep scientific expertise without real `Person` credentials.
