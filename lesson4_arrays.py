# einfache datentypen int, String, Float, ...
example_int = 5

# arrays / Listen:
example_list = [3, 77, 43, 12, 3, 8]
print(example_list[3])

string_list = ["Golf", "Football", "Skating", "Baseball"]
print(string_list)

mixed_list = [55, "markus", False, "programmer", 3.54]

print(example_list)
example_list.sort()
print(example_list)

# mixed_list.sort() geht nicht, weil er mit den datentypen nichts anfangen kann

for item in mixed_list:
    print(item)
