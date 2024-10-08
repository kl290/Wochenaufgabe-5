import random
print("Willkommen zum Zahlen raten!")
print("Gesucht wird eine Zahl zwischen 1 und 100.")
Zahl = random.randint(1,100)
while True:
    versuch = int(input("Rate meine Zahl:"))
    if versuch == Zahl:
        print("Erraten!")
        break
    if versuch < Zahl : print("zu klein!")
    if versuch > Zahl : print("zu groß!")


