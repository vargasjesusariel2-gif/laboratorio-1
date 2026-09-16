import math
class MiPunto:
    def __init__(self, x=0.0, y=0.0):
        self.__x = float(x)
        self.__y = float(y)
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def distancia(self, otro_punto):
        dx = self.__x - otro_punto.getX()
        dy = self.__y - otro_punto.getY()
        return math.sqrt(dx ** 2 + dy ** 2)
    def distancia_xy(self, x2, y2):
        dx = self.__x - x2
        dy = self.__y - y2
        return math.sqrt(dx ** 2 + dy ** 2)
p1 = MiPunto()
p2 = MiPunto(10, 30.5)
d1 = p1.distancia(p2)
print("Punto 1:", p1.getX(), ",", p1.getY())
print("Punto 2:", p2.getX(), ",", p2.getY())
print("La distancia entre p1 y p2 es:", d1)
