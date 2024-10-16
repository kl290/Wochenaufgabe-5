def punkt_eingabe():
    while True:
        try:
            zahl = int(input("Geben Sie eine Punktezahl zwischen 0 und 100 ein: "))
            if 0 <= zahl <= 100:
                return zahl
            else:
                print("Bitte gib eine Zahl zwischen 0 und 100 ein.")
        except ValueError:
            print("Bitte gib eine gültige Zahl ein.")


punkte = punkt_eingabe()

if   punkte > 89:
    print("Die Note lautet: Sehr gut")
elif punkte > 79:
    print("Die Note lautet: Gut")
elif punkte > 69:
    print("Die Note lautet: Befriedigend")
elif punkte > 59:
    print("Die Note lautet: Ausreichend")
elif punkte < 60:
    print("Die Note lautet: Nicht bestanden")



