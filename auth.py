class AuthSystem:
    def login(self, username, password):
        if username == "user" and password == "password":
            return "Zalogowano pomyślnie"
        return "Błąd logowania"

