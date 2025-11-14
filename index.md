---
layout: default
title: AI Chatbot Support Service
description: Enterprise-Grade Customer Support AI Platform - Technical Documentation
---

<link rel="stylesheet" href="/assets/style.css">
{% include nav.html %}

## Documentation

- [Overview](/overview/)
- [Architecture](/architecture/)
- [Technical Implementation](/technical-implementation/)
- [Schema](/schema/)
- [Usage](/usage/)

Maintained by bluntjoint — Rishabh A.

<!-- Mermaid support for rendering diagrams -->
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script>
  mermaid.initialize({ 
    startOnLoad: true, 
    theme: 'neutral',
    securityLevel: 'loose',
    flowchart: {
      useMaxWidth: true,
      htmlLabels: true,
      curve: 'basis'
    }
  });
  
  // Convert fenced code blocks with language-mermaid
  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('pre > code.language-mermaid').forEach(function (code) {
      var pre = code.parentElement;
      var container = document.createElement('div');
      container.className = 'mermaid';
      container.textContent = code.textContent;
      pre.parentElement.replaceChild(container, pre);
    });
  });
  
  // Handle different markdown renderers
  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('code.language-mermaid').forEach(function (code) {
      if (code.parentElement && code.parentElement.tagName.toLowerCase() !== 'pre') {
        var container = document.createElement('div');
        container.className = 'mermaid';
        container.textContent = code.textContent;
        code.parentElement.replaceChild(container, code);
      }
    });
  });
</script>
