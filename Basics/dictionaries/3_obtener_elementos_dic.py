dic = {"a": 1, "b": 2, "c": 3}

# Obtener valor de la llave
valor = dic["c"]

# Saber si una llave se encuentra dentro del diccionaro
print("d" in dic)

# Obtener el valor de una llave con metodo
# get

valor = dic.get("c")
print(valor)

# Obtener un valor que no existe

print(dic.get("g", "La llave no existe ene el dic"))
