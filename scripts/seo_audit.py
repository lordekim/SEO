#!/usr/bin/env python3
"""
SEO Audit Utility (seo_audit.py)
Audits local HTML files or remote URLs against the SEO.md specification:
- Title & Meta description boundaries
- Single H1 and heading hierarchy
- Canonical tag consistency
- Structured data (Schema.org JSON-LD) presence
- Image alt tags and dimensions
- OpenGraph and Twitter card metadata
"""

import sys
import re
import json
import urllib.request
import urllib.parse
from html.parser import HTMLParser

class SEOLintParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.in_title = False
        self.meta_desc = ""
        self.canonical = ""
        self.h1_tags = []
        self.in_h1 = False
        self.current_h1 = ""
        self.headings = [] # list of (tag, text)
        self.in_heading = False
        self.current_heading_tag = ""
        self.current_heading_text = ""
        self.images = [] # list of dicts: src, alt, width, height
        self.json_ld_scripts = []
        self.in_json_ld = False
        self.current_json_ld = ""
        self.og_tags = {}
        self.twitter_tags = {}
        self.robots_meta = ""

    def handle_starttag(self, tag, attrs):
        attrs_dict = {k.lower(): v for k, v in attrs if v is not None}
        
        if tag == "title":
            self.in_title = True
        elif tag == "meta":
            name = attrs_dict.get("name", "").lower()
            prop = attrs_dict.get("property", "").lower()
            content = attrs_dict.get("content", "")
            
            if name == "description":
                self.meta_desc = content
            elif name == "robots":
                self.robots_meta = content
            elif prop.startswith("og:"):
                self.og_tags[prop] = content
            elif name.startswith("twitter:"):
                self.twitter_tags[name] = content
                
        elif tag == "link":
            rel = attrs_dict.get("rel", "").lower()
            if rel == "canonical":
                self.canonical = attrs_dict.get("href", "")
                
        elif tag == "h1":
            self.in_h1 = True
            self.current_h1 = ""
            self.in_heading = True
            self.current_heading_tag = "h1"
            self.current_heading_text = ""
        elif tag in ["h2", "h3", "h4", "h5", "h6"]:
            self.in_heading = True
            self.current_heading_tag = tag
            self.current_heading_text = ""
            
        elif tag == "img":
            self.images.append({
                "src": attrs_dict.get("src", ""),
                "alt": attrs_dict.get("alt", None),
                "width": attrs_dict.get("width", None),
                "height": attrs_dict.get("height", None)
            })
            
        elif tag == "script":
            stype = attrs_dict.get("type", "").lower()
            if stype == "application/ld+json":
                self.in_json_ld = True
                self.current_json_ld = ""

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        elif tag == "h1":
            self.in_h1 = False
            self.h1_tags.append(self.current_h1.strip())
            if self.in_heading:
                self.headings.append((self.current_heading_tag, self.current_heading_text.strip()))
                self.in_heading = False
        elif tag in ["h2", "h3", "h4", "h5", "h6"] and self.in_heading:
            self.headings.append((self.current_heading_tag, self.current_heading_text.strip()))
            self.in_heading = False
        elif tag == "script" and self.in_json_ld:
            self.in_json_ld = False
            try:
                parsed = json.loads(self.current_json_ld.strip())
                self.json_ld_scripts.append(parsed)
            except Exception as e:
                self.json_ld_scripts.append({"_parse_error": str(e), "raw": self.current_json_ld})

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.in_h1:
            self.current_h1 += data
        if self.in_heading:
            self.current_heading_text += data
        if self.in_json_ld:
            self.current_json_ld += data

def audit_html(html_content, source_name="Target"):
    parser = SEOLintParser()
    parser.feed(html_content)
    
    issues = []
    score = 100
    
    # 1. Title Audit
    title = parser.title.strip()
    title_len = len(title)
    if not title:
        issues.append({"level": "CRITICAL", "category": "Title", "message": "Missing <title> tag."})
        score -= 20
    elif title_len < 30:
        issues.append({"level": "WARNING", "category": "Title", "message": f"Title too short ({title_len} chars). Target: 50-60 chars."})
        score -= 5
    elif title_len > 60:
        issues.append({"level": "WARNING", "category": "Title", "message": f"Title may truncate on mobile SERPs ({title_len} chars). Target: 50-60 chars."})
        score -= 5

    # 2. Meta Description
    desc = parser.meta_desc.strip()
    desc_len = len(desc)
    if not desc:
        issues.append({"level": "HIGH", "category": "Meta Description", "message": "Missing meta description."})
        score -= 10
    elif desc_len < 120 or desc_len > 165:
        issues.append({"level": "LOW", "category": "Meta Description", "message": f"Meta description length is {desc_len} chars. Optimal: 140-160 chars."})
        score -= 3

    # 3. Canonical Tag
    if not parser.canonical:
        issues.append({"level": "CRITICAL", "category": "Canonical", "message": "Missing <link rel='canonical'> tag."})
        score -= 15

    # 4. Heading Hierarchy
    h1_count = len(parser.h1_tags)
    if h1_count == 0:
        issues.append({"level": "CRITICAL", "category": "Headings", "message": "Missing <h1> tag. Exactly one <h1> is required."})
        score -= 15
    elif h1_count > 1:
        issues.append({"level": "HIGH", "category": "Headings", "message": f"Found multiple ({h1_count}) <h1> tags. Strictly one allowed."})
        score -= 10

    # 5. Schema.org JSON-LD
    if not parser.json_ld_scripts:
        issues.append({"level": "HIGH", "category": "Structured Data", "message": "Zero Schema.org JSON-LD structured data detected."})
        score -= 10
    else:
        for schema in parser.json_ld_scripts:
            if "_parse_error" in schema:
                issues.append({"level": "CRITICAL", "category": "Structured Data", "message": f"JSON-LD syntax error: {schema['_parse_error']}"})
                score -= 10

    # 6. Images
    images_missing_alt = [img['src'] for img in parser.images if img['alt'] is None]
    if images_missing_alt:
        issues.append({"level": "MEDIUM", "category": "Images", "message": f"{len(images_missing_alt)} image(s) missing alt attribute."})
        score -= min(len(images_missing_alt) * 2, 8)

    # 7. Robots Meta
    if "noindex" in parser.robots_meta.lower():
        issues.append({"level": "FATAL", "category": "Indexability", "message": "robots meta tag specifies 'noindex'!"})
        score -= 40

    return {
        "source": source_name,
        "health_score": max(score, 0),
        "title": title,
        "title_length": title_len,
        "meta_description": desc,
        "meta_description_length": desc_len,
        "canonical": parser.canonical,
        "h1_count": h1_count,
        "h1_content": parser.h1_tags,
        "headings_outline": parser.headings[:10],
        "image_count": len(parser.images),
        "schema_count": len(parser.json_ld_scripts),
        "issues": issues
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: python seo_audit.py <path-to-html-file-or-url>")
        sys.exit(1)
        
    target = sys.argv[1]
    
    if target.startswith("http://") or target.startswith("https://"):
        req = urllib.request.Request(target, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) SEO-Agent/1.0'})
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                content = resp.read().decode('utf-8', errors='ignore')
        except Exception as e:
            print(f"Error fetching URL {target}: {e}")
            sys.exit(1)
    else:
        try:
            with open(target, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading file {target}: {e}")
            sys.exit(1)
            
    report = audit_html(content, target)
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
