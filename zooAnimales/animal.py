class Animal:
    totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero, zona=None):
        self.__nombre = nombre
        self.__edad = edad
        self.__habitat = habitat
        self.__genero = genero
        self.__zona = zona
        Animal.totalAnimales += 1

    def movimiento(self):
        return "desplazarse"

    def totalPorTipo():
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.pez import Pez
        from zooAnimales.ave import Ave
        from zooAnimales.reptil import Reptil
        return (f"Mamíferos: {len(Mamifero.listado)}\n"
                f"Aves: {len(Ave.listado)}\n"
                f"Reptiles: {len(Reptil.listado)}\n"
                f"Peces: {len(Pez.listado)}\n"
                f"Anfibios: {len(Anfibio.listado)}")

    def toString(self):
        base = f"Mi nombre es {self.__nombre}, tengo una edad de {self.__edad}, habito en {self.__habitat} y mi genero es {self.__genero}"
        if self.__zona:
            return (f"{base}, la zona en la que me ubico es {self.__zona.getNombre()}, en el {self.__zona.getZoo().getNombre()}.")
        return base

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getEdad(self):
        return self.__edad

    def setEdad(self, edad):
        self.__edad = edad

    def getHabitat(self):
        return self.__habitat

    def setHabitat(self, habitat):
        self.__habitat = habitat

    def getGenero(self):
        return self.__genero

    def setGenero(self, genero):
        self.__genero = genero

    def getZona(self):
        return self.__zona

    def setZona(self, zona):
        self.__zona = zona
