import json

with open("lesson4_Übung_Textfile.txt","r") as output_file:
    output_data = json.loads(output_file.read())

while True:
    conv = input("Umrechnung wählen (ftc = Fahrenheit zu Celsius, ctml = cups zu ml, ptg = Pfund zu Gramm): ")
    if conv == "ftc":
        zahl1 = float(input("Geben Sie die umzurechnende Zahl ein: "))
        ftc = (zahl1 - 32)/1.8
        solution = "{:.2f} ° Fahrenheit ist {:.2f} ° Celsius".format(zahl1, ftc)
        print(solution)
        output_data.append(solution)
    elif conv == "ctml":
        zahl1 = float(input("Geben Sie die umzurechnende Zahl ein: "))
        ctml = zahl1 * 250
        solution = "{:.2f} Cups sind {:.2f} Milliliter".format(zahl1, ctml)
        print(solution)
        output_data.append(solution)
    elif conv == "ptg":
        zahl1 = float(input("Geben Sie die umzurechnende Zahl ein: "))
        ptg = zahl1 * 453.592
        solution = "{:.2f} Pfund sind {:.2f} Gramm".format(zahl1, ptg)
        print(solution)
        output_data.append(solution)
    else:
        print("Falsche Eingabe für Umrechnung.")
    nochmal = input("Wollen Sie noch etwas umrechnen? (J/n): ")
    if nochmal == "n":
        break

with open("lesson4_Übung_Textfile.txt", "w") as output_file:
    output_file.write(json.dumps(output_data))