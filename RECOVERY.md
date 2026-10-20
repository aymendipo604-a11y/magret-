# Recovery Guide

## Current State Summary
- Repo: private GitHub (aymendipo604-a11y/magret-), main branch up to date
- Fusion: v0.77.0 running, embedded Postgres healthy
- Project: proj_96e2a48388f54daa (magret-)
- OpenRouter: minimax/minimax-m3.1-flash:free configured (custom provider dd937eef-...)
- Tasks: KB-002, KB-003 completed successfully (calculator/ and fusion-test2/ committed)
- Commits pushed (docs, code, task evidence)

## Backup Files (not committed to Git)
- backups/settings.json.enc - encrypted Fusion settings (AES-256-CBC, passphrase set separately)
- backups/postgres-embedded.tar.gz - embedded Postgres data snapshot
- backups/checksums.sha256 - integrity checksums

## Recovery Steps
1. Clone repo: git clone https://github.com/aymendipo604-a11y/magret-
2. Install Node 22.19.0+, run npx --yes runfusion.ai (or use existing install)
3. Decrypt settings: openssl enc -aes-256-cbc -pbkdf2 -d -in backups/settings.json.enc -out ~/.fusion/settings.json -k $BACKUP_PASSPHRASE
4. Restore Postgres: stop Fusion, backup existing if needed, extract postgres-embedded.tar.gz to ~/.fusion/embedded-postgres/
5. Start Fusion, verify health, project, provider configuration
6. Test with small task

## Notes
- Secrets encrypted; decryption key must be kept separate from backups
- Database backup is snapshot of live state - stop Fusion before restoration for safety
- OpenRouter API key is in encrypted settings
