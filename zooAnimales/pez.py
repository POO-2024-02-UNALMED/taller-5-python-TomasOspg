class Pez(Animal):
    listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self.__colorEscamas = colorEscamas
        self.__cantidadAletas = cantidadAletas
        Pez.listado.append(self)

    def movimiento(self):
        return "nadar"

    @staticmethod
    def cantidadPeces():
        return len(Pez.listado)

    @staticmethod
    def crearSalmon(nombre, edad, genero):
        Pez.salmones += 1
        return Pez(nombre, edad, "océano", genero, "rojo", 6)

    @staticmethod
    def crearBacalao(nombre, edad, genero):
        Pez.bacalaos += 1
        return Pez(nombre, edad, "océano", genero, "gris", 6)

    def getColorEscamas(self):
        return self.__colorEscamas

    def setColorEscamas(self, colorEscamas):
        self.__colorEscamas = colorEscamas

    def getCantidadAletas(self):
        return self.__cantidadAletas

    def setCantidadAletas(self, cantidadAletas):
        self.__cantidadAletas = cantidadAletas