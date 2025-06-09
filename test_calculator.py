import pytest
from calculator import Calculator

def test_addition():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_subtraction():
    calc = Calculator()
    assert calc.subtract(5, 2) == 3

def test_multiplication():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6

def test_division():
    calc = Calculator()
    assert calc.divide(6, 2) == 3

