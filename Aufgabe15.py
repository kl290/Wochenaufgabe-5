def woerter_zaehlen():
    satz = input("Bitte einen Satz eingeben: ")
    woerter = satz.split()
    haeufigkeit = {}

    for wort in woerter:
        if not wort.isdigit():
            if wort in haeufigkeit:
                haeufigkeit[wort] += 1
            else:
                haeufigkeit[wort] = 1
        else:
            print("Fehler: Der Satz darf keine Zahlen enthalten.")
            return

    print(f"Der Satz enthält {len(woerter)} Wörter.")
    print(haeufigkeit)


woerter_zaehlen()