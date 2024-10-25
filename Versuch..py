def ist_palindrom(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]


while True:
    eingabe = input("Bitte geben Sie ein Wort ein: ")

    if not eingabe:
        print("Fehler: Das Programm prüft nur bei Eingabe auf Palindrom. Bitte versuchen Sie es erneut.")
        continue

    if ist_palindrom(eingabe):
        print(f'"{eingabe}" ist ein Palindrom.')
    else:
        print(f'"{eingabe}" ist kein Palindrom.')