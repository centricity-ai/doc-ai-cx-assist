## Execution Logic

### Request Handling
- Validate input (length, profanity, PII) before processing.
- Resolve session and user context.

### Retrieval Augmented Generation
- Expand query with synonyms when needed.
- Perform vector similarity search over chunk embeddings.
- Assemble context window with citations.

### Response Generation
- Select provider (Azure OpenAI / AWS Bedrock) based on policy.
- Apply output validations (toxicity, hallucination flags).
- Return answer with sources and metadata.