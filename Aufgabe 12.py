def ist_palindrom(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]


while True:
    eingabe = input("Bitte geben Sie ein Wort ein: ")

    if not eingabe:
        print("Fehler: Die Eingabe darf nicht leer sein. Bitte versuchen Sie es erneut.")
        continue

    try:
        int(eingabe)
        print("Fehler: Die Eingabe darf keine Zahlen enthalten. Bitte geben Sie nur Buchstaben ein.")
        continue
    except ValueError:
        break

if ist_palindrom(eingabe):
    print(f'"{eingabe}" ist ein Palindrom.')
else:
    print(f'"{eingabe}" ist kein Palindrom.')
