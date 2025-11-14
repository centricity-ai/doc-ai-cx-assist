## AI Interaction Layers

### Providers
- Azure OpenAI (chat/completions) with safety filters.
- AWS Bedrock (Anthropic/Meta) adapters with request shaping.

### Prompting
- System instructions + user query + retrieved context.
- Token budget management and truncation policies.

### Validations
- Input: profanity, PII, length, schema adherence for structured queries.
- Output: toxicity, jailbreak attempts, citation presence.