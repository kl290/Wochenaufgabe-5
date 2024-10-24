def groesste_zahl():
    while True:
        eingabe = input("Bitte eine Liste von Zahlen eingeben (durch Kommas getrennt): ")
        try:
            zahlen_liste = list(map(float, eingabe.split(',')))
        except ValueError:
            print("Fehler: Bitte nur gültige Zahlen eingeben.")
            continue

        return max(zahlen_liste)


print(f"Die größte Zahl in der Liste ist: {groesste_zahl()}")
