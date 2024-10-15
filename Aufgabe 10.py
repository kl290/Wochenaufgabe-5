print("Taschenrechner!")
print("Berechnungen: +, -, *, /")


def eingabe_zahl(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine gültige Zahl ein.")


def addition(zahl1, zahl2):
    return zahl1 + zahl2


def subtraktion(zahl1, zahl2):
    return zahl1 - zahl2


def multiplikation(zahl1, zahl2):
    return zahl1 * zahl2


def division(zahl1, zahl2):
    if zahl2 == 0:
        raise ValueError("Division durch Null ist nicht erlaubt.")
    return zahl1 / zahl2


def taschenrechner():
    while True:
        operation = input("Wähle die Grundrechenart (+, -, *, /): ")

        if operation not in ["+", "-", "*", "/"]:
            print("Ungültige Auswahl. Bitte versuche es erneut.")
            continue

        zahl1 = eingabe_zahl("Gib die erste Zahl ein: ")
        zahl2 = eingabe_zahl("Gib die zweite Zahl ein: ")

        try:
            if operation == "+":
                ergebnis = addition(zahl1, zahl2)
            elif operation == "-":
                ergebnis = subtraktion(zahl1, zahl2)
            elif operation == "*":
                ergebnis = multiplikation(zahl1, zahl2)
            elif operation == "/":
                ergebnis = division(zahl1, zahl2)
        except ValueError as e:
            print(e)
            continue

        print(f"Das Ergebnis ist: {ergebnis}")
        break


taschenrechner()