def groesste_zahl(liste):
    return max(liste)


while True:
    try:
        eingabe = input("Bitte eine Liste von Zahlen eingeben (durch Kommas getrennt): ")
        zahlen_liste = [float(x) for x in eingabe.split(',')]
        print(f"Die größte Zahl in der Liste ist: {groesste_zahl(zahlen_liste)}")
        break
    except ValueError:
        print("Fehler: Bitte nur gültige Zahlen eingeben.")
