def mi_funcion(nombre, apellido):
    print('saludos desde mi función')
    print(f'Nombre: {nombre}, Apellido: {apellido}')


mi_funcion('Juan', 'Perez')
mi_funcion('Karla', 'Lara')


def sumar(a=0, b=0) -> int:
    return a + b


resultado = sumar(5, 3)
print(f'Resultado sumar: {resultado}')


def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)


listarNombres('Juan', 'Karla', 'María', 'Ernesto')
listarNombres('Laura', 'Carlos')


def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')


listarTerminos(IDE='Integrated Developement Environment', PK='Primary Key')
listarTerminos(DBMS='Database Management System')


def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)


nombres = ['Juan', 'Karla', 'Guillermo']
desplegarNombres(nombres)
desplegarNombres('Carlos')
desplegarNombres((8, 9))
desplegarNombres([10, 11])


# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2
# 5! = 5 * 4 * 6
# 5! = 5 * 24
# 5! = 120
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)


numero = 5
resultado = factorial(numero)
print(f'El factorial de {numero} es {resultado}')
