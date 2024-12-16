class Zoologico:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas = []

    def agregar_zona(self, zona):
        self.zonas.append(zona)

    def cantidad_total_animales(self):
        return sum(zona.cantidad_animales() for zona in self.zonas)