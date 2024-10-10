print("Multiplikationstabelle ( kleines 1-mal-1 )")
while True :
    try :
     zahl = int(input(" Bitte gib eine Zahl ein: "))
     for i in range(1,11) :
         if range :
             ergebnis = zahl * i
             print(f"{zahl} * {i} = {ergebnis}")
         else :
             break
    except ValueError:
             print("Fehler: Bitte gib eine gültige Zahl ein!")
