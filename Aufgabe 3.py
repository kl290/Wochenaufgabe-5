print("Dieser Rechner berechent die Summe, Differenz, Multiplikation und die Division von 2 Zahlen die Sie eingeben können.")
while True:
    eingabe1 = input("Gib die erste zahl ein: ")
    eingabe2 = input("Gib die zweite zahl ein: ")
    try:
        zahl1 = float(eingabe1)
        zahl2 = float(eingabe2)
        ergebnis = zahl1 + zahl2
        print(f"{zahl1} + {zahl2} = {ergebnis}")
        ergebnis = zahl1 - zahl2
        print(f"{zahl1} - {zahl2} = {ergebnis}")
        ergebnis = zahl1 * zahl2
        print(f"{zahl1} * {zahl2} = {ergebnis}")
        ergebnis = zahl1 / zahl2
        print(f"{zahl1} / {zahl2} = {ergebnis}")
        break
    except ValueError :
        print("Ungültige Operation. Bitte eine zahl eingeben!")

