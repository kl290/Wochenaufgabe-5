print("Willkommen zum Zahlenraten")
import random
Zufallszahl = random.randint(1,100)
geraten = False
while not geraten:
    try:
        tipp = int(input("Rate eine Zahl zwischen 1 und 100: "))
        if tipp < 1 or tipp > 100:
            print("Die Zahl muss zwischen 1 und 100 liegen.")
            continue
        if tipp < Zufallszahl :
            print("Zu niedrig!")
            continue
        elif tipp > Zufallszahl :
            print("Zu hoch!")
            continue
        else:
            print("Glückwunsch! Du hast die Zahl erraten.")
        geraten = True
    except ValueError :
        print("Bitte gib eine Zahl zwischen 1 und 100 ein!")
