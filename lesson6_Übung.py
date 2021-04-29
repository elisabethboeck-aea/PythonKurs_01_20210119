from lesson6_übung_functions import func_ftc, func_ctml, func_ptg

conv_dict = {"ftc": func_ftc, "ctml": func_ctml, "ptg": func_ptg}

while True:
    conv = input("Umrechnung wählen (ftc = Fahrenheit zu Celsius, ctml = cups zu ml, ptg = Pfund zu Gramm): ")
    if conv in conv_dict:
        conv_func = conv_dict[conv]
        zahl = int(input("Geben Sie die umzurechnende Zahl ein: "))
        print(conv_func(zahl))
    else:
        print("Falsche Eingabe für Umrechnung.")
    nochmal = input("Wollen Sie noch etwas umrechnen? (ja/nein): ")
    if nochmal == "nein":
        break