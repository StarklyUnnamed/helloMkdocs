
"""Provide several sample math calculations.

This module allows the user to make mathematical calculations.

Examples:
    >>> from calculator import calculations
    >>> calculations.add(2, 4)
    6.0
    >>> calculations.multiply(2.0, 4.0)
    8.0
    >>> from calculator.calculations import divide
    >>> divide(4.0, 2)
    2.0


The module contains the following functions:

- `add(a, b)` - Returns the sum of two numbers.
- `subtract(a, b)` - Returns the difference of two numbers.
- `multiply(a, b)` - Returns the product of two numbers.
- `divide(a, b)` - Returns the quotient of two numbers.
"""

from typing import Union
# Modern python would implement typeHinting the following way:
# def function(a: float | int, b: float | int) -> float
def add(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the sum of two values.

    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0

    Args:
        a: A number representing the first addend in the addition.
        b: A number representing the second addend in the addition.

    Returns:
        The sum of 'a' and 'b'
    """
    return float(a + b)
# Modern python would implement typeHinting the following way:
# def function(a: float | int, b: float | int) -> float
def subtract(a: Union[float, int], b: Union[float, int]) -> float:
    """Returns the difference of two numbers.

    Examples:
        >>> subtract(4.0, 2.0)
        2.0
        >>> subtract(4, 2)
        2.0

    Args:
        a: A number representing the minuend of the subtraction.
        b: A number representing the subtrahend of the subtraction.

    Returns:
        A number that is the difference between both arguments.
    """
    return float(a - b)
# Modern python would implement typeHinting the following way:
# def function(a: float | int, b: float | int) -> float
def multiply(a: Union[float, int], b: Union[float, int]) -> float:
    """Returns the product of two numbers.

    Examples:
        >>> multiply(4.0, 2.0)
        8.0
        >>> multiply(4, 2)
        8.0

    Args:
        a: A number representing the multiplicand in the multiplication.
        b: A number representing the multiplier in the multiplication.

    Returns:
        The product of both arguments.
    """
    return float(a * b)
# Modern python would implement typeHinting the following way:
# def function(a: float | int, b: float | int) -> float
def divide(a: Union[float, int], b: Union[float, int]) -> float:
    """Returns the quotient of two numbers. 

    Examples:
        >>> divide(4.0, 2.0)
        2.0
        >>> divide(4, 2)
        2.0

    Args:
        a: (float, int): A number that represents the dividend in the division.
        b: (float, int): A number that represents the divider in the division.

    Raises:
        ZeroDivisionError: An error will occur if the divider is 0.

    Returns:
        The quotient of both arguments.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)