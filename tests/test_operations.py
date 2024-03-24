"""
Calculator Module

This module provides basic arithmetic operations using the Decimal class.
"""

from decimal import Decimal
import pytest
from faker import Faker
from app.calculator.calculation import Calculation
from app.calculator.operations import add, subtract, multiply, divide

faker = Faker()

def test_operation_add():
    """
    Test the addition operation of the calculator.
    """
    num1 = Decimal(faker.pydecimal(left_digits=2, right_digits=2, positive=True))
    num2 = Decimal(faker.pydecimal(left_digits=2, right_digits=2, positive=True))
    calculation = Calculation(num1, num2, add)
    assert calculation.perform() == num1 + num2, "Add operation failed with dynamic values"

def test_operation_subtract():
    """
    Test the subtraction operation of the calculator.
    """
    num1 = Decimal(faker.pydecimal(left_digits=2, right_digits=2, positive=True))
    num2 = Decimal(faker.pydecimal(left_digits=2, right_digits=2, positive=True))
    calculation = Calculation(num1, num2, subtract)
    assert calculation.perform() == num1 - num2, "Subtraction operation failed with dynamic values"

def test_operation_multiply():
    """
    Test the multiplication operation of the calculator.
    """
    num1 = Decimal(faker.pydecimal(left_digits=2, right_digits=2, positive=True))
    num2 = Decimal(faker.pydecimal(left_digits=2, right_digits=2, positive=True))
    calculation = Calculation(num1, num2, multiply)
    assert calculation.perform() == num1 * num2, "Multiplication operation failed with dynamic values"

def test_operation_divide():
    """
    Test the division operation of the calculator.
    """
    num1 = Decimal(faker.pydecimal(left_digits=2, right_digits=2, positive=True))
    num2 = Decimal(faker.pydecimal(left_digits=2, right_digits=2, positive=True, min_value=1))  # Ensure num2 is not zero
    calculation = Calculation(num1, num2, divide)
    assert calculation.perform() == num1 / num2, "Division operation failed with dynamic values"

def test_operation_divide_by_zero():
    """
    Test the division operation when dividing by zero.
    """
    num1 = Decimal(faker.pydecimal(left_digits=2, right_digits=2, positive=True))
    num2 = Decimal('0')
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(num1, num2, divide)
        calculation.perform()
