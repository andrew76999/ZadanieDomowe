def test_calculator_operations():
    calc = Calculator()
    result = calc.add(10, calc.multiply(2, 3))
    assert result == 16

