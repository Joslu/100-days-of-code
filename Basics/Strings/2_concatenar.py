# RECUERDA! Los strings en python son inmutables

nombre = "Jose Luis"
apellido = "Cruz"

nombre_completo = nombre + " " + apellido

new_nombre_completo = "Mr. %s %s" % (nombre, apellido)

print(new_nombre_completo)
