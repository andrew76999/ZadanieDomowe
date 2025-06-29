import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from NewCalculator import oblicz


def test_dodawanie():
    assert oblicz(2, '+', 3) == 5

def test_odejmowanie():
    assert oblicz(7, '-', 2) == 5

def test_mnozenie():
    assert oblicz(4, '*', 3) == 12

def test_dzielenie():
    assert oblicz(8, '/', 2) == 4

def test_dzielenie_przez_zero():
    try:
        oblicz(5, '/', 0)
        assert False, "Powinien być rzucony wyjątek"
    except ValueError as e:
        assert str(e) == "Dzielenie przez zero"

def test_bledny_operator():
    try:
        oblicz(1, '%', 2)
        assert False, "Powinien być rzucony wyjątek"
    except ValueError as e:
        assert str(e) == "Nieprawidłowy operator"

