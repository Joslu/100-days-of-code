# Tuplas soy mur parecidas a las listas
# Pero las tuplas son inmutables
# No podemos añadir, modificar elementos

my_tupla = ("Gracias", "Por favor", "Con gusto")


# Acces to element
print(my_tupla[0])


# No podemos hacer esto
# tuple' object does not support item assignment

# my_tupla[2] = "ajjaa"


# Crear una tupla desde una lsta

lista_to_convert = ["Mexico", "Peru", "Colombia"]

nueva_tupla = tuple(lista_to_convert)
print(type(nueva_tupla))
