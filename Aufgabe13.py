def woerter_zaehlen():
    satz = input("Bitte einen Satz eingeben: ").strip()

    if not satz:
        print("Fehler: Sie haben keinen gültigen Satz eingegeben. Bitte erneut versuchen.")
        return woerter_zaehlen()
    woerter = satz.split()

    print(f"Der Satz enthält {len(woerter)} Wörter.")


woerter_zaehlen()
