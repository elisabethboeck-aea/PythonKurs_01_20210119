from prettytable import PrettyTable

table = PrettyTable(["name", "ps"])

table.add_row(["Audi", 500])
table.add_row(["vw", 700])
table.add_row(["bmw", 44])
table.add_row(["porsche", 900])

print(table)
