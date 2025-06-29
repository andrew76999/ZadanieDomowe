import pytest
from NewCalculator import oblicz


def test_dodawanie():
    assert oblicz(2, '+', 3) == 5

def test_odejmowanie():
    assert oblicz(5, '-', 2) == 3

def test_mnozenie():
    assert oblicz(4, '*', 3) == 12

def test_dzielenie():
    assert oblicz(10, '/', 2) == 5

def test_dzielenie_przez_zero():
    with pytest.raises(ValueError, match="Dzielenie przez zero"):
        oblicz(5, '/', 0)

def test_nieznany_operator():
    with pytest.raises(ValueError, match="Nieprawidłowy operator"):
        oblicz(1, '%', 2)

