# Free Provider (Kilo Gateway)

- Endpoint: https://ai-gateway.kilo.ai/api/v1 (OpenAI-compatible)
- Auth: none for anonymous free models (do not send Authorization header). Subject to rate limits.
- Discovery: GET https://ai-gateway.kilo.ai/api/v1/models (look for models with :free suffix or free pricing)
- Tested working: cohere/north-mini-code:free, minimax/minimax-m3.1-flash:free, nvidia/nemotron-3.5-lightning:free (all support tool calls)
- Fusion config: custom provider type openai-compatible, baseUrl as above, apiKey empty, add model IDs.
- Limitations: anonymous rate limits apply; some models may be unavailable; Fusion's runtime may still require auth - see setup doc.
