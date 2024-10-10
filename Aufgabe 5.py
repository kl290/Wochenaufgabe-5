print("Noten-Berechnung")
while True:
    try:
        Punktzahl= int(input("Bitte geben Sie Ihre Punktzahl (0-100) an: "))
        if  100 < Punktzahl or 0> Punktzahl:
            print("Ungültige Punktzahl")
        elif Punktzahl > 89:
            print("Sehr gut")
            break
        elif Punktzahl > 79:
            print("Gut")
            break
        elif Punktzahl > 69:
            print("Befriedigend")
            break
        elif Punktzahl > 59:
            print("Ausreichend")
            break
        if 0 < Punktzahl < 60:
            print("Nicht bestanden")
            break
    except ValueError :
        print("Ungültige Eingabe.Bitte gib eine Zahl ein!")