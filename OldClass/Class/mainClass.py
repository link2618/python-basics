from OldClass.Class.Persona import Persona

persona1 = Persona('Juan', 'Perez', 28)
persona1.desplegar()
persona1.nombre = 'Juan Carlos'
persona1.desplegar()

persona2 = Persona('Karla', 'Gomez', 30)
persona2.desplegar()

print('Eliminación objetos'.center(30, '-'))
del persona1
del persona2