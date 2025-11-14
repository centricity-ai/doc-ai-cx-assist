---
layout: default
title: Technical Implementation
description: Implementation details, modules, and interfaces
permalink: /technical-implementation/
---

<link rel="stylesheet" href="/assets/style.css">
{% include nav.html %}

# Technical Implementation

## Services
- Chat service orchestrates conversations and state.
- Knowledge base service processes documents and indexing.
- Embeddings service generates and manages vectors.

## Integrations
- Provider adapters for Azure OpenAI and AWS Bedrock.
- External adapters (e.g., storage, analytics) via interfaces.

## APIs
- REST endpoints for sessions, chat, documents.
- Swagger docs available at `/api/docs/` when running locally.

## Observability
- Metrics and dashboards for performance and reliability.