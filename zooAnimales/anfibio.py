class Anfibio(Animal):
    listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self.__colorPiel = colorPiel
        self.__venenoso = venenoso
        Anfibio.listado.append(self)

    def movimiento(self):
        return "saltar"

    @staticmethod
    def cantidadAnfibios():
        return len(Anfibio.listado)

    @staticmethod
    def crearRana(nombre, edad, genero):
        Anfibio.ranas += 1
        return Anfibio(nombre, edad, "selva", genero, "rojo", True)

    @staticmethod
    def crearSalamandra(nombre, edad, genero):
        Anfibio.salamandras += 1
        return Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)

    def getColorPiel(self):
        return self.__colorPiel

    def setColorPiel(self, colorPiel):
        self.__colorPiel = colorPiel

    def isVenenoso(self):
        return self.__venenoso

    def setVenenoso(self, venenoso):
        self.__venenoso = venenoso

