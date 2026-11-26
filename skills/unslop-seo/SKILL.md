---
name: unslop-seo
description: >-
  Executes an in-place editorial anti-AI slop pass across articles, landing pages,
  documentation, and marketing copy. Strips 20 common AI filler patterns, removes adjective puffery,
  replaces vague feelings with concrete technical mechanisms, and optimizes opening passages
  for direct answer engine citation (Google AI Overviews, Perplexity).
  Use when editing AI drafts, cleaning marketing text, removing buzzwords,
  or grounding claims in verifiable codebase facts.
user-invocable: true
argument-hint: "[target-file-or-path]"
metadata:
  version: "1.0.0"
  category: seo
---

# Anti-AI Slop & Editorial Grounding (`unslop-seo`)

AI-generated copy fails twice: human readers recognize the robotic filler and bounce, while AI answer engines skip the long-winded preamble and fail to quote the answer.

This skill runs a strict 3-phase editorial pass on Markdown, MDX, TSX, and HTML files:
1. **Ground the Facts:** Replace feeling words with verifiable mechanisms and numbers.
2. **Structure for Citations:** Place direct answers in the first 40 words under headings.
3. **Strip the 20 Slop Patterns:** Purge formulaic AI prose.

---

## Phase 1: Mechanism Over Feeling (Fact Grounding)

Never describe how software or architecture *feels*; describe how it *works*:

| Robotic / Slop Phrasing | Grounded Technical Mechanism |
| :--- | :--- |
| *"Our blazing-fast build system ensures seamless developer experience."* | *"Our build pipeline compiles 1,400 MDX routes in 1.8 seconds using Turbopack with parallel AST caching."* |
| *"We offer enterprise-grade security and bulletproof reliability."* | *"We provide SOC2 Type II compliance, TLS 1.3 encryption at rest, and automated blue-green rollouts with 99.99% uptime SLA."* |
| *"The database stays close at hand for lightning-fast queries."* | *"Read replicas in 12 global regions maintain p99 read latencies under 4.2ms via memory-mapped NVMe storage."* |

> **The Verification Rule:** If a claim cannot be verified from the codebase, pricing page, or `seo/kb/brand-ssot.md`, do not guess. Insert `<!-- [NEEDS FACT: specific metric] -->` and delete the unverified adjective.

---

## Phase 2: The 20-Point AI Slop Purge Table

Search the target file and eliminate every instance of these 20 patterns:

| # | Slop Category | Banned Phrases / Patterns | Replacement Rule |
|---|---|---|---|
| 1 | **Epochal Preamble** | *"In today's fast-paced digital world...", "In the ever-evolving landscape of..."* | Delete entire sentence. Start directly with the core thesis. |
| 2 | **Rhetorical Questions** | *"Have you ever wondered how...", "Looking to take your X to the next level?"* | Delete. Replace with a declarative assertion or problem statement. |
| 3 | **Pompous Verbs** | *"Delve into", "embark on", "unleash", "harness the power of", "elevate"* | Use plain operational verbs: *configure, test, deploy, measure, compile*. |
| 4 | **Puffery Adjectives** | *"Seamless", "blazing-fast", "game-changing", "revolutionary", "cutting-edge", "state-of-the-art"* | Delete adjective or replace with measured benchmarks (e.g., `3.2ms`). |
| 5 | **Metaphor Crutches** | *"Double-edged sword", "testament to", "tip of the iceberg", "beacon of hope"* | State the exact trade-off or technical limitation literally. |
| 6 | **Formulaic Transitions** | *"Moreover", "Furthermore", "Additionally", "It is worth noting that"* | Delete transition. Modern technical prose flows through logical ideas. |
| 7 | **Hollow Summaries** | *"In conclusion...", "All in all...", "Ultimately, only time will tell..."* | Replace with an actionable "Next Steps" checklist or code sample. |
| 8 | **Passive Evasions** | *"It is widely considered that...", "Studies suggest that..."* | Name the exact researcher, company, or benchmark test. |
| 9 | **Symmetrical Trios** | Forcing concepts into groups of three parallel adjectives (*"fast, reliable, and secure"*) | Cut down to the single most critical differentiator. |
| 10 | **Em-Dash Overload** | Littering every paragraph with 3+ em-dashes (`—`) | Break into clean, standalone sentences. |
| 11 | **Bland Synonyms for "Important"**| *"Crucial", "pivotal", "paramount", "vital", "essential"* | Explain the consequence: *"Skipping this causes database deadlocks."* |
| 12 | **Preachy Cheerleading** | *"Remember, consistency is key!", "Happy coding!"* | Delete entirely. Respect the reader's professional time. |
| 13 | **Echo Headings** | Headings that rephrase the intro: *"Introduction to What We Will Cover"* | Use specific topic noun phrases: *"Multi-Region Failover Architecture"*. |
| 14 | **Empty Intensifiers** | *"Very", "extremely", "incredibly", "truly"* | Delete intensifier. |
| 15 | **False Balance** | Giving equal weight to outdated practices out of politeness | Give a clear engineering verdict based on modern standards. |
| 16 | **Generic Definitions** | Starting a high-level guide with elementary dictionary definitions | Assume target audience competency; define only novel terms. |
| 17 | **Vague Proof** | *"Thousands of happy developers love our tool"* | *"Used by 4,200 engineering teams across 80 countries."* |
| 18 | **AI Throat-Clearing** | *"Let's dive right in!", "Without further ado..."* | Delete immediately. |
| 19 | **Over-Formatted Bold Lists** | Every single bullet point begins with a bolded buzzword followed by a colon | Use natural sentence prose or tables. |
| 20 | **"Not Only X, But Y"** | *"Not only does it save time, but it also increases revenue"* | State the primary value directly: *"It cuts monthly AWS compute by 34%."* |

---

## Phase 3: Structural Direct-Answer Pass

After purging slop, verify the structure:
1. **First 40 Words:** Does the opening paragraph immediately define what the page solves without preamble?
2. **Buyer Question Headings:** Are at least two `<h2>` headings phrased as natural buyer questions (e.g., *"How does memory-mapping prevent read latency spikes?"*)?
3. **Self-Contained Evaluation Blocks:** If comparing alternatives, does each section follow a consistent rubric:
   - **Verdict:** One-sentence summary.
   - **Best For:** Target team or architecture.
   - **Trade-Offs:** The real drawback or missing feature.
   - **Pricing:** Exact dollars or free tier limits.
