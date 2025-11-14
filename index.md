---
layout: default
title: AI Chatbot Support Service
description: Enterprise-Grade Customer Support AI Platform - Technical Documentation
---

<link rel="stylesheet" href="/assets/style.css">
 
## Contents

{:toc}

{% include_relative backend-doc-files/overview.md %}
{% include_relative backend-doc-files/architecture.md %}
{% include_relative backend-doc-files/designs.md %}
{% include_relative backend-doc-files/execution-logic.md %}
{% include_relative backend-doc-files/knowledge-base.md %}
{% include_relative backend-doc-files/ai-interaction.md %}
{% include_relative backend-doc-files/validations.md %}
{% include_relative backend-doc-files/usage.md %}

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
