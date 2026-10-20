# Fusion Runbook

## Start/Stop (current env)
- Started with: `npx --yes runfusion.ai` (background). If stopped, restart same way. Logs in /tmp/fusion-start*.log.
- Port may change on restart (previous runs used 4040 and 38799). Check logs for "Open:" line.
- Token: check logs for "Token: ..."; do not commit.

## Health check
- curl http://localhost:<port>/api/health (may require auth)
- With token: curl -H "Authorization: Bearer <token>" http://localhost:<port>/api/health

## Project
- Registered via `fn init` in repo; project id proj_96e2a48388f54daa.

## Troubleshooting
- If model auth fails, verify custom provider is configured and model ids match exactly. Anonymous free models require no API key.

## Anonymous free models
- Not compatible with Fusion v0.77.0 agent runtime as-is. Use a provider with valid auth (API key/OAuth/CLI) or local model server.

## Free provider recommendations
- OpenRouter (recommended for compatibility): requires API key; no payment needed for free models. Add as OpenAI-compatible custom provider with baseUrl https://openrouter.ai/api/v1.
- Local llama.cpp: free, no external API; needs installation. Check CPU/RAM limits (Codespaces: 2 CPUs, 7.8GB). May be slow for larger models.

## Working with OpenRouter
- Provider configured in Fusion settings (OpenAI-compatible). Key stored securely in settings, not in repo.
- To restart: run `npx --yes runfusion.ai` as before; check logs for port/token.
- Create tasks via Fusion API/UI; ensure model lanes point to OpenRouter free model.
