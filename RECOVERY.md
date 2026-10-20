# Recovery Guide

## Current State Summary
- Repo: private GitHub (aymendipo604-a11y/magret-), main branch up to date
- Fusion: v0.77.0 running (port 4040), embedded PostgreSQL 15.18 at /home/codespace/.fusion/embedded-postgres/default (port 37943)
- Project: proj_96e2a48388f54daa (magret-, path /workspaces/magret-)
- OpenRouter configured (custom provider)
- Tasks: KB-001, KB-002, KB-003 present (KB-002/KB-003 committed; KB-001 task evidence in .fusion/tasks/KB-001)
- Storage architecture: Postgres schemas (project, central, archive) in embedded Postgres cluster (authoritative); project-local .fusion/ contains metadata, tasks, memory, agents; global .fusion/agent/ contains agent sessions/config; fusion-central.db/fusion.db are legacy SQLite artifacts not present (migrated to Postgres).

## Backup Files (not committed to Git)
- backups/settings.json.enc - encrypted Fusion settings (AES-256-CBC/PBKDF2). Decryption key separate.
- backups/postgres-embedded.tar.gz - embedded Postgres data snapshot (file-level copy of live data dir). Note: file-level copy of a running Postgres cluster may not be fully consistent; prefer pg_basebackup/consistent logical backup when client tools available.
- backups/agent-state.tar.gz.enc - encrypted archive of global agent state (~/.fusion/agent/). Contains agent sessions and config; auth.json treated as secret.
- backups/checksums.sha256 - SHA256 checksums for all backup files.

## Required Persistent State (actual locations)
- Global settings: /home/codespace/.fusion/settings.json (encrypted backup exists)
- Embedded PostgreSQL: /home/codespace/.fusion/embedded-postgres/default/ (backed up as tar.gz; pg_basebackup unavailable in this environment - no postgresql-client tools found)
- Global agent state: /home/codespace/.fusion/agent/ (encrypted backup exists)
- Project metadata/tasks/memory/agents: /workspaces/magret-/.fusion/ (KB-002/KB-003 committed; KB-001 present locally; committed where safe)

## Do NOT restore (transient)
- engine.lock, engine.lock.lock, worktree lock files
- postmaster.pid, postmaster.opts from restored data dir (remove before starting Postgres)
- caches/tmp files

## Recovery Steps
1. Clone repo: git clone https://github.com/aymendipo604-a11y/magret-
2. Install Node 22.19.0+, ensure Fusion v0.77.0 available (npx --yes runfusion.ai)
3. Decrypt settings: openssl enc -aes-256-cbc -pbkdf2 -d -in backups/settings.json.enc -out ~/.fusion/settings.json -k $BACKUP_PASSPHRASE
4. Restore agent state (if needed): openssl enc -aes-256-cbc -pbkdf2 -d -in backups/agent-state.tar.gz.enc -out /tmp/agent-state.tar.gz -k $BACKUP_PASSPHRASE && tar xzf /tmp/agent-state.tar.gz -C ~; rm /tmp/agent-state.tar.gz
5. Restore Postgres: stop Fusion (if running) only if you own the instance; for this environment live instance must remain untouched. Extract postgres-embedded.tar.gz to ~/.fusion/embedded-postgres/, remove postmaster.pid/postmaster.opts. Postgres will run recovery on start.
6. Start Fusion, verify health, project (proj_96e2a48388f54daa), provider configuration. Do not start another engine for same project while live holds locks.
7. Verify schemas/tables in Postgres (project, central, archive) contain expected data.

## Verification
- Checksum: sha256sum -c backups/checksums.sha256
- Postgres: starts from restored data, "database system is ready", schemas present, central.projects contains project, project.tasks present
- Fusion health endpoint responsive, project registered, tasks accessible

## Notes
- Central/project state lives in Postgres schemas (authoritative), not SQLite fusion-central.db/fusion.db (migrated). Those SQLite files do not exist and need not be restored.
- Live instance must not be stopped/modified; isolated recovery requires different project identity or avoiding engine startup if same project ID would conflict.
