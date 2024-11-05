def woerter_zaehlen():
    satz = input("Bitte einen Text eingeben: ")
    anzahl_zahlen = sum(1 for wort in satz.split() if wort.isdigit())
    woerter = satz.split()
    haeufigkeit = {}

    for wort in woerter:

        wort = wort.strip(".,!?;:()\"")

        if wort:
            wort = wort.lower()
            if wort in haeufigkeit:
                haeufigkeit[wort] += 1
            else:
                haeufigkeit[wort] = 1

    print(f"Der Text enthält {len(woerter)} Wörter, und {anzahl_zahlen} Zahlen insgesamt.")
    print("Häufigkeit der Wörter und Zahlen:", haeufigkeit)


(woerter_zaehlen())
