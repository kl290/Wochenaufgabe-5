print("Dieser Rechner berechent die Summe, Differenz, Multiplikation und die Division von 2 Zahlen die Sie eingeben können.")
while True:
    eingabe1 = input("Gib die erste zahl ein: ")
    eingabe2 = input("Gib die zweite zahl ein: ")
    try:
        Zahl1 = float(eingabe1)
        Zahl2 = float(eingabe2)
        ergebnis = Zahl1 + Zahl2
        print(f"{Zahl1} + {Zahl2} = {ergebnis}")
        ergebnis = Zahl1 - Zahl2
        print(f"{Zahl1} - {Zahl2} = {ergebnis}")
        ergebnis = Zahl1 * Zahl2
        print(f"{Zahl1} * {Zahl2} = {ergebnis}")
        ergebnis = Zahl1 / Zahl2
        print(f"{Zahl1} / {Zahl2} = {ergebnis}")
        break
    except ValueError :
        print("Ungültige Eingabe. Bitte eine zahl eingeben!")

