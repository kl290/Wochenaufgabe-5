print("Dieser Rechner berechent die Summe, Differenz, Multiplikation und die Division von 2 Zahlen die Sie eingeben können.")
while True:
    Zahl1 = float(input("Gib die erste Zahl ein: "))
    Zahl2 = float(input("Gib die zweite Zahl ein: "))
    try:
        Ergebnis = Zahl1 + Zahl2
        print(f"{Zahl1} + {Zahl2} = {Ergebnis}")
        print(f"{Zahl1} - {Zahl2} = {Ergebnis}")
        print(f"{Zahl1} * {Zahl2} = {Ergebnis}")
        print(f"{Zahl1} / {Zahl2} = {Ergebnis}")
        break
    except ValueError :
        print("Ungültige Eingabe. Bitte eine Zahl eingeben!")
