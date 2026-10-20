# Task: KB-003 - Create a simple calculator in ./calculator: implement

**Created:** 2026-10-21
**Size:** S

## Original Description

<!-- fusion-original-description:start -->
Create a simple calculator in ./calculator: implement add/subtract/multiply/divide in calc.py, add tests in test_calc.py using assert, add README.md. Keep isolated.
<!-- fusion-original-description:end -->

## What This Delivers

- A small, self-contained calculator lives in its own `calculator` folder at the top of the project.
- Anyone can call four plain arithmetic operations — add, subtract, multiply, divide — with two numbers and get the exact result back.
- Dividing by zero fails loudly with a clear error instead of producing a nonsense number.
- A test file proves every operation (including the zero-division case) actually works, using simple `assert` statements, and runs to a green pass with a single command and no setup.
- A README in the folder explains what each operation does, how to use it, and how to run the tests.

## Before → After Transformation

- **Before:** The project has no calculator capability; the `calculator` directory does not exist, and there is nothing that adds, subtracts, multiplies, or divides numbers, and no tests for such behavior.
- **After:** The `calculator` directory contains `calc.py` (four arithmetic functions with a well-defined zero-division error), `test_calc.py` (assert-based tests covering all four operations plus the error case), and `README.md` (usage and test instructions) — all self-contained, with no changes to the rest of the repository.

## Review Level: 0 (None)

**Assessment:** The change is a new, fully isolated Python folder with no existing behavior changed, no external dependencies, and no shared code paths touched.
**Score:** 0/8 — Blast radius: 0, Pattern novelty: 0, Security: 0, Reversibility: 0

## Mission

Create a minimal, dependency-free Python calculator under the `calculator` directory at the repository root, providing `add`, `subtract`, `multiply`, and `divide`, plus an assert-based test module and a README documenting usage. The work must be completely isolated: every new file lives inside that one directory, nothing outside it is created, modified, or deleted, and no package metadata, CI config, or dependency manifests are introduced.

## Dependencies

- **None**

## Context to Read First

- `README.md` (repository root) — the existing project README; read only for context. It must **not** be modified (the task must stay isolated).
- `.gitignore` (repository root) — confirms `.fusion/`, `.pi/`, `.worktrees/`, and `fusion.db*` are ignored; the new calculator directory is normal tracked content and must not be ignored.
- `docs/` (repository root) — project documentation for the Fusion factory setup; out of scope, do not edit.
- The `calculator` directory — does not exist yet; the executor creates it in full.

Repository facts confirmed during planning (do not re-derive, do not change):
- The repository has **no** `package.json`, no JavaScript/TypeScript toolchain, and no root-level lint, test, build, or typecheck script. Verification for this task is Python-based only.
- Python 3.14.2 is available as `python3` (and `python`).
- The repository has no `conftest.py`, no `pytest.ini`/`pyproject.toml`/`setup.cfg`, and no shared test conventions to follow.

## File Scope

- `calculator/calc.py` (new)
- `calculator/test_calc.py` (new)
- `calculator/README.md` (new)

Nothing else. Do **not** add a package `__init__.py`, a requirements file, a `pyproject.toml`, a `setup.py`, a CI workflow, or any file outside the three paths above.

## Steps

### Step 0: Preflight

- [ ] Confirm the worktree root contains `README.md`, `docs/`, and `.gitignore`, and that no `calculator` directory exists yet.
- [ ] Confirm `python3 --version` reports a working interpreter (3.x) and record the version in the commit body / task notes.
- [ ] Confirm no root-level `package.json`, `pyproject.toml`, `setup.cfg`, `pytest.ini`, or `conftest.py` exists, so no project-wide test or lint command needs to be integrated.
- [ ] Confirm the working tree is clean (`git status --porcelain` is empty) before creating files.

### Step 1: Implement the calculator functions

- [ ] Create `calculator/calc.py` with exactly four public functions — `add(a, b)`, `subtract(a, b)`, `multiply(a, b)`, `divide(a, b)` — each taking two numeric arguments and returning the arithmetic result. Use `+`, `-`, `*`, `/` respectively; do not add extra operations, a CLI, a REPL, or a class.
- [ ] Give every function a type hint (`a: float, b: float -> float` style is fine, `int` inputs must be accepted) and a one-line docstring stating what it returns. Do not import anything from the standard library beyond what is strictly needed; no third-party imports.
- [ ] Implement `divide` so that a zero divisor raises `ZeroDivisionError` with a clear message (e.g. `raise ZeroDivisionError("cannot divide by zero")`) — do **not** return `None`, `0`, `float("inf")`, or `NaN`.
- [ ] Keep the module side-effect free: no code at import time, no `print` calls, no `if __name__ == "__main__"` block, no file or environment access.
- [ ] Verify the module compiles and the functions behave as specified with an ad-hoc check, e.g. `python3 -c "import sys; sys.path.insert(0, 'calculator'); import calc; print(calc.add(2,3), calc.subtract(5,3), calc.multiply(4,3), calc.divide(10,2))"` prints `5 2 12 5.0`.

**Artifacts:**
- `calculator/calc.py` (new)

### Step 2: Write the assert-based tests

- [ ] Create `calculator/test_calc.py` with test functions named `test_*` that use **plain `assert` statements** (no `unittest.TestCase`, no external test framework import) to verify the behavior.
- [ ] Make the file runnable **both** as a script and under a pytest-style runner: import `calc` via a `sys.path` fallback that inserts the directory containing `test_calc.py` (`os.path.dirname(os.path.abspath(__file__))`) into `sys.path` before `from calc import add, subtract, multiply, divide`, so the import works whether the file is run from the repository root or from inside the calculator directory.
- [ ] Add a `if __name__ == "__main__":` block that discovers every module-level function whose name starts with `test_`, runs each one, prints a `PASS`/`FAIL` line per test with the function name, prints a final summary (`N passed, M failed`), and exits with a non-zero status (`sys.exit(1)`) if any test failed. Do not use `unittest.main()`.
- [ ] Cover, with explicit assert messages where helpful, at least these scenarios:
  - `add(2, 3) == 5`; `add(-2, 3) == 1`; `add(0, 0) == 0`; `add(2.5, 0.5) == 3.0`
  - `subtract(5, 3) == 2`; `subtract(3, 5) == -2`; `subtract(0, 0) == 0`
  - `multiply(4, 3) == 12`; `multiply(-4, 3) == -12`; `multiply(0, 5) == 0`
  - `divide(10, 2) == 5`; `divide(-10, 2) == -5`; non-terminating case `divide(1, 3)` within a float tolerance (`abs(result - 1/3) < 1e-9`) rather than exact equality
  - `divide(1, 0)` raises `ZeroDivisionError` — assert this with an explicit `try/except ZeroDivisionError` block that fails the test if no exception is raised
- [ ] Assert a float result is compared with a tolerance, never with `==` against a repeating decimal.
- [ ] Keep the test file free of `print` output outside the `__main__` runner, and free of any network, file, or clock access.

**Artifacts:**
- `calculator/test_calc.py` (new)

### Step 3: Write the calculator README

- [ ] Create `calculator/README.md` with: a one-line title and description; a "Requirements" line stating that only Python 3 (no third-party packages) is needed; a "Usage" section with a short Python snippet importing from `calc` and calling all four functions; a table or list of each function with its signature and behavior; an explicit note that `divide` raises `ZeroDivisionError` for a zero divisor; a "Running the tests" section giving the exact command `python3 calculator/test_calc.py` (run from the repository root) and the alternative `python3 test_calc.py` (run from inside the calculator directory), noting that a successful run prints `N passed, 0 failed` and exits 0; and a short "Project layout" section listing the three files in the calculator directory.
- [ ] Do not claim the tests require pytest, a virtualenv, or any install step — the runner works with the standard library only.

**Artifacts:**
- `calculator/README.md` (new)

### Step 4: Testing & Verification

> ZERO failures allowed. Run the checks below from the repository root. This repository has **no** JavaScript toolchain and therefore no `pnpm lint` / `pnpm test` / `pnpm build` / typecheck script — the Python equivalents below are the quality gates for this task. Do not run a workspace-wide suite; the only tests in scope are the ones added by this task.

- [ ] Static check (lint substitute): `python3 -m compileall -q calculator` succeeds with no output and exit code 0 (covers `calc.py` and `test_calc.py`).
- [ ] Test run (primary): `python3 calculator/test_calc.py` exits 0 and prints a `N passed, 0 failed` summary with zero `FAIL` lines.
- [ ] Test run (alternate working directory): `cd calculator && python3 test_calc.py` exits 0 with the same all-pass summary — this proves the `sys.path` fallback and import behavior work from both locations.
- [ ] Import/behavior spot check: from the repository root, run `python3 -c "import sys; sys.path.insert(0,'calculator'); from calc import divide; ..."` in a way that calls `divide(1, 0)` inside a `try/except ZeroDivisionError` and prints `ok cannot divide by zero`.
- [ ] Failure-path proof: confirm the runner actually fails when it should — e.g. run a one-liner that asserts `add(2,3) == 6` and observe a non-zero exit — then remove the temporary check. (Do not leave any temporary or broken variant of the committed files behind.)
- [ ] Isolation check: `git status --porcelain` shows **only** the three new files `calculator/calc.py`, `calculator/test_calc.py`, and `calculator/README.md`; no tracked file outside the calculator directory is modified, and no extra package or CI files were added.
- [ ] If any check fails, fix the source or the test in place and re-run the full set above until every check passes.

### Step 5: Documentation & Delivery

- [ ] Confirm `calculator/README.md` matches the shipped behavior (function names, zero-division behavior, and the exact test command) — no drift between README and code.
- [ ] Save the final README content as a task document via `fn_task_document_write` with `key="docs"` and `content=` the full text of `calculator/README.md`.
- [ ] No visual/media deliverable exists for this task, so no `fn_artifact_register` call is required (there is no UI, screenshot, mockup, recording, HTML prototype, or PDF to register).
- [ ] Do not modify the repository-root `README.md` or anything under `docs/` — the task must stay isolated. If a root-level pointer to the new calculator directory seems genuinely useful, raise it as a separate follow-up task via `fn_task_create` rather than editing it here.
- [ ] Commit the work with the task ID in the message per the convention below, and confirm `git log --oneline` shows the commits for this task on the current branch.

## Environment Constraints

- The ideal tool-driven check for this project layout would be `pytest calculator/`, but **pytest is not installed in this environment** (`python3 -c "import pytest"` → `ModuleNotFoundError`). Installing it would also violate the "no dependencies" isolation requirement. This is explicitly **non-blocking**.
- Runnable substitute used as the authoritative gate: `python3 calculator/test_calc.py` (and `cd calculator && python3 test_calc.py`), which is a real automated test run with real assertions and a non-zero exit code on failure. `calculator/test_calc.py` is deliberately written to also be collectible by pytest if it is ever installed, but no acceptance criterion depends on pytest.
- No JavaScript runtime toolchain (`pnpm lint`, `pnpm test`, typecheck, build) exists in this repository, so those template checkboxes are replaced by `python3 -m compileall -q calculator` plus the test runs above.

## Documentation Requirements

**Must Update:**
- `calculator/README.md` (new) — purpose, requirements, usage examples, per-function reference, zero-division behavior, and how to run the tests.

**Check If Affected:**
- `README.md` (repository root) — checked; not affected. The task must remain isolated, so the root README is intentionally left untouched.
- `docs/` — checked; these document the Fusion factory setup and are unrelated to the calculator, so they are not updated.

## Completion Criteria

- [ ] All steps complete
- [ ] `python3 -m compileall -q calculator` passes (static check substitute for lint)
- [ ] `python3 calculator/test_calc.py` exits 0 with all tests passing, from the repository root and from inside the calculator directory
- [ ] Typecheck passing (if available) — no type checker is configured in this repository; type hints are present on all four functions in `calculator/calc.py` and this criterion is satisfied vacuously
- [ ] Documentation updated (`calculator/README.md` exists, is accurate, and is saved via `fn_task_document_write` with `key="docs"`)
- [ ] `git status --porcelain` shows only the three new files under the calculator directory

## Git Commit Convention

Commits at step boundaries. All commits include the task ID:

- **Step completion:** `feat(KB-003): complete Step N — <short summary>` (the `<short summary>` is required — use a concrete 5–10 word description)
- **Bug fixes:** `fix(KB-003): description` (short, concrete summary required)
- **Tests:** `test(KB-003): description` (short, concrete summary required)

Good examples:
- `feat(KB-003): complete Step 1 — add calc.py with four arithmetic operations`
- `test(KB-003): complete Step 2 — add assert-based calculator test suite`
- `feat(KB-003): complete Step 3 — document calculator usage in README`

Bad example:
- `feat(KB-003): complete Step 2`

## Do NOT

- Do not modify, create, or delete any file outside the calculator directory (in particular, do not touch the repository-root `README.md`, the `docs` folder, or `.gitignore`).
- Do not add third-party dependencies, a requirements file, a `pyproject.toml`, a `setup.py`, virtualenvs, or CI configuration — the calculator must run on a bare Python 3 interpreter.
- Do not add features beyond the requested scope: no CLI, REPL, GUI, calculator class, extra operations (power, modulo, square root), or expression parser.
- Do not swallow the zero-division error (no returning `None`, `0`, `inf`, or `NaN`).
- Do not use `unittest.TestCase` or an external test framework in `calculator/test_calc.py` — the request specifies `assert`-based tests.
- Do not skip tests or leave any test as a placeholder, `pass`, or `TODO`.
- Do not commit without the `KB-003` task ID prefix.
- Do not force-add ignored `.fusion/` artifacts and do not create empty/fabricated commits.
- If something seems unused or out of scope, create a follow-up task via `fn_task_create` instead of expanding this task.

## Changeset Requirements

No changeset is required. This task only adds new files under the calculator directory; it removes no existing functionality, settings, endpoints, or exports, and it is net-additive.
