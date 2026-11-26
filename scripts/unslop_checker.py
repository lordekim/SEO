#!/usr/bin/env python3
"""
Anti-AI Slop Checker (unslop_checker.py)
Scans markdown, MDX, TSX, HTML, or plain text files for the 20 AI slop patterns:
- Epochal preambles
- Pompous verbs (delve into, harness, unleash)
- Puffery adjectives (seamless, blazing-fast, game-changing, revolutionary)
- Formulaic transitions (furthermore, moreover, it is worth noting)
- Cliché metaphors (double-edged sword, testament to)
Outputs line numbers, matched phrases, and suggested fixes.
"""

import sys
import re
import os

SLOP_PATTERNS = [
    # 1. Epochal preambles
    (r"\b(in today'?s (?:fast-paced|digital|modern|rapidly changing|ever-evolving) (?:world|age|landscape|era))\b", 
     "Epochal Preamble", "Delete entire phrase; start directly with core fact."),
    
    # 2. Rhetorical Questions
    (r"\b(have you ever wondered (?:how|what|why))\b", 
     "Rhetorical Question", "Delete and replace with a declarative assertion."),
    (r"\b(looking to (?:take your|elevate your|supercharge your))\b",
     "Rhetorical Question", "State exact technical solution directly."),
     
    # 3. Pompous Verbs
    (r"\b(delve(?:s|d|ing)? into)\b", 
     "Pompous Verb", "Use: analyze, inspect, examine, review, configure."),
    (r"\b(unleash(?:es|ed|ing)? (?:the (?:power|potential))?)\b", 
     "Pompous Verb", "Use: enable, deploy, run, activate."),
    (r"\b(harness(?:es|ed|ing)? (?:the (?:power|potential))?)\b", 
     "Pompous Verb", "Use: use, utilize, apply, execute."),
    (r"\b(embark(?:s|ed|ing)? on a journey)\b", 
     "Pompous Verb", "Delete; state the operational task."),
     
    # 4. Puffery Adjectives
    (r"\b(seamless(?:ly)?)\b", 
     "Puffery Adjective", "Replace with exact mechanism (e.g. 'zero-downtime', 'single-command')."),
    (r"\b(blazing(?:ly)?-?fast)\b", 
     "Puffery Adjective", "Replace with exact benchmark latency (e.g. 'sub-5ms p99')."),
    (r"\b(game-?changing)\b", 
     "Puffery Adjective", "Delete or state measurable delta (e.g. 'cuts compute by 34%')."),
    (r"\b(revolutionary)\b", 
     "Puffery Adjective", "Delete adjective; let technical benchmarks speak."),
    (r"\b(cutting-?edge|state-?of-?the-?art)\b", 
     "Puffery Adjective", "Name specific version or standard (e.g. 'PostgreSQL 16', 'HTTP/3')."),
     
    # 5. Metaphor Crutches
    (r"\b(double-edged sword)\b", 
     "Metaphor Crutch", "Explain specific architectural trade-off."),
    (r"\b(testament to)\b", 
     "Metaphor Crutch", "Replace with concrete evidence or metric."),
    (r"\b(tip of the iceberg)\b", 
     "Metaphor Crutch", "State actual scope or additional capabilities."),
    (r"\b(beacon of (?:hope|light))\b", 
     "Metaphor Crutch", "Delete hyperbolic metaphor."),
     
    # 6. Formulaic Transitions
    (r"\b(it is worth noting that)\b", 
     "Formulaic Transition", "Delete phrase; state the fact directly."),
    (r"\b(furthermore|moreover)\b", 
     "Formulaic Transition", "Delete; connect thoughts by logical idea flow."),
    (r"\b(needless to say)\b", 
     "Formulaic Transition", "If needless to say, delete the sentence."),
     
    # 7. Hollow Summaries
    (r"\b(in conclusion|to wrap it up|all in all)\b", 
     "Hollow Summary", "Replace with actionable 'Next Steps' or code snippet."),
    (r"\b(only time will tell)\b", 
     "Hollow Summary", "State the projected engineering trade-off."),
     
    # 8. AI Throat-Clearing
    (r"\b(without further ado|let'?s dive right in)\b", 
     "AI Throat-Clearing", "Delete immediately.")
]

def scan_file(filepath):
    hits = []
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        
    for idx, line in enumerate(lines, start=1):
        for pattern, category, recommendation in SLOP_PATTERNS:
            matches = re.finditer(pattern, line, re.IGNORECASE)
            for m in matches:
                hits.append({
                    "line": idx,
                    "matched": m.group(0),
                    "category": category,
                    "recommendation": recommendation,
                    "context": line.strip()
                })
    return hits

def main():
    if len(sys.argv) < 2:
        print("Usage: python unslop_checker.py <file-or-directory-path>")
        sys.exit(1)
        
    target_path = sys.argv[1]
    files_to_scan = []
    
    if os.path.isdir(target_path):
        for root, _, files in os.walk(target_path):
            for file in files:
                if file.endswith(('.md', '.mdx', '.txt', '.html', '.tsx', '.ts', '.astro')):
                    files_to_scan.append(os.path.join(root, file))
    else:
        files_to_scan.append(target_path)
        
    total_hits = 0
    print(f"Scanning {len(files_to_scan)} file(s) for AI slop patterns...\n" + "="*60)
    
    for fpath in files_to_scan:
        file_hits = scan_file(fpath)
        if file_hits:
            print(f"\n📄 {fpath} ({len(file_hits)} hits):")
            for h in file_hits:
                total_hits += 1
                print(f"  Line {h['line']}: [{h['category']}] '{h['matched']}'")
                print(f"    Context: {h['context']}")
                print(f"    Fix: {h['recommendation']}")
                
    print("\n" + "="*60)
    print(f"Scan complete. Found {total_hits} AI slop trigger(s).")
    if total_hits > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()
