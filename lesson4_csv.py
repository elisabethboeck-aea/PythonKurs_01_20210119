with open("lesson4.csv", "r") as csv_file:
    csv_data = csv_file.read().splitlines()

    for row in csv_data:
        row_data = row.split(",")
        print(f"{row_data[0]} is {row_data[1]} years old and {row_data[2]}.") # runde klammer für Funktionen, als index für eine Liste eckige Klammern, geschwungene Klammern wird hier von der Syntax gebraucht

# so können die einzelnen Daten aus der Datenliste gelesen werden. Das geht aus verschiedenen Listendateien wie csv, xml, json etc ausgelesen werden
