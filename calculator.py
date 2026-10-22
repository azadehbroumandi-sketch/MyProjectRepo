"""A small calculator supporting basic arithmetic and square roots."""

import math
from numbers import Real


def _validate_number(value: Real) -> None:
    """Raise ValueError when *value* is not a real number."""
    if isinstance(value, bool) or not isinstance(value, Real):
        raise ValueError("operands must be real numbers")


def add(left: Real, right: Real) -> Real:
    """Return the sum of two numbers."""
    _validate_number(left)
    _validate_number(right)
    return left + right


def subtract(left: Real, right: Real) -> Real:
    """Return the difference between two numbers."""
    _validate_number(left)
    _validate_number(right)
    return left - right


def multiply(left: Real, right: Real) -> Real:
    """Return the product of two numbers."""
    _validate_number(left)
    _validate_number(right)
    return left * right


def divide(left: Real, right: Real) -> float:
    """Return the quotient of two numbers.

    Raises:
        ZeroDivisionError: if *right* is zero.
    """
    _validate_number(left)
    _validate_number(right)
    if right == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return left / right


def sqrt(value: Real) -> float:
    """Return the non-negative square root of *value*.

    Raises:
        ValueError: if *value* is not a real number or is negative.
    """
    _validate_number(value)
    return math.sqrt(value)


def calculate(left: Real, operator: str, right: Real) -> Real:
    """Apply ``operator`` to ``left`` and ``right``.

    Supported operators are ``+``, ``-``, ``*``, and ``/``. Invalid
    operands or operators raise ValueError.
    """
    _validate_number(left)
    _validate_number(right)
    if not isinstance(operator, str) or operator not in {"+", "-", "*", "/"}:
        raise ValueError("operator must be one of +, -, *, /")

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    return operations[operator](left, right)


if __name__ == "__main__":
    print("ماشین حساب: برای خروج Ctrl-D را فشار دهید.")
    try:
        while True:
            expression = input("> ").split()
            if len(expression) != 3:
                print("ورودی باید به شکل: عدد عملگر عدد باشد")
                continue
            try:
                left, operator, right = float(expression[0]), expression[1], float(expression[2])
                print(calculate(left, operator, right))
            except (ValueError, ZeroDivisionError) as error:
                print(f"خطا: {error}")
    except EOFError:
        pass
