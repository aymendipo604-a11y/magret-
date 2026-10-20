# Fusion Factory Setup

## State
- Fusion v0.77.0 running on http://localhost:4040 (daemon token in logs; not stored in repo). Project magret- registered.
- Custom provider registered via API: id kilo-free, apiType openai-compatible, baseUrl https://ai-gateway.kilo.ai/api/v1, apiKey empty (anonymous).
- Free models discovered from https://ai-gateway.kilo.ai/api/v1/models: cohere/north-mini-code:free, minimax/minimax-m3.1-flash:free, nvidia/nemotron-3.5-lightning:free (and others) — all support tool/function calling as tested.
- Project lanes (execution/planning/validator) configured to use custom:kilo-free with cohere/north-mini-code:free.

## How anonymous access was tested
- GET /api/v1/models without auth returns models including *:free.
- POST /chat/completions to cohere/north-mini-code:free without Authorization header returns valid completions and tool_calls when requested.

## Issues encountered
- Fusion created and attempted to run task KB-001; planning failed with "No API key found for the selected model" despite anonymous base URL. This appears to be how Fusion's agent runtime authenticates requests (it may not honor empty apiKey for anonymous endpoints as expected). Further investigation would require checking Fusion's provider auth logic.

## Verified limitation
- Anonymous free models work at HTTP level, but Fusion v0.77.0 agent runtime (pi-coding-agent) requires API key resolution for the selected provider/model path; custom provider with empty apiKey is not accepted for task execution. Attempted with new custom provider and task KB-002 - failed same way.

## Free provider comparison (updated)
- Kilo gateway anonymous: HTTP works, but Fusion agent runtime rejects (needs API key) - not compatible.
- OpenRouter free models: require API key (account needed). Many :free models, supports tools. Compatible with OpenAI-compatible custom provider if key provided.
- Groq/Cerebras/Fireworks/Together: require API keys (free tiers often exist but still need signup/auth).
- Local llama.cpp: free/no external API; needs installation + model download. Hardware limited (2 CPUs, 7.8GB RAM) - may be slow.
