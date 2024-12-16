class Zoologico:
    def __init__(self, nombre, ubicacion):
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__zonas = []

    def agregarZonas(self, zona):
        self.__zonas.append(zona)

    def cantidadTotalAnimales(self):
        return sum(zona.cantidadAnimales() for zona in self.__zonas)

    # Getters y Setters
    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getUbicacion(self):
        return self.__ubicacion

    def setUbicacion(self, ubicacion):
        self.__ubicacion = ubicacion

    def getZona(self):
        return self.__zonas

    def setZona(self, zonas):
        self.__zonas = zonas