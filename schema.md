---
layout: default
title: Schema
description: Database and data model schema definitions
permalink: /schema/
---

<link rel="stylesheet" href="/assets/style.css">
{% include nav.html %}

# Schema

## Core Collections
- `users`: profiles, roles, and auth metadata.
- `sessions`: chat sessions with context and timestamps.
- `knowledge_base_documents`: source documents with metadata.
- `knowledge_base_chunks`: chunked content with embeddings and indexes.

## Embedding Metadata
- Model name, dimension, vector id.
- Generation timestamp and chunk context.

## Indexes
- Unique ids, compound indexes for fast retrieval.