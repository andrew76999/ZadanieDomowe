def kalkulator():
    print("Prosty kalkulator w Pythonie")
    print("Dostępne operacje: +, -, *, /")

    liczba1 = float(input("Wprowadź pierwszą liczbę: "))
    operator = input("Wybierz operację (+, -, *, /): ")
    liczba2 = float(input("Wprowadź drugą liczbę: "))

    if operator == '+':
        wynik = liczba1 + liczba2
    elif operator == '-':
        wynik = liczba1 - liczba2
    elif operator == '*':
        wynik = liczba1 * liczba2
    elif operator == '/':
        if liczba2 != 0:
            wynik = liczba1 / liczba2
        else:
            return print("Błąd: Dzielenie przez zero!")
    else:
        return print("Błąd: Nieprawidłowy operator!")

    print(f"Wynik: {wynik}")

kalkulator()
