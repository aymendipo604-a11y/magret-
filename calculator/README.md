# Calculator

A tiny, dependency-free Python calculator with four arithmetic operations: add, subtract, multiply, and divide.

## Requirements

Python 3 only. No third-party packages, no install step, and no virtualenv are needed.

## Usage

```python
import sys

sys.path.insert(0, "calculator")  # when running from the repository root

from calc import add, subtract, multiply, divide

print(add(2, 3))        # 5
print(subtract(5, 3))   # 2
print(multiply(4, 3))   # 12
print(divide(10, 2))    # 5.0
```

If you are already inside the `calculator` directory, `from calc import ...` works on its own.

## Function reference

| Function | Signature | Behavior |
| --- | --- | --- |
| `add` | `add(a: float, b: float) -> float` | Returns the sum `a + b`. |
| `subtract` | `subtract(a: float, b: float) -> float` | Returns the difference `a - b`. |
| `multiply` | `multiply(a: float, b: float) -> float` | Returns the product `a * b`. |
| `divide` | `divide(a: float, b: float) -> float` | Returns the quotient `a / b`. Raises `ZeroDivisionError` when `b` is zero. |

Integer arguments are accepted everywhere; `add(2, 3)` returns `5` and `divide(10, 2)` returns `5.0`.

### Zero division

`divide` never returns `None`, `0`, `inf`, or `NaN` for a zero divisor. It raises `ZeroDivisionError` with the message `cannot divide by zero`:

```python
try:
    divide(1, 0)
except ZeroDivisionError as exc:
    print(exc)  # cannot divide by zero
```

## Running the tests

From the repository root:

```
python3 calculator/test_calc.py
```

Or from inside the `calculator` directory:

```
python3 test_calc.py
```

Both commands print one `PASS`/`FAIL` line per test followed by a summary line. A successful run prints `5 passed, 0 failed` and exits with status `0`; any failure prints a `FAIL` line and exits with a non-zero status.

The test file uses only plain `assert` statements and the Python standard library — no test framework needs to be installed.

## Project layout

```
calculator/
├── README.md      # this file
├── calc.py        # the four arithmetic functions
└── test_calc.py   # assert-based tests and the standalone test runner
```
