while True:
    try:
        Zahl = int(input("Bitte geben Sie eine Zahl ein: "))
        if Zahl == 0:
            print("Die eingegebene Zahl ist 0!")
        elif Zahl > 0:
            print("Die eingegebene Zahl ist positiv!")
        elif Zahl < 0:
            print("Die eingegebene Zahl ist negativ!")
        break
    except ValueError:
        print("Ungültige Eingabe.Bitte eine Zahl eingeben!")
