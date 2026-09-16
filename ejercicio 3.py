import math
class Vector3D:
    def __init__(self, a1=0.0, a2=0.0, a3=0.0):
        self.a1 = float(a1)
        self.a2 = float(a2)
        self.a3 = float(a3)
    def __add__(self, otro):
        return Vector3D(self.a1 + otro.a1, self.a2 + otro.a2, self.a3 + otro.a3)
    def __mul__(self, otro):
        if isinstance(otro, (int, float)):
            return Vector3D(self.a1 * otro, self.a2 * otro, self.a3 * otro)
        elif isinstance(otro, Vector3D):
            return self.a1 * otro.a1 + self.a2 * otro.a2 + self.a3 * otro.a3
    def __rmul__(self, otro):
        return self.__mul__(otro)
    def longitud(self):
        return math.sqrt(self.a1**2 + self.a2**2 + self.a3**2)
    def normal(self):
        l = self.longitud()
        if l == 0:
            return Vector3D(0, 0, 0)
        return Vector3D(self.a1 / l, self.a2 / l, self.a3 / l)
    def __xor__(self, otro):
        c1 = self.a2 * otro.a3 - self.a3 * otro.a2
        c2 = self.a3 * otro.a1 - self.a1 * otro.a3
        c3 = self.a1 * otro.a2 - self.a2 * otro.a1
        return Vector3D(c1, c2, c3)
    def __str__(self):
        return "(" + str(round(self.a1, 2)) + ", " + str(round(self.a2, 2)) + ", " + str(round(self.a3, 2)) + ")"
a = Vector3D(2, 4, 1)
b = Vector3D(1, -1, 3)
print("a =", a)
print("b =", b)
print("Suma (a + b) =", a + b)
print("Multiplicacion por escalar (3 * a) =", 3 * a)
print("Longitud |a| =", a.longitud())
print("Normal de a =", a.normal())
print("Producto escalar (a * b) =", a * b)
print("Producto vectorial (a ^ b) =", a ^ b)
