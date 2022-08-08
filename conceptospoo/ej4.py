import math


class Punto:

    def __init__(self, coordenada_x: int, coordenada_y: int):
        self.x: int = coordenada_x
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

    def __init__(self, coordenada_x: int, coordenada_y: int):
        self.x: int = coordenada_x
        self.y: int = coordenada_y

    def calcular_perimetro(self, otro_punto):
        c1 = self.y - otro_punto.y
        c2 = self.x - otro_punto.x
        perimetro = ((math.fabs(c1))*2)+((math.fabs(c2))*2)
        return perimetro

    def calcular_area(self, otro_punto):
        c1 = self.y - otro_punto.y
        c2 = self.x - otro_punto.x
        area = (c1*c2)
        return area

    def comprobar_cuadrado(self, otro_punto):
        c1 = self.y - otro_punto.y
        c2 = self.x - otro_punto.x
        if c1 == c2:
            print("El rectangulo es un cuadrado")
        else:
            print("El rectangulo NO es un cuadrado")
