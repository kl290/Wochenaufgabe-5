# Funktionen für die Grundrechenarten
print("Taschenrechner!")
print("Dieser Rechner kann die Addition,Subtraktion,Multiplikation und Division zweier Zahlen berechnen.")


def addition(x, y):
    return x + y


def subtraktion(x, y):
    return x - y


def multiplikation(x, y):
    return x * y


def division(x, y):
    return x / y


# Rechenprogramm
def taschenrechner():
    print("Wähle die Grundrechenart: ")
    print("+")
    print("-")
    print("*")
    print("/")


auswahl = input("Wähle die gewünschte Grundrechenart (+,-,*,/): ")
zahl1 = float(input("Gib die erste zahl ein:"))
zahl2 = float(input("Gib die zweite Zahl ein:"))

if auswahl == "+":
    ergebnis = zahl1 + zahl2
    print(f"{zahl1} + {zahl2} = {ergebnis}")
elif auswahl == "-":
    ergebnis = zahl1 - zahl2
    print(f"{zahl1} - {zahl2} = {ergebnis}")
elif auswahl == "*":
    ergebnis = zahl1 * zahl2
    print(f"{zahl1} * {zahl2} = {ergebnis}")
elif auswahl == "/":
    ergebnis = zahl1 / zahl2
    print(f"{zahl1} / {zahl2} = {ergebnis}")
else:
    print("ungültige Auswahl")
