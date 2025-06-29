def oblicz(liczba1, operator, liczba2):
    if operator == '+':
        return liczba1 + liczba2
    elif operator == '-':
        return liczba1 - liczba2
    elif operator == '*':
        return liczba1 * liczba2
    elif operator == '/':
        if liczba2 != 0:
            return liczba1 / liczba2
        else:
            raise ValueError("Dzielenie przez zero")
    else:
        raise ValueError("Nieprawidłowy operator")


def kalkulator():
    print("Prosty kalkulator w Pythonie")
    liczba1 = float(input("Wprowadź pierwszą liczbę: "))
    operator = input("Wybierz operację (+, -, *, /): ")
    liczba2 = float(input("Wprowadź drugą liczbę: "))
    try:
        wynik = oblicz(liczba1, operator, liczba2)
        print(f"Wynik: {wynik}")
    except ValueError as e:
        print(f"Błąd: {e}")
