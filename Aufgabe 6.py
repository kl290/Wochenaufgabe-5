import random

def zahlen_raten():
    zufallszahl = random.randint(1, 100)
    geraten = False

    print("Ich habe eine Zahl zwischen 1 und 100 gewählt. Versuche, sie zu erraten!")

    while nicht_geraten(geraten):
        try:
            rateversuch = int(input("Gib deine Schätzung ein: "))

            if rateversuch < 1 or rateversuch > 100:
                print("Deine Zahl liegt außerhalb des gültigen Bereichs (1-100).")
            elif rateversuch < zufallszahl:
                print("Zu niedrig!")
            elif rateversuch > zufallszahl:
                print("Zu hoch!")
            else:
                print("Glückwunsch! Du hast die richtige Zahl erraten.")
                geraten = True
        except ValueError:
            print("Bitte gib eine gültige Zahl ein.")


def nicht_geraten(geraten):
    return not geraten
