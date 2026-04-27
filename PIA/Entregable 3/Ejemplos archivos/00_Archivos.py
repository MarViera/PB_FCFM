import json

# 1. Crear un diccionario
datos = {
    "nombre": "Pikachu",
    "tipo": "Eléctrico",
    "nivel": 25,
    "movimientos": ["Impactrueno", "Placaje", "Ataque Rápido"]
}

# 2. Guardarlo como archivo JSON
with open("data/pokemon.json", "w") as f:
    json.dump(datos, f, indent=4)

print("Archivo JSON guardado correctamente.")

# 3. Leer el archivo JSON
with open("data/pokemon.json", "r") as f:
    datos_cargados = json.load(f)

# 4. Mostrar el diccionario cargado
print("Diccionario cargado desde JSON:")
print(datos_cargados)

# 5. Verificar que realmente es un dict
print("Tipo de datos:", type(datos_cargados))
if datos == datos_cargados:
    print("Proceso de escrutra / lectura exitoso!")
