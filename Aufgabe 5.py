print("Noten-Berechnung")
Punktzahl= int(input("Bitte geben Sie Ihre Punktzahl an:"))
if Punktzahl == 0:
    print("nicht bestanden")
if  100 < Punktzahl or 0> Punktzahl:
    print("ungültige Punktzahl")
elif Punktzahl > 89:
    print("Sehr gut")
elif Punktzahl > 79:
    print("Gut")
elif Punktzahl > 69:
    print("Befriedigend")
elif Punktzahl > 59:
    print("Ausreichend")
if 0 < Punktzahl < 60:
    print("Nicht bestanden")
