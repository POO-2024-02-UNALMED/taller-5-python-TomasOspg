from zooAnimales.animal import Animal

class Ave(Animal):
    listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre="", edad=0, habitat="", genero="", colorPlumas=""):
        super().__init__(nombre, edad, habitat, genero)
        self.__colorPlumas = colorPlumas
        Ave.listado.append(self)

    def movimiento(self):
        return "volar"

    @staticmethod
    def crearHalcon(nombre, edad, genero):
        Ave.halcones += 1
        return Ave(nombre, edad, "montañas", genero, "café glorioso")

    @staticmethod
    def crearAguila(nombre, edad, genero):
        Ave.aguilas += 1
        return Ave(nombre, edad, "montañas", genero, "blanco y amarillo")

    @staticmethod
    def cantidadAves():
        return len(Ave.listado)