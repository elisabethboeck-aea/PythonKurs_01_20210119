# API files über laufend aktualisierte Daten direkt aus dem Internet laden, ohne file lokal zu speichern
# daten von https://openweathermap.org/

import json
from urllib.request import urlopen

api_key = "6f7a58b8c90c384bed33b0dc0c5ea70b"
response = urlopen("http://api.openweathermap.org/data/2.5/weather?q=Vienna&appid=" + api_key).read()
data = json.loads(response) # Um Codierung hinzuzufügen: response.decode('utf-8')
print(data)

print(data["weather"])
print(data["weather"][0])
print(data["weather"][0]["description"])
print(data["main"]["temp"])

#Hausübung: für unsere Arbeit relevante API streams finden (z.b. data.gv.at, ENTSO-E)