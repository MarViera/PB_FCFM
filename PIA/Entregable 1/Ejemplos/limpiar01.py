import requests
import re

url = "https://swapi.dev/api/people/13"
response = requests.get(url)
data = response.json()
if data["species"] == []:
    especie = "humano"
else:
    response2 = requests.get(data["species"][0])
    data2 = response2.json()
    especie = data2["name"]

clean = {
    "nombre": data["name"].capitalize(),
    "altura": int(data["height"]),
    "peso": int(data["mass"]),
    "especie": especie
}

print(clean)
