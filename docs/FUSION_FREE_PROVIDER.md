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

## Free provider options (investigated)
- OpenRouter: many free models listed (e.g. minimax-m3.1-flash:free), but public HTTP endpoints require API key; testing via direct curl gives 401 without key. Requires account + API key. Not anonymous.
- Cerebras/Groq/Fireworks/Together/DeepSeek/etc: require API keys; unauthenticated requests rejected.
- Anthropic/OpenAI/Google: require credentials/payment context.
- HuggingFace Hub: models available; Inference API typically requires auth/token (many models behind gated access or need HF token). Not straightforward anonymous access for coding execution.
- llama.cpp via HTTP server: possible locally if ollama/runpod etc available. In this Codespaces environment: 2 CPUs, 7.8GB RAM; no ollama installed. Running small local model (e.g. 3-7B) could work with llama.cpp, but requires setup and may be slow on 2 CPUs; not available out of box.
- Kilo gateway anonymous: works directly via curl for free models and supports tools, but Fusion runtime (pi-coding-agent v0.77.0) requires API key resolution for the selected provider/model path; cannot use anonymous endpoints with custom provider in this Fusion version.

Recommendation: If you need free task execution through Fusion, the simplest path is OpenRouter with a free API key. No payment required to obtain key; many free models available. Alternatively, set up local llama.cpp if you want to avoid any cloud provider; however that requires installing/running a server.
