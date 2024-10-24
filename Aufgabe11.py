def groesste_zahl():
    eingabe = input("Bitte eine Liste von Zahlen eingeben (durch Kommas getrennt): ").strip()

    try:
        zahlen_liste = list(map(float, eingabe.split(',')))
    except ValueError:
        print("Fehler: Bitte nur gültige Zahlen im richtigen Format eingeben.")
        return groesste_zahl()

    groesste = max(zahlen_liste)

    print(f"Die größte Zahl in der Liste ist: {groesste}")


groesste_zahl()
