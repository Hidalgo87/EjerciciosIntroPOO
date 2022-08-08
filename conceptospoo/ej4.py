import math


class Punto:

    def __init__(self, coordenada_x: int, coordenada_y: int):
        self.x: int= coordenada_x
        self.y: int = coordenada_y

    def mostrar(self):
        print(f"({self.x}, {self.y})")

    def mover(self, dx: int, dy: int):
        self.x += dx
        self.y += dy

    def calcular_distancia(self, otro_punto):
        c1 = self.y - otro_punto.y
        c2 = self.x - otro_punto.x
        distancia = math.sqrt(c1**2 + c2**2)
        return distancia
# Cree una clase Rectángulo la cual contiene dos atributos de instancia
# que representan los puntos que definen sus esquinas.
# Agregue métodos a la clase Rectángulo para calcular su perímetro,
# calcular su área e indicar si el rectángulo es un cuadrado.


class Rectangulo:

    def __init__(self, x1: int, y1: int):
        self.x1 = x1
        self.y1 = y1


