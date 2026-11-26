<div align="center">

# Autonomous SEO & GEO Skillset for AI Agents

**Production-grade SEO & Generative Engine Optimization (GEO) skills for Antigravity, Claude Code, Cursor, Codex, and AI Coding Agents.**

Rank at the top of Google & Bing · Secure citations in Google AI Overviews, Perplexity, ChatGPT Search, Claude & Gemini.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills: 12 Modules](https://img.shields.io/badge/Skills-12%20Specialized%20Modules-brightgreen.svg)](.agents/skills/)
[![Standard: Agent Skills](https://img.shields.io/badge/Standard-Agent%20Skills%20Spec-purple.svg)](https://agentskills.io)
[![MCP: Ryze Connected](https://img.shields.io/badge/MCP-Ryze%20%2F%20GSC%20%2F%20GA4-orange.svg)](#live-data--mcp-integration)

</div>

---

## Overview

This repository provides an autonomous, end-to-end SEO skillset engineered for agentic pair-programmers and autonomous developers. It turns your AI agent into an experienced **Principal Technical SEO Architect, Content Strategist, and Search Experience Engineer**.

Synthesized from enterprise production standards and the best open-source AI agent SEO repositories:
- **[AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)**: Multi-agent orchestration, 9-category technical audits, 0–100 scoring rubrics, Core Web Vitals, Agentic Browsing (Lighthouse), and Schema.org graphs.
- **[Illyism/seo-skills](https://github.com/Illyism/seo-skills)**: Fatal-first revenue triage (`Fatal -> Revenue -> Compounding -> Fluff`), 20-point anti-AI slop editing (`unslop-seo`), and atomic first-hand proof knowledge bases (`seo/kb/`).
- **[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)**: Search intent classification, programmatic SEO defensibility (30% unique content rule), topic cluster siloing, and bottom-of-funnel comparison pages (`vs-and-alternatives`).
- **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)**: Live search data via MCP, real GA4 AI referral tracking (ChatGPT, Perplexity, Gemini, Claude), and striking-distance query hunting (#4–#15).

---

## Repository Architecture

```
.
├── SEO.md                                 # Master Autonomous SEO Specification & Agent Playbook
├── README.md                              # Repository Documentation & Setup Guide
├── .agents/skills/                        # Native Antigravity Discovery Root
│   ├── seo/SKILL.md                       # Master Orchestrator & CLI Router (/seo)
│   ├── seo-audit/SKILL.md                 # 9-Category Technical & Core Web Vitals Audit
│   ├── seo-roast/SKILL.md                 # Fatal-First Revenue Teardown (Ends in PR code fixes)
│   ├── seo-geo/SKILL.md                   # Generative Engine Optimization & llms.txt
│   ├── seo-agentic/SKILL.md               # AI Agent Browsing Readiness & WebMCP
│   ├── seo-schema/SKILL.md                # Interconnected Schema.org JSON-LD Knowledge Graph
│   ├── seo-content/SKILL.md               # High-Information Gain Content & Structured Briefs
│   ├── unslop-seo/SKILL.md                # 20-Point Anti-AI Slop Editor (Mechanism over Feeling)
│   ├── seo-proof-kb/SKILL.md              # First-Hand Proof Store (seo/kb/) & Proof Cards
│   ├── seo-programmatic/SKILL.md          # Database-Driven Scaled Pages & Anti-Doorway Guardrails
│   ├── seo-competitor-pages/SKILL.md      # High-Converting [Brand] vs [Competitor] Pages
│   ├── seo-internal-linking/SKILL.md      # Topic Clusters, PageRank Flow & 3-Click Crawl Depth
│   └── seo-analytics-mcp/SKILL.md         # Live GSC/GA4 Data, AI Referrals & Rank Tracking
├── skills/                                # Universal Mirrored Root (Claude Code, Cursor, Codex)
├── templates/                             # Production-Ready Configuration & Markup Templates
│   ├── robots.txt.template                # Production Robots.txt with Generative AI Policies
│   ├── llms.txt.template                  # Standard /public/llms.txt AI Engine Manifest
│   ├── schema-graph.json.template         # Interconnected @graph Schema.org JSON-LD
│   ├── brand-ssot.md.template             # Single Source of Truth for verifiable metrics
│   └── pages-index.md.template            # Mapping of money pages to required proof files
└── scripts/                               # Python Automation Utilities
    ├── seo_audit.py                       # Automated Title/Meta/H1/Canonical/Schema Linter
    └── unslop_checker.py                  # Automated 20-Point AI Slop & Buzzword Scanner
```

---

## The 12 Modular Skills

| Skill | Role & Focus | Command |
| :--- | :--- | :--- |
| **[`seo`](.agents/skills/seo/SKILL.md)** | **Master Orchestrator:** Automatically detects business archetype (SaaS, E-commerce, Local Service, Publisher, DevTool) and routes execution. | `/seo [cmd] [target]` |
| **[`seo-roast`](.agents/skills/seo-roast/SKILL.md)** | **Fatal-First Teardown:** Triages issues into `FATAL -> REVENUE -> COMPOUNDING -> FLUFF`. Blocks indexing self-owns and generates direct PR code fixes. | `/seo roast [target]` |
| **[`seo-audit`](.agents/skills/seo-audit/SKILL.md)** | **9-Category Technical Audit:** Evaluates Crawlability, Canonicalization, Rendering (SSR/SSG), Semantic HTML, Metadata, Schema, CWV (LCP/INP/CLS), Media, and Hreflang with 0–100 score. | `/seo audit [target]` |
| **[`seo-geo`](.agents/skills/seo-geo/SKILL.md)** | **AI Citability (GEO & LLMO):** Inverted pyramid direct answers (40–60 words under H2), HTML `<table>` density, entity disambiguation, and `/public/llms.txt`. | `/seo geo [target]` |
| **[`seo-agentic`](.agents/skills/seo-agentic/SKILL.md)** | **Agent Readiness:** Accessibility Tree optimization, form autofill tokens, ARIA landmarks, and WebMCP machine-callable action endpoints. | `/seo agentic [target]` |
| **[`seo-schema`](.agents/skills/seo-schema/SKILL.md)** | **Structured Data:** Interconnected `@graph` linking `#organization`, `#website`, `#author` (Person E-E-A-T), and `SoftwareApplication` / `Product` / `FAQPage` with Next.js & Astro recipes. | `/seo schema [target]` |
| **[`unslop-seo`](.agents/skills/unslop-seo/SKILL.md)** | **Anti-AI Slop:** 20-point slop purge. Replaces feeling words (*"blazing-fast"*, *"seamless"*) with measured mechanisms (*"sub-5ms p99 latency"*). | `/seo unslop [file]` |
| **[`seo-proof-kb`](.agents/skills/seo-proof-kb/SKILL.md)** | **First-Hand Proof Store:** Stacks 4+ proof categories (benchmarks, customer migrations, terminal traces, unit economics) and injects uncopyable Consensus Proof Cards. | `/seo proof-kb [action]` |
| **[`seo-content`](.agents/skills/seo-content/SKILL.md)** | **High-Information Gain Content:** Search intent classification, structured content briefs, heading outlines, and content decay revitalization. | `/seo content [topic]` |
| **[`seo-programmatic`](.agents/skills/seo-programmatic/SKILL.md)** | **Scale Without Penalties:** Enforces the 30% unique content rule, conditional noindex for sparse records, and partitioned sub-sitemaps ($\le 10,000$ URLs). | `/seo programmatic [plan]` |
| **[`seo-competitor-pages`](.agents/skills/seo-competitor-pages/SKILL.md)** | **Bottom-of-Funnel Conversion:** `[Brand] vs [Competitor]` matrices, Reddit/community sentiment answers, and 3-step migration workflows. | `/seo vs-pages [brand] [comp]` |
| **[`seo-internal-linking`](.agents/skills/seo-internal-linking/SKILL.md)** | **PageRank Flow:** Topic cluster siloing, 3-click crawl depth rules, descriptive anchor text matrices, and trailing-slash normalization. | `/seo links [target]` |
| **[`seo-analytics-mcp`](.agents/skills/seo-analytics-mcp/SKILL.md)** | **Live MCP Data:** Connects Search Console and GA4 via Ryze MCP. Tracks actual AI referral sessions (ChatGPT, Perplexity, Gemini, Claude) and hunts striking-distance queries (#4–#15). | `/seo data [action]` |

---

## Quick Start & Installation

### Option 1: In Google Antigravity (Native Discovery)
Antigravity automatically discovers customizations stored in `.agents/skills/`:
1. Clone or copy this repository into your project workspace.
2. The skills are instantly available. Ask Antigravity:
   > *"Run an SEO audit on our pricing page"* or *"/seo roast app/pricing/page.tsx"*

### Option 2: In Claude Code
Copy the skills into your project or Claude's global skills directory:
```bash
# Workspace level (Claude Code discovers ./skills or ./.agents/skills):
git clone https://github.com/your-username/seo-skillset.git

# Or copy into Claude's global skills:
cp -r .agents/skills/* ~/.claude/skills/
```

### Option 3: In Cursor, Windsurf, or Codex
Cursor and other agent environments discover skills located in `.agents/skills/` or `.cursor/skills/`.

---

## Live Data & MCP Integration

Connect real Search Console, GA4, and Google Ads data without paid SaaS subscriptions:

```bash
# Add the free Ryze MCP connector to Claude Code:
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

Once connected, execute live queries:
- **Track AI Referrals:** Measure real session volume and conversions originating from `chatgpt.com`, `perplexity.ai`, `gemini.google.com`, and `claude.ai`.
- **Striking Distance Queries:** Uncover queries ranked #4–#15 with $\ge$ 500 impressions ready for page-1 optimization.
- **CTR Anomalies:** Identify high-ranking queries underperforming expected click-through rates.

---

## Automation Scripts

Lightweight, dependency-free Python scripts are bundled in `scripts/`:

### 1. Automated SEO Linter (`seo_audit.py`)
Scans any local HTML file or live URL for single H1 integrity, title pixel widths, meta description boundaries, canonical tags, schema JSON-LD, missing image alt tags, and robots directives:
```bash
python scripts/seo_audit.py https://yourdomain.com
# Or audit a local build file:
python scripts/seo_audit.py dist/index.html
```

### 2. 20-Point Anti-AI Slop Scanner (`unslop_checker.py`)
Scans markdown, MDX, TSX, or HTML files for robotic filler, preambles, and puffery adjectives:
```bash
python scripts/unslop_checker.py content/blog/
```

---

## Core Operating Tenets & Safety Rails

Every agent using this skillset enforces these five invariant rules:
1. **Preserve Search Equity:** Never alter an existing URL slug without provisioning an immutable **301 Permanent Redirect**.
2. **Fatal First, Fluff Never:** Never spend hours optimizing meta tags while a `noindex` or broken canonical kills an indexable revenue page.
3. **Deterministic Canonicalization:** Every page outputs an explicit self-referential canonical URL with normalized trailing slashes.
4. **Information Gain & Grounding:** Ban generic AI filler. Ground all claims in real codebase facts, benchmarks, and production receipts.
5. **No Hallucinated Schema:** Only output Schema.org fields that accurately reflect verifiable data visibly rendered on the page.

---

## License

MIT License. Free to use, adapt, and integrate into client projects or commercial agents.
