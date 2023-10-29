# Profundizando en el tipo str
import math
from mi_clase import MiClase

# Concatenación automática en python
variable = 'Adios'
mensaje = 'Hola' 'Mundo' + variable
mensaje += 'Universidad' 'Python'
print(mensaje)

# Obtener ayuda
help(math.isnan)
help(str.capitalize)
help(math)
help(str)

# Documentacion
# help(MiClase)
print(MiClase.__doc__)
print(MiClase.__init__.__doc__)
print(MiClase.mi_metodo.__doc__)
print(MiClase.mi_metodo)
print(type(MiClase.mi_metodo))


mensaje1 = 'hola mundo'
mensaje2 = mensaje1.capitalize()
print(f'mensaje1: {mensaje1}, id: {hex(id(mensaje1))}')
print(f'mensaje2: {mensaje2}, id: {hex(id(mensaje2))}')
mensaje1 += 'adios'
print(f'mensaje1: {mensaje1}, id: {hex(id(mensaje1))}')


tupla_str = ('Hola', 'Mundo', 'Universidad', 'Python')
mensaje = ' '.join(tupla_str)
print(f'mensaje: {mensaje}')

lista_cursos = ['Java', 'Python', 'Angular', 'Spring']
mensaje = ', '.join(lista_cursos)
print(f'mensaje: {mensaje}')

cadena = 'HolaMundo'
mensaje = '.'.join(cadena)
print(f'mensaje: {mensaje}')

diccionario = {'nombre': 'Juan', 'apellido': 'Perez', 'edad': '18'}
llaves = ' '.join(diccionario.keys())
valores = ' '.join(diccionario.values())
print(f'llaves: {llaves}, type: {type(llaves)}')
print(f'valores: {valores}, type: {type(valores)}')


cursos = 'Java Python JavaScript Angular Spring Excel'
lista_cursos = cursos.split()
# print(f'lista cursos: {lista_cursos}')
# print(type(lista_cursos))

cursos_separados_coma = 'Java, Python, JavaScript, Angular, Spring, Excel'
lista_cursos = cursos_separados_coma.split(', ')
# print(f'lista cursos: {lista_cursos}')
# print(len(lista_cursos))

lista_cursos = cursos_separados_coma.split(', ', 3)
print(f'lista cursos: {lista_cursos}')
print(len(lista_cursos))


# Dar formato a un str
nombre = 'Juan'
edad = 28
mensaje_con_formato = 'Mi nombre es %s y tengo %d años' % (nombre, edad)
# print(mensaje_con_formato)

persona = ('Karla', 'Gomez', 5000.00)
# mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.2f'%persona
# print(mensaje_con_formato)
mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.2f'
print(mensaje_con_formato % persona)

nombre = 'Juan'
edad = 28
sueldo = 3000
mensaje = 'Nombre {} Edad {} Sueldo {:.2f}'.format(nombre, edad, sueldo)
# print(mensaje)

mensaje = 'Nombre {0} Edad {1} Sueldo {2:.2f}'.format(nombre, edad, sueldo)
# print(mensaje)

mensaje = 'Sueldo {2:.2f} Edad {1} Nombre {0}'.format(nombre, edad, sueldo)
print(mensaje)

mensaje = 'Nombre {n} Edad {e} Sueldo {s:.2f}'.format(n=nombre, e=edad, s=sueldo)
# print(mensaje)

diccionario = {'nombre': 'Ivan', 'edad': 35, 'sueldo': 8000.00}
mensaje = 'Nombre {dic[nombre]} Edad {dic[edad]} Sueldo {dic[sueldo]:.2f}'.format(dic=diccionario)
print(mensaje)

mensaje = f'Nombre {nombre} Edad {edad} Sueldo {sueldo:.2f}'
# print(mensaje)
# Método print
print(nombre, edad, sueldo, sep=', ')






# multiplicación str
resultado = 3*'Hola'
print(f'Resultado: {resultado}')

# multiplicación tuplas
resultado = 5*('Hola', 10)
print(f'Resultado: {resultado}')

# multiplicación listas
resultado = 10*[0]
print(f'Resultado: {resultado}, largo: {len(resultado)}')

# caracteres de escape
resultado = 'Hola \' Mundo'
print(f'Resultado: {resultado}')

resultado = 'Se va a eliminar el punto.\b\b\b'
print(f'Resultado: {resultado}')

# Caracter \
resultado = 'c:\\nuevo\\juan'
print(f'Resultado: {resultado}')

# raw string
resultado = r'Cadena con \n salto de línea'
print(f'Resultado: {resultado}')

resultado = R'c:\nuevo\juan'
print(f'Resultado: {resultado}')

# caracteres unicode
print('Hola\u0020Mundo')
print('Notación simple:', '\u0041')
print('Notación extendida:', '\U00000041')
print('Notación hexadecimal', '\x41')
print('Corazón:', '\u2665')
print('Cara sonriendo:', '\U0001f600')
print('Serpiente:', '\U0001F40D')

# Caracteres ascii
caracter = chr(65)
print('A mayúscula:', caracter)
caracter = chr(64)
print('Símbolo @:', caracter)
caracter = chr(97)
print('a minúscula:', caracter)

# caracteres bytes
caracteres_en_bytes = b'Hola Mundo'
print(caracteres_en_bytes)

mensaje = b'Universidad Python'
print(mensaje[1])
print(chr(mensaje[1]))

lista_caracteres = mensaje.split()
print(lista_caracteres)

# Convertir str a bytes
string = 'Programación con Python'
print('string original:', string)
bytes = string.encode('UTF-8')
print('bytes codificado:', bytes)
# Convertir bytes a str
string2 = bytes.decode('UTF-8')
print('string decodificado:', string2)
print(string == string2)


# Alinear cadenas

# center - Centrar un str
titulo = 'Sitio Web de GlobalMentoring.com.mx'
# print(len(titulo))
# print(titulo.center(10,'*'))
# print(len(titulo.center(50,'*')))
print(titulo.center(len(titulo)+10, '-'))

# ljust - alinea a la izquierda
# print(titulo.ljust(50,'*'))
print(titulo.ljust(len(titulo)+10, '-'))

# rjust - alinea a la derecha
# print(titulo.rjust(50,'*'))
print(titulo.rjust(len(titulo)+10, '-'))

# Reemplazar contenido en un str
print(titulo.replace(' ', '-'))

# Eliminar caracteres al inicio y final de un str - strip
titulo = ' *** GlobalMentoring.com.mx *** '
print('Cadena original:', titulo, len(titulo))
titulo = titulo.strip()
print('Cadena modificada:', titulo, len(titulo))
titulo = '***GlobalMentoring.com.mx***'.strip('*')
print('Cadena modificada:', titulo)
titulo = '***GlobalMentoring.com.mx***'.lstrip('*')
print('Cadena modificada:', titulo)
titulo = '***GlobalMentoring.com.mx***'.rstrip('*')
print('Cadena modificada:', titulo)

titulo = ' *** GlobalMentoring.com.mx *** '.strip().strip('*').strip()
print('Cadena modificada:', titulo)
