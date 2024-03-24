"""
Testing calculation.py
"""
from decimal import Decimal
import pytest
from app.calculator.calculation import Calculation
from app.calculator.operations import add, divide


def test_calculation_operations(a1, b1, operation, expected):
    """
    Test calculation operations
    """
    calc = Calculation(a1, b1, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a1} and {b1}"

def test_calculation_repr():
    """
    Test calculation __repr__ method
    """
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert repr(calc) == expected_repr, "The __repr__ method output does not match the expected string"

def test_divide_by_zero():
    """
    Test divide by zero scenario
    """
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()
