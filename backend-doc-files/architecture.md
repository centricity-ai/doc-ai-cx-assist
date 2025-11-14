## Architecture

### High‑Level
- Client applications connect via API gateway.
- Core services: chat, knowledge base, embeddings.
- Storage: MongoDB (documents, sessions), Pinecone (vectors).
- Observability: metrics and dashboards.

### Data Flow
- Ingest → chunk → embed → index.
- Retrieve relevant chunks → assemble context → call LLM adapter.

### Deployment
- Containerized services; Kubernetes manifests for scaling.
- Environment via `.env` and settings modules.