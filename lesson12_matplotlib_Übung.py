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
    values_lw, values_ind, values_dl, values_mob, values_res = [], [], [], [], []

    for row in reader:
        year = int(row[0])
        years.append(year)
        value_lw = float(row[1])
        values_lw.append(value_lw)
        value_ind = float(row[2])
        values_ind.append(value_ind)
        value_dl = float(row[3])
        values_dl.append(value_dl)
        value_mob = float(row[4])
        values_mob.append(value_mob)
        value_res = float(row[5])
        values_res.append(value_res)

values_eev = {
    'Landwirtschaft': values_lw,
    'Industrie': values_ind,
    'Dienstleistungen': values_dl,
    'Verkehr': values_mob,
    'Haushalte': values_res
}

print(years)
print(values_eev)

fig, ax = plt.subplots()
ax.stackplot(years, values_eev.values(), labels=values_eev.keys())
ax.legend(loc="upper left")
ax.set_title("Endenergieverbrauch je Verbrauchssektor")
ax.set_xlabel("Jahr")
ax.set_ylabel("Endenergieverbrauch [PJ]")

plt.show()


