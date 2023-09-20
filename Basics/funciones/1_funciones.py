# Sin argumentos


def suma():
    numero_uno = int(input("Ingresa el primer número entero: "))
    numero_dos = int(input("Ingresa el segundo número: "))

    resultado = numero_uno + numero_dos
    print(resultado)


# Con argumentos


def suma_argumentos(numero_1, numero_2):
    resultado = numero_1 + numero_2
    print(resultado)


suma()
