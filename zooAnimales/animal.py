from Mamifero import Mamifero
from Ave import Ave
from Pez import Pez
from Anfibio import Anfibio
from Reptil import Reptil

class Animal:
    total_animales = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, zona=None):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.zona = zona
        Animal.total_animales += 1

    def movimiento(self):
        return "desplazarse"

    @staticmethod
    def total_por_tipo():
        mamiferos = len(Mamifero.listado)
        aves = len(Ave.listado)
        reptiles = len(Reptil.listado)
        peces = len(Pez.listado)
        anfibios = len(Anfibio.listado)
        return f"Mamíferos: {mamiferos}\nAves: {aves}\nReptiles: {reptiles}\nPeces: {peces}\nAnfibios: {anfibios}"

    def __str__(self):
        if self.zona:
            return (f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} "
                    f"y mi género es {self.genero}, la zona en la que me ubico es {self.zona.nombre}, en el {self.zona.zoo.nombre}.")
        else:
            return (f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} "
                    f"y mi género es {self.genero}.")