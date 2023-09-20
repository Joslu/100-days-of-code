## Metodos importandes de listas
# Split
# Join

my_string = "Ruby Python C C++"

my_string_with_underscore = "Ruby_Python_C_C++"

# Split: Generar y retornar un nuevo listado a traves de un string
# Por default divide por espacio
# Para separar por otros caracteres agregar argumento

listado_lenguajes = my_string.split()
listado_lenguajes_2 = my_string_with_underscore.split("_")

print(f"This is the list 1 {listado_lenguajes}")
print(f"This is the list 2 {listado_lenguajes_2}")


#################### Para hacer lo inverso

# Usar metodo join para unir mediante un caracter

my_list = ["Ruby", "Python", "C", "C++"]

my_join = "-".join(my_list)

print(f"This is my new string: {my_join}")
