import matplotlib.pyplot as plt
import numpy as np
import csv

# years = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

# Endenergieverbrauch einlesen
with open("lesson12_Übung_Endenergieverbrauch_AUT_2005-2019.csv", "r") as eev:
    reader = csv.reader(eev, delimiter=";")
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    years = []

    values_eev = {
        'Landwirtschaft': [],
        'Industrie': [],
        'Dienstleistungen': [],
        'Verkehr': [],
        'Haushalte': []
    }

    for row in reader:
        year = int(row[0])
        years.append(year)

        values_eev['Landwirtschaft'].append(float(row[1]))
        values_eev['Industrie'].append(float(row[2]))
        values_eev['Dienstleistungen'].append(float(row[3]))
        values_eev['Verkehr'].append(float(row[4]))
        values_eev['Haushalte'].append(float(row[5]))


print(years)
print(values_eev)

#values_eev = {x:[v for v in y[0]] for x, y in values_eev.items()}

fig, ax = plt.subplots()
ax.stackplot(years, values_eev.values(), labels=values_eev.keys())
ax.legend(loc="upper left")
ax.set_title("Endenergieverbrauch je Verbrauchssektor")
ax.set_xlabel("Jahr")
ax.set_ylabel("Endenergieverbrauch [PJ]")

plt.show()