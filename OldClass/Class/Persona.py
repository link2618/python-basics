class Persona:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    def __del__(self):
        print(f'Persona: {self.__nombre} {self.__apellido}')

    def desplegar(self):
        print(f'Nombre: {self.__nombre}, Edad: {self.__edad}')


if __name__ == '__main__':
    print('Prueba el local'.center(50, '-'))

    persona1 = Persona('Juan', 'Perez', 28)
    persona1.desplegar()
    persona1.nombre = 'Juan Carlos'
    persona1.desplegar()
