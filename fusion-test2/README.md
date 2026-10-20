# fusion-test2

A minimal, dependency-free Python utility that adds two numbers together.

## Requirements

Python 3 only — no third-party packages, no install step, no virtualenv.

## Usage

```python
import sys

sys.path.insert(0, "fusion-test2")
import add as add_module

print(add_module.add(2, 3))  # 5
```

The module name and the function name are both `add`, so import the module
itself and call `add_module.add(...)`.

## Function reference

| Function | Signature | Behavior |
| --- | --- | --- |
| `add` | `add(a: float, b: float) -> float` | Returns the sum of `a` and `b` using the plain `+` operator. `int` and `float` arguments are both accepted; the result is `0` for `add(0, 0)`. |

Example results: `add(2, 3) == 5`, `add(-2, 3) == 1`, `add(2.5, 0.5) == 3.0`.

## Running the tests

From the repository root:

```bash
python3 fusion-test2/test_add.py
```

Or from inside this directory:

```bash
cd fusion-test2 && python3 test_add.py
```

A successful run prints one `PASS <test name>` line per test and a final
summary of `6 passed, 0 failed`, and exits with status `0`. If any assertion
fails, the runner prints a `FAIL` line for it and exits with a non-zero status.

The tests use plain `assert` statements and the standard library only. They are
also collectible by pytest if it is ever installed, but pytest is not required.

## Project layout

```
fusion-test2/
├── add.py        # the add(a, b) helper
├── test_add.py   # assert-based tests
└── README.md     # this file
```
