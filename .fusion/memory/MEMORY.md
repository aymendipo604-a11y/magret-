# Project Memory

<!-- Curated long-term memory. Store durable decisions, conventions, preferences, and pitfalls. -->

## Decisions

## Conventions

## Pitfalls

## Context

## Repository toolchain (durable)

This repo has **no** `package.json`, JS/TS toolchain, or root-level lint/test/build/typecheck script. Tasks here are verified with language-native commands only (e.g. Python: `python3 -m compileall -q <dir>` plus direct test runs) — do not look for `pnpm lint` / `pnpm test` / `pnpm build` gates.

Python 3.14.2 is available as `python3`; `pytest` is **not** installed, so assert-based scripts with a `__main__` runner are the sanctioned verification path for isolated Python work.
