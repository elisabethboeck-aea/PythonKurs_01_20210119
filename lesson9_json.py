import json

# Einfache Variante mit lokal gespeichertem json file
with open("example_2.json") as file:
    data = json.load(file)

print(data["quiz"]["sport"]["q1"]["answer"])


