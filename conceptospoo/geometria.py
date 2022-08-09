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

# Cree una clase Circulo que tenga las propiedades centro y radio,
# las cuales se inicializan con parámetros en el constructor.
# Defina métodos en la clase para calcular el área,
# el perímetro e indicar si un punto pertenece al círculo o no.

class Circulo:

    def __init__(self, centro_x: int, centro_y: int, radio: int):
        self.cx: int = centro_x
        self.cy: int = centro_y
        self.radio: int = radio

    def calcular_area(self):
        area = (self.radio**2)*math.pi
        return area

    def calcular_perimetro(self):
        perimetro = 2*math.pi*self.radio
        return perimetro

    def comprobar_pertenece_circulo(self, punto_x: int, punto_y: int):


