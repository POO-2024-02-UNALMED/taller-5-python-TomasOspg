from zooAnimales.mamifero import Mamifero
from zooAnimales.ave import Ave
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil
from zooAnimales.anfibio import Anfibio

class Animal:
    totalAnimales = 0

    def __init__(self, nombre="", edad=0, habitat="", genero=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__habitat = habitat
        self.__genero = genero
        self.__zona = None
        Animal.totalAnimales += 1

    def movimiento(self):
        return "desplazarse"

    def __str__(self):
        if self.__zona:
            return (f"Mi nombre es {self.__nombre}, tengo una edad de {self.__edad}, habito en {self.__habitat} "
                    f"y mi género es {self.__genero}, la zona en la que me ubico es {self.__zona.getNombre()}, "
                    f"en el {self.__zona.getZoo().getNombre()}.")
        else:
            return (f"Mi nombre es {self.__nombre}, tengo una edad de {self.__edad}, habito en {self.__habitat} "
                    f"y mi género es {self.__genero}.")

    @staticmethod
    def totalPorTipo():
        return (f"Mamíferos: {Mamifero.cantidadMamiferos()}\n"
                f"Aves: {Ave.cantidadAves()}\n"
                f"Reptiles: {Reptil.cantidadReptiles()}\n"
                f"Peces: {Pez.cantidadPeces()}\n"
                f"Anfibios: {Anfibio.cantidadAnfibios()}")

    # Getters y Setters
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
