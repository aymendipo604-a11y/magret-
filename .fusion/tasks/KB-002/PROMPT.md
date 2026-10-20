# Task: KB-002 - Create a minimal Python utility in ./fusion-test2: add.py

**Created:** 2026-10-21
**Size:** S

## Original Description

<!-- fusion-original-description:start -->
Create a minimal Python utility in ./fusion-test2: add.py with add(a,b) and test_add.py, README.md. Keep isolated.
<!-- fusion-original-description:end -->

## What This Delivers

- A small, self-contained Python helper lives in its own `fusion-test2` folder at the top of the project.
- Anyone can call a single plain function that adds two numbers together and get the exact result back.
- A test file proves the function actually adds correctly (including negative and decimal inputs) using simple `assert` statements, and runs to a green pass with one command and no setup.
- A README in the folder explains what the function does, how to call it, and how to run the tests.

## Before → After Transformation

- **Before:** The project has no `fusion-test2` directory and no addition helper at all; there is nothing to import and nothing that proves the behavior works.
- **After:** The `fusion-test2` directory contains `add.py` (one `add(a, b)` function), `test_add.py` (assert-based tests covering the helper), and `README.md` (usage and test instructions) — all self-contained, with no changes to the rest of the repository.

## Review Level: 0 (None)

**Assessment:** The change is a new, fully isolated Python folder with no existing behavior changed, no external dependencies, and no shared code paths touched.
**Score:** 0/8 — Blast radius: 0, Pattern novelty: 0, Security: 0, Reversibility: 0

## Mission

Create a minimal, dependency-free Python utility under the `fusion-test2` directory at the repository root, providing a single `add(a, b)` function, plus an assert-based test module and a README documenting usage. The work must be completely isolated: every new file lives inside that one directory, nothing outside it is created, modified, or deleted, and no package metadata, CI config, or dependency manifests are introduced.

## Dependencies

- **None**

## Context to Read First

- `README.md` (repository root) — the existing project README; read only for context. It must **not** be modified (the task must stay isolated).
- `.gitignore` (repository root) — confirms `.fusion/`, `.pi/`, `.worktrees/`, and `fusion.db*` are ignored; the new `fusion-test2` directory is normal tracked content and must not be ignored.
- `docs/` (repository root) — project documentation for the Fusion factory setup; out of scope, do not edit.
- The `fusion-test2` directory — does not exist yet; the executor creates it in full.

Repository facts confirmed during planning (do not re-derive, do not change):
- The repository has **no** `package.json`, no JavaScript/TypeScript toolchain, and no root-level lint, test, build, or typecheck script. Verification for this task is Python-based only.
- Python 3.14.2 is available as `python3` (and `python`).
- The repository has no `conftest.py`, no `pytest.ini`/`pyproject.toml`/`setup.cfg`, and no shared test conventions to follow.

## File Scope

- `fusion-test2/add.py` (new)
- `fusion-test2/test_add.py` (new)
- `fusion-test2/README.md` (new)

Nothing else. Do **not** add a package `__init__.py`, a requirements file, a `pyproject.toml`, a `setup.py`, a CI workflow, or any file outside the three paths above.

## Steps

### Step 0: Preflight

- [ ] Confirm the worktree root contains `README.md`, `docs/`, and `.gitignore`, and that no `fusion-test2` directory exists yet.
- [ ] Confirm `python3 --version` reports a working interpreter (3.x) and record the version in the commit body / task notes.
- [ ] Confirm no root-level `package.json`, `pyproject.toml`, `setup.cfg`, `pytest.ini`, or `conftest.py` exists, so no project-wide test or lint command needs to be integrated.
- [ ] Confirm the working tree is clean (`git status --porcelain` is empty) before creating files.

### Step 1: Implement the `add` function

- [ ] Create `fusion-test2/add.py` with exactly one public function — `add(a, b)` — taking two numeric arguments and returning their sum. Do not add extra functions, a CLI, a REPL, or a class.
- [ ] Give the function a type hint (e.g. `def add(a: float, b: float) -> float:` — `int` inputs must be accepted) and a one-line docstring stating what it returns. Use the plain `+` operator; do not import anything (standard library or third-party) — no `math`, no `numbers`, no `Decimal`.
- [ ] Keep the module side-effect free: no code at import time, no `print` calls, no `if __name__ == "__main__":` block, no file or environment access.
- [ ] Verify the module compiles and behaves as specified with an ad-hoc check, e.g. `python3 -c "import sys; sys.path.insert(0, 'fusion-test2'); import add as m; print(m.add(2,3), m.add(-2,3), m.add(2.5,0.5))"` prints `5 1 3.0`.

**Artifacts:**
- `fusion-test2/add.py` (new)

### Step 2: Write the assert-based tests

- [ ] Create `fusion-test2/test_add.py` with test functions named `test_*` that use **plain `assert` statements** (no `unittest.TestCase`, no external test framework import) to verify the behavior.
- [ ] Make the file runnable **both** as a script and under a pytest-style runner: import the helper via a `sys.path` fallback that inserts the directory containing `test_add.py` (`os.path.dirname(os.path.abspath(__file__))`) into `sys.path` before `from add import add`, so the import works whether the file is run from the repository root or from inside the `fusion-test2` directory. (Note: the module name `add` and the function name `add` collide, so import the module itself — e.g. `import add as add_module` — and call `add_module.add(...)`; do not rely on `from add import add` shadowing.)
- [ ] Add a `if __name__ == "__main__":` block that discovers every module-level function whose name starts with `test_`, runs each one, prints a `PASS`/`FAIL` line per test with the function name, prints a final summary (`N passed, M failed`), and exits with a non-zero status (`sys.exit(1)`) if any test failed. Do not use `unittest.main()`.
- [ ] Cover, with explicit assert messages where helpful, at least these scenarios:
  - `add(2, 3) == 5`
  - `add(-2, 3) == 1` (negative operand)
  - `add(0, 0) == 0`
  - `add(2.5, 0.5) == 3.0` (decimal operands)
  - `add(-1.5, -2.5) == -4.0` (both operands negative)
  - `add(10, 0) == 10` (identity with zero)
- [ ] Assert a float result with a tolerance (`abs(result - expected) < 1e-9`) rather than exact `==` where a repeating decimal could appear; do not assert on values that cannot be represented exactly.
- [ ] Keep the test file free of `print` output outside the `__main__` runner, and free of any network, file, or clock access.

**Artifacts:**
- `fusion-test2/test_add.py` (new)

### Step 3: Write the README

- [ ] Create `fusion-test2/README.md` with: a one-line title and description; a "Requirements" line stating that only Python 3 (no third-party packages) is needed; a "Usage" section with a short Python snippet importing the helper and calling `add`; a "Function reference" table or list giving the `add(a, b)` signature and behavior; a "Running the tests" section giving the exact command `python3 fusion-test2/test_add.py` (run from the repository root) and the alternative `python3 test_add.py` (run from inside the `fusion-test2` directory), noting that a successful run prints `N passed, 0 failed` and exits 0; and a short "Project layout" section listing the three files in the directory.
- [ ] Do not claim the tests require pytest, a virtualenv, or any install step — the runner works with the standard library only.

**Artifacts:**
- `fusion-test2/README.md` (new)

### Step 4: Testing & Verification

> ZERO failures allowed. Run the checks below from the repository root. This repository has **no** JavaScript toolchain and therefore no `pnpm lint` / `pnpm test` / `pnpm build` / typecheck script — the Python equivalents below are the quality gates for this task. Do not run a workspace-wide suite; the only tests in scope are the ones added by this task.

- [ ] Static check (lint substitute): `python3 -m compileall -q fusion-test2` succeeds with no output and exit code 0 (covers `add.py` and `test_add.py`).
- [ ] Test run (primary): `python3 fusion-test2/test_add.py` exits 0 and prints a `N passed, 0 failed` summary with zero `FAIL` lines.
- [ ] Test run (alternate working directory): `cd fusion-test2 && python3 test_add.py` exits 0 with the same all-pass summary — this proves the `sys.path` fallback and import behavior work from both locations.
- [ ] Import/behavior spot check: from the repository root, run `python3 -c "import sys; sys.path.insert(0,'fusion-test2'); import add; print(add.add(2,3))"` and confirm it prints `5`.
- [ ] Failure-path proof: confirm the runner actually fails when it should — e.g. run a one-liner that asserts `add.add(2,3) == 6` inside a `try/except AssertionError` and confirm the exit status is non-zero — then remove the temporary check. (Do not leave any temporary or broken variant of the committed files behind.)
- [ ] Isolation check: `git status --porcelain` shows **only** the three new files `fusion-test2/add.py`, `fusion-test2/test_add.py`, and `fusion-test2/README.md`; no tracked file outside the `fusion-test2` directory is modified, and no extra package or CI files were added.
- [ ] If any check fails, fix the source or the test in place and re-run the full set above until every check passes.

### Step 5: Documentation & Delivery

- [ ] Confirm `fusion-test2/README.md` matches the shipped behavior (function name, behavior, and the exact test command) — no drift between README and code.
- [ ] Save the final README content as a task document via `fn_task_document_write` with `key="docs"` and `content=` the full text of `fusion-test2/README.md`.
- [ ] No visual/media deliverable exists for this task, so no `fn_artifact_register` call is required (there is no UI, screenshot, mockup, recording, HTML prototype, or PDF to register).
- [ ] Do not modify the repository-root `README.md` or anything under `docs/` — the task must stay isolated. If a root-level pointer to the new `fusion-test2` directory seems genuinely useful, raise it as a separate follow-up task via `fn_task_create` rather than editing it here.
- [ ] Commit the work with the task ID in the message per the convention below, and confirm `git log --oneline` shows the commits for this task on the current branch.

## Environment Constraints

- The ideal tool-driven check for this project layout would be `pytest fusion-test2/`, but **pytest is not installed in this environment** (`python3 -c "import pytest"` → `ModuleNotFoundError`). Installing it would also violate the "no dependencies" isolation requirement. This is explicitly **non-blocking**.
- Runnable substitute used as the authoritative gate: `python3 fusion-test2/test_add.py` (and `cd fusion-test2 && python3 test_add.py`), which is a real automated test run with real assertions and a non-zero exit code on failure. `fusion-test2/test_add.py` is deliberately written to also be collectible by pytest if it is ever installed, but no acceptance criterion depends on pytest.
- No JavaScript runtime toolchain (`pnpm lint`, `pnpm test`, typecheck, build) exists in this repository, so those template checkboxes are replaced by `python3 -m compileall -q fusion-test2` plus the test runs above.

## Documentation Requirements

**Must Update:**
- `fusion-test2/README.md` (new) — purpose, requirements, usage example, function reference, and how to run the tests.

**Check If Affected:**
- `README.md` (repository root) — checked; not affected. The task must remain isolated, so the root README is intentionally left untouched.
- `docs/` — checked; these document the Fusion factory setup and are unrelated to this utility, so they are not updated.

## Completion Criteria

- [ ] All steps complete
- [ ] `python3 -m compileall -q fusion-test2` passes (static check substitute for lint)
- [ ] `python3 fusion-test2/test_add.py` exits 0 with all tests passing, from the repository root and from inside the `fusion-test2` directory
- [ ] Typecheck passing (if available) — no type checker is configured in this repository; a type hint is present on `add` in `fusion-test2/add.py` and this criterion is satisfied vacuously
- [ ] Documentation updated (`fusion-test2/README.md` exists, is accurate, and is saved via `fn_task_document_write` with `key="docs"`)
- [ ] `git status --porcelain` shows only the three new files under the `fusion-test2` directory

## Git Commit Convention

Commits at step boundaries. All commits include the task ID:

- **Step completion:** `feat(KB-002): complete Step N — <short summary>` (the `<short summary>` is required — use a concrete 5–10 word description)
- **Bug fixes:** `fix(KB-002): description` (short, concrete summary required)
- **Tests:** `test(KB-002): description` (short, concrete summary required)

Good examples:
- `feat(KB-002): complete Step 1 — add add.py with the add helper function`
- `test(KB-002): complete Step 2 — add assert-based test suite for add helper`
- `feat(KB-002): complete Step 3 — document fusion-test2 usage in README`

Bad example:
- `feat(KB-002): complete Step 2`

## Do NOT

- Do not modify, create, or delete any file outside the `fusion-test2` directory (in particular, do not touch the repository-root `README.md`, the `docs` folder, or `.gitignore`).
- Do not add third-party dependencies, a requirements file, a `pyproject.toml`, a `setup.py`, virtualenvs, or CI configuration — the utility must run on a bare Python 3 interpreter.
- Do not add features beyond the requested scope: no CLI, REPL, GUI, class, extra operations (subtract, multiply, divide), or expression parser.
- Do not use `unittest.TestCase` or an external test framework in `fusion-test2/test_add.py` — the request specifies `assert`-based tests.
- Do not skip tests or leave any test as a placeholder, `pass`, or `TODO`.
- Do not commit without the `KB-002` task ID prefix.
- Do not force-add ignored `.fusion/` artifacts and do not create empty/fabricated commits.
- If something seems unused or out of scope, create a follow-up task via `fn_task_create` instead of expanding this task.

## Changeset Requirements

No changeset is required. This task only adds new files under the `fusion-test2` directory; it removes no existing functionality, settings, endpoints, or exports, and it is net-additive.
