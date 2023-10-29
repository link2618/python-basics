# Unpacking - desempaquetado
valores = 1, 2, 3
print(valores)
print(type(valores))

valor1, valor2, valor3 = 1, 2, 3
print(valor1, valor2, valor3)

valor1, _, valor3 = 1, 2, 3
print(valor1, valor3)

valor1, valor2, *valor3 = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(valor1, valor2, valor3)

valor1, valor2, *valor3, valor4, valor5 = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(valor1, valor2, valor3, valor4, valor5)
print(type(valor3))

valor1, valor2, *valor3, valor4, valor5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(valor1, valor2, valor3, valor4, valor5)
print(type(valor3))

def regresa_varios_datos():
    return (1, 2, 3)

valor1, valor2, valor3 = regresa_varios_datos()
print(valor1, valor2, valor3)

valor1, *valores_restantes = regresa_varios_datos()
print(valor1, valores_restantes)

# help(str.partition)
hora, _, minutos = '17:20'.partition(':')
# print(type(variable))
print(hora, minutos)

# * desempaquetar
numeros = [1, 2, 3]
print(numeros)
print(*numeros)
print(*numeros, sep=' - ')

# Desempaquetando al momento de pasar un parámetro a una función
def sumar(a, b, c):
    print(f'Resultado suma: {a + b + c}')

sumar(*numeros)

# Extraer algunas partes de una lista
mi_lista = [1, 2, 3, 4, 5, 6]
a, *b, c, d = mi_lista
print(a, b, c, d)

# Unir lista
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [lista1, lista2]
print(f'Lista de listas: {lista3}')
lista3 = [*lista1, *lista2]
print(f'Unir listas: {lista3}')

# Unir diccionarios
dic1 = {'A': 1, 'B': 2, 'C': 3}
dic2 = {'D': 4, 'E': 5}
dic3 = {**dic1, **dic2}
print(f'Unir diccionarios: {dic3}')

# Construir una lista a partir de un str
lista = [*'HolaMundo']
print(lista)
print(*lista, sep='')
