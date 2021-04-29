while True:
    conv = input("Umrechnung wählen (ftc = Fahrenheit zu Celsius, ctml = cups zu ml, ptg = Pfund zu Gramm): ")
    if conv == "ftc":
        zahl1 = int(input("Geben Sie die umzurechnende Zahl ein: "))
        print((zahl1 - 32)/1.8)
    elif conv == "ctml":
        zahl1 = int(input("Geben Sie die umzurechnende Zahl ein: "))
        print(zahl1 * 250)
    elif conv == "ptg":
        zahl1 = int(input("Geben Sie die umzurechnende Zahl ein: "))
        print(zahl1 * 453.592)
    else:
        print("Falsche Eingabe für Umrechnung.")
    nochmal = input("Wollen Sie noch etwas umrechnen? (ja/nein): ")
    if nochmal == "nein":
        break

