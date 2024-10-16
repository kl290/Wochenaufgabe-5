def woerter_zaehlen():
    while True:
        satz = input("Bitte einen Satz eingeben: ").strip()

        if satz:
            woerter = satz.split()

            if any(wort.isdigit() for wort in woerter):
                print("Fehler: Der Satz darf keine Zahlen enthalten. Bitte erneut versuchen.")
            else:
                print(f"Der Satz enthält {len(woerter)} Wörter.")
                break
        else:
            print("Fehler: Sie haben keinen gültigen Satz eingegeben. Bitte erneut versuchen.")


woerter_zaehlen()
