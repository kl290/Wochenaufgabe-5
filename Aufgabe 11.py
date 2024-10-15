def eingabe_zahlen_liste():
    while True:
        try:
            eingabe = input("Bitte eine Liste von Zahlen eingeben (durch Kommas getrennt): ")
            return list(map(float, eingabe.split(',')))
        except ValueError:
            print("Fehler: Bitte nur gültige Zahlen eingeben.")


def groesste_zahl(liste):
    return max(liste)


zahlen_liste = eingabe_zahlen_liste()
print(f"Die größte Zahl in der Liste ist: {groesste_zahl(zahlen_liste)}")
