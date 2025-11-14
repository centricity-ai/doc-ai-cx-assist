#!/usr/bin/env python3
"""
Documentation Generator for AI Chatbot Support Service
Consolidates all documentation files into a single comprehensive index.md
"""

import os
import re
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent

# Source files
README_FILE = BASE_DIR / "README.md"
BACKEND_DOC_DIR = BASE_DIR / "backend-doc-files"

# Output file
OUTPUT_FILE = BASE_DIR / "index.md"

# Front matter for Just the Docs
FRONT_MATTER = """---
layout: default
title: AI Chatbot Support Service
nav_order: 1
description: "Enterprise-Grade Customer Support AI Platform with RAG, Multi-LLM Support & Semantic Search"
permalink: /
---

"""

# Hero section
HERO_SECTION = """<div class="hero" markdown="1">

# AI Chatbot Support Service
{: .fs-10 .fw-700 .text-center }

Enterprise-Grade Customer Support AI Platform with RAG, Multi-LLM Support & Semantic Search
{: .fs-6 .fw-300 .text-center }

Build intelligent customer support experiences powered by AWS Bedrock, Azure OpenAI, Pinecone vector search, and Django. This comprehensive platform provides semantic search across knowledge bases, context-aware conversations, and production-ready infrastructure with full observability.
{: .fs-5 .fw-300 .text-center }

[Get Started](#getting-started){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[View on GitHub](https://github.com/centricity-ai/doc-ai-cx-assist){: .btn .btn-outline .fs-5 .mb-4 .mb-md-0 }

</div>

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

"""

# Footer with Mermaid initialization
FOOTER = """

---

**Last Updated**: January 14, 2025
**Documentation Version**: 2.0.0
**System Version**: 1.0.0

<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<script>
mermaid.initialize({
  startOnLoad: true,
  theme: 'dark',
  themeVariables: {
    primaryColor: '#21262d',
    primaryTextColor: '#c9d1d9',
    primaryBorderColor: '#58a6ff',
    lineColor: '#58a6ff',
    secondaryColor: '#161b22',
    tertiaryColor: '#0d1117'
  }
});
</script>
"""


def clean_content(content: str) -> str:
    """Clean and format content for Just the Docs"""
    # Remove any existing front matter
    content = re.sub(r'^---[\s\S]*?---\n*', '', content)

    # Add Just the Docs styling to headers
    lines = content.split('\n')
    formatted_lines = []

    for i, line in enumerate(lines):
        # Add spacing classes to level 2 headers
        if line.strip().startswith('## ') and not line.strip().startswith('###'):
            formatted_lines.append(line)
            formatted_lines.append('{: .fs-9 }')
            formatted_lines.append('')
        # Add spacing to level 3 headers
        elif line.strip().startswith('### ') and not line.strip().startswith('####'):
            formatted_lines.append(line)
            formatted_lines.append('{: .fs-7 }')
            formatted_lines.append('')
        # Add spacing to level 4 headers
        elif line.strip().startswith('#### '):
            formatted_lines.append(line)
            formatted_lines.append('{: .fs-6 }')
            formatted_lines.append('')
        else:
            formatted_lines.append(line)

    return '\n'.join(formatted_lines)


def add_api_labels(content: str) -> str:
    """Add Just the Docs labels to API methods"""
    # Add labels for HTTP methods
    content = re.sub(
        r'(\*\*Method:\*\* )(GET)',
        r'{: .label .label-green }\n\2\n\n**Endpoint:**',
        content
    )
    content = re.sub(
        r'(\*\*Method:\*\* )(POST)',
        r'{: .label .label-blue }\n\2\n\n**Endpoint:**',
        content
    )
    content = re.sub(
        r'(\*\*Method:\*\* )(PUT)',
        r'{: .label .label-yellow }\n\2\n\n**Endpoint:**',
        content
    )
    content = re.sub(
        r'(\*\*Method:\*\* )(DELETE)',
        r'{: .label .label-red }\n\2\n\n**Endpoint:**',
        content
    )

    return content


def add_callouts(content: str) -> str:
    """Convert blockquotes to Just the Docs callouts where appropriate"""
    # This is a simple implementation - you can make it more sophisticated
    lines = content.split('\n')
    formatted_lines = []
    in_blockquote = False
    blockquote_lines = []

    for line in lines:
        if line.strip().startswith('> '):
            if not in_blockquote:
                in_blockquote = True
                blockquote_lines = []
            blockquote_lines.append(line[2:].strip())  # Remove '> '
        else:
            if in_blockquote:
                # Determine callout type based on content
                full_text = ' '.join(blockquote_lines)
                if any(word in full_text.lower() for word in ['note', 'info', 'remember']):
                    formatted_lines.append('{: .note }')
                elif any(word in full_text.lower() for word in ['warning', 'caution', 'careful']):
                    formatted_lines.append('{: .warning }')
                elif any(word in full_text.lower() for word in ['important', 'critical', 'must']):
                    formatted_lines.append('{: .important }')
                elif any(word in full_text.lower() for word in ['tip', 'pro tip', 'best practice']):
                    formatted_lines.append('{: .tip }')
                else:
                    formatted_lines.append('{: .highlight }')

                # Add blockquote lines
                for bq_line in blockquote_lines:
                    formatted_lines.append(f'> {bq_line}')
                formatted_lines.append('')

                in_blockquote = False
                blockquote_lines = []

            formatted_lines.append(line)

    return '\n'.join(formatted_lines)


def generate_documentation():
    """Generate comprehensive consolidated documentation"""
    print("Generating comprehensive documentation...")

    # Read README.md
    print(f"Reading {README_FILE}...")
    with open(README_FILE, 'r', encoding='utf-8') as f:
        readme_content = f.read()

    # Clean and format content
    readme_content = clean_content(readme_content)
    readme_content = add_api_labels(readme_content)
    readme_content = add_callouts(readme_content)

    # Combine all content
    print("Combining content...")
    full_content = FRONT_MATTER + HERO_SECTION + readme_content + FOOTER

    # Write output file
    print(f"Writing to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(full_content)

    print(f"✅ Documentation generated successfully!")
    print(f"   Output: {OUTPUT_FILE}")
    print(f"   Size: {len(full_content):,} characters")
    print(f"   Lines: {len(full_content.splitlines()):,}")


if __name__ == "__main__":
    generate_documentation()
