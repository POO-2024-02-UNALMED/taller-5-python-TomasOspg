from zooAnimales.animal import Animal

class Mamifero(Animal):
    listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self.__pelaje = pelaje
        self.__patas = patas
        Mamifero.listado.append(self)

    @staticmethod
    def cantidadMamiferos():
        return len(Mamifero.listado)

    @staticmethod
    def crearCaballo(nombre, edad, genero):
        Mamifero.caballos += 1
        return Mamifero(nombre, edad, "pradera", genero, True, 4)

    @staticmethod
    def crearLeon(nombre, edad, genero):
        Mamifero.leones += 1
        return Mamifero(nombre, edad, "selva", genero, True, 4)

    def getPelaje(self):
        return self.__pelaje

    def setPelaje(self, pelaje):
        self.__pelaje = pelaje

    def isPelaje(self):
        return self.__pelaje    

    def getPatas(self):
        return self.__patas

    def setPatas(self, patas):
        self.__patas = patas