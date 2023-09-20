dic = {"a": 1, "b": 2, "c": 3, "d": 5}
print(dic)

# [1] Eliminar elementos con 'del'

del dic["b"]

print(dic)

# [2] Eliminar con metodo pop

valor = dic.pop("a")

# Retorna el valor y lo borra del dic
print(valor)
print(dic)

# [3] Borrar todos los elementos
dic.clear()
print(dic)
