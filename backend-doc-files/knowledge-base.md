## Knowledge Base

### Ingestion
- Supported sources: Markdown, PDF, HTML, structured data.
- Normalize and segment content with deterministic heuristics.

### Chunking
- Fixed window with overlap to preserve context.
- Store chunk metadata: indices, positions, section titles.

### Embeddings
- Sentence‑Transformer or provider embeddings.
- Store vector id, model, dimension, generated_at.

### Storage
- Documents, chunks in MongoDB.
- Vectors in Pinecone with namespace per environment.