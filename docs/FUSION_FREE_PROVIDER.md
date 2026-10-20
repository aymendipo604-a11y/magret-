# Free Provider (Kilo Gateway)

- Endpoint: https://ai-gateway.kilo.ai/api/v1 (OpenAI-compatible)
- Auth: none for anonymous free models (do not send Authorization header). Subject to rate limits.
- Discovery: GET https://ai-gateway.kilo.ai/api/v1/models (look for models with :free suffix or free pricing)
- Tested working: cohere/north-mini-code:free, minimax/minimax-m3.1-flash:free, nvidia/nemotron-3.5-lightning:free (all support tool calls)
- Fusion config: custom provider type openai-compatible, baseUrl as above, apiKey empty, add model IDs.
- Limitations: anonymous rate limits apply; some models may be unavailable; Fusion's runtime may still require auth - see setup doc.

## Diagnosis (anonymous)
- Tested directly with curl: anonymous requests to https://ai-gateway.kilo.ai/api/v1/chat/completions succeed without Authorization header for free models (e.g. cohere/north-mini-code:free) including tool calls.
- Fusion v0.77.0 uses @earendil-works/pi-coding-agent (ModelRegistry/ModelRuntime). For providers requiring auth, pi's model-runtime requires resolved API key unless authHeader is explicitly false/disabled and auth can be resolved without key. Fusion's custom-provider integration passes apiKey from settings and registers providers via pi's registerProvider; with empty apiKey, pi still expects API key resolution for the provider in the agent runtime path, causing "No API key found for the selected model".
- Verified: Fusion accepts the custom provider in settings/dashboard, but agent execution fails at planning/specification due to auth resolution in pi-coding-agent. No safe way to make anonymous OpenAI-compatible work in this Fusion version was found without modifying Fusion/installed deps or adding fake credentials (not attempted).
