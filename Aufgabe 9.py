Zahl = int()
for Zahl in range(1,101):
    if Zahl % 3 == 0 and Zahl % 5 == 0:
        print("PingPong")
    elif Zahl % 3 == 0:
        print("Ping")
    elif Zahl % 5 == 0:
        print("Pong")
    else:
        print(Zahl)
if Zahl > 100:
    print ("ungültige Zahl")
elif Zahl < 1:
    print("ungültige Zeit")
