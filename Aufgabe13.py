def woerter_zaehlen():
    satz = input("Bitte einen Satz eingeben: ").strip()

    while not satz:
        print("Fehler: Sie haben keinen gültigen Satz eingegeben. Bitte erneut versuchen.")
        satz = input("Bitte einen Satz eingeben: ").strip()

    woerter = satz.split()
    print(f"Der Satz enthält {len(woerter)} Wörter.")

woerter_zaehlen()