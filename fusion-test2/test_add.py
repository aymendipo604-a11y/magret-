"""Assert-based tests for the :func:`add` helper.

Runnable either as a plain script (``python3 test_add.py``) or under a
pytest-style runner. No third-party dependencies are required.
"""

import os
import sys

# Make the helper importable no matter which directory the script is run from.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# The module name and the function name are both "add", so import the module
# itself and call ``add_module.add(...)`` to avoid shadowing.
import add as add_module  # noqa: E402

TOLERANCE = 1e-9


def test_add_two_positive_integers():
    assert add_module.add(2, 3) == 5, "add(2, 3) should equal 5"


def test_add_negative_operand():
    assert add_module.add(-2, 3) == 1, "add(-2, 3) should equal 1"


def test_add_zeros():
    assert add_module.add(0, 0) == 0, "add(0, 0) should equal 0"


def test_add_decimal_operands():
    result = add_module.add(2.5, 0.5)
    assert abs(result - 3.0) < TOLERANCE, "add(2.5, 0.5) should equal 3.0"


def test_add_two_negative_operands():
    result = add_module.add(-1.5, -2.5)
    assert abs(result - (-4.0)) < TOLERANCE, "add(-1.5, -2.5) should equal -4.0"


def test_add_identity_with_zero():
    assert add_module.add(10, 0) == 10, "add(10, 0) should equal 10"


def _main() -> int:
    """Run every module-level ``test_*`` function and report the results."""
    tests = [
        (name, obj)
        for name, obj in sorted(globals().items())
        if name.startswith("test_") and callable(obj)
    ]

    passed = 0
    failed = 0
    for name, test in tests:
        try:
            test()
        except AssertionError as exc:
            failed += 1
            print(f"FAIL {name}: {exc}")
        except Exception as exc:  # pragma: no cover - defensive
            failed += 1
            print(f"FAIL {name}: {type(exc).__name__}: {exc}")
        else:
            passed += 1
            print(f"PASS {name}")

    print(f"{passed} passed, {failed} failed")
    if failed:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(_main())
