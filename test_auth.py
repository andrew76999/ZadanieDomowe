import pytest
from auth import AuthSystem

def test_login_success():
    auth = AuthSystem()
    assert auth.login("user", "password") == "Zalogowano pomyślnie"

def test_login_failure():
    auth = AuthSystem()
    assert auth.login("user", "wrongpass") == "Błąd logowania"

