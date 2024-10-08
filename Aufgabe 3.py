print("Rechner")
rechenart = str(input("Welche Rechenart möchtest du benutzen:"))
zahl1 = int(input("Gebe die erste zahl ein:"))
zahl2 = int(input("Gebe die zweite zahl ein:"))
if rechenart == "+" :
    print(f"{zahl1} {rechenart} {zahl2} = {zahl1+zahl2}")
elif rechenart == "-" :
    print(f"{zahl1} {rechenart} {zahl2} = {zahl1-zahl2}")
elif rechenart == "*" :
    print(f"{zahl1} {rechenart} {zahl2} = {zahl1*zahl2}")
elif rechenart == "/" :
    print(f"{zahl1} {rechenart} {zahl2} = {zahl1/zahl2}")
else:
    print("Kein gültiger Operator")