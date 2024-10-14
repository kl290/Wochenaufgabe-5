print("Durchschnittsberechner")

while True:
    try:
        eingabe = input("Bitte gib die Zahlen ein, getrennt durch Leerzeichen: ")

        zahlen_liste = list(map(float, eingabe.split()))

        if not zahlen_liste:
            print("Es wurden keine Zahlen eingegeben. Bitte versuche es erneut.")
            continue

        durchschnitt = sum(zahlen_liste) / len(zahlen_liste)

        print(f"Der Durchschnitt der eingegebenen Zahlen ist: {durchschnitt}")
        break

    except ValueError:
        print("Fehler: Du hast einen Buchstaben oder ungültige Zeichen eingegeben. Bitte gib nur Zahlen ein, ", end= "")
        print("getrennt durch Leerzeichen.")
