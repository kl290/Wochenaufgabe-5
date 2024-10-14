def note_berechnen(punkt):
    if 90 <= punkte <= 100:
        return "Sehr gut"
    elif 80 <= punkte < 90:
        return "Gut"
    elif 70 <= punkte < 80:
        return "Befriedigend"
    elif 60 <= punkte < 70:
        return "Ausreichend"
    else:
        return "Nicht bestanden"


gueltige_eingabe = False

while not gueltige_eingabe:
    try:
        punkte = float(input("Geben Sie eine Punktezahl zwischen 0 und 100 ein: "))
        if 0 <= punkte <= 100:
            gueltige_eingabe = True
            print(f"Die Note lautet: {note_berechnen(punkte)}")
        else:
            print("Ungültige Eingabe. Die Zahl muss zwischen 0 und 100 liegen.")
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
