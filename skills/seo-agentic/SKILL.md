---
name: seo-agentic
description: >-
  Audits and optimizes a website for AI Agent Browsing, Autonomous Assistants,
  and WebMCP readiness. Evaluates Lighthouse Agentic Browsing scores, accessibility tree
  fidelity, ARIA semantic landmarks, interactive form associations, and machine discovery files
  (/.well-known/ai-plugin.json, ai-catalog.json, WebMCP tools).
  Use when the user asks about AI agents browsing the site, Lighthouse Agentic Browsing,
  accessibility for AI, or implementing WebMCP endpoints.
user-invocable: true
argument-hint: "[audit|fix|lighthouse] [target-url-or-path]"
metadata:
  version: "1.0.0"
  category: seo
---

# Agentic Browsing Readiness & WebMCP

AI agents (ChatGPT Operator, Claude in Chrome, Gemini 1.5/2.0 in Chrome, Microsoft Copilot) actively browse the web, compare products, fill out forms, schedule appointments, and complete checkouts on behalf of human users.

**Agent readiness is built on three pillars:**
1. **Flawless Accessibility Tree:** Deterministic DOM nodes, labels, and ARIA roles that agents can inspect without hallucination.
2. **Deterministic Discovery & Machine Manifests:** `llms.txt`, `ai-catalog.json`, and `robots.txt` content policy.
3. **WebMCP & Action Interfaces:** Exposing core business interactions as callable tools for agentic systems.

---

## 1. The Accessibility Tree for Autonomous Agents

Autonomous agents navigate pages through the browser's **Accessibility Tree** rather than visual pixels alone. If an interactive element is an unlabelled `<div>` with an `onClick` listener, agent clicks fail.

### The 5 Agent Accessibility Invariants:
1. **Explicit Semantic Roles:**
   - Every interactive control must be a native `<button>`, `<a href="...">`, or `<input>`.
   - Never use `<div onclick="...">` or `<span class="btn">`.
2. **Unbroken Form Label Associations:**
   - Every input must be tied to a `<label>` via `id` and `for`:
     ```html
     <label for="user-email">Work Email</label>
     <input id="user-email" type="email" name="email" required autocomplete="email" />
     ```
3. **ARIA Landmarks:**
   - Clearly delineate document regions: `<header role="banner">`, `<nav role="navigation">`, `<main role="main">`, `<footer role="contentinfo">`.
4. **Descriptive Interactive Labels:**
   - Icon-only buttons must declare an `aria-label`:
     ```html
     <button type="submit" aria-label="Search Knowledge Base">
       <svg aria-hidden="true">...</svg>
     </button>
     ```
5. **Predictable Focus & State:**
   - Dialogs and modals must implement focus trapping and expose `role="dialog"` with `aria-modal="true"`.

---

## 2. Lighthouse Agentic Browsing Score

Google's Lighthouse Agentic Browsing evaluation assesses how reliably an AI agent can traverse the site and perform critical user tasks.

### Key Evaluation Criteria:
- **TBT (Total Blocking Time) < 200ms:** Agents experience timeouts when heavy client JavaScript freezes the main thread.
- **Form Predictability:** Standard `name`, `type`, and `autocomplete` attributes on all inputs.
- **No CAPTCHA Walls on Read-Only Content:** Do not force anti-bot challenges or proof-of-work gates on public information pages.
- **Clean Fallback Markup:** Server-rendered HTML must provide full navigation links so agents with disabled JS can still traverse the site.

---

## 3. WebMCP Tool Integration (Machine Callable Actions)

For applications that offer search, booking, checkout, or quote generation, WebMCP allows agents to call frontend actions directly without brittle visual scraping.

### Embedding WebMCP Tool Declarations:
Place a WebMCP script in the page `<head>` or expose via `/.well-known/webmcp.json`:

```json
{
  "$schema": "https://webmcp.org/schemas/v1/tool.json",
  "tools": [
    {
      "name": "search_pricing_calculator",
      "description": "Calculate monthly SaaS subscription cost based on active seat count and data volume",
      "parameters": {
        "type": "object",
        "properties": {
          "seats": { "type": "integer", "description": "Number of team member seats" },
          "tier": { "type": "string", "enum": ["starter", "pro", "enterprise"] }
        },
        "required": ["seats", "tier"]
      },
      "endpoint": "/api/pricing/calculate",
      "method": "POST"
    }
  ]
}
```

---

## 4. Agentic Readiness Audit Workflow

When auditing a site or route for agentic readiness:

1. **Accessibility Tree Inspection:**
   - Run DOM query to find unlabelled inputs: `input:not([aria-label]):not([id])`.
   - Verify every link has an `href` attribute.
2. **Form Interaction Check:**
   - Test primary conversion form (signup, checkout, contact). Can an agent autofill using standard autocomplete tokens?
3. **Machine Policy & Manifests:**
   - Verify `/public/llms.txt` exists and returns HTTP 200.
   - Verify `/robots.txt` does not disallow browsing agents.
4. **Generate Code Fixes:**
   - Convert non-semantic clickable elements into standard semantic controls with proper ARIA attributes.
