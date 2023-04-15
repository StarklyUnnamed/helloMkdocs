from typing import Union

def add(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the sum of two values.

    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0

    Args:
        a (float, int): A number representing the first addend in the addition.
        b (float, int): A number representing the second addend in the addition.

    Returns:
        float: The sum of 'a' and 'b'
    """
    return float(a + b)

def subtract(a: Union[float, int], b: Union[float, int]) -> float:
    """Returns the difference of two numbers.

    Examples:
        >>> subtract(4.0, 2.0)
        2.0
        >>> subtract(4, 2)
        2.0

    Args:
        a (float, int): A number representing the minuend of the subtraction.
        b (float, int): A number representing the subtrahend of the subtraction.

    Returns:
        float: A number that is the difference between both arguments.
    """
    return float(a - b)

def multiply(a: Union[float, int], b: Union[float, int]) -> float:
    """Returns the product of two numbers.

    Examples:
        >>> multiply(4.0, 2.0)
        8.0
        >>> multiply(4, 2)
        8.0

    Args:
        a (float, int): A number representing the multiplicand in the multiplication.
        b (float, int): A number representing the multiplier in the multiplication.

    Returns:
        float: The product of both arguments.
    """
    return float(a * b)

def divide(a: Union[float, int], b: Union[float, int]) -> float:
    """Returns the quotient of two numbers. 

    Examples:
        >>> divide(4.0, 2.0)
        2.0
        >>> divide(4, 2)
        2.0

    Args:
        a (float, int): A number that represents the dividend in the division.
        b (float, int): A number that represents the divider in the division.

    Raises:
        ZeroDivisionError: An error will occur if the divider is 0.

    Returns:
        float: The quotient of both arguments.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)