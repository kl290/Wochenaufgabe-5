def groesste_zahl():
    while True:
        try:
            eingabe = input("Bitte eine Liste von Zahlen eingeben (durch Kommas getrennt): ")
            zahlen_liste = list(map(float, eingabe.split(',')))
            return max(zahlen_liste)
        except ValueError:
            print("Fehler: Bitte nur gültige Zahlen eingeben.")


print(f"Die größte Zahl in der Liste ist: {groesste_zahl()}")
