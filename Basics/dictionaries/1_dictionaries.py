# El tipo de datos más interesante de python
# Son multables
# No se rigen por indices, los valores corresponden a llaves
# Todo valor una llave, cada llave un valor}
# Toda llave puede ser cualquier tipo de dato

diccionario1 = {}
diccionario2 = dict()

# { LLAVE : VALOR }

diccionario1 = {"Precio": 40.5}

diccionario2 = {"Precio": 20, "Descuento": True, "Producto": "Agua"}


# Obtener las llaves
diccionario1.keys()

# Obtenet los valores
diccionario2.values()

# Interar en un diccionario

for key, value in diccionario2.items():
    print(key, value)

# Comprehension en dicionarios

usuarios = ["Luis", "Jose", "Carlos", "Aldo"]

diccionario = {usuario: position + 1 for position, usuario in enumerate(usuarios)}

print(diccionario)
