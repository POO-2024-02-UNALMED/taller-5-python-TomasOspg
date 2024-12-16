class Ave(Animal):
    listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self.__colorPlumas = colorPlumas
        Ave.listado.append(self)

    def movimiento(self):
        return "volar"

    @staticmethod
    def cantidadAves():
        return len(Ave.listado)

    @staticmethod
    def crearHalcon(nombre, edad, genero):
        Ave.halcones += 1
        return Ave(nombre, edad, "montañas", genero, "café glorioso")

    @staticmethod
    def crearAguila(nombre, edad, genero):
        Ave.aguilas += 1
        return Ave(nombre, edad, "montañas", genero, "blanco y amarillo")

    def getColorPlumas(self):
        return self.__colorPlumas

    def setColorPlumas(self, colorPlumas):
        self.__colorPlumas = colorPlumas
