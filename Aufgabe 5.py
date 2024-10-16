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

if 90 <= punkte <= 100:
    print("Die Note lautet: Sehr gut")
elif 80 <= punkte < 90:
    print("Die Note lautet: Gut")
elif 70 <= punkte < 80:
    print("Die Note lautet: Befriedigend")
elif 60 <= punkte < 70:
    print("Die Note lautet: Ausreichend")
else:
    print("Die Note lautet: Nicht bestanden")



