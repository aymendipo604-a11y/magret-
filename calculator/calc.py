"""Minimal, dependency-free arithmetic helpers.

Each function takes two numbers and returns the result of the corresponding
operation. Dividing by zero raises ``ZeroDivisionError`` with a clear message.
"""

from __future__ import annotations

__all__ = ["add", "subtract", "multiply", "divide"]


def add(a: float, b: float) -> float:
    """Return the sum of ``a`` and ``b``."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of ``a`` minus ``b``."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of ``a`` and ``b``."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of ``a`` divided by ``b``.

    Raises:
        ZeroDivisionError: If ``b`` is zero.
    """
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return a / b
