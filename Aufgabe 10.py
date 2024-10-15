print("Taschenrechner!")
print("Berechnungen: +, -, *, /")


def eingabe_zahl(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine gültige Zahl ein.")


def taschenrechner():
    while True:
        operation = input("Wähle die Grundrechenart (+, -, *, /): ")

        if operation not in ["+", "-", "*", "/"]:
            print("Ungültige Auswahl. Bitte versuche es erneut.")
            continue

        zahl1 = eingabe_zahl("Gib die erste Zahl ein: ")
        zahl2 = eingabe_zahl("Gib die zweite Zahl ein: ")

        if operation == "/" and zahl2 == 0:
            print("Fehler: Division durch Null ist nicht erlaubt.")
            continue

        ergebnis = {
            "+": zahl1 + zahl2,
            "-": zahl1 - zahl2,
            "*": zahl1 * zahl2,
            "/": zahl1 / zahl2
        }[operation]

        print(f"Das Ergebnis ist: {ergebnis}")
        break


taschenrechner()
