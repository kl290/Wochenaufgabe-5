def woerter_zaehlen():
    while True:
        satz = input("Bitte einen Satz eingeben: ").strip()

        if satz:
            woerter = satz.split()

            print(f"Der Satz enthält {len(woerter)} Wörter.")
            break

print("Fehler: Sie haben keinen gültigen Satz eingegeben. Bitte erneut versuchen.")

woerter_zaehlen()
