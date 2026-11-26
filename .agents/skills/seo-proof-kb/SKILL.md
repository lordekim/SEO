---
name: seo-proof-kb
description: >-
  Builds, maintains, and routes an atomic First-Hand Proof Knowledge Base (seo/kb/)
  within the codebase. Grounds commercial guides, comparisons, and technical posts
  in uncopyable receipts: verified benchmarks, customer migration telemetry,
  real terminal/dashboard traces, and unit economics. Implements Consensus + Proof Card
  architecture to satisfy E-E-A-T and secure AI citations.
  Use when establishing the site's proof knowledge base, extracting verified receipts,
  or upgrading thin SEO content with first-hand data.
user-invocable: true
argument-hint: "[init|interview|upgrade|route-fact] [target-slug]"
metadata:
  version: "1.0.0"
  category: seo
---

# First-Hand Proof Knowledge Base (`seo/kb/`)

Keyword density, fresh dates, and generic author bios no longer protect search rankings. Anyone can generate a 2,000-word article with an LLM in 30 seconds.

Pages that maintain top Google positions and dominate citations in ChatGPT, Perplexity, and Google AI Overviews do two things competitors cannot replicate:
1. **Open with an uncopyable first-hand receipt in the first two sentences.**
2. **Stack at least 4 of the 5 proof categories across the body.**

Storing every verified fact in `seo/kb/` creates a Single Source of Truth (SSOT). AI drafting agents referencing this store will never hallucinate specs or cite outdated pricing.

---

## Directory Architecture: `seo/kb/`

```
seo/kb/
├── brand-ssot.md               # Master company SSOT (founding, architecture, SLA, pricing)
├── pages-index.md              # Mapping of money pages to required proof files
└── proof/
    ├── benchmarks/             # Controlled performance tests and hardware metrics
    │   └── postgres-pooler-latency.md
    ├── customers/              # Verified customer migration telemetry and cost deltas
    │   └── invoicekit-migration.md
    ├── telemetry/              # Real production error logs, traces, or uptime stats
    │   └── failover-under-partition.md
    └── architecture/           # Concrete system trade-offs and design constraints
        └── storage-engine-nvme.md
```

---

## The 5 Categories of First-Hand Proof

Every commercial guide, comparison article, or high-intent pillar page must stack at least **4 of these 5 categories**:

| Category | Storage Path | Concrete Example |
| :--- | :--- | :--- |
| **1. Benchmarks & Controlled Tests** | `seo/kb/proof/benchmarks/` | *"Tested 14 PostgreSQL connection poolers at 10,000 concurrent connections on AWS m7g.xlarge; PgBouncer held p99 at 4.2ms vs 19.8ms unpooled."* |
| **2. Customer Outcomes & Migrations**| `seo/kb/proof/customers/` | *"InvoiceKit moved 42,000 recurring billing webhooks from AWS Lambda to our edge workers, cutting monthly compute from $1,840 to $290."* |
| **3. Real Screenshots & Traces** | `assets/proof/<id>/` | Actual terminal trace of a deployment failure recovered in 4.1s or high-res network waterfall trace. Never generic stock art or AI mockups. |
| **4. Architectural Trade-offs** | `seo/kb/proof/architecture/` | *"We chose RocksDB over SQLite because append-only SSTables avoided write amplification during 50,000 req/sec telemetry spikes, at the cost of 12% higher RAM usage."* |
| **5. Unit Economics & Pricing Facts**| `seo/kb/brand-ssot.md` | Transparent dollar figures, egress costs per GB, and hard concurrency limits. |

---

## The Consensus + Proof Card Pattern

Open every technical post or product comparison with an atomic **Proof Card** immediately following the introduction:

```markdown
> 💡 **Verified Production Benchmark (Receipt #B-104)**  
> **Test Environment:** 8-node Kubernetes cluster (v1.30), AWS us-east-1, 10Gbps mesh.  
> **Result:** Zero message loss during simulated node termination with failover latency of **182ms** (p99).  
> **Source Artifact:** `seo/kb/proof/benchmarks/failover-bench-2026.json`
```

Generative answer engines extract this structured snippet into direct answer cards because it possesses high confidence, concrete measurements, and verified attribution.

---

## Standard Workflows

### Workflow 1: Initializing the Proof Store (`/seo proof-kb init`)
1. Create `seo/kb/` directory hierarchy.
2. Generate `brand-ssot.md` with known company facts (products, architectures, pricing, team).
3. Generate `pages-index.md` listing top 5 money pages and their target proof categories.

### Workflow 2: Upgrading a Thin Page (`/seo proof-kb upgrade [slug]`)
1. Scan target page for generic adjectives (*"fast"*, *"reliable"*, *"industry-leading"*).
2. Check `seo/kb/proof/` for matching proof files.
3. If proof files exist, inject the Consensus Proof Card and replace adjectives with measurements.
4. If proof is missing, output an interview question list for the engineering team.

### Workflow 3: Routing a New Fact (`/seo proof-kb route-fact [file]`)
1. When a new benchmark or customer case study is shipped, save it in `seo/kb/proof/`.
2. Inspect `seo/kb/pages-index.md` to identify all money pages and comparison guides referencing that topic.
3. Update each page with the new receipt.
