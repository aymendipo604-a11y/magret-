"""Assert-based tests for the calculator module.

Runnable directly (``python3 test_calc.py``) or collected by a pytest-style
runner. Uses only plain ``assert`` statements and the standard library.
"""

from __future__ import annotations

import os
import sys

# Make the import work whether this file is run from the repository root or
# from inside the calculator directory.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from calc import add, divide, multiply, subtract  # noqa: E402

TOLERANCE = 1e-9


def test_add() -> None:
    assert add(2, 3) == 5, "add(2, 3) should be 5"
    assert add(-2, 3) == 1, "add(-2, 3) should be 1"
    assert add(0, 0) == 0, "add(0, 0) should be 0"
    assert add(2.5, 0.5) == 3.0, "add(2.5, 0.5) should be 3.0"


def test_subtract() -> None:
    assert subtract(5, 3) == 2, "subtract(5, 3) should be 2"
    assert subtract(3, 5) == -2, "subtract(3, 5) should be -2"
    assert subtract(0, 0) == 0, "subtract(0, 0) should be 0"


def test_multiply() -> None:
    assert multiply(4, 3) == 12, "multiply(4, 3) should be 12"
    assert multiply(-4, 3) == -12, "multiply(-4, 3) should be -12"
    assert multiply(0, 5) == 0, "multiply(0, 5) should be 0"


def test_divide() -> None:
    assert divide(10, 2) == 5, "divide(10, 2) should be 5"
    assert divide(-10, 2) == -5, "divide(-10, 2) should be -5"
    result = divide(1, 3)
    assert abs(result - 1 / 3) < TOLERANCE, "divide(1, 3) should be close to 1/3"


def test_divide_by_zero_raises() -> None:
    raised = False
    try:
        divide(1, 0)
    except ZeroDivisionError:
        raised = True
    assert raised, "divide(1, 0) should raise ZeroDivisionError"


def main() -> int:
    tests = [
        (name, obj)
        for name, obj in sorted(globals().items())
        if name.startswith("test_") and callable(obj)
    ]
    failures = 0
    for name, func in tests:
        try:
            func()
        except AssertionError as exc:
            failures += 1
            print(f"FAIL {name}: {exc}")
        except Exception as exc:  # pragma: no cover - defensive
            failures += 1
            print(f"FAIL {name}: {type(exc).__name__}: {exc}")
        else:
            print(f"PASS {name}")
    print(f"{len(tests) - failures} passed, {failures} failed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
