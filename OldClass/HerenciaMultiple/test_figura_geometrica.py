from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('Creación Objeto cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(5, 'rojo')
print(f'Cálculo área cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)

print('Creación Objeto rectángulo'.center(50, '-'))
rectangulo1 = Rectangulo(3, 8, 'verde')
print(f'Cálculo área rectángulo: {rectangulo1.calcular_area()}')
print(rectangulo1)

# MRO - Method Resolution Order
print(Cuadrado.mro())
