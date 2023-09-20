elementos = {}


# Crea la llave, ya que no existe
elementos["nombre"] = "Luis"
elementos[(1, 2, 3)] = "La llave es una tupla"

print(elementos)

# Actualiza la llave, ya que si existe
elementos["nombre"] = "Jose"

print(elementos)
