list_courses = ["Python", "Flask", "PLC", "C", "Django", "SQL", "JAVA"]


# Sub Listas
# [start:] -> Obtenemos los ultimos elementos de la lista
print(list_courses[2:])
# [:end] -> Obtenemos los primeros elementos de la lista
print(list_courses[:3])
# [start:end:skip] -> Obtenemos elemtos, haciendo un salt
print(list_courses[1::2])


# Metodos listas

# Ordenar
# Con sort ordena ascendente, para hacer deforma descendente usar reverse = True
lista_to_sort = [4, 0, 50, 12, 304, 5, 3, 9, 135]
lista_to_sort.sort()
print(lista_to_sort)

# Get max number
print(lista_to_sort[-1])
print(max(lista_to_sort))

# Ger mini nummber
print(lista_to_sort[0])
print(min(lista_to_sort))

# Check if some item is inside our list
print(10 in lista_to_sort)

print(343 not in lista_to_sort)
