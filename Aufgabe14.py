def woerter_zaehlen():
    while True:
        satz = input("Bitte einen Satz eingeben: ").strip()

        if satz:
            woerter = satz.split()
            anzahl_woerter = len(woerter)
            anzahl_zeichen = len(satz)
            anzahl_buchstaben = sum(c.isalpha() for c in satz)
            anzahl_ziffern = sum(c.isdigit() for c in satz)
            anzahl_whitespaces = sum(c.isspace() for c in satz)

            print(f"\nStatistik:")
            print(f"Der Satz enthält {anzahl_woerter} Wörter.")
            print(f"Der Satz enthält {anzahl_zeichen} Zeichen.")
            print(f"Der Satz enthält {anzahl_buchstaben} Buchstaben.")
            print(f"Der Satz enthält {anzahl_ziffern} Ziffern.")
            print(f"Der Satz enthält {anzahl_whitespaces} Whitespaces.")
            break
        else:
            print("Fehler: Sie haben keinen gültigen Satz eingegeben. Bitte erneut versuchen.")


woerter_zaehlen()
